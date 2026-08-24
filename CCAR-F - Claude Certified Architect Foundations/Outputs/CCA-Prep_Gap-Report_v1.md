# CCA-F Prep Pack — Gap Report

**Folder audited:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\mock exams`
**Date:** 2026-08-18
**Scope:** the circulation material only. `Test-1.html` through `Test-7.html` were read for facts but not edited.
**Lens:** a student who has just been handed this folder, is short on time, and has to pass.

---

## Part 1 — What was changed

All eight non-test files were edited in place. No file was renamed, so no existing link or bookmark breaks.

| File | Change |
|---|---|
| `README.md`, `README.html` | Rewritten as the folder's gateway. Now references all thirteen files, opens with a stop-when-you-run-out-of-time study order, and carries the exam-facts table, the D1–D5 table, and a stated-limitations section. |
| `Exam-Day-Guide.html` | Removed the owner-specific schedule. "Sunday / Monday / Tuesday" became "Three days out / Two days out / Exam day"; domain codes in the plan are now spelled out; footer no longer reads "Built for Ram's Tuesday exam." Answer-format chip changed from "One best answer of four" to "Each item states how many to select." |
| `CCA-F_Concept-Atlas_v2.html` | Nav tabs expanded from `D1 · 27%` to `D1 Agentic · 27%`. Source line now cites Exam Guide v0.2 (30 June 2026) explicitly. |
| `CCA-F_Trap-Sheet_v1.html` | Nav tabs expanded from bare `D1`–`D5` to named domains. Added a "The five domains" paragraph spelling out all five codes, weights and the `D1-07` card-numbering convention. Added a source-and-disclaimer footer matching the Atlas (it had none). Clarified the `§` legend so it no longer promises a jump the reader cannot make. |
| `Dashboard.html` | Added a "What D1–D5 mean" card visible before any result is pasted, with names, weights and coverage. |
| All five HTML files | Added a shared "CCA-F prep pack" navigation bar linking every file, with the current page highlighted. Previously no file linked to any other. |

**Verified in a browser** (served over `http://localhost:18795`): all 32 local links resolve, no console errors on any page, the Trap Sheet's and Atlas's page-switching JS still work after the nav insert, and the string "Tuesday" and the owner's name no longer appear anywhere.

**One change worth a second look before circulating.** The three reference documents said the exam has multiple-response items; `Exam-Day-Guide.html` said "One best answer of four." I aligned the guide to the other two, since they are the ones anchored to Exam Guide v0.2. Confirm against the official guide, because it is a claim a student will act on.

---

## Part 2 — What is still missing, ranked by what it costs a student

### 1. Test explanations cite files that are not in the folder

Every answer explanation in `Test-1.html`–`Test-7.html` ends with a citation like `CCA-Prep_Domain-4_v2.md §4.9`, and `CCA-F_Trap-Sheet_v1.html` uses the same `§` numbering on its cards. Those files exist at `prep with quiz\CCA-Prep_Domain-1_v2.md` through `_Domain-5_v2.md`, outside the circulation folder. A student sees a reference, wants to read the source, and hits nothing.
**Fix:** render the five corpus files (plus `CCA-Prep_Corpus-Index_v2.md`) into one self-contained HTML file in this folder and link it from the pack bar. Failing that, strip the citation line from the tests.

### 2. Nothing routes a wrong answer to the page that fixes it

The dashboard names the weakest domain and the tests explain each wrong option, but no missed question points at the Atlas, Trap Sheet or Guide card covering that concept. The student is told *what* they got wrong and left to find *where* to read about it.
**Fix:** add a per-domain deep link on the results page and on the dashboard's weakest-domain callout — the anchors already exist (`#d1`…`#d5` in the Atlas, `#p-d1`…`#p-d5` in the Trap Sheet).

### 3. No practice at multiple-response items

The real exam has items that state how many options to select and score all-or-nothing. All 420 practice questions are single-choice. A student can score 900 across seven tests and still meet an item type they have never attempted. The README now warns about this, which is not the same as fixing it.
**Fix:** add an eighth test, or a short supplementary block, made only of multiple-response items.

### 4. No one-page printable cheat sheet

The three references run 67, 124 and 136 cards. All three print, but none is short. There is nothing a student can carry on one sheet in the last hour.
**Fix:** a single-page sheet — the five domains and weights, the ten highest-frequency traps, the escalation and permission-precedence rules, and the "answer everything" reminder.

### 5. Practice scores have no stated meaning

A test reports a scaled score against the 720 pass line, but nothing tells the student what a practice score predicts about the real exam, or how many attempts to sit before trusting the number.
**Fix:** two paragraphs on the dashboard: what a score does and does not predict, and a suggested readiness bar (for example, two consecutive Hint-off tests above a chosen margin).

### 6. The practice tests have no way back to the pack

The new pack navigation bar is on all five reference and tracker pages but not on `Test-1.html`–`Test-7.html`, which were out of scope for this pass. A student who clicks "Practice tests" can only return via the browser's back button.
**Fix:** insert the same `packbar` block into the seven tests — it is one `<style>` and one `<nav>`, and it is hidden in print.

### 7. The Trap Sheet never names the six scenarios

The Atlas and the Exam Day Guide both name all six production scenarios the exam draws from. The Trap Sheet names none, although its whole subject is how stems are built — and stems are built inside those scenarios.
**Fix:** add the six scenario names to the Trap Sheet's "setter's toolkit" page.

### 8. Out-of-scope content is never stated for the student

The Exam Guide has explicit in-scope and out-of-scope lists. The reference documents use them internally, but no file tells a student plainly what will *not* be tested — which is where a panicking candidate wastes their last day.
**Fix:** a short "not on the exam" list in the README or the Exam Day Guide's start page.

### 9. File names are inconsistent

Two files carry the `CCA-F_` prefix and a version suffix (`CCA-F_Concept-Atlas_v2.html`, `CCA-F_Trap-Sheet_v1.html`); three do not (`Exam-Day-Guide.html`, `Dashboard.html`, `README.html`). This is cosmetic and costs a student nothing, which is why it is last.
**Fix:** if you want them uniform, rename on a version bump and update the pack bar and README in the same pass. Renaming now would break links people may already hold.

---

## Part 3 — Verdict on the question asked

**Is there enough here for a crunched student to study, sit a mock test, and self-diagnose?** Yes, for study and for sitting the test. The three references cover the syllabus at three depths, the tests are full-length and weighted to the official domain split, and Hint mode turns any test into a teaching session with a full explanation of every option.

**Self-diagnosis is the weak leg.** The dashboard tells a student *which domain* is weak; nothing tells them *which page to open next*. Gaps 1 and 2 are the two that actually cost marks, and they are the same underlying problem — the folder's diagnostic half and its teaching half are not wired to each other. Fixing those two would do more than everything else on this list combined.
