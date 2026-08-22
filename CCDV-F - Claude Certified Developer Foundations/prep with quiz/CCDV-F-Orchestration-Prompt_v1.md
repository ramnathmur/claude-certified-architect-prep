# CCDV-F Mock Exam Orchestration Prompt — v1

Ported from `..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\CCA-Orchestration-Prompt_v10.md`,
which generated fourteen Foundations papers. Stripped to the phases that earned their place and
re-pointed at CCDV-F's confirmed blueprint.

**Quotas below are verified** against `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` (v1.0, July 2026).
This prompt is unblocked once the corpus exists.

---

## The paper being simulated

| | |
|---|---|
| Items | **53** |
| Time | **120 minutes** |
| Format | Multiple-choice and multiple-response, **standalone items — no scenario blocks**. Each item states how many responses to select |
| Pass | 720 scaled, on 100–1,000. **No domain floor** — total score only |

### Domain quota — 53 items

| D | Domain | % | Items |
|---|---|---|---|
| 1 | Agents and Workflows | 14.7 | **8** |
| 2 | Applications and Integration | 33.1 | **17** |
| 3 | Claude Code | 3.1 | **2** |
| 4 | Eval, Testing, and Debugging | 2.6 | **1** |
| 5 | Model Selection and Optimization | 16.8 | **9** |
| 6 | Prompt and Context Engineering | 11.0 | **6** |
| 7 | Security and Safety | 8.1 | **4** |
| 8 | Tools and MCPs | 10.6 | **6** |
| | | | **53** |

*Exact weights give 7.8 / 17.5 / 1.6 / 1.4 / 8.9 / 5.8 / 4.3 / 5.6. The rounding above is one
defensible allocation; state in the generation entry which rounding a paper used, and vary it across
papers so the small domains are not always rounded the same way. D3 and D4 are 1–2 items each — over a
run of papers they must sometimes be 1 and sometimes 2.*

Within a domain, distribute across the **published skills** in proportion to their weights. The section
map is in `CCDV-F_Corpus-Index_v1.md`.

---

## Phase 0 — Preflight (abort conditions)

Abort and report if any of these fail:

1. `CCDV-F_Corpus-Index_v1.md` lists any section needed for this paper's quota as `not created`.
2. The requested paper number already exists in `mock-exams/`.
3. `DASHBOARD-DATA.jsonl` has an entry for this paper number.
4. `../EXAM-FACTS_v1.md` records a guide version later than the one this prompt's quota is built on
   (v1.0). If the guide has moved, re-derive the quota before generating.

## Phase 1 — Read state

Read, in this order:
1. `EXAM-LOG.md` — every `SCORED` entry, sorted **by attempt date**, not paper number.
2. The most recent **Professor's Note — Intent for Paper N** (the note written after the most recently
   *attempted* paper, which is not necessarily the highest-numbered one).
3. The most recent Insights Round, if one is more recent than that note.

If the latest Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
generation entry and state which one won and why. Do not silently prefer one.

## Phase 2 — Set the distribution

1. **Base quota** = the table above, with the rounding choice recorded.
2. **Carry-over loading on paper 1.** The six CCAR-F 0% objectives touch §1.1, §1.2, §1.3, §2.6, §3.1
   and §6.1 — roughly 17% of the paper. Paper 1 deliberately over-tests them. Record the loading and
   revert it from paper 2.
3. **Confirmed-weakness adjustment.** If a domain is confirmed weak (unambiguously weakest on two
   consecutive papers *by attempt date*), raise its quota by 2–4 items and lower the strongest domain by
   the same. Record the adjustment and revert it on the following paper. **Do not apply this to D3 or
   D4** — at 1–2 items each, a single miss makes them "weakest" as noise, not signal.
4. **Section targeting.** From the Professor's Note, list the specific sections to test and, for each,
   **the direction of the error being retested**. A repeat miss retested from the same direction proves
   nothing — CCAR-F closed `tool_choice` in one direction and it reopened in the other within a week.
5. **Format split.** Multiple-response items get deliberate weight — they were the largest scoring leak
   on CCAR-F. **Every multiple-response stem must state how many responses to select**, because the
   real exam does.

## Phase 3 — Generate

- Generate **only** from `CCDV-F_Domain-N_v1.md` files. Never from notes, the web, or memory.
- Every question carries: `domain`, `section` (the §N.M skill), `format`, the correct answer,
  `whyRight`, and a `whyWrong` for each distractor.
- **Item shape follows the official samples.** A short scenario that states a constraint, then four
  options. The constraint is what decides the answer — cost-primary, latency-tolerant, untrusted input,
  reusable across apps, maintained independently. A stem with no constraint has no correct answer.
- **Distractors should mostly be legitimate techniques that do not match the stated constraint.** In
  official Sample 1, parallel sync calls, lowering `max_tokens` and downsizing the model are all real
  things a developer does — they just do not answer the question asked.
- Draw from **different** distractor families per item. Ten are defined in
  `CCDV-F_Domain-Template_v1.md`: six from CCAR-F plus IRRELEVANT-LEVER / UNENFORCEABLE /
  BIGGER-HAMMER / FALSE-CAPABILITY, taken from the guide's own sample rationales.
- **Do not write syntax-recall items.** No official sample shows code, and the format is selection, not
  production. Code belongs in a stem only where the decision is about the code — schema shape,
  defensive parsing, error-handling strategy.

## Phase 4 — Fidelity gate

Reject the paper and regenerate if any check fails:

1. Domain tallies match the intended quota, and skill-level distribution within each domain is
   proportional to the published skill weights.
2. **Each question's `domain` and `section` tags match the citations in its own `whyRight`/`whyWrong`.**
   A CCAR-F paper shipped with a question tagged D3 whose every citation was D4 — it corrupted the
   domain breakdown and nearly triggered a false confirmed-weakness. Check per question.
3. Every cited section exists in the corpus file it claims.
4. No question is a near-duplicate of one in an earlier paper unless it is a deliberate retest, and
   deliberate retests are listed in the generation entry.
5. Distractor families are varied within each question.
6. Every targeted section from the Professor's Note is actually covered.
7. **Every stem states a constraint** that decides between the options.
8. **Every multiple-response item states its response count.**
9. **No item is answerable from the stem alone**, and none turns purely on recalling a name.

## Phase 5 — Write the generation entry

Append to `EXAM-LOG.md`:
- Which Professor's Note and Insights Round were consumed.
- The quota used, the rounding choice, and any carry-over or confirmed-weakness adjustment with its
  justification.
- Sections deliberately targeted, and the direction of each retest.
- Sections deliberately left untargeted — untargeted recovery is stronger evidence than targeted
  recovery, and it can only be claimed if the omission was recorded up front.

Then write the `DASHBOARD-DATA.jsonl` line with null scores, per `DASHBOARD-SCHEMA.md`.

## Phase 6 — After the sitting

1. Score from results-json. Split single-answer from multiple-response.
2. Log every miss with section, format, time, picked, correct, why it was wrong, and **`RECALL` or
   `CONCEPT`** (see `EXAM-LOG.md`). Every miss gets a tag.
3. Run the confirmed-weakness check against the paper attempted immediately before this one **by date**.
   A tie records `false`. Skip D3 and D4 — too small to be signal.
4. Classify each miss by distractor family. Families that recur are habits, and habits need a different
   remedy from knowledge gaps.
5. **Check the tripwire.** If `RECALL` misses exceed a quarter of all misses across the last three
   papers, the judgement-shaped assumption is wrong — say so in the log and escalate to the roadmap.
6. Note pace: misses slower than the paper average are decision errors, not time pressure. On CCAR-F
   every single miss cluster turned out to be considered-and-wrong.
7. Write the Professor's Note for the next paper, ranked by evidence strength.
8. If this scoring brings the count to a multiple of 3, run an Insights Round.

---

## Deliberately not ported

- **The scenario-block architecture.** CCAR-F drew 4 scenarios of 15 items from a pool of 6. **The
  CCDV-F guide confirms standalone items**, so this is not a deferred question — it is settled and the
  phase is gone for good.
- **The `archetype_gate.py` tooling.** Rebuild if paper volume justifies it. On a target of ≥8 papers it
  might.

## A note on the small domains

D3 (Claude Code, 3.1%) and D4 (Eval/Testing/Debugging, 2.6%) are **1–2 items each**. Two consequences:

- **They cannot be measured paper-by-paper.** A 0/2 is not a trend. Judge them across the whole run, not
  within a paper, and never let them trigger a confirmed-weakness quota bump.
- **They still matter more than their weight for Ram**, because the CCAR-F 0% objectives live there.
  The fix is corpus coverage and targeted retests across many papers — not quota inflation, which would
  make the paper unrepresentative of the real thing.
