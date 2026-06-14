# QA Gate 2 — Build & Usability Report

**File under review:** `courses/claude-101/extensions/context-management-reliability.html`
**Reference (shipped, for parity):** `courses/claude-101/extensions/tool-use-agent-loop.html`
**Reviewer role:** Senior QA Lead + AI Student (independent — did not build this file)
**Date:** 2026-06-05

---

# VERDICT: **PASS**

**0 Blockers · 0 Majors · 2 Minors.** Meets the PASS bar (0 Blockers AND 0 Majors). The lesson is fully self-contained, the quiz scoring math is correct on both quizzes, all MCQ answer indices are in range, code blocks are properly escaped, accessibility is wired, and every required structural element is present. The two Minors are cosmetic/non-blocking.

---

## Headline metrics

| Metric | Result |
|---|---|
| **External dependencies** | **0** — zero CDN/font/image/script. All 9 `http(s)://` refs are Anthropic doc URLs inside the visible "Sources" section + source-citation prose (allowed). Opens offline from `file://`. |
| **Inline `<svg>` diagrams** | **7** (≥5 required ✓) — diagrams (a)–(g), one per Sections 2–9 |
| **MCQ blocks (total)** | **22** — 8 standalone inline checks + 14 in-quiz (4 in Quiz A, 10 in Final) |
| **Options per MCQ** | 4 on every block (verified all 22) |
| **`data-correct` range** | All values 0–3 — every index in range for 4 options. No off-by-one. |
| **`<main>` landmarks** | 1 (single) |
| **Duplicate IDs** | None |

### Per-quiz question count vs. scoring denominator

| Quiz | Rendered `data-inquiz` questions | Denominator (`total = mcqs.length`) | Verdict |
|---|---|---|---|
| Checkpoint Quiz A (`data-quiz="1"`) | 4 | 4 (dynamic) | ✓ exact |
| Final Knowledge Check (`data-quiz="final"`) | 10 (heading says "10 questions") | 10 (dynamic) | ✓ exact |

Denominator is computed live as `quiz.querySelectorAll('.mcq[data-inquiz]').length` (line 1303) — scoped per-quiz, so it cannot drift from the rendered count. The lesson-progress denominator `TOTAL` (line 1209) is likewise `navOrder.length` (10 nav targets), computed from the same array that builds the TOC. No hardcoded totals anywhere.

**Zero external dependencies confirmed.** Only outbound references are the 9 Anthropic citation URLs in the Sources `<ol>` and inline source tags — no remote scripts, fonts, stylesheets, or images.

---

## Blockers

**None.**

Verification notes for each Blocker-class check:
- **Self-contained:** No `<link>`, no external `<script src>`, no `@import`, no `url(http…)`, no remote image/font. All styling is one inline `<style>`; all JS is one inline `<script>`. ✓
- **Scoring math:** Both quizzes use a dynamic denominator equal to the actual question count (4 and 10). ✓
- **MCQ indices:** All 22 `data-correct` values ∈ {0,1,2,3}; every block has exactly 4 `.opt` buttons. No out-of-range index. ✓
- **Code escaping:** The `<budget:token_budget>` / `</budget:token_budget>` and `<system_warning>` XML (line 958–959) are escaped as `&lt;`/`&gt;`. JSON blocks with nested braces (lines 609–623, 630–644, 752–758, 931–936, 1055) contain no HTML-special chars that the browser would swallow. Scan for raw `<lowercase` inside any `<pre>` returned nothing. ✓
- **No null-ref JS errors:** Every `getElementById`/`querySelector` target exists — `progressBar`, `progPct`, `sidebar`, `scrim`, `toc`, `.menubtn` all present. MCQ handler reads `.fbmsg` via `mcq.querySelector('.fbmsg')` with a null-guard (`msgEl?…:''`, line 1276). ✓
- **Required structural elements (all present):**
  - "Extension — beyond the Academy course" banner (line 211–216) ✓
  - "← Back to the base course" → `../claude-101.html` (line 189; also footer line 1174) ✓
  - Sibling link → `tool-use-agent-loop.html` (lines 219, 1174) ✓
  - Forward "What's next" → `mcp-at-a-builder-level.html` (lines 1146, 1174) ✓
  - "Sources" section with 9 citation URLs (lines 1149–1170) ✓
  - Single `<main>` landmark ✓

---

## Majors

**None.**

Verification notes:
- **Scroll-spy + sticky nav:** TOC links carry `data-target` = section IDs (`l1`–`l9`, `sources`). `onScroll` (lines 1215–1236) matches `section.lesson` elements by `offsetTop`, sets `.active` on the matching `nav a[data-target=…]`, and marks `.done`. Selectors match real IDs. ✓
- **Reading-progress bar:** Updates on scroll via `progressBar.style.width = pct + '%'` (line 1220), listener registered passive (line 1237) plus an initial `onScroll()` call. ✓
- **MCQ reveal / predict-before-reveal / collapsibles:** `doReveal` toggles `.ans.show` and disables the button (1263–1268); `toggleCall` toggles `.collapsed` and flips `aria-expanded` (1249–1252); MCQ click disables all options, marks correct/wrong, shows feedback, and pipes in-quiz results to `updateQuiz`. All wired to real elements. ✓
- **Hamburger menu:** `toggleNav` (1242–1246) toggles `.open` on sidebar + scrim and updates the button's `aria-expanded`. Button `onclick="toggleNav()"` (line 179) and scrim `onclick` (line 180) both wired. ✓
- **Accessibility:** Collapsible headers are made keyboard-operable in JS — `role="button"`, `tabindex="0"`, `aria-expanded` initialized to match state, and an Enter/Space keydown handler with `preventDefault` (lines 1253–1260). Each of the 22 MCQ feedback panes is an `aria-live="polite"` region (22 found). Hamburger button has `aria-label` + `aria-expanded`. Nav is reachable (anchor links). ✓
- **Duplicate IDs / overflow / dead controls:** None found. Tables wrapped in `.tablewrap{overflow-x:auto}`; code in `pre{overflow-x:auto}`. ✓
- **Parity with C-E1 reference:** Same interaction model (data-mcq blocks, aria-live feedback, collapsibles, reveal buttons, scroll-spy, progress bar). Reference uses 20 `data-mcq` / 19 `aria-live`; this file uses the same component vocabulary and is consistent. ✓

---

## Minors (cosmetic — non-blocking)

1. **Hero pill says "9 sections" but the TOC renders 10 nav entries.** The pill (line 204) counts the 9 teaching sections; the TOC + progress denominator include a 10th "Reference / Sources" entry (`navOrder.length = 10`, line 1195/1209). This is internally consistent for scoring (progress correctly reaches 100% only after Sources is seen), but a reader comparing the "9 sections" pill to the 10-item sidebar may briefly notice the mismatch. Optional fix: reword the pill to "9 lessons + sources" or leave as-is (Sources is a reference appendix, not a lesson). No functional impact.

2. **Forward link to `mcp-at-a-builder-level.html` will 404 until that file ships.** This is *correctly and explicitly disclosed* inline ("that file is not built yet — this forward link may 404 until it lands," line 1146), so it is an intentional, labeled forward reference rather than a defect. Noted only for completeness; no action required.

---

## Summary

The lesson reads as a coherent, scrollable long-form document (sidebar TOC + sticky scroll-spy + progress bar + 9 teaching sections + 2 scored quizzes + sources), not a deck. Build mechanics are sound: self-contained, correct scoring on both quizzes, in-range answer keys, escaped code, wired accessibility, and all required structural elements present. Interaction parity with the shipped C-E1 reference is maintained.

**Gate 2 result: PASS.**
