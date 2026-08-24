# Prep-pack build scripts

The scripts that generated and patched the circulation pack in `mock exams/` on 2026-08-18. Kept because the pack now has a real build dependency: every practice test and every Trap Sheet card cites a `§` section of `CCA-F_Corpus_v1.html`. If the domain source files change, the corpus must be rebuilt or those citations drift.

Run from anywhere; the paths inside are absolute.

The pack is split into two folders and every script writes into the right one:

```
mock exams/Learning corpus/   Exam-Day-Guide, Concept-Atlas, Trap-Sheet, Corpus, One-Page-Sheet
mock exams/Mock tests/        README, Test-1..7, Test-MR, Dashboard
```

| Script | Produces | Reads |
|---|---|---|
| `build_corpus.py` | `Learning corpus/CCA-F_Corpus_v1.html` | `prep with quiz/CCA-Prep_Domain-1..5_v2.md` |
| `build_mr.py` | `Mock tests/Test-MR.html` | `wf_payload.json` |
| `build_onepager.py` | `Learning corpus/CCA-F_One-Page-Sheet_v1.html` | `wf_payload.json` |
| `patch_tests.py` | edits `Mock tests/Test-1..7.html` in place | — |
| `split_pack.py` | performs the flat → two-folder split and rewrites every cross-folder link | — |
| `check_links.py` | verifies every link and fragment across both folders | — |

Supporting modules:

- `md2blocks.py` — the markdown renderer. Guarded against non-advancing loops; it raises rather than hanging if it meets a construct it cannot place.
- `corpus_extras.py` — the hand-written student-facing corpus index page, plus `clean()`, which strips author-facing front matter (`Source:` / `Version:` / `Changelog:`), de-links files that are not shipped, and rewrites the one D3 note that was addressed to the question author.
- `wf_payload.json` — the authored content: 30 verified multiple-response items and the one-page sheet's blocks. Regenerating this needs the authoring workflow, not these scripts.

## Order

`patch_tests.py` is not idempotent for the pack bar (it skips if one is present) but the other three replacements match exact source strings and will simply report `MISSED` if already applied. Rebuild in this order if you rebuild at all:

```bash
python build_corpus.py && python build_mr.py && python build_onepager.py
```

Then re-run the pack-bar standardiser, because the builders emit their own bar and it must stay identical across all 15 HTML files.

`split_pack.py` is a one-time migration and has already run — re-running it on the split layout is a no-op, because the files are no longer at the root. Keep it as the record of how the links were rewritten.

## What to re-verify after any rebuild

Run `python check_links.py` first — it walks both folders and reports broken files, broken fragments, and unresolved citations in one pass. Then:

1. Every `§N.M` cited in `Test-*.html` and `CCA-F_Trap-Sheet_v1.html` resolves to an `id="s-N-M"` in the corpus. Last run: 479 distinct citations, 0 unresolved.
2. Cross-folder links use `%20`-encoded folder names (`../Learning%20corpus/`, `../Mock%20tests/`). The JS link builders inside the tests (`citeHref`, `studyLinks`) carry the prefix too — `check_links.py` skips template literals, so verify those in a browser.
3. No dead file links in the corpus — the source markdown links to sibling working files that are not shipped, and `clean()` is what neutralises them.
4. No author-facing content leaked: grep the corpus for `Changelog`, `Generator rule`, `EXAM-LOG`, `guide_en`, `SESSION-STATE`, `banlist`.
5. The one-page sheet still fits one side. Measure with its own `@media print` rules against 1062px (A4) and 996px (US Letter) usable height. Last run: 926px.
