# Launchpad — Wrapper Prompt (paste this back to Claude)

> Copy everything below the line into a new Claude session (attach `Launchpad.html` if you have it).
> It carries the full brief, every design decision, the token system, the data model, and the rules
> for extending the dashboard — so a fresh Claude can rebuild or safely modify it without re-deriving anything.

---

## ROLE

You are continuing work on **"Launchpad"** — a single, self-contained, **offline** HTML dashboard that
is the front door to an interactive study library for the **Claude Certified Architect — Foundations
(CCA-F)** exam. Treat the existing `Launchpad.html` as the source of truth; preserve its design system
and architecture exactly unless I explicitly ask you to change them.

## HARD CONSTRAINTS (non-negotiable — never violate)

- **Self-contained & offline.** All CSS and JS inline in one `.html` file. **No CDNs, no web fonts,
  no external scripts, no hot-linked images.** Opens by double-click from `file://` with no server.
- **`file://` launch mechanism:** lessons open via plain relative `<a href="courses/…">` anchors only.
  **Never** use `window.open()`, `fetch()`, or `XHR` for navigation — they're blocked/flaky under `file://`.
- **Imagery = inline SVG only.** No `assets/` folder, no base64. All illustrations, the hero graphic,
  and every progress ring are hand-rolled vector markup tinted by domain color. Nothing may require the
  internet to load. (If a raster image is ever unavoidable: store locally / base64, never hot-link.)
- **Scrollable long-form page, not a slide deck.**
- **Accessible:** semantic landmarks + headings, real `<a>`/`<button>` controls, `aria-pressed`,
  `aria-label` on meaningful SVG, visible `:focus-visible`, color never the only signal,
  `prefers-reduced-motion` honored, a "skip to courses" link first.

## DESIGN SYSTEM (inherited from the lesson files — keep identical)

**Tokens live in `:root` at the top of `<style>`. Edit there; the page follows.**

Colors: `--bg #faf8f5` (warm paper) · `--paper #fff` · `--ink #2b2622` · `--ink-soft #5c544c` ·
`--ink-faint #8c8278` · `--line #e7e0d8` · accent (clay) `--accent #c96442` (+ `-soft #f4e6df`,
`-deep #a44a2e`). Category/domain hues, each with `-soft` + `-deep`: `--teal #3a7d7b` ·
`--gold #b8860b` · `--green #3f7d4f` · `--red #b3402f` · **`--plum #7a5e8e`** (added beyond the four
lesson hues because there are five exam domains; matches their muted character).

Type: **system stack only** — `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
Arial, sans-serif`. Scale: hero 52 → featured 30 → base-card title 26 → ext-card title 21 → body 17 →
meta 12.5–13px. Negative letter-spacing on headings; `text-wrap: balance` (headings) / `pretty` (body).

Shape: radius `14px` (chips/small) and `20px` (cards/panels). Two-layer warm soft shadows
(`--shadow` resting, `--shadow-lg` focal). Max width `1120px`, gutter `28px`.

Tone: calm, premium, **encouraging not corporate** — "Ready for liftoff", "Nice momentum",
a celebratory toast on completion. Restraint over decoration; generous whitespace.

## EXAM FACTS (use verbatim)

- Snapshot: **60 questions · 120 min · 720 scaled score to pass.**
- Domains → category colors (name · weight · hue):
  1. Agentic Architecture & Orchestration · 27% · `--accent` (clay)
  2. Claude Code Configuration · 20% · `--teal`
  3. Prompt Engineering & Structured Output · 20% · `--gold`
  4. Tool Design & MCP · 18% · `--green`
  5. Context Management & Reliability · 15% · `--plum`
  - "Foundations" (Claude 101, spans all) → `--ink-soft` neutral.

## PAGE STRUCTURE

`hero` (title, one-line purpose, exam-snapshot stats, aggregate progress ring + encouraging message)
→ `featured` "Continue / Start here" block (the single computed next action)
→ `Course library`: a **basics → advanced ladder**. Each **base course** is the trunk; its
**extensions** branch beneath it on a left connector spine with nodes. Live cards launch; queued cards
are desaturated with a `🔒 Coming soon` tag.
→ `footer` (brand, "saved on this browser / offline" note, Reset progress).

**Reusable card anatomy (top→bottom):** topic SVG illustration (domain-tinted bg) → domain pill
(name · weight%) → title (optional colored `code` prefix like `C-E2 ·`) → one-line blurb →
meta chips (📘 level · N lessons) → divider → progress ring + state text + `[Mark done]` + `[Launch →]`.
Done cards get a green `✓ Completed` ribbon and a filled ring.

## DATA MODEL (single source of truth)

Everything renders from a JS `DATA` array of tracks; a `DOMAINS` map holds the palette; `ILLO(type,color)`
returns SVG motifs; `ring()`/`ringBig()` draw progress rings. Card markup is generated — **do not
hand-write cards.**

Current contents:
- **Track 1 — Claude 101** (Base, 14 lessons, Foundations) → `courses/claude-101/claude-101.html`
  - LIVE ext: *The Tool-Use Agent Loop* (Domain 2) → `courses/claude-101/extensions/tool-use-agent-loop.html`
  - QUEUED: C-E2 Context Management & Reliability (D5) · C-E3 MCP at a Builder Level (D2) ·
    C-E4 Prompt Caching Economics (D5) · C-E5 Prompt Engineering Depth + Model Selection (D4)
- **Track 2 — Introduction to Subagents** (Base, 4 lessons, Domain 1) →
  `courses/introduction-to-subagents/introduction-to-subagents.html`
  - LIVE ext: *The Five Orchestration Patterns* (Domain 1) →
    `courses/introduction-to-subagents/extensions/orchestration-patterns.html`
  - QUEUED: S-E2 Subagents as a Programmable Primitive (D1) · S-E3 Orchestrator-Worker at Scale +
    Failure Modes (D1)

SVG motif ids: `foundations` (ascending bars) · `agentloop` (loop+arrow) · `subagents` (node→branches) ·
`orchestration` (node mesh) · `context` (concentric arcs) · `mcp` (hub+plugs) · `caching` (stacked
layers) · `prompt` (three blocks).

## PROGRESS MODEL

- `localStorage` key **`cca-launchpad:v1:progress`** → `{ "<cardId>": "in-progress" | "done" }`.
- Statuses: `not-started` (absent) · `in-progress` (set when a card is launched) · `done` (toggled by
  Mark done). Ring: empty / half / full+check.
- Aggregate = done ÷ **shipped** cards × 100 (queued excluded from denominator). Drives the hero ring,
  the slim top bar, and the "N of 4 modules" chip.
- Featured block recomputes the first non-done shipped card in ladder order each time progress changes.
- `pageshow` re-reads storage so returning from a lesson repaints fresh. Footer Reset clears the key.

## HOW TO EXTEND (do this, nothing else)

- **A queued extension ships:** in its `DATA` object, set `status:'queued'`→`'live'` and add a relative
  `href`. The card un-greys, gains Launch, and joins the denominator. Touch no other code.
- **New extension:** push an object to that track's `extensions[]` (`id, title, domain, illo, status,
  level, lessons, blurb`, + `href` if live, optional `code`).
- **New base course:** add a top-level `{ id, base:{…}, extensions:[…] }` to `DATA`. Array order = page
  order = the order featured-next walks.
- **New illustration:** add a `case` to `ILLO()` returning SVG that uses the passed color, 400×210 viewBox.
- **Leave alone:** ring math, localStorage plumbing, render functions, CSS — they're data-agnostic.

## KNOWN LIMITATIONS (keep, don't "fix" without asking)

Progress is per-browser-profile and per-`file://`-origin (no server sync by design); tracking is
module-level not lesson-level; the aggregate %\ dips when a new module ships (same completions, bigger
denominator) — that's intended.

---

### What I want now

> _(Add your request here — e.g. "C-E2 just shipped at `courses/claude-101/extensions/context-management.html`,
> wire it up", or "add a search/filter bar by domain", or "rebuild this from scratch following the spec above".)_
