# Stage A Plan — Academy Course → Interactive HTML Pipeline

**Status:** Awaiting Ram's approval before Stage B (Claude 101 build)
**Created:** 2026-06-04
**Source prompt:** `C:\Claude Cowork\Projects\prompts\Academy-Course-to-HTML_Prompt_v1.md`

---

## 1. Content Acquisition + Gating Dependency

**The gating dependency:** nothing downstream works until each course's full content is captured faithfully from the Skilljar web UI. This is the single highest-risk step.

**Method:**
- Capture runs through **Ram's authenticated browser session** via the Chrome MCP (`mcp__Claude_in_Chrome__*`). Ram is logged into Anthropic Academy via Infosys / Claude Partner Network access, so auth is assumed handled.
- For each course: navigate lesson-by-lesson, extract full page text (`get_page_text` / `read_page`), capture any code blocks verbatim, and note any images/diagrams (with their alt text / captions).
- **Video lessons** are the known weak point: Skilljar courses often embed video. Where a lesson is video-only, we capture the transcript/captions if available; if neither exists, that lesson is flagged `SOURCE-GAP` in the capture file rather than reconstructed from memory (anti-hallucination rule).

**Fallback if Chrome capture fails:** Ram manually copies lesson content into a per-course source file. Pipeline does not proceed on a course until its source file is complete.

---

## 2. Source-of-Truth Capture Format

Every course gets a raw capture file BEFORE any HTML is built. All later steps trace back to it.

```
courses/<course-slug>/source/<course-slug>_source.md
```

Format inside:
- One `## Lesson N — <title>` heading per lesson, in course order
- Verbatim body text, code blocks fenced, diagrams described with caption + alt text
- `SOURCE-GAP` markers where content could not be captured (video w/o transcript, etc.)
- A capture manifest at top: total lessons, captured count, gap count, capture date

This file is the **ground truth** the QA Gate 1 diffs against. The HTML can never contain a claim absent from this file.

---

## 3. Persona Selection (from the real 13-persona library)

The library at `C:\Claude Cowork\Projects\AI agents personas\` ships 13 personas across 5 families. Six map directly onto this pipeline. Assignment scales with course difficulty.

| Pipeline role | Persona | Family | Why |
|---|---|---|---|
| **Converter** (faithful content → HTML structure) | Senior Tech Writer | Generation | Renders source into clean, complete, well-structured prose + headings without losing fidelity |
| **Interactivity / UX** (nav, quizzes, MCQs, SVG illustrations, emojis) | Senior Frontend Engineer | Generation | Builds the self-contained interactive HTML, vanilla JS, SVG/CSS visuals |
| **Pedagogy layer** (analogies, why-before-how, no dumbing-down) | Domain Translator | Analysis | Adds real-world analogies and intuition WITHOUT simplifying away depth |
| **Conceptual-depth layer** (200-level only) | AI Professor | Critique | For harder courses, ensures technical concepts are explained at architect depth, not surface |
| **QA Gate 1 — content fidelity** | AI Professor + Senior Research Analyst | Critique + Research | Professor checks correctness; Research Analyst checks traceability (every claim → source line) |
| **QA Gate 2 — build & usability** | Senior QA Lead + AI Student | Critique + Critique | QA Lead checks the HTML is well-built/works; AI Student checks a learner can actually follow it |

**Difficulty-based scaling:**
- **Beginner (e.g. Claude 101):** Converter (Tech Writer) + Interactivity (Frontend Engineer) + Pedagogy (Domain Translator). QA both gates.
- **Intermediate / Advanced (200-level):** add **AI Professor** into the conversion itself (not just QA) for conceptual depth.

No new personas need to be invented — the library covers every role.

---

## 4. Subagent Task Map

Each task is an independent subagent with a clean handoff. Reviewers are independent of producers (never grade own output).

| # | Task | Subagent (persona) | Input | Output → handoff |
|---|---|---|---|---|
| 1 | **Capture** | Research Analyst + Chrome MCP | Course URL | `source/<slug>_source.md` → Task 2 |
| 2 | **Convert** | Senior Tech Writer | Source file | Structured HTML content draft → Task 3 |
| 3 | **Enrich** | Senior Frontend Engineer + Domain Translator | Content draft | Interactive HTML (nav, MCQs, quizzes, SVG, emojis) → Gates |
| 4 | **QA Gate 1** | AI Professor + Research Analyst | HTML + source file | `qa/gate1.md` (coverage/correctness/traceability) |
| 5 | **QA Gate 2** | Senior QA Lead + AI Student | HTML | `qa/gate2.md` (build/usability/no-dilution) |
| 6 | **Revise** | Frontend Engineer / Tech Writer (as defect dictates) | Gate failures | Revised HTML → re-run failed gate |

---

## 5. Two-Gate QA Loop

**Gate 1 — Content fidelity & correctness** (pass = all three clear):
- **Coverage:** section-by-section diff HTML vs source. Any missing lesson/concept/code = FAIL.
- **Correctness:** any distortion vs source = FAIL.
- **Traceability:** any HTML claim NOT in source = FAIL (hallucination).

**Gate 2 — Build quality & usability** (pass = all three clear):
- **Build:** HTML well-formed, nav works, quizzes/MCQs function, opens with no server/CDN.
- **Usability:** an AI-Student-persona learner can follow it end to end.
- **No-dilution:** interactivity did NOT reduce coverage or depth vs Gate-1-passed content.

**Failure handling:** log specific defects → revise → re-run that gate only. **Max 2 revision cycles per gate**, then escalate to Ram (mirrors the persona library's own 2-cycle rule). A course ships only when both gates pass. Both QA reports surface to Ram.

---

## 6. Candidate Course Set (NEEDS RAM'S CONFIRMATION)

Per the prompt's scope rule, the default is the **CCA-F-relevant set**, not all 13 Academy courses. From research, the exam-relevant tier is the **Partner Network Learning Path** (4 focused courses) plus the foundational **Claude 101**. Proposed roadmap:

| Order | Course | Tier | Status |
|---|---|---|---|
| 1 | **Claude 101** (foundations) | Beginner | ⬜ Build first |
| 2 | Claude with the API | 100/200 | ⬜ Pending confirm |
| 3 | Model Context Protocol (MCP) | 200 | ⬜ Pending confirm |
| 4 | Claude Code in Action | 200 | ⬜ Pending confirm |
| 5 | Agents / Agent SDK | 200 | ⬜ Pending confirm |

> **Exact course titles + the full list will be confirmed by live capture in Stage B.** This table is the proposed *scope*, not the verified catalog. Ram confirms: CCA-F subset (above) or all 13 Academy courses?

---

## 7. Folder Layout

```
Claude Certified Architect Prep/
  courses/
    claude-101/
      source/  claude-101_source.md
      claude-101.html
      qa/  gate1.md  gate2.md
  COURSE-ROADMAP.md         (master status tracker, generated after scope confirm)
```

Quizzes/MCQs in each course tie back to the 5 CCA-F exam domains; weak spots Ram reveals get logged to the existing `GAPS.md` so course prep and curriculum prep stay unified.

---

## 8. What I Need From Ram to Start Stage B

1. **Scope confirm:** CCA-F subset (5 courses above) or all 13?
2. **Chrome connection:** confirm the Chrome extension is connected and you're logged into Academy, so capture can run.

On approval, Stage B builds **Claude 101 only**, runs both gates, and shows you the HTML + both QA reports before any other course.
```
