# QA Gate 2 — Build & Usability
**File:** `extensions/subagents-as-sdk-primitive.html`
**Reviewer:** Gate 2 (independent) · Senior QA Lead + AI Student
**Scope:** Build mechanics & usability (NOT factual accuracy)

## Verdict: **PASS**

0 Blockers, 0 Majors. Code-heavy lesson is escaping-clean, self-contained, and the quiz scoring is sound.

---

## Quick metrics
- **Inline SVG diagrams:** 10 (≥6 required ✓) — three-doors, AgentDefinition anatomy, precedence ladder, delegation flow, boundary crossing, context isolation, no-nesting, least-privilege combos, frontmatter↔SDK map, subagent-vs-workflow.
- **MCQ count:** 20 total — 10 inline (`data-mcq` without `data-inquiz`) + 10 final-quiz (`data-inquiz`).
- **Quiz questions vs denominator:** 10 questions (`data-inquiz`); `total=mcqs.length` → denominator **10**; display `0 / 10`. No off-by-one. ✓
- **External dependencies:** ZERO. All 7 `https://` refs are inside the visible Sources `<ol>` (lines 1155–1161). No CDN/font/image/remote-script refs anywhere. Opens cleanly from `file://`.

---

## Blockers
None.

## Majors
None.

## Minors
1. **Self-acknowledged dead forward link.** `nextbox` (line 1169) points to `orchestrator-worker-at-scale.html` which "may 404." The page labels this inline ("not built yet; this forward link may 404"), so it is honest and not a defect — flagged only so the link is wired once S-E3 ships. No fix required now.
2. **`.fbmsg` carries `hidden` attribute but is read via `innerHTML` only** (lines 1272–1273) — the hidden source div is never displayed directly (its HTML is copied into `.fb` on answer). Works correctly; just noting the `hidden` div remains in DOM as a (harmless) source-of-truth element.
3. **Scroll-spy "done" uses `data-target` keyed on `seen[]`** (line 1229) — the Assessment/Final link has `data-target="final"` but `final` is a `sec-divider`, not a `section.lesson`, so it never marks "done." Cosmetic only; lesson progress (10 lessons) is the intended completion metric and computes correctly.

---

## Detailed checks

### 1. Self-contained — PASS
Grep for `https?://` returns only the 7 Sources citation links (lines 1155–1161). No `<link>`, no `<script src>`, no `@import`, no external `url()`/font/image. Fully offline-capable.

### 2. Code-block escaping — PASS (critical for this lesson)
Programmatic scan of all 4 `<pre class="code">` blocks (after stripping allowed `<span>`/`<code>` tags) found **zero raw `<`** that the browser would swallow.
- TS `AgentDefinition` (333–348): uses `string[]`, `number`, `boolean`, union strings — square brackets only, no angle generics. Clean.
- Python dataclass (353–367): `list[str]`, `dict[str, Any]`, `Literal[...]`, `| None` — square brackets only. Clean.
- Python `query()` example (470–497): string literals + Agent tool — clean.
- YAML frontmatter (863–871): no angle brackets.
- Inline-code generics that DO need escaping are correctly escaped: `Record&lt;string, AgentDefinition&gt;` (464, 540), `.claude/agents/&lt;name&gt;.md` (230, 854, 914, 881), `agents: { "&lt;name&gt;": ... }` (890, 914). ✓

### 3. JS logic — PASS
- **Quiz denominator:** `total=mcqs.length` over `.mcq[data-inquiz]` = 10; `score/total` correct; result box thresholds (≥75 pass, ≥50 mid) fire only when `answered.length===total`. No off-by-one.
- **`data-correct` range:** all 20 values are 0–3, valid for the 4-option questions (verified each MCQ has exactly 4 `.opt` buttons).
- **Scroll-spy + sticky nav:** TOC built from `sections[]`, links `#l1`…`#l10` with `data-target` matching real `section.lesson` IDs; active-state toggled in `onScroll`. ✓
- **Progress bar:** `#progressBar` width updated on scroll (passive listener + resize + initial call). ✓
- **MCQ reveal / predict / collapsibles:** single-answer guard (`answered` flag), `doReveal` disables button, `toggleCall` toggles `.collapsed`. No null-ref paths (every `.fb`/`.fbmsg` guarded with `if`/ternary).
- **Hamburger menu:** `.menubtn onclick="toggleNav()"` wired to a real global handler; scrim also calls it; `aria-expanded` synced.

### 4. Accessibility — PASS
- Collapsibles: `role="button"`, `tabindex="0"`, Enter/Space handler (`keydown`), `aria-expanded` initialized and toggled to reflect state (1249–1256, 1247).
- MCQ feedback: `.fb` gets `aria-live="polite"` + `role="status"` (1271).
- Single `<main>` (line 198 / close 1178). One only.
- Nav reachable via keyboard; menu button has `aria-label`.

### 5. Required structural elements — PASS
- Extension banner "Beyond the Academy course" — lines 202–205 ✓
- "← Back to the base course" → `../introduction-to-subagents.html` — lines 192, 1169(footer back), 1174 ✓
- Sibling link to `orchestration-patterns.html` — lines 212, 1174 ✓
- Forward "What's next" → `orchestrator-worker-at-scale.html` — line 1169 ✓
- Sources section listing citation URLs — lines 1151–1163 (7 sources) ✓
- Inline SVG count: 10 (≥6) ✓

### 6. Usability / parity — PASS
Coherent long-form scrollable document (sticky sidebar TOC + section dividers + lesson sections), not a deck. No duplicate IDs (l1–l10, secA/B/C, final, top, sources all unique). No dead controls. Matches the S-E1 reference design system (same `:root` tokens, callout/mcq/quiz/svgfig components, progress bar, mobile drawer).

---

**Zero-external-deps confirmation:** All network references are the 7 Sources citation URLs inside the visible Sources block; no CDN, font, image, or remote script — the file is fully self-contained and renders offline from `file://`.
