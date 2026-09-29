# xinmurat.github.io

The family's entry page: **[xinmurat.github.io](https://xinmurat.github.io/)**

Canonical description of four Claude skills that keep each other honest —
**İskele builds · Mizan weighs · Kıyas generates · ux-mizan measures
experience** — plus the handoff chain between them and the constants they
share.

The four repositories link here rather than each carrying its own copy of the
family description. One canonical source, four pointers: the alternative is
eight copies that go stale one at a time.

**English first, Turkish second, and the two are mirrors.** Every section exists
in both languages at the same depth; a row added to one is added to the other in
the same commit. A canonical description that says different things in two
languages is two descriptions, and the page had drifted that way before — the TR
half carried a handoff diagram, a constants table and a releases table that the
EN half did not.

The page ships its own layout (`_layouts/default.html`) rather than a gem theme:
four accent colours, two language panes and a dark mode are cheaper to own than
to override. The language toggle defaults to English, remembers a choice in
`localStorage`, and `#en` / `#tr` link straight to one.

| Skill | Verb | Repository | Docs |
|---|---|---|---|
| İskele | builds | [Iskele](https://github.com/XINMurat/Iskele) | [docs](https://xinmurat.github.io/Iskele/) |
| Mizan | weighs | [Mizan](https://github.com/XINMurat/Mizan) | [docs](https://xinmurat.github.io/Mizan/) |
| Kıyas | generates | [Kiyas](https://github.com/XINMurat/Kiyas) | [docs](https://xinmurat.github.io/Kiyas/) |
| ux-mizan | measures experience | [ux-mizan](https://github.com/XINMurat/ux-mizan) | [docs](https://xinmurat.github.io/ux-mizan/) |

The **Current releases** table in `index.md` is typed by hand, so CI checks it:
`tools/check_releases.py` compares every row that links to `/releases/latest`
with the tag GitHub reports, on every push and once a day — a release in one of
the four repositories changes the answer without touching this one.

The same daily run compares the four repositories' shared tools
(`tools/check_family_tools.py`): each repository checks its own copies against
`tools/shared-tools.json`, and this page checks that the four manifests — and
the files they list — still agree on `main`.

The daily run also reports **rule health** (`tools/rule_health.py`): every
historical version of every registry and seed batch in the four repositories
is re-validated with today's validators, and each rule is counted by how many
versions it fires on. A rule that has never fired is a question for review,
not a verdict. The first run's answer is itself a finding: across 19 pushed
versions of real registries no rule fires, because violations are fixed before
the push and leave no trace in git. History cannot tell a sleeping rule from a
working one; counting pre-push failures needs the hook or CI to record them.

Content is CC BY 4.0.
