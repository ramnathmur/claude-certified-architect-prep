# Gate 2 — Build & Usability QA: `mcp-at-a-builder-level.html`

**Verdict: PASS**

**Blockers: 0 / Majors: 0 / Minors: 3**

Reviewer: Senior QA Lead + AI Student (independent — did not build this file).
Method: full read of all 1416 lines (HTML/CSS/JS) plus targeted grep verification of dependencies, escaping, `data-correct` ranges, quiz denominators, and link targets.

---

## Check-by-check results

### 1. Self-contained — PASS
No external asset dependencies. Grep for `https?://`, `cdn`, `@import`, `<link>`, `<script src>`, external fonts returned only **content** references:
- Sources section anchors (lines 1250–1257) — citation links, allowed.
- Example URLs *inside* code blocks / prose (`https://example.com/mcp` L693, `https://mcp.notion.com/mcp` L1005) — content, not loaded assets.

There is **no** `<link>`, no `<script src>`, no `@import`, no `url()` asset, no web font. Font stack is system-only (`-apple-system,BlinkMacSystemFont,"Segoe UI"…`, L22). All CSS is one inline `<style>` (L7–175); all JS is one inline `<script>` (L1274–1413); all 8 diagrams are inline `<svg>`. **Loads fully offline.**

### 2. JS logic soundness — PASS

**Quiz scoring — denominator is dynamic and correct.** `updateQuiz()` (L1395–1411) computes `var total=mcqs.length` from `quiz.querySelectorAll('.mcq[data-inquiz]')` — no hardcoded total. Verified counts: Quiz A has 4 `data-inquiz` MCQs (L531/536/541/546) and its static label reads `0 / 4` (L529); Final has 10 (L1185–1230) labelled `0 / 10` (L1182). Static labels match the dynamic counts, and the result box only shows when `answered.length===total` (L1402). No off-by-one. `pct=score/total*100` is sound.

**Every `data-correct` is in range.** All 24 MCQs carry exactly 4 `.opt` buttons; all `data-correct` values are 0–3 (grep: 0,1,2,3 only). Spot-checked answer↔text mapping on several (S1=2 "standardizes exchange, not reasoning" ✓; S5=1 "stdio" for the local-subprocess question ✓; Quiz-A Q3=0 "M-A-U" ✓; Q1=2 ✓). 0-based indexing matches the click handler `(i===correct)` (L1375). No off-by-one.

**Section nav + scroll-spy — all targets exist.** TOC is built from the `sections` array (L1278–1290) producing links to `#l1…#l10` and `#sources`. Every one of those IDs exists as a `section.lesson` (`id="l1"…"l10"`, and `id="sources" data-lesson` at L1244). Scroll-spy (`onScroll`, L1309–1330) queries `section.lesson` and matches `el.id` against `nav a[data-target=...]` — no dangling target. (The `sec1…sec10` divider IDs are not referenced by the spy; harmless.)

**Progress bar — wired and live.** `#progressBar` width updated from scroll ratio (L1314); `onScroll` bound to `scroll` (passive) and `resize` and called once on load (L1331–1333). Lesson-completion `%` recomputed from `doneCount/TOTAL` where `TOTAL=navOrder.length` (L1303, explicitly commented "dynamic denominator — no off-by-one"). Correct.

**MCQ reveal — per-question state, no global leak.** Each `.mcq` gets its own closure with a local `var answered=false` (L1371); `opts`, `fb`, `msg` are all scoped per-MCQ inside the `forEach` (L1365–1391). Clicking locks that MCQ only, disables its own options, marks its own correct/wrong, reveals its own `.fb`. No shared/global state. Predict-reveal (`doReveal`, L1357) is also self-scoped via `btn.parentElement`.

**Collapsible callouts — fully keyboard-operable.** L1347–1354 sets `role="button"`, `tabindex="0"`, initial `aria-expanded`, and a `keydown` handler for Enter / Space / Spacebar with `preventDefault`. `toggleCall` (L1343) toggles `aria-expanded` in sync with the `collapsed` class. Click handler also present (inline `onclick` on each `.chead`). Meets the bar.

**MCQ feedback uses `aria-live`.** Every `.fb` carries `aria-live="polite"` (e.g. L308, 400, 514…), and feedback text is injected into that same `.fb` element via `innerHTML` (L1383) — the live region is the mutated node, so SR announcement fires correctly.

### 3. Code blocks render — PASS (this is the #1 known failure mode; checked carefully)
All angle-bracket placeholders inside code blocks are **escaped**:
- L696: `MCP-Protocol-Version: &lt;protocol-version&gt;` ✓
- L1008: `claude mcp add --transport sse &lt;name&gt; &lt;url&gt;` ✓

Grep for raw `<name>`, `<url>`, `<protocol-version>`, `<command>`, `<server-name>`, `<path>`, `<your…>` → **no matches**. The six `<pre><code>` JSON/shell blocks (L797, 810, 827, 902, 909, 1004) contain only braces, quotes, `#` comments, and a `\` line-continuation — no unescaped `<`/`>`. Nothing is silently deleted.

### 4. Cross-links + banner + Sources — PASS
- **Extension banner** present: "Extension — beyond the Academy course" (L211–216) plus sidebar badge "Extension · beyond the Academy course" (L188).
- **Back to base course:** `← Back to the base course (Claude 101)` → `../claude-101.html` (L189) — target file confirmed to exist.
- **C-E1 link:** `tool-use-agent-loop.html` linked twice in the crosslink (L219) — target exists.
- **C-E2 link:** footer also links `context-management-reliability.html` (L1267) — target exists (bonus, reference sibling).
- **Forward link (C-E4):** `prompt-caching-economics.html` (L1240, L1267) — file does **not** exist on disk, and the lesson explicitly flags it: "that file is **not built yet** — this forward link may 404 until it lands" (L1240). Correctly marked.
- **Sources section** present (L1243–1263): an ordered list of 8 official citation URLs plus a preserved `[VERIFY]` flag manifest.

### 5. Usability / a11y — PASS
- Heading hierarchy sane: one `h1` (hero), `h2` per section divider, `h3` lesson title, `h4`/`h5` subsections. No skips that break semantics.
- Sticky sidebar is a separate flex column (`aside` L27–31), `main` is the sibling flex child — no overlap with content; on ≤980px the sidebar becomes an off-canvas drawer (L167–174).
- Mobile menu works: `toggleNav` (L1336) toggles `.open` on sidebar + scrim, syncs `aria-expanded` on the button; nav links auto-close the drawer on click below 980px (L1298). Scrim click closes (L180).
- Tab order reasonable (DOM order: menu button → sidebar links → main content → quiz buttons). All interactive elements are real `<button>`/`<a>` (quiz options are `<button class="opt">`), so the whole quiz is keyboard-operable.
- `.sr-only` utility defined and used for screen-reader text; SVGs carry `role="img"` + `aria-label`.

### 6. No-dilution — PASS
Architect-level depth is intact and not contradicted:
- Real JSON-RPC `initialize` request/response/notification with capability semantics (L795–828).
- The testable nuances are kept precise: one-client-per-server incl. the "two connections to one remote server = two clients" trap (L380–381); HTTP+SSE deprecation nuance "SSE survives *inside* Streamable HTTP" (L702–704); roots are SHOULD-not-MUST advisory (L605–606); connector is product-limited (remote-only, tool-calls-only) vs protocol-limited distinction (L988–996, L1032).
- Version-sensitive facts carry inline `⚠ VERIFY` flags and a consolidated VERIFY manifest (L1261). No oversimplification, no internal contradiction detected.

---

## Findings by severity

### Blockers (0)
None.

### Majors (0)
None.

### Minors (3)

**m1 — Scroll-spy "completion" can mark a section done before it's truly read (cosmetic).**
`onScroll` (L1319): `if(el.offsetTop<=scrollTop+window.innerHeight*0.6){seen[el.id]=true;}` marks a lesson "done" as soon as its *top* passes 60% of the viewport — a fast scroll past flips it to ✓ and inflates the progress %. Purely cosmetic (no scoring impact).
*Fix:* gate completion on the section **bottom** clearing the fold, e.g. `if(el.offsetTop + el.offsetHeight <= scrollTop + window.innerHeight){seen[el.id]=true;}`.

**m2 — `.fbmsg` payload is `hidden` but not `aria-hidden`; minor SR redundancy.**
Each MCQ stores its explanation in a `<div class="fbmsg" hidden>` (e.g. L309) and copies it into the live `.fb` on answer. The `hidden` attribute removes it from the a11y tree, so this is fine in practice — but if any future style override unsets `hidden`, the same text would exist twice for SR users.
*Fix (defensive):* add `aria-hidden="true"` alongside `hidden` on each `.fbmsg`. Optional.

**m3 — Sources URLs differ from the in-body "(source: …)" short labels.**
In-body citations use short paths like `modelcontextprotocol.io/architecture` and `code.claude.com/mcp` (e.g. L292, L704), while the Sources list uses the canonical full paths (`/docs/learn/architecture`, `code.claude.com/docs/en/mcp`, L1251/1257). Not wrong — the Sources list is authoritative — but a reader cross-referencing the short label won't find a verbatim match.
*Fix:* optionally align the in-body short labels to the Sources slugs, or add a one-line note that short labels map to the numbered Sources list. Cosmetic.

---

**Readout:** Self-contained, all 24 MCQs in-range with a dynamic `mcqs.length` denominator, every code-block angle bracket escaped, all internal links resolve (forward C-E4 correctly flagged not-built) — ships as a PASS with only 3 cosmetic minors.
