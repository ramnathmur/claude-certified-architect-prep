# Reusable Prompt — Generating "Extension" (Level-Up) Material for a Course

**Version:** 1.0 (2026-06-05) · **Project:** Claude Certified Architect Prep
**What it does:** Turns a shipped, faithfully-replicated Academy course into one or more **extension HTML lessons** that take a learner from course-level → architect-level for the CCA-F exam. Validated on two pilots: `orchestration-patterns.html` (extends Subagents) and `tool-use-agent-loop.html` (extends Claude 101).
**When to use:** Any time we add "next-degree-of-learning" material on top of an existing base course in this project.

> This is the EXTENSION pipeline. It differs from the base-course capture pipeline (`Academy-Course-to-HTML_Prompt_v1.md`) in one critical way: base courses are grounded ONLY in the captured Academy source; **extensions are researched from the web and grounded in cited, reputable sources (Anthropic docs first).** Every extension claim must trace to its citations file, and enrichment must be visibly labeled as such.

---

# CONTEXT

I'm preparing for the Claude Certified Architect — Foundations (CCA-F) exam. I have base course HTML files (faithful Academy replications) and I want linked "extension" files that deepen each one into architect-level knowledge — more mechanism, worked examples, patterns, and exam-relevant depth.

Project root: `C:\Claude Cowork\Projects\Claude Certified Architect Prep\`
Persona library (real, 13 personas): `C:\Claude Cowork\Projects\AI agents personas\` (use `AI-Agents-Personas_Overview_v1.html` as the index)
Learning style + rules: `C:\Claude Cowork\About Me\`
Exam domains + weights: `PREP-MATERIAL-INDEX.md`
Reference quality bar (approved): the base course HTML and the two shipped pilots in `courses/*/extensions/`.

# GOAL

For a given **base course** and a **named extension topic**, produce one self-contained, interactive, source-grounded extension HTML lesson, QA-gated, cross-linked into a basics→advanced ladder. Run the full pipeline below; ship only when both QA gates PASS.

# THE PIPELINE (run in order)

### Step 1 — Designate the researcher
Use the live **`web-researcher` agent** to do the searching, **embodying the Senior Research Analyst persona** (the persona-library Research Analyst is a conceptual role with no web access; the web-researcher agent is the actual tool). One researcher per extension topic.

### Step 2 — Build the citations source-of-truth file (the grounding artifact)
Dispatch the web-researcher to produce a DEEP, citation-grounded notes file — the analog of the base course's capture file, and the thing Gate 1 diffs against.
- **Prioritize Anthropic primary sources** (docs at `platform.claude.com` / `code.claude.com`, `anthropic.com/engineering`, Academy), then reputable engineering writing.
- Extract substantive content: verbatim definitions (quoted + attributed), real numbers, code/JSON shapes, when-to-use guidance — not just a topic list.
- **Every substantive claim carries an inline `(source: URL)`.** No fabrication. Mark uncertain or version-sensitive facts `[VERIFY]`. Never invent or reproduce proprietary CCA-F exam questions.
- Note which CCA-F domain(s) each section reinforces.
- **Note:** the `web-researcher` agent may lack a Write tool — if so, it returns the full notes in its message and the orchestrator writes the file.
- Save to: `courses/<base-course>/extensions/source/<slug>_citations.md` (with a manifest: date, sources list, domains; and a `[VERIFY]` list at the end).

### Step 3 — Build the extension HTML (persona build team)
Dispatch ONE build agent embodying **Senior Tech Writer + Senior Frontend Engineer + Domain Translator + AI Professor** (AI Professor mandatory — extensions are architect-depth). Inputs: the citations file (ONLY source of facts) + the base course HTML (quality bar / design language to match). Requirements:
- **Grounding:** every substantive claim traces to the citations file; preserve its `[VERIFY]` flags as visible inline notes; author analogies allowed ONLY if clearly labeled "analogy, not a product fact."
- **Extension labeling:** prominent banner "Extension — beyond the Academy course" + one-line note that it's researched material (cite the sources), plus a compact "Sources" section near the end listing the citation URLs.
- **Cross-linking:** "← Back to the base course" link near the top (`../<base-course>.html`) + a note on which base lesson it builds on; a "What's next" pointer to the next extension in the ladder (link it even if not built yet, and say so).
- **Self-contained:** inline CSS/JS/SVG only — no CDNs, no external images/fonts. Opens offline. Code/JSON in proper `<pre><code>` (no HTML-escaping breakage).
- **Interactivity (match the base course):** sticky section nav + scroll-spy + progress bar; inline MCQs with reveal + source-grounded explanations; ≥1 end-of-lesson quiz with scoring (denominator = actual question count, no off-by-one); predict-before-reveal blocks; collapsible callouts that are keyboard-operable (role=button, tabindex=0, Enter/Space, aria-expanded); MCQ feedback with `aria-live`.
- **SVG illustrations:** ≥5 inline SVG/CSS diagrams of the key concepts (no raster, no external images).
- **Pedagogy (Ram's style):** why-before-how, real-world analogies, predict-before-reveal, Andrew-Ng tone; weight quizzes toward the extension's CCA-F domain(s); keep architect depth — never dumb down.
- **Format:** long-form SCROLLABLE document, NOT a slide deck. Never invoke `/frontend-slides`.
- Output: `courses/<base-course>/extensions/<slug>.html`.

### Step 4 — Two QA gates (independent reviewers, never the producer), in parallel
- **Gate 1 — Content fidelity (AI Professor + Senior Research Analyst):** coverage (every citations section present), correctness (numbers/quotes/code exact vs citations), traceability/anti-hallucination (every HTML claim traces to the citations file; no distractor presented as true; MCQ answer keys source-grounded), and `[VERIFY]`-preservation. Report → `courses/<base-course>/extensions/qa/gate1-<slug>.md`.
- **Gate 2 — Build & usability (Senior QA Lead + AI Student):** self-contained (no external deps), JS logic sound (scoring denominators, in-range `data-correct`, nav/scroll-spy, reveals, collapsibles, mobile menu), code blocks render, cross-links + banner + Sources present, usability, and no-dilution vs citations. Report → `courses/<base-course>/extensions/qa/gate2-<slug>.md`.
- **PASS bar:** 0 blockers, 0 majors. On FAIL: log defects → revise → re-run that gate only (max 2 cycles, then escalate to Ram).

### Step 5 — Close valuable minors, then ship
Fix cheap high-value minors directly (e.g., diagram-count labels, aria-live, keyboard a11y). Leave features/cosmetic/forward-404 minors logged. Then:
- Update `courses/COURSE-ROADMAP.md` (status ✅ Shipped + gate results).
- **Wire it into the Launchpad dashboard (REQUIRED, same session).** Edit `Launchpad.html`'s `DATA` array: flip the card's `status:'queued'`→`'live'` and add its relative `href` (or add a new card object). Steps in `Launchpad-DESIGN-NOTES.md` §5. The dashboard is the front door and must never lag behind shipped content. Re-run dashboard Gate 2 if the change is non-trivial.
- Open the file in Chrome via the OS (`Start-Process chrome <path>`) — the Chrome MCP `navigate` mangles `file://` URLs, so use the OS launch.

# CONSTRAINTS (non-negotiable)
- Extensions are researched, not invented: cite reputable sources, Anthropic-first; label enrichment vs. official course content; flag version-sensitive facts `[VERIFY]`.
- Self-contained HTML only (inline CSS/JS/SVG, no CDNs/external images). Scrollable document, never a deck.
- Reviewers are independent of the producer; never let an agent grade its own output.
- Don't create files beyond: the citations file, the extension HTML, and the two QA reports.
- Don't start any graded certificate quiz on Academy.

# OUTPUT FORMAT (per extension)
1. `extensions/source/<slug>_citations.md` — cited source-of-truth.
2. `extensions/<slug>.html` — the lesson.
3. `extensions/qa/gate1-<slug>.md` + `extensions/qa/gate2-<slug>.md`.
4. Updated `COURSE-ROADMAP.md` row + a one-paragraph readout to Ram (gate results, any [VERIFY] flags, what's next).

# FOLDER LAYOUT
```
courses/<base-course>/
  <base-course>.html                  ← base (faithful Academy replication)
  extensions/
    source/<slug>_citations.md        ← cited source-of-truth (Gate-1 diffs against this)
    <slug>.html                       ← the extension lesson
    qa/gate1-<slug>.md  gate2-<slug>.md
```

# TONE / STYLE
- Lead with the deliverable. State assumptions; flag tradeoffs.
- Inside the HTML: Andrew-Ng pedagogy — why-before-how, analogies, predict-before-reveal, encouraging but rigorous.
- Be honest about [VERIFY] facts and forward links that don't resolve yet.

---

## Worked precedent (the two pilots — copy this shape)
- **S-E1 Orchestration Patterns** (extends Subagents): citations from Building Effective Agents + Multi-Agent Research System + Agent SDK docs → 108 KB HTML, 11 SVGs, 23 MCQs → G1 PASS (0/0/2), G2 PASS (0/0/3).
- **C-E1 Tool-Use Agent Loop** (extends Claude 101): citations from platform.claude.com tool-use docs + Building Effective Agents → 99 KB HTML, 5 SVGs, 19 MCQs → G1 PASS (0/0/0), G2 PASS (0/0/3).

## Remaining queued extensions (full set) — apply this prompt to each
C-E2 Context Management & Reliability · C-E3 MCP at a Builder Level · C-E4 Prompt Caching Economics · C-E5 Prompt Engineering Depth + Model Selection (optional) · S-E2 Subagents as a Programmable Primitive (SDK) · S-E3 Orchestrator-Worker at Scale + Failure Modes. Topic briefs + source pointers are in `courses/EXTENSION-RECOMMENDATION.md`.
