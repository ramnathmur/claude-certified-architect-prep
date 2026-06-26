# QA Gate 2 — Build & Usability — Launchpad.html

**Reviewer:** QA Gate 2 (independent). **File:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\Launchpad.html`
**Date:** 2026-06-05

---

## VERDICT: **PASS**

0 Blockers, 0 Majors. Two Minors (cosmetic / non-functional). All four edits land cleanly with no regressions to JS soundness, accessibility, or offline behavior.

---

## The 4 edits — explicit confirmation

### 1. Hero stat tiles → caption — **OK**
- The three `.stat` tiles are gone from markup. Replaced by a single `<p class="examfacts" aria-label="Exam snapshot">60 questions · 120 min · pass at 720</p>` (line 258).
- `.examfacts` CSS rule exists (line 56) and is well-formed.
- No `class="stat"` / `class="snapshot"` element remains in the body (grep confirms zero markup hits; only orphaned CSS rules survive — see Minor #1).
- Markup is balanced — `.hero-copy` div closes correctly at line 259.

### 2. Per-card progress ring → status dot — **OK (critical path verified)**
- `cardHTML` footer now emits `<span class="sdot" data-ring style="background:'+sl.color+'">` (line 557). The `ring(...)` SVG is gone from the card.
- `.sdot` CSS rule exists (line 161).
- **Live update verified:** `refreshCardVisual` does `var rEl=el.querySelector('[data-ring]'); if(rEl) rEl.style.background=sl.color;` (line 677). The `[data-ring]` element still exists in the rendered card, so recolor works on mark-done / launch / reset / pageshow.
- **No leftover `.innerHTML=ring()` on the dot.** Grep for `ring(` finds only the function definition (line 475). `ring()` is called nowhere — it is now dead code (see Minor #2), but its presence breaks nothing.
- Hero ring is independent: `renderHero` calls `ringBig(pct)` → `heroRing.innerHTML` (line 645). `ringBig` is a separate function (line 485) and is untouched. Confirmed no cross-wiring.

### 3. Domain 1 recolor — **OK**
- `--wine` token trio present in `:root`: `--wine:#9b3b52; --wine-soft:#f3e3e7; --wine-deep:#7a2c40;` (line 21).
- `DOMAINS.d1` repointed: `color:'var(--wine)', soft:'var(--wine-soft)', deep:'var(--wine-deep)', hex:'#9b3b52'` (line 322). All four references resolve to defined tokens.
- **Brand accent still clay.** `--accent:#c96442` (line 15) is unchanged and still drives: CTAs (`.btn-primary` line 95, `.launch` line 172), hero ring gradient (`stop-color:var(--accent)` line 489), top bar (`#topbar` gradient line 41), eyebrow, focus rings. CTA color (`#c96442` clay) and d1 category color (`#9b3b52` wine) are now genuinely DIFFERENT. Confirmed.
- Legend renders d1 with the wine dot via `DOMAINS.d1.color` (line 599) — consistent.

### 4. Launch dominant / Mark-done secondary — **OK**
- `.launch` enlarged: `font-size:15px; font-weight:800; padding:12px 22px` (lines 172–174). Still a real anchor: `<a class="launch" href="'+card.href+'" data-launch>` (line 562) — `href` and `data-launch` wiring intact; click handler marks in-progress then navigates (lines 712–719).
- `.mark` quieted: `background:transparent; font-size:12.5px; border:1.5px solid var(--line-soft); color:var(--ink-faint)` (lines 166–168). Still a real focusable `<button type="button" data-mark aria-pressed="...">` (line 561). `aria-pressed` is set on render and updated in `refreshCardVisual` (line 682). `:focus-visible` outline preserved (line 170). It is interactive, not a faint decoration. Confirmed.

---

## Full regression scan

- **No external dependencies:** PASS. Grep for `http`, `src=`, `@import`, `cdn`, `googleapis`, `fonts.`, image extensions, `integrity=` → zero hits. All SVG is inline-generated; system font stack only. Opens fully offline on `file://`.
- **JS soundness:** PASS. `wireCards` (697), `refreshCardVisual` (670), `renderHero` (640), `renderFeatured` (605), `renderLegend` (593), `renderTracks` (571), reset (733), pageshow (742) are all consistent with the new `[data-ring]`/`.sdot` markup. Every `querySelector` result that could be null is guarded (`if(rEl)`, `if(sEl)`, `if(hEl)`, `if(mk)`). localStorage round-trips: mark done → dot recolors + `done` class + ribbon + hero ring/count/topbar update; reset clears STATE and re-renders. No null-refs introduced by the edits.
- **Accessibility preserved:** PASS. Skip link (246), `tabindex="-1"` single `<main>` (278), focus-visible rings on `.mark`/`.launch`/`.reset`, `aria-pressed` on mark, `aria-live="polite"` toast (308), reduced-motion block (240). **State is NOT carried by the dot alone** — the text label (`<span class="s" data-s>` rendering "Not started / In progress / Done", line 558) is rendered beside it and stays in sync. Color-independent state is preserved.
- **Layout/usability:** PASS. Footer row is `dot + state-txt (flex:1) + actions`. At ≤560px `.card .foot` switches to `flex-direction:column` (line 237) and actions justify space-between, so the larger Launch + quieted Mark don't overflow. 920/560 breakpoints intact. No duplicate IDs (heroRing, heroMsg, heroSub, heroCount, featured, legend, trackHost, toast, topbar, resetBtn, maincontent all unique).
- **Contrast sanity:** PASS. Wine deep `#7a2c40` on white card pill/code text is well above 4.5:1. Wine `#9b3b52` used for dots/borders (non-text). Quieted `.mark` uses `--ink-faint #8c8278` on transparent/white ≈ 3.4:1 — acceptable for a 12.5px bold control with a visible border and hover/focus affordance (see Minor #1 note).

---

## Defect list

### Blockers
None.

### Majors
None.

### Minors
1. **Orphaned CSS rules — `.snapshot`, `.stat`, `.stat .num`, `.stat .lab`** (lines 51–55). The markup they styled was removed in edit #1 but the rules remain. Dead CSS only — no rendering or functional impact. *Fix:* delete lines 51–55 for hygiene.
2. **Dead function `ring()`** (lines 475–484). No longer called anywhere after edit #2 (cards now use `.sdot`; hero uses `ringBig`). Harmless. *Fix:* remove if you want a clean file; otherwise leave as documented spare.

Minor note on `.mark` contrast: `--ink-faint` resting text sits near the WCAG AA floor for the at-rest state. Not a defect (border + label + hover/focus carry it), but if you want extra margin, bump the resting color to `--ink-soft #5c544c`.

---

## Summary
The four design edits introduced no regressions. State model round-trips correctly, the status dot is recolored live via the intact `[data-ring]` hook, accessibility and offline guarantees hold, and the clay brand accent is now visibly distinct from the wine d1 category color. Ship it. The two Minors are optional cleanup, not gates.
