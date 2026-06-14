# Gate 2 — BUILD / INTERACTIVITY — `claude-code-configuration.html`

**VERDICT: PASS** — 0 blockers · 0 majors · 2 minors

Independent adversarial QA (reviewer did not author the lesson). JS was traced by hand and re-verified with Python/grep scans over the 1,415-line file. Every interactive widget was confirmed to bind, score, and resolve its element references correctly. The two findings below are non-breaking content/cosmetic miscounts.

---

## Checklist results

| Check | Result | Evidence |
|---|---|---|
| 1. Self-contained / offline | PASS | No `<script src>`, no `<link href>`, no `@import`, no CDN/font/image network loads. The only `http(s)` hrefs are 16 `code.claude.com/docs` citation links + the grep hit at line 1295 is `a.href='#'+l[0]` (an in-page anchor, not external). Works under `file://`. |
| 2. Duplicate ids | PASS | 27 ids extracted; `uniq -d` returns nothing. Includes 3 SVG marker ids (`ah`, `ah2`, `ah3`) — all distinct. |
| 3. TOC / scroll-spy / progress | PASS | JS `sections` array targets `lA…lH` + `sources` (9). All 9 resolve to `<section class="lesson" id=...>`. No TOC anchor points nowhere; no lesson section missing from TOC. `TOTAL=navOrder.length` (dynamic, =9) — no hard-coded denominator. |
| 4. MCQ + quiz scoring | PASS | 17 MCQs total (7 inline + 10 in-quiz). Every `data-correct` index (0–3) maps to the genuinely correct option text (traced all 17 — see below). Final quiz: exactly 10 `data-inquiz` MCQs, labelled Q1–Q10, wired to `updateQuiz`. Denominator = `mcqs.length` (per-block, =10) — no off-by-one. 17 `aria-live="polite"` regions (one per `.fb`). |
| 5. Collapsible callouts / toggles | PASS | `toggleCall`, `toggleNav`, `doReveal` all defined as `window.*` and referenced by `onclick`. Callout `.chead` elements also get `role=button`, `tabindex=0`, keydown (Enter/Space) handlers, and `aria-expanded` sync. |
| 6. Code-block escaping | PASS | 14 `<pre><code>` blocks; Python scan found zero raw `<` inside any block. Angle brackets in prose use `&lt;`/`&gt;` / `&amp;` (verified in MCQ option text e.g. Q1 `Managed &gt; CLI args`). |
| 7. JS errors / dead refs | PASS | All 5 `getElementById` targets exist (`toc`, `progressBar`, `progPct`, `sidebar`, `scrim`). No undefined-variable refs. `pct` guarded against divide-by-zero (`height>0?…:0`). No intervals/timeouts (scroll/resize listeners only; nothing to clear). Tags balanced: svg 7/7, pre 14/14, section 9/9, table 9/9, script 1/1. In-quiz MCQs carry no static `data-result` attr, so `dataset.result!==undefined` correctly counts only answered questions. |
| 8. `.cnav` link resolution | PASS | From `courses/claude-101/extensions/`: `../../../Launchpad.html` EXISTS, Prev `prompt-engineering-depth.html` EXISTS, base backlink `../claude-101.html` EXISTS (all confirmed on disk). C-track END confirmed: `.cnav` has only Home + Prev, NO `cnav-next`; the "What's Next" box and footer both state "no next lesson." |

### MCQ answer-key trace (all 17 correct)
Inline: A→2 (concatenated/broadest-first), C→3 (opus + rules merge), D→1 (deny absolute), E→2 (PreToolUse exit 2), F→0 (skill precedence), G→3 (local=old "project"), H→1 ("solves the wrong problem"). 
Quiz Q1→2, Q2→3, Q3→0, Q4→1, Q5→2, Q6→3, Q7→1, Q8→0, Q9→2, Q10→1 — each index lands on the substantively correct option. Pass/mid thresholds (`pct>=75` / `>=50`) are sound.

---

## Findings

### Minor 1 — Hero pill claims "8 diagrams" but only 7 exist
- **Location:** line 223 `<span class="pill">…🎨 8 diagrams</span>`; figures at lines 283, 373, 475, 599, 715, 1032, 1127.
- **What breaks:** Nothing functional. `class="svgfig"` count = 7 (all render, all SVG tags balanced). The count claim is off by one.
- **Why:** Diagram captions run "(a) (b) (c) (d) (e) (g) (h)" — caption **(f) is skipped** (line ~952's Section F "decision table" is an HTML `<table>`, not an SVG figure, but the caption lettering still jumped from e→g as if an (f) diagram existed and was removed).
- **Suggested fix:** Either change the pill to "7 diagrams" (line 223), OR relabel captions g→f and h→g so the sequence is contiguous (a–g). Cosmetic only.

### Minor 2 — `secA…secH` divider ids are unreferenced (dead-but-harmless)
- **Location:** lines 261/334/447/576/692/860/992/1079 (`id="secA"` … `id="secH"`).
- **What breaks:** Nothing. The TOC intentionally links to the `lA…lH` lesson sections, not the dividers. The `sec*` ids are simply never targeted by any anchor or JS.
- **Suggested fix:** Optional — leave as-is (useful as future anchor handles), or remove to trim. No action required for PASS.

---

## Notes for downstream gates
- Content-accuracy claims (verbatim quotes, ⚠ VERIFY flags, exam facts) are **out of scope for Gate 2** and were not assessed — defer to Gate 3.
- The "(f)" caption gap (Minor 1) is worth a glance in Gate 3 to confirm no diagram was meant to exist for Section F.
