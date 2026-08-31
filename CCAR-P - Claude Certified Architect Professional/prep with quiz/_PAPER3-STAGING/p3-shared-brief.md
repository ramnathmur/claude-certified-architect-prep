# Paper 3 — Shared Authoring Brief

You are authoring a sub-batch of items for CCAR-P Mock Test Paper 3, an AUTHOR-mode 63-item practice
exam for the Claude Certified Architect – Professional certification. This brief is handed to every
authoring sub-batch unchanged. Your specific slot assignment (which g-numbers, which facets/sections,
which correct letter, which shape, which format) is given separately in your dispatch prompt.

**Ground everything in the actual corpus file** —
`CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P_Domain-<N>_v1.md` — read the
full section you're assigned before writing. Never paraphrase from a ledger's truncated excerpt (the
excerpts in `FACET-LEDGER.md` are for planning only, not source material).

## Item schema — one JSON object per item

```
{
  "g": <int>,                 // your assigned g-number, exactly
  "domain": "D<N>",
  "section": "<N.M>",
  "facet": "F-<N.M>-<NN>" or "M-<N.M>",   // exactly as assigned
  "objective": "O<N.M>",      // exactly as assigned
  "shape": "S<1-8>",          // as assigned — you may substitute a better-fitting shape if the
                               // assigned one genuinely doesn't fit the facet's content; note the
                               // substitution in your batch's build notes if you do
  "direction": "normal",      // every item this paper — direction inversion starts Paper 4
  "format": "single" or "multi",   // as assigned
  "selectN": 1 or 2,          // 1 for single, 2 for multi
  "stem": "...",
  "opts": [
    {"l": "A", "t": "...", "family": null or "<FAMILY-NAME>"},
    {"l": "B", "t": "...", "family": null or "<FAMILY-NAME>"},
    {"l": "C", "t": "...", "family": null or "<FAMILY-NAME>"},
    {"l": "D", "t": "...", "family": null or "<FAMILY-NAME>"}
  ],
  "whyRight": "...",
  "whyWrong": {"A": "...", "B": "...", "C": "..."},   // one entry per non-correct letter, omit the correct letter
  "deepDive": null,           // literal null on every item — Phase 9 populates this later, only for missed items. Do not author it.
  "t1Clause": "...",
  "t1Alt": "<letter>",
  "source": "AUTHORED",
  "block": null,
  "blockLabel": null,
  "factAnswerRaw": "..."      // the underlying facet's corpus Answer-column text, VERBATIM. "" for
                               // a misconception-unit item or a multi item genuinely built from two
                               // rows with no single verbatim answer. Used centrally at assembly to
                               // compute lessonKey — do not compute lessonKey yourself, and do not
                               // include a "lessonKey" or "correct" field in your output (see below).
}
```

**Do NOT include a `lessonKey` field or a `correct` field in your output.** `lessonKey` is computed
centrally at assembly from `factAnswerRaw` (per §5.5 of the orchestration prompt). `correct` is added
centrally at assembly from the pre-planned letter/pair — encoding it yourself risks a false JSON_VALID
finding at review time (this happened on Paper 1, F-09). Correctness is encoded purely by which
option(s) carry `"family": null`.

## Your assigned correct answer is a hard constraint

Your dispatch prompt tells you which letter (single) or letter-pair (multi) must be correct for each
g-number. **Write the substantively correct option into that exact position** — this was pre-shuffled
centrally so the paper's letter tally comes out balanced (Paper 3's target: A×14, B×13, C×14, D×14
across the 55 single-answer items — B is Paper 3's "short" letter). Do not renumber or swap positions
to make drafting easier; if the assigned letter genuinely cannot hold the correct answer for a specific
facet, say so in your build notes rather than silently reassigning it.

## The four rejection tests — every item must pass all four

| Test | Pass condition |
|---|---|
| **T1 · Constraint sensitivity** | Name one clause in the stem whose deletion or inversion makes a **different** option correct. Record it as `t1Clause`, and the letter of the option that would then be correct as `t1Alt`. **`t1Alt` must resolve to a real, nameable row in the cited section's decision table** — check this yourself before shipping; do not leave it as a plausible guess (Paper 1 shipped 13 of 63 that didn't resolve, found only by a later audit; Paper 2 got this to 92% resolved *before* shipping by authors checking it themselves) |
| **T2 · Neighbour-correct distractor** | At least one distractor is an action the same section's decision table lists as correct in a neighbouring situation |
| **T3 · No vocabulary answer** | Delete the situation, leave the question line. If the correct option is still identifiable, reject and rewrite |
| **T4 · Production dimension** | The stem carries at least one of: volume/scale, cost, a latency budget, a regulator/compliance regime, an SLA, or a named stakeholder who must approve |

If a section genuinely cannot support a T1/T2 resolution (this happens, especially in D2's thinner
sections and misconception-unit items), do not fabricate one — write your best `t1Clause`/`t1Alt`
attempt, and flag it plainly in your batch's build notes as a likely IRREDUCIBLE case for the grounding
audit to confirm. Honesty here is worth more than a false pass.

## Distractor families — one of eight, three different families per item

`HALF-MOVE` · `WRONG-AXIS` · `REPAIR` · `DISCARD` · `ARCHITECTED` · `OVERSPEC` · `EVIDENCE-MISMATCH` ·
`DETECTIVE-FOR-PREVENTIVE`. Three distractors, three different families, tagged in `opts[].family`.

- Do not default to `WRONG-AXIS` or `HALF-MOVE` for convenience — both are already over-represented
  paper-wide across Papers 1-2. Reach for `EVIDENCE-MISMATCH` (the stem's own stated evidence already
  rules the option out) and `DETECTIVE-FOR-PREVENTIVE` (an option that monitors/logs/confirms a misuse
  where the actual requirement is to remove the capability) wherever the facet genuinely supports them
  — sections about tool/capability scoping, access removal, or guardrail placement (common in D3, D5,
  D7) are natural homes for `DETECTIVE-FOR-PREVENTIVE`.
- `ARCHITECTED` (more capable/thorough than the requirement supports) is capped paper-wide at 10% —
  don't avoid it entirely, but don't lean on it either.
- The paper-wide family balance is checked and fixed centrally at assembly (this is expected, not a
  sign your batch did something wrong) — write the best-fitting family for each distractor's actual
  reasoning, and a central pass will relabel if the paper-wide tally needs it.

## Style targets — caps are binding, bands are guidance

| Target | Value |
|---|---|
| Stem hard cap | **45 words**. Soft band 28–40 |
| Option hard cap | **20 words**. Within-item spread ≤ 8 words |
| Point of view | Third-person indefinite; second person on at most 1 in 7 stems |
| Inline code/config tokens | ≤ 15% of options **paper-wide** — and **never** in a D1, D5, or D6 option, regardless of section |
| Named companies, products, personas | **Zero**, anywhere |
| `whyRight` | 35–50 words |
| `whyWrong` (each) | 15–30 words |

The corpus's own `Exam scenario` block for your assigned section is reference-only — your item must
test a **different failure mode** than that scenario shows, not a re-skin of it.

## Misconception-unit items (only if your slot is an `M-<section>` facet)

Built from the section's own `Misconception` block (a stated wrong belief + its correction), not from
a `Situation | Answer | Why` decision-table row. Read that block in the corpus file in full — the
truncated one-line excerpt in `FACET-LEDGER.md`'s misconception table is not enough to author from.
Leave `factAnswerRaw` as `""` for these items (no single verbatim Answer-column string applies).

## Output — write your file the instant you finish, immediately

Write a single JSON object to the exact filename given in your dispatch prompt, inside
`CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER3-STAGING/`, shaped exactly:

```json
{"items": [ /* your items, in g order */ ], "notes": [ /* strings, or [] if nothing to flag */ ]}
```

Do this as soon as you're done drafting — do not hold the result only in your own response. Put any
likely T1/T2 IRREDUCIBLE case, shape substitution, or genuine grounding shortfall in `notes` as a short
string naming the g-number and the issue.
