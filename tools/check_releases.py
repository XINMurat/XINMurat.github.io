#!/usr/bin/env python3
"""The release table must say what the Releases pages say.

index.md carries a "Current releases" table in two languages. Each row links
to <repo>/releases/latest and prints a version beside it. The link was always
right -- GitHub resolves it -- but the printed number was typed by hand, and
nothing compared the two. This does: every row whose link ends in
/releases/latest must print the tag that GitHub reports as latest.

Rows that link to a fixed tag (/releases/tag/vX) are history and are checked
only for agreeing with their own link.

Usage:
    python tools/check_releases.py            # exit 1 on any mismatch
    GITHUB_TOKEN=... python tools/check_releases.py   # CI, avoids rate limits
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "index.md")

ROW = re.compile(
    r'<a href="https://github\.com/(?P<owner>[\w.-]+)/(?P<repo>[\w.-]+)/releases/'
    r'(?:latest|tag/(?P<tag>[^"]+))">[^<]*</a></td>\s*<td><strong>(?P<shown>[^<]+)</strong>')


def latest(owner: str, repo: str) -> str:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
        headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)["tag_name"]


def main() -> int:
    with io.open(PAGE, encoding="utf-8") as fh:
        text = fh.read()
    rows = list(ROW.finditer(text))
    if not rows:
        # A table the pattern no longer matches would otherwise pass forever.
        print("FAIL: no release rows found in index.md -- did the table's markup change?")
        return 1
    cache: dict[tuple[str, str], str] = {}
    bad = []
    for mt in rows:
        line = text.count("\n", 0, mt.start()) + 1
        shown = mt["shown"].strip()
        if mt["tag"]:
            want = mt["tag"]
        else:
            key = (mt["owner"], mt["repo"])
            if key not in cache:
                try:
                    cache[key] = latest(*key)
                except Exception as exc:  # network, 404, rate limit
                    bad.append(f"index.md:{line}: could not read {key[1]}'s latest release ({exc})")
                    continue
            want = cache[key]
        if shown != want:
            bad.append(f"index.md:{line}: {mt['repo']} shows {shown}, the release is {want}")
    if bad:
        print("FAIL: the release table disagrees with GitHub Releases:")
        for b in bad:
            print("  " + b)
        return 1
    print(f"ok  {len(rows)} release row(s) agree with GitHub Releases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
