# CCAR-P Generation Intelligence Log

AI-to-AI working memory for the mock-exam engine. A generating session reads this at Phase 1 and appends
to it at Phase 8. It carries no scores — `EXAM-LOG.md` is the only file that does.

**What belongs here:** what a generation session learned that the next one needs and cannot re-derive
cheaply. Distractors that turned out weak, shapes going stale, sections that read heavier than their use
count suggests, findings that are open, decisions that are pending.

**What does not:** standing, domain percentages, anything with a score in it.

---

## The reconciliation promotion gate

A finding recorded here is not acted on until it is promoted. Promotion requires one of:

1. **Two independent observations** across different papers, or
2. **One observation plus a computed check** confirming it from a shipped file, or
3. **Ram's explicit decision** for anything touching a corpus file.

An unpromoted finding stays in the Open Findings ledger and is re-read each session. It never silently
becomes a rule.

This gate exists because the Foundations log accumulated three separate conditions — a seed logged in one
file that never reached the tracker, a KD cap that had become structurally unreachable, a reconciliation
that was noted and never performed — each of which was recorded correctly and then had nothing forcing
it to resolve. One was recoverable. One was lost permanently. The SOP the CCAR-P engine was built from
omits this gate; it is added here.

---

## Session 1 — 2026-08-29 — Engine build

No paper generated. This session built the engine from
`Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md` Part C.

### What was built

| Artifact | Kind |
|---|---|
| `CCAR-P_Objective-Map_v1.md` | derived — 78 sections mapped to the 38 official objectives |
| `FACET-LEDGER.md` | derived — 351 facets, 78 misconception units |
| `STEM-LEDGER.md` | derived — 48 seeded stems, Jaccard threshold calibrated |
| `ARCHETYPE-LEDGER.md` | authored — 8 shapes, 8 distractor families, per-paper caps |
| `CCAR-P-Orchestration-Prompt_v2.md` | authored — supersedes v1 |
| `mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html` | authored — engine, `validateItems()`, demo items |
| `mock-exams/DASHBOARD.html` | authored — reads `DASHBOARD-DATA.jsonl` |

### Corpus measurements, taken once so no later session re-derives them

Extracted mechanically from the seven domain files, not estimated:

| Measure | Value |
|---|---|
| Sections | 78 |
| Decision-table facets | **351** |
| Exam scenarios | 79 |
| Tagged distractors | 158 |
| Sections carrying an `\| Objective \|` row | 62 of 78 |
| Distinct objective spellings in the corpus | 41, for 38 objectives |
| Sections with no decision table | 4 — 6.5, 7.4, 7.6, 7.7 |

Corpus distractor family distribution, all 158:

| Family | Count | Share |
|---|---|---|
| HALF-MOVE | 46 | 29.1% |
| WRONG-AXIS | 36 | 22.8% |
| REPAIR | 25 | 15.8% |
| DISCARD | 22 | 13.9% |
| ARCHITECTED | 20 | 12.7% |
| OVERSPEC | 9 | 5.7% |
| EVIDENCE-MISMATCH | 0 | — |
| DETECTIVE-FOR-PREVENTIVE | 0 | — |

The last two rows are the point. They are 5 of the 9 distractors the official guide's own rationales
reject, and the corpus names neither.

### Findings from this session

**F-01 · D2 facet supply will not reach ten papers. — PROMOTED (computed check).**
D2 holds 18 facets against 8 items per paper: 2.2 papers before every distinct decision repeats.
Sections 2.6, 2.7, 2.8 and 2.9 hold exactly one facet each. Direction doubling takes D2 to 4.5 papers
and misconception units to 5.6. **Papers 1–5 are reachable; 6–10 are not.** D2 needs roughly 20 more
decision-table rows. Touches corpus files, so it needs Ram's decision — raise it at the Paper 4 Insights
Round at the latest, so the rows exist before Paper 6.

**F-02 · The community mocks are not independent of the official guide. — PROMOTED (computed check).**
Jaccard across all 1,128 pairs of the 48 seeded stems: independent pairs top out at 0.207, and one pair
sits at 0.480 — ExternalMock-1 Q11 against official sample 2. They are the same item. The community set
derived at least one question from the guide. Two consequences: the ExternalMock papers are worth less
as independent practice than their item count suggests, and the 2.3× separation between that pair and
the independent maximum is what makes a Jaccard gate usable here.

**F-03 · The Foundations 0.40 Jaccard threshold is too loose for CCAR-P. — PROMOTED (computed check).**
Set to **0.30**. Foundations set 0.40 on a 51.5-word stem median; CCAR-P caps stems at 45 words and the
official samples run 29–37, so there is less room to accumulate overlap. Recalibrate after Paper 1 adds
63 full-length stems, and expect the independent maximum to rise above 0.207 because the 45 ExternalMock
stems average only 15.3 words. If it passes 0.25, move the threshold to 0.35.

**F-04 · The Foundations inline-code-token mechanism is inverted for this exam. — PROMOTED (computed
check).** Foundations enforces a 20–25% floor from its own exam's measured 21%. The CCAR-P guide's 12
sample options contain **zero** inline code or config tokens. The rule here is a ≤15% ceiling. Copying
the Foundations mechanism unchanged would have made every CCAR-P paper measurably less like its own
exam — the clearest case in the build where mimicking the sibling project reduces fidelity.

**F-05 · Sixteen sections were assigned to objectives by judgement, not by the corpus. — OPEN.**
Only 62 of 78 sections declare an objective. The other 16 are mapped in
`CCAR-P_Objective-Map_v1.md`'s audit table with a stated reason each. If any is wrong the cost is one
objective over-covered and another under-covered on every paper, visible in fidelity-gate check 5.
Review after Paper 1's objective breakdown, when there is evidence rather than judgement.

**F-06 · The ARCHITECTED cap works against Ram's most documented habit. — OPEN.**
Root `CLAUDE.md` habit 3 is the pull toward the more-architected option, and the official samples reject
zero distractors for over-architecting, so the family is capped at 10%. That reduces practice against the
habit. The intended remedy is Phase 7.1 rule 4 — make the architected option *correct* on 2–3 items once
the family qualifies as a habit — but that is untested. Watch ARCHITECTED capture rate on Papers 1–3
before trusting the cap.

**F-07 · TRANSCRIBE mode cannot produce a multiple-response item. — PROMOTED (computed check).**
The corpus holds no multi-response scenario. Paper 1 therefore ships 55 TRANSCRIBED + 8 ASSEMBLED, where
ASSEMBLED items use verbatim corpus option text in an authored combination. Tagged `source:"ASSEMBLED"`
so the distinction survives into the miss log. Without this, Paper 1 would carry zero practice against
Ram's largest documented scoring leak.

> **Superseded 2026-08-30 — the finding holds, its Paper 1 conclusion does not.** The paragraph above is
> Session 1's text, left as written. Its premise is still a live corpus fact and still binds every paper:
> the corpus holds no multiple-response scenario, so all eight multi-response items must be authored,
> drawn from sections whose decision table holds two independently-true rows for one situation.
>
> What is no longer true is everything downstream of "Paper 1 therefore". **F-08 rejected TRANSCRIBE
> outright** the next day, so the 55/8 split never happened and the ASSEMBLED escape hatch was never
> needed — a mode that produces no items needs no exception for the items it cannot produce.
> **Paper 1 shipped 2026-08-30 with 63/63 items tagged `source:"AUTHORED"` and zero tagged `ASSEMBLED`
> or `TRANSCRIBED`.** Verified against the shipped file, not against this log.
>
> Do not read this finding as an instruction to tag anything `ASSEMBLED`. See F-08, and
> `CCAR-P-Orchestration-Prompt_v2.md` §2.

### Coverage trackers — empty until Paper 1

**Facet freshness:** see `FACET-LEDGER.md`. All 351 unused.
**Shape rotation:** see `ARCHETYPE-LEDGER.md`. All 8 unused.
**Family capture rates:** no data.
**Weak distractors:** no data.
**Effective patterns:** no data.

### Open findings ledger

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | **promoted** | Ram decides on ~20 new D2 decision rows |
| F-02 | Community mocks derive from the guide | **promoted** | — recorded, no action needed |
| F-03 | Jaccard threshold 0.30 | **promoted** | Recalibrate after Paper 1 |
| F-04 | Token rate inverted vs Foundations | **promoted** | — in force |
| F-05 | 16 objective assignments are judgement | open | Paper 1 objective breakdown |
| F-06 | ARCHITECTED cap vs habit 3 | open | ARCHITECTED capture rate over Papers 1–3 |
| F-07 | TRANSCRIBE cannot do multi-response | **promoted** | — Session 1 resolved it with the ASSEMBLED tag; **superseded 2026-08-30**, see the note under F-07 |

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01). Blocks Paper 6. Needed by the Paper 4 Insights Round.
2. **Fidelity-gate script** at Paper 4. Deferred deliberately; revisit when check 11 runs against 237
   stems.

### Session reflection

The audit estimated ~300 facets at roughly 4 per section and concluded the corpus supported ten papers
with no facet reused. The measured figure is 351 facets, but distributed so unevenly that the conclusion
does not hold: D4 has 7.0 papers of supply and D2 has 2.2. An average computed over a skewed
distribution said the corpus was fine when its narrowest domain was not. Any future capacity claim
should be made per domain, against that domain's own quota, and never from a corpus-wide total.

---

## Session 2 — 2026-08-30 — Paper 1 generated

`mock-exams/CCAR-P_MockTest-1_v1.html`. AUTHOR mode (TRANSCRIBE rejected — see F-08). Full detail,
fidelity-gate result, and the token-cost audit are in `EXAM-LOG.md`'s Paper 1 entry. What belongs here
is what the *next* generating session needs and cannot re-derive cheaply.

### Findings from this session

**F-08 · TRANSCRIBE mode makes the key guessable by length. — PROMOTED (computed check).**
84% of the corpus's 79 ready-made scenarios have the correct answer as the longest option (chance is
~33%). A verbatim paper would be answerable without reading most stems. AUTHOR mode was used instead;
every authored item's option-length spread is capped and checked (paper-wide key-longest rate: 0/63,
2%, well under the 40% ceiling). Do not revert to TRANSCRIBE for any future paper.

**F-09 · A dispatched verify/reverify prompt must never require a literal `correct` field on the
AUTHORING-stage item JSON. — PROMOTED (computed check).** The item schema is deliberately built without
one: correctness is encoded by `family: null` on the correct option(s), and only gets a `correct` array
added later, at assembly time, when the ledger's `plan.json` correct-letter assignment is written in.
A verify prompt that checks the raw authoring output for a `correct` field will always false-positive.
This produced 5 false JSON_VALID findings on Paper 1 (D3 and D7), caught and discounted by hand before
the final repair pass. **If a future session writes its own author/verify/repair prompts from
`CCAR-P-Orchestration-Prompt_v2.md`, do not add this check** — only the FINAL SHIPPED item (post-assembly,
inside the HTML) has a `correct` field, and `tools/run-gate.js`'s own `validateItems()` already checks
that correctly.

**F-10 · The cross-domain lesson-collision check now exists as a mechanized field, not a manual step. —
PROMOTED (implemented this session).** Paper 1 shipped with two items independently drawn from
different domains testing the identical underlying corpus decision — g36 (D4 §4.11) and g16 (D2 §2.8)
both "order static content first, enable caching"; g44 (D5 §5.6) and g35 (D4 §4.10) both "confidently
wrong after a refresh → check retrieval/indexing first." No per-domain authoring agent could see this;
it was found by comparing every item's underlying facet **answer text** pairwise, by hand, after all
seven domains returned. That text is not in the shipped item schema (only the facet ID string is), so
the check could not be mechanized into `tools/run-gate.js` without a schema change. Both are fixed now:
- Every item's shipped JSON carries a new `lessonKey` field — the facet's answer text, lowercased,
  punctuation-stripped, token-sorted (the same normalisation `STEM-LEDGER.md`'s dedup already uses).
- `mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html`'s `validateItems()` now flags any two items sharing an
  identical non-empty `lessonKey` as a gate ERROR (folded into check 11, dedup). `tools/run-gate.js`
  inherits this automatically — it only calls `validateItems()` from whatever file it's pointed at.
- `CCAR-P-Orchestration-Prompt_v2.md` §5.5 (item schema) and Phase 6 (fidelity gate) are updated to
  document `lessonKey` and the check as mechanized, not manual.
- Paper 1's shipped HTML was regenerated with `lessonKey` populated on all 63 items and re-passed the
  gate (0 errors, 0 lesson collisions found — the two known ones were already fixed by hand before this
  field existed).
A future session generating Paper 2 must populate `lessonKey` from `plan.json`'s facet-answer text when
assembling items, the same way `facet`, `objective`, and `shape` are already populated.

**F-11 · An independent token-cost audit measured Paper 1's real generation cost at ~7.7–8M tokens,
roughly double what the generating session believed it had spent (~4.3M, from only the dispatches with
a printed aggregate). — PROMOTED (computed check, full report in `EXAM-LOG.md` finding 8).** The single
largest gap: a background workflow's `resumeFromRunId` was believed to replay already-completed calls
from cache; it measurably did not, re-dispatching 6 already-succeeded domains' verify calls plus one
already-succeeded author call, at a cost of 1,166,297 tokens for work that had already finished. A
retry storm during the triggering interruption cost a further ~1.68M tokens for zero output. **Do not
trust a resumed workflow's cost to be near-zero without checking its journal for duplicate dispatches of
already-`result`-ed keys.** Six further named fixes (collapsing the 4-stage pipeline into one persistent
conversation per domain, explicit `effort` tiers on Author/Repair, a retry cooldown) are cost
optimisations for whoever builds Paper 2's generation script, not corpus or design changes — they don't
belong in this file's promotion gate, but skipping them means Paper 2 likely costs similarly to Paper 1.

### Open findings ledger — updated

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | promoted | Ram decides on ~20 new D2 decision rows |
| F-02 | Community mocks derive from the guide | promoted | — recorded, no action needed |
| F-03 | Jaccard threshold 0.30 | promoted | Recalibrate after Paper 1 — **still open, see F-03 below** |
| F-04 | Token rate inverted vs Foundations | promoted | — in force |
| F-05 | 16 objective assignments are judgement | open | Paper 1 objective breakdown |
| F-06 | ARCHITECTED cap vs habit 3 | open | ARCHITECTED capture rate over Papers 1–3 |
| F-07 | TRANSCRIBE cannot do multi-response | promoted | — premise still binds (all 8 multi items authored); the ASSEMBLED resolution is moot, F-08 rejected TRANSCRIBE entirely and Paper 1 shipped 63/63 AUTHORED |
| F-08 | TRANSCRIBE key-longest at 84% | **promoted** | — resolved, AUTHOR mode used |
| F-09 | No `correct` field on authoring-stage JSON | **promoted** | — documented, do not reintroduce |
| F-10 | Lesson-collision check mechanized via `lessonKey` | **promoted** | — implemented, verify on Paper 2 |
| F-11 | Real generation cost ~7.7–8M tokens, resume duplicated work | **promoted** | Cost-optimisation fixes are Paper 2's generating session's call |

**F-03 recalibration, still due**: `STEM-LEDGER.md`'s 0.30 threshold was set on 48 short seeded stems.
Paper 1 added 63 full-length (28–45 word) stems to that ledger. Recalibrate before Paper 3.

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01). Blocks Paper 6. Needed by the Paper 4 Insights Round.
2. **Fidelity-gate script** at Paper 4. Deferred deliberately; revisit when check 11 runs against 237
   stems.
3. **Cost-optimisation fixes from F-11** — collapsing the 4-stage pipeline, explicit effort tiers, a
   retry cooldown, resume-duplicate-dispatch prevention. None touch the corpus or the paper's content;
   all touch how Paper 2 onward should be generated. Worth a decision before Paper 2, since the same
   ~7.7–8M-token cost will likely repeat otherwise.

### Session reflection

Two of this session's three findings (F-09, F-10) are bugs in the generating session's OWN verification
tooling, not in the corpus or the exam content — caught only because an independently-dispatched
reverify stage and, separately, an independently-dispatched cost audit were both told explicitly not to
trust the generating session's own account of what it had done, and to check the artifacts cold. That
pattern held twice in one paper. It is worth keeping as standing practice, not a one-off.
