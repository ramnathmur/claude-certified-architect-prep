# CCAR-P Mock Exam Orchestration Prompt — v2

**Supersedes v1.** v1 ported the Foundations feedback loop and left the item-fidelity half behind: of the
20 Foundations mechanisms that govern what a generated question actually looks like, none were operative
and only two were a recorded decision. See `Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md` for the full
comparison. v2 closes that gap and adds four mechanisms Foundations never had.

Read `../CLAUDE.md`, `../../CLAUDE.md`, `../EXAM-FACTS_v1.md` first. Nothing here overrides them.

## Preflight — abort conditions

Abort and report if any fails:

1. `../EXAM-FACTS_v1.md` shows unresolved rows for domain list, weightings, or item count.
   *(Cleared 2026-08-25: all three VERIFIED against the official guide v1.0, with the S3-mirror
   provenance caveat recorded in that file.)*
2. Any `CCAR-P_Domain-N_v1.md` is missing. *(Cleared: all seven exist.)*
3. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md` are missing.
4. The requested paper number already exists in `mock-exams/`, or `DASHBOARD-DATA.jsonl` already has a
   line for it.

---

## Phase 1 — Read state

In this order:

1. `EXAM-LOG.md` — every `SCORED` entry, sorted **by attempt date**, never by paper number.
2. The most recent **Professor's Note — Intent for Paper N**, meaning the note written after the most
   recently *attempted* paper, which is not necessarily the highest-numbered one.
3. The most recent Insights Round, if it is more recent than that note.
4. `GENERATION-INTELLIGENCE.md` — open findings, family capture rates, shape fatigue.
5. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md`.
6. `../EXAM-FACTS_v1.md`.

If the latest Professor's Note and the latest Insights Round disagree, reconcile explicitly in the
generation entry and state which won and why. Do not silently prefer one.

---

## Phase 2 — Mode

Two item-sourcing modes. The mode is fixed per paper and is recorded in the generation entry.

| Mode | Papers | Item source |
|---|---|---|
| **TRANSCRIBE** | Paper 1 only | Options are the corpus's own verbatim text |
| **AUTHOR** | Papers 2–10 | Items written fresh from the corpus's decision-table facets |

Ram's decision, 2026-08-29. Paper 1 gives a clean baseline against material he has already reviewed, so
a miss on Paper 1 is unambiguously a knowledge gap rather than a generation artefact. From Paper 2 the
corpus cannot supply enough distinct options — 158 exist and one paper needs 189 — so authoring is the
only route to a ten-paper series.

### TRANSCRIBE mode, in detail

Each item is built from one section's `Exam scenario` block:

- **Correct option** — the section's ✅ line, verbatim.
- **Distractors 1 and 2** — the section's two ❌ lines, verbatim, carrying their existing family tags.
- **Distractor 3** — the `Answer` cell of a **different row** of the same section's decision table: an
  action that section states is correct in a *neighbouring* situation, verbatim. This satisfies the T2
  test by construction and keeps every word on the paper corpus-sourced.

Supply check, run before committing to this mode: 79 scenarios against a 63-item paper, and every
domain holds more scenarios than its quota (D1 12≥11, D2 9≥8, D3 14≥12, D4 12≥10, D5 11≥9, D6 12≥9,
D7 9≥4). A full-length 63-item Paper 1 is reachable.

**The one authored element.** The corpus contains no multiple-response scenario, and multiple-response
is Ram's largest documented scoring leak. Paper 1 therefore ships **55 TRANSCRIBED + 8 ASSEMBLED**: the
8 are drawn from sections whose decision table holds two independently-true rows for one situation, and
their option text is verbatim corpus text while the *combination* is authored. Tag them `ASSEMBLED` in
the item data so the distinction survives into the miss log.

From Paper 2, the section scenarios revert to reference-only: they are each section's canonical worked
example, and a generated item must produce a **different failure mode** from the one they show.

---

## Phase 3 — Set the distribution

### 3.1 Domain quota

Published weights × 63 items. Plain rounding lands exactly on 63; no largest-remainder step is needed.

| Domain | Weight | Exact | **Items** |
|---|---|---|---|
| D1 Solution Design & Architecture | 17% | 10.71 | **11** |
| D2 Claude Models, Prompting & Context Engineering | 13% | 8.19 | **8** |
| D3 Integration | 19% | 11.97 | **12** |
| D4 Evaluation, Testing & Optimization | 16% | 10.08 | **10** |
| D5 Governance, Safety & Risk Management | 14% | 8.82 | **9** |
| D6 Stakeholder Communication & Lifecycle Management | 14% | 8.82 | **9** |
| D7 Developer Productivity & Operational Enablement | 7% | 4.41 | **4** |
| **Total** | 100% | 63.00 | **63** |

**Confirmed-weakness adjustment.** If a domain is confirmed weak — unambiguously weakest on two
consecutive papers *by attempt date*, a tie failing the bar — raise its quota by 2–4 and lower the
strongest domain by the same. Record it, revert it on the following paper.

Two constraints on the adjustment:
- **D7 floors at 3 and caps at 6.** At 4 items it cannot absorb a −4 without dropping below its 3
  objectives; at 8 it is over-weighted by 78%.
- **The confirmed-weakness check runs on single-answer items only.** Under all-or-nothing scoring a
  majority-right multi-response miss is indistinguishable from a knowledge gap. Eight Foundations
  misses were exactly that, and they would have dragged a domain into false confirmed weakness.

### 3.2 Objective floor pass — the primary seeding unit

63 items against 38 objectives, in two passes.

- **Floor pass — 38 items.** Every objective in `CCAR-P_Objective-Map_v1.md` gets exactly one item.
  Satisfiable inside every domain quota; the narrowest margin is D7 at 3 objectives against 4 items.
- **Discretionary pass — 25 items.** Allocated by the targeting instruction (§7), then by facet
  freshness. **Cap 3 items per objective per paper**, so no objective absorbs the discretionary budget.

This is the mechanism Foundations did not have, and its absence is measurable: the real CCAR-F score
report returned **six objectives at 0%**, two of which had been open in the mock corpus for weeks.

### 3.3 Format split

**55 single-answer + 8 multiple-response (12.7%).**

- Every multi-response stem states its count in the stem text — "Select two." The guide's §5 confirms
  each real item does this.
- `selectN = 2` on all eight, Papers 1–7. Nothing in the guide supports 3.
- A multi-response item may be drawn only from a section whose decision table holds **≥2 independently
  true rows for the same situation**. Otherwise a 2-of-4 is a 1-of-4 with a filler, and it teaches the
  wrong selection habit.
- Across the eight, no correct pair — {A,B}, {A,C}, {A,D}, {B,C}, {B,D}, {C,D} — appears more than
  twice. Position clustering has no reason to spare multi-select items.

**Scoring is all-or-nothing** until proven otherwise. This is a stance, not a finding: `EXAM-FACTS_v1.md`
records it as OPEN. The item data stores the raw `picked` set per item so every prior paper can be
rescored under partial credit retroactively if the guide later settles it.

---

## Phase 4 — Facet selection

Address the corpus by **facet**, not by section. A facet is one `Situation | Answer | Why` row —
351 exist, indexed in `FACET-LEDGER.md`.

Rules, in precedence order:

1. No facet appears twice on one paper.
2. No facet is reused until every facet in its section has been used once.
3. A facet whose item was **missed** is eligible for immediate reuse, but only from the **opposite
   direction**. A repeat miss retested from the same direction proves nothing — Foundations closed the
   `tool_choice` trap in the under-specification direction and it reopened in the over-specification
   direction within a week.
4. A section contributes **at most 2 items** to one paper. This is a ceiling, not a schedule.
5. When a section's facets are exhausted, use its **misconception unit** (`M-<section>`) before reusing
   any facet.

### The D2 supply constraint — read before planning Paper 6

Facet supply is not uniform. Measured:

| Domain | Facets | Items/paper | Papers before reuse |
|---|---|---|---|
| D1 | 62 | 11 | 5.6 |
| **D2** | **18** | **8** | **2.2** |
| D3 | 65 | 12 | 5.4 |
| D4 | 70 | 10 | 7.0 |
| D5 | 52 | 9 | 5.8 |
| D6 | 45 | 9 | 5.0 |
| D7 | 39 | 4 | 9.8 |

D2 binds hard. Sections 2.6, 2.7, 2.8 and 2.9 hold exactly one facet each, and Paper 1 alone consumes
44% of every distinct decision D2 contains. Direction doubling takes D2 to 4.5 papers and the
misconception units take it to 5.6.

**Papers 1–5 are reachable on the corpus as it stands. Papers 6–10 are not.** D2 needs roughly 20 more
decision-table rows to match its siblings' density. That touches corpus files and is Ram's call; raise
it at the Paper 4 Insights Round at the latest, so there is time to write them before Paper 6.

Four sections carry no decision table at all — 6.5, 7.4, 7.6, 7.7 — and can supply items only through
their scenario and misconception.

---

## Phase 5 — Item construction

### 5.1 Correct-answer position, pre-planned

**Before any option text is written**, lay out the 55 single-answer positions as a balanced multiset
**{A×14, B×14, C×14, D×13}**, shuffled into a random per-item order. The short letter rotates across
papers: Paper 1 short D, Paper 2 short C, Paper 3 short B, Paper 4 short A, then repeat.

The correct letter for item *k* is decided here. Drafting writes the correct option into that position.

This is carried from Foundations on hard evidence. Its Phase 4.d.5 exists because one block shipped all
15 questions at the same option letter, undetected by that block's own QA. The measured effect: Exam 2,
before the pre-plan, tallied A20/B17/D12/C11; Exam 20, after it, tallied exactly 13/13/13/13.

It matters more here than it did there. The corpus lists ✅ first and both ❌ after, in fixed order, so
an authoring agent reading a section drifts toward A. The pre-plan is the only defence and gate check 6
is the proof it held.

### 5.2 Distractor families

Three distractors, **three different families**, from the eight defined in `ARCHETYPE-LEDGER.md`.

Per-paper caps across the paper's 189 distractors:

| Rule | Threshold |
|---|---|
| No family above 25% | ≤ 47 |
| EVIDENCE-MISMATCH floor | ≥ 15 |
| DETECTIVE-FOR-PREVENTIVE floor | ≥ 9 |
| ARCHITECTED ceiling | ≤ 19 |

The corpus's own tagged distribution is skewed — HALF-MOVE 29.1%, WRONG-AXIS 22.8%, OVERSPEC 5.7% — and
without caps two families supply more than half of every paper's wrong answers. The ARCHITECTED ceiling
and the EVIDENCE-MISMATCH floor come from the official samples directly: **zero of nine** official
distractors are rejected for over-architecting, and **three of nine** are rejected for not fitting the
stem's own stated evidence.

### 5.3 The Professional-tier floor — four rejection tests

An item ships only if it passes all four. Each is checkable by reading the item.

| Test | Pass condition |
|---|---|
| **T1 · Constraint sensitivity** | Name one clause in the stem whose deletion or inversion makes a **different** option correct. Record the clause and that option in the item's build note |
| **T2 · Neighbour-correct distractor** | At least one distractor is an action the same section's decision table lists as correct in a neighbouring situation |
| **T3 · No vocabulary answer** | Delete the situation, leave the question line. If the correct option is still identifiable, reject |
| **T4 · Production dimension** | The stem carries at least one of: volume or scale, cost, a latency budget, a regulator or compliance regime, an SLA, or a named stakeholder who must approve |

T1 is the load-bearing one. It is the mechanical form of what separates a Professional item from a
Foundations item: the Foundations stem describes a failure and lets the candidate find the axis, while
the Professional stem hands over the axis and tests whether the candidate applies it against options
that are all defensible on some other axis. All three official samples pass T1. A Foundations-tier stem
fails it, because its correct answer holds regardless of the stated constraints.

T1 is cheap to check because the alternative answer is already written down — it is the row of the same
decision table where the other option wins.

### 5.4 Style targets

Measured from the official samples (n=3 stems, 12 options). **Caps are binding. Bands are provisional**
— a cap on n=3 is violated by a single counter-example and none appeared; a median on n=3 is not a
target anyone can be held to.

| Target | Value | Basis |
|---|---|---|
| Stem hard cap | **45 words** | Official max 37, with headroom. Not the Foundations 95 |
| Stem soft band | 28–40 words | Observed 29–37, widened ±3 |
| Option hard cap | **20 words** | Official max 15, with headroom. Not the Foundations 35 |
| Within-item option spread | ≤ 8 words | Official max spread 6 |
| Point of view | Third-person indefinite; second person on ≤15% of stems | 3/3 official third-person. The Foundations 46% "You/Your" rate has no support here |
| Inline code/config tokens | **≤ 15% of options**, never in a D1/D5/D6 option | 0/12 official |
| Named companies, products, personas | **0** | 3/3 official generic; the Foundations 76-text audit found zero |
| `whyRight` | 35–50 words | Official rationales run 39–44 covering key plus all distractors; CCAR-P splits them per option |
| `whyWrong` | 15–30 words each | — |

**The inline-token rule is inverted from Foundations, deliberately.** Foundations enforces a 20–25%
*floor*, derived from its own exam's 21% rate. CCAR-P's samples show 0 of 12. Copying the Foundations
mechanism unchanged would make every CCAR-P paper measurably less like its own exam. This is the
clearest single case where mimicking the sibling project actively reduces fidelity.

### 5.5 Item schema

Every item carries: `g` · `domain` · `section` · `facet` · `objective` · `shape` · `direction` ·
`lessonKey` · `format` · `selectN` · `stem` · `opts[{l, t, family}]` · `correct[]` · `whyRight` ·
`whyWrong{}` · `t1Clause` · `t1Alt` · `source` (TRANSCRIBED / ASSEMBLED / AUTHORED) · `block` ·
`blockLabel`.

`block` and `blockLabel` stay **dormant and null**. If the guide later confirms shared-scenario blocks,
papers gain them by populating two fields rather than by a schema migration and a re-tag of the whole
miss history. `EXAM-FACTS_v1.md` records the block question as OPEN and nothing here resolves it.

**`lessonKey`** — added Paper 1, `GENERATION-INTELLIGENCE.md` F-10. The underlying corpus facet's
`answer` text, lowercased, punctuation-stripped, token-sorted (same normalisation `STEM-LEDGER.md`'s
dedup already uses). Populate it at assembly time from `plan.json`'s `facet.answer` — the same source
the correct-answer letter and family assignments already come from — never invented at authoring time.
Leave `""` for an item with no facet (a misconception-unit item). This is what makes cross-domain
lesson collision a property of the *shipped file itself*, checkable by `validateItems()` without any
external corpus or ledger access: two items independently drawn from different sections can carry the
identical `answer` text (Paper 1 shipped two such pairs — D4 §4.11 vs D2 §2.8, and D5 §5.6 vs D4 §4.10
— found only because a coordinating pass compared every item's facet text pairwise, since no
per-domain authoring agent can see another domain's output). Before `lessonKey` existed, this check
required `plan.json`, which is session-scratch and does not survive between sessions — the whole reason
the check "existed" only as something run by hand at generation time rather than as a durable gate.

---

## Phase 6 — Fidelity gate

Ordered. A paper that has not produced this table has not finished generating and may not be sat.
Checks 1–4 are structural and run first, because a structurally broken paper makes every later check
meaningless. 5–9 are fidelity. 10–13 are dedup and difficulty, and run last because their fixes can
reintroduce failures in 5–9.

| # | Check | Pass condition |
|---|---|---|
| 1 | **`validateItems()` in a Node `vm` on the shipped file** | Exits clean: 63 items, `g` sequential and unique, every item has `whyRight`, every non-correct option has a `whyWrong`, every multi-response stem states its count |
| 2 | **Domain quota** | Exactly 11/8/12/10/9/9/4, or the declared weakness-adjusted values |
| 3 | **Per-item `domain` tag vs its own citations** | Every item's `domain` matches the domain of every section cited in its `whyRight` and all `whyWrong` |
| 4 | **Cited sections exist** | Every `§N.M` resolves to a real heading in the file it names |
| 5 | **Objective coverage** | All 38 have ≥1 item; none has >3 |
| 6 | **Correct-answer letter tally** | Across the 55 single-answer items no letter is below 12 or above 16, and the achieved sequence matches the §5.1 pre-plan |
| 7 | **Multi-response pairs** | No correct pair appears more than twice across the 8; all 8 stems state their count |
| 8 | **Style budget** | Every stem ≤45 words, every option ≤20, within-item spread ≤8, stem median inside 28–40 |
| 9 | **Framing and token rate** | 0 invented company/product/persona names. Inline code/config tokens ≤15% of options, none in D1/D5/D6 |
| 10 | **Distractor families** | 3 different families per item; no family >47; EVIDENCE-MISMATCH ≥15; DETECTIVE-FOR-PREVENTIVE ≥9; ARCHITECTED ≤19 |
| 11 | **Dedup** | Every stem **<0.30 Jaccard** against `STEM-LEDGER.md`. **No two items share a non-empty `lessonKey` — mechanized in `validateItems()` as of Paper 1, needs no external file.** No `(section, facet, shape)` triple used more than twice historically |
| 12 | **Professional-tier floor** | Every item passes T1–T4; `t1Clause` and `t1Alt` populated on every item |
| 13 | **Targeting satisfied** | Every Professor's Note triple has ≥1 item from the opposite direction; ≥3 triples deliberately untargeted and named |

Report all thirteen with computed values, thresholds, and any fix applied.

**Re-run checks 2, 3, 6 and 10 after any fix that swaps or reorders an item.** A swapped item carries
its own domain, letter and family, and can reintroduce exactly what the earlier check cleared.

**Check 3 is the one that has already failed elsewhere and is still open.** Foundations shipped Exam 20
Q55 tagged D3 with every citation in D4; the block-level check passed because both were primary domains
for that block. Run it per item, never per block.

**On check 11's threshold.** 0.30, not the Foundations 0.40. Calibrated in `STEM-LEDGER.md` against all
1,128 pairs among the 48 seeded stems: independent pairs top out at 0.207 and the one known duplicate
sits at 0.480. Recalibrate after Paper 1 adds 63 full-length stems.

Checks 1, 6, 8, 9, 10 and 11 are mechanisable. Build the script at **Paper 4**, when check 11 is running
Jaccard against a ledger of 237 stems and hand-checking stops being reliable.

---

## Phase 7 — Targeting and the shape policy

### 7.1 What a miss produces

Each miss yields a **targeting triple** `(section, facet, direction)`. The Professor's Note ranks them
by evidence strength. Four rules bind the next paper:

1. Every triple gets **≥1 item**, from the **opposite** facet or the opposite direction. Same triple,
   same direction is banned.
2. Triples are satisfied **inside** the fixed domain quota. The Note never changes quotas — that is the
   confirmed-weakness rule's job, and the two must stay separate.
3. **Untargeted control set.** Every paper leaves ≥3 previously-missed triples deliberately untargeted
   and records which. Untargeted recovery is stronger evidence than targeted recovery, and it can only
   be claimed if the omission was recorded up front.
4. **Habit escalation.** If one distractor family captures ≥3 items across two consecutive papers, it is
   a habit and not a gap. The next paper places that family's shape as the **correct** answer on 2–3
   items, so recognising the shape stops being a safe heuristic.

Rule 4 is the only mechanism here that attacks root `CLAUDE.md` habit 3 directly — "choosing an option
because of how it *sounds* — safer, more architected, more thorough — rather than because it matches the
requirement the scenario actually states." Banning a shape teaches avoidance. Making it sometimes
correct teaches discrimination.

### 7.2 Pattern familiarity, as a phased policy

Ram names pattern recognition as one of two decisive factors on Foundations, where it was built by
accident and then banned as a defect. Neither is right. Shape repetition is scheduled:

- **Papers 1–3 · build recognition.** The eight shapes in `ARCHETYPE-LEDGER.md`, each appearing 6–9
  times per paper with entirely different content. Within-paper dedup is enforced on `(section, facet)`,
  **not** on shape.
- **Papers 4–7 · break the reflex.** Same eight shapes, each appearing at least twice with its direction
  inverted, per the inversion table in the archetype ledger.
- **Papers 8–10 · rehearse under the clock.** Shape and direction randomised, Exam Mode, full 120
  minutes, no per-question feedback.

**The measurement that says this worked, rather than producing false confidence: mean seconds-per-item
falls across Papers 1→7 while accuracy holds or rises.** If accuracy falls as pace rises, recognition is
substituting for knowledge, and the Foundations ban-list's warning applies — its own audit conceded that
an unknown share of Exams 7–13's correct answers was template recognition rather than knowledge.

### 7.3 The series

| Paper | Mode | Source | Targeting | Shape policy | What changes |
|---|---|---|---|---|---|
| 1 | Practice | TRANSCRIBE | none — diagnostic | 8 shapes, content-varied | Objective floor pass only. Establishes the per-objective baseline |
| 2 | Practice | AUTHOR | P1 triples, inverted | same 8 | First Professor's Note consumed |
| 3 | Practice | AUTHOR | P2 triples | same 8 | **Insights Round 1** after scoring |
| 4 | Practice | AUTHOR | P3 triples + first habit check | direction-inverted | Habit remedy fires if a family qualifies. Gate script built. D2 expansion decision due |
| 5 | Practice | AUTHOR | rolling triples | direction-inverted | Confirmed-weakness adjustment first eligible to fire twice running |
| 6 | Practice | AUTHOR | rolling triples | direction-inverted | **Insights Round 2** |
| 7 | Practice | AUTHOR | **none — deliberate control** | direction-inverted | The untargeted paper. Recovery here is the real evidence |
| 8 | **Exam** | AUTHOR | rolling triples | randomised | First full-clock dress rehearsal, no per-question feedback |
| 9 | Practice | AUTHOR | facets missed ≥1 time across P1–P8 | randomised | The remediation paper. **Insights Round 3** |
| 10 | **Exam** | AUTHOR | none | randomised | Final rehearsal, ~2 weeks before the sitting |

Ten papers matches `ROADMAP.md` Phase 4's own target and Phase 5's requirement of two Exam Mode papers
before booking.

---

## Phase 8 — Write the generation entry

Append to `EXAM-LOG.md`:

- Mode (TRANSCRIBE / AUTHOR) and which Professor's Note and Insights Round were consumed.
- The quota used, and any confirmed-weakness adjustment with its justification.
- Sections and facets targeted, with the direction of each retest.
- Sections deliberately left untargeted.
- The full fidelity-gate table with computed values.

Then write the `DASHBOARD-DATA.jsonl` line with null scores, per `DASHBOARD-SCHEMA.md`.

Then **rebuild** `STEM-LEDGER.md`, `FACET-LEDGER.md` and `ARCHETYPE-LEDGER.md` from the shipped HTML
file — never from this session's own account of what it wrote. Foundations lost two seed records to
prose self-report and recovered only one of them.

---

## Phase 9 — After the sitting

1. Score from the results JSON. Split single-answer from multiple-response.
2. Log every miss with the full field set in §9.1 below.
3. Run the confirmed-weakness check against the paper attempted immediately before this one **by date**,
   on **single-answer items only**. A tie records `false`.
4. Classify each miss by capturing distractor family. Families that recur are habits and need §7.1
   rule 4, not more of the same testing.
5. Note pace. Misses slower than the paper average are decision errors, not time pressure — on
   Foundations every miss cluster turned out to be considered-and-wrong.
6. Write the Professor's Note for the next paper, ranked by evidence strength.
7. If this scoring brings the count to a multiple of 3, run an Insights Round.
8. Append a session entry to `GENERATION-INTELLIGENCE.md`.

### 9.1 Per-miss fields

| Field | Why it is logged |
|---|---|
| `q` | position |
| `domain` · `section` · `facet` | the addressable unit. A miss with no section reference cannot become a pattern |
| `objective` | the score-report unit. Six objectives came back at 0% on CCAR-F |
| `shape` | feeds the shape-fatigue check and the pace measurement |
| `format` (single / multi-`selectN`) | the all-or-nothing leak lives here |
| `picked[]` · `correct[]` | full sets, not a boolean. This is what makes a partial-credit rescore possible |
| `pickedFamily` | which of the eight families captured him. The habit signal |
| `direction` | which side of the section's axis the miss fell on |
| `seconds` · `paperMeanSeconds` | fast = time pressure; slow = a decision error |
| `t1Clause` | the constraint the item was built around. A miss that ignored it is "did not read the constraint", which needs a different remedy from "does not know the material" |

---

## Deliberately not ported from Foundations

- **The 4-of-6 scenario draw and block × domain allocation.** It rests on a pool structure the CCAR-P
  guide never describes. `block`/`blockLabel` stay dormant in the schema so this is reversible at zero
  cost.
- **The Key Distinctions file as a separate seed bank.** Foundations needed it because its corpus
  sections were explanatory. CCAR-P's corpus already names a discriminator per section and tags every
  distractor by family; a separate trap file would duplicate the corpus and drift from it.
- **The KD seeding cap.** Foundations recorded this target as structurally unreachable and needing Ram's
  decision. Do not import an unresolved conflict.
- **The five-branch `SESSION-STATE.md` recovery.** Add it if a CCAR-P generation session is ever
  interrupted mid-paper. Not before.
- **`archetype_gate.py` at Paper 1.** Correctly deferred. Build it at Paper 4 — see Phase 6.
