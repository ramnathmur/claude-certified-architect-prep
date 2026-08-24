# CCAR-P Mock Exam Orchestration Prompt — v1

Ported from `Projects\Claude Certified Architect Prep\prep with quiz\CCA-Orchestration-Prompt_v10.md`,
which generated fourteen Foundations papers. Stripped to the phases that earned their place and
re-pointed at CCAR-P.

**Do not run this until Phase 0 closes.** Domain quotas come from the official exam guide. Running it
against the community weightings would generate a paper testing the wrong distribution.

---

## Phase 0 — Preflight (abort conditions)

Abort and report if any of these fail:

1. `../EXAM-FACTS_v1.md` shows unresolved ⚠️ rows for domain list, weightings, or item count.
2. `CCAR-P_Corpus-Index_v1.md` lists any domain file as `not created`.
3. The requested paper number already exists in `mock-exams/`.
4. `DASHBOARD-DATA.jsonl` has an entry for this paper number.

## Phase 1 — Read state

Read, in this order:
1. `EXAM-LOG.md` — every `SCORED` entry, sorted **by attempt date**, not paper number.
2. The most recent **Professor's Note — Intent for Paper N** (the note written after the most
   recently *attempted* paper, which is not necessarily the highest-numbered one).
3. The most recent Insights Round, if one is more recent than that note.
4. `../EXAM-FACTS_v1.md` for the confirmed quotas.

If the latest Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
generation entry and state which one won and why. Do not silently prefer one.

## Phase 2 — Set the distribution

1. **Base quota** = the official domain weightings applied to the confirmed item count.
2. **Confirmed-weakness adjustment.** If a domain is confirmed weak (unambiguously weakest on two
   consecutive papers *by attempt date*), raise its quota by 2–4 items and lower the strongest
   domain by the same. Record the adjustment and revert it on the following paper.
3. **Section targeting.** From the Professor's Note, list the specific sections to test and, for each,
   **the direction of the error being retested**. A repeat miss retested from the same direction
   proves nothing — Foundations closed `tool_choice` in one direction and it reopened in the other
   within a week.
4. **Format split.** Match the confirmed single-answer / multiple-response ratio. Multiple-response
   items get deliberate weight: they were the largest scoring leak on Foundations.

## Phase 3 — Generate

- Generate **only** from `CCAR-P_Domain-N_v1.md` files. Never from notes, the web, or memory.
- Every question carries: `domain`, `section`, `format`, the correct answer, `whyRight`, and a
  `whyWrong` for each distractor.
- Distractors are drawn from **different** families (OVERSPEC / DISCARD / REPAIR / ARCHITECTED /
  HALF-MOVE / WRONG-AXIS — see `CCAR-P_Domain-Template_v1.md`). Three flavours of the same wrong
  answer make an item that tests nothing.
- Professional-tier framing: the stem should carry a production constraint — volume, cost, latency,
  a regulator, a stakeholder who has to approve it. A stem that works unchanged on a Foundations
  paper is pitched a tier too low.

## Phase 4 — Fidelity gate

Reject the paper and regenerate if any check fails:

1. Domain tallies match the intended quota.
2. **Each question's `domain` tag matches the citations in its own `whyRight`/`whyWrong`.**
   A Foundations paper shipped with a question tagged D3 whose every citation was D4 — it corrupted
   the domain breakdown and nearly triggered a false confirmed-weakness. Check per question, not just
   per block.
3. Every cited section exists in the corpus file it claims.
4. No question is a near-duplicate of one in an earlier paper unless it is a deliberate retest, and
   deliberate retests are listed in the generation entry.
5. Distractor families are varied within each question.
6. Every targeted section from the Professor's Note is actually covered.

## Phase 5 — Write the generation entry

Append to `EXAM-LOG.md`:
- Which Professor's Note and Insights Round were consumed.
- The quota used, and any confirmed-weakness adjustment with its justification.
- Sections deliberately targeted, and the direction of each retest.
- Sections deliberately left untargeted — untargeted recovery is stronger evidence than targeted
  recovery, and it can only be claimed if the omission was recorded up front.

Then write the `DASHBOARD-DATA.jsonl` line with null scores, per `DASHBOARD-SCHEMA.md`.

## Phase 6 — After the sitting

1. Score from results-json. Split single-answer from multiple-response.
2. Log every miss with section, format, time, picked, correct, and why it was wrong.
3. Run the confirmed-weakness check against the paper attempted immediately before this one **by
   date**. A tie records `false`.
4. Classify each miss by distractor family. Families that recur are habits, and habits need a
   different remedy from knowledge gaps.
5. Note pace: misses slower than the paper average are decision errors, not time pressure. On
   Foundations every single miss cluster turned out to be considered-and-wrong.
6. Write the Professor's Note for the next paper, ranked by evidence strength.
7. If this scoring brings the count to a multiple of 3, run an Insights Round.

---

## Deliberately not ported

- The scenario-block architecture. Foundations drew 4 scenarios of 15 items from a pool of 6. Whether
  CCAR-P has any block structure is unresolved — see the contradiction logged in
  `CCAR-P_Corpus-Index_v1.md`. Add this phase back once the guide settles it.
- The `archetype_gate.py` tooling. Rebuild only if paper volume justifies it.
