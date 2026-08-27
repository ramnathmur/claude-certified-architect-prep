# Build Prompt — CCAR-P Objective Spines, Domains 2 to 7

Paste everything below the line into a fresh session. Written for Sonnet: every decision that
could be made wrong is pre-made, and every claim you produce has to trace to a file already on disk.

---

You are building six HTML files for Ram's CCAR-P exam prep. A working pilot already exists. Your job
is to replicate it for the remaining six domains, changing only the content and the accent colour.

## Read these first, in this order

1. `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCAR-P - Claude Certified Architect Professional\Outputs\CCAR-P_Objective-Spine-Domain-1_v1.html`
   — the pilot. Read it completely, including the HTML comment at the top, which states the artifact's
   contract. This file is your template.
2. `...\CCAR-P - Claude Certified Architect Professional\EXAM-FACTS_v1.md` — §6 carries the official
   objectives and weights. This is the only authority for what an objective says.
3. `C:\Claude Cowork\CLAUDE.md` and `...\CCAR-P - Claude Certified Architect Professional\CLAUDE.md`
   — house rules. The teaching-prose bans in the global file are binding on every word you write.

Repo root is `C:\Claude Cowork\Projects\Claude Certified Architect Prep\`. Work in the main checkout
unless you are already in a worktree. **Note:** work committed in a worktree does not reach `master`
on its own. Before you say the files are delivered, confirm they exist at the real `Outputs\` path.

## What an Objective Spine is

A four-minute refresher, not a lesson. One tile per published objective, one scenario running through
all of them, about 130 words of prose per tile. The lesson it sits beside runs ~945 words per section.

It deliberately omits decision tables, distractor families and worked arithmetic — those stay in the
lesson and the corpus. **It is not a question source.** Practice items are generated only from
`prep with quiz\CCAR-P_Domain-N_v1.md`.

## The six builds

Each row is one file. The tile count equals the objective count — that is the whole point of the
format, so do not merge or invent objectives to make a nicer number.

| Domain | Weight | Tiles | Source lesson (read this one) | Scenario lives in |
|---|---|---|---|---|
| 2 — Claude Models, Prompting & Context Engineering | 13% | 5 | `Outputs\lessons\CCAR-P_Lesson-Domain-2_v1.html` | §6 "One production design, all five" |
| 3 — Integration | 19% | 8 | `Outputs\lessons\CCAR-P_Lesson-Domain-3_v2.html` | §9 "One system, all eight objectives" |
| 4 — Evaluation, Testing & Optimization | 16% | 6 | `Outputs\lessons\CCAR-P_Lesson-Domain-4_v2.html` | §7 "How it all runs as one system" |
| 5 — Governance, Safety & Risk Management | 14% | 5 | `Outputs\lessons\CCAR-P_Lesson-Domain-5_v2.html` | §6 "One regulated system, all five objectives" |
| 6 — Stakeholder Communication & Lifecycle Management | 14% | 5 | `Outputs\lessons\CCAR-P_Lesson-Domain-6_v1.html` | §6 "One engagement, five phases" |
| 7 — Developer Productivity & Operational Enablement | 7% | 3 | `Outputs\lessons\CCAR-P_Lesson-Domain-7_v1.html` | §5 "Enabling a team end to end" |

**Read the `_v2` file where one exists.** D3, D4 and D5 have both; `_v1` is superseded.

Output filenames follow the pilot exactly:
`Outputs\CCAR-P_Objective-Spine-Domain-N_v1.html`

**Structural gift:** in every lesson, sections `1..N` correspond one-to-one with objectives `N.1..N.N`,
and the final section is the synthesis. So lesson §3 becomes tile 3. The one exception is Domain 7,
which has an extra §4 ("The two documented gaps") that is *not* an objective — its three objectives
are §1, §2, §3, and §5 is the synthesis. Fold anything from §4 that belongs to an objective into that
objective's tile.

## Where the content comes from

**Introduce no new facts.** Every number, name and claim must already appear in the source lesson.
The synthesis section is the richest seam: it already runs one scenario through every objective, which
is exactly the spine's shape. Take the scenario from there, then pull each tile's rule from that
objective's own section.

If the synthesis is thin on an objective, read that objective's section for the detail. If you cannot
source a fact, leave it out. Do not reach for the corpus, the web, or your own knowledge.

### Per tile, four things

- **`beat`** (italic, ~60 words) — what happens in the scenario at this objective. Concrete, with the
  real figures from the lesson.
- **`rule`** (~35 words) — the transferable decision rule, with the load-bearing clause in `<b>`.
  This is what the student carries into the exam.
- **`tell`** (~30 words, in the grey box) — how the exam probes it, or the trap. Give the box a short
  uppercase label in `<span class="k">` such as "What decided it", "Exam shape", "The trap".
- **`viz`** — one inline SVG, `viewBox="0 0 190 168"`, using only the `s-*` classes already in the
  template. Every SVG needs `<title>` and `<desc>` with unique ids (`v0t`/`v0d`, `v1t`/`v1d`, …).

### Per tile, also

A stakeholder line: `data-who` (a role, uppercase in render), `data-said` (something that role would
actually say, one sentence), `data-chip` (a short present-participle status such as "Setting the
gate"). The script swaps these as the tile changes. Tile 1's values must *also* be hardcoded into the
`#voice-who` / `#voice-said` / `#voice-chip` elements in the hero, because that is the pre-JS state.

### On the last tile only

A `<p class="thread">` that traces one constraint across the objectives in order, the way the pilot's
does. Find the real dependency chain in the synthesis; do not manufacture one. If a domain genuinely
has no such chain, write instead a one-sentence statement of what makes its objectives one discipline,
which is the pattern D5 and D6 use in their own lessons.

## Prose rules — these are hard

From `C:\Claude Cowork\CLAUDE.md`, and they are the reason the pilot reads the way it does:

- **No manufactured drama.** The reference deck this format came from used thriller titles ("The
  Legacy Codebase Nobody Dares Touch"). Titles here state the situation flatly: "A regional insurer,
  8,000 claims a month". Do the same.
- **No diagnose-negate-reveal for plain facts.** Do not write "That is not X. That is Y, and it is Z"
  unless X is a misconception a real candidate holds.
- **A checkable fact gets one flat sentence.** No setup, no invented false belief to negate.
- **Say a new idea once.** No paragraph that restates its own first sentence with more feeling.
- **Max ~2 em-dashes per file.** The pilot has one. Use colons, periods, commas.
- **Banned:** "not just X but Y", "it's not about X, it's about Y", leverage, robust, seamless, delve,
  ecosystem, comprehensive, holistic, myriad, plethora, "it's worth noting".

## The exact substitution checklist

Copy the pilot, then change every one of these. The last two are the ones that get missed, and they
break silently.

| # | What | In the pilot | Change to |
|---|---|---|---|
| 1 | `<title>` | Domain 1: Solution Design & Architecture | the domain's name |
| 2 | Top HTML comment | domain, tile count, paths, accent | this domain's |
| 3 | Accent tokens in `:root` and `[data-theme="dark"]` | amber | see the colour table |
| 4 | Skip-link text | "Skip to the six objectives" | match the tile count |
| 5 | `.topnav .home` | "CCAR-P · Domain 1" | this domain |
| 6 | `.badge` | Domain 1 · 17% · Solution Design & Architecture | this domain and weight |
| 7 | `<h1>` | the situation, flatly stated | this scenario |
| 8 | `.setup` | scenario setup, key figures in `<b>` | this scenario |
| 9 | `.concepts` | six terms, `·` separated | one per objective |
| 10 | Hero voice elements | tile 1's who/said/chip | this domain's tile 1 |
| 11 | `<ol class="stepper">` `aria-label` | "The six objectives" | match the count |
| 12 | Stepper `<li>` items | 6 items, `tab-0..5`, labels | one per objective |
| 13 | `<section class="tile">` blocks | 6 tiles, `tile-0..5` | one per objective |
| 14 | `.count` initial text | `1 / 6` | `1 / N` |
| 15 | `.foot` | paths and weight | this domain's |
| 16 | **`history.replaceState`** | `'#1.' + (at + 1)` | `'#2.'`, `'#3.'` … |
| 17 | **hash regex on the last line** | `/^#1\.([1-6])$/` | `/^#2\.([1-5])$/` etc. — the digit *and* the range |

Items 16 and 17 are the trap. If you leave them at `1`, deep links silently stop working and nothing
errors. Grep your finished file for `#1.` and confirm zero hits in any domain but 1.

Do **not** change: the theme script, the `show()` function, the tablist keyboard handling, the no-JS
fallback CSS, or any `s-*` SVG class. They are domain-agnostic and already verified.

## Colour

Each domain gets one accent. The first four are already audited in this token system; the last three
are proposed and the contrast gate decides. **If a proposed hue fails the gate, fall back to an
audited one and note it in the file's top comment** — a repeated hue across two domains is fine, a
failing contrast ratio is not.

| Domain | Accent | Status |
|---|---|---|
| 1 | amber (done) | audited |
| 2 | blue | audited — alias `--blue`, `--blue-dark`, `--blue-light`; `--accent-on-raised: oklch(0.78 0.09 247)` |
| 3 | green | audited — alias `--green*`; `--accent-on-raised: oklch(0.78 0.10 152)` |
| 4 | coral | audited — alias `--coral*`; `--accent-on-raised: oklch(0.79 0.11 32)` |
| 5 | violet | proposed — light `0.47 0.11 300` / light-tint `0.93 0.03 298` / dark-text `0.40 0.10 300`; dark-mode `0.70 0.11 300` / `0.24 0.04 300` / `0.80 0.09 300`; on-raised `0.80 0.11 300` |
| 6 | teal | proposed — light `0.48 0.09 195` / `0.93 0.025 192` / `0.40 0.08 195`; dark-mode `0.70 0.10 195` / `0.23 0.04 193` / `0.80 0.08 195`; on-raised `0.80 0.10 197` |
| 7 | rose | proposed — light `0.53 0.13 350` / `0.94 0.028 352` / `0.44 0.11 350`; dark-mode `0.70 0.12 350` / `0.24 0.045 350` / `0.80 0.10 350`; on-raised `0.80 0.11 352` |

For a proposed hue, add the full token triple to both `:root` and `[data-theme="dark"]` following the
shape of the existing `--amber*` entries, then alias `--accent*` to it.

## Verification — do this per file, in a browser, before moving on

Reading the source is not verification. Open the file with the browser tools and run these. **All five
must pass.** Two of them caught real defects in the pilot that reading could not have.

1. **Paging.** Click every stepper node. Exactly one tile visible each time; `.count` tracks;
   `data-who`/`data-said`/`data-chip` swap; `aria-selected` follows; prev disabled on the first tile,
   next disabled on the last.
2. **Keyboard.** Dispatch `ArrowRight` / `ArrowLeft` on `document.body` and confirm the counter moves
   and returns. (Dispatching on `document` gives a target with no `.closest`, which is a flaw in your
   test, not the page.)
3. **Deep link.** Confirm the regex resolves `#N.1`…`#N.<last>` to the right tile and anything out of
   range falls back to tile 1. If the preview pane serves the file as a `data:` URL it will strip the
   hash, so test the regex directly rather than by loading a URL.
4. **SVG geometry.** For every tile, `getBBox()` each `<text>` and assert it sits inside the 190×168
   viewBox, and that no two labels on the same baseline overlap. A 1.6px overrun in the pilot was
   invisible by eye and only this caught it.
5. **Contrast, both themes, every tile.** Walk every text node and check against its background at
   4.5:1 (3:1 for large or bold). **SVG text needs a separate check** — hit-test which `<rect>` sits
   under each label's centre and use that rect's `fill`, because walking CSS backgrounds reports SVG
   labels as clean when they are not. Zero failures required in light *and* dark.

Then check the prose mechanically: em-dash count ≤2, no banned phrases, no space before a comma or
period (a stray `" ,"` pattern has bitten this project before), and roughly 130 words per tile.

## Delivering

Commit each domain separately so a bad one can be reverted alone. Message states which domain, the
tile count, the accent, and what the browser verification actually returned — not that you ran it.

End your turn with: the file paths, the per-file verification results, and anything you could not
source from the lesson and therefore left out. If a domain's synthesis was too thin to build a
faithful spine, say so plainly rather than filling the gap yourself.
