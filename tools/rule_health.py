#!/usr/bin/env python3
"""Which rules ever fire? Rule health, from the family's own git history.

Rules only accumulate: every escape found so far became a new R/G/U rule, and
nothing records which rules have ever caught anything. A rule that has never
fired is either guarding something that never happens or blind to what it was
written for; either way it is a candidate for review, and the only way to
know which is to count.

The count is retrospective and uses no logs: every historical version of
every registry and seed batch in the four repositories is re-validated with
each repository's CURRENT validator, and each rule code is tallied by the
number of distinct file versions it fired on. It therefore answers "would
today's rules have caught something in what was actually written", not
"what did CI say at the time".

What it cannot see, stated with the numbers: versions that never reached a
pushed commit (a violation fixed before the first push leaves no trace), and
files that are examples or templates, which are written to pass.

Usage:
    python tools/rule_health.py --root /path/with/the/four/clones [--json out.json]

Exit 0 always (a report, not a gate); 2 if a clone or validator is missing.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
import tempfile

FAMILY = {
    # validator family: (repo holding it, validator, rule-code prefix)
    "Mizan": ("Mizan", "tools/mizan_validate.py", "R"),
    "Kiyas": ("Kiyas", "tools/kiyas_validate.py", "G"),
    "ux-mizan": ("ux-mizan", "skill/ux-mizan/scripts/ux_validate.py", "U"),
}
# Files are found by name in every repository and handed to each validator in
# turn; the first that accepts the file (valid JSON out, not exit 2) scores it.
# A family's product registry is often a MIZAN registry, so repo != validator.
GLOBS = ["*registry*.yaml", "*kiyas-seed*.yaml"]
REPOS = ["Mizan", "Kiyas", "Iskele", "ux-mizan"]
SKIP = re.compile(r"(^|/)(templates?|schemas?)/|\.example\.|/fixtures?/")


def git(repo_dir: str, *args: str) -> str:
    return subprocess.run(["git", "-C", repo_dir, *args], capture_output=True,
                          text=True, check=True).stdout


def defined_codes(validator: str, prefix: str) -> set[str]:
    src = open(validator, encoding="utf-8").read()
    return set(re.findall(r'"(%s\d+)[_"]' % prefix, src))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--json")
    a = ap.parse_args()

    validators = {}
    for fam, (repo, vpath, prefix) in FAMILY.items():
        v = os.path.join(a.root, repo, vpath)
        if not os.path.exists(v):
            print(f"ERROR: {v} missing", file=sys.stderr)
            return 2
        validators[fam] = (v, os.path.join(a.root, repo), prefix)
    report = {fam: {"files": set(), "versions": 0, "fired": collections.Counter()}
              for fam in FAMILY}
    for repo in REPOS:
        rdir = os.path.join(a.root, repo)
        if not os.path.isdir(rdir):
            print(f"ERROR: clone {rdir} missing", file=sys.stderr)
            return 2
        paths = sorted({p for g in GLOBS for p in git(rdir, "log", "--all", "--format=",
                                                       "--name-only", "--", g).split()})
        seen = set()
        for p in (p for p in paths if not SKIP.search(p)):
            for sha in git(rdir, "log", "--all", "--format=%H", "--", p).split():
                try:
                    blob = git(rdir, "rev-parse", f"{sha}:{p}").strip()
                except subprocess.CalledProcessError:
                    continue  # deleted in this commit
                if blob in seen:
                    continue
                seen.add(blob)
                with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False,
                                                 encoding="utf-8") as fh:
                    fh.write(git(rdir, "show", blob))
                for fam, (v, vdir, _) in validators.items():
                    out = subprocess.run([sys.executable, v, "--format", "json", fh.name],
                                         capture_output=True, text=True, cwd=vdir)
                    try:
                        res = json.loads(out.stdout)
                    except json.JSONDecodeError:
                        continue  # not this family's file
                    r = report[fam]
                    r["files"].add(f"{repo}/{p}")
                    r["versions"] += 1
                    r["fired"].update({f["code"] for f in res.get("violations", [])
                                       + res.get("warnings", []) if f.get("code")})
                    break
                os.unlink(fh.name)
    for fam, r in report.items():
        v, _, prefix = validators[fam]
        defined = defined_codes(v, prefix)
        r["files"] = len(r["files"])
        r["never_fired"] = sorted(defined - set(r["fired"]), key=lambda c: int(c[1:]))
        r["fired"] = dict(sorted(r["fired"].items(), key=lambda kv: -kv[1]))

    # Pre-push blocks, exported by tools/rule_hits.py from each clone's hook
    # log. History cannot see these; they are the only record of a rule
    # actually stopping something.
    hits = collections.Counter()
    exports = 0
    for repo in REPOS:
        d = os.path.join(a.root, repo, "rule-hits")
        for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if name.endswith(".json"):
                data = json.load(open(os.path.join(d, name), encoding="utf-8"))
                hits.update(data.get("violations", {}))
                exports += 1
    report["pre_push"] = {"exports": exports, "violations": dict(hits.most_common())}

    lines = ["# Rule health", ""]
    for repo, r in report.items():
        if repo == "pre_push":
            continue
        lines.append(f"## {repo}: {r['versions']} historical versions of {r['files']} file(s)")
        if r["fired"]:
            lines.append("fired (versions): " + ", ".join(f"{k} {v}" for k, v in r["fired"].items()))
        lines.append(f"never fired ({len(r['never_fired'])}): " + (", ".join(r["never_fired"]) or "—"))
        lines.append("")
    pp = report["pre_push"]
    lines.append(f"## Pre-push blocks (hook logs, {pp['exports']} export(s))")
    lines.append(", ".join(f"{k} {v}" for k, v in pp["violations"].items()) or "none exported yet")
    lines.append("")
    lines.append("A never-fired rule is a question, not a verdict: guarding something "
                 "that never happens, or blind to it. Versions never pushed are invisible here.")
    text = "\n".join(lines)
    print(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        open(summary, "a", encoding="utf-8").write(text + "\n")
    if a.json:
        json.dump(report, open(a.json, "w"), indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
