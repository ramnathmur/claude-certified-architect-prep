# CCAR-P Exam Log

**The single source of truth for Ram's standing on CCAR-P.** No other file in this project carries
scores. If one starts to, delete it.

**Status:** **Paper 1 generated 2026-08-30, not yet sat. Paper 2 generated 2026-08-31, not yet sat.
Paper 3 generated 2026-08-31, not yet sat. Paper 4 generated 2026-08-31, not yet sat. Paper 5
generated 2026-09-02, not yet sat.**
`mock-exams/CCAR-P_MockTest-1_v1.html` · `mock-exams/CCAR-P_MockTest-2_v1.html` ·
`mock-exams/CCAR-P_MockTest-3_v1.html` · `mock-exams/CCAR-P_MockTest-4_v1.html` ·
`mock-exams/CCAR-P_MockTest-5_v1.html`.

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

**Post-generation change, 2026-08-30 — the shipped file is not byte-identical to what the gate table
below first ran against.** Paper 1 gained a per-item `deepDive` layer (all 63 items, 181 `wrongDeep`
entries) rendered below the existing quick verdict, and a pass/fail running-accuracy pill. The quick
feedback was not touched: `whyRight` and `whyWrong` hash identically across all 63 items before and
after (sha256 `9565ea2b…a679a5`), and no item's `correct[]`, family, letter, or domain/objective/shape
tagging was altered. The gate was re-run on the changed file — **0 errors, and the same 12
stem-length warnings**, unchanged from the run recorded below. Grounding provenance, including the 13
items whose `t1Alt` resolves to no corpus row, is in
`../Outputs/CCAR-P_DeepDive-Grounding-Record_v1.md`; the engine-level record is
`GENERATION-INTELLIGENCE.md` Session 3 (F-12, F-13, F-14).

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

## Paper 2 — GENERATED 2026-08-31, not yet attempted

**File:** `mock-exams/CCAR-P_MockTest-2_v1.html`
**Mode:** AUTHOR (63/63 items authored fresh from corpus facets).
**Professor's Note / Insights Round consumed:** none — Paper 1 is not yet scored, so Paper 2 is an
**explicitly untargeted second diagnostic**, confirmed with Ram before generation started. No
targeting triples exist to satisfy or deliberately leave untargeted.
**deepDive:** every item ships `deepDive: null`. Deferred to a miss-driven Phase 9 step this paper
onward — see the mid-generation correction below. Paper 1 is unaffected and keeps its own `deepDive`.

### What actually happened during generation — the full story, because it changed mid-session

1. **First attempt failed outright.** The pipeline redesign that F-11 (Paper 1's cost audit) called
   for — inline `deepDive`, one grounding pass instead of four stages, Agent tool instead of Workflow
   — was implemented and tried first. Of 7 parallel full-domain authoring dispatches, 6 failed with an
   identical `"stream watchdog"` stall and zero output, including on retry for four of them; only D7
   (the smallest, 4 items) succeeded. Roughly 3 hours of wall-clock time and substantial token spend
   produced 4 usable items.
2. **Ram asked for an independent, arms-length audit** rather than another self-directed patch,
   explicitly citing that a first attempt at fixing the cost problem had "already failed once." A
   fresh agent, briefed on the full history but told explicitly not to defer to any prior session's
   framing, audited the system cold. Its report:
   `Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md`.
3. **The audit's verdict:** the core spec (domain quotas, letter pre-plan, T1-T4, distractor-family
   caps) is well-evidenced and not the problem — each mechanism traces to a specific, named, measured
   failure. `deepDive` is the problem: added in a later session with no cited evidence of need,
   roughly tripling per-item cost, and the project's own prior grounding record
   (`Outputs/CCAR-P_DeepDive-Grounding-Record_v1.md`) already showed it overreaches the corpus in 44%
   of Paper 1's items (28/63, 13 flatly IRREDUCIBLE). Separately, the outright failure correlated
   cleanly with dispatch size (item count per turn) rather than corpus size — the only success was
   also the smallest ask, by a wide margin.
4. **Ram approved the audit's recommendation in full.** Two changes, both implemented same-session:
   - `deepDive` demoted from a mandatory generation-time field to a deferred, miss-driven Phase 9
     addition — spec updated in `CCAR-P-Orchestration-Prompt_v2.md` §5.5/§5.6/Phase 9,
     `validateItems()` updated in the template and this paper's file so `deepDive: null` is not an
     error by default. Recorded as `GENERATION-INTELLIGENCE.md` F-15.
   - Authoring dispatch shrunk from one turn per full domain to sub-batches of ~5-6 items, each
     persisted immediately on completion instead of one file written at the very end of a long turn.
     Recorded as F-16.
5. **The redesigned shape was retried: 12 sub-batches covering D1-D6 (D7 untouched, already valid).
   All 12 eventually succeeded — 13 of 13 total dispatches on the corrected shape, zero failures.**
   10 finished in 11.5-17 minutes each; 2 (D2-batch1, D4-batch1) took ~38-39 minutes but still
   completed cleanly, not stalling the way "running long" did on the first attempt's D4/D6.
6. **Assembly, done centrally, not per-agent.** `lessonKey` was computed for all 63 items from each
   item's reported raw corpus answer text (lowercase, punctuation-stripped, stopword-removed, deduped,
   sorted), then the cross-domain collision check (F-10) ran BEFORE shipping, catching 3 collision
   groups: two were false positives from generically short corpus answers ("Reject", "Synchronous")
   shared by items testing genuinely unrelated decisions — resolved by excluding answer texts under 3
   content words from the collision check entirely, since a one-word answer isn't a reliable duplicate
   signal (documented in `tools/run-gate.js`'s sibling assembly script, not added to the committed
   gate). One was a genuine duplicate — g44 (D5 §5.6) and g37 (D4 §4.10) both tested "app not resending
   conversation history" — fixed by repointing g44 to a different §5.6 facet (positional attention /
   "lost in the middle" diagnosis) before either item shipped.
7. **The distractor-family cap was violated on first assembly** — WRONG-AXIS hit 52 of 181 distractors
   against a 45 cap (25%), an artifact of 12 independently-dispatched batches each defaulting to
   WRONG-AXIS as a safe choice without seeing the paper-wide total. Fixed by reading each flagged
   option's own `whyWrong` reasoning and relabelling 10 that were already, on their own terms, a better
   fit for a different family (e.g. a "log the refund for weekly review" distractor was WRONG-AXIS but
   is textbook DETECTIVE-FOR-PREVENTIVE) — content unchanged, only the family tag corrected. Final:
   WRONG-AXIS 42, well clear of the cap.
8. **The independent grounding audit** (7 fresh agents, one per domain, checking only `whyRight`/
   `whyWrong`/`t1Alt` — no `deepDive` to check this paper) found 14 findings across the 63 items, the
   large majority `t1Alt` claims that didn't actually resolve to a real corpus row (the exact F-12
   defect from Paper 1). 9 were fixed directly, grounded in the cited section's actual content re-read
   for the fix. **5 are documented, IRREDUCIBLE exceptions** — down from Paper 1's 13, and unlike
   Paper 1, found and resolved-or-documented in the same generation session rather than discovered
   after shipping:
   - **g14, g15 (D2 §2.2)** — the section's "first-message rule" durability fact is stated as an
     absolute, with no conditional row anywhere in the section (env-var placement is equally absolute
     in the other direction). No single-clause inversion makes any distractor correct.
   - **g19 (D2 §2.9)** — same shape: "keep separate copies" is never the documented correct answer
     under any stated condition in this section's decision table.
   - **g25 (D3 §3.7)** — none of the three distractors' underlying corpus rows resolve cleanly to a
     single-clause inversion of the stated compliance/audit requirement.
   - **g46 (D5 §5.5)** — T2 exception: the section's decision table has only 2 accept-rows and 2
     reject-rows, not enough situational diversity to give a multi-select item's distractors a
     genuine neighbour-correct role without inventing content. Same shape as Paper 1's 4 documented D2
     T2 exceptions for single-facet sections.

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
All **38 of 38** official objectives covered (floor pass of 1 item each, plus a discretionary pass,
cap 3/objective). Facet selection deliberately favoured sections Paper 1 left untouched (D1 §1.8, D3
§3.10/§3.12, D4 §4.6/§4.7/§4.8, D5 §5.9/§5.11, D6 §6.10/§6.11, D7 §7.5) and fresh rows within sections
Paper 1 already used, per the per-domain exclude-lists computed from Paper 1's shipped HTML at
planning time (`_PAPER2-STAGING/p2-slots.md`).

### Fidelity gate — full result
Computed by `tools/run-gate.js` against the shipped file with `expectCount:63`, plus supplementary
checks the mechanized gate does not cover (run as one-off scripts, not committed to `tools/run-gate.js`
— that mechanization stays deliberately deferred to Paper 4 per the orchestration prompt).

| # | Check | Result |
|---|---|---|
| 1 | `validateItems()` structural | **PASS** — 63 items, sequential `g`, every non-key option has `whyWrong`, every item has `whyRight`, all 8 multi-response stems state their count, `deepDive:null` accepted without error |
| 2 | Domain quota | **PASS** — exact match, table above |
| 3 | Per-item domain vs citation | **PASS** — every item's `domain` matches its own `section`'s domain number; every grounding-audit pass independently confirmed `whyRight`/`whyWrong` claims trace to the item's own cited section |
| 4 | Cited sections exist | **PASS** — every section drawn directly from `CCAR-P_Objective-Map_v1.md`'s real section list; every grounding auditor read the cited section directly and found it |
| 5 | Objective coverage | **PASS** — 38/38, verified against the canonical 38 objective codes (not just 38 distinct strings), max 3 per objective |
| 6 | Correct-answer letter tally | **PASS** — A14 / B14 / C13 / D14, matches the §5.1 pre-plan exactly (Paper 2's short letter is C, per the rotation) |
| 7 | Multi-response pairs | **PASS** — AB×2, CD×2, AC×1, BD×1, AD×1, BC×1 across the 8 multi items; no pair exceeds the cap of 2; all 8 stems state "Select two." |
| 8 | Style budget | **PASS** on hard caps (stem ≤45, option ≤20, spread ≤8). 7 items sit outside the 28-40 soft band (max 43) — comparable to Paper 1's 12, a direct cost of the T1/grounding repair pass needing more words to state a precise clause |
| 9 | Framing and token rate | **PASS** — 0 invented company/product/persona names (verified by targeted scan; the only capitalized multi-word phrases found were real terms — Claude Code, Batch API, Social Security, Structured JSON). Inline tokens 0% of options (cap 15%) |
| 10 | Distractor families | **PASS** — WRONG-AXIS 42, HALF-MOVE 38, DISCARD 28, EVIDENCE-MISMATCH 22 (floor 15), REPAIR 16, OVERSPEC 13, ARCHITECTED 11 (ceiling 19), DETECTIVE-FOR-PREVENTIVE 11 (floor 9), of 181 total distractors, cap 45 each. Required a 10-item relabelling pass after first assembly — see generation notes above |
| 11 | Dedup | **PASS** — 0 stem pairs ≥0.30 Jaccard, either within the paper or against the 111-row `STEM-LEDGER.md` (max 0.206 vs ledger, 0.176 within paper). 0 `lessonKey` collisions after resolving 3 groups (2 false-positive from generically short corpus answers, 1 genuine duplicate fixed by repointing g44) |
| 12 | Professional-tier floor | **PASS with 5 documented IRREDUCIBLE exceptions** (g14, g15, g19, g25, g46 — see generation notes above). All other 58 items' `t1Clause`/`t1Alt` pairs were independently verified, by a cold grounding pass that had not seen the authoring reasoning, to resolve to a real, nameable corpus row |
| 13 | Targeting satisfied | **N/A** — no Professor's Note exists yet; Paper 1 is not yet scored |

**t1Alt resolution rate: 58/63 (92%) verified resolving to a real corpus row**, up from Paper 1's
implicit rate (13/63 later found NOT to resolve, i.e. 79% — F-12). The improvement comes from running
the grounding audit BEFORE the generation entry was written, not after.

### Confirmed-weakness check
N/A — no prior SCORED paper exists (Paper 1 is generated but not yet sat).

### Findings
Ranked by evidence strength — these are process/engine findings, not corpus-content findings, so they
belong in `GENERATION-INTELLIGENCE.md` Session 5 in full; summarized here for the record:
1. `deepDive` demoted to deferred Phase 9 (F-15) — the single highest-value change this session.
2. Dispatch granularity (~5-6 items per turn, not a full domain) prevents the stall pattern that broke
   the first attempt (F-16) — untested whether this holds at Paper 3's scale or whether size needs to
   shrink further toward D7's proven 4-item ceiling.
3. Central pre-planning (letters, pairs, objective floor, family minimums) continues to work cleanly
   across independently-dispatched batches — confirmed twice now (Paper 1, and again here across 12
   separate sub-batch agents that never saw each other's output) and should not be revisited.
4. D2's structural thinness (F-01, F-12) is now evidenced a third way: 3 of this paper's 5 IRREDUCIBLE
   T1 exceptions are in D2 (§2.2 ×2, §2.9 ×1), both sections with an absolute, non-conditional decision
   table that cannot support the T1 apparatus regardless of how carefully an item is written. This adds
   weight to the pending D2 corpus-expansion decision.

### Pace
N/A — not yet attempted.

### Professor's Note — Intent for Paper 3
Paper 2, like Paper 1, is a diagnostic with no prior scored paper to target — there is no Professor's
Note to consume yet for Paper 3 either. It will be written after Paper 1 and/or Paper 2 are actually
sat, per Phase 9. Structural items to carry forward regardless of score:
- **Decide on the D2 corpus expansion** (F-01, F-12, and now this paper's 3 D2 IRREDUCIBLE exceptions)
  before Paper 4's Insights Round, since Papers 6-10 depend on it and the evidence for needing it keeps
  accumulating.
- **Re-verify the sub-batch dispatch fix holds** on Paper 3's generation — if a repeat run also needs
  12+ small dispatches to avoid stalling, that is itself worth a line in the next Insights Round.

---

## Paper 3 — GENERATED 2026-08-31, not yet attempted

**File:** `mock-exams/CCAR-P_MockTest-3_v1.html`
**Mode:** AUTHOR (63/63 items authored fresh from corpus facets and, for D2, misconception units).
**Professor's Note / Insights Round consumed:** none — Papers 1 and 2 are both generated but neither
is scored yet, so Paper 3 is **another explicitly untargeted diagnostic**, confirmed with Ram before
generation started (he chose to generate a third paper now rather than pause to sit an existing one
first). No targeting triples exist to satisfy or deliberately leave untargeted.
**deepDive:** every item ships `deepDive: null`, per the standing Paper 2-onward rule.

### What actually happened during generation

1. **Facet freshness was computed from the shipped HTML directly, not from `FACET-LEDGER.md`'s own
   "used" column** — per §3d of `Outputs/CCAR-P_Paper-3-4-Generation-Prompt_v1.md`, which flags that
   column as having at least one known gap. A Node script loaded Papers 1 and 2's `ITEMS` arrays the
   same way `tools/run-gate.js` does and extracted every `facet` string actually shipped; that set,
   not the ledger, was the exclusion list for Paper 3's central plan.
2. **D2's misconception-unit fallback (Phase 4 rule 5) fired for the first time.** D2 holds only 18
   decision-table facets against an 8-item/paper quota (F-01); after Papers 1-2 consumed 16 of them,
   only 2 fresh facets remained (§2.2's and §2.3's). The other 6 of D2's 8 items this paper are built
   from a section's `Misconception` block instead — M-2.1, M-2.2, M-2.4, M-2.6, M-2.7, M-2.8 — spread
   across 8 of D2's 9 sections with no section repeated. This is expected, mechanized behaviour the
   engine was specifically built to support (the D2 supply note's "Papers 1-5 reachable via direction
   doubling + misconception units" plan), not a corpus failure. M-2.3, M-2.5, M-2.9 remain in reserve
   for Papers 4-5; the D2 corpus-expansion decision (F-01) is still not due until the Paper 4 Insights
   Round, but this paper is the first hard evidence the fallback mechanism actually works in practice.
3. **The redesigned sub-batch pipeline held a third time — 13 of 13 dispatches succeeded, zero
   failures**, matching Paper 2's clean run exactly (D1×2, D2×2, D3×2, D4×2, D5×2, D6×2, D7×1
   sub-batches of 4-6 items each). No stalls, no retries needed. F-16/F-17's dispatch-granularity fix
   is now confirmed across two consecutive full generations, not a one-off.
4. **Assembly-stage checks caught three real, paper-wide problems no individual sub-batch could see**
   (F-19's pattern held a third time):
   - **ARCHITECTED at 20/181 distractors against the 19 cap.** Fixed by relabelling one distractor
     (D5 g49-D) to `EVIDENCE-MISMATCH`, matching what its own `whyWrong` text already argued — no
     content rewrite, same as every prior instance of this fix.
   - **Two genuine cross-item content collisions**, both found by the stem-Jaccard check, not the
     `lessonKey` check (0 `lessonKey` collisions this paper): (a) **g55 (D6 §6.11, multi) scored 0.349
     against Paper 2's own g55** — both items independently combined §6.11's "40 users → 800 users"
     and "12% human review" facts with near-identical numbers; fixed by changing Paper 3's g55 to a
     60-user → 1,200-user pilot instead, preserving the same ratio and the facets' own genuine numbers
     (1-in-500 failure, 200 cases, 12%) untouched. (b) **g34 and g40 (both D4 §4.9) scored 0.356 against
     each other, within this paper** — g34's multi-response answer already tested the "guardrail
     breach → do not ship" row (F-4.9-05) as one of its two correct options, and g40 independently
     tested the identical row as its own single-answer item; fixed by repointing g40 to the unused
     F-4.9-06 row (aggregate-vs-segment masking) instead, a genuinely different D4 decision. Both fixes
     re-verified below threshold (0.295 and 0.271 respectively) after the edit.
   - A first attempt at the ARCHITECTED fix (relabelling D5 g47-B to `DETECTIVE-FOR-PREVENTIVE` to
     backfill the floor after g40's rewrite removed g40's own old `DETECTIVE-FOR-PREVENTIVE` tag) was
     itself **wrong** — see finding 6 below.
5. **The independent grounding audit (7 fresh agents, one per domain, blind to the authors' own
   reasoning) ran before this entry was written, per F-20**, and found more than either prior paper:
   - **8 formal `t1Alt`-does-not-resolve findings, classified IRREDUCIBLE** — g2, g5, g11 (D1); g13,
     g17 (D2); g25 (D3); g36 (D4); g55 (D6, the same item fixed for the content collision above, on a
     separate axis). This is higher than Paper 2's 5 and closer to Paper 1's 13, despite the
     same-session-audit practice that produced Paper 2's improvement — see finding 4 below for the
     likely reason. All 8 were re-verified as genuinely unsupported by any real corpus row, not just
     under-checked; documented rather than force-resolved, per Phase 6/9's standing rule.
   - **11 FIXABLE findings, all corrected before shipping:** a citation gap (D2 g13 — its correct
     option rests partly on §2.9, not only its cited §2.2), three `t1Clause`/`t1Alt` misdirections (D3
     g22; D5 g45), two option-wording mismatches against the corpus's actual stated granularity (D3
     g20, g28 — "single-tool agent" reworded to match the corpus's own "4-6 tools each"), one
     fabricated stem-claim in a distractor's `whyWrong` (D5 g43), one internally-inconsistent
     `whyWrong` (D6 g51), one item whose stem was missing a field the corpus's own four-part definition
     requires (D6 g58 — added "the expected output" to the tracked-fields list), a stale numeric
     leftover from the g55 collision fix (D6 g55's `whyWrong.B` still said "800-user" after the stem
     changed to 1,200), and two `facet` fields that pointed at the reject-row for one of the item's own
     distractors instead of either row the multi-response item actually tests (D7 g60, g62).
   - Several additional low-confidence, non-blocking notes (D3 g29/g31, D5 g42/g44/g48/g49/g54, D2
     g14/g15) — cross-section reasoning borrowed for a distractor's flavour text, or a family-tag
     shape debatable but not wrong. None contradicts a corpus fact; documented, not fixed, consistent
     with how the audit's own authors classified them as secondary.
6. **The D5 audit caught this session's own error** — the ARCHITECTED-fix relabel of D5 g47's option B
   to `DETECTIVE-FOR-PREVENTIVE` (step 4 above) was checked against the audit's own contrast case
   (D5 g42's genuinely correct `DETECTIVE-FOR-PREVENTIVE` distractor) and found backwards: a
   pre-execution approval gate is a preventive control, not a detective one. g47-B was reverted to
   `ARCHITECTED` (its original, honest label), and D6 g59-D — "ship now, audit a sample of outputs
   afterward" — was relabelled to `DETECTIVE-FOR-PREVENTIVE` instead, a genuine after-the-fact-detection
   case confirmed against the same contrast pair. Worth keeping as a standing caution: a family-cap fix
   made without grounding-audit review is exactly the kind of change the audit exists to catch, and did.

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
All **38 of 38** official objectives covered (floor pass of 1 item each, plus a discretionary pass,
cap 3/objective, actual max 2). 49 distinct sections drawn from, spread across the domain — D2 drew on
8 of its 9 sections (only §2.9 untouched among sections with any facet/misconception left) precisely
because of the misconception-unit fallback documented above.

### Fidelity gate — full result
Computed by `tools/run-gate.js` against the shipped file with `expectCount:63`, plus the same
supplementary one-off scripts Paper 2 used for the checks the mechanized gate doesn't yet cover
(deliberately deferred to Paper 4's gate-mechanization work).

| # | Check | Result |
|---|---|---|
| 1 | `validateItems()` structural | **PASS** — 63 items, sequential `g`, every non-key option has `whyWrong`, every item has `whyRight`, all 8 multi-response stems state their count (3 needed a rewrite from "which two" / "select the two" phrasing to a literal "select two" match), `deepDive:null` accepted without error |
| 2 | Domain quota | **PASS** — exact match, table above |
| 3 | Per-item domain vs citation | **PASS** — no domain/citation mismatch surfaced by any of the 7 independent grounding-audit passes, each of which read every item's own cited section directly |
| 4 | Cited sections exist | **PASS** — every section drawn from `CCAR-P_Objective-Map_v1.md`'s real section list; every grounding auditor read the cited section directly and found it, including the 6 D2 misconception-unit items' `Misconception` blocks |
| 5 | Objective coverage | **PASS** — 38/38, max 2 per objective (cap is 3) |
| 6 | Correct-answer letter tally | **PASS** — A14 / B13 / C14 / D14, matches the §5.1 pre-plan exactly (Paper 3's short letter is B, per the D→C→B→A rotation) |
| 7 | Multi-response pairs | **PASS** — AB×2, CD×2, AC×1, BD×1, AD×1, BC×1 across the 8 multi items; no pair exceeds the cap of 2; all 8 stems state "Select two" |
| 8 | Style budget | **PASS** on hard caps (stem ≤45 after 1 fix from 47, option ≤20 after 1 fix from 21, spread ≤8). 21 items sit outside the 28-40 soft band (median exactly 40, max 45) — a larger deviation than Paper 2's 7, worth watching but not a gate failure since the band is explicitly provisional guidance, not a cap |
| 9 | Framing and token rate | **PASS** — 0 invented company/product/persona names (every author explicitly checked this; no finding raised by any grounding audit). Inline code/config tokens: 6 of 252 options (2.4%, cap 15%), all in D7 where the content is inherently about Claude Code configuration mechanisms; confirmed 0 in D1/D5/D6 by direct scan |
| 10 | Distractor families | **PASS** — WRONG-AXIS 38, HALF-MOVE 24, DISCARD 30, EVIDENCE-MISMATCH 29 (floor 15), REPAIR 20, ARCHITECTED 19 (ceiling 19, exact), OVERSPEC 12, DETECTIVE-FOR-PREVENTIVE 9 (floor 9, exact), of 181 total distractors, cap 47 each. Required a same-session self-correction — see finding 6 above |
| 11 | Dedup | **PASS after 2 real fixes** — 0 stem pairs ≥0.30 Jaccard after fixing g55 (was 0.349 vs Paper 2's own g55, now 0.295) and g34/g40 (was 0.356 within-paper, now 0.271). 0 `lessonKey` collisions. 0 `(section, facet, shape)` triples used more than twice across Papers 1-3 |
| 12 | Professional-tier floor | **PASS with 8 documented IRREDUCIBLE exceptions** (g2, g5, g11, g13, g17, g25, g36, g55 — see finding 5 above). All other 55 items' `t1Clause`/`t1Alt` pairs were independently verified, by a cold grounding pass that had not seen the authoring reasoning, to resolve to a real, nameable corpus row |
| 13 | Targeting satisfied | **N/A** — no Professor's Note exists yet; Papers 1 and 2 are both unscored |

**t1Alt resolution rate: 55/63 (87%) verified resolving to a real corpus row** before shipping — lower
than Paper 2's 92% (58/63) but the audit that measured it was also more thorough (Paper 3 used the same
one-audit-per-domain shape, but every auditor was instructed to check every item's `t1Alt` regardless of
whether the author had already flagged it, rather than prioritizing flagged items). Still well above
Paper 1's discovered-after-shipping 79%, and — critically — found and resolved-or-documented in this
same generation session, per F-20.

### Confirmed-weakness check
N/A — no prior SCORED paper exists (Papers 1 and 2 are both generated but not yet sat).

### Findings
Ranked by evidence strength — process/engine findings, not corpus-content findings, so they belong in
`GENERATION-INTELLIGENCE.md` Session 6 in full; summarized here for the record:
1. **The `t1Alt` IRREDUCIBLE rate rose to 8/63 (13%) despite the same-session-audit discipline that
   lowered Paper 2's rate — the driver looks like which specific facets got drawn, not a process
   regression.** 3 of the 8 are in D1, a facet-rich domain (62 facets) with no supply pressure,
   spanning two different sections (§1.10, §1.11 ×2) that simply don't carry a row supporting the
   claimed pivot. This extends F-14's original point (some findings are a property of the item, not
   the checking) — facet-rich domains are not immune, and the rate may be closer to a corpus-wide
   baseline than Paper 2's 8% suggested.
2. **A same-session fix made to satisfy a mechanized cap, without grounding-audit review, was itself
   wrong** (finding 6 above) — caught only because the audit's own contrast pair (a genuinely correct
   `DETECTIVE-FOR-PREVENTIVE` distractor elsewhere in the same domain) made the mislabel visible. Worth
   a standing caution for any future paper: a family-tag fix applied to satisfy a cap, not because a
   grounding pass confirmed the label, should be treated as provisional until the grounding audit runs.
3. **Extracting facet freshness from the shipped HTML rather than trusting `FACET-LEDGER.md`'s own
   "used" column (per §3d) is now standing practice, confirmed working** — the ledger's known gap did
   not propagate into this paper's plan.
4. **D2's misconception-unit fallback is now proven in practice, not just planned** — 6 of 8 D2 items
   this paper are misconception-unit items, built and grounding-audited exactly like facet-based items,
   with no structural problems the fallback itself introduced (both D2 IRREDUCIBLE findings, g13 and
   g17, trace to the underlying section's thin table structure, not to the misconception-unit format).
5. **Dispatch granularity (~5-6 items per turn) held a third consecutive time, 13/13, zero stalls** —
   F-16/F-17 can now be treated as settled rather than provisional.

### Pace
N/A — not yet attempted.

### Professor's Note — Intent for Paper 4
Paper 3, like Papers 1 and 2, is a diagnostic with no prior scored paper to target — there is still no
Professor's Note to consume for Paper 4 either, unless Papers 1-3 get sat and scored before Paper 4 is
generated. Structural items to carry forward regardless of score:
- **Decide on the D2 corpus expansion** (F-01, F-12, now with a third D2-specific signal — this
  paper's misconception-unit fallback firing for the first time) — still due by the Paper 4 Insights
  Round, and Paper 4 itself is the paper the orchestration prompt names for the gate-mechanization work
  and the D2 decision surfacing, per §5 of `Outputs/CCAR-P_Paper-3-4-Generation-Prompt_v1.md`.
- **Watch the `t1Alt` IRREDUCIBLE rate on Paper 4** — if it stays near 8/63 rather than reverting toward
  Paper 2's 5/63, that is evidence the rate is closer to a real corpus-wide baseline than a fixable
  process defect, worth raising at the Paper 4 Insights Round alongside the D2 decision.
- **A separate, unrelated defect was found and flagged (not fixed) while building this paper**: Paper
  2's own shipped landing page still shows the TEMPLATE's placeholder title and demo-content banner
  instead of real Paper 2 content — spawned as its own background task rather than fixed here, since it
  is out of Paper 3's scope.

---

## Paper 4 — GENERATED 2026-08-31, not yet attempted

**File:** `mock-exams/CCAR-P_MockTest-4_v1.html`
**Mode:** AUTHOR (63/63 items authored fresh from corpus facets, decision-table reuse-inversion,
and misconception units).
**Professor's Note / Insights Round consumed:** none — Papers 1-3 are all generated but none is
scored yet, so Paper 4 is a **third explicitly untargeted diagnostic**, confirmed with Ram before
generation started (he chose to keep generating rather than pause to sit an existing paper first).
No targeting triples exist to satisfy or deliberately leave untargeted; Phase 7.1 rule 4 (habit
escalation) has no scored data to fire on.
**deepDive:** every item ships `deepDive: null`, per the standing Paper 2-onward rule.

**Structural upgrade this paper, per §7.2/§7.3 of the orchestration prompt:** direction inversion
begins. 17 items ship `direction: "inverted"` — at least 2 per shape, all 8 shapes covered, spread
across 6 of 7 domains (D2 supplies 5, structurally forced by its supply crisis; the other 12 spread
across D1/D3/D4/D5/D6).

### D2's facet-supply decision — Ram's approved mechanism, implemented

D2's real decision-table facet supply is fully exhausted across Papers 1-3 (0 of 18 facets fresh).
Before generating any D2 item, Ram was asked which of the facet-supply note's three fallbacks to
use for the remaining 5 items after the 3 unused misconception units (M-2.3, M-2.5, M-2.9). He
chose **direction-inverted reuse of an already-used facet** (option a) over corpus expansion now or
a one-off quota shift. Implemented exactly as approved: sections 2.1, 2.2, 2.4, 2.7, 2.8 each reuse
their own section's primary facet as a conceptual anchor, but the authored item tests the shape's
**inverted** direction against a genuinely different scenario and correct answer — not a reword of
the anchor's own lesson. This is recorded here as the locked-in decision for this paper, the same
way the `deepDive` demotion and sub-batch size were recorded as Ram's decisions in Paper 2's entry.

### What actually happened during generation — the full story, including two real mistakes

1. **Facet freshness was computed from all three shipped papers' HTML directly**, extending the
   Paper 3 method (`_PAPER4-STAGING/analyze-prior-papers.js`, `parse-facet-ledger.js`) — confirmed
   D2 fully exhausted (0/18 fresh, matching the prompt's own §2 warning) before any D2 item was
   planned.
2. **The central plan caught and fixed a shape-distribution violation before any authoring
   started.** The raw freshness-greedy draw put S1 at 15 items (over the archetype ledger's hard
   ceiling of 11) and S8 at 3 (under the hard floor of 4) — `ARCHETYPE-LEDGER.md`'s own stated
   budget, not one of the 13 numbered gate checks, but a real requirement all the same. Fixed by
   moving 4 normal-direction items to a better-fitting shape (3.2, 5.1×2 → S8; 4.6 → S6), verified
   in-code before dispatch.
3. **13 of 13 sub-batch dispatches succeeded on the first try, zero stalls** — the fourth
   consecutive clean run on the F-16/F-17 dispatch-granularity fix (D1×2, D2×2, D3×2, D4×2, D5×2,
   D6×2, D7×1, 4-6 items each).
4. **The D2 misconception fallback and the reuse-inversion mechanism both worked as designed on
   first authoring**, with one expected exception: section 2.2's reuse-inverted item was flagged by
   its own author as a likely IRREDUCIBLE T1/T2 case, matching Paper 2's g14/g15 precedent for the
   same section's absolute rule.
5. **Assembly caught two real family-cap violations** (ARCHITECTED 20/19 cap, DETECTIVE-FOR-
   PREVENTIVE 7/9 floor) and one real stem-Jaccard collision (g49 scored 0.319 against Paper 3's own
   g49 — same underlying "claims team / review everything, ease off later" framing) — fixed by
   relabelling two distractors whose own `whyWrong` text already argued the correct family, and by
   recasting g49's cover story from insurance claims to expense reports while preserving the same
   M-5.8 misconception and routing logic. Re-verified below threshold after the edit (max 0.275).
6. **`validateItems()` caught 4 real construction errors at the mechanized gate** (this paper's
   check-1 run, not a one-off script): three multi-response stems (g29, g34, g55) stated their count
   in a phrasing the schema's `/select\s+(two|three|\d)/i` regex didn't match ("select the two...",
   "which two...") — fixed by rewording to the literal pattern, matching Paper 3's own precedent for
   the identical defect. **g34 also had a genuine, non-cosmetic bug**: its `t1Alt` named an option
   that was already one of its own two correct answers, which is nonsensical — this item has two
   independently-sufficient reasons not to ship (a guardrail breach and a segment regression), so no
   single-clause deletion could isolate one without leaving the other still correct. Fixed with a
   documented compound-clause T1 (both facts removed together flip the answer to A) — the
   independent grounding audit confirmed this holds up logically but is a structurally different
   kind of T1 than the paper's other single-clause entries, and should be read as a documented
   exception for multi-select items with two independently-sufficient correct reasons, not a
   template to copy casually.
7. **A real, if easily-fixed, bug was found only by opening the shipped file in a browser and
   clicking through it, exactly as §4f/step-9 requires**: every item was missing the `cite` field
   the template renders in every feedback footer, so the UI showed "undefined" instead of e.g.
   "D1 1.1" on every single question. This traces to an omission in this session's own shared
   authoring brief (`p4-shared-brief.md`'s item schema didn't list `cite`, unlike Papers 1-3's own
   briefs) — not a sub-batch error. Fixed by adding `cite: domain + " " + section` to all 63 items,
   and by adding `cite` to `validateItems()`'s required-field list in the TEMPLATE itself so a
   future paper cannot silently ship the same gap. This is the clearest single piece of evidence in
   this paper's own generation for why the browser-click step is not optional busywork.
8. **The fidelity gate was mechanized into `tools/run-gate.js`, per the orchestration prompt's own
   note that Paper 4 is where hand-checking stops being reliable.** Checks 10 (distractor-family
   caps) and 11 (stem-Jaccard vs `STEM-LEDGER.md`, plus (shape,section,facet) triple reuse vs
   `ARCHETYPE-LEDGER.md`) are now committed, reusable code instead of a one-off script rebuilt every
   paper. Building this caught its own bug before it shipped: a first draft computed the family
   floors/ceiling as a live percentage of the paper's actual distractor count (181, since
   multi-response items carry 2 distractors instead of 3) rather than the orchestration prompt's
   fixed thresholds (15/9/19/47, calibrated against a 189-distractor baseline) — `ceil(181×0.05)=10`
   would have failed a paper sitting exactly at the correct floor of 9. Fixed to use the fixed
   numbers directly.
9. **The independent grounding audit (7 fresh agents, one per domain, blind to the authors' own
   reasoning and to each other's notes) ran before this entry was written, per F-20, and found
   materially more than any prior paper — itself a sign the process is working, not regressing:**
   - **One direct disagreement with a sub-batch author's own self-assessment, resolved in the
     audit's favour**: the D2 section-2.2 item's author flagged it as IRREDUCIBLE (T1/T2 do not
     resolve). The independent D2 auditor read it fresh and concluded it **does** resolve, just
     weakly, and named the specific wording fix needed (make option A's no-op function explicit).
     Applied exactly as recommended; the item is now a genuine T1 pass, not a documented exception.
     This is the single clearest demonstration this paper produced of why the audit is blind to the
     author's own reasoning — two competent readers reached opposite conclusions from the same item,
     and the fresh read was right.
   - **One confirmed real failure of Ram's own approved D2 mechanism**: the D2 section-2.8
     reuse-inverted item (g19) was found to be a **cosmetic restate**, not a genuine inversion — its
     "compliance stamp" framing reduced to the exact same "order static content first, satisfies
     both constraints" lesson Paper 1's own already-shipped item at this facet already teaches, just
     with different nouns. This is precisely the risk §2 of the generation prompt warned about
     before any D2 item was authored. Reworked into a genuine S2-inverted item: a regulator-mandated
     per-request token that must be first, non-negotiable, which genuinely cannot be reconciled with
     caching's byte-identical-prefix requirement — the correct answer accepts caching does not apply
     here, rather than finding an ordering trick, which is a structurally different lesson from the
     anchor facet's own answer.
   - **8 more fixable findings, all corrected**: two family-tag mismatches in D1 (g2-C REPAIR→
     EVIDENCE-MISMATCH, g5-D OVERSPEC→ARCHITECTED) and one in D3 (g21-B ARCHITECTED→HALF-MOVE), a
     shape mistag in D2 (g15 S6→S3, since a root-cause "what changed" diagnosis is S3's textbook
     shape, not S6's), an objective mistag in D5 (g46 O5.4→O5.5, matching section 5.10's own stated
     objective), a section mis-citation in D6 (g56's actual tested content is section 6.6's
     attestation-requirement row, not 6.2's — re-cited with the matching facet F-6.6-04, which
     re-verifying in the browser caught a second bug in: the `cite` field wasn't updated alongside
     the section/facet/objective retag, so it still showed "D6 6.2" — fixed), a t1Clause exact-
     substring typo in D6 (g57, "this segment" vs the stem's "the segment"), and an internal
     contradiction in D3 (g22's stem stated the SLA had "no slack" while its own correct answer
     claimed a lever that "fits the SLA" — fixed by giving the SLA a small, stated ~30ms of slack so
     the correct answer's own premise holds).
   - **One structural (not corpus-fidelity) grounding gap in D5**: g45's stem never mentioned an
     AI/LLM system at all, reading as a generic cloud-network-security question on a certification
     that tests AI architecture specifically. Fixed by tying the network-layer control explicitly to
     the assistant's own inference-endpoint traffic.
   - **One cross-paper structural duplication concern in D7, found by a targeted comparison the
     audit brief specifically asked for**: g60 (a 2-of-4 multi-response item combining D7's
     `allowed-tools` and `context:fork` mechanisms) was found to closely structurally mirror Paper
     1's own g60 at the same two facets — same two-part mechanism pairing, same two-part problem
     shape, differing only in renamed nouns. This traces to a real, if milder, supply-depth
     constraint in D7's section 7.2 (only two positive mechanism rows exist to pair for a
     multi-response item there, similar in kind to D2's own F-01 finding), not to authoring
     carelessness — reworked with a substantially different scenario (an incident-triage skill and a
     package-publish restriction, instead of a code-review skill and a git-rebase restriction) to
     reduce recognition risk while keeping the same underlying, corpus-forced mechanism pairing. A
     milder, partial overlap was also found between this paper's g62 and Paper 1's own g62 (same
     deny+hook mechanism pair, different specific illustration) — documented, not reworked, since the
     audit itself called this the less severe of the two findings and it did not reach the "strongest
     duplication" bar g60 did.
   - **One genuinely unresolved T1, confirmed IRREDUCIBLE by two independent readers**: g63 (D7
     §7.1)'s own author flagged doubt about whether negating "the live sessions retired" cleanly
     promotes the re-record option to correct. The independent D7 auditor tried the same clause and
     two alternates, found none resolve without removing the scenario's premise entirely, and
     concluded IRREDUCIBLE. Documented as such rather than forced — every other part of the item
     (Reject-row anchoring, sibling-row accuracy, whyRight/whyWrong) checks out.
   - **Applying these fixes required two further correction passes of my own**, each caught by
     re-running the mechanized gate rather than by a human eye: the g1 and g19 reworks were first
     written with the correct answer sitting on a different letter than the paper's own pre-planned
     balanced letter tally required (breaking `correct[]`/family-tag consistency, not just cosmetics
     — `validateItems()` caught both as "distractor has no family" and "t1Alt names an already-
     correct option"), and a family relabel needed to change g59's tag introduced a duplicate-family
     violation on a different item. Both are recorded here in the interest of the same honesty
     standard this project applies to authoring: a fix is not verified just because it looks
     plausible: it must be re-run through the same gate as everything else.
10. **`t1Alt` resolution rate: 62/63 (98%) after the audit and its fixes** — the highest of any
    paper so far (Paper 1: 79% discovered after shipping; Paper 2: 92%; Paper 3: 87%), with exactly
    one documented IRREDUCIBLE case (g63), against Paper 3's 8 and Paper 2's 5. This is not
    necessarily evidence the underlying rate has improved structurally — this paper received an
    unusually heavy fix cycle (three separate correction passes after the initial audit) that no
    prior paper needed, so the comparison should be read with that caveat attached, not as a clean
    trend line.

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
All **38 of 38** official objectives covered (floor pass of 1 item each, plus a discretionary pass,
cap 3/objective, actual max 3). 52 distinct corpus sections drawn from (of 78) — D2 drew on all 9 of
its sections (all fully exhausted of fresh facets; 3 via misconception unit, 5 via direction-
inverted reuse, all shown correctly-cited after the D6/g56 mis-citation fix).

### Fidelity gate — full result
Checks 1, 10, 11 are now mechanized in `tools/run-gate.js` (this paper's own contribution, per the
orchestration prompt's Phase 6 closing note). Checks 5, 7, 12 run as a one-off script
(`_PAPER4-STAGING/extra-checks.js`, same shape as Papers 2-3's); 2-4, 6, 8-9, 13 checked directly
against the assembled items and the plan.

| # | Check | Result |
|---|---|---|
| 1 | `validateItems()` structural | **PASS** — 63 items, sequential `g`, every non-key option has `whyWrong`, every item has `whyRight`, all 8 multi-response stems match the literal `/select (two\|three\|\d)/i` pattern after 3 rewrites, `deepDive:null` accepted, `cite` present on all 63 (added to the required-field list this paper after being found missing in the browser) |
| 2 | Domain quota | **PASS** — exact match, table above |
| 3 | Per-item domain vs citation | **PASS** — the D6/g56 mis-citation (section 6.2 tagged, content actually 6.6's) found by the independent audit is fixed; no other mismatch found by any of the 7 audits |
| 4 | Cited sections exist | **PASS** — every section resolves in `CCAR-P_Objective-Map_v1.md`'s real section list; every grounding auditor read the cited section directly |
| 5 | Objective coverage | **PASS** — 38/38, max 3 per objective |
| 6 | Correct-answer letter tally | **PASS** — A13 / B14 / C14 / D14, matches the §5.1 pre-plan exactly (Paper 4's short letter is A, per the D→C→B→A rotation) — preserved through two rounds of audit-fix rework that initially broke it and was caught by the gate, not by inspection |
| 7 | Multi-response pairs | **PASS** — AB×2, CD×2, AC×1, BD×1, AD×1, BC×1 across the 8 multi items; no pair exceeds the cap of 2; all 8 stems state their count |
| 8 | Style budget | **PASS** on hard caps (stem ≤45, option ≤20, spread ≤8) after fixing 2 whyWrong entries found over the 30-word cap during a post-fix re-sweep. 30 items sit outside the 28–40 soft band (median 40) — comparable to Paper 3's 21, not a gate failure since the band is guidance |
| 9 | Framing and token rate | **PASS** — 0 invented company/product/persona names (scanned programmatically, not just by eye). Inline code/config tokens 2.4% of options (cap 15%), 0 in D1/D5/D6 |
| 10 | Distractor families | **PASS**, now mechanized — WRONG-AXIS 36, HALF-MOVE 34, DISCARD 29, REPAIR 18, ARCHITECTED 19 (ceiling 19, exact), EVIDENCE-MISMATCH 28 (floor 15), OVERSPEC 8, DETECTIVE-FOR-PREVENTIVE 9 (floor 9, exact), of 181 total distractors, no family over the 47 cap. Needed 2 assembly-time relabels plus 3 more during the audit-fix cycle to hold both bounds simultaneously — see the generation story above |
| 11 | Dedup | **PASS**, stem-Jaccard now mechanized — 0 stem pairs ≥0.30 Jaccard against 237 seeded+prior stems or within-paper, after fixing g49 (was 0.319 vs Paper 3's own g49, now 0.275 max). 0 `lessonKey` collisions (3 misconception-unit items per domain correctly carry `lessonKey:""`, matching the schema's own carve-out). 0 `(section, facet, shape, direction)` triple used more than twice historically, now mechanized against `ARCHETYPE-LEDGER.md` |
| 12 | Professional-tier floor | **PASS with 1 documented IRREDUCIBLE exception** (g63 — see finding above). All other 62 items' `t1Clause`/`t1Alt` pairs were independently verified, by 7 cold grounding passes that had not seen the authoring reasoning, to resolve to a real, nameable corpus row — including the D2/g13 case the author had flagged as IRREDUCIBLE and the audit found actually resolves |
| 13 | Targeting satisfied | **N/A** — no Professor's Note exists yet; Papers 1-3 are all unscored |

**Shape distribution** (ARCHETYPE-LEDGER.md's own hard floor 4 / ceiling 11, not one of the 13
numbered checks but verified anyway): S1 11, S2 8, S3 11, S4 5, S5 7, S6 6, S7 9, S8 6 — all within
bounds after the pre-dispatch rebalance described above. **Direction-inversion floor**: all 8 shapes
carry ≥2 inverted-direction items (S1:3, S2:2, S3:2, S4:2, S5:2, S6:2, S7:2, S8:2 = 17 total),
spread across 6 of 7 domains.

**`t1Alt` resolution rate: 62/63 (98%)** — see finding 10 above for the caveat on reading this as a
trend.

### Confirmed-weakness check
N/A — no prior SCORED paper exists (Papers 1-3 are all generated but not yet sat).

### Findings
Ranked by evidence strength — process/engine findings belong in `GENERATION-INTELLIGENCE.md` Session
7 in full; summarized here for the record:
1. **The independent grounding audit overturned an author's own IRREDUCIBLE self-assessment for the
   first time** (D2/g13) — the strongest evidence yet that the audit's value is specifically in
   being blind to the author's reasoning, not merely in re-checking arithmetic.
2. **Ram's approved D2 direction-inverted-reuse mechanism failed its own genuineness test on one of
   its five uses** (g19, a cosmetic restate) and was caught before shipping — validates that the
   mechanism needs the audit's scrutiny applied to it specifically, not just assumed sound because
   Ram approved the general approach.
3. **A parallel, lower-severity version of D2's supply problem exists in D7's section 7.2**: its
   multi-response item structurally duplicated Paper 1's own item at the same two facets, because
   only two positive mechanism rows exist there to pair. Worth watching whether this recurs on future
   D7 multi-response items, though D7's overall facet count (39) is not remotely as constrained as
   D2's (18).
4. **The `cite` field gap is a new, previously-unseen failure mode**: a schema field a paper's own
   shared brief omits doesn't fail the mechanized gate (it wasn't in `validateItems()`'s required
   list either, until this paper), doesn't fail dedup or family checks, and is invisible in the raw
   JSON unless you know to look for it — it only surfaces by actually using the rendered page. This
   is the concrete argument for §4f/step-9's browser-click requirement being load-bearing, not
   ceremonial.
5. **Family-cap and shape-budget rebalancing needed more rounds than any prior paper** (2 rounds
   pre-dispatch for shape, 2 rounds post-audit for family caps) — directly caused by the volume of
   audit-driven content reworks this paper needed, each of which could shift either tally. Future
   papers with a heavy audit-fix cycle should expect to re-run both checks after every content
   rework, not just after the original assembly pass.
6. **The gate mechanization (Phase 6's Paper-4 milestone) is done for checks 10/11**; checks 2-9,
   12-13 remain one-off/manual. A natural next step for a future paper, not required by this one.

### Pace
N/A — not yet attempted.

### Professor's Note — Intent for Paper 5
Paper 4, like Papers 1-3, is a diagnostic with no prior scored paper to target — there is still no
Professor's Note to consume for Paper 5 either, unless Papers 1-4 get sat and scored before Paper 5
is generated. Structural items to carry forward regardless of score:
- **The D2 corpus-expansion decision is now due.** Per the orchestration prompt's own supply table,
  "Papers 1-5 are reachable on the corpus as it stands. Papers 6-10 are not." Paper 4 already needed
  the direction-inverted-reuse fallback for 5 of 8 D2 items, and one of those five failed its
  genuineness test on the first attempt. Paper 5 can likely repeat the same mechanism once more
  (D2's 18 facets each still support at most one more inverted slot), but Papers 6-10 cannot without
  the ~20 new decision-table rows `FACET-LEDGER.md` has flagged since Session 1. Raise this
  explicitly before Paper 6 is planned, not after.
- **Watch D7's section 7.2 the same way**: if a future paper's 7.2 multi-response item also
  duplicates an already-shipped mechanism pairing, that is a second data point suggesting D7 needs
  its own version of D2's supply conversation, on a much smaller scale.
- **The `t1Alt` 98% resolution rate should not be read as the new baseline** without a caveat: this
  paper had an unusually thorough fix cycle. Whether the rate holds without that much correction
  effort is worth checking on Paper 5.
- If Papers 1-4 get sat before Paper 5, apply Phase 7.1 in full for the first time this series.

---

## Paper 5 — GENERATED 2026-09-02, not yet attempted

**File:** `mock-exams/CCAR-P_MockTest-5_v1.html`
**Mode:** AUTHOR (63/63 items authored fresh from corpus facets, one direction-doubling reuse pair,
and one misconception-unit item repurposed as a fresh inverted anchor).
**Professor's Note / Insights Round consumed:** none — Papers 1-4 are all generated but none is
scored yet, so Paper 5 is a **fifth explicitly untargeted diagnostic**, confirmed with Ram before
generation started (per `Outputs/CCAR-P_Paper-5-Generation-Prompt_v1.md` §3, which named this the
strongest case yet for pausing to sit one first — Ram chose to proceed). No targeting triples exist
to satisfy or deliberately leave untargeted; Phase 7.1 rule 4 has no scored data to fire on.
**deepDive:** every item ships `deepDive: null`, per the standing Paper 2-onward rule.

### D2's facet-supply decision — Ram's approved corpus expansion, implemented

D2's decision-table facet supply was fully exhausted before this paper was planned (0/18 facets
fresh across Papers 1-4, all 9 misconception units spent). Before generating any D2 item, Ram was
asked to choose among (a) proceed with the ~13 facet-level reuse-inversion slots the fresh
bookkeeping actually found available, (b) expand the D2 corpus now, (c) temporarily lower D2's
quota, or (d) something else. **He chose (b), corpus expansion, matching the evidence the
generation prompt itself pointed toward.** Implemented same-session: 21 new decision-table rows
added to `CCAR-P_Domain-2_v1.md` across all 9 sections (F-2.1-04/05, F-2.2-05, F-2.3-04/05,
F-2.4-03/04, F-2.5-03/04, F-2.6-02/03/04, F-2.7-02/03/04, F-2.8-02/03/04, F-2.9-02/03/04),
`FACET-LEDGER.md` updated to match (D2: 18 → 39 facets; corpus total: 351 → 372). **D2 needed no
reuse-inversion or misconception fallback at all this paper** — all 8 D2 items are built from
genuinely fresh facets, three of them tested in direction-inverted form, the same as any other
domain. This is expected to hold for at least Paper 6 as well before D2's supply pressure returns.

Two smaller decisions, also confirmed before generation: **proceed as a fifth untargeted
diagnostic** rather than pause to sit an existing paper (see above), and **formalize
`ARCHETYPE-LEDGER.md`'s shape-budget floor/ceiling (F-31) as gate check 14** in `tools/run-gate.js`
— closing the gap that let Paper 2 ship a silent violation (S8 at 12, S7 at 3) undetected since
Paper 1.

### What actually happened during generation — the heaviest audit-and-fix cycle of any paper so far

1. **Central planning ran the same freshness-greedy algorithm as every prior paper, now unified
   across all 7 domains** (D2 no longer needed a hard-coded branch). Two objectives — O3.1 (section
   3.1) and O5.3 (section 5.8) — had every one of their own facets already used across Papers 1-4
   with no misconception unit left either. The standing "direction doubling" fallback (in force
   since Paper 4, documented in `FACET-LEDGER.md`) applied: these two items (g20, g44) reuse an
   already-shipped facet as an anchor but test the inverted direction.
2. **The shape-budget rebalance (F-31) fired a second time**, same as Paper 4: the raw freshness
   draw put S1 at 15 (over the ceiling of 11). Fixed pre-dispatch by moving 4 normal-direction items
   to a better-fitting shape (3.2→S8, 3.5→S6, 1.9→S4, 4.12→S6), each with a stated content reason,
   verified in-code before dispatch. Final tally: S1 11, S2 8, S3 6, S4 11, S5 6, S6 10, S7 5, S8 6
   — all within [4, 11].
3. **All 13 sub-batch dispatches succeeded on the first try, zero stalls** — the fifth consecutive
   clean run on the F-16/F-17 dispatch-granularity fix (D1×2, D2×2, D3×2, D4×2, D5×2, D6×2, D7×1,
   4-6 items each).
4. **A real planning bug surfaced from the sub-batches' own honest flagging, not from a mechanized
   check**: three items (D1 g9, D4 g34, D6 g52) were assigned `direction:"inverted"` in the central
   plan, but the freshness-greedy algorithm had actually placed all three on that section's
   misconception-unit fallback — and the shared brief states misconception items never invert
   (there is no clean "opposite direction" of a stated wrong belief). All three sub-batch agents
   caught the conflict themselves, followed the explicit inversion guidance anyway, and flagged it
   for confirmation rather than silently picking an interpretation. **Resolution: kept as
   direction-inverted** — each authored a fresh, section-grounded scenario using the misconception
   id as a scenario anchor rather than literally inverting the boxed Misconception paragraph, and
   the independent audit confirmed all three genuinely differ from their section's normal lesson.
   Recorded as a new finding for Paper 6 onward: check `plan-raw.json`'s `kind` field before
   assigning a direction override, so this interaction is anticipated rather than discovered after
   dispatch.
5. **Assembly caught the usual paper-wide problems, at higher volume than any prior paper**: the
   `ARCHITECTED` family cap was breached twice during the session (22, then 20 after a merge) before
   settling at exactly 19 — the ceiling. Two multi-response stems (g28, g36) needed their "select
   two" phrasing corrected to match the mechanized regex. One option-spread violation (g37) and one
   word-cap overrun (g57) were fixed. **Seven stem-Jaccard collisions ≥0.30 against Papers 2-4**
   were found and fixed by reworking the colliding stems' surface details (industry, numbers,
   illustration) while preserving each item's underlying lesson — one of them (g45) had
   inadvertently reinvented Paper 4's own g45 scenario almost exactly.
6. **The independent grounding audit (7 fresh agents, one per domain, blind to the sub-batches' own
   notes) found materially more than any prior paper — the clearest evidence yet that the audit's
   value scales with the volume of construction work a paper needs, not just with paper count.**
   Findings, by severity:
   - **One item (D5 g44) was a CONFIRMED cosmetic restate** — the exact failure mode this project
     has been watching for since F-27/F-28: the "inverted" item taught the identical
     route-by-confidence-and-consequence lesson its anchor's own normal-direction scenario already
     teaches, just with fraud/SLA nouns substituted for document/volume nouns. Reworked to anchor on
     the section's *other* row instead (genuinely low-volume, uniformly high-consequence work, where
     blanket review actually is correct) — the true opposite lesson, not a nearby restate.
   - **Two items (D5 g45, D6 g53) were IRREDUCIBLE as originally constructed** — both rested on a
     mechanism invented in this session's own planning that does not exist anywhere in the cited
     corpus section (a fabricated "scoped infrastructure-layer exception" for g45; a case-mix-
     confound scenario with no matching row in g53's cited section). Both were fully reworked
     against the section's actual, real decision-table mechanism rather than patched.
   - **One item (D5 g49) rested on the same class of invented mechanism** (a FedRAMP "scoped
     exception" the corpus explicitly forecloses — its own Misconception block states no
     configuration makes a deployment compliant, and the word "exception" appears nowhere in
     Domain 5). Resolved by flipping the item to `direction:"normal"` and moving the correct answer
     to the option that already matched the corpus's real, stated resolution (comply, or keep the
     data out) — this is not a defect in the direction-doubling mechanism itself, just evidence that
     an S8 inversion cannot be manufactured where the underlying section is genuinely absolutist.
   - **One item (D7 g63) was IRREDUCIBLE as constructed for an unrelated reason**: its correct
     answer's justification (a CLI changelog check) appeared nowhere in Domain 7 at all, and
     collided with section 7.7's own already-established, differently-answered version of a
     similar-sounding scenario. Re-authored around section 7.1's own configuration-scope content,
     using section 7.7's real `/context`-comparison mechanism as the verification action rather than
     inventing a new one.
   - **Two citation/objective mismatches** (D4 g34, D6 g51) where an item's actual tested content
     traced cleanly to a *different* section than the one it was cited to. g34 was rewritten to
     genuinely fit its assigned section 4.9 instead of relocating (section 4.10 was already at its
     2-item cap); g51 was re-cited to section 6.6, which is where its attestation-requirement content
     actually lives.
   - **One item (D3 g28) was judged genuinely IRREDUCIBLE on structural-duplication grounds, not a
     T1 failure** — section 3.3 does not carry enough distinct row-pairs to guarantee a
     non-repetitive multi-response item at a fifth time of asking; any 3.3 multi-item from here is
     structurally forced onto the same identity-propagation-plus-query-filter pairing. Documented,
     not forced into a rewrite — a smaller-scale echo of D2's own pre-expansion problem.
   - **A parallel, lower-severity version of D7's own known section-7.2 supply-thinness (F-29) fired
     again**: this paper's 7.2 multi-response item necessarily reused the same two-mechanism pairing
     Papers 1 and 4 both used (only two positive mechanism rows exist there), though the auditor
     judged the concrete illustration distinct enough to avoid reading as a reskin. One coincidental
     match (identical distractor-family fingerprint against Paper 1 specifically) was flagged for
     awareness, not as a proven duplication.
   - **Roughly a dozen smaller, single-field fixes** across every domain — mismatched family tags
     against this project's own established usage (6 in D1 alone), self-contradictory `t1Clause`
     text that didn't actually justify its `t1Alt` (D3 g20's whyRight mechanism, D4 g35, D5 g43/g47,
     D6 g54's stale wording, D7 g61/g62), and one numeric self-contradiction between a stem and its
     own options (D6 g55) — all fixed directly, each re-verified against the corpus fresh rather than
     patched on the audit's word alone.
7. **Applying these fixes required two further correction rounds of my own**, each caught only by
   re-running the mechanized gate, not by inspection — matching Paper 4's own standing lesson that a
   fix is provisional until it clears the same gate everything else goes through. First: merging the
   5 domains' fix batches reintroduced the `ARCHITECTED` cap violation (a retagged option from the
   D5 g49 rework pushed it back to 20) and a duplicate-family violation on an already-fixed D1 item
   (g10, from an earlier pass in this same session) — both corrected and re-verified. Second: one
   fix-agent's rebuilt item (D7 g62) silently reverted an already-applied Jaccard-collision fix to
   its stem while correctly applying its own assigned fix elsewhere on the same item — caught only
   by re-running the full gate a final time, not by re-reading the fix output. A facet-reuse cap
   violation was also caught this way: the D6 fix agent's chosen re-citation for g51 used a facet
   (`F-6.6-04`) already at its 2-use historical cap, requiring a second facet substitution
   (`F-6.6-01`) before the gate cleared.
8. **`t1Alt` resolution rate: 63/63 (100%) after the full audit-fix cycle** — the first paper in this
   series with zero documented IRREDUCIBLE Professional-tier exceptions. This should not be read as
   evidence the underlying construction got easier: this paper needed by far the heaviest
   correction cycle of any paper so far (17 items touched by the audit's own findings, out of 63),
   and the honest comparison is "how much correction effort produced a clean paper," not "how clean
   the first draft was." G28's structural-duplication finding and D7's F-29 echo are dedup-adjacent
   documented limitations, not Professional-tier (T1-T4) failures, and are recorded separately.

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
All **38 of 38** official objectives covered (floor pass of 1 item each, plus a discretionary pass,
cap 3/objective, actual max 3). D2 drew on 7 of its 9 sections from genuinely fresh post-expansion
facets (sections 2.5 and 2.9 untouched this paper, left for Paper 6's supply).

### Fidelity gate — full result
Checks 1, 10, 11, and — new this paper — **14** are mechanized in `tools/run-gate.js`. Checks 5, 7,
12 verified via `_PAPER5-STAGING/extra-checks.js`; 2-4, 6, 8-9, 13 checked directly against the
assembled items and the plan.

| # | Check | Result |
|---|---|---|
| 1 | `validateItems()` structural | **PASS** — 63 items, sequential `g`, every non-key option has `whyWrong`, every item has `whyRight`, all 8 multi-response stems match the literal `/select (two\|three\|\d)/i` pattern after 2 rewrites, `deepDive:null` accepted, `cite` present on all 63 |
| 2 | Domain quota | **PASS** — exact match, table above |
| 3 | Per-item domain vs citation | **PASS** — the D4/g34 and D6/g51 citation mismatches the independent audit found are both fixed (g34 reworked to fit its own cited section; g51 re-cited to the section its content actually matches) |
| 4 | Cited sections exist | **PASS** — every section resolves in `CCAR-P_Objective-Map_v1.md`'s real section list; every grounding auditor read the cited section directly, including D2's 9 sections' new 2026-09-01 tables |
| 5 | Objective coverage | **PASS** — 38/38, max 3 per objective |
| 6 | Correct-answer letter tally | **PASS on the numeric floor/ceiling** — A13 / B14 / C15 / D13, all within [12,16]. This deviates by one letter each from the §5.1 pre-plan (A14/B14/C14/D13, short letter D) — a direct, traceable consequence of the D5/g49 audit-driven direction flip (its correct answer moved from A to C for content-correctness reasons, not for balance). Matches Paper 4's own precedent that an audit-driven content fix can shift the tally within the gate's actual tolerance without that counting as a failure |
| 7 | Multi-response pairs | **PASS** — AB×2, CD×2, AC×1, BD×1, AD×1, BC×1 across the 8 multi items; no pair exceeds the cap of 2; all 8 stems state their count |
| 8 | Style budget | **PASS** on hard caps (stem ≤45, option ≤20, spread ≤8) after fixing 1 spread violation and 2 word-cap overruns found during the fix cycle. 29 items sit outside the 28–40 soft band (median 43) — comparable to Paper 4's 30, not a gate failure since the band is guidance |
| 9 | Framing and token rate | **PASS** — 0 invented company/product/persona names (confirmed by all 7 independent audits plus a final programmatic scan). Inline code/config tokens 4.4% of options (cap 15%), 0 in D1/D5/D6 |
| 10 | Distractor families | **PASS**, mechanized — WRONG-AXIS 34, HALF-MOVE 31, EVIDENCE-MISMATCH 31 (floor 15), DISCARD 28, REPAIR 16, ARCHITECTED 19 (ceiling 19, exact), OVERSPEC 11, DETECTIVE-FOR-PREVENTIVE 11 (floor 9), of 181 total distractors. Needed 2 relabeling rounds during assembly plus 2 more during the audit-fix merge to hold the ceiling exactly at 19 while fixing genuine family-tag inaccuracies the audit found (6 in D1 alone) |
| 11 | Dedup | **PASS**, mechanized — 0 stem pairs ≥0.30 Jaccard against 300 seeded+prior stems or within-paper, after fixing 7 collisions (see generation story). 0 `lessonKey` collisions, recomputed for the 6 items whose underlying answer changed during the audit-fix cycle. 0 `(shape, section, facet)` triple used more than twice historically, after one facet substitution (D6 g51: `F-6.6-04`→`F-6.6-01`) caught the cap by re-running this check, not by inspection |
| 12 | Professional-tier floor | **PASS with 0 documented IRREDUCIBLE exceptions** — the first paper in this series to clear T1-T4 on every item. See the generation story for why this reflects audit-fix effort, not first-draft cleanliness. One dedup-adjacent structural limitation (D3 g28, section 3.3's own supply thinness) is documented separately and does not count against this check |
| 13 | Targeting satisfied | **N/A** — no Professor's Note exists yet; Papers 1-4 are all unscored |
| 14 | **Shape-budget floor 4 / ceiling 11** | **PASS**, mechanized for the first time this paper (F-31, Ram's decision) — S1 11, S2 8, S3 6, S4 11, S5 6, S6 10, S7 5, S8 6, all within bounds after the pre-dispatch rebalance |

**Shape distribution**: S1 11, S2 8, S3 6, S4 11, S5 6, S6 10, S7 5, S8 6 — all within [4, 11].
**Direction-inversion floor**: all 8 shapes carry exactly 2 inverted-direction items (16 total,
one fewer than the 17 originally planned — D5's g49 was flipped back to normal during the audit,
see the generation story), spread across all 7 domains (max 3 per domain: D1, D2, D5, D6 each carry
3; D3 carries 2; D4 and D7 carry 1 each).

**`t1Alt` resolution rate: 63/63 (100%)** — see finding 8 above for the caveat on reading this as a
trend rather than a reflection of correction effort.

### Confirmed-weakness check
N/A — no prior SCORED paper exists (Papers 1-4 are all generated but not yet sat).

### Findings
Ranked by evidence strength — process/engine findings belong in `GENERATION-INTELLIGENCE.md` Session
8 in full; summarized here for the record:
1. **The D2 corpus-expansion decision resolved the series' longest-standing structural risk.** 21
   new rows closed a gap flagged since Session 1 (F-01). D2 needed zero fallback mechanism this
   paper — the first time since Paper 2 that every D2 item came from a genuinely fresh facet.
2. **A planning-stage interaction between direction overrides and the misconception fallback
   produced three items that technically break the shared brief's own stated rule, and all three
   were caught by the sub-batches' own honest flagging, not by a mechanized check or the central
   plan's own validation.** This is now a documented, accepted pattern (a misconception-fallback
   slot can supply a genuine inverted item if the audit confirms it), but the *planning* gap that
   let it happen unnoticed should close before Paper 6 (see the process fix noted above).
3. **The independent grounding audit found and fixed one confirmed cosmetic restate (D5 g44) and
   two IRREDUCIBLE-as-constructed items resting on an invented mechanism (D5 g45, D5 g49) — all
   three in the same domain, all three stemming from this session's own planning-stage inversion
   guidance reaching further than the cited corpus sections actually support.** D5 is now the
   domain to watch most closely on Paper 6's own audit — not because its corpus is thinner than
   others, but because this session's own inversion-guidance drafting was weakest there.
4. **A fix is provisional until it clears the same gate everything else goes through — reconfirmed
   at a new scale.** Merging five domains' independent fix batches reintroduced two already-fixed
   violations (a family-cap breach, a duplicate-family tag) and one fix agent's rebuild silently
   reverted an unrelated, already-applied stem fix on the same item. All three were caught only by
   re-running the full gate after the merge, not by re-reading any individual fix's own summary.
5. **The `t1Alt` IRREDUCIBLE rate hit 0/63 for the first time**, but this is the single most
   correction-heavy paper in the series (17 of 63 items touched by audit findings) — read this as
   evidence the audit-and-fix cycle works at scale, not as a claim that authoring quality improved.
6. **Gate check 14 (shape-budget) is now mechanized and already caught what it was built to catch**
   — the same S1-overflow pattern Paper 4 hit was rebalanced pre-dispatch again this paper, and the
   check itself passed cleanly once the rebalance was in place.

### Pace
N/A — not yet attempted.

### Professor's Note — Intent for Paper 6
Paper 5, like Papers 1-4, is a diagnostic with no prior scored paper to target — there is still no
Professor's Note to consume for Paper 6 either, unless Papers 1-5 get sat and scored before Paper 6
is generated. Structural items to carry forward regardless of score:
- **D2's corpus expansion held for this paper; re-check its remaining supply before Paper 6.** 39
  facets against an 8-item/paper quota gives meaningfully more runway than the pre-expansion 18, but
  extract fresh usage from the shipped HTML (per standing practice, F-21) rather than assuming
  supply — sections 2.5 and 2.9 were untouched this paper and should be prioritized.
- **Check `plan-raw.json`'s `kind` field before assigning any `DIRECTION_OVERRIDES` target**, so a
  direction-override never lands on a misconception-fallback slot unnoticed the way it did three
  times this paper (caught only by the sub-batches' own flagging).
- **D5 needs closer attention during Paper 6's own planning stage**, not just its audit — three of
  this paper's most serious findings originated in D5-specific inversion guidance that reached past
  what the cited corpus sections actually support. Ground every D5 `invGuidance` in a directly-quoted
  corpus row before dispatch, not a paraphrased summary of the section's general theme.
- **If Papers 1-5 get sat before Paper 6, apply Phase 7.1 in full for the first time this series** —
  this is now the fifth consecutive deferral, and the series table names Paper 5 as where the
  confirmed-weakness mechanism was first eligible to fire twice running, which still has no data to
  work with.

---

## Insights Rounds

*None yet. First one fires at 3 scored papers.*
