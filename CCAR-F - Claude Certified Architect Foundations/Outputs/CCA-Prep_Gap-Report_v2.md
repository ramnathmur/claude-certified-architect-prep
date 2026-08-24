# CCA-F Prep Pack — Gap Remediation Report

**Folder:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\mock exams`
**Date:** 2026-08-18
**Supersedes:** `CCA-Prep_Gap-Report_v1.md` (the audit). This is what was done about it.

The folder went from 13 files to 16. Three are new; the other thirteen were edited in place, so no existing link or bookmark breaks.

---

## Part 1 — The nine gaps

| # | Gap | Status | What was done |
|---|---|---|---|
| 1 | Test explanations cite files that are not in the folder | **Fixed** | Built `CCA-F_Corpus_v1.html` — the five domain source files as one paged document, 73 numbered sections with `§`-anchored ids. Every `Source:` line in all eight tests is now a live link into it, and all 172 `§` marks on the Trap Sheet were linkified. **479 distinct section citations across the pack; 0 unresolved.** |
| 2 | Nothing routes a wrong answer to the page that fixes it | **Fixed** | Each domain card on every results page and on the dashboard now carries **Study this → Guide · Atlas · Traps · Corpus**, deep-linked to that domain. Domains below 70% are visually marked. The dashboard's weakest-domain and slowest-domain callouts carry the same links, with different advice attached to each. |
| 3 | No practice at multiple-response items | **Fixed** | Built `Test-MR.html` — 30 authored items, 2 or 3 correct of 5 or 6 options, domain-weighted 8/5/6/6/5. Enforces the select-N cap, scores all-or-nothing, explains why a partly-right answer scored zero, and exports to the dashboard. |
| 4 | No one-page printable cheat sheet | **Fixed** | Built `CCA-F_One-Page-Sheet_v1.html` — 5 domains, 19 hard rules, 10 confusable pairs, 8 escalation and enforcement rules, 7 exam-mechanics lines, out-of-scope list. |
| 5 | Practice scores have no stated meaning | **Fixed** | Added a **"What your score actually means"** card to the dashboard: what the linear scaling does and does not predict, why one test tells you little, why Hint-on scores do not count, and a three-band readiness bar. |
| 6 | The practice tests have no way back to the pack | **Fixed** | The shared pack bar is now on all 15 HTML files, verified byte-identical apart from the current-page marker. |
| 7 | The Trap Sheet never names the six scenarios | **Fixed** | Added a scenarios table to its setter's-toolkit page: what each scenario's stem typically shows you and which domains it leans on. |
| 8 | Out-of-scope content is never stated | **Fixed** | *Correction to the v1 report: the Exam Day Guide already carried this list — I missed it.* The real gap was that the README did not. All 16 exclusions are now a README section. |
| 9 | File names are inconsistent | **Not done, deliberately** | Renaming breaks links people may already hold, for a purely cosmetic gain. The three new files follow the `CCA-F_*_v1.html` convention; the older names stay. Revisit only on a version bump that changes the links anyway. |

---

## Part 2 — Problems found while fixing, not in the original audit

**The corpus index was an internal build document.** The source `CCA-Prep_Corpus-Index_v2.md` is written to the question author: changelogs, generation constraints, an archetype banlist, a script invocation, and a line reading "open decision for Ram". Shipping it verbatim would have put project internals in circulation. It was replaced with a hand-written student-facing index page, and the build now strips author-facing front matter (`Source:` / `Version:` / `Changelog:`) from all five domain files.

**One note inside D3 was written to the question author.** A currency note about `@import` nesting depth ended with a generator rule and a pointer to `EXAM-LOG.md`. The underlying fact is genuinely useful — the community guides say 5, current Anthropic docs say four hops, the Exam Guide is silent — so it was rewritten for a candidate: learn that imports nest and the depth is bounded, do not memorise the digit.

**The official guide has been republished.** The corpus index records that Anthropic reissued the Exam Guide as **v1.0 (effective July 2026)** under the official exam code **CCAR-F**, superseding the v0.2 this material was authored against, and that a measured diff found the domain weights, all six scenarios, all thirty task statements and both scope lists **identical**. Nothing needed rewriting, but candidates should not be surprised by a different version number and exam code on the official page, so a note now says this in the README and on the corpus index page.

**A contradiction about answer format, carried over from v1 of this report.** Three files said multiple-response items exist; the Exam Day Guide said "One best answer of four". That was aligned in the previous pass. It is now also true of the material rather than only of the wording, because the MR drill exists.

**The pass line is 42 raw, not 41.** The adversarial critic on the one-page sheet caught a draft claim that 720 scaled corresponds to about 41 of 60. On the linear approximation the tests use, 41 gives 715 and 42 gives 730. Corrected before it shipped.

---

## Part 3 — How the new material was produced and checked

The 30 multiple-response items and the one-page sheet were authored by a 12-agent workflow, one author per domain reading only that domain's corpus file, then an adversarial verifier per domain instructed to treat every item as broken until checked against the source. The verifiers repaired one D4 item and passed the other 29. The one-page sheet went through a separate critic that raised 13 corrections — one factual error, several duplicated lines, and two coverage gaps (D3 was under-weighted, and lost-in-the-middle was missing from D5 entirely).

Independent structural validation of all 30 items afterwards: domain weighting correct, every `(Select N.)` marker matches its key length, `whyWrong` covers exactly the non-keyed options on every item, 30 distinct corpus sections with no repeats, and every one of the 120 citations resolves to a real anchor. **Zero structural problems.**

Everything was verified in a browser over `http://localhost:18795`:

- 15 HTML files, **0 broken file links, 0 broken fragments**, all 16 URLs return 200.
- **479 distinct section citations across the pack, 0 unresolved.**
- Pack bar present on all 15 files, one variant, correct current-page marker on each.
- No console errors on any page.
- The Trap Sheet's and Atlas's page-switching JS still work after the nav insert; 172 section links created, 0 malformed, 0 injected inside `<code>`.
- The MR drill was driven end to end: select-N cap enforced, all-or-nothing scoring correct, weak domains marked, dashboard payload valid.
- The one-page sheet was measured against real print metrics using its own `@media print` rules: **926px against 1062px usable on A4 and 996px on US Letter** — fits both, with headroom.

---

## Part 4 — What I would look at next

Not gaps, and none of them blocks circulation.

1. **The MR drill is 30 items and single-sitting.** There is no second form, so it can be memorised. A second drill would make it re-usable.
2. **The corpus is the pack's dependency.** Everything now points into it. If the domain source files change, `CCA-F_Corpus_v1.html` has to be rebuilt or the citations drift. The build script lives in this session's scratchpad, not in the repo — worth checking in if this becomes a maintained artifact.
3. **No one has sat this pack cold.** Every check here is structural or mine. One real candidate working through the crunch path start to finish would surface ordering and pacing problems that no amount of link-checking will.

---

## Part 5 — Packaging change (same day, after the remediation above)

The pack was split into two folders for distribution, and `claudecertificationguide.com` was added to the README as the concept-learning layer.

```
mock exams/Learning corpus/   5 reference documents  — what to read
mock exams/Mock tests/        8 practice exams, the dashboard, the README
```

**Every cross-folder link was rewritten**, including the ones built at runtime in JavaScript — `citeHref()` in all eight tests and `studyLinks()` in the tests and the dashboard. Folder names are `%20`-encoded in hrefs. Re-verified after the move: **16 files, 0 broken links, 0 broken fragments, 479 section citations still resolving, all 15 pack bars 9-for-9 with the correct current-page marker, no console errors.** A citation clicked in `Mock tests/Test-1.html` was followed live and landed on `§2.2` on the D2 page of `Learning corpus/CCA-F_Corpus_v1.html`.

**On the external site.** `claudecertificationguide.com` is a free, independent community study site. Its 30 lessons map one-to-one onto the exam's 30 official task statements, with the same five domains and weights as this pack (7/5/6/6/6 lessons for D1–D5). It also carries a diagnostic, per-domain quick-reference sheets, glossaries, build exercises, a drill mode and a progress tracker. It is now **step 0 of a documented eight-step learning pathway** in the README, on the honest division that the site *explains* and this pack *drills and diagnoses* — the pack never taught the subject from zero, and the README now says so plainly instead of letting a beginner start at Test-1 and fail.

Two cautions were carried into the README: the site is not affiliated with Anthropic, and it suggests **MCP transport selection** may be tested where the official guide puts *deploying or hosting MCP servers* and *streaming / server-sent events* explicitly out of scope. That divergence was already recorded in this project's own crawl coverage report; the README now tells a candidate to answer with the official framing.

**One thing worth a decision.** The parent folder is still called `mock exams`, but it now holds a learning corpus as well, and the README — the package's entry point — sits inside `Mock tests/` rather than at the top. That is what was asked for, and it works, but someone opening the package cold sees two folders and no obvious front door. Renaming the parent, or placing a one-line pointer at the top level, would fix that; neither was done because neither was requested.
