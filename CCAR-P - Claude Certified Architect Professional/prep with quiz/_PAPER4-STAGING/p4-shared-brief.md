# Paper 4 — Shared Authoring Brief

You are authoring a sub-batch of items for CCAR-P Mock Test Paper 4, an AUTHOR-mode 63-item practice
exam for the Claude Certified Architect – Professional certification. This brief is handed to every
authoring sub-batch unchanged. Your specific slot assignment (which g-numbers, which facets/sections,
which correct letter, which shape, which format, which direction) is given separately in your dispatch
prompt.

**Ground everything in the actual corpus file** —
`CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P_Domain-<N>_v1.md` — read the
full section you're assigned before writing. Never paraphrase from a ledger's truncated excerpt (the
excerpts in `FACET-LEDGER.md` are for planning only, not source material).

## What's new this paper: direction inversion

Paper 4 begins Papers 4-7's shape policy: each of the eight shapes must appear at least twice this
paper with its direction **inverted**, per `ARCHETYPE-LEDGER.md`'s inversion table. This is the
mechanism aimed directly at the standing habit of choosing an option because it *sounds* safer, more
architected, or more thorough, rather than because it matches the stated requirement.

If your dispatch prompt marks an item `"direction": "inverted"`, it will also give you an `invGuidance`
string quoting the exact inversion definition for that item's shape, plus a specific scenario anchor.
**Read `invGuidance` before drafting that item.** Three rules bind every inverted item:

1. **The correct answer must be genuinely different from what the section's normal-direction facet
   teaches** — not the same lesson restated with different nouns. If your item reuses an already-shipped
   facet as its anchor (see the D2 note below), the new item's correct answer and its `factAnswerRaw`
   must differ from that facet's own answer text, or the assembly-stage lessonKey collision check will
   flag it as a duplicate.
2. **If the section genuinely cannot support the stated inversion**, do not force one. Write your best
   attempt, set `t1Clause`/`t1Alt` honestly, and flag it in your batch's `notes` as a likely T1
   IRREDUCIBLE case for the grounding audit to confirm — exactly the same honesty standard as a normal
   T1 exception. This is expected to happen at least once (see the D2/§2.2 note below) and is not a
   failure on your part.
3. **An inverted item still needs three distractor families and must still pass T2/T3/T4** — direction
   inversion changes which option is correct and why, not the item's other construction rules.

## D2 note — direction-inverted reuse, Ram's approved decision

D2's real decision-table facet supply is fully exhausted (0 of 18 facets fresh across Papers 1-3).
Three of D2's 8 items use the last unused misconception units (`M-2.3`, `M-2.5`, `M-2.9`) — these are
built normally, exactly like Paper 3's misconception-unit items, `direction: "normal"`.

The other **five D2 items (sections 2.1, 2.2, 2.4, 2.7, 2.8) reuse an already-shipped facet as an
anchor, but must test the inverted direction** — this is Ram's explicitly approved mechanism for D2's
supply crisis, recorded in `EXAM-LOG.md`'s Paper 4 entry. Your dispatch prompt names the anchor facet
and gives `invGuidance` describing the specific inversion to build. Read the anchor facet's own row in
`CCAR-P_Domain-2_v1.md` first, understand what it normally teaches, then construct a fresh scenario
that inverts it per the guidance — do not just reword the anchor facet's own scenario.

**Section 2.2 is flagged as a likely IRREDUCIBLE case.** Its core rule (the system prompt is the only
location with durable authority) is absolute — Paper 2's g14/g15 already found no conditional row
supports a clean T1 inversion there. Attempt the best defensible inversion per the guidance, but do not
force a technically-invalid one; document honestly if it doesn't resolve.

## Item schema — one JSON object per item

```
{
  "g": <int>,                 // your assigned g-number, exactly
  "domain": "D<N>",
  "section": "<N.M>",
  "facet": "F-<N.M>-<NN>" or "M-<N.M>",   // exactly as assigned (for D2 reuse-inverted items, this
                               // is the ANCHOR facet id — the item you write is a fresh inversion of it)
  "objective": "O<N.M>",      // exactly as assigned
  "shape": "S<1-8>",          // as assigned — you may substitute a better-fitting shape if the
                               // assigned one genuinely doesn't fit the facet's content; note the
                               // substitution in your batch's build notes if you do (do NOT substitute
                               // away from an assigned shape on an inverted-direction item without
                               // flagging it prominently, since shape/direction pairs are planned
                               // centrally to hit the paper-wide floor)
  "direction": "normal" or "inverted",   // exactly as assigned
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
  "factAnswerRaw": "..."      // for a normal-direction item: the underlying facet's corpus Answer-
                               // column text, VERBATIM. For an inverted-direction item (including D2's
                               // reuse-inverted items): the NEW correct answer's own text, verbatim as
                               // you wrote it into the option — never the anchor facet's original
                               // answer text. "" for a misconception-unit item. Used centrally at
                               // assembly to compute lessonKey — do not compute lessonKey yourself, and
                               // do not include a "lessonKey" or "correct" field in your output.
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
centrally so the paper's letter tally comes out balanced (Paper 4's target: A×13, B×14, C×14, D×14
across the 55 single-answer items — A is Paper 4's "short" letter, per the D→C→B→A rotation). Do not
renumber or swap positions to make drafting easier; if the assigned letter genuinely cannot hold the
correct answer for a specific facet, say so in your build notes rather than silently reassigning it.

## The four rejection tests — every item must pass all four

| Test | Pass condition |
|---|---|
| **T1 · Constraint sensitivity** | Name one clause in the stem whose deletion or inversion makes a **different** option correct. Record it as `t1Clause`, and the letter of the option that would then be correct as `t1Alt`. **`t1Alt` must resolve to a real, nameable row in the cited section's decision table** — check this yourself before shipping; do not leave it as a plausible guess |
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
  paper-wide across Papers 1-3. Reach for `EVIDENCE-MISMATCH` (the stem's own stated evidence already
  rules the option out) and `DETECTIVE-FOR-PREVENTIVE` (an option that monitors/logs/confirms a misuse
  where the actual requirement is to remove the capability) wherever the facet genuinely supports them
  — sections about tool/capability scoping, access removal, or guardrail placement (common in D3, D5,
  D7) are natural homes for `DETECTIVE-FOR-PREVENTIVE`.
- `ARCHITECTED` (more capable/thorough than the requirement supports) is capped paper-wide at 10% —
  don't avoid it entirely, but don't lean on it either. Note: on an **inverted-direction** item, the
  "architected-sounding" option is very often the CORRECT one, not a distractor — do not force an
  ARCHITECTED-tagged distractor onto an inverted item where the architected-sounding choice is the key.
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
test a **different failure mode** than that scenario shows, not a re-skin of it. For a D2 reuse-inverted
item, this applies doubly: it must differ from both the exam scenario AND the anchor facet's own row.

## Misconception-unit items (only if your slot is an `M-<section>` facet)

Built from the section's own `Misconception` block (a stated wrong belief + its correction), not from
a `Situation | Answer | Why` decision-table row. Read that block in the corpus file in full — the
truncated one-line excerpt in `FACET-LEDGER.md`'s misconception table is not enough to author from.
Leave `factAnswerRaw` as `""` for these items (no single verbatim Answer-column string applies).

## Output — write your file the instant you finish, immediately

Write a single JSON object to the exact filename given in your dispatch prompt, inside
`CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER4-STAGING/`, shaped exactly:

```json
{"items": [ /* your items, in g order */ ], "notes": [ /* strings, or [] if nothing to flag */ ]}
```

Do this as soon as you're done drafting — do not hold the result only in your own response. Put any
likely T1/T2 IRREDUCIBLE case, shape substitution, or genuine grounding shortfall in `notes` as a short
string naming the g-number and the issue.
