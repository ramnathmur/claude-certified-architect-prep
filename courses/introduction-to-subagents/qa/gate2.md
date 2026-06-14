# GATE 2 — Build Quality & Usability QA Report

**Artifact:** `courses/introduction-to-subagents/introduction-to-subagents.html`
**Source of truth:** `source/introduction-to-subagents_source.md`
**Reviewer role:** Senior QA Lead + AI Student (independent / adversarial)
**Date:** 2026-06-05

---

## 1. Build Quality

### Self-containment / external dependencies — PASS
- Single self-contained `.html` file. All CSS is in one inline `<style>` block; all JS is in one inline `<script>`.
- **Grep for `http(s)://`, `src=`, remote `href`, CDN hosts, `@import`, `url(http…)` returned ZERO matches.** No remote scripts, stylesheets, fonts, or images.
- Fonts are system stacks only (`-apple-system`, `"SF Mono"`, etc.) — no Google Fonts / webfont fetches.
- The only `href` values are in-page anchors (`#l1`–`#l4`, `#final`, `#top`). No external navigation.
- **No external dependency. Self-contained requirement met.**

### Images / illustrations — PASS
- All 7 illustrations are **inline `<svg>`** (context-vs-subagent, 15-files collapse, /agents flow, config anatomy, description dual-role, tool-access tiers, anti-patterns, decision-rule flowchart — actually 8 figures total, hero pill claims "7 architecture diagrams"; see MINOR-3).
- No `<img>`, no raster, no external/base64 images. Each `<svg>` has `role="img"` + `aria-label`. Markup is well-formed (matched tags, valid attributes).

### `<pre><code>` blocks — PASS
- 5 code blocks render correctly with no HTML-escaping breakage:
  - L2 subagent YAML config (block 1 of 3) — frontmatter `---`, fields, body intact.
  - L2 `description: Proactively…` snippet.
  - L3 structured output format (block 2 of 3) — numbered list 1–6.
  - L3 "Obstacles Encountered" section (item 7).
  - L4 JWT summary (block 3 of 3).
- `white-space:pre` preserves indentation. No raw `<`/`>` collisions; syntax spans (`.frontmatter`, `.key`) are valid. Multi-line content not mangled.

### HTML validity — PASS
- `<!DOCTYPE html>`, `lang="en"`, charset + viewport meta present. Tag nesting is balanced; layout (`aside` + `main` inside `.layout`, `.wrap` inside `main`) closes cleanly.
- All nav targets referenced by JS-built TOC (`#l1`–`#l4`, `#final`, `#top`) exist in the DOM. No dangling ID references.

### Accessibility — PASS (minor gaps)
- Collapsible callout headers: JS adds `role="button"`, `tabindex="0"`, `aria-expanded`, and a `keydown` handler for **Enter / Space / Spacebar** with `preventDefault`. Keyboard-operable. ✓
- `aria-expanded` is initialised on load and toggled on each open/close. ✓
- Mobile menu button has `aria-label` and `aria-expanded` (toggled in `toggleNav`). ✓
- Heading hierarchy is sane: `h1` (hero) → section dividers `h2` → lesson titles `h3` → `h4`/`h5`. Logical order.
- Contrast: charcoal ink (#2b2622) on cream (#faf8f5) and white code text on dark (#2b2622) are high-contrast. Accent (#c96442) used on soft backgrounds — acceptable.
- Gaps (MINOR): MCQ option `<button>`s have no `aria-live` region for feedback; quiz feedback appears visually but is not announced. The `chev` indicator relies on rotation only. Not blockers.

---

## 2. JS-Logic Trace Summary

| Mechanism | Trace result | Verdict |
|---|---|---|
| TOC build | `sections` array → 4 lesson links + Assessment/Final link, injected into `#toc`. Targets all exist. | OK |
| Progress bar | `onScroll` computes `scrollTop/height*100` → `#progressBar` width. Guards `height>0`. | OK |
| Course progress % | `doneCount/TOTAL_LESSONS*100`, `TOTAL_LESSONS=4` (correct denominator). | OK |
| Scroll-spy active nav | Tracks `section.lesson` via `offsetTop`; sets `.active` on matching `nav a[data-target]`. | OK for 4 lessons; final-check link never activates (MINOR-1) |
| "Seen"/done ticks | `seen[el.id]` set when lesson passes 60% viewport; adds `.done` ✓. Final link never marked done (MINOR-1). | OK (lessons) |
| Smooth scroll nav | CSS `html{scroll-behavior:smooth}` + anchor hrefs. No JS needed. | OK |
| Mobile menu | `toggleNav` toggles `.open` on sidebar+scrim, updates `aria-expanded`. Nav links auto-close on click ≤980px. | OK |
| Collapsible callouts | `toggleCall` toggles `.collapsed`; click + keyboard (Enter/Space). | OK |
| Predict / reveal | `doReveal` shows `.ans`, disables button, relabels "Answer shown ✓". | OK |
| MCQ selection | First click locks (`answered` flag), marks correct/wrong, shows feedback from hidden `.fbmsg`, appends ✓/✗. | OK |
| `data-correct` mapping | Spot-checked all 4 standalone + final Q8 + sampled in-quiz items — indices map to intended option. | OK, no off-by-one |
| Quiz scoring | `updateQuiz` counts `.mcq[data-inquiz]`; score = results==='1'; denominator = actual MCQ count. | OK |
| Quiz denominators | L1–L4 = **4 each** (verified 4 `data-inquiz` per `quizblock`); Final = **8** (verified). Display "0 / 4" and "0 / 8" match. | OK, no off-by-one |
| Result band | ≥75% pass, ≥50% mid, else re-read. Shows only when all answered. | OK |

**No undefined variables, no broken selectors, no IDs referenced-but-absent, no handlers that fail to fire.** `appendMark` defined before use (hoisted function declaration). `mcq.dataset.result` vs the `data-result` resultbox div are on different elements — no collision. IIFE with `"use strict"` and `window.`-scoped global handlers correctly exposed for inline `onclick=`.

---

## 3. Usability

**Can an AI-Student follow it end to end? — Yes.**
- Clear linear order: hero/about → "From what to when" divider → Lesson 1→2→3→4, each followed immediately by its 4-question quiz, then an 8-question final check. Matches source lesson order exactly.
- Each lesson opens with an "What you'll be able to do" objectives box and ends with "What's next" + a collapsible Key Takeaways — good orientation and recall scaffolding (aligns with the project's AI-first methodology: Why-before-How, predict-before-reveal, active recall).
- Quizzes are understandable; feedback is immediate, color-coded, and explains *why* (pulled from `.fbmsg`). Predict-first reveals are well placed.
- Progress bar + per-lesson done-ticks + % give a sense of advancement.

**Where a learner could get mildly stuck (none blocking):**
- **MINOR-1:** Clicking "Final knowledge check" in the nav scrolls there, but the nav link never highlights as active/done (scroll-spy only watches `section.lesson`, and the final block is a `div.quizblock`). A learner who relies on the highlight to confirm location gets no feedback there. Course % also caps based on the 4 lessons only.
- **MINOR-2:** Quizzes lock on first click with no reset/retry. Fine for a one-shot check, but a learner who misclicks cannot re-attempt without reloading.
- The quizzes are not gated (you can scroll past), which is acceptable for self-study.

---

## 4. No-Dilution Check (vs source)

| Source element | In HTML? | Notes |
|---|---|---|
| 4 lessons (What are / Creating / Designing / Using) | ✅ all 4 | Full prose preserved, near-verbatim |
| Built-in subagents (General purpose, Explore, Plan) | ✅ | All 3 named with descriptions |
| 2 inputs + 1 return (system prompt + task → summary) | ✅ | Stated and diagrammed |
| Tradeoff (lose visibility into *how*) | ✅ | Bolded, in reveal + quiz |
| `/agents` flow, scope (project/user), generate, tools, model, color | ✅ | All fields + flow diagram |
| Config file + 5 frontmatter fields + body=system prompt | ✅ | YAML block verbatim + anatomy SVG |
| "proactively" + example conversations | ✅ | Included |
| **4 design patterns** (descriptions, output format, obstacle reporting, limited tools) | ✅ all 4 | Section per pattern + summary + takeaways |
| Description's dual role (when + what) | ✅ | Diagram + reveal |
| Structured output format code block (1–6) | ✅ verbatim | |
| Obstacles section (item 7) | ✅ verbatim | |
| **Tool-access tiers** (read-only Glob/Grep/Read; reviewer +Bash; modifier +Edit/Write) | ✅ all 3 | Tiered SVG + prose + quiz |
| **3 anti-patterns** (expert claims, sequential pipelines, test runners) | ✅ all 3 | Collapsible callouts + SVG; "test runner performed worst" preserved |
| When subagents shine (research, code review, custom prompts) + JWT example | ✅ | JWT code block verbatim |
| **Decision rule** ("does the intermediate work matter?") | ✅ | Flowchart + use/avoid table |

**No content was trimmed to make room for visuals.** Interactivity and SVGs *augment* the source; every source claim is traceable. Author analogy (intern/archives) is explicitly labelled "(Author analogy, not a product fact.)". CCA-F domain mapping is framed as orientation, not added syllabus. **No dilution.**

---

## 5. Findings by Severity

**BLOCKER:** none.

**MAJOR:** none.

**MINOR:**
1. Final-knowledge-check nav link never gets `.active`/`.done` and course % is capped to the 4 lessons (scroll-spy/seen logic only watches `section.lesson`, not the quiz/final blocks). Cosmetic nav feedback gap.
2. Quizzes lock permanently on first click — no retry/reset without page reload.
3. Hero pill says "7 architecture diagrams" but there are 8 inline SVG figures. Harmless undercount.
4. MCQ feedback is not exposed to assistive tech via `aria-live`; screen-reader users get no announcement on answer.

---

## 6. Verdict

- Build quality: valid, self-contained, zero external dependencies, sound JS, correct quiz denominators (4 / 4 / 4 / 4 / 8), all code blocks render, accessible collapsibles.
- Usability: clear, linear, well-scaffolded; only cosmetic gaps.
- No dilution: all 4 lessons, 4 design patterns, 3 tool tiers, 3 anti-patterns, and the decision rule are fully present and source-faithful.

**GATE 2: PASS**
