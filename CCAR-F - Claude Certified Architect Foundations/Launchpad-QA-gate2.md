# GATE 2 — Build Quality & Usability QA Report
**Artifact:** `Launchpad.html` (project root)
**Reviewer role:** Independent Senior QA Lead + AI Student (adversarial; logic traced by hand — no browser run)
**Date:** 2026-06-05

---

## 1. Build / Self-Contained

| Check | Result |
|---|---|
| Single file, no companion assets needed to render | PASS |
| Remote `<script>` references | None |
| Remote `<link>` / stylesheet references | None |
| External fonts (`fonts.googleapis`, `@font-face`) | None — uses system font stack only |
| External images (`<img src="http...">`) | None — all illustrations are inline SVG generated in JS |
| `http(s)://` resource references | None |
| `url(...)` references | One: `url(#hg)` (line 489) — an **internal** SVG gradient fragment, not external. OK. |

Grep for `https?://|src=|@import|url(|<link|cdn|googleapis|fonts.` returned only the internal `url(#hg)`. **The page is fully self-contained and works offline / over `file://`. No BLOCKER, no MAJOR.**

---

## 2. Launch Correctness

All four LIVE launchable cards point to files that exist on disk (verified via glob).

| Card id | Live? | `href` in DATA | Resolves? |
|---|---|---|---|
| `claude-101` (base; no `status` field → treated as shipped) | Yes | `courses/claude-101/claude-101.html` | ✅ exists |
| `tool-use-agent-loop` (ext, `status:'live'`) | Yes | `courses/claude-101/extensions/tool-use-agent-loop.html` | ✅ exists |
| `intro-subagents` (base, `status:'live'`) | Yes | `courses/introduction-to-subagents/introduction-to-subagents.html` | ✅ exists |
| `orchestration-patterns` (ext, `status:'live'`) | Yes | `courses/introduction-to-subagents/extensions/orchestration-patterns.html` | ✅ exists |

**Queued cards** (`c-e2`…`c-e5`, `s-e2`, `s-e3`): all have `status:'queued'` and **no `href` key**. In `cardHTML()` the queued branch renders only a "Coming soon" chip — no `<a class="launch">`, and `.card.queued .foot{display:none}`. They are not clickable and cannot navigate. Correct.

**No BLOCKER. Launch wiring is correct.**

---

## 3. JS Logic — Hand Trace

**localStorage (lines 500–513):** Key `cca-launchpad:v1:progress`. `loadState()` JSON-parses with try/catch → `{}` fallback (handles disabled storage / corrupt value / null). `saveState()` wrapped in try/catch (won't throw in private mode). `statusOf` defaults to `'not-started'`. `setStatus` deletes the key for `'not-started'` (keeps the store lean) else writes. Clean.

**`shippedCards()` (516–523):** Pushes base if `base.status!=='queued'`. The `claude-101` base has **no** `status` field → `undefined!=='queued'` → `true` → included (intended). Pushes each extension where `status!=='queued'`. Result = exactly the 4 live cards, in ladder order. Correct.

**Aggregate / divide-by-zero (638–653):** `total = ship.length` = 4 (always ≥1 given current DATA). `pct = total ? done/total*100 : 0` — guarded against zero regardless. **No divide-by-zero.** `done===total` and `done===0` branches both handled; `pct>=60` and fallback messages cover the middle. Pluralization `module(s)` handled.

**Featured "next" (603–635):** Loops shipped cards; `next` = first non-`done`. `allDone` starts true and is cleared on any non-done. `anyStarted` true if any status ≠ not-started.
- **All-done case:** `next` stays null in loop, then `if(allDone){ next=ship[ship.length-1]; }` reassigns to last card before any `next.*` deref → safe.
- **None-started case:** `next` = first card, kick = "✦ Start here". Correct.
- **Edge:** `next.domain` / `next.href` only dereferenced after the all-done guard, and `ship` is non-empty, so `next` is never null. Safe. (Would only break if DATA had zero shipped cards — not the case, but noted as a latent assumption: MINOR.)

**Renderers:** `renderLegend` (d1–d5), `renderTracks` → `wireCards`, `renderHero`, `renderFeatured` all run at boot (749–752). `renderTracks` rebuilds innerHTML then re-wires — handlers correctly re-attached after each full re-render (reset path). Per-card updates use `refreshCardVisual` (no full re-render, no handler loss). Good.

**Handlers:**
- `mark` button: toggles done ↔ not-started, toasts on completion, refreshes card + hero + featured. Fires (delegated via per-card `addEventListener` set in `wireCards`).
- `launch` anchor: sets `in-progress` if `not-started`, refreshes, then lets the plain anchor navigate (file://-safe — no `preventDefault`). Correct.
- Featured launch: separate **document-level** delegated listener (722–728) keyed on `[data-feat-launch]` — survives `renderFeatured` re-renders (the featured node's innerHTML is replaced, so a per-node listener would be lost; document delegation is the right call). Sets in-progress + re-renders hero. Good design choice.
- `reset` (731): confirm() gate, clears state, full re-render, toast. Fires.
- `pageshow` (740): reloads state from storage and refreshes every card + hero + featured — correctly resyncs progress after returning from a lesson via back-button/bfcache. Idempotent on initial load.

**Undefined vars / broken selectors / off-by-one:** None found. All `getElementById`/`querySelector` targets exist in the static HTML or are produced before they're queried. `data-mark-em`/`data-mark-tx` inner spans are queried inside the `if(mk)` guard in `refreshCardVisual` and always exist when `mk` does. No off-by-one in the ring math (`stroke-dasharray`/`dashoffset` standard).

**JS verdict: no BLOCKER, no MAJOR.**

---

## 4. Accessibility

| Item | Status | Note |
|---|---|---|
| Skip link | Partial — **MAJOR** | `.skip` exists and targets `#tracks`, but `#tracks` is a plain `<section>`, **not** a `<main>` landmark; the link lands mid-page but there is no programmatic main region. |
| Landmarks (`<main>`, `<nav>`) | **MAJOR gap** | No `<main>` element wraps the content; no `<nav>`. Screen-reader users get only `<header>`, `<section>`, `<footer>` implicit roles. Wrapping the course library (or the whole `.shell`) in `<main id="main">` and pointing the skip link at it would close this. |
| `aria-pressed` on mark buttons | PASS | Set on render (line 559) and kept in sync in `refreshCardVisual` (680). Toggles true/false correctly. |
| `aria-label` on rings | PASS | Small ring: "N% complete"; hero ring: "Overall progress N percent". Illustration SVGs correctly `aria-hidden="true"`. |
| `focus-visible` | PASS | Defined for `.btn`, `.mark`, `.launch`, `.reset` (3px outline). |
| `prefers-reduced-motion` | PASS | Global `transition:none!important; scroll-behavior:auto` (237–239). Note: the SVG ring `style="transition:..."` is inline and **not** overridden by the media query's `*{transition:none!important}` — actually it IS, because `!important` beats inline. OK. |
| Color not sole signal | PASS | Status conveyed by text ("Done"/"In progress"/"Not started"), ✓/○ glyph, ribbon text "Completed", and "Coming soon" chip — not color alone. |
| Toast | PASS | `role="status" aria-live="polite"`. |
| Reset confirmation | PASS | Native `confirm()` — accessible. |

**Accessibility: 2 MAJOR gaps (missing `<main>`/landmark; skip link target is not a true landmark). Everything else passes.**

---

## 5. Usability (AI-Student lens)

**Can a learner succeed at the core loop?** Yes.
- **Understand the ladder:** The sec-sub explains base-course-at-top / extensions-branch-beneath, the visual rail + "↳ Go deeper" label reinforce it, and the domain legend with weights orients exam relevance. Clear.
- **Find the next step:** The Featured card ("✦ Start here" → "Claude 101") is the single most prominent CTA and updates as you progress (Start → Continue → Revisit). Strong.
- **Launch:** Big primary button on featured + per-card "Launch →". Works.
- **Mark done & see progress update:** Mark-done toggles instantly, fires a celebratory toast, updates the card ring, hero ring, "N of 4" count, and the top progress bar. Satisfying, immediate feedback.
- **Queued / coming-soon clarity:** Desaturated illo, faint text, dashed "🔒 Coming soon" chip, and **no** launch/mark controls. Unambiguous that they're not yet available.

**Where a learner might get stuck / friction (MINOR):**
1. **"In progress" is a one-way trap-ish state.** Launching a lesson sets `in-progress` and shows a 50% ring, but there's no way to clear `in-progress` back to "not started" — only Mark-done (→done) or a global Reset. A learner who clicks Launch by accident is stuck at a permanent 50% ring for that card until they mark done or reset everything. Minor confusion risk.
2. **Progress is per-browser/per-device with no sync** — stated in the footer ("Progress saved on this browser only"), so expectations are set. Fine, but worth knowing.
3. The hero `done===0` copy hard-codes "Start with Claude 101 below" — correct today, but coupled to DATA ordering (a content assumption, not a bug).

**Usability verdict: the core learn-loop is clear and works. Only MINOR friction.**

---

## 6. Dead Code / Minor Smells

| Item | Severity | Note |
|---|---|---|
| `tint(hex,a)` (line 374) | MINOR | Defined, self-described as "overkill," and **never called** anywhere. Dead code — safe to delete. |
| Latent `next` null assumption in `renderFeatured` | MINOR | Safe only because DATA always has ≥1 shipped card. If every card were ever queued, `next.domain` would throw. Defensive guard would harden it. |
| `.dotw` inline-styled span inside pill (line 546) | MINOR | Styled entirely inline rather than via the existing `.dot` class — cosmetic inconsistency, no functional impact. |
| Inline ring `transition` style | MINOR/none | Overridden by reduced-motion `!important`, so fine. |

---

## Severity Summary

| Severity | Count | Items |
|---|---|---|
| **BLOCKER** | 0 | — |
| **MAJOR** | 2 | (a) No `<main>`/landmark wrapper; (b) skip link targets a non-landmark `<section>` |
| **MINOR** | 4 | dead `tint()`; latent `next`-null assumption; in-progress not user-clearable; `.dotw` inline-style smell |

No external dependencies. No broken launch links. No JS error that breaks render. No divide-by-zero.

---

**GATE 2: PASS**
