# CCAR-P Mock Test Paper 2 — Shared Authoring Brief

You are authoring items for ONE domain of a 63-item certification-prep mock exam (Claude Certified
Architect – Professional). This brief is shared across all seven domain-authoring agents; a separate
file gives your specific item slots.

## The one rule that overrides everything else

Your assigned `CCAR-P_Domain-N_v1.md` corpus file is the ONLY permitted source for facts, decision
logic, distractor content, and explanations. Never invent a decision-table row, a misconception, or a
consequence that the corpus does not state. Never draw on outside AI/architecture knowledge to fill a
gap — if the corpus doesn't support something, say so in your report rather than inventing it. Read
your ENTIRE corpus file before writing anything, and re-read the specific section you're drawing an
item from immediately before writing that item's `whyRight`/`whyWrong`/`t1Alt` — not from memory of
"what it probably says."

Do not read any other domain's corpus file, EXAM-LOG.md, or GENERATION-INTELLIGENCE.md. You do not
need them and reading them wastes your budget.

**Corrected 2026-08-30, mid-session, after Paper 2's first generation attempt failed outright and an
independent cost/failure audit was run.** `deepDive` (the second explanation layer) is REMOVED from
this batch's scope — every item ships `deepDive: null`. It is now a deferred, miss-driven Phase 9
addition generated later, only for items actually missed, not a generation-time requirement. This cuts
your per-item workload roughly in half to a third: you are writing `stem`/`opts`/`whyRight`/`whyWrong`/
`t1Clause`/`t1Alt` only, nothing past that. You are also authoring a SMALL SUB-BATCH of roughly 5-6
items, not a full domain — see your dispatch prompt for exactly which g-numbers are yours this round.
This split exists because today's failure data showed item-count-per-turn, not corpus size, predicted
which dispatches stalled — smaller, faster turns with the file written immediately on completion are
the fix.

## AUTHOR mode

Every item is freshly written, testing the same underlying decision as a corpus decision-table row but
NOT copying its wording verbatim (that produces answerable-by-length items — measured on this project
at 84% key-longest, see the rejected TRANSCRIBE mode). The corpus's own "Exam scenario" block for a
section is reference-only — your item must produce a different failure mode / different phrasing than
that scenario shows, even when drawing on the same section.

## Item schema — every field required

```
g          item number (given to you per slot)
domain     "D<N>" (given)
section    corpus section number as a string, e.g. "3.4"
facet      "F-<section>-<2digit>" — see facet-ID convention below, or "M-<section>" for a
           misconception-unit item (only if explicitly told to use one; you should not need to this paper)
objective  "O<N>.<M>" exactly as given in your slot table
shape      one of S1..S8 (table below) — pick whichever fits the item
direction  "normal" for every item this paper (direction inversion starts Paper 4)
lessonKey  LEAVE AS EMPTY STRING "" — do not compute it yourself. Instead add the extra field
           `factAnswerRaw` (below). The orchestrator computes lessonKey centrally so cross-domain
           collisions can be checked before anything ships.
factAnswerRaw   EXTRA field, not part of the shipped schema: the VERBATIM "Answer" column text of the
           decision-table row this item is built from (copy-paste exact corpus wording). Empty string
           only if no single row applies. This is how the orchestrator detects two items (possibly in
           different domains) that test the identical underlying decision under different wording.
format     "single" | "multi" (given per slot)
selectN    1 for single, 2 for multi (given per slot)
stem       <= 45 words, soft band 28-40. Third person, no "you"/"your". Multi-response stems MUST
           literally contain the phrase "Select two." A validator regex requires /select\s+(two|three|\d)/i.
opts       array of exactly 4: [{l:"A", t:"...", family:"..."}, ...] in order A,B,C,D.
           family is null on every CORRECT option, and one of the eight family names (below) on every
           distractor. Each option <= 20 words. Word-count spread across the 4 options <= 8 words
           (spread = longest-minus-shortest by word count) — do NOT make the correct option
           conspicuously longer or shorter than the distractors.
correct    array of letters. Single: exactly 1 letter, and it MUST equal the letter given in your slot
           table. Multi: exactly 2 letters, and they MUST equal the pair given in your slot table.
whyRight   35-50 words. Why this option wins THIS item.
whyWrong   {letter: text} — one entry per NON-correct option, 15-30 words each. None for a correct letter.
t1Clause   the exact stem clause whose deletion or inversion makes a DIFFERENT option correct.
t1Alt      the letter of the option that becomes correct once t1Clause is gone. **This letter MUST
           resolve to a real, nameable row in the SAME section's decision table** (or, if genuinely
           necessary, a clearly-related neighbouring section) — the row where that option is the
           documented correct answer once the clause is removed/inverted. If your first choice of
           t1Clause/t1Alt does not resolve to an actual row, pick a different clause/alt pair. Do not
           ship a t1Alt letter you cannot point at a specific row for. (This is THE most important
           fix from Paper 1 — see "F-12" below.)
deepDive   **literal JSON `null` for every item.** Do not write a principle/rightDeep/wrongDeep object —
           this is deferred to Phase 9 (miss-driven, after the paper is sat). Not your job this batch.
source     "AUTHORED" for every item.
block      null
blockLabel null
cite       "D<N> <section>" (a convenience string, e.g. "D3 3.4")
```

### Facet-ID convention

A facet ID is `F-<section>-<2digit>`, numbered by the row's position in that section's `Situation |
Answer | Why` decision table, top to bottom, starting at 01. E.g. the 3rd row of section 3.4's decision
table is `F-3.4-03`. Your slot table names exactly which facet IDs are already used by Paper 1 in your
domain — do not reuse those. Any other row in the section, or any row in a wholly-untouched section, is
fair game. Verify the row you pick is genuinely a DIFFERENT row than the excluded ones before writing.

## Why AUTHOR mode is strict about this: F-12 and F-13 (read before starting)

**F-12 (Paper 1 finding):** 13 of Paper 1's 63 items recorded a `t1Alt` letter that, on closer
inspection, resolved to no corpus row at all — the field was populated (so the old gate check passed)
but the claim was false. Do not repeat this. Before finalizing an item, actually locate the row your
`t1Alt` depends on and be ready to name it.

**F-13 (Paper 1 finding):** an author checking its own grounding reliably finds its own paraphrase
"close enough." This applies to `whyRight`/`whyWrong`/`t1Alt` too, not just the now-deferred `deepDive`
layer — an independent pass may still check your grounding cold. Write as if it will be checked.

## The eight shapes (pick the one that fits; vary across your items, don't default to one)

| Shape | What the stem does | What the candidate must do |
|---|---|---|
| S1 Named-principle application | States a governing principle by name, describes a violating configuration | Apply the principle against options defensible on some other axis |
| S2 Two-constraint optimisation | Names two constraints that must both be satisfied | Find the one change that moves both, not the one that trades one for the other |
| S3 Post-change diagnosis | Describes a behaviour change after an event, pins what did NOT change | Order the investigation — what to check FIRST |
| S4 Mechanism selection under a stated shape | Describes a data/query/connection shape | Match the mechanism to the shape; every option is a real mechanism used correctly somewhere else |
| S5 Rung selection on a ladder | Describes a requirement set, partly enumerable | Pick the cheapest rung that meets a STATED requirement, either direction |
| S6 Measurement definition | Describes a system about to be evaluated, or a number being reported | Define or repair the measurement |
| S7 Stakeholder framing | Describes a request/commitment/report to a non-technical audience | Separate the stated mechanism from the stated requirement, or bound an unbounded ask |
| S8 Scope and enforcement placement | Describes a control at the wrong altitude | Move it to the layer that owns it, rather than compensating where it sits |

## The eight distractor families

`HALF-MOVE` (correct as far as it goes, leaves a stated requirement untouched) · `WRONG-AXIS` (real
technique, wrong dimension) · `REPAIR` (reconstructs downstream what an upstream step should have done)
· `DISCARD` (solves it by throwing away something the scenario requires) · `ARCHITECTED` (more capable/
future-proof/thorough than the requirement supports — use SPARINGLY, at most 2 per domain this paper) ·
`OVERSPEC` (substitutes a monitoring/threshold guarantee for a stated hard constraint) ·
`EVIDENCE-MISMATCH` (a cause the stem's own stated evidence already rules out) ·
`DETECTIVE-FOR-PREVENTIVE` (detects/logs/confirms misuse where the requirement is to remove the
capability). Your slot file gives you a MINIMUM count of EVIDENCE-MISMATCH and DETECTIVE-FOR-PREVENTIVE
items to hit for your domain — these two families are under-supplied and have hard paper-wide floors.
Every item's 3 distractors must be 3 DIFFERENT families.

## The four rejection tests (T1-T4) — every item must pass all four

- **T1 Constraint sensitivity** — name one stem clause whose deletion/inversion makes a DIFFERENT
  option correct (this is `t1Clause`/`t1Alt` — see the F-12 warning above, it must resolve to a real row).
- **T2 Neighbour-correct distractor** — at least one distractor must be the action your section's
  decision table lists as correct for a NEIGHBOURING situation (a different row of the same table).
- **T3 No vocabulary answer** — delete the situation, leave only the question line. If the correct
  option is still identifiable without the specifics, rewrite — the answer must depend on the stated
  facts, not on option phrasing alone.
- **T4 Production dimension** — the stem must carry at least one of: volume/scale, cost, a latency
  budget, a named regulator/compliance regime, an SLA, or a named stakeholder who must approve.

## Style caps (hard) and bands (soft, still aim inside them)

Stem: hard cap 45 words, soft band 28-40. Options: hard cap 20 words each, hard cap 8 words spread
within one item. Third person only, never "you"/"your". Zero invented company, product, or persona
names — generic nouns only ("a support assistant", "a regulated workflow", "a 40-person engineering
org"). Inline code/config tokens (backtick-quoted, or flag-like `--something`) in at most 1-2 of your
options total this domain, and **zero** if you are D1, D5, or D6 (told in your slot file if this
applies to you) — never invent a token the corpus doesn't already use.

## `deepDive` is NOT part of this batch

Do not write it. Every item's `deepDive` field is literal JSON `null`. If you finish an item's
`stem`/`opts`/`whyRight`/`whyWrong`/`t1Clause`/`t1Alt` and are tempted to add more explanation, stop —
that extra layer is deferred to Phase 9 and writing it now only costs time this batch doesn't need to
spend. `whyRight` (35-50 words) and `whyWrong` (15-30 words per distractor) are the full explanation
layer this batch ships.

## Output format

Write a single JSON file to the path you're given AS SOON AS your items are ready — do not hold it
until some larger batch is done, this IS the whole batch. Contents: a JSON array of your assigned
items in EXACTLY the schema above (including the extra `factAnswerRaw` field, `lessonKey:""`, and
`deepDive:null` on every item). Use plain text everywhere — no markdown, no HTML, no newlines inside
string values. Then, as your final message, report: (1) confirmation of item count and g-range written,
(2) any slot where you deviated from the suggested section/facet and why, (3) your per-item family
tally and confirmation you hit your EVIDENCE-MISMATCH / DETECTIVE-FOR-PREVENTIVE minimums for this
sub-batch (your dispatch prompt states the target for your specific g-numbers), (4) any item where the
corpus could not genuinely support what was asked, named explicitly rather than silently worked around.
Keep this report short — under 200 words. Speed and finishing matter more than a long report this round.
