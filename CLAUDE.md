# Project: Claude Certification Prep

**Owner:** Ram
**Created:** 2026-06-04 · **Restructured:** 2026-08-19 into one folder per exam
**Scope:** all four Anthropic Claude certifications

Global rules live in `~/.claude/CLAUDE.md`. This file covers what applies across every exam folder.
Each folder has its own `CLAUDE.md` with rules specific to that exam — read both.

---

## Structure

One folder per exam. Each is self-contained: its own exam facts, roadmap, material index, corpus and
mock-exam engine. Nothing at this root carries exam content.

| Folder | Exam | Status |
|---|---|---|
| `CCAR-F - Claude Certified Architect Foundations/` | Architect – Foundations | ✅ Passed 2026-08-18, 851/720. Renewal due 2027-08-18 |
| `CCAR-P - Claude Certified Architect Professional/` | Architect – Professional | Parallel track — kept warm. Phases 0/2/4 closed, mock-exam engine built 2026-08-29, Paper 1 generated 2026-08-30 — see its own `ROADMAP.md` for the live stage |
| `CCAO-F - Claude Certified Associate Foundations/` | Associate – Foundations | Deferred |
| `CCDV-F - Claude Certified Developer Foundations/` | Developer – Foundations | ⭐ **ACTIVE — next exam.** Guide v1.0 filed, Phase 0 closed. All 34 course chapters authored 2026-08-25 — see its own `ROADMAP.md` for the live stage |

**CCDV-F is the active exam.** If Ram says "the exam" or "my prep" without naming one, he means
CCDV-F. CCAR-P runs alongside it as a warm parallel track — its Integration and Responsible-AI lessons
feed CCDV-F and are front-loaded for that reason.

**CCDV-F and CCAR-P hold their official exam guides.** CCDV-F's `EXAM-FACTS_v1.md` is fully VERIFIED —
8 domains, 25 skills, published weights. CCAR-P's guide was obtained 2026-08-25 (a verified
third-party mirror, not a direct Partner Academy login) and its 7 domains / 38 objectives are
VERIFIED with that provenance caveat attached — see its `EXAM-FACTS_v1.md`. **CCAO-F does not** hold a
guide, so its weightings remain UNVERIFIED and no practice question may be generated from it.
*(Corrected 2026-08-26 via `/sync-up` — this previously grouped CCAR-P with CCAO-F as both
guide-less.)*

**Work inside one exam folder at a time.** A question about standing, weightings, or next steps is
always a question about a specific exam, and the answer lives in that folder. If a request does not
name an exam, ask which one before reading anything.

Root holds `README.md`, this file, `index.html` (the hub), deployment config, and `sop/`.

## `sop/` — repeatable procedures

`sop/SOP_Academy-Course-Extraction_v1.md` — how to pull an Anthropic Partner Academy prep path into
local text. **Read it before any Academy course capture; do not improvise.** Every step exists because
a plausible alternative was tried and failed, and §7 lists the dead ends so they are not retried.
Established on the CCDV-F path 2026-08-19 (4 modules, 83 screens, ~381k chars). The extractor script
is `sop/extract-module.js`.

`sop/SOP_Mock-Exam-Engine_v1.md` — the mock-exam engine's design stance (Practice Mode default, Exam
Mode as a narrow exception), item schema, domain-weighted seeding methodology, dashboard pattern, and
verification discipline. **Read it before building or porting a mock-exam engine, a paper, or a
dashboard into any exam folder.** Extracted from CCDV-F 2026-08-25 after two real defects were found
and fixed in that build (an inverted design-stance default, a chapter-to-domain mistagging that passed
every structural check). Governs the engine only — it does not relax each folder's own corpus-
verification gate (§2 below), which stays the deciding factor for whether any item may actually be
generated.

Both apply to CCAR-P and CCAO-F when their turn comes.

---

## Rules that apply to every exam folder

These are the four things that produced a first-attempt pass on CCAR-F. They are not stylistic.

### 1. One source of truth for standing

`<exam folder>/prep with quiz/EXAM-LOG.md`. No other file carries scores. If one starts to, delete it.

The CCAR-F project lost a month to a stale `academy/PROGRESS.md` reporting 45/60 and NO-GO long after
the real figure was 57/60, and it produced a materially wrong artifact before anyone noticed.

### 2. The verification rule

Each folder's `EXAM-FACTS_v1.md` has two tables.

- **VERIFIED** requires an Anthropic-controlled source — anthropic.com, claude.com,
  anthropic-partners.skilljar.com, or pearsonvue.com/anthropic.
- **UNVERIFIED** is everything else, including every community certification guide.
- **Never generate a practice question, a domain quota, or a study plan from the UNVERIFIED table.**

Precedent: on CCAR-F, a community guide stated the exam draws 8 scenarios. The real number is 6. That
error reached generated practice material.

### 3. Corpus discipline

- Domain files are the **only** permitted source for generated questions. Never generate from notes,
  from the web, or from memory.
- Each domain file carries: core-facts table · decision tables · exam scenarios with ✅ correct and ❌
  wrong options · an explicit "Misconception" block per section.
- Write decision rules, not explanatory prose.
- Section numbering is permanent. Misses are logged by section, so renumbering breaks the miss history.

### 4. Exam-log conventions

- **Attempt chronology, never file numbering.** The CCAR-F log was corrupted twice by assuming paper
  number equalled attempt order.
- Confirmed weakness = the same domain unambiguously weakest on two consecutive papers *by attempt
  date*. A tie fails the bar.
- Insights Round every 3 scored papers.
- Multiple-response items are recorded separately and treated as all-or-nothing until proven otherwise.
  Eight CCAR-F misses were majority-right answers scored zero.

---

## Habits that carry across all four exams

From all 64 documented CCAR-F misses:

1. Reaching for a workaround beside a mechanism instead of a narrow adjustment to it.
2. Losing multiple-response items by being majority-right.
3. Choosing an option because of how it *sounds* — safer, more architected, more thorough — rather than
   because it matches the requirement the scenario actually states.

Each folder adds its own fourth habit where one applies. CCAO-F tracks `ALTITUDE` misses (answering
above the tier the exam tests); CCDV-F splits every miss into `RECALL` versus `CONCEPT` because it is
sat closed book.

---

## Output folders

Deliverables go to `Outputs/` **inside the relevant exam folder**. Never to
`C:\Claude Cowork\CLAUDE OUTPUTS\` — this is project-scoped work, and never to the repo root.

## File authoring

Use Write/Edit to author file content. Bash is for executing commands (git, npm, python, mv), not
authoring files. Exception: single-line appends to existing config.

## HTML artifacts

Paged with sticky top nav and prev/next — never one long scroll. Verify in a browser before calling any
artifact done.

## Teaching and explainer prose

The hard bans in `~/.claude/CLAUDE.md` apply to everything written here: no manufactured strawman to
negate, no diagnose-negate-reveal tricolon for plain facts, no isolated dramatic one-liners as
punctuation. A checkable fact gets one flat sentence.

---

## Reference

- Anthropic Partner Academy: https://anthropic-partners.skilljar.com
- Pearson VUE Anthropic program: https://www.pearsonvue.com/us/en/anthropic.html
- Claude platform docs: https://platform.claude.com/docs · Claude Code docs: https://code.claude.com/docs
- Ram's About Me: `C:\Claude Cowork\About Me\about-me.md`
