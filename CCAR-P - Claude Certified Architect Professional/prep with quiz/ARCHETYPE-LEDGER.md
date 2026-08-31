# CCAR-P Archetype Ledger — v1

**Built:** 2026-08-29 · **Instances:** Paper 1 populated both instance tables 2026-08-30 (63 shape rows, 8-family tally); Paper 2 appended 2026-08-31 (63 more shape rows, 8-family tally). Rebuilt from the shipped HTML files, not from a session's own account.

Two taxonomies live here. **Shapes** are how an item is put together — the rhetorical form of the stem
and what it asks the candidate to do. **Families** are how a distractor is wrong. An item has one shape
and three distractors from three different families.

Both are enforced in the fidelity gate: shapes by check 11, families by check 10.

---

## Part 1 — The eight shapes

Derived from the three official samples in `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf` §8 and from
the decision axes the corpus already uses. Three shapes are evidenced directly by an official sample.
The other five are the recurring decision forms in the corpus, written in the official register.

Shape repetition is deliberate on this exam series and is not a defect. Ram's stated reason for sitting
papers is pattern familiarity: recognising a shape fast enough to answer without reading every option
under a 120-minute clock. The Foundations project built that by accident and then banned it as a defect
in its ban-list. Here it is a phased policy — see `CCAR-P-Orchestration-Prompt_v2.md` §7.

| # | Shape | What the stem does | What the candidate must do | Official evidence |
|---|---|---|---|---|
| **S1** | Named-principle application | States a governing principle by name, then describes a configuration that violates it | Apply the named principle against options that are all defensible on some other axis | Sample 1 — "Applying least-privilege principles, which change best reduces risk?" |
| **S2** | Two-constraint optimisation | Names two constraints that must be satisfied at once | Find the single change that moves both, rather than the one that trades one for the other | Sample 2 — "Latency and cost are both concerns. Which optimization most directly addresses both?" |
| **S3** | Post-change diagnosis | Describes a behaviour change after a specific event, and pins the variables that did **not** change | Order the investigation. Not "what is wrong" but "what to check **first**" | Sample 3 — "after a document refresh, while latency and model version are unchanged… most likely first place to investigate?" |
| **S4** | Mechanism selection under a stated shape | Describes a data shape, a query pattern, or a connection requirement | Match the mechanism to the shape, where every option is a real mechanism used correctly somewhere else | Corpus §3.11, §3.13, §7.2 |
| **S5** | Rung selection on a ladder | Describes a requirement set, some of which is enumerable and some not | Pick the cheapest rung that meets a **stated** requirement, in either direction | Corpus §1.3, §1.4 — the corpus tests both directions by design |
| **S6** | Measurement definition | Describes a system about to be evaluated, or a number already being reported | Define or repair the measurement — threshold in advance, stratified reporting, grader choice | Corpus §4.1, §4.4, §4.5 |
| **S7** | Stakeholder framing | Describes a request, a commitment, or a report to a non-technical audience | Separate the stated mechanism from the stated requirement, or bound an unbounded ask | Corpus §6.1, §6.2, §6.9 |
| **S8** | Scope and enforcement placement | Describes a control, a configuration, or a permission that exists at the wrong altitude | Move it to the layer that owns it, rather than compensating for it where it sits | Corpus §5.3, §7.1, §7.8 |

### Per-paper shape budget

63 items across 8 shapes. Target 6–9 items per shape, hard floor 4, hard ceiling 11. No shape may be
absent from a paper — a shape the series stops using is a shape Ram stops recognising.

### Direction inversion, Papers 4 onward

From Paper 4 each shape appears at least twice with its direction inverted, so recognising the shape
stops being sufficient to answer it. Inversion is defined per shape:

| Shape | Normal direction | Inverted direction |
|---|---|---|
| S1 | The principle demands removing something; the distractors compensate instead | The principle is already correctly applied and a **further** restriction would break a stated requirement |
| S2 | One change satisfies both constraints | No single change satisfies both; the answer is the one that satisfies the binding constraint and states the trade |
| S3 | The recent change is the cause | The recent change is a coincidence; the pinned variables point elsewhere |
| S4 | The stated shape rules out the obvious mechanism | The obvious mechanism is correct and the sophisticated alternative is the trap |
| S5 | Over-engineering — the item wants the lower rung | Under-engineering — a stated requirement is genuinely non-enumerable and the higher rung is correct |
| S6 | The measurement is missing and must be defined | The measurement exists, is correctly defined, and is being read wrongly |
| S7 | The stakeholder's stated mechanism is not the requirement | The stakeholder's stated mechanism **is** the requirement and the architect's preferred redesign is out of scope |
| S8 | The control is too low and must move up | The control is too high and is blocking a legitimate stated need |

The inverted direction of every shape is where Foundations habit 3 lives — "choosing an option because
of how it *sounds* — safer, more architected, more thorough". S5-inverted and S8-inverted are the two
that punish that habit most directly.

### Shape instance ledger

One row per `(shape, section, facet, direction)` used. A triple is banned after **2 uses**, and two
approved re-frames are recorded here at ban time.

| shape | section | facet | direction | paper | outcome | notes |
|---|---|---|---|---|---|---|
| S5 | 1.1 | F-1.1-01 | normal | 1 | shipped | |
| S5 | 1.3 | F-1.3-01 | normal | 1 | shipped | |
| S5 | 1.6 | F-1.6-01 | normal | 1 | shipped | |
| S5 | 1.10 | F-1.10-01 | normal | 1 | shipped | |
| S5 | 1.11 | F-1.11-01 | normal | 1 | shipped | |
| S5 | 1.12 | F-1.12-01 | normal | 1 | shipped | |
| S5 | 1.5 | F-1.5-01 | normal | 1 | shipped | |
| S5 | 1.7 | F-1.7-01 | normal | 1 | shipped | |
| S4 | 1.9 | F-1.9-01 | normal | 1 | shipped | |
| S4 | 1.2 | F-1.2-01 | normal | 1 | shipped | |
| S4 | 1.4 | F-1.4-01 | normal | 1 | shipped | |
| S2 | 2.1 | F-2.1-01 | normal | 1 | shipped | |
| S2 | 2.2 | F-2.2-01 | normal | 1 | shipped | |
| S2 | 2.3 | F-2.3-01 | normal | 1 | shipped | |
| S2 | 2.5 | F-2.5-01 | normal | 1 | shipped | |
| S2 | 2.8 | F-2.8-01 | normal | 1 | shipped | |
| S2 | 2.4 | F-2.4-01 | normal | 1 | shipped | |
| S2 | 2.6 | F-2.6-01 | normal | 1 | shipped | |
| S2 | 2.7 | F-2.7-01 | normal | 1 | shipped | |
| S4 | 3.1 | F-3.1-01 | normal | 1 | shipped | |
| S4 | 3.2 | F-3.2-01 | normal | 1 | shipped | |
| S4 | 3.4 | F-3.4-01 | normal | 1 | shipped | |
| S4 | 3.7 | F-3.7-01 | normal | 1 | shipped | |
| S4 | 3.8 | F-3.8-01 | normal | 1 | shipped | |
| S1 | 3.11 | F-3.11-01 | normal | 1 | shipped | |
| S1 | 3.13 | F-3.13-01 | normal | 1 | shipped | |
| S1 | 3.14 | F-3.14-01 | normal | 1 | shipped | |
| S1 | 3.3 | F-3.3-01 | normal | 1 | shipped | |
| S1 | 3.5 | F-3.5-01 | normal | 1 | shipped | |
| S1 | 3.6 | F-3.6-01 | normal | 1 | shipped | |
| S1 | 3.9 | F-3.9-01 | normal | 1 | shipped | |
| S6 | 4.1 | F-4.1-01 | normal | 1 | shipped | |
| S6 | 4.3 | F-4.3-01 | normal | 1 | shipped | |
| S6 | 4.9 | F-4.9-01 | normal | 1 | shipped | |
| S6 | 4.10 | F-4.10-01 | normal | 1 | shipped | |
| S6 | 4.11 | F-4.11-04 | normal | 1 | shipped | |
| S6 | 4.12 | F-4.12-01 | normal | 1 | shipped | |
| S6 | 4.5 | F-4.5-01 | normal | 1 | shipped | |
| S6 | 4.2 | F-4.2-01 | normal | 1 | shipped | |
| S3 | 4.4 | F-4.4-01 | normal | 1 | shipped | |
| S3 | 4.9 | F-4.9-02 | normal | 1 | shipped | |
| S1 | 5.1 | F-5.1-01 | normal | 1 | shipped | |
| S8 | 5.3 | F-5.3-01 | normal | 1 | shipped | |
| S8 | 5.6 | F-5.6-04 | normal | 1 | shipped | |
| S8 | 5.8 | F-5.8-01 | normal | 1 | shipped | |
| S8 | 5.10 | F-5.10-01 | normal | 1 | shipped | |
| S8 | 5.2 | F-5.2-01 | normal | 1 | shipped | |
| S8 | 5.4 | F-5.4-01 | normal | 1 | shipped | |
| S8 | 5.5 | F-5.5-01 | normal | 1 | shipped | |
| S8 | 5.7 | F-5.7-01 | normal | 1 | shipped | |
| S7 | 6.1 | F-6.1-01 | normal | 1 | shipped | |
| S7 | 6.4 | F-6.4-01 | normal | 1 | shipped | |
| S7 | 6.9 | F-6.9-01 | normal | 1 | shipped | |
| S7 | 6.7 | F-6.7-01 | normal | 1 | shipped | |
| S7 | 6.12 | F-6.12-01 | normal | 1 | shipped | |
| S7 | 6.2 | F-6.2-01 | normal | 1 | shipped | |
| S7 | 6.3 | F-6.3-01 | normal | 1 | shipped | |
| S7 | 6.6 | F-6.6-01 | normal | 1 | shipped | |
| S3 | 6.8 | F-6.8-01 | normal | 1 | shipped | |
| S3 | 7.2 | F-7.2-01 | normal | 1 | shipped | |
| S3 | 7.3 | F-7.3-01 | normal | 1 | shipped | |
| S3 | 7.8 | F-7.8-01 | normal | 1 | shipped | |
| S3 | 7.1 | F-7.1-01 | normal | 1 | shipped | |
| S1 | 1.1 | F-1.1-03 | normal | 2 | shipped | |
| S6 | 1.2 | F-1.2-03 | normal | 2 | shipped | |
| S4 | 1.9 | F-1.9-04 | normal | 2 | shipped | |
| S1 | 1.5 | F-1.5-02 | normal | 2 | shipped | |
| S8 | 1.10 | F-1.10-02 | normal | 2 | shipped | |
| S5 | 1.3 | F-1.3-04 | normal | 2 | shipped | |
| S1 | 1.4 | F-1.4-04 | normal | 2 | shipped | |
| S1 | 1.7 | F-1.7-04 | normal | 2 | shipped | |
| S4 | 1.8 | F-1.8-04 | normal | 2 | shipped | |
| S1 | 1.11 | F-1.11-03 | normal | 2 | shipped | |
| S1 | 1.12 | F-1.12-02 | normal | 2 | shipped | |
| S5 | 2.1 | F-2.1-02 | normal | 2 | shipped | |
| S5 | 2.1 | F-2.1-03 | normal | 2 | shipped | |
| S8 | 2.2 | F-2.2-02 | normal | 2 | shipped | |
| S2 | 2.2 | F-2.2-04 | normal | 2 | shipped | |
| S4 | 2.4 | F-2.4-02 | normal | 2 | shipped | |
| S1 | 2.3 | F-2.3-03 | normal | 2 | shipped | |
| S6 | 2.5 | F-2.5-02 | normal | 2 | shipped | |
| S8 | 2.9 | F-2.9-01 | normal | 2 | shipped | |
| S4 | 3.1 | F-3.1-03 | normal | 2 | shipped | |
| S1 | 3.2 | F-3.2-02 | normal | 2 | shipped | |
| S5 | 3.4 | F-3.4-04 | normal | 2 | shipped | |
| S2 | 3.3 | F-3.3-02 | normal | 2 | shipped | |
| S1 | 3.5 | F-3.5-02 | normal | 2 | shipped | |
| S6 | 3.7 | F-3.7-03 | normal | 2 | shipped | |
| S1 | 3.11 | F-3.11-04 | normal | 2 | shipped | |
| S1 | 3.12 | F-3.12-04 | normal | 2 | shipped | |
| S1 | 3.13 | F-3.13-02 | normal | 2 | shipped | |
| S2 | 3.10 | F-3.10-01 | normal | 2 | shipped | |
| S1 | 3.9 | F-3.9-03 | normal | 2 | shipped | |
| S1 | 3.14 | F-3.14-03 | normal | 2 | shipped | |
| S3 | 4.2 | F-4.2-03 | normal | 2 | shipped | |
| S1 | 4.6 | F-4.6-05 | normal | 2 | shipped | |
| S1 | 4.7 | F-4.7-03 | normal | 2 | shipped | |
| S6 | 4.8 | F-4.8-04 | normal | 2 | shipped | |
| S2 | 4.9 | F-4.9-03 | normal | 2 | shipped | |
| S4 | 4.10 | F-4.10-06 | normal | 2 | shipped | |
| S1 | 4.11 | F-4.11-06 | normal | 2 | shipped | |
| S1 | 4.11 | F-4.11-05 | normal | 2 | shipped | |
| S1 | 4.12 | F-4.12-02 | normal | 2 | shipped | |
| S1 | 4.12 | F-4.12-07 | normal | 2 | shipped | |
| S2 | 5.1 | F-5.1-03 | normal | 2 | shipped | |
| S1 | 5.9 | F-5.9-02 | normal | 2 | shipped | |
| S3 | 5.6 | F-5.6-03 | normal | 2 | shipped | |
| S1 | 5.7 | F-5.7-03 | normal | 2 | shipped | |
| S2 | 5.5 | F-5.5-03 | normal | 2 | shipped | |
| S2 | 5.8 | F-5.8-02 | normal | 2 | shipped | |
| S8 | 5.3 | F-5.3-03 | normal | 2 | shipped | |
| S6 | 5.10 | F-5.10-03 | normal | 2 | shipped | |
| S1 | 5.11 | F-5.11-04 | normal | 2 | shipped | |
| S7 | 6.1 | F-6.1-02 | normal | 2 | shipped | |
| S7 | 6.2 | F-6.2-02 | normal | 2 | shipped | |
| S7 | 6.4 | F-6.4-02 | normal | 2 | shipped | |
| S7 | 6.6 | F-6.6-04 | normal | 2 | shipped | |
| S1 | 6.11 | F-6.11-01 | normal | 2 | shipped | |
| S7 | 6.9 | F-6.9-03 | normal | 2 | shipped | |
| S6 | 6.10 | F-6.10-02 | normal | 2 | shipped | |
| S7 | 6.8 | F-6.8-02 | normal | 2 | shipped | |
| S7 | 6.12 | F-6.12-04 | normal | 2 | shipped | |
| S7 | 7.1 | F-7.1-02 | normal | 2 | shipped | |
| S4 | 7.5 | F-7.5-07 | normal | 2 | shipped | |
| S2 | 7.8 | F-7.8-05 | normal | 2 | shipped | |
| S3 | 7.5 | F-7.5-06 | normal | 2 | shipped | |

---

## Part 2 — The eight distractor families

Six come from `CCAR-P_Domain-Template_v1.md` and are already tagged on all 158 corpus distractors. Two
are added from the official rationales, which name rejection reasons the corpus taxonomy has no slot for.

| Family | A distractor of this family is… | Corpus instances | Official instances |
|---|---|---|---|
| **HALF-MOVE** | Correct as far as it goes; leaves a stated requirement untouched | 46 (29.1%) | — |
| **WRONG-AXIS** | Applies a real technique on the wrong dimension of the problem | 36 (22.8%) | Sample 1 D — "model size is unrelated to authorization scope" |
| **REPAIR** | Reconstructs downstream what an upstream step should have done cleanly | 25 (15.8%) | — |
| **DISCARD** | Solves the problem by throwing away something the scenario requires | 22 (13.9%) | Sample 2 A — "truncation loses needed policy" |
| **ARCHITECTED** | More capable, more future-proof, more thorough than the requirement supports | 20 (12.7%) | **0 of 12** |
| **OVERSPEC** | Substitutes a monitoring or threshold guarantee for a stated hard constraint | 9 (5.7%) | — |
| **EVIDENCE-MISMATCH** | A cause the evidence stated in the stem already rules out | **0 — untagged** | Sample 3 A, C, D (3 of 12) |
| **DETECTIVE-FOR-PREVENTIVE** | Detects or confirms a misuse where the requirement is to remove the capability | **0 — untagged** | Sample 1 A, C (2 of 12) |

### Reconciling the official rejection reasons against this taxonomy

The engine audit's Part B named five rejection reasons visible in the official rationales. Three of
them map onto existing families and do not need their own slot; two do not map and became the seventh
and eighth families above.

| Official rejection reason | Instances | Maps to | Why |
|---|---|---|---|
| DETECTIVE-FOR-PREVENTIVE | S1 A, S1 C | **new family** | No corpus family covers "monitors the thing instead of removing it". OVERSPEC is adjacent but is about thresholds substituting for hard constraints, not controls substituting for removal |
| EVIDENCE-MISMATCH | S3 A, C, D | **new family** | No corpus family covers "the stem's own evidence excludes this". This is the family the official samples use most and the corpus does not name at all |
| LOSSY-SHORTCUT | S2 A, S2 B | DISCARD | Truncating the policy and blind-downsizing both discard something the scenario requires |
| RIGHT-TECHNIQUE-WRONG-MECHANISM | S2 D | HALF-MOVE | Moving the policy to a few-shot block is a real technique that leaves the stated caching requirement unmet |
| IRRELEVANT-LEVER | S1 D | WRONG-AXIS | A larger model is a real lever on the wrong dimension |

### Per-paper family caps

189 distractors per paper. Enforced in fidelity-gate check 10.

| Rule | Threshold | Reason |
|---|---|---|
| No family above 25% | ≤ 47 | The corpus is 29.1% HALF-MOVE and 22.8% WRONG-AXIS. Uncapped, two families supply more than half of every paper's wrong answers and Ram learns shapes rather than decisions |
| EVIDENCE-MISMATCH floor | ≥ 15 (8%) | 3 of 9 official distractors. The family the exam uses most is the one the corpus never tags |
| DETECTIVE-FOR-PREVENTIVE floor | ≥ 9 (5%) | 2 of 9 official distractors |
| ARCHITECTED ceiling | ≤ 19 (10%) | **0 of 12** official distractors are rejected for over-architecting. The corpus over-supplies this family at 12.7% |
| Per item | 3 distractors, 3 different families | Three flavours of one wrong answer make an item that tests nothing |

The ARCHITECTED ceiling is the one cap that carries a risk worth stating: root `CLAUDE.md` habit 3 is
precisely the pull toward the more-architected option, so capping the family reduces practice against
Ram's most documented habit. The remedy is not a higher cap — it is §7's habit escalation, which makes
the architected-sounding option **correct** on 2–3 items once the family qualifies as a habit.
Suppressing a shape teaches avoidance; making it sometimes right teaches discrimination.

### Family instance ledger

Rebuilt from shipped papers, never from a generating session's own tally.

| paper | HALF-MOVE | WRONG-AXIS | REPAIR | DISCARD | ARCHITECTED | OVERSPEC | EVIDENCE-MISMATCH | DETECTIVE-FOR-PREVENTIVE |
|---|---|---|---|---|---|---|---|---|
| 1 | 38 | 34 | 21 | 21 | 16 | 11 | 23 | 17 |
| 2 | 38 | 42 | 16 | 28 | 11 | 13 | 22 | 11 |

---

## Maintenance

Both ledgers are rebuilt from shipped HTML files. A session that generates a paper does not write its
own instance rows from memory — it writes the paper, then the ledger is rebuilt from what actually
shipped. Foundations lost two seed records to prose self-report and recovered only one.
