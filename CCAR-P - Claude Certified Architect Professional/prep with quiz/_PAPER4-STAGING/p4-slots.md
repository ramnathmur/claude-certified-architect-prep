# Paper 4 — Central Plan (Slots)

Computed centrally, before any authoring dispatch, per Phase 6/§6 of
`Outputs/CCAR-P_Paper-4-Generation-Prompt_v1.md`. Untargeted diagnostic — Papers 1, 2 and 3 are
all generated but none has been sat, confirmed with Ram before generating (§3). Mode: AUTHOR.
**Direction inversion begins this paper** — 17 items ship `direction: "inverted"`, >=2 per shape,
each with an `invGuidance` string quoting the exact inversion definition. Every item ships
`deepDive: null` at generation time.

## D1 (11 items, g1-g11)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g1 | 1.1 | O1.1 | F-1.1-04 | floor | S6 | inverted | single | C |
| g2 | 1.10 | O1.2 | F-1.10-04 | floor | S4 | inverted | single | D |
| g3 | 1.3 | O1.3 | F-1.3-03 | floor | S5 | normal | single | D |
| g4 | 1.6 | O1.4 | F-1.6-03 | floor | S1 | normal | multi | MULTI selectN:2, pair AB |
| g5 | 1.11 | O1.5 | F-1.11-05 | floor | S5 | inverted | single | B |
| g6 | 1.12 | O1.6 | F-1.12-04 | floor | S2 | normal | single | B |
| g7 | 1.2 | O1.1 | F-1.2-04 | discretionary | S6 | inverted | single | B |
| g8 | 1.9 | O1.2 | F-1.9-03 | discretionary | S1 | normal | single | A |
| g9 | 1.4 | O1.3 | F-1.4-03 | discretionary | S5 | normal | single | D |
| g10 | 1.5 | O1.4 | F-1.5-03 | discretionary | S5 | normal | multi | MULTI selectN:2, pair CD |
| g11 | 1.11 | O1.5 | F-1.11-06 | discretionary | S5 | normal | single | D |

### D1 inversion guidance

**g1** (1.1, S6): The measurement exists, is correctly defined, and is being read wrongly. Invert: the outcome metric is already correctly defined in advance; the trap is a superficially-similar proxy metric being treated as equivalent when it doesn't actually measure the stated business decision.

**g2** (1.10, S4): The obvious mechanism is correct and the sophisticated alternative is the trap. Invert: the obvious mechanism (a straightforward schema/contract check at the input or output boundary) is already correct; a sophisticated addition (an extra LLM-based validation pass) is the unneeded, costlier trap.

**g5** (1.11, S5): Under-engineering -- a stated requirement is genuinely non-enumerable and the higher rung is correct. Invert: the stated subtask is genuinely non-enumerable (open-ended synthesis/judgment, not a checklist), so a coarser single-call approach is wrong and finer, named-step decomposition is actually required -- the higher rung, not the lower one.

**g7** (1.2, S6): The measurement exists, is correctly defined, and is being read wrongly. Invert: the baseline/value-unit measurement is already correctly and stably defined; apparent 'drift' is the metric's own definition having silently changed upstream, not real performance change.

## D2 (8 items, g12-g19)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g12 | 2.1 | O2.1 | F-2.1-01 (REUSE ANCHOR, invert) | floor | S5 | inverted | single | A |
| g13 | 2.2 | O2.2 | F-2.2-01 (REUSE ANCHOR, invert) | floor | S8 | inverted | single | D |
| g14 | 2.3 | O2.3 | M-2.3 (misconception unit) | floor | S1 | normal | single | C |
| g15 | 2.5 | O2.4 | M-2.5 (misconception unit) | floor | S6 | normal | single | D |
| g16 | 2.9 | O2.5 | M-2.9 (misconception unit) | floor | S8 | normal | single | A |
| g17 | 2.4 | O2.3 | F-2.4-01 (REUSE ANCHOR, invert) | discretionary | S1 | inverted | single | A |
| g18 | 2.7 | O2.4 | F-2.7-01 (REUSE ANCHOR, invert) | discretionary | S1 | inverted | single | D |
| g19 | 2.8 | O2.5 | F-2.8-01 (REUSE ANCHOR, invert) | discretionary | S2 | inverted | single | B |

### D2 inversion guidance

**g12** (2.1, S5): Under-engineering -- a stated requirement is genuinely non-enumerable and the higher rung is correct. Normal-direction facet F-2.1-01 tests avoiding an oversized model for a bounded, high-volume task. Invert: state an explicit regulatory/compliance requirement (a named audit or certification mandate) that cannot be captured by an accuracy-bar test alone -- the higher-capability model is correct despite volume pressure toward the cheaper one. Must NOT reproduce F-2.1-02's already-shipped 'ambiguous multi-step synthesis' framing.

**g13** (2.2, S8): The control is too high and is blocking a legitimate stated need. Section 2.2's core rule (system prompt is the only durable-authority location) is absolute -- Paper 2's g14/g15 already found no conditional row supports a clean T1 inversion here. Attempt the best defensible S8-inverted framing (an existing system-prompt guardrail is over-broad and blocks a legitimate case) but if no clause deletion/inversion produces a genuinely different correct option, flag this item as a T1 IRREDUCIBLE candidate in t1Clause/t1Alt rather than forcing one -- document honestly, matching Paper 2's precedent.

**g17** (2.4, S1): The principle is already correctly applied and a further restriction would break a stated requirement. Normal-direction facet F-2.4-01 tests adding a reasoning cue for multi-step tasks. Invert: a chain-of-thought cue is already correctly present for a genuinely multi-step task; the trap option removes it 'to save tokens/cost', which would break the accuracy requirement the cue exists to satisfy. Correct answer: keep the cue.

**g18** (2.7, S1): The principle is already correctly applied and a further restriction would break a stated requirement. Normal-direction facet F-2.7-01 tests hybrid extraction for precision-critical facts. Invert: the conversation has NO precision-critical facts (pure open-ended discussion) and a stated cost/latency ceiling exists; applying the hybrid-extraction approach anyway is over-engineered overhead that would blow the ceiling for no benefit -- plain summarization is correct and sufficient. Punishes the 'sounds more careful' reflex directly.

**g19** (2.8, S2): No single change satisfies both constraints; the answer is the one that satisfies the binding constraint and states the trade. Normal-direction facet F-2.8-01 tests static-first ordering for caching. Invert: a stated hard requirement (a compliance disclaimer/audit stamp) must appear in every request and looks like it has to go first, seemingly breaking the cacheable prefix. Naive options either drop the stamp (breaks the requirement) or reorder in a way that kills caching for no reason. Correct answer states the trade: the stamp can go AFTER the stable cached prefix without weakening its effect, satisfying both constraints.

## D3 (12 items, g20-g31)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g20 | 3.1 | O3.1 | F-3.1-05 | floor | S4 | inverted | single | D |
| g21 | 3.2 | O3.2 | F-3.2-04 | floor | S8 | normal | single | C |
| g22 | 3.4 | O3.3 | F-3.4-03 | floor | S2 | inverted | single | B |
| g23 | 3.6 | O3.4 | F-3.6-03 | floor | S1 | normal | single | B |
| g24 | 3.10 | O3.5 | F-3.10-02 | floor | S3 | inverted | single | C |
| g25 | 3.12 | O3.6 | F-3.12-01 | floor | S1 | normal | single | C |
| g26 | 3.13 | O3.7 | F-3.13-04 | floor | S4 | normal | single | B |
| g27 | 3.14 | O3.8 | F-3.14-04 | floor | S1 | normal | single | A |
| g28 | 3.1 | O3.1 | M-3.1 (misconception unit) | discretionary | S4 | normal | single | D |
| g29 | 3.3 | O3.2 | F-3.3-04 | discretionary | S2 | normal | multi | MULTI selectN:2, pair AC |
| g30 | 3.5 | O3.3 | F-3.5-04 | discretionary | S1 | normal | single | B |
| g31 | 3.7 | O3.4 | F-3.7-04 | discretionary | S6 | normal | single | A |

### D3 inversion guidance

**g20** (3.1, S4): The obvious mechanism is correct and the sophisticated alternative is the trap. Invert: the obvious mechanism (a narrowly-scoped tool surface matched to the task) is already correct; granting a broader tool surface 'for flexibility' is the sophisticated-sounding trap that reintroduces capability bloat.

**g22** (3.4, S2): No single change satisfies both constraints; the answer is the one that satisfies the binding constraint and states the trade. Invert: a hard regulatory latency SLA is stated and cannot be relaxed. No single change satisfies both a stricter accuracy target and the SLA at once -- the correct answer accepts an explicit accuracy trade to hold the binding latency constraint, rather than chasing an option that claims to fix both.

**g24** (3.10, S3): The recent change is a coincidence; the pinned variables point elsewhere. Invert: after an index refresh, degraded retrieval quality persists, but the refresh is a coincidence -- the pinned variables (chunking, embedding model) point elsewhere, e.g. an embedding-model version drift that happened in the same window. The reflex answer (re-check the refresh pipeline) is the trap.

## D4 (10 items, g32-g41)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g32 | 4.2 | O4.1 | F-4.2-02 | floor | S3 | normal | single | B |
| g33 | 4.4 | O4.2 | F-4.4-02 | floor | S6 | normal | single | C |
| g34 | 4.9 | O4.3 | F-4.9-05 | floor | S3 | normal | multi | MULTI selectN:2, pair BD |
| g35 | 4.10 | O4.4 | F-4.10-04 | floor | S3 | inverted | single | D |
| g36 | 4.11 | O4.5 | F-4.11-02 | floor | S1 | inverted | single | C |
| g37 | 4.12 | O4.6 | F-4.12-04 | floor | S1 | normal | single | C |
| g38 | 4.2 | O4.1 | F-4.2-04 | discretionary | S3 | normal | single | D |
| g39 | 4.6 | O4.2 | F-4.6-01 | discretionary | S6 | normal | single | A |
| g40 | 4.9 | O4.3 | F-4.9-07 | discretionary | S3 | normal | single | A |
| g41 | 4.10 | O4.4 | F-4.10-05 | discretionary | S4 | normal | single | D |

### D4 inversion guidance

**g35** (4.10, S3): The recent change is a coincidence; the pinned variables point elsewhere. Invert: accuracy drops at the same time as a prompt-template edit, but investigation shows the drop actually correlates with a simultaneous, easily-missed upstream data-schema change -- the recent prompt edit is a coincidence, not the cause.

**g36** (4.11, S1): The principle is already correctly applied and a further restriction would break a stated requirement. Invert: caching is already correctly enabled via static-first ordering. The trap over-applies caching to content that is actually per-user/highly dynamic, which would serve stale or cross-user data -- a further 'more aggressive caching' restriction breaks a stated correctness/freshness requirement.

## D5 (9 items, g42-g50)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g42 | 5.1 | O5.1 | F-5.1-02 | floor | S8 | normal | single | B |
| g43 | 5.6 | O5.2 | F-5.6-05 | floor | S3 | normal | multi | MULTI selectN:2, pair AD |
| g44 | 5.8 | O5.3 | F-5.8-05 | floor | S2 | normal | single | C |
| g45 | 5.3 | O5.4 | F-5.3-02 | floor | S8 | inverted | single | A |
| g46 | 5.10 | O5.5 | F-5.10-02 | floor | S6 | normal | single | A |
| g47 | 5.1 | O5.1 | F-5.1-04 | discretionary | S8 | normal | single | D |
| g48 | 5.6 | O5.2 | F-5.6-06 | discretionary | S3 | normal | single | A |
| g49 | 5.8 | O5.3 | M-5.8 (misconception unit) | discretionary | S2 | normal | single | B |
| g50 | 5.5 | O5.4 | F-5.5-02 | discretionary | S2 | normal | single | C |

### D5 inversion guidance

**g45** (5.3, S8): The control is too high and is blocking a legitimate stated need. Invert: a compliance-mandated boundary control (e.g. data-residency enforcement) is already correctly placed at the infrastructure/network layer and is now blocking a legitimate new use case (a partner integration needing controlled cross-region access). Correct answer: a scoped, explicit exception process at the same layer -- not moving the control down to the application layer to work around it.

## D6 (9 items, g51-g59)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g51 | 6.1 | O6.1 | F-6.1-03 | floor | S7 | normal | single | B |
| g52 | 6.4 | O6.2 | F-6.4-04 | floor | S7 | normal | single | B |
| g53 | 6.9 | O6.3 | F-6.9-02 | floor | S7 | inverted | single | A |
| g54 | 6.8 | O6.4 | F-6.8-03 | floor | S7 | normal | single | A |
| g55 | 6.12 | O6.5 | F-6.12-02 | floor | S7 | normal | multi | MULTI selectN:2, pair BC |
| g56 | 6.2 | O6.1 | F-6.2-03 | discretionary | S7 | inverted | single | C |
| g57 | 6.6 | O6.2 | F-6.6-03 | discretionary | S7 | normal | single | D |
| g58 | 6.9 | O6.3 | F-6.9-04 | discretionary | S7 | normal | single | B |
| g59 | 6.8 | O6.4 | F-6.8-04 | discretionary | S7 | normal | single | C |

### D6 inversion guidance

**g53** (6.9, S7): The stakeholder's stated mechanism IS the requirement and the architect's preferred redesign is out of scope. Invert: the requested SLA framing is the binding commitment already stated in a signed agreement -- re-negotiating a 'more technically honest' probabilistic framing is out of scope for this engagement, however defensible it would be in the abstract.

**g56** (6.2, S7): The stakeholder's stated mechanism IS the requirement and the architect's preferred redesign is out of scope. Invert: the stakeholder's stated mechanism (e.g. a specific named review workflow) is itself the actual compliance-driven requirement, not just their guess at implementation -- the architect's preferred, more elegant automated redesign is out of scope even though it looks better engineered.

## D7 (4 items, g60-g63)

| g | section | objective | source | pass | shape | direction | format | correct |
|---|---|---|---|---|---|---|---|---|
| g60 | 7.2 | O7.1 | F-7.2-02 | floor | S3 | normal | multi | MULTI selectN:2, pair AB |
| g61 | 7.3 | O7.2 | F-7.3-03 | floor | S5 | normal | single | C |
| g62 | 7.8 | O7.3 | F-7.8-02 | floor | S2 | normal | multi | MULTI selectN:2, pair CD |
| g63 | 7.1 | O7.1 | F-7.1-03 | discretionary | S3 | normal | single | C |

## Pre-plan tallies (gate checks 2, 5, 6, 7 targets)

- **Domain quota**: 11/8/12/10/9/9/4 — no confirmed-weakness adjustment (no scored papers exist yet to confirm one).
- **Correct-letter tally (55 single-answer)**: {"C":14,"D":14,"B":14,"A":13} — Paper 4's short letter is A (P1 short D, P2 short C, P3 short B, P4 short A, then repeats).
- **Multi-response pairs (8 items)**: {"AB":2,"CD":2,"AC":1,"BD":1,"AD":1,"BC":1} — each pair used at most twice.
- **Shape tally**: {"S6":7,"S4":5,"S5":7,"S1":11,"S2":8,"S8":6,"S3":10,"S7":9} — all within the hard floor 4 / hard ceiling 11 (rebalanced from a raw SHAPE_HINTS draw that put S1 at 15 and S8 at 3 — three normal-direction items at D3/3.2 and D5/5.1(x2) were moved from S1 to S8, and D4/4.6 from S1 to S6, since those sections fit the reassigned shape at least as naturally). Soft guidance only beyond that: an authoring sub-batch may substitute a better-fitting shape for a specific facet's content, but do not let any shape fall below 4 or rise above 11.
- **Inverted-direction shape tally**: {"S6":2,"S4":2,"S5":2,"S8":2,"S1":3,"S2":2,"S3":2,"S7":2} — all 8 shapes have >=2 inverted instances, spread across 6 of 7 domains (D2 supplies 5, structurally forced by its supply crisis; the other 12 spread across D1/D3/D4/D5/D6).
- **Objective floor**: all 38 objectives covered exactly once at minimum; discretionary pass caps every objective at 3 items total this paper.
- **Distractor family paper-wide floors to keep in mind while drafting** (checked and fixed centrally at assembly per F-19 — do not force it per-batch, but do not default to WRONG-AXIS/HALF-MOVE for convenience either): EVIDENCE-MISMATCH >= 15 of ~189 distractors (8%), DETECTIVE-FOR-PREVENTIVE >= 9 (5%), no family > 47 (25%), ARCHITECTED <= 19 (10%). D3/D5/D7 items about removing/restricting a capability are natural DETECTIVE-FOR-PREVENTIVE homes. Items where the stem states specific evidence that itself rules out a plausible-sounding cause are natural EVIDENCE-MISMATCH homes.

## D2 note — direction-inverted reuse fires for the first time, Ram's approved decision

D2's real decision-table facet supply is fully exhausted (0 of 18 facets fresh across Papers
1-3). Per Ram's decision recorded in `EXAM-LOG.md`'s Paper 4 entry: 3 of D2's 8 items use the
last unused misconception units (M-2.3, M-2.5, M-2.9, sections 2.3/2.5/2.9), built normally. The
other 5 (sections 2.1, 2.2, 2.4, 2.7, 2.8) reuse an already-shipped facet as an anchor but must
test the inverted direction — see the D2 inversion guidance above and `p4-shared-brief.md`'s D2
section. Section 2.2 is flagged as a likely IRREDUCIBLE case (Paper 2's g14/g15 already found no
conditional row there); attempt the best defensible inversion but document honestly if it does
not resolve, per the shared brief's honesty rule.
