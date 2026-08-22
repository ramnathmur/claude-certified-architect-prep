# GATE 2 — Build Quality & Usability QA Report

**Artifact:** `courses/claude-101/extensions/tool-use-agent-loop.html`
**Reviewer role:** Independent Senior QA Lead + AI Student (adversarial; did not build this)
**Reference (no-dilution baseline):** `extensions/source/tool-use-agent-loop_citations.md`
**Date:** 2026-06-05

---

## 1. Build findings

### Self-contained / no external dependencies — PASS
- Grepped for `https?://`, `src=`, `@import`, `url(http`, `integrity=`, `crossorigin`.
- The **only** `http(s)` references are the six citation hyperlinks in the Sources `<ol>` (lines 1046–1051) and the footer crosslinks — these are intended outbound links a learner clicks, **not** resource loads. No stylesheet, script, font, or image is fetched from the network.
- No `<img>`, no external `<link rel=stylesheet>`, no `<script src>`. CSS is one inline `<style>` block; JS is one inline IIFE. **Fully self-contained.**

### SVG — PASS
- 5 inline `<svg>` figures; `<svg>` open/close balanced (5/5).
- Each carries `role="img"` + descriptive `aria-label`. Markers, gradients, and `<text>` nodes are well-formed. No external `xlink:href` / image refs.

### Code blocks (`<pre><code>` JSON) — PASS (clean)
- 6 fenced JSON blocks (server-tool request, get_weather tool def, full request, assistant `tool_use` response, `tool_result`, error `tool_result`).
- Checked for HTML-escaping artifacts: **zero** `&lt;`, `&gt;`, `&quot;`, or numeric entities anywhere in the file.
- Confirmed **no angle brackets** (`<`/`>`) inside any code-block body, so nothing can be mis-parsed as a stray tag. JSON uses only `{}[]":,` which are not HTML-special and render verbatim.
- `pre` 6/6 and `code` 342/342 tags balanced. The JSON renders exactly as authored.

### Tag balance — PASS
`svg 5/5`, `pre 6/6`, `code 342/342`, `section 8/8`, `table 5/5`, `div 228/228`. No structural imbalance.

---

## 2. JS logic trace (by hand)

### TOC / nav build — correct
- `sections[]` produces 8 nav links: `l1`–`l7` + `sources`. Every `data-target` resolves to an existing element ID (section IDs at lines 237, 340, 492, 594, 701, 773, 925, 1040). **No dangling scroll-spy targets.**
- `TOTAL = navOrder.length` = 8 → **dynamic denominator, no off-by-one.**

### Progress / scroll-spy — correct
- `onScroll` computes progress from scrollTop/height for the top bar (independent of lesson count — fine).
- Lesson-completion `progPct` uses `doneCount/TOTAL` over the same 8 `navOrder` IDs that drive the nav. Denominators match. `seen[]` is set off `section.lesson` offsets; the 8th section (`sources`) is a `section.lesson`, so 100% is reachable. **Correct.**

### MCQ scoring — correct, no off-by-one
- 19 MCQs total = 7 standalone quick-checks + 4 (Checkpoint Quiz A) + 8 (Final). Verified programmatically.
- **Every** MCQ has exactly 4 `.opt` buttons and a `data-correct` in `[0,3]` — all in range (verified by script; full table below).
- Per-quiz denominator = `mcqs.length` (`.mcq[data-inquiz]` within that quizblock) → Quiz A = 4, Final = 8. **Dynamic, matches actual question counts.** No hard-coded denominator drift; the visible "0 / 4" and "0 / 8" labels are overwritten by JS to `score + ' / ' + total`.
- Result thresholds: ≥75 pass, ≥50 mid, else mid — all branches reachable; box shows only when `answered.length===total`.
- Standalone MCQs: `mcq.closest('.quizblock')` is null and guarded by `if(quiz && mcq.hasAttribute('data-inquiz'))` — they correctly do **not** feed any quiz score. No crash.

**data-correct vs. answer-text spot audit (semantics):** Quiz A Q1–Q4 (idx 2/3/0/1), Final Q1–Q8 (idx 1/2/0/3/2/0/1/3), and the 7 quick-checks all point at the factually correct option per the citations. No mis-keyed answers found.

### Reveals / collapsibles / nav / a11y — correct
- `doReveal`: shows `.ans`, disables button, relabels — idempotent. Good.
- Collapsibles: each `.chead` gets `role="button"`, `tabindex="0"`, and an initialized `aria-expanded`; `keydown` handles Enter / Space / Spacebar with `preventDefault`; `toggleCall` flips both the `collapsed` class and `aria-expanded`. **Fully keyboard-operable.** (Initial state of all callouts is `collapsed` → `aria-expanded="false"`, consistent.)
- Mobile menu: `toggleNav` toggles `open` on sidebar + scrim and updates the menu button's `aria-expanded`. Nav links close the drawer on click at ≤980px. Works.
- MCQ feedback `.fb` carries `aria-live="polite"`; the explanation is stored in a `hidden` `.fbmsg` and injected on answer — screen readers announce it. Good pattern.

**No JS bugs found.** `"use strict"` IIFE, no globals leaked except intentional `window.toggleNav/toggleCall/doReveal`.

| MCQ | data-correct | #opts | In range |
|----|----|----|----|
| 1–19 | 2,1,2,3,0,1,2,1,0,3,2,1,2,0,3,2,0,1,3 | 4 each | YES (all) |

---

## 3. Cross-link check — PASS

| Required link | Present | Location | Correct target |
|---|---|---|---|
| ← Back to base course → `../claude-101.html` | Yes | sidebar (L192), crosslink box (L222), footer (L1061) | Yes |
| "What's next" → `context-management.html` | Yes | nextbox (L1036), footer (L1061) | Yes (sibling path; honest "may not exist yet" caveat) |
| Extension banner | Yes | L214–219 ("Extension — beyond the Academy course") + sidebar badge L191 | Correct framing |
| Sources section | Yes | L1040–1057, all 6 sources as clickable links + [VERIFY] note | Complete |

Relative paths are correct given the file sits in `extensions/` and `claude-101.html` is one level up.

---

## 4. Usability findings (AI-Student lens)

**Overall: a learner can follow this end to end.** Strong points:
- "Why before how" honored (Section 1 opens with the contract mental model before the loop steps).
- The Section 6 worked example is the standout: Steps 1→5 are in strict logical wire order (request → `tool_use` response → execute → `tool_result` → `end_turn`), each JSON block labeled with a realistic "POST /v1/messages" / "Response · assistant turn" / "Next request · appended user message" header. The `tool_use_id`/`id` pairing is explicitly called out (L866). **The JSON steps are readable and correctly ordered.**
- Predict-first reveals before answers reinforce active recall; per-bucket responsibility table removes the most common confusion.

Minor friction points (not blockers):
- **MINOR:** All callouts (including "Key takeaways" and the QA-critical traps) default to **collapsed**. A skimming learner could miss the takeaways entirely. Consider defaulting Key-takeaways open. Functional, just a discoverability nudge.
- **MINOR:** Section 3's `disable_parallel_tool_use` "at most one" vs "exactly one" distinction is subtle; it is handled well by the predict-reveal, but a learner who skips the reveal only gets it from a bullet list. Acceptable.
- **MINOR:** The "what's next" link points to a file the report confirms may not exist yet; the inline caveat is honest, but a click will 404 until `context-management.html` lands. This is by design (wired ahead) and disclosed.

No place where a learner gets truly stuck.

---

## 5. No-dilution check vs. citations — PASS

| Citation element | Present in HTML | Note |
|---|---|---|
| Tool-use-as-contract + "model never executes anything on its own" | Yes (L252, L326) | Verbatim quotes retained |
| Canonical 5-step `while` loop | Yes (L266–272) | All 5 steps intact |
| 4 loop-exit stop reasons (end_turn/max_tokens/stop_sequence/refusal) | Yes (L296, table L298–307) | Complete |
| Server loop + `pause_turn` | Yes (L320–322) | Intact |
| No `tool`/`function` role; tool_use→assistant, tool_result→user | Yes (L353–360, diagram L362) | Intact |
| Three buckets (user-defined / Anthropic-schema / server) | Yes (L386–406, diagram, table) | All three, with per-bucket dev responsibility |
| Server tools: no `tool_result`, no `is_error` | Yes (L406, L421, reveal L412) | Intact |
| All 4 `tool_choice` options + defaults | Yes (L505–512) | auto/any/tool/none all present with both defaults |
| Prefill gotcha for any/tool | Yes (L530–532) | Verbatim |
| Extended-thinking restriction (only auto/none) | Yes (L546–547) | Intact |
| tool_choice invalidates message cache | Yes (L548–549) | Intact |
| `disable_parallel_tool_use` (at most/exactly one) | Yes (L551–556) | Both cases |
| Unordered parallel-call semantics | Yes (L557) | Intact |
| Tool def fields + name regex `^[a-zA-Z0-9_-]{1,64}$` | Yes (L612–615) | Intact |
| Description "by far the most important factor" + best practices | Yes (L646–647) | Consolidate / namespacing / high-signal all kept |
| Good vs poor description contrast | Yes (L650–658) | Verbatim |
| `strict: true` guarantee | Yes (L667–668) | Intact |
| Auto-injected system prompt + [VERIFY] token counts | Yes (L670–672) | [VERIFY] flag preserved |
| Worked turn (all 5 steps, real JSON) | Yes (Section 6) | Full fidelity, including error case |
| Ordering rules → 400 (immediately-follow + result-first) | Yes (L868–872, recap L912) | Both rules, both flagged 400-causing |
| `is_error: true` + retry 2–3 times | Yes (L877–889) | Intact |
| Parallel results in one user message | Yes (L894–895) | Intact |
| When to / not to use tools + regex heuristic | Yes (Section 7) | Intact |
| Security: indirect prompt injection, keep in tool_result | Yes (L962–964, MCQ L966) | Intact |
| [VERIFY] flags (model id, web_search version, token counts) | Yes (L436, L672, L786, L1055) | All preserved, not silently "corrected" |

**Depth is not reduced.** Every substantive claim, all `tool_choice` options, the three buckets, the full worked turn, the ordering rules, and the security note survive intact. Author-supplied framing (observe–think–act) is explicitly flagged as a teaching overlay (L741), preserving source honesty.

---

## Severity summary

- **BLOCKER:** 0
- **MAJOR:** 0
- **MINOR:** 3 (collapsed-by-default takeaways; subtle parallel-tool distinction; forward-wired next link 404s until target lands — all disclosed/by-design)

All three MINORs are usability nudges, not defects. Build is clean, JS is correct, cross-links resolve, content matches the citations at full depth.

---

**GATE 2: PASS**
