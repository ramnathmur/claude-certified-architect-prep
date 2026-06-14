# GATE 2 — Build Quality & Usability Review

**Artifact:** `courses/claude-101/claude-101.html` (1,624 lines, single file)
**Source of truth:** `courses/claude-101/source/claude-101_source.md` (597 lines)
**Reviewer role:** Independent Senior QA Lead + AI Student (adversarial)
**Date:** 2026-06-04

---

## 1. Build Quality Findings

### Self-containment / external dependencies — PASS
- A full scan for `https?://`, `src=`, `href="http`, `@import`, `url(http`, `cdn`, `googleapis`, `fonts.` returned **zero matches**.
- The only `href` attributes are in-page anchors (`#l1`…`#l14`, `#top`, `#sec1`). No remote scripts, stylesheets, fonts, or images.
- All CSS is inline in a single `<style>` block; all JS is in a single inline `<script>` IIFE.
- Fonts use system stacks only (`-apple-system, … sans-serif`). No webfont fetch.
- **No external dependency exists.** Opening the file offline will render and run fully.

### Illustrations / SVG — PASS
- All 8 figures are inline `<svg>` with `role="img"` and `aria-label`. No `<img>`, no raster, no external/base64 image.
- SVGs are well-formed: `viewBox` set, markers (`#ah`, `#ah2`, `#ah3`) defined before use, paths/rects/text closed. `max-width:100%;height:auto` keeps them responsive.
- Minor note: each SVG redefines a `<style>` inside `<defs>` with class names (`.rb`, `.pc`, `.dc`, etc.) scoped per-SVG. SVG `<style>` is **not** scoped to the SVG by spec — it leaks to the document. Class names are unique enough here that no visible collision occurs, but it is technically global. Cosmetic only. (MINOR)

### HTML well-formedness — PASS
- `<!DOCTYPE html>`, `lang="en"`, `charset`, viewport meta all present.
- Structure balances: `.layout` → `aside` + `main` → `.wrap` closed at line 1496, `main` 1497, `layout` 1498.
- Headings hierarchy is sane: `h1` (hero) → section dividers `h2` → lesson `h3.ltitle` → `h4` → `h5`. No skipped-down jumps within a lesson. Quiz blocks use `h4`. Acceptable.

### Accessibility basics — PASS with minor notes
- SVGs are labeled (`role="img"` + `aria-label`). Good.
- Color palette is an editorial warm theme; ink `#2b2622` on paper `#fff`/`#faf8f5` is high contrast (>12:1). Accent `#c96442` is used for non-essential chrome and on white in pills; body text never relies on the accent for legibility.
- **MINOR:** MCQ feedback encodes correctness with color (green/red) plus a `✓`/`✗` mark and a "Correct!/Not quite." text prefix — so it is not color-only. Good.
- **MINOR:** Collapsible callouts (`.chead` with `onclick`) are `<div>`s, not `<button>`s, and have no `role="button"`/`tabindex`/keyboard handler. They are mouse-operable only — not keyboard-focusable. Same for the reveal/quiz which DO use real `<button>`s (those are fine). The callouts are progressive-disclosure of supplementary content, not core, so this is MINOR, not a blocker.
- **MINOR:** Mobile menu button has `aria-label="Menu"` (good) but no `aria-expanded` state toggle.

---

## 2. JS-Logic Trace Summary

The script is a single IIFE (`"use strict"`). Traced each subsystem against the DOM as written:

**TOC build (1503–1520):** `sections` array lists all 14 lessons across 5 groups. For each lesson it creates `<a href="#l{n}" data-target="l{n}">`. Targets `l1`…`l14` — every one matches a real `<section class="lesson" id="l{n}">`. No dangling anchors. Mobile click closes the nav. **Sound.**

**Progress bar + scroll-spy + completion (1522–1552):**
- `onScroll` computes scroll % into `#progressBar`. Guarded against divide-by-zero (`height>0`). Sound.
- Active link: iterates `lessonEls`, picks last whose `offsetTop<=mid`, sets `.active` on matching nav `a`. Section-divider blocks (`#sec1`…) are NOT `section.lesson`, so they're correctly ignored by scroll-spy. Sound.
- Completion ticks: marks `seen[el.id]=true` once a lesson's top passes 60% viewport; nav links get `.done`. `doneCount=Object.keys(seen).length`; percent = `doneCount/14`. There are exactly 14 lesson sections, so the denominator is correct. **No off-by-one.**
- `onScroll` runs once on load. Sound.

**Mobile nav (1554–1558):** toggles `.open` on `#sidebar` and `#scrim`. Both IDs exist. Scrim has inline `onclick="toggleNav()"`; `toggleNav` is exposed on `window` *inside* the IIFE — exposed before any user interaction can fire, so the inline handler resolves. Sound.

**Callout collapse (1561):** `toggleCall(head)` toggles `.collapsed` on `head.parentElement` (the `.callout`). All callouts ship with class `collapsed` so they start closed and the chevron CSS rotation matches. `toggleCall` exposed on `window` for the inline `onclick`. Sound.

**Reveal (1564–1569):** finds `.ans` sibling, adds `.show`, disables the button. Each `.reveal` block has exactly one `.ans`. Sound.

**MCQ handler (1572–1599):** For every `.mcq[data-mcq]`:
- `correct=parseInt(data-correct)`. Spot-checked several: L1 `data-correct="2"` → option index 2 = "1M tokens" (correct). L4 `data-correct="0"` → "Connectors first, then Chrome, then screen interaction" (matches source priority order). Section-2 Q3 `data-correct="3"` → "Live database connections" as the NOT-a-type answer (correct). Final-check Q3 `data-correct="0"` → "Code" mode (matches source: Code applies file edits, checks before terminal). **`data-correct` indices verified correct on sampled questions.**
- On click: guards `answered` (one-shot), disables all options, marks the correct one with `✓`, marks a wrong pick with `✗`, shows feedback pulling text from the hidden `.fbmsg`. Every `.mcq` includes both an empty `.fb` and a hidden `.fbmsg`, so `msg` is never empty. Sound.
- `appendMark` (1600) creates the `.mark` span. The guard `o.querySelector('.mark')||appendMark(...)` prevents double-marking. Sound.

**Quiz scoring (1602–1619):** For `data-inquiz` MCQs inside a `.quizblock`:
- After an answer, `mcq.dataset.result` is set to `'1'`/`'0'` and `updateQuiz` runs.
- `answered` = MCQs whose `dataset.result!==undefined`. For an unanswered MCQ the attribute is absent and `dataset.result` is the JS value `undefined`, so it is correctly excluded. Live score `score/total` updates the `[data-score]` pill on each answer.
- When `answered.length===total`, the result box shows tiered messaging at ≥75% / ≥50% / below. Each section quiz has 4 MCQs; the final check has 10. Counts match the rendered `data-score` initial text ("0 / 4", "0 / 10"). **No off-by-one; thresholds sound.**

**Console-error scan:** No reference to IDs/selectors that don't exist; no undefined variables; all `window.*` handlers defined before reachable. **No console errors expected from the code as written.**

**One genuine logic limitation (MAJOR-adjacent, classified MINOR):** Quiz state is **per-page-load only** — there is no persistence (no `localStorage`). Reloading resets all progress, scores, and reveals. For a self-study prep tool this is acceptable (and avoids stale-state bugs), but a learner who refreshes loses everything. Documenting as MINOR since the spec did not require persistence.

---

## 3. Usability Findings (AI-Student persona)

- **Navigation is clear.** Left sidebar groups 14 lessons under 5 named sections with numbered circles; active lesson highlights; completed lessons get a green check; a live "Course progress %" sits at the top. Smooth-scroll on click. On mobile a hamburger + scrim pattern works and auto-closes on selection.
- **Reading order is linear and sensible** — section divider → lessons → section quiz, repeated, ending with conclusion + final check. Each lesson ends with a "What's next" pointer, which is good scaffolding for a learner.
- **Quizzes are understandable.** Each option is a large clickable button; after answering, the correct answer is always revealed (even on a wrong pick) with `✓`/`✗` and an explanation. This is good pedagogy (no dead-ends). Section quizzes show a running `n / 4` and a tiered result message once all are answered.
- **Predict-before-reveal** blocks match Ram's stated learning methodology ("predict before run") — a real plus.
- **Potential stick points (all MINOR):**
  1. Collapsible callouts are not keyboard-operable (mouse-only). A keyboard-first learner can't open "Key takeaways" — but the core lesson prose is always visible, so no content is truly locked away.
  2. No quiz "reset/retry" button; to re-attempt a question the learner must reload (losing all other progress). Minor friction for active recall / spaced repetition.
  3. The final check is 10 questions but the lesson meta says "Quiz · 13 questions (on Academy)" — this is correct (the 13 is the official gated quiz; the 10 is the practice check) and the in-page note explains it well, so unlikely to confuse.

No blocker-level usability defect: a learner can read every lesson, take every quiz, see feedback, and track progress without getting stuck.

---

## 4. No-Dilution Check

Compared the HTML against the 597-line source markdown.

- **All 14 lessons present**, in source order, under the correct 5 sections.
- Lesson 1 capabilities (5 bullets), access methods, 200K/1M-token detail — **verbatim-faithful**.
- Lesson 2 three-part prompt framework, the full example prompt, 4D-framework attribution (Dakan/Feller), file types, Memory/Styles — **all retained**.
- Lesson 3 full 5-row challenges table reproduced cell-for-cell; 4D framework; eval methodology (4 steps) — **retained**.
- Lesson 4 Cowork — the densest lesson — retains the full feature list (Folder access, Scheduled tasks, Subagents, Dispatch, Projects, Browser use, Computer use w/ priority order + blocklist + macOS-only research-preview caveat, Plugins, Protected environment), the Code Ask/Code/Plan modes, local vs remote, and the 3-column comparison table including the "Hooks" cell. **Nothing trimmed for the SVG.**
- Lessons 5–12 (Projects/RAG-10x, Artifacts/15-line threshold/publish-not-indexed, Skills/projects-vs-skills, Connectors/MCP-USB-C/two types, Enterprise Search required connectors, Research 5–15/45-min + agentic loop + web-search-required, role use-cases, other tools + summary table) — **all key facts present and source-grounded**.
- **Lesson 14 / certificate quiz:** The source itself records (line 581+) that the 13 official questions sit behind a graded gate and were **intentionally not harvested**. The HTML faithfully discloses this in an exam note and substitutes a freshly-authored, source-grounded 10-question practice check. This is **not dilution** — it matches the source's own integrity decision and Ram's project rule against republishing a graded answer key.
- Footer claim ("every claim traces to a lesson section; no external facts introduced") is **substantiated** by the comparison.

**Verdict on dilution:** The interactivity and illustrations were **added on top of** the content, not at its expense. No lesson was dumbed-down or truncated.

---

## 5. Findings Ledger

| # | Severity | Finding |
|---|---|---|
| 1 | MINOR | Collapsible callout headers are `<div onclick>`, not keyboard-focusable/operable. Core prose unaffected. |
| 2 | MINOR | No quiz persistence or per-question retry; reload resets all state. |
| 3 | MINOR | SVG `<defs><style>` class rules are document-global (SVG style isn't auto-scoped); no visible collision due to unique class names. |
| 4 | MINOR | Mobile menu button lacks `aria-expanded` toggle. |

**BLOCKER: 0  |  MAJOR: 0  |  MINOR: 4**

No external dependency, no broken handler, no off-by-one in scoring, no content dilution.

---

## FINAL VERDICT

**GATE 2: PASS**
