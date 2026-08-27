# CCDV-F Mock Exams

`CCDV-F_MockTest-TEMPLATE_v1.html` is the exam engine. Every generated paper is a copy of it with a
new item array. This file explains how to make that copy, what must change, and what must not.

Read `..\..\CLAUDE.md`, `..\..\..\CLAUDE.md` and `..\..\EXAM-FACTS_v1.md` first. Nothing here
overrides them.

---

## Status

**Paper 1 exists.** `CCDV-F_MockTest-1_v1.html`, generated 2026-08-25 — 53 items at the exact published
domain weights, drawn from the 34 chapters' own self-tests. This corpus source superseded the original
domain-file plan on 2026-08-22 (`../GENERATION-INTELLIGENCE.md` DV-09); the eight
`CCDV-F_Domain-N_v1.md` files this section used to require **still do not exist and are not planned**.
Every item on Paper 1 carries a `reviewStatus` field (`"gate-verified"` / `"partial-review"` /
`"unreviewed"`) with a matching on-page badge, because 19 of the 34 source chapters were never
independently reviewed — see `../GENERATION-INTELLIGENCE.md` DV-11 for a real chapter-mistagging bug
this caught before the paper shipped. The template still ships with the three official sample questions
as demo items, unrelated to any generated paper.

**Corrected 2026-08-25 (DV-12):** the template and Paper 1 both shipped defaulting to Exam Mode,
permanently, with no way to get per-question feedback at all. That inverted CCAR-F's own explicit,
documented design stance — see "Never change these → Exam mode" below. Both files now default to
Practice Mode. `mock-exams/DASHBOARD.html` also did not exist until this fix; it now does, ported from
CCAR-F's `DASHBOARD.html`.

**Three external-source papers added 2026-08-25:** `Amey-Thakur_CLAUDE-CERTIFICATIONS_MockTest-{1,2,3}_v1.html`
— 15 questions each, transcribed verbatim from a third-party GitHub repository
([Amey-Thakur/CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/tree/main/developer-foundations)),
reformatted into this engine's construct at Ram's request. **These are not CCDV-F-generated content** —
every item card carries an EXTERNAL SOURCE badge, the filename is prefaced with the source repo's name,
and none of it counts as corpus-grounded per this project's own discipline. `format: "DRILL15"`, not
`FULL53` — short untimed drills, not domain-weighted simulations. Every answer, stem, and option set was
programmatically cross-checked against the source's own raw markdown after transcription: 0 mismatches
across all 45 items.

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

**The only permitted source for generated questions is the 34 course chapters' own self-tests**
(`..\Outputs\regeneration\chapters\Ch01_*.md` through `Ch34_*.md`), per the 2026-08-22 supersession of
the domain-file plan the eight paths below used to name. Kept here so the old instruction isn't silently
lost, not because it's still live:

    ~~prep with quiz\CCDV-F_Domain-1_v1.md    Agents and Workflows              14.7%~~
    ~~prep with quiz\CCDV-F_Domain-2_v1.md    Applications and Integration      33.1%~~
    ~~prep with quiz\CCDV-F_Domain-3_v1.md    Claude Code                        3.1%~~
    ~~prep with quiz\CCDV-F_Domain-4_v1.md    Eval, Testing, and Debugging       2.6%~~
    ~~prep with quiz\CCDV-F_Domain-5_v1.md    Model Selection and Optimization  16.8%~~
    ~~prep with quiz\CCDV-F_Domain-6_v1.md    Prompt and Context Engineering    11.0%~~
    ~~prep with quiz\CCDV-F_Domain-7_v1.md    Security and Safety                8.1%~~
    ~~prep with quiz\CCDV-F_Domain-8_v1.md    Tools and MCPs                    10.6%~~

Map a chapter to its domain/section by cross-checking `..\Outputs\regeneration\CCDV-F_Coverage-
Contract_v1.md` §4 **before** dispatching a selection agent, not after — DV-11 in
`..\GENERATION-INTELLIGENCE.md` documents a real chapter mistagged into the wrong domain that a
selection agent then executed faithfully, and that only a Coverage-Contract cross-check caught.

Also record each item's source-chapter review status (`"gate-verified"` for Ch1-15, `"partial-review"`
for Ch16, `"unreviewed"` for Ch17-34, per `..\ROADMAP.md`) in a `reviewStatus` field — Paper 1 added
this field and its on-page badge; keep both.

Never from notes, never from the web, never from memory, and never paraphrased from a chapter's own
self-test — transcribe verbatim. This is a repo-level rule, and it exists because a community guide's
wrong scenario count reached generated CCAR-F practice material.

Item shape:

| Field | Notes |
|---|---|
| `g` | 1-based position. Must equal array index + 1 |
| `domain` | `"D1"`..`"D8"` |
| `section` | Skill section `"N.M"`. Must sit inside its own domain |
| `reviewStatus` | `"gate-verified"` \| `"partial-review"` \| `"unreviewed"` — the source chapter's own review status, shown as a badge on the item card. Omitted defaults to `"gate-verified"` |
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

**Design stance — Practice Mode is the default, not Exam Mode.** `EXAM_MODE = false` on every new
paper unless it is a genuine final dress rehearsal. This mirrors CCAR-F's own explicit design stance
(`..\..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\CLAUDE.md`, "Design stance,
Ram, 2026-07-06": *"per-question feedback is deliberate. The tool optimizes learning-per-question, not
exam-condition realism."*). Exam Mode (`EXAM_MODE = true`: no correctness signal during the sitting, no
live score pill, answers freely changeable until submit, 120:00 countdown, no auto-submit at zero) is
the documented **exception** CCAR-F reserved only for its final two pre-exam sittings — spec:
`..\..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\EXAM-MODE-DESIGN_v1.md`. There
is no runtime toggle by design (that spec's own §7); pick the mode once, per paper, at generation time,
and revert to Practice Mode for the paper after any dress rehearsal. **Getting this backwards is exactly
what shipped in Session 1 and Paper 1's first version** — see `../GENERATION-INTELLIGENCE.md` DV-12.

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
| `Amey-Thakur_CLAUDE-CERTIFICATIONS_MockTest-{1,2,3}_v1.html` | External-source drills, not CCDV-F-generated — see Status above |
| `DASHBOARD.html` | Reads `..\DASHBOARD-DATA.jsonl`. Static snapshot with a paste-to-refresh panel — see its own header comment |
| `README.md` | This file |
