# CCAO-F Mock Exam Orchestration Prompt — v1

Ported from `..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\CCA-Orchestration-Prompt_v10.md`,
which generated fourteen Foundations papers. Stripped to the phases that earned their place and
re-pointed at CCAO-F.

**Do not run this until Phase 0 closes.** Domain quotas come from the official exam guide. Running it
against the community weightings would generate a paper testing the wrong distribution — and the
CCAO-F weightings, though well corroborated, are still an inference from lesson minutes.

---

## Phase 0 — Preflight (abort conditions)

Abort and report if any of these fail:

1. `../EXAM-FACTS_v1.md` shows unresolved ⚠️ rows for domain list, weightings, or item count.
2. `CCAO-F_Corpus-Index_v1.md` lists any domain file as `not created`.
3. The requested paper number already exists in `mock-exams/`.
4. `DASHBOARD-DATA.jsonl` has an entry for this paper number.

## Phase 1 — Read state

Read, in this order:
1. `EXAM-LOG.md` — every `SCORED` entry, sorted **by attempt date**, not paper number.
2. The most recent **Professor's Note — Intent for Paper N** (the note written after the most recently
   *attempted* paper, which is not necessarily the highest-numbered one).
3. The most recent Insights Round, if one is more recent than that note.
4. `../EXAM-FACTS_v1.md` for the confirmed quotas.

If the latest Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
generation entry and state which one won and why. Do not silently prefer one.

## Phase 2 — Set the distribution

1. **Base quota** = the official domain weightings applied to the confirmed item count.
2. **Gap loading on early papers.** Papers 1 and 2 deliberately over-weight Product and Model Selection
   and Configuration and Knowledge Management. Those two domains carry no ported material, and the
   point of an early paper is to find out how bad they are, not to produce a comfortable score. Record
   the loading and revert it from paper 3.
3. **Confirmed-weakness adjustment.** If a domain is confirmed weak (unambiguously weakest on two
   consecutive papers *by attempt date*), raise its quota by 2–4 items and lower the strongest domain
   by the same. Record the adjustment and revert it on the following paper.
4. **Section targeting.** From the Professor's Note, list the specific sections to test and, for each,
   **the direction of the error being retested**. A repeat miss retested from the same direction proves
   nothing — CCAR-F closed `tool_choice` in one direction and it reopened in the other within a week.
5. **Format split.** Match the confirmed single-answer / multiple-response ratio. Multiple-response
   items get deliberate weight: they were the largest scoring leak on CCAR-F.

## Phase 3 — Generate

- Generate **only** from `CCAO-F_Domain-N_v1.md` files. Never from notes, the web, or memory.
- Every question carries: `domain`, `section`, `format`, the correct answer, `whyRight`, and a
  `whyWrong` for each distractor.
- Distractors are drawn from **different** families (OVERSPEC / DISCARD / REPAIR / ARCHITECTED /
  HALF-MOVE / WRONG-AXIS — see `CCAO-F_Domain-Template_v1.md`). Three flavours of the same wrong answer
  make an item that tests nothing.
- **Associate-tier framing.** The stem is a desk problem: a report to check before it goes to a client,
  a team that needs a shared workspace, a document too long to paste. No API parameters, no SDK calls,
  no terminal. A stem that requires code to answer is out of scope for this exam.
- **Over-supply the ARCHITECTED distractor family.** Ram holds a higher credential than this exam
  tests; the more-architected-sounding option needs to be wrong often enough to break the reflex.

## Phase 4 — Fidelity gate

Reject the paper and regenerate if any check fails:

1. Domain tallies match the intended quota.
2. **Each question's `domain` tag matches the citations in its own `whyRight`/`whyWrong`.** A CCAR-F
   paper shipped with a question tagged D3 whose every citation was D4 — it corrupted the domain
   breakdown and nearly triggered a false confirmed-weakness. Check per question, not just per block.
3. Every cited section exists in the corpus file it claims.
4. No question is a near-duplicate of one in an earlier paper unless it is a deliberate retest, and
   deliberate retests are listed in the generation entry.
5. Distractor families are varied within each question.
6. Every targeted section from the Professor's Note is actually covered.
7. **Altitude check.** No question requires API, SDK, or command-line knowledge to answer. Any that do
   are rewritten or cut — they test CCAR-F, not CCAO-F.

## Phase 5 — Write the generation entry

Append to `EXAM-LOG.md`:
- Which Professor's Note and Insights Round were consumed.
- The quota used, plus any gap loading or confirmed-weakness adjustment with its justification.
- Sections deliberately targeted, and the direction of each retest.
- Sections deliberately left untargeted — untargeted recovery is stronger evidence than targeted
  recovery, and it can only be claimed if the omission was recorded up front.

Then write the `DASHBOARD-DATA.jsonl` line with null scores, per `DASHBOARD-SCHEMA.md`.

## Phase 6 — After the sitting

1. Score from results-json. Split single-answer from multiple-response.
2. Log every miss with section, format, time, picked, correct, why it was wrong, and whether it was an
   `ALTITUDE` miss (see `EXAM-LOG.md` convention 8).
3. Run the confirmed-weakness check against the paper attempted immediately before this one **by date**.
   A tie records `false`.
4. Classify each miss by distractor family. Families that recur are habits, and habits need a different
   remedy from knowledge gaps. If `ALTITUDE` misses cluster, the corpus is pitched too high — fix the
   corpus, not the revision plan.
5. Note pace: misses slower than the paper average are decision errors, not time pressure. On CCAR-F
   every single miss cluster turned out to be considered-and-wrong.
6. Write the Professor's Note for the next paper, ranked by evidence strength.
7. If this scoring brings the count to a multiple of 3, run an Insights Round.

---

## Deliberately not ported

- **The scenario-block architecture.** CCAR-F drew 4 scenarios of 15 items from a pool of 6. The
  community source for CCAO-F describes standalone items and does not mention blocks. Unresolved — see
  `CCAO-F_Corpus-Index_v1.md`. Add this phase back if the guide says blocks exist.
- **The `archetype_gate.py` tooling.** Rebuild only if paper volume justifies it. On a 4–6 paper plan
  it will not.
