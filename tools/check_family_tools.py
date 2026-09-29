#!/usr/bin/env python3
"""The four repositories must share one copy of their shared tools.

Each repository checks its own copies against tools/shared-tools.json, which
catches a tool edited alone. It cannot catch the manifest moving in one
repository only: that repository stays self-consistent and green. This page is
where the family is described as one thing, so this is where the four `main`
branches are compared -- manifests with each other, and every listed file
with the manifest, fetched as published.

A repository that has no manifest yet is reported, not failed: adoption lands
one pull request at a time, and a daily red that nobody can fix today is
noise.

Usage:
    python tools/check_family_tools.py     # exit 1 on disagreement
"""
from __future__ import annotations

import hashlib
import json
import sys
import urllib.error
import urllib.request

OWNER = "XINMurat"
REPOS = ["Mizan", "Kiyas", "Iskele", "ux-mizan"]
RAW = "https://raw.githubusercontent.com/%s/%s/main/%s"


def fetch(repo: str, path: str) -> bytes | None:
    try:
        with urllib.request.urlopen(RAW % (OWNER, repo, path), timeout=20) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise


def main() -> int:
    manifests = {}
    for repo in REPOS:
        raw = fetch(repo, "tools/shared-tools.json")
        if raw is None:
            print("note  %s: no tools/shared-tools.json on main yet" % repo)
            continue
        manifests[repo] = json.loads(raw)["files"]
    if len(manifests) < 2:
        print("ok  fewer than two repositories carry a manifest; nothing to compare")
        return 0

    bad = []
    ref_repo, ref = next(iter(manifests.items()))
    for repo, files in manifests.items():
        if files != ref:
            diff = sorted(k for k in set(files) | set(ref) if files.get(k) != ref.get(k))
            bad.append("%s's manifest differs from %s's on: %s" % (repo, ref_repo, ", ".join(diff)))
        for path, want in sorted(files.items()):
            body = fetch(repo, path)
            if body is None:
                bad.append("%s: %s listed but missing on main" % (repo, path))
            elif hashlib.sha256(body.replace(b"\r\n", b"\n")).hexdigest() != want:
                bad.append("%s: %s does not match its own manifest" % (repo, path))
    if bad:
        print("FAIL: the shared tools have drifted across the family:")
        for b in bad:
            print("  " + b)
        return 1
    print("ok  %d repositories share %d tool(s)" % (len(manifests), len(ref)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
