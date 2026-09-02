# Paper 5 — Shared Authoring Brief

You are authoring a sub-batch of items for CCAR-P Mock Test Paper 5, an AUTHOR-mode 63-item practice
exam for the Claude Certified Architect – Professional certification. This brief is handed to every
authoring sub-batch unchanged. Your specific slot assignment (which g-numbers, which facets/sections,
which correct letter, which shape, which format, which direction) is given separately in your dispatch
prompt.

**Ground everything in the actual corpus file** —
`CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P_Domain-<N>_v1.md` — read the
full section you're assigned before writing. Never paraphrase from a ledger's truncated excerpt (the
excerpts in `FACET-LEDGER.md` are for planning only, not source material). **If your slot is in D2,
several of the corpus's decision tables were added today (2026-09-01, marked in the file with an
"Added 2026-09-01" note) — read them the same as any other table; they are just as authoritative.**

## `cite` is a required field — Paper 4 shipped without it and it showed as "undefined" on every item

Paper 4's own shared brief omitted `cite` from the schema, which passed every mechanized check and
only surfaced when the shipped file was opened in a browser (every feedback footer showed literal
"undefined"). **Include `"cite": "<domain> <section>"` on every item** (e.g. `"cite": "D2 2.7"`) —
it is in the schema below and is now a required field in `validateItems()`. Do not omit it.

## Direction inversion — same mechanism as Paper 4, now on healthier D2 supply

Papers 4-7's shape policy continues: each of the eight shapes must appear at least twice this paper
with its direction **inverted**, per `ARCHETYPE-LEDGER.md`'s inversion table. This is the mechanism
aimed directly at the standing habit of choosing an option because it *sounds* safer, more
architected, or more thorough, rather than because it matches the stated requirement.

If your dispatch prompt marks an item `"direction": "inverted"`, it will also give you an `invGuidance`
string quoting the exact inversion definition for that item's shape, plus a specific scenario anchor.
**Read `invGuidance` before drafting that item.** Three rules bind every inverted item:

1. **The correct answer must be genuinely different from what the section's normal-direction facet
   teaches** — not the same lesson restated with different nouns. Paper 4 shipped one reuse-inverted
   item that failed exactly this test on first attempt (a cosmetic restate caught only by the
   independent audit) — the standard is real, not a formality.
2. **If the section genuinely cannot support the stated inversion**, do not force one. Write your best
   attempt, set `t1Clause`/`t1Alt` honestly, and flag it in your batch's `notes` as a likely T1
   IRREDUCIBLE case for the grounding audit to confirm — this is not a failure on your part.
3. **An inverted item still needs three distractor families and must still pass T2/T3/T4** — direction
   inversion changes which option is correct and why, not the item's other construction rules.

## Two items reuse an already-exhausted facet — everyone else uses fresh content

D2's corpus expansion (21 new decision-table rows, added today) means D2 no longer needs the
reuse-inversion or misconception fallback Paper 4 required — every D2 item in this paper, including
its inverted ones, is built from a **genuinely fresh** facet, the same as every other domain.

Two objectives elsewhere (**O3.1** → section 3.1, and **O5.3** → section 5.8) had every one of their
own facets already used across Papers 1-4, with no misconception unit left either — the standing
"direction doubling" fallback (in force since Paper 4, documented in `FACET-LEDGER.md`) applies: these
two items reuse an already-shipped facet as an anchor but must test the **inverted** direction. Your
dispatch prompt names the anchor facet and gives `invGuidance` for these two specifically. Read the
anchor facet's own row first, understand what it normally teaches, then construct a fresh scenario that
inverts it per the guidance — do not just reword the anchor facet's own scenario. Rule 1 above (a
genuinely different correct answer, not a restate) applies with extra weight to these two items.

## Misconception-unit items never carry `direction: "inverted"`

If your slot is an `M-<section>` facet, it ships `direction: "normal"` regardless of anything else in
this brief — a misconception is a stated wrong belief plus its correction, not a two-sided decision
axis, so there is no clean "opposite direction" to test. (This is why Paper 5's central plan replaced
one exhausted-section pick that landed on its misconception unit — D3 §3.2 — with a different item for
the inverted-shape slot it would otherwise have filled; nothing about this affects your own slot unless
your dispatch prompt tells you your item is a misconception-unit pick.)

## Item schema — one JSON object per item

```
{
  "g": <int>,                 // your assigned g-number, exactly
  "domain": "D<N>",
  "section": "<N.M>",
  "facet": "F-<N.M>-<NN>" or "M-<N.M>",   // exactly as assigned (for the two reuse-inverted items,
                               // this is the ANCHOR facet id — the item you write is a fresh inversion of it)
  "objective": "O<N.M>",      // exactly as assigned
  "cite": "D<N> <N.M>",       // REQUIRED — see above. Domain + section, exactly as assigned.
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
                               // column text, VERBATIM. For an inverted-direction item (including the
                               // two reuse-inverted items): the NEW correct answer's own text, verbatim
                               // as you wrote it into the option — never the anchor facet's original
                               // answer text. "" for a misconception-unit item. Used centrally at
                               // assembly to compute lessonKey — do not compute lessonKey yourself, and
                               // do not include a "lessonKey" or "correct" field in your output.
}
```

**Do NOT include a `lessonKey` field or a `correct` field in your output.** `lessonKey` is computed
centrally at assembly from `factAnswerRaw` (per §5.5 of the orchestration prompt). `correct` is added
centrally at assembly from the pre-planned letter/pair — encoding it yourself risks a false JSON_VALID
finding at review time. Correctness is encoded purely by which option(s) carry `"family": null`.

## Your assigned correct answer is a hard constraint

Your dispatch prompt tells you which letter (single) or letter-pair (multi) must be correct for each
g-number. **Write the substantively correct option into that exact position** — this was pre-shuffled
centrally so the paper's letter tally comes out balanced (Paper 5's target: A×14, B×14, C×14, D×13
across the 55 single-answer items — D is Paper 5's "short" letter, per the D→C→B→A rotation, mirroring
Paper 1's shape). Do not renumber or swap positions to make drafting easier; if the assigned letter
genuinely cannot hold the correct answer for a specific facet, say so in your build notes rather than
silently reassigning it.

## The four rejection tests — every item must pass all four

| Test | Pass condition |
|---|---|
| **T1 · Constraint sensitivity** | Name one clause in the stem whose deletion or inversion makes a **different** option correct. Record it as `t1Clause`, and the letter of the option that would then be correct as `t1Alt`. **`t1Alt` must resolve to a real, nameable row in the cited section's decision table** — check this yourself before shipping; do not leave it as a plausible guess |
| **T2 · Neighbour-correct distractor** | At least one distractor is an action the same section's decision table lists as correct in a neighbouring situation |
| **T3 · No vocabulary answer** | Delete the situation, leave the question line. If the correct option is still identifiable, reject and rewrite |
| **T4 · Production dimension** | The stem carries at least one of: volume/scale, cost, a latency budget, a regulator/compliance regime, an SLA, or a named stakeholder who must approve |

If a section genuinely cannot support a T1/T2 resolution, do not fabricate one — write your best
`t1Clause`/`t1Alt` attempt, and flag it plainly in your batch's build notes as a likely IRREDUCIBLE case
for the grounding audit to confirm. Honesty here is worth more than a false pass.

## Distractor families — one of eight, three different families per item

`HALF-MOVE` · `WRONG-AXIS` · `REPAIR` · `DISCARD` · `ARCHITECTED` · `OVERSPEC` · `EVIDENCE-MISMATCH` ·
`DETECTIVE-FOR-PREVENTIVE`. Three distractors, three different families, tagged in `opts[].family`.

- Do not default to `WRONG-AXIS` or `HALF-MOVE` for convenience — both are already over-represented
  paper-wide across Papers 1-4. Reach for `EVIDENCE-MISMATCH` (the stem's own stated evidence already
  rules the option out) and `DETECTIVE-FOR-PREVENTIVE` (an option that monitors/logs/confirms a misuse
  where the actual requirement is to remove the capability) wherever the facet genuinely supports them.
- `ARCHITECTED` (more capable/thorough than the requirement supports) is capped paper-wide at 19 of 189
  distractors (~10%) — don't avoid it entirely, but don't lean on it either. Note: on an
  **inverted-direction** item, the "architected-sounding" option is very often the CORRECT one, not a
  distractor — do not force an ARCHITECTED-tagged distractor onto an inverted item where the
  architected-sounding choice is the key.
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
test a **different failure mode** than that scenario shows, not a re-skin of it. For a reuse-inverted
item, this applies doubly: it must differ from both the exam scenario AND the anchor facet's own row.

## Misconception-unit items (only if your slot is an `M-<section>` facet)

Built from the section's own `Misconception` block (a stated wrong belief + its correction), not from
a `Situation | Answer | Why` decision-table row. Read that block in the corpus file in full — the
truncated one-line excerpt in `FACET-LEDGER.md`'s misconception table is not enough to author from.
Leave `factAnswerRaw` as `""` for these items (no single verbatim Answer-column string applies).
`direction` is always `"normal"` for these — see the rule above.

## Output — write your file the instant you finish, immediately

Write a single JSON object to the exact filename given in your dispatch prompt, inside
`CCAR-P - Claude Certified Architect Professional/prep with quiz/_PAPER5-STAGING/`, shaped exactly:

```json
{"items": [ /* your items, in g order */ ], "notes": [ /* strings, or [] if nothing to flag */ ]}
```

Do this as soon as you're done drafting — do not hold the result only in your own response. Put any
likely T1/T2 IRREDUCIBLE case, shape substitution, or genuine grounding shortfall in `notes` as a short
string naming the g-number and the issue.
