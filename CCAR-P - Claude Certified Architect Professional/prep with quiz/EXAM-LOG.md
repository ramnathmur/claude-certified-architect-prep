# CCAR-P Exam Log

**The single source of truth for Ram's standing on CCAR-P.** No other file in this project carries
scores. If one starts to, delete it.

**Status:** **Paper 1 generated 2026-08-30, not yet sat.** `mock-exams/CCAR-P_MockTest-1_v1.html`.

*(Corrected 2026-08-29: this line previously read "Blocked on Phase 0" for four days after Phase 0
closed, and briefly said generation would run in TRANSCRIBE mode. Both are superseded below — Ram
chose full AUTHOR mode for Paper 1 once the TRANSCRIBE key-longest problem was measured.)*

---

## Conventions

Carried over from the Foundations project, where each of these was learned by getting it wrong.

1. **`SCORED` headings are the record.** Count `## Paper N — SCORED <date>` headings and attempt
   dates together. Never read standing off a generation entry's status line — on the Foundations log,
   two entries read "Not yet attempted" for a month after they had been scored.
2. **Attempt chronology, never paper numbering.** Papers are sat out of order. Every comparison —
   confirmed weakness, trend, "the previous paper" — uses attempt date, not paper number.
3. **Confirmed weakness** = the same domain *unambiguously* weakest on two consecutive papers by
   attempt date, computed on **single-answer items only**. A tie fails the bar and is recorded as
   `false`. *(Single-answer restriction added 2026-08-29.)* Under all-or-nothing scoring a
   majority-right multi-response miss scores zero and is indistinguishable from a knowledge gap, so
   including those items lets a format leak masquerade as a weak domain and trigger a quota bump that
   tests the wrong thing.
4. **Insights Round every 3 scored papers.** Looks across the window for trends no single paper shows.
5. **Every miss is logged to a corpus section.** A miss with no section reference cannot become a
   pattern, and patterns are the entire point.
6. **Multiple-response items are recorded separately** from single-answer. On Foundations, eight
   misses were majority-right answers scored zero by all-or-nothing grading — a scoring leak that
   looked like a knowledge gap until the formats were split out.
7. **Time per question is recorded.** It distinguishes rushed errors from considered-and-wrong errors.
   On Foundations every miss cluster turned out to be considered-and-wrong, which changed the
   remediation entirely.

---

## Entry template

Copy this block for each paper. Do not abbreviate it — the Professor's Note is what makes the next
paper better than the last.

```markdown
## Paper N — SCORED YYYY-MM-DD (XX/YY, scaled ZZZ)

**File:** `mock-exams/CCAR-P_MockTest-N_v1.html`
**Attempt date:** YYYY-MM-DD | **Score source:** results-json | **Total time:** MM:SS of 120:00
**Total score:** XX / YY correct (estimated scaled ZZZ; pass line 720)
**Item formats:** single-answer A/B (x%) · multiple-response C/D (y%)
**Mode:** Exam Mode (no per-question feedback) / Practice Mode

### Domain Breakdown
| Domain | Questions | Correct | % |
|---|---|---|---|
| ... | | | |

### Misses
The paper's results page generates this table already filled in — use its "EXAM-LOG miss table" export
rather than transcribing by hand.

| Q | Domain § | Facet | Obj | Shape | Format | Time | Picked | Correct | Family | Why wrong |
|---|---|---|---|---|---|---|---|---|---|---|

`Picked` and `Correct` are recorded as full sets (`A+C`), never as a boolean. That is what makes a
retroactive partial-credit rescore possible if multi-response scoring is ever settled — it is still
OPEN in `../EXAM-FACTS_v1.md`. `Family` is which of the eight distractor families captured the answer;
a family recurring across two consecutive papers is a habit, not a knowledge gap, and needs the
Phase 7.1 rule 4 remedy instead of more testing in the same direction.

### Confirmed-weakness check
Comparator: Paper M, attempted YYYY-MM-DD (the true immediate predecessor by attempt date).
Weakest this paper: ... | Unambiguous? yes/no | confirmed_weakness: true/false

### Findings
Ranked by evidence strength. A finding needs a section reference and a stated direction of error.

### Pace
Average s/question. Were the misses fast or slow? Fast = time pressure. Slow = a real decision error.

### Professor's Note — Intent for Paper N+1
Ranked list of what the next paper must test, and from which direction.
```

---

## Papers

## Paper 1 — GENERATED 2026-08-30, not yet attempted

**File:** `mock-exams/CCAR-P_MockTest-1_v1.html`
**Mode:** AUTHOR (63/63 items authored fresh from corpus facets — not TRANSCRIBE). Ram's decision,
2026-08-29: TRANSCRIBE was rejected after measurement showed the correct option is the longest option
in 84% of the corpus's 79 ready-made scenarios (chance is ~33%), which would have made the paper
answerable by length alone. See `Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md` and the chat record for
the full TRANSCRIBE-vs-AUTHOR comparison.
**Professor's Note / Insights Round consumed:** none — this is the diagnostic paper. No targeting
instruction exists yet.
**Random seed:** 20260829 (facet order, correct-letter shuffle, distractor-family draw — recorded for
reproducibility, not because the seed carries any meaning).

### Domain quota (matches EXAM-FACTS_v1.md weighting exactly)
| Domain | Weight | Items |
|---|---|---|
| D1 Solution Design & Architecture | 17% | 11 |
| D2 Claude Models, Prompting & Context Engineering | 13% | 8 |
| D3 Integration | 19% | 12 |
| D4 Evaluation, Testing & Optimization | 16% | 10 |
| D5 Governance, Safety & Risk Management | 14% | 9 |
| D6 Stakeholder Communication & Lifecycle Management | 14% | 9 |
| D7 Developer Productivity & Operational Enablement | 7% | 4 |
| **Total** | 100% | **63** |

### Objective and section coverage
All **38 of 38** official objectives covered, floor pass of 1 item each plus a discretionary pass
(cap 3/objective). 62 distinct corpus sections drawn from (of 78) — one section, 4.11, contributed 2
items after the collision fix below repointed one item there.

### Fidelity gate — full result
Computed by `tools/run-gate.js` against the shipped file with `expectCount:63`.

| # | Check | Result |
|---|---|---|
| 1 | `validateItems()` structural | **PASS** — 63 items, sequential `g`, every non-key option has `whyWrong`, every item has `whyRight`, both multi-response stems state their count |
| 2 | Domain quota | **PASS** — exact match, table above |
| 3 | Per-item domain vs citation | **PASS** — no mismatch found |
| 4 | Cited sections exist | **PASS** |
| 5 | Objective coverage | **PASS** — 38/38, max 3 per objective |
| 6 | Correct-answer letter tally | **PASS** — A14 / B14 / C14 / D13, matches the pre-plan exactly |
| 7 | Multi-response pairs | **PASS** — 8 items, no pair used more than twice |
| 8 | Style budget | **PASS** on hard caps (stem ≤45, option ≤20, spread ≤8). 12 items sit outside the 28–40 soft band (max 45) — a direct cost of the T1/CANONICAL_RESKIN repair pass, which needed more words to state a sharp deciding clause |
| 9 | Framing and token rate | **PASS** — 0 invented entities exam-wide; inline tokens 2% of options (ceiling 15%) |
| 10 | Distractor families | **PASS** — HALF-MOVE 38, WRONG-AXIS 34, EVIDENCE-MISMATCH 23 (floor 15), REPAIR 21, DISCARD 21, DETECTIVE-FOR-PREVENTIVE 17 (floor 9), ARCHITECTED 16 (ceiling 19), OVERSPEC 11. No family over the 47-cap |
| 11 | Dedup | **PASS** — 0 stem pairs ≥0.30 Jaccard within the paper or against the 48-stem seeded ledger. **2 cross-domain lesson collisions found and fixed** (see below) — this check does not exist in the mechanized gate; it was run by hand at generation time and should be added to `tools/run-gate.js` before Paper 2 |
| 12 | Professional-tier floor | **PASS** — every item carries `t1Clause`/`t1Alt`; T1 validity was adversarially checked per item during repair (see below) |
| 13 | Targeting satisfied | **N/A** — no Professor's Note exists yet for Paper 1 |

**Key-longest rate: 0/63 for the final paper** (1 item, g36, has the key as the longest option after a
late content swap — 2%, well under the 40% cap and the corpus's own 84% baseline this mechanism exists
to fix).

### What actually happened during generation — for the next session's benefit

1. **Allocation planned centrally before any prose was written** — domain quota, objective floor pass,
   facet selection, the A14/B14/C14/D13 letter pre-plan, the 8-multi-response pair schedule, and the
   181-distractor family budget were all computed in one pass (`plan.json`), then handed to per-domain
   authoring specs. This is what produced a clean letter tally and family distribution on the first
   pass — no authoring agent ever chose its own letter or family.
2. **First authoring/verify/repair pass ran as a background Workflow and was interrupted twice**: once
   by a single agent's API stream breaking mid-response (D6's author call — the file it had already
   written survived intact, only its status report was lost), and once by the session hitting its usage
   limit during the repair stage (resets tracked by time-of-day, not by this project). Both are
   infrastructure interruptions, not corpus or design problems — the workflow was resumed the next
   session via `resumeFromRunId`.

   **Correction, 2026-08-30, from an independent token audit:** the line above originally claimed the
   resume "replayed completed calls from cache and only re-ran what had actually failed." That is false
   and was never verified before being written — a claim-without-checking of exactly the kind this
   project's own conventions exist to catch. The audit measured the resume actually re-dispatching
   AUTHOR:D7 and VERIFY on six already-succeeded domains (D1, D2, D3, D4, D5, D7), at a cost of
   **1,166,297 tokens for work that had already completed**. Separately, the interruption itself caused
   a retry storm — 12 abandoned stub dispatches plus 6 formally-failed agents burned **~1.68M tokens for
   zero output** in the same window. Combined with the resumed run's own ~3.3M-token cost (never printed
   as a total, since the run was stopped manually rather than left to finish), the real session total
   was **~7.7–8M tokens**, roughly double the ~4.3M that was visible from the three dispatches with
   known aggregates. Full findings, phase-by-phase reconstruction, and 8 named fixes (each pointing at a
   specific file/line) are in finding 8 below.
3. **An independent reverify stage was added after the interruption**, checking every domain fresh
   against the current file state rather than trusting any repair agent's self-reported "fixed" count.
   It found real remaining issues in every domain that had already reported itself clean — this is the
   single strongest piece of evidence in this project for why reverify exists as its own stage rather
   than folding into repair.
4. **A bug in the reverify prompt itself produced false positives**: a `JSON_VALID` check wrongly
   required a literal `correct` field that the item schema was never designed to have (correctness is
   encoded by `family:null`, matching what the assembler and the shipped `validateItems()` both expect).
   This inflated D3's and D7's apparent failure counts by 5 items combined. Caught and discounted before
   the final repair pass — **`tools/run-gate.js` and any future verify prompt should not add a
   `correct`-field requirement.**
5. **Four items in D2 (g15, g16, g18, g19) carry a documented, unfixable T2 exception**: corpus sections
   2.5, 2.6, 2.7, and 2.8 each have exactly one decision-table row, so no same-section neighbouring-
   correct action exists to build a T2 distractor from. This is `GENERATION-INTELLIGENCE.md`'s F-01
   finding materializing concretely on the first paper — **D2 needs roughly 20 more decision-table rows
   before Papers 6–10 are reachable at all**, and this is now overdue evidence for that decision, not
   just a projection.
6. **A cross-domain lesson-collision check caught two duplicates that no per-domain agent could see**:
   g36 (D4 §4.11) and g16 (D2 §2.8) were both drawn from a facet whose answer is "order static content
   first, enable caching" — the identical lesson tested twice under different nouns. g44 (D5 §5.6) and
   g35 (D4 §4.10) were both "confidently wrong after a refresh → check retrieval/indexing first," same
   problem. Both were resolved by repointing the D4/D5 item at a *different facet within the same
   section* (§4.11 has 7 facets, §5.6 has 10 — cascading-model routing and model-version-drift
   respectively), so quota, objective, letter, and family assignments were untouched. **This check does
   not exist anywhere in the mechanized gate and should be added before Paper 2** — it is cheap (compare
   every item's underlying facet-answer text pairwise) and this paper proves it catches something real.
7. **The Jaccard dedup threshold held**: 0 collisions among the paper's 63 stems and the 48-stem seeded
   ledger, at the 0.30 threshold set in `STEM-LEDGER.md`. Worth recalibrating after Paper 2 or 3 once
   more full-length generated stems exist, as that file already flags.
8. **An independent efficiency audit, dispatched cold with no access to this session's own reasoning,
   measured Paper 1's real generation cost at ~7.7–8M tokens** (see the correction on finding 2) and
   named 8 specific fixes, ranked by evidence:
   - **Collapse the 4-stage Author→Verify→Repair→Reverify pipeline into one persistent conversation per
     domain** instead of 4 fresh agent dispatches — every stage transition currently pays a ~65K-token
     "spin-up tax" re-reading the same spec and corpus file from scratch. Estimated 850K–1.3M
     tokens/paper, recurring on all 9 remaining papers.
   - **Make resume check the journal for an already-resolved call before re-dispatching** — the
     mechanism this project believed was already doing this, per the now-corrected finding 2. Measured
     saving: 1,166,297 tokens on this run alone.
   - **Delete the `correct`-field requirement from the reverify prompt's `JSON_VALID` check** — the item
     schema deliberately has no such field; this bug produced the 5 false positives finding 4 already
     documents, and will recur on every future paper's reverify pass until fixed at the source.
   - **Set `effort: 'high'` explicitly on Author and Repair calls**, matching the already-proven
     Verify/Reverify tier, rather than leaving them on the framework's unexamined `xhigh` default —
     these two stages are the largest individual token consumers measured (up to 264,744 output tokens
     on a single call, 97% of it thinking).
   - **Add a cooldown before automatic retry re-dispatches a full fresh agent** — 2+ consecutive
     near-zero-output attempts for the same call within seconds is a throttling signature, not a task
     failure. Measured cost of the retry storm this run hit: 747,010 tokens for zero output.
   - **Codify the cross-domain lesson-collision check into `tools/run-gate.js`** rather than running it
     by hand — already flagged in finding 6, now doubly evidenced: it is the single best value-per-token
     mechanism the audit found, precisely because it isn't a dispatched agent at all.
   - Two more (mechanized-gate-first triage before dispatching reverify; the D2 corpus expansion from
     finding 5, reframed as a recurring cost rather than a one-time gap) are in the full report.
   - The audit's own worked-out numbers should be treated as directional, not exact — it flagged its own
     method (reconstructing per-agent cost from each transcript's final-turn cumulative usage) as an
     approximation where a formal aggregate was never printed.

### Confirmed-weakness check
N/A — no prior paper exists.

### Professor's Note — Intent for Paper 2
This is the diagnostic paper; there is no prior miss data to target. Paper 2's Professor's Note should
be written after Paper 1 is scored, per Phase 9. One structural item to carry forward regardless of
score: **decide on the D2 corpus expansion** (finding 5 above) before Paper 4's Insights Round, since
Papers 6–10 depend on it.

---

## Insights Rounds

*None yet. First one fires at 3 scored papers.*
