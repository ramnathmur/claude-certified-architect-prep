# Resume Prompt — CCA-F Academy-to-HTML Pipeline (Desktop App)
_Generated: 2026-06-05 · For: Claude Code Desktop (has credential access)_

---

## YOUR TASK

You are resuming a multi-session project: converting Anthropic Academy courses into rich, self-contained interactive HTML study files for Ram's **Claude Certified Architect — Foundations (CCA-F)** exam prep.

**Claude 101 is already done and approved.** Your job this session is to build the next course: **Agents / Agent SDK** (specifically the two agent-related courses found on the Academy: "Introduction to agent skills" and "Introduction to subagents"). Start with whichever one is more directly exam-relevant to CCA-F (see Domain Map below), or confirm with Ram before starting if unsure which to prioritize.

---

## PROJECT LOCATION

All project files live at:
```
C:\Claude Cowork\Projects\Claude Certified Architect Prep\
```

Key files to read before starting:
- `CLAUDE.md` — project brief and operating rules
- `COURSE-CONVERSION-PLAN.md` — the full pipeline spec (read this carefully)
- `courses/COURSE-ROADMAP.md` — master status tracker
- `courses/claude-101/claude-101.html` — the approved reference output (match this quality)
- `courses/claude-101/qa/gate1.md` and `gate2.md` — what a passing QA gate looks like

---

## WHAT'S ALREADY DONE

| Item | Status |
|---|---|
| Project scaffolded (CLAUDE.md, CURRICULUM.md, GAPS.md, ROADMAP.md) | ✅ Done |
| Pipeline spec finalized (`COURSE-CONVERSION-PLAN.md`) | ✅ Done |
| Claude 101 captured (14 lessons) | ✅ Done |
| Claude 101 HTML built, QA Gate 1 + Gate 2 PASS, shipped | ✅ Done |
| Agents / Agent SDK — capture | ⬜ Your job |
| Agents / Agent SDK — HTML build | ⬜ Your job |
| Agents / Agent SDK — QA Gate 1 + Gate 2 | ⬜ Your job |

---

## THE PIPELINE (follow this exactly)

### Step 0 — Read the spec
Read `COURSE-CONVERSION-PLAN.md` in full before doing anything else. It contains the full pipeline, persona assignments, QA gate rules, and folder layout.

### Step 1 — Course identification
Navigate to **https://anthropic.skilljar.com** (log in using Ram's credentials — you have access). Find the Agents course(s). The Academy homepage showed these two agent-related courses as of 2026-06-05:
- **"Introduction to agent skills"** — about building/configuring Skills in Claude Code
- **"Introduction to subagents"** — about sub-agents in Claude Code for context delegation

Confirm which one maps to the CCA-F "Agentic Architecture & Orchestration" domain (27% weight). If both are relevant, plan to build both — one at a time. Start with the higher-weight one.

**Important:** You may need to register (free) for the course to unlock lessons. Do so. Do NOT click "Start" on the graded certificate quiz lesson — that consumes a real attempt.

### Step 2 — Capture (ground truth file)
Capture the full course lesson-by-lesson via the browser. For each lesson:
- Navigate to the lesson page
- Extract the full page text
- Record verbatim body text, code blocks (fenced), any diagrams (alt text + caption)
- For video-only lessons with no transcript: mark `SOURCE-GAP`

Write the capture to:
```
courses/<course-slug>/source/<course-slug>_source.md
```

Format: one `## Lesson N — <title>` per lesson, capture manifest at top (total/captured/gap counts + capture date). This is the ground truth all QA diffs against.

**Gotchas from the previous session:**
- `get_page_text` on Skilljar sometimes returns only the privacy banner — use `read_page` or take a snapshot to get real content
- Lesson IDs are non-sequential; pull links from the sidebar as you progress
- Screenshots via Chrome MCP can time out; text extraction is more reliable
- The sidebar reveals lesson links only as you advance through the course

### Step 3 — HTML build (3 subagents working together)

Dispatch these three personas as subagents (persona library is at `C:\Claude Cowork\Projects\AI agents personas\`):

| Persona | Role |
|---|---|
| **Senior Tech Writer** | Converts source → clean, complete, well-structured HTML content draft |
| **Senior Frontend Engineer** | Builds the self-contained interactive HTML (nav, MCQs, quizzes, SVG illustrations, vanilla JS, inline CSS) |
| **Domain Translator** | Adds real-world analogies and pedagogy WITHOUT dumbing down |
| **AI Professor** | Required for 200-level courses — adds architect-depth technical explanations |

Since both agent courses are 200-level, **include the AI Professor** in the build team.

**HTML requirements (non-negotiable, match claude-101.html):**
- 100% self-contained: inline CSS, inline JS, inline SVG — zero CDN, zero external images
- Navigation sidebar with lesson links
- Quiz widgets (MCQs with reveal, not graded)
- SVG illustrations for key architecture concepts
- Scrollable long-form document — do NOT make it a slide deck
- All quiz MCQs must be grounded in the source file (no hallucinated questions)

Output to: `courses/<course-slug>/<course-slug>.html`

### Step 4 — QA Gate 1: Content fidelity

Run as two independent subagents:

**AI Professor** — checks:
- Every key concept from the source is present in the HTML
- No technical distortions or inaccuracies
- Depth is preserved (200-level concepts not flattened)

**Senior Research Analyst** — checks:
- Every HTML claim traces back to a line in the source file
- No lessons missing from the HTML
- No hallucinated content

Write combined findings to: `courses/<course-slug>/qa/gate1.md`

Gate 1 PASS requires: 0 blockers, 0 majors. Minors are logged but don't block.
Gate 1 FAIL: log specific defects → fix → re-run Gate 1 (max 2 cycles).

### Step 5 — QA Gate 2: Build quality and usability

Run as two independent subagents:

**Senior QA Lead** — checks:
- HTML is well-formed and opens without a server
- Navigation works (lesson links jump correctly)
- All quiz widgets function (reveal answers, no JS errors)
- No broken SVGs or layout issues

**AI Student** — checks:
- A learner can follow the course end-to-end
- Analogies and explanations are clear and correct
- No coverage loss vs Gate-1-passed content (interactivity didn't dilute depth)

Write combined findings to: `courses/<course-slug>/qa/gate2.md`

Gate 2 PASS requires: 0 blockers, 0 majors. Minors are logged but don't block.
Gate 2 FAIL: log specific defects → fix → re-run Gate 2 (max 2 cycles).

### Step 6 — Ship
Only after BOTH gates pass:
1. Confirm the HTML opens correctly in browser
2. Update `courses/COURSE-ROADMAP.md` with status ✅ Shipped + Gate results
3. Update `resume-prompt.md` with what's done and what's next

---

## FOLDER LAYOUT

```
Claude Certified Architect Prep/
  courses/
    claude-101/                          ← reference (already shipped)
      source/claude-101_source.md
      claude-101.html
      qa/gate1.md  gate2.md
    <new-course-slug>/                   ← your output goes here
      source/<slug>_source.md
      <slug>.html
      qa/gate1.md  gate2.md
  COURSE-ROADMAP.md
  COURSE-CONVERSION-PLAN.md
  CLAUDE.md
```

Use a clean kebab-case slug for the course folder (e.g., `intro-to-agent-skills`, `intro-to-subagents`).

---

## CCA-F DOMAIN MAP (for MCQ grounding)

Tie quiz questions to the exam domains they reinforce:

| # | Domain | Weight |
|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% |
| 2 | Tool Design & MCP Integration | 18% |
| 3 | Claude Code Configuration & Workflows | 20% |
| 4 | Prompt Engineering & Structured Output | 20% |
| 5 | Context Management & Reliability | 15% |

The agent courses primarily hit Domain 1 (27%) and Domain 3 (20%). Weight your MCQs accordingly.

---

## OPERATING RULES (from project CLAUDE.md)

- Never summarise when you can quiz — end each section with a question
- Challenge any incorrect mental models immediately with the right one
- Every factual claim about Claude must be grounded in the captured source (not hallucinated)
- Course HTML = long-form scrollable document — NEVER invoke `/frontend-slides`
- Self-contained HTML only — no CDNs, no external images
- Do NOT start the graded certificate quiz lesson

---

## QUALITY BAR

Reference `courses/claude-101/claude-101.html` — that is the approved quality standard. The build must match or exceed it on:
- Visual polish and SVG illustrations
- Quiz widget interactivity
- Navigation usability
- Content depth and accuracy

Both QA gate reports (`gate1.md`, `gate2.md`) must surface to Ram before the course is declared shipped.

---

## WHEN YOU'RE DONE

Update `resume-prompt.md` (the main handoff file at the project root) with:
- What was built and shipped
- Gate results
- What's next in the roadmap

The roadmap order after the agent course(s) is:
1. ✅ Claude 101 (shipped)
2. ⬜ Agents course(s) ← you are here
3. ⬜ Introduction to Model Context Protocol
4. ⬜ Building with the Claude API
5. ⬜ Claude Code in Action
