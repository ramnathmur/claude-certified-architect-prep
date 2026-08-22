# CCDV-F Mock Exams

`CCDV-F_MockTest-TEMPLATE_v1.html` is the exam engine. Every generated paper is a copy of it with a
new item array. This file explains how to make that copy, what must change, and what must not.

Read `..\..\CLAUDE.md`, `..\..\..\CLAUDE.md` and `..\..\EXAM-FACTS_v1.md` first. Nothing here
overrides them.

---

## Status

**No paper can be generated yet.** The eight domain corpus files do not exist — Phase 3 builds them.
The template currently ships with the three official sample questions as demo items so the engine can
be exercised end to end. They are not a paper and not corpus output.

---

## The paper being simulated

53 items · 120 minutes · standalone items, each stating how many responses to select · 720 scaled on
100–1,000 · **no domain floor**, total score only. All verified against the official exam guide v1.0
(July 2026). Source: `..\..\EXAM-FACTS_v1.md`.

---

## Generating a real paper

### 1. Copy the template

    CCDV-F_MockTest-TEMPLATE_v1.html  ->  CCDV-F_MockTest-N_v1.html

Check the directory first and take the next free `N`. Never overwrite an existing paper.

### 2. Replace the item array

Everything between the `/* ==== ITEMS ==== */` banner and `/* ==== END ITEMS ==== */` at the bottom of
the `<script>` block. Delete all three demo items.

**The only permitted source for generated questions is the eight domain corpus files:**

    prep with quiz\CCDV-F_Domain-1_v1.md    Agents and Workflows              14.7%
    prep with quiz\CCDV-F_Domain-2_v1.md    Applications and Integration      33.1%
    prep with quiz\CCDV-F_Domain-3_v1.md    Claude Code                        3.1%
    prep with quiz\CCDV-F_Domain-4_v1.md    Eval, Testing, and Debugging       2.6%
    prep with quiz\CCDV-F_Domain-5_v1.md    Model Selection and Optimization  16.8%
    prep with quiz\CCDV-F_Domain-6_v1.md    Prompt and Context Engineering    11.0%
    prep with quiz\CCDV-F_Domain-7_v1.md    Security and Safety                8.1%
    prep with quiz\CCDV-F_Domain-8_v1.md    Tools and MCPs                    10.6%

Never from notes, never from the web, never from memory. This is a repo-level rule, and it exists
because a community guide's wrong scenario count reached generated CCAR-F practice material.

Item shape:

| Field | Notes |
|---|---|
| `g` | 1-based position. Must equal array index + 1 |
| `domain` | `"D1"`..`"D8"` |
| `section` | Skill section `"N.M"`. Must sit inside its own domain |
| `stem` | The scenario. **Multiple-response stems must state their count**, e.g. `(Select two.)` |
| `options` | Array of strings. Backticks render as inline code |
| `correct` | Single-answer: option index. Multiple-response: sorted array of indexes |
| `selectN` | Multiple-response only. How many to select |
| `whyRight` | `{text, cite}` |
| `whyWrong` | `[{option, text, cite}]` — one entry per non-correct option |

### 3. Change the paper-level fields

| Where | Field | To |
|---|---|---|
| `/* ==== CONFIG ==== */` | `KEY` | `"ccdvf-mock-N"` — **a unique key per paper, or two papers share one save file** |
| `/* ==== ITEMS ==== */` | `paper_n` | the paper number |
| | `paper_label` | usually the same number |
| | `format` | `"FULL53"` for a full simulation. A short drill names itself, e.g. `"DRILL20"` |
| | `generated` | `YYYY-MM-DD` |
| | `file` | the new filename |
| Start card | the `id="startProse"` block | what this paper targets and why, from the last Professor's Note |

Everything else on the landing card, the hero and the tags is filled from `DATA` at load time. Do not
hand-edit those.

### 4. Open it in a browser before calling it done

The template runs a self-check on load and paints a red banner listing any problem it finds: an item
whose section does not belong to its domain, an unknown section, a multiple-response stem that does
not state its count, a missing `whyWrong` entry, a `FULL53` paper that is not 53 items, a `FULL53`
paper still carrying the template `KEY` or `paper_n`. **A red banner means the paper is malformed.**

Serve it over `http://localhost`, not `file://` — the preview pane rewrites `file://` as a `data:` URL
and in-page anchors die.

### 5. Write the generation line

One line in `..\DASHBOARD-DATA.jsonl` with nulls, per `..\DASHBOARD-SCHEMA.md` rule 1. It is updated in
place when the paper is scored.

---

## After sitting a paper

1. Submit. The results card and the full-rationale review appear.
2. **Tag every miss `RECALL` or `CONCEPT`** in the review. The results card shows an untagged count and
   will not go quiet until it reaches zero. `recall_misses + concept_misses` must equal the miss count
   — `..\DASHBOARD-SCHEMA.md` rule 5 admits no "unclassified" bucket.
   - `RECALL` — you knew which approach was right but could not recall a specific.
   - `CONCEPT` — you did not know which approach was right for the constraint the stem stated.
   - Unanswered items count as misses and are taggable, so the arithmetic closes.
3. Copy the three export panes:
   - **JSONL line** — append to `..\DASHBOARD-DATA.jsonl`
   - **Results JSON** — the full per-item record
   - **Log entry** — paste into `..\EXAM-LOG.md` and finish by hand
4. Fill in what the paper cannot compute. See below.

### Two fields the paper cannot compute

| Field | Exported as | Why |
|---|---|---|
| `confirmed_weakness` | `null` | Needs the previous paper **by attempt date**. The paper does not know the log |
| `insight_round_due` | `false` | Needs the scored-paper count from `..\EXAM-LOG.md` |

Set both by hand before writing the line. The "Why wrong" column of the miss table is also blank on
purpose — that is the diagnosis, and it is the part that makes the next paper better than this one.

---

## Never change these

**The scoring assumption comment.** Multiple-response items are scored all-or-nothing at `isRight()`
in the `/* ==== STATE ==== */` section, under a comment saying in plain terms that this is an
assumption and not a verified fact. The official guide v1.0 does not say whether the real exam awards
partial credit. Keep the comment where it is: it is the note whoever confirms this from the real score
report needs to find. If it turns out to be partial credit, that comment names every place that has to
change.

**Section numbering.** The `SECTIONS` map is the guide's own skill order, numbered `N.M`, and it is
permanent. Misses are logged by section, so renumbering destroys the miss history. If a section
assignment on an existing paper is found to be wrong, fix it as a finding in `..\EXAM-LOG.md` and get
explicit sign-off first — `..\DASHBOARD-SCHEMA.md` rule 4.

**No scenario blocks.** CCDV-F items are standalone; the guide is explicit. The CCAR-F block
architecture was removed wholesale from this engine — no block headers, no block grouping in the jump
map, no per-block results breakdown. Do not reintroduce it.

**Exam mode.** `EXAM_MODE = true`. No correctness signal of any kind during the sitting, no live score
pill, answers freely changeable until submit, 120:00 countdown, no auto-submit at zero. Spec:
`..\..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\EXAM-MODE-DESIGN_v1.md`.

**Self-contained.** No web fonts, no CDN, no external stylesheets or scripts, no network calls. The
CCAR-F reference linked Google Fonts; that link is gone and local font stacks replace it. Keep it that
way — these are sat offline.

**Scores live in one file.** `..\EXAM-LOG.md` is the only file that carries standing. If any other
file starts carrying scores, delete it.

---

## The scaled-score estimate

The results card shows an estimated scaled score and labels it an estimate, with the mapping printed
next to it:

    round( correct / items x 900 + 100 )

A straight linear map of raw percentage onto the published 100–1,000 range. On 53 items it puts the
pass line at **37 raw correct**. It is the same mapping the CCAR-F papers used, kept identical on
purpose so estimates from the two projects stay comparable.

It is not what the real exam does. The real exam is criterion-referenced, with a cut score set by a
formal standard-setting study and applied through psychometric scaling across equated forms. Treat the
number as a rough gauge. The export carries `authoritative: false` and the formula string alongside
the value so nothing downstream mistakes it for an Anthropic figure.

---

## Schema note — `section_scores` is an additive extension

`..\DASHBOARD-SCHEMA.md` already carries the RECALL/CONCEPT counts (`recall_misses`,
`concept_misses`), so those needed nothing new. It has **no field that can express skill-section
numbers**, and CCDV-F logs misses by section.

The exported JSONL line therefore carries one extra key:

```json
"section_scores": {"2.3": [0,1], "7.1": [1,1], "8.3": [1,1]}
```

Same `[correct, of]` array shape as `domain_scores`. Additive only — every documented field keeps its
name, type and meaning.

**`..\DASHBOARD-SCHEMA.md` has not been edited.** The amendment needs the project owner's sign-off
first. Until then the exported line carries a key the schema does not document.

---

## Files

| File | What it is |
|---|---|
| `CCDV-F_MockTest-TEMPLATE_v1.html` | The engine. Copy it; do not sit it |
| `CCDV-F_MockTest-N_v1.html` | Generated papers |
| `README.md` | This file |
