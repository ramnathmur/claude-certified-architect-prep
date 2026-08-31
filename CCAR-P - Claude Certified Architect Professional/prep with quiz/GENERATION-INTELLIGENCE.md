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

---

## Session 3 — 2026-08-30 — Deep-dive explanation layer added to the engine

No paper was generated. The engine gained a second per-item explanation layer and a pass/fail running
accuracy indicator, both in `mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html` so every future paper
inherits them, and both backfilled into Paper 1. Full detail is in
`../Outputs/CCAR-P_DeepDive-Grounding-Record_v1.md`. What belongs here is what the *next* generating
session needs and cannot re-derive cheaply.

### What changed in the engine

- **Item schema gained `deepDive{principle, rightDeep, wrongDeep{}}`** — documented in
  `CCAR-P-Orchestration-Prompt_v2.md` §5.5, with the render policy in §5.6. Required on every item
  from Paper 1 onward. `whyRight`/`whyWrong` are unchanged and are not what it replaces.
- **`validateItems()` gained one presence check**, structurally identical to the `whyWrong` check it
  sits beside: `principle` and `rightDeep` non-empty, `wrongDeep` holding an entry for every
  non-correct option and none for a correct one. No existing pass condition was altered. It is a
  presence check only — grounding cannot be checked from a file that carries no corpus.
- **`PASS_PCT_THRESHOLD = 620/9`**, the inversion of `estimateScaled()` against the 720 pass line.

### Findings from this session

**F-12 · 13 of 63 Paper 1 items record a `t1Alt` that resolves to no corpus row. — PROMOTED
(computed check).**
§5.3's T1 test assumes the alternative answer "is already written down — it is the row of the same
decision table where the other option wins." For 13 items no such row exists anywhere in the domain
file, and deleting the recorded `t1Clause` does not surface one: g5, g12, g13, g14, g17, g18, g35,
g44, g54, g55, g59, g60, g63. **Gate check 12 passes all of them, because it asks only that
`t1Clause` and `t1Alt` be populated, never that `t1Alt` resolve to a row.** Nothing had read them
closely enough to notice until a per-item corpus pass was run against every cited section.
**Six of the thirteen are D2**, which F-01 already flags as the binding supply constraint — a second,
independent route to the same conclusion. Do not change Paper 1's recorded values; they feed the miss
history. For Paper 2 onward, resolve `t1Alt` to a named row at authoring time, or pick a different
`t1Clause`.

**F-13 · A per-domain authoring agent cannot check its own grounding. — PROMOTED (two observations).**
Seven authoring agents each read only their own corpus file and wrote deep explanations for their own
items. Two independent grounding passes, given the corpus and the output but never the author's
reasoning, raised 67 findings between them; 54 were real and were repaired. The recurring failure was
not invention but *mis-paraphrase*: a decision-table row quoted with a load-bearing precondition
silently dropped, a misconception attributed to a section that does not carry it, a family named that
conflicts with the item's own tag. An author asked to check its own grounding reliably finds its own
paraphrase sufficient. This is the same pattern Session 2 recorded for F-09 and F-10, now on a third
kind of work.

**F-14 · Some findings are properties of the item, not of the text under review. — OPEN.**
The second grounding pass was asked to classify each finding FIXABLE or IRREDUCIBLE, and 13 of 34 came
back IRREDUCIBLE — every one an F-12 case, where no rewrite could name a row the corpus does not
contain. Without that split, a repair loop rewrites the same honest text every round and never
converges. Worth building into any future adversarial-review stage; untested beyond this one use.

### Open findings ledger — updated

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | promoted | Ram decides on ~20 new D2 decision rows — **F-12 is a second signal** |
| F-02 | Community mocks derive from the guide | promoted | — recorded, no action needed |
| F-03 | Jaccard threshold 0.30 | promoted | Recalibrate before Paper 3 |
| F-04 | Token rate inverted vs Foundations | promoted | — in force |
| F-05 | 16 objective assignments are judgement | open | Paper 1 objective breakdown |
| F-06 | ARCHITECTED cap vs habit 3 | open | ARCHITECTED capture rate over Papers 1–3 |
| F-07 | TRANSCRIBE cannot do multi-response | promoted | — premise binds; ASSEMBLED resolution superseded, see the note under F-07 |
| F-08 | TRANSCRIBE key-longest at 84% | promoted | — resolved, AUTHOR mode used |
| F-09 | No `correct` field on authoring-stage JSON | promoted | — documented, do not reintroduce |
| F-10 | Lesson-collision check mechanized via `lessonKey` | promoted | — implemented, verify on Paper 2 |
| F-11 | Real generation cost ~7.7–8M tokens | promoted | Cost fixes are Paper 2's session's call |
| F-12 | 13 items' `t1Alt` resolves to no corpus row | **promoted** | Resolve `t1Alt` to a named row at authoring time, from Paper 2 |
| F-13 | Authors cannot grade their own grounding | **promoted** | — standing practice, keep the pass separate |
| F-14 | FIXABLE vs IRREDUCIBLE finding split | open | Reuse on Paper 2's review stage, then judge |

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01, now also F-12). Blocks Paper 6. Needed by the Paper 4 Insights Round.
2. **Fidelity-gate script** at Paper 4. Deferred deliberately.
3. **Cost-optimisation fixes from F-11.** Worth a decision before Paper 2.
4. **Should gate check 12 resolve `t1Alt` to a row** (F-12), rather than only checking the field is
   populated? It would have caught all thirteen. It needs corpus access at gate time, which check 1
   deliberately does not have, so it is a real design change and not a one-line fix.

### Session reflection

The engine's own gate passed Paper 1 on a field it never actually validated. `t1Clause`/`t1Alt` were
populated on all 63 items and check 12 was satisfied; that thirteen of them pointed at options the
corpus never makes correct only surfaced because unrelated work — writing an explanation of *why* each
wrong option is wrong — forced every cited section to be read against every option. A check that
verifies a field is filled in is not the same as a check that verifies it is true, and the gap between
those two is invisible until something reads the content.

---

## Session 4 — 2026-08-30 — Paper 2 generation failed outright; `deepDive` demoted after independent audit

No paper shipped this session. Attempted Paper 2 generation with a redesigned pipeline (inline
`deepDive`, one grounding pass instead of four stages, Agent tool instead of Workflow — the F-11 cost
fixes) and it failed completely: of 7 parallel per-domain authoring dispatches, only the smallest (D7,
4 items) succeeded; all 6 others (D1-D6, 8-12 items each) failed with an identical `"stream watchdog"`
stall and zero partial output, including on retry for four of them. Ram asked for an independent,
arms-length audit rather than another self-directed patch — full detail in
`Outputs/CCAR-P_Mock-Exam-Generation-Cost-Audit_v1.md` and this session's `resume-prompt.md`. What
belongs here is the decision the audit produced and what the next generating session needs to know.

### Findings from this session

**F-15 · `deepDive` was the single largest, least-evidenced cost addition in the engine, and the
project's own grounding record already shows it overreaches the corpus. — PROMOTED (Ram's explicit
decision, 2026-08-30, after an independent cold audit).**
Unlike every other mechanism in `CCAR-P-Orchestration-Prompt_v2.md` — each traceable to a specific,
named, measured failure (the objective floor pass to CCAR-F's six 0% objectives, the letter pre-plan to
a real same-letter block, the inline-token ceiling to the official guide's 0/12 rate) — `deepDive` has
no such citation anywhere in the project; it does not appear once in the original 91KB
`Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md`. It roughly triples per-item prose (500-700 words vs.
80-140 for the existing `whyRight`/`whyWrong` layer) and requires its own dedicated grounding-audit
pipeline. `CCAR-P_DeepDive-Grounding-Record_v1.md` already documented, before this session, that 28 of
Paper 1's 63 items (44%) hit a real grounding shortfall in this layer alone — 13 flatly IRREDUCIBLE
(F-12/F-14). Separately, today's failure data shows item-count-per-dispatch (not corpus file size)
cleanly separates the one success from all six failures — see the cost-audit report's table. **Decision:
`deepDive` is demoted from a mandatory generation-time field to a deferred, miss-driven Phase 9
addition.** A freshly generated item now ships `deepDive: null`; Phase 9 (§ orchestration prompt, "After
the sitting") generates it only for items actually missed, at that same small scale, independently
grounding-audited at that scale rather than all 63 up front. Mechanics: `CCAR-P-Orchestration-Prompt_v2.md`
§5.5/§5.6/Phase 9 updated in place (correction kept alongside the original text, same convention as the
TRANSCRIBE-rejection note in §2); `validateItems()` in both the template and any already-copied Paper 2
file changed so `deepDive: null` is not an error unless the caller passes `opts.requireDeepDive`.
**Paper 1 is not touched — it already shipped its `deepDive` layer and keeps it.**

**F-16 · Dispatch granularity, not corpus size, predicted today's failures. — PROMOTED (computed check,
in the audit report).**
Cross-checking today's 7 dispatches against their corpus file size and item count: D2 had the
*smallest* corpus file (15,564 bytes) of all seven and still failed; D7's corpus file was not the
smallest and it succeeded. Item count is what cleanly separates the outcome — D7 was asked for 4 items
and succeeded; every domain asked for 8-12 items failed, without exception, across two attempts each
for four of them. This does not prove a specific infrastructure root cause (the controlled isolation
test — one mid-size domain dispatched alone — was never run), but it is a strong, reproducible signal
that a single authoring turn should not be asked to produce a full domain's worth of items in one
uninterrupted, unpersisted turn. **Decision: from Paper 2 onward, split each domain's authoring dispatch
into sub-batches of roughly 5-6 items, each persisted to its own file immediately on completion**,
instead of one file written per domain at the very end. Domain-level parallelism itself is unchanged and
still spec-mandated (§5.5: "one worker per corpus file") — only the unit of work *inside* that changed.
This is a process choice, not a spec change, so it is not reflected in the orchestration prompt itself.

### Open findings ledger — updated

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | promoted | Ram decides on ~20 new D2 decision rows — F-12 is a second signal |
| F-11 | Real generation cost ~7.7-8M tokens | promoted | Attempted fix this session (inline deepDive, one grounding pass, Agent not Workflow) did NOT resolve it — generation failed outright instead. F-15/F-16 are the corrected fix |
| F-12 | 13 items' `t1Alt` resolves to no corpus row | promoted | Still applies to Paper 1; Paper 2 onward still must resolve `t1Alt` to a named row at authoring time regardless of the `deepDive` timing change |
| F-13 | Authors cannot grade their own grounding | promoted | — standing practice; still applies once Phase 9 grounding-audits a miss set |
| F-14 | FIXABLE vs IRREDUCIBLE finding split | open | Reuse whenever Phase 9 runs its grounding audit on a miss set |
| F-15 | `deepDive` demoted to deferred Phase 9 addition | **promoted** | Implemented this session — engine and spec both updated |
| F-16 | Dispatch granularity (not corpus size) predicted today's failures | **promoted** | Sub-batch dispatch (~5-6 items) adopted this session; re-verify it actually prevents stalls on the retry |

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01, F-12). Blocks Paper 6. Needed by the Paper 4 Insights Round.
2. **Fidelity-gate script** at Paper 4. Deferred deliberately.
3. ~~Cost-optimisation fixes from F-11~~ — attempted this session, insufficient on its own; superseded
   by F-15/F-16.
4. Should gate check 12 resolve `t1Alt` to a row (F-12)? Still open, unrelated to this session's changes.
5. **Untested: whether sub-batch dispatch (F-16) actually eliminates the stall, or whether it recurs
   even at ~5-6 items per turn.** If it recurs at that size too, the driver is not item count/output
   length after all, and the investigation needs to look at infrastructure directly (see the cost audit
   report's §2.2 for the controlled test that was never run).

### Session reflection

Two rationalizations of the same underlying problem (generation cost/reliability) happened back to
back: F-11's cost-optimisation fixes were proposed, implemented this session, and failed to prevent an
outright generation failure — worse than Paper 1's own experience, which at least finished. What broke
the pattern was not more self-directed tuning but stopping and dispatching a genuinely independent
review with explicit permission to conclude the design itself was wrong, briefed on exactly what to be
skeptical of (including this same session's own resume-prompt.md). It found something neither prior
pass had named: `deepDive` itself, added without the evidentiary discipline every other mechanism in
this project is held to, was the largest cost and the thing already shown (before this session) to
outrun the corpus in 44% of a shipped paper. The lesson worth keeping: when an attempted fix to a
measured problem fails again, the next move is not a third self-authored patch — it is a cold,
independently-briefed audit that is explicitly told not to defer to the fixing session's own framing.

---

## Session 5 — 2026-08-31 — Paper 2 generated on the redesigned pipeline

`mock-exams/CCAR-P_MockTest-2_v1.html`. Continuation of Session 4's work, same day. Full narrative
(the failed first attempt, the audit, the two fixes) is in `EXAM-LOG.md`'s Paper 2 entry — this session
covers only what the *next* generating session needs from actually finishing on the redesigned shape.

### Findings from this session

**F-17 · The sub-batch dispatch fix (F-16) held completely — 13 of 13 dispatches succeeded, zero
failures. — PROMOTED (computed check).**
12 replacement sub-batches (5-6 items each, `deepDive:null`) covering D1-D6 were dispatched; all 12
eventually succeeded, joining D7 (already valid from the failed first attempt) for a clean 13-for-13.
10 finished in 11.5-17 minutes; 2 (D2-batch1, D4-batch1) took ~38-39 minutes but still completed —
notably, this did NOT repeat the first attempt's pattern where "running long" (D4/D6 at 41+ minutes)
was itself a precursor to failure. **Open question for Paper 3:** is the ~2x-3x runtime variance on 2
of 12 batches meaningful (something about those specific batches) or just normal variance at this
scale? Untested. If a future paper's batches start running consistently long without failing, that is
a cost signal worth measuring, separate from the stall question F-16 addressed.

**F-18 · The lesson-collision check (F-10) needs a minimum-token floor, discovered on first use with
real full-length Paper 2 stems. — PROMOTED (computed check, fixed same session).**
Computing `lessonKey` from each item's raw corpus answer text surfaced 3 collision groups on first
assembly. Two were false positives: `"Reject"` and `"Synchronous"` are each the literal, terse
Answer-column text for multiple, semantically unrelated decision-table rows across different sections
(and in D7's case, even within the same section, for genuinely different reasons) — a 1-2 content-word
answer is not a reliable duplicate-decision signal. Fix: `lessonKey` returns `""` (not compared) when
the normalised answer has fewer than 3 content-word tokens, rather than either falsely flagging or
silently trusting a misleading short key. This is NOT yet in the committed gate (deliberately deferred
to Paper 4 per the standing decision), but should be built into whatever script Paper 4 produces. The
third collision (g44/g37, `"application not resending history"`) was a genuine duplicate and was fixed
by repointing g44 to a different facet — the check did exactly what F-10 designed it to do.

**F-19 · The distractor-family cap needs enforcement at assembly time regardless of dispatch shape —
confirmed again, this time under sub-batching. — PROMOTED (computed check, fixed same session).**
First assembly had WRONG-AXIS at 52 of 181 distractors against a 45 cap (25%) — 12 independently
authored sub-batches each defaulted to WRONG-AXIS as a safe choice with no visibility into the
paper-wide total (the same structural risk Paper 1's per-domain-not-paper-wide authoring already
carried; sub-batching didn't introduce this, it just didn't remove it either). Fixed by relabelling 10
distractors to a family their own `whyWrong` reasoning already supported better — no content rewrite
needed, confirming the original prose was fine and only the bookkeeping tag was wrong. **This is the
second time in two papers a central, assembly-time check caught something no individual authoring
agent could see** (the first being Paper 1's cross-domain `lessonKey` collision) — the pattern is
reliable enough to treat as a standing expectation, not a one-off: budget an assembly-stage family-cap
check into every future paper's plan, not just a hope that per-batch minimums add up correctly.

**F-20 · Running the grounding audit BEFORE the generation entry is written, in the same session,
produced a large improvement in `t1Alt` resolution rate. — PROMOTED (computed check).**
58 of 63 items (92%) had their `t1Clause`/`t1Alt` pair independently verified to resolve to a real
corpus row, up from Paper 1's discovered-after-shipping rate of 50/63 (79%, F-12). The mechanism is
simple: Paper 1's grounding audit happened in a *later* session, after Paper 1 was already recorded as
generated with unverified `t1Alt` claims; this paper's audit ran before the generation entry was
written, so all 14 raised findings were fixed-or-documented before anything shipped. **Do not defer the
grounding audit to "later" on a future paper** — it belongs inside the same generation session, as a
hard gate before Phase 8 close-out, not an optional follow-up.

### Open findings ledger — updated

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | promoted | Ram decides on ~20 new D2 decision rows — now also evidenced by 3 of this paper's 5 IRREDUCIBLE T1 exceptions landing in D2 |
| F-10 | Cross-domain lesson-collision check | promoted | Still holds; F-18 refines it with a minimum-token floor |
| F-12 | `t1Alt` resolving to no corpus row | promoted | Paper 2 rate improved to 58/63 (92%) via same-session grounding audit (F-20); 5 documented IRREDUCIBLE exceptions remain (3 in D2, 1 in D3, 1 in D5) |
| F-15 | `deepDive` demoted to deferred Phase 9 addition | promoted | Held for the whole paper; 0 items needed it at generation time |
| F-16 | Dispatch granularity fix | **promoted, confirmed** | 13/13 succeeded on the redesigned shape — see F-17 for the residual runtime-variance question |
| F-17 | Sub-batch runtime variance (2 of 12 took ~3x longer, still succeeded) | open | Watch on Paper 3; may just be normal variance |
| F-18 | `lessonKey` needs a minimum-token floor to avoid false collisions | **promoted** | Fixed in the assembly script this session; fold into the Paper 4 gate-mechanization work |
| F-19 | Family-cap check must run at assembly time regardless of dispatch shape | **promoted, confirmed a second time** | Standing expectation now, budget it into every future paper's close-out |
| F-20 | Same-session grounding audit materially improves `t1Alt` resolution rate | **promoted** | Standing practice — do not defer to a later session |

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01, F-12). Blocks Paper 6. Now has a third independent signal (3 of this
   paper's 5 IRREDUCIBLE exceptions are D2). Needed by the Paper 4 Insights Round at the latest.
2. **Fidelity-gate script** at Paper 4 — now with two more things to fold in when it's built: the
   `lessonKey` minimum-token floor (F-18) and the family-cap assembly-time check (F-19), both already
   proven as one-off scripts this paper.
3. Should gate check 12 resolve `t1Alt` to a row, mechanically, rather than only checking the field is
   populated? Still open. This paper's 92% resolution rate was achieved by a grounding-audit agent
   pass, not a mechanized check — the gap F-12 originally identified (a check that verifies presence
   is not the same as a check that verifies truth) is narrowed by process this paper, not closed by
   tooling.

### Session reflection

The redesigned pipeline (F-15, F-16) was validated by actually finishing, not just by argument: 63/63
items authored, 0 gate errors, 92% `t1Alt` resolution before shipping rather than discovered after.
But two of the three assembly-time problems found this paper (the `lessonKey` false positives, the
family-cap violation) were NOT predicted by the cost audit or by either redesign decision — they only
surfaced because the paper was actually assembled and checked centrally, the same way F-10's original
lesson-collision finding only surfaced because a coordinating pass compared every item pairwise. The
standing lesson across both papers now: distributed authoring (whether 7 full-domain agents or 12
sub-batches) reliably produces excellent per-item content and reliably misses paper-wide properties no
individual agent can see — plan for a real assembly-and-check stage every time, not a formality.

---

## Session 6 — 2026-08-31 — Paper 3 generated on the redesigned pipeline, third consecutive clean run

`mock-exams/CCAR-P_MockTest-3_v1.html`. Untargeted third diagnostic (Papers 1 and 2 both generated but
neither sat by the time this session ran, confirmed with Ram before generating). Full detail is in
`EXAM-LOG.md`'s Paper 3 entry — this session covers only what the *next* generating session needs.

### Findings from this session

**F-21 · Facet freshness computed from shipped HTML, not from `FACET-LEDGER.md`'s own "used" column,
is now standing practice and worked cleanly. — PROMOTED (implemented and verified this session).**
Per §3d of `Outputs/CCAR-P_Paper-3-4-Generation-Prompt_v1.md`, a script loaded Papers 1 and 2's
`ITEMS` arrays the same way `tools/run-gate.js` does and extracted every shipped `facet` string
directly, rather than trusting the ledger's own "used" column (documented as having at least one gap).
This is what surfaced that D2 had only 2 fresh decision-table facets left, not an approximate "getting
low" — an exact count the ledger's own bookkeeping could not be trusted to give.

**F-22 · The D2 misconception-unit fallback (Phase 4 rule 5) fired for the first time and worked as
designed. — PROMOTED (implemented and grounding-audited this session).** 6 of D2's 8 items this paper
are built from a section's `Misconception` block instead of a decision-table row (M-2.1, M-2.2, M-2.4,
M-2.6, M-2.7, M-2.8), spread across 8 of D2's 9 sections. The independent grounding audit found no
structural problem the fallback format itself introduced — the 2 D2 IRREDUCIBLE findings both trace to
the underlying section's thin table, the same root cause as prior papers' D2 findings, not to
misconception-unit items being harder to ground. This was the F-01 supply-note's planned mechanism
(direction-doubling → misconception units → corpus expansion), confirmed working on the first paper
where fresh facets actually ran out.

**F-23 · Dispatch granularity (F-16/F-17) held a third consecutive time, 13/13, zero stalls, zero
retries. — PROMOTED, now settled rather than provisional.** No batch this paper ran unusually long
(unlike Paper 2's two ~38-39 minute batches) or needed a retry. Three clean runs at this shape is
enough to stop treating it as an open question for future papers' planning.

**F-24 · The `t1Alt` IRREDUCIBLE rate rose to 8/63 (13%), from Paper 2's 5/63 (8%), despite the same
same-session-audit discipline that produced Paper 2's improvement. — PROMOTED (computed check).**
3 of the 8 are in D1, a facet-rich domain (62 facets, no supply pressure), across two different
sections. This means facet-rich domains are not immune to producing an IRREDUCIBLE T1 case — which
facet a section's decision table happens to yield for a given draw matters more than that domain's
overall supply health. Extends F-14's original point (some findings are a property of the item, not
of how carefully it's checked). **Open question for Paper 4:** does the rate hold near 8/63, revert
toward Paper 2's 5/63, or is there enough data after a third data point to estimate a real baseline?

**F-25 · A same-session fix applied to satisfy a mechanized cap, without grounding-audit review, was
itself wrong — caught only because the audit ran before the generation entry was written (F-20's
discipline held for exactly the case it exists to catch). — PROMOTED (computed check, this session).**
Assembly found `DETECTIVE-FOR-PREVENTIVE` had dropped from 9 to 8 (a byproduct of rewriting an item to
fix a content collision, which removed that item's own DETECTIVE-FOR-PREVENTIVE-tagged distractor).
The fix applied at assembly time — relabelling a different item's distractor to restore the floor —
turned out, on independent audit, to be backwards: a pre-execution approval gate is a preventive
control, not a detective one. The audit's own contrast case (a different item's genuinely correct use
of the same family tag, in the same domain) is what made the error visible. Reverted, then fixed
honestly by relabelling a distractor that actually fits the family's definition (ship now, detect via
audit afterward, instead of preventing before). **Standing caution: treat any family-tag relabel made
solely to satisfy a cap as provisional until the grounding audit confirms it — do not assume a cap-fix
is self-evidently correct just because it makes the numbers work.**

### Open findings ledger — updated

| id | finding | status | resolves when |
|---|---|---|---|
| F-01 | D2 supply stops at ~5 papers | promoted | Ram decides on ~20 new D2 decision rows — **now also evidenced by the misconception-unit fallback actually firing (F-22), the mechanism F-01 predicted would be needed by this point** |
| F-10 | Cross-domain lesson-collision check | promoted | Held a third time — 0 `lessonKey` collisions this paper; the 2 real collisions found (F-26) were caught by the stem-Jaccard check instead |
| F-12 | `t1Alt` resolving to no corpus row | promoted | Paper 3 rate: 55/63 (87%) — see F-24, the IRREDUCIBLE count rose from Paper 2 |
| F-15 | `deepDive` demoted to deferred Phase 9 addition | promoted | Held for a third full paper; 0 items needed it at generation time |
| F-16/F-17 | Dispatch granularity fix | **promoted, now settled** | 13/13 succeeded a third consecutive time (F-23) — stop treating as provisional |
| F-19 | Family-cap check must run at assembly time regardless of dispatch shape | **promoted, confirmed a third time** | Held again this paper (ARCHITECTED over cap, fixed by 1 relabel) — but see F-25, a cap-driven relabel still needs audit review |
| F-20 | Same-session grounding audit materially improves `t1Alt` resolution rate | promoted | Held again — and this paper is the first time the audit also caught the *generating session's own* error (F-25), not just authoring errors |
| F-21 | Facet freshness from shipped HTML, not the ledger's "used" column | **promoted** | Standing practice from this paper forward |
| F-22 | D2 misconception-unit fallback fires and works | **promoted** | First real use, grounding-audited clean |
| F-23 | Dispatch granularity settled at 3/3 clean runs | **promoted, settled** | No longer an open question |
| F-24 | `t1Alt` IRREDUCIBLE rate variance across papers (5/63 to 8/63) | open | Watch on Paper 4; may indicate a real baseline rather than a defect |
| F-25 | Cap-driven family relabels need audit review, not just arithmetic | **promoted** | Standing caution for every future paper's assembly stage |
| F-26 | Two real cross-item content collisions found only by stem-Jaccard, not `lessonKey` | **promoted** | See detail below — both fixed this session |

**F-26 · Two genuine content collisions surfaced by the stem-Jaccard check even though `lessonKey`
found zero collisions this paper.** (a) Paper 3's own g55 (D6 §6.11, multi) scored 0.349 against Paper
2's own g55 — independently, both items combined the same section's "40 users → 800 users" and "12%
human review" facts with the same numbers. (b) Within Paper 3, g34 and g40 (both D4 §4.9) scored 0.356
against each other — g34's multi-response answer and g40's single-answer item independently tested the
identical "latency guardrail breach → do not ship" row. Both fixed (see `EXAM-LOG.md`'s Paper 3 entry
for the exact changes) and re-verified below threshold. **This means `lessonKey` and stem-Jaccard catch
different failure modes and both need to run at assembly — `lessonKey` catches two items resting on
the identical underlying answer text; stem-Jaccard catches two items built from overlapping *numbers
and phrasing* even when the underlying facet differs.** Worth folding both into the Paper 4
gate-mechanization work explicitly as complementary, not redundant, checks.

### Pending decisions for Ram

1. **D2 corpus expansion** (F-01, F-12, F-22). Blocks Paper 6. Now has direct evidence the
   misconception-unit fallback is the active mechanism, not just a contingency plan — worth surfacing
   plainly at the Paper 4 Insights Round.
2. **Fidelity-gate script** at Paper 4 — now with three things to fold in: the `lessonKey`
   minimum-token floor (F-18), the family-cap assembly-time check (F-19), and the stem-Jaccard
   cross-paper + within-paper collision check (F-26), all proven as one-off scripts across two papers
   now.
3. Should gate check 12 resolve `t1Alt` to a row, mechanically? Still open. Paper 3's resolution rate
   (87%) is lower than Paper 2's (92%) despite using the same audit process, which argues the gap is
   partly about which facets get drawn each paper, not solely about process rigor (F-24).

### Session reflection

Three consecutive papers on the redesigned pipeline (13/13, 13/13, 13/13) settles F-16/F-17 as a fixed
part of how this engine runs, not a fragile fix. But this session's most useful finding wasn't about
authoring at all — it was that the *orchestrating session's own* assembly-time fix (the family-tag
relabel, F-25) was wrong, and the same grounding-audit discipline built to catch authoring errors
caught it too, for the same reason: independent, skeptical, blind to the reasoning that produced the
thing being checked. The practice generalizes further than "audit what the sub-agents wrote" — it
should audit *this session's own* patches as well, whenever one is made to satisfy a mechanized number
rather than because a specific piece of grounding was checked.
