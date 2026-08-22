# Gate 2 — Build & Usability Review
## prompt-engineering-depth.html (C-E5)

_Reviewer personas: Senior QA Lead + AI Student (independent of the producer). Date: 2026-06-06._

**VERDICT: PASS** — 0 blockers, 0 majors.

**Counts:** Blockers: 0 · Majors: 0 · Minors: 1

---

## Findings
### Blockers (0) / Majors (0)
None.

### Minor 1 — SVG `<g>` group closes mid-stream in the ladder diagram (cosmetic)
The technique-ladder SVG `<g>` wraps only rungs 1–5; rungs 6–7 + caption render outside it. The `<g>` carries no transform/style, so grouping has zero visual effect and all 7 rungs render correctly. Global `<g>`/`</g>` balance is 1:1 (not malformed). **→ FIXED post-gate (group extended to wrap all rungs).**

---

## Checklist (items 1–8)
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Self-contained, no external loaded deps | PASS | 0 external script/link/@import; 0 `<img>`; URLs only in Sources `<a href>`. All CSS/JS/SVG inline. |
| 2 | Code-block escaping (CRITICAL, XML-heavy) | PASS | **9 `<pre><code>` blocks + 142 inline `<code>` spans — ZERO raw `<`/`>`.** Every XML example (`<thinking>`, `<answer>`, `<example>`, `<document>`, `<instructions>`, `<smoothly_flowing_prose_paragraphs>`) escaped. |
| 3 | Quiz/MCQ JS logic | PASS | Final quiz = 10 `.mcq[data-inquiz]`; denominator `total=mcqs.length` (dynamic) — no off-by-one. All 22 MCQs 4 options, `data-correct` 0–3. 12 inline MCQs lack `data-inquiz` → don't pollute score. |
| 4 | Standardized `.cnav` bar | PASS | Present once after `<div class="wrap">`, before `<header class="hero">`. Values confirmed below. Self-contained `.cnav` `<style>`. |
| 5 | Navigation | PASS | Sticky sidebar TOC, scroll-spy `.active`, `#progressBar`, mobile menu + scrim. Only in-page anchor `#top` resolves. No duplicate IDs (21 unique). |
| 6 | Collapsibles keyboard-operable | PASS | `role="button"`, `tabindex="0"`, `aria-expanded`, Enter/Space/Spacebar handlers. |
| 7 | Required elements | PASS | Extension banner; back-link → `../claude-101.html`; "What's next" points only to Launchpad + "no next lesson" (no invented forward link); Sources (6 PRIMARY + 2 SECONDARY); 7 inline SVGs (≥6). |
| 8 | Usability / no JS errors | PASS | Heading hierarchy clean; no undefined refs / duplicate IDs; `aria-live="polite"` on all 22 feedback divs; predict-reveal functional; no orphan SVG groups (Minor 1 cosmetic, fixed). |

## Explicit confirmations
- `.cnav`: `cnav-home="../../../Launchpad.html"`, `cnav-prev="prompt-caching-economics.html"`, **`cnav-next` ABSENT** (correct — C-E5 is the last file). ✓
- Both nav hrefs resolve on disk: `Launchpad.html` ✓ and `prompt-caching-economics.html` ✓ (bonus: `../claude-101.html` back-link resolves ✓).
- `<pre><code>` count: **9**; raw angle brackets across all blocks + 142 inline code spans: **ZERO**. ✓

**Gate 2 result: PASS.** Self-contained, all XML code escaped, dynamic-denominator quiz, correct `.cnav` (no Next), all required elements + a11y present. Single cosmetic SVG minor fixed post-gate.
