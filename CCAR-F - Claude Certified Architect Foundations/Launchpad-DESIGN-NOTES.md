# Launchpad — Design Notes & Editor's Guide

*Companion to `Launchpad.html`. Read this before you extend the dashboard so you can add cards without breaking anything.*

---

## 0. The one-paragraph summary

`Launchpad.html` is the **Option B** dashboard: a single, self-contained, offline HTML file
(~40 KB, **zero external dependencies** — no CDNs, no web fonts, no scripts, no raster images).
It presents every CCA-F lesson as a **basics → advanced ladder**: each *base course* sits at the
top of a track, and its *extensions* branch beneath it on a connector spine. A reusable card
shows a topic illustration, a domain tag with exam weight, a title, a meta line, a progress ring
with state, and a **Launch** button. Progress lives in `localStorage` and drives an aggregate ring
in the hero plus a computed **"Continue / Start here"** featured block. Lessons open via plain
relative `<a href>` links so they launch reliably from `file://`.

---

## 1. Design decisions & rationale

| Decision | Why |
|---|---|
| **Inherited the lesson design system wholesale** (colors, type, radius, shadows, pill/badge styling). | The dashboard must feel like the front door to the lessons, not a different product. Same warm paper background (`#faf8f5`), same clay accent (`#c96442`), same `14–20px` radii and soft two-layer shadows. |
| **Basics → advanced ladder, not a flat grid.** | The brief's core idea. A base course is the *trunk*; extensions *branch* off it with a left spine + connector nodes, so the "go deeper" relationship is visible at a glance rather than implied by ordering. |
| **Progress as the hero metric.** | An aggregate ring + "N of 4 modules" + a slim top bar make "how far am I?" the first thing you see. Per-card rings repeat the signal locally. |
| **One computed focal point** (the featured block). | Removes decision paralysis — there is exactly one obvious next action, recalculated every time progress changes. |
| **Inline SVG for all imagery.** | The only way to be image-rich *and* offline-safe. See §3. |
| **Data-driven rendering.** | One `DATA` array is the single source of truth; the card markup is generated from it. Adding a shipped extension is a one-object edit (see §5). |
| **Plain `<a>` launchers.** | `window.open()` / `fetch()` are blocked or flaky under `file://`. A normal relative anchor is the only reliable launcher, so that's all we use. |
| **Encouraging, not corporate tone.** | "Ready for liftoff", "Nice momentum", a celebratory toast on completion — motivation cues borrowed from streak-style apps, kept restrained. |

---

## 2. The design system (tokens)

All tokens are CSS custom properties in `:root` at the top of the `<style>` block. **Change them
there and the whole page follows.**

### Color
```
--bg        #faf8f5   page background (warm paper)
--paper     #ffffff   cards & raised surfaces
--ink       #2b2622   primary text
--ink-soft  #5c544c   secondary text
--ink-faint #8c8278   tertiary / hints
--line      #e7e0d8   borders & ring tracks
--accent    #c96442   clay — primary action / brand   (+ -soft, -deep)
```
**Category (exam-domain) hues** — each domain owns a color, a soft tint, and a deep text shade:
```
Domain 1  Agentic Architecture & Orchestration  27%  → --accent (clay)
Domain 3  Claude Code Configuration             20%  → --teal
Domain 4  Prompt Engineering & Structured Output 20% → --gold
Domain 2  Tool Design & MCP                      18%  → --green
Domain 5  Context Management & Reliability       15%  → --plum   ← the one hue added beyond the lessons
Foundations (Claude 101, spans everything)            → --ink-soft (neutral)
```
`--plum` (`#7a5e8e`) was added because the lessons only ship four category hues and there are five
exam domains. It shares the lessons' muted, slightly-desaturated character so it doesn't look bolted on.

### Type
System font stack only (offline constraint): `-apple-system, BlinkMacSystemFont, "Segoe UI",
Roboto, Helvetica, Arial, sans-serif`. Scale: hero `52px` → featured `30px` → base-card title
`26px` → extension-card title `21px` → body `17px` → meta `12.5–13px`. Headings use negative
letter-spacing (`-.02em`) and `text-wrap: balance`; body uses `text-wrap: pretty`.

### Spacing, radius, shadow
- Radius: `--radius 14px` (chips, small cards) and `--radius-lg 20px` (cards, hero panel).
- Shadow: `--shadow` (resting) and `--shadow-lg` (hover / focal). Two-layer, low-opacity, warm-tinted.
- Page width: `--maxw 1120px`, gutter `28px` (`18px` on mobile).

### Card anatomy (top → bottom)
```
┌─────────────────────────────┐
│  topic SVG illustration      │  ← domain-tinted background, geometric motif
├─────────────────────────────┤
│  ● Domain name · weight%     │  ← .pill-domain  (category tag)
│  Title (code prefix if queued)│
│  One-line blurb               │
│  📘 Level   ·   N lessons     │  ← .meta chips
│  ──────────────────────────   │
│  ◔ State / hint     [Mark][Launch]│  ← progress ring + actions  (.foot)
└─────────────────────────────┘
```
Queued cards swap the `.foot` for a `🔒 Coming soon` tag and are desaturated. Done cards get a
green `✓ Completed` ribbon and a filled ring.

---

## 3. Imagery approach — **inline SVG only** (no raster assets)

**What I used:** custom inline SVG, generated by the `ILLO(type, color)` function. There is **no
`assets/` folder and no base64** — every illustration is vector markup drawn at runtime, tinted
with the card's domain color. This keeps the file small, crisp at any zoom, and 100% offline.

Each motif is abstract/geometric and maps to the topic:

| `illo` id | Motif | Used by |
|---|---|---|
| `foundations` | ascending stacked bars (a ladder of lessons) | Claude 101 |
| `agentloop` | a loop with an arrowhead + node | Tool-Use Agent Loop |
| `subagents` | one big node branching to small nodes | Introduction to Subagents |
| `orchestration` | a mesh of connected nodes | Orchestration Patterns |
| `context` | concentric arcs (a context window) | C-E2 |
| `mcp` | central hub with radiating plugs | C-E3 |
| `caching` | offset stacked layers | C-E4 |
| `prompt` | three stacked blocks (stage / task / rules) | C-E5 |

The hero ring and every progress ring are also hand-rolled SVG (`ringBig()` and `ring()`).
**No design depends on the internet to load.**

> If you ever *must* use a photo, the rule from the brief stands: store it locally in an `assets/`
> folder (or base64-embed it) and reference it relatively — never hot-link. Prefer adding a new
> SVG motif to `ILLO()` instead; it keeps the set cohesive.

---

## 4. The progress model (localStorage)

- **Key:** `cca-launchpad:v1:progress`
- **Value:** a JSON object mapping card id → status, e.g.
  ```json
  { "claude-101": "done", "tool-use-agent-loop": "in-progress" }
  ```
- **Statuses:** `not-started` (absent from the object) · `in-progress` · `done`.
- **Transitions:**
  - Clicking **Launch** (or the featured CTA) sets a `not-started` card to `in-progress` on the way out.
  - **Mark done** toggles `done` ⇄ `not-started`.
- **Ring encoding:** `not-started` = empty · `in-progress` = half-filled · `done` = full + check.
  (We don't track lesson-by-lesson progress *inside* a course — the unit is the whole module.)
- **Aggregate:** `done count ÷ number of shipped cards × 100`. **Queued cards are excluded** from the
  denominator, so "Coming soon" modules never make you look behind.
- **`pageshow` re-sync:** when you return from a lesson (back button / bfcache), the page re-reads
  `localStorage` and repaints, so state is never stale.
- **Reset:** the footer button clears the key after a confirm.

Versioning: the `v1` in the key means if you ever change the data model, bump to `v2` and old
progress is simply ignored (not corrupted).

---

## 5. How to add a new course or extension card  ← do this when a queued module ships

Everything is driven by the **`DATA`** array inside the `<script>`. You almost never touch markup or CSS.

### A. A queued extension just shipped (the common case)
Find its object in `DATA` (e.g. `c-e2`). Make two changes:
1. Change `status:'queued'` → **`status:'live'`**.
2. Add an **`href`** pointing at the new file, relative to the project root:
   ```js
   { id:'c-e2', title:'Context Management & Reliability', domain:'d5', illo:'context',
     status:'live',                                            // ← was 'queued'
     href:'courses/claude-101/extensions/context-management.html', // ← add this
     level:'Extension', lessons:'Domain 5 deep-dive',
     blurb:'…' }
   ```
That's it. The card un-greys, gains its Launch button, and joins the progress denominator
(the hero ring will recalculate, e.g. "1 of 5"). **Do not** edit the rendering code.

### B. A brand-new extension under an existing course
Add a new object to that track's `extensions:[ … ]` array. Required fields:
`id` (unique, kebab-case), `title`, `domain` (`'d1'`–`'d5'` or `'foundations'`), `illo`
(an id from the §3 table — or add a new motif), `status` (`'live'` or `'queued'`),
`level`, `lessons`, `blurb`, and — if live — `href`. Optional: `code` (e.g. `'C-E6'`), shown as a
colored prefix on the title.

### C. A brand-new base course (new track)
Add a new top-level object to `DATA`:
```js
{
  id:'track-…',
  base:{ id:'…', title:'…', domain:'…', illo:'…', status:'live',
         href:'courses/…/….html', level:'Base course', lessons:'N lessons', blurb:'…' },
  extensions:[ /* zero or more, same shape as above */ ]
}
```
Order in `DATA` = order on the page = order the featured block walks when picking "next".

### D. Adding a new illustration motif
Add a `case '<id>':` to the `switch` in `ILLO(type, c)`, returning SVG that uses `c` (the domain
hex) for fills. Keep it to a 400×210 viewBox and simple geometry to match the set.

### What to leave alone
- The `ring()` / `ringBig()` math, the `STATE` / `localStorage` plumbing, the `renderTracks` /
  `renderFeatured` / `renderHero` functions, and the CSS. They're generic and data-agnostic.
- The `DOMAINS` map — only edit it if the exam's domain names or weights officially change.

---

## 6. Accessibility notes

- Semantic landmarks: `<header>`, `<section>`, `<footer>`, real `<h1>/<h2>/<h3>`, `<article>` per card.
- A **Skip to courses** link is the first focusable element.
- Launchers are real `<a>`; Mark-done / Reset are real `<button>`s with `aria-pressed` — all
  keyboard-operable with visible `:focus-visible` outlines.
- Decorative SVG is `aria-hidden`; progress rings carry an `aria-label` with the percentage.
- Color is never the *only* signal — state always has a text label too. Contrast meets the
  lessons' established palette.
- `prefers-reduced-motion` disables transitions and smooth scroll.

---

## 7. Known limitations

- **Progress is per browser profile.** `localStorage` is scoped to the exact origin — and on
  `file://`, opening the dashboard from a different folder, a different browser, or a private
  window is a *different* origin, so progress won't carry over. There is no cross-device sync by
  design (no server). To move progress, you'd export/import the JSON manually.
- **Module-level, not lesson-level, tracking.** A course counts as one unit; we don't record how
  far you got *inside* Claude 101's 14 lessons. (The lessons track their own scroll progress
  internally; the dashboard intentionally stays coarse.)
- **`file://` quirks vary by browser.** Plain anchors are reliable everywhere; that's why nothing
  here uses `fetch`/`XHR`/`window.open`. If a browser ever blocks `localStorage` on `file://`
  (rare, configurable), progress silently no-ops — the page still works, it just won't remember.
- **The aggregate denominator is "shipped modules" (currently 4).** It grows automatically as you
  flip queued cards to `live` (§5A), which is the intended behavior — but expect the percentage to
  *drop* the moment a new module ships, since the same completions now divide by a larger total.
