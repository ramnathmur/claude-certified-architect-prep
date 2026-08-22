# Landing-Page / Dashboard — Evaluation & Recommendation

**Status:** Evaluation only (no build yet — awaiting Ram's pick).
**Created:** 2026-06-05
**Goal:** One opening dashboard that cleanly presents every base course + extension and launches each individual HTML file in the browser.

---

## 1. What it must launch (current files)

```
courses/
  claude-101/claude-101.html                                  ← Base · Claude 101 (14 lessons)
  claude-101/extensions/tool-use-agent-loop.html              ← Ext C-E1 · Tool-Use Agent Loop
  introduction-to-subagents/introduction-to-subagents.html    ← Base · Introduction to Subagents (4 lessons)
  introduction-to-subagents/extensions/orchestration-patterns.html ← Ext S-E1 · Orchestration Patterns
```
Plus 6 queued extensions (C-E2…C-E5, S-E2, S-E3) — the dashboard must be **trivial to extend** as each ships.

---

## 2. The one real constraint: how the dashboard opens local files

These are `file://` pages opened from disk (no server). That shapes the options:

- A plain `<a href="claude-101/claude-101.html">` link **works natively** from a local file — clicking navigates the browser to the course. This is the simplest, most robust path and needs zero server.
- JavaScript `window.open()` / `fetch()` of local files is **blocked or flaky** under the `file://` origin (browser security). So the dashboard should rely on plain relative `<a>` links, not JS-driven navigation.
- Therefore: **place the dashboard at the project root** (`Launchpad.html` beside the `courses/` folder, or inside `courses/`) and link with relative paths. Opening it = `Start-Process chrome <path>` (same OS-launch method we use for the lessons, since the Chrome MCP mangles `file://`).

**Recommendation on placement:** put it at `courses/index.html` (links become `claude-101/claude-101.html`, etc.) OR project-root `Launchpad.html` (links become `courses/claude-101/...`). Root placement is slightly friendlier to find; either works.

---

## 3. Three design options

| Option | What it is | Pros | Cons | Effort |
|---|---|---|---|---|
| **A — Static link index** | A clean single HTML page: title, short intro, a card/list per course with its extensions nested, each a relative `<a>` link. No JS needed. | Dead simple, can't break, instant to extend (add a link), fully offline | No progress tracking, no search | Low |
| **B — Self-contained dashboard (RECOMMENDED)** | Option A's polish + the project's design language (matches the lessons): course cards grouped by base→extensions, CCA-F domain tags + weights, status badges (Shipped/Queued), a learning-ladder view, and **localStorage-based "visited/done" ticks** + overall progress bar. All inline CSS/JS/SVG, links are plain `<a>`. | Looks like one product with the lessons; shows the basics→advanced ladder; light progress tracking that works on `file://` (localStorage is allowed); still no server | A bit more build; localStorage is per-browser-profile only | Medium |
| **C — App-like SPA** | A router/searchable single-page app with filters, tags, fuzzy search, maybe iframe previews. | Most powerful at scale (dozens of files) | Overkill for ~10 files; iframe of `file://` can be blocked; more JS surface to QA; fragile offline | High |

---

## 4. Recommendation

**Build Option B — a self-contained "Launchpad" dashboard.** Rationale:
- It matches the course/extension visual language so the whole prep feels like one product (your "land cleanly on an opening dashboard" goal).
- Plain relative `<a>` links are the only reliable launch mechanism from `file://` — B keeps those and adds polish *around* them, avoiding the JS-navigation pitfalls of C.
- It makes the **basics → advanced ladder** visible (base course → its extensions), which is exactly the progression you asked for earlier.
- `localStorage` progress ticks work fine under `file://` and need no server — a real usability win without fragility.
- Adding a newly-shipped extension = adding one card entry. Future-proof for the queued 6.

Skip C unless the library grows past ~25 files. A is the fallback if you want it in 10 minutes with zero JS.

---

## 5. Proposed contents of the Launchpad (Option B)

- **Header:** title ("CCA-F Study Launchpad"), one-line purpose, overall progress bar (localStorage), exam snapshot (60 Q / 120 min / 720 pass).
- **Suggested path strip:** the basics→advanced ladder as an ordered rail (Claude 101 → its extensions → Subagents → its extensions).
- **Course sections (one per base course):** a base-course card (title, lesson count, CCA-F domains it reinforces, "Launch" link) with its **extension cards nested beneath** (topic, domain + weight tag, Shipped/Queued badge, "Launch" link; queued ones disabled/greyed).
- **Per-card:** a "mark complete" checkbox (localStorage) feeding the progress bar; a domain-weight chip; an "Extension — beyond Academy" badge on extension cards.
- **Footer:** links to the trackers (`COURSE-ROADMAP.md`, `EXTENSION-RECOMMENDATION.md`), and a note that it's a local offline dashboard.
- **Self-contained:** inline CSS/JS/SVG, no CDNs; relative `<a>` links only; long-form scrollable (not a deck).
- **QA:** run the same Gate 2 (build/usability — QA Lead + AI Student) before declaring done; Gate 1 (content fidelity) is light here since the dashboard has little prose, but verify every link path resolves to a real file.

---

## 6. Open questions for Ram (before building)
1. **Option A, B, or C?** (Recommend B.)
2. **Placement:** project-root `Launchpad.html`, or `courses/index.html`?
3. **Build now, or after the remaining 6 extensions ship?** (Dashboard is easiest to finalize once all cards exist, but a B version now — with queued cards greyed — also works and gives you a hub immediately.)
