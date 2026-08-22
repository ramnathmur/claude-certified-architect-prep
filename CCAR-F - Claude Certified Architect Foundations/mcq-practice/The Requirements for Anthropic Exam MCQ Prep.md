# The Requirements for Anthropic Exam MCQ Prep

**Project:** Claude Certified Architect — Foundations (CCA-F)  
**Author:** Ram  
**Created:** 2026-06-06  
**Status:** Requirements — v1.1 (post-self-evaluation fixes applied 2026-06-06)

---

## 1. Executive Summary

This application generates fresh, AI-authored multiple-choice questions (MCQs) for the Anthropic Claude Certified Architect — Foundations (CCA-F) exam. Every session produces a new question set — no static bank is ever reused. The learner configures four parameters at launch (scope, difficulty, session size, output format), and the application delivers either an interactive scored HTML file or a plain-text question list, ready to use immediately.

The application lives entirely within this project folder (`mcq-practice/`) and requires no external API key. It runs through Claude Code and the Claude Max plan the user already holds.

**Why this exists:** The CCA-F exam is 60 scenario-weighted MCQs in 120 minutes. Passing requires fluency with anti-patterns, not just definitions. Static practice sets get stale after one use. Fresh generation means every session tests genuine recall, not pattern-matched memory.

---

## 2. Exam Domain Coverage

### 2.1 Official Domain Weightages

| # | Domain | Exam Weight | MCQ share per 60 Qs | MCQ share per 40 Qs | MCQ share per 20 Qs |
|---|---|---|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% | ~16 questions | ~11 questions | ~5 questions |
| 2 | Tool Design & MCP Integration | 18% | ~11 questions | ~7 questions | ~4 questions |
| 3 | Claude Code Configuration & Workflows | 20% | ~12 questions | ~8 questions | ~4 questions |
| 4 | Prompt Engineering & Structured Output | 20% | ~12 questions | ~8 questions | ~4 questions |
| 5 | Context Management & Reliability | 15% | ~9 questions | ~6 questions | ~3 questions |

Rounding rule: always round domain counts to the nearest integer; total must equal the requested N exactly. In case of rounding conflict, assign the remainder to Domain 1 (highest weight).

### 2.2 Per-Chapter Mode

When the learner selects "Per Chapter," they pick a single domain and receive the full requested question count from that domain alone. No cross-domain distribution applies.

### 2.3 Exam Question Characteristics (from research)

The CCA-F exam uses the following MCQ styles — the application must weight generation accordingly:

| Question Type | Share (approx.) | Description |
|---|---|---|
| Scenario-based | ~40% | "An architect built X. What is wrong / right / the next step?" |
| Anti-pattern recognition | ~25% | "Which of the following is an anti-pattern for Y?" |
| Concept + application | ~25% | "When should you use X over Y? Select the correct criteria." |
| Definition / recall | ~10% | "What does X stand for / return / require?" |

> **Scoring note from PREP-MATERIAL-INDEX.md:** Production-scenario questions and anti-pattern questions carry higher scaled weight than recall questions. The generator must reflect this mix, not default to definition-heavy output.

### 2.4 Exam Format Reference

| Parameter | Value | Source |
|---|---|---|
| Total questions | 60 | Multiple third-party sources |
| Time limit | 120 minutes | Multiple third-party sources (unconfirmed by Anthropic directly) |
| Passing score | 720 / 1000 (scaled) | Anthropic / Skilljar |
| Answer format | Single correct answer per question | Official |
| Exam delivery | Proctored online, no tools | Official |
| Scenarios per sitting | 4 drawn randomly from a pool of 6 | Official exam guide |

---

## 3. Application Architecture

### 3.1 High-Level Design

```
mcq_launcher.py
    ↓
[Config interview — 4 questions to user via CLI]
    ↓
[Prompt builder — constructs the MCQ generation prompt from config]
    ↓
[Claude generator — invokes Claude Code in headless mode]
    ↓
[Output renderer — formats questions as HTML or plain text]
    ↓
sessions/
  └── session_YYYYMMDD_HHMMSS.[html|txt]
```

Three components:

1. **Config Collector** — CLI prompts to the user at launch. Four decisions collected before any question generation begins. No question generation starts until all four are answered.

2. **Prompt Builder** — Takes the four config values and constructs a detailed generation prompt. The prompt instructs Claude on: domain distribution, question type mix, difficulty calibration, and output schema. This is the layer that ensures freshness — different random seeds (via timestamp + domain rotation) produce different questions each run.

3. **Output Renderer** — Takes Claude's raw output and either:
   - Renders an interactive HTML file (full scoring, tracking, explanations), or
   - Writes a formatted plain-text file (print-ready)

### 3.2 Runtime Dependency

The launcher calls Claude Code in headless/print mode:
```
claude -p "<generated prompt>" --output-format text
```

No `ANTHROPIC_API_KEY` is required. The user's Claude Max subscription covers this. If Claude Code is not in PATH, the launcher prints a diagnostic and exits cleanly.

**Code fence handling:** Claude frequently wraps JSON output in markdown code fences (` ```json ... ``` `). The launcher must strip these deterministically before passing output to the renderer — this is not treated as an error condition to retry, but as a routine normalisation step. The stripping rule: if the response starts with ` ``` `, remove the first and last fence lines before parsing. If after stripping the result is still not valid JSON, then the retry logic in Section 6.5 applies.

**Token limit risk:** A 60-question Anthropic-Grade session (2–4 sentence stems + 4 options + 2–4 sentence explanations) can exceed 10,000 output tokens. To stay within Claude's practical output limits, the prompt builder chunks large sessions: any request for N > 30 questions is split into two calls of ceil(N/2) each, results merged, then shuffled before rendering. This is transparent to the user.

### 3.3 Output Storage

All sessions are written to `mcq-practice/sessions/`. File naming:

```
session_YYYYMMDD_HHMMSS_<scope>_<difficulty>_<N>q.[html|txt]
```

Example: `session_20260606_053000_full_anthro_40q.html`

Sessions are never overwritten. Old sessions accumulate and can be reviewed to track improvement over time.

> **v1 scope note:** Per-session score tracking is the sole tracking mechanism in this version. Cross-session progress (e.g., "Domain 3 has been weak across 4 sessions") is a v2 feature. The session file naming convention is chosen to support future aggregation: a v2 summary tool can read all `session_*.html` files in `sessions/` and parse scores from their metadata headers.

---

## 4. User-Facing Options

All four options are collected at launch via numbered CLI prompts before any generation begins.

### 4.1 Option 1 — Scope

```
[1] Full Exam    — all 5 domains, proportional to official weightages
[2] Per Chapter  — questions from one domain only (you choose which)
```

If "Per Chapter" is selected, a follow-up prompt lists the 5 domains by name and number.

> **Mapping decision:** The user's original brief referenced *"individual chapter that is covered by Anthropic's official web page on this course."* This is mapped here to the 5 official CCA-F exam domains, which are the primary organisational unit on the Anthropic exam page and drive the official weightages. The Anthropic Academy has a separate course/module structure (Claude 101, Introduction to Subagents, and their extensions) — this structure does not map 1:1 to the 5 exam domains. If per-Academy-module selection is preferred over per-exam-domain selection, this section should be revised and the chapter list updated to match the Academy course menu.

### 4.2 Option 2 — Difficulty Level

```
[A] Anthropic-Grade  — exam-level difficulty; 40% scenario-based, 25% anti-pattern, 25% application, 10% recall
[B] Prep Range       — learning-mode difficulty; 20% scenario-based, 20% anti-pattern, 30% application, 30% recall
```

**Anthropic-Grade** questions: distractors are plausible, not obviously wrong. Scenario stems are 2–4 sentences. Anti-pattern options require architectural reasoning to eliminate.

**Prep Range** questions: shorter stems, clearer distractors, recall-friendly. Good for first pass through a new domain.

### 4.3 Option 3 — Session Size

```
[N] Number of Questions  — enter a number (5–60)
[T] Duration             — enter minutes (5–120); app converts to question count at exam pace of 2 min/question
```

Duration-to-count conversion: `N = floor(minutes / 2)`. Minimum enforced: 5 questions. Maximum enforced: 60 questions.

### 4.4 Option 4 — Output Format

```
[H] HTML file  — interactive, scored, with per-question explanations on submission
[P] Plain text — formatted for printing or reading; no interactivity
```

Plain text is also useful for pasting into a document or using as a study card set. See Section 5.6 for the plain text output format specification.

---

## 5. HTML Output Specification

### 5.1 File Structure

Each HTML file is fully self-contained — one file, no external dependencies, no internet required. Styles and scripts are inlined.

### 5.2 Layout

```
┌─────────────────────────────────────────────────────┐
│  CCA-F Practice Session                              │
│  Scope: Full Exam · Difficulty: Anthropic-Grade      │
│  40 Questions · Generated: 2026-06-06 05:30          │
│  Score: 0 / 40 correct                              │
├─────────────────────────────────────────────────────┤
│  Q1 of 40 · Domain: Agentic Architecture            │
│                                                      │
│  [Scenario or question stem — 1-4 sentences]         │
│                                                      │
│  ○ A. [Option text]                                  │
│  ○ B. [Option text]                                  │
│  ○ C. [Option text]                                  │
│  ○ D. [Option text]                                  │
│                                                      │
│  [Submit Answer]                                     │
├─────────────────────────────────────────────────────┤
│  [← Previous]                    [Next →]           │
└─────────────────────────────────────────────────────┘
```

### 5.3 Answer Handling

- **On submit:** The selected option is locked. No changes permitted after submission.
- **Correct answer:** Selected option turns green. A one-sentence confirmation is shown.
- **Wrong answer:** Selected option turns red. The correct answer turns green. An explanation section appears (2–4 sentences) explaining WHY the correct answer is right and WHY the submitted answer is wrong. The explanation is generated at the same time as the question — it is baked into the HTML, not fetched live.

### 5.4 Score Tracker

- Displayed persistently at the top of every question.
- Format: `Score: X / N correct (Y%)` — updates immediately after each submission.
- Domain sub-scores shown in a collapsible panel at the top: one row per domain, showing X/N for that domain.

### 5.5 Final Summary Page

Shown automatically after the last question is submitted.

```
┌─────────────────────────────────────────────────────┐
│  Session Complete                                    │
│  Total Score: 32 / 40 (80%)                         │
│                                                      │
│  Domain Breakdown:                                   │
│  ✅ Agentic Architecture:      9/11  (82%)           │
│  ✅ Claude Code:               7/8   (88%)           │
│  ⚠️  Prompt Engineering:       5/8   (63%)  ← WEAKEST│
│  ✅ Tool Design & MCP:         7/7   (100%)          │
│  ✅ Context Management:        4/6   (67%)           │
│                                                      │
│  Weakest domain: Prompt Engineering & Structured    │
│  Output. Review modules/module-3.md and retry.      │
│                                                      │
│  [Review Wrong Answers]  [Start New Session]        │
└─────────────────────────────────────────────────────┘
```

"Review Wrong Answers" scrolls to a list of all incorrectly answered questions, each with the explanation visible.

"Start New Session" links to the launcher instructions (since a new session requires re-running `mcq_launcher.py`).

### 5.6 Plain Text Output Specification

When the user selects `[P] Plain text`, the renderer writes a `.txt` file to `sessions/` using this format:

```
CCA-F Practice Session
Scope: Full Exam  |  Difficulty: Anthropic-Grade  |  20 Questions
Generated: 2026-06-06 05:30
─────────────────────────────────────────────────────

Q1 [Domain: Agentic Architecture & Orchestration]
An architect is building a multi-agent research system...

  A. Option text
  B. Option text
  C. Option text
  D. Option text

─────────────────────────────────────────────────────

Q2 [Domain: Claude Code Configuration & Workflows]
...
```

**Answers and explanations** appear in a separate block at the end of the file, after all questions. This preserves the ability to study questions without accidentally seeing answers:

```
─────────────────────────────────────────────────────
ANSWERS & EXPLANATIONS
─────────────────────────────────────────────────────

Q1 — Correct answer: B
B is correct because... A is wrong because...

Q2 — Correct answer: D
...
```

**No tracking in plain text mode.** The plain text file is static — there is no right/wrong tracking, score calculation, or weakest-domain identification. These features are HTML-only. If the user selects plain text, the final score summary is omitted and a note is added to the file footer: `"To get interactive scoring and per-question explanations, re-run with HTML output."`

### 5.7 Accessibility

- All answer choices use `<input type="radio">` with visible labels (not icon-only).
- Color is never the only indicator — correct/wrong answers also get a ✅ / ❌ symbol.
- Font size minimum: 16px body text.

---

## 6. Technical Implementation Plan

### 6.1 File Structure

```
mcq-practice/
├── The Requirements for Anthropic Exam MCQ Prep.md   ← this file
├── mcq_launcher.py                                   ← main entry point (CLI config + orchestration)
├── prompt_builder.py                                 ← assembles the generation prompt from config
├── html_renderer.py                                  ← converts parsed question list to HTML (Jinja2)
├── text_renderer.py                                  ← converts parsed question list to plain text
├── templates/
│   └── session_template.html                        ← Jinja2 HTML scaffold (inline CSS/JS)
├── sessions/
│   ├── stems_log.txt                                ← running log of generated question stems (deduplication)
│   └── session_YYYYMMDD_HHMMSS_*.{html,txt}        ← generated sessions
└── README.md                                         ← how to launch
```

**Renderer technology:** `html_renderer.py` uses [Jinja2](https://jinja.palletsprojects.com/) to merge the parsed question list into `session_template.html`. The template contains all inline CSS and JavaScript — no external dependencies. `text_renderer.py` uses plain Python string formatting; no template engine required.

### 6.2 Launch Method

```bash
cd "C:\Claude Cowork\Projects\Claude Certified Architect Prep\mcq-practice"
python mcq_launcher.py
```

The launcher runs in the terminal, collects options, calls Claude Code headlessly, writes the output file, and prints the path to the generated file. Total time from launch to usable session: under 90 seconds.

### 6.3 Fresh Question Generation

The generator prompt is assembled by `prompt_builder.py` and contains four components:

**Component 1 — Curriculum context (injected at runtime)**
The full domain curriculum is read from:
```
C:\Claude Cowork\Projects\Claude Certified Architect Prep\CURRICULUM.md
```
The relevant module section for the requested domain(s) is extracted and included in the prompt. This grounds questions in the actual study material rather than Claude's general knowledge.

**Component 2 — Deduplication via stems log**
`sessions/stems_log.txt` stores the first 12 words of every question stem generated across all sessions. At runtime, the last 50 stems from this log are injected into the prompt as a "do not repeat" list. After generation, the new stems are appended to the log. This is the real mechanism for freshness — a timestamp alone does not prevent repetition because Claude has no memory across runs.

**Component 3 — Output schema (enforced in the prompt)**
Claude is instructed to return a raw JSON array with no markdown fences, no preamble, and no postamble. The prompt ends with: `Return ONLY a valid JSON array. Do not wrap it in code fences. Do not add any text before or after the array.`

**Component 4 — Question type distribution**
The prompt specifies exact counts per question type based on the difficulty setting from Section 4.2.

**Prompt skeleton (Anthropic-Grade, Full Exam, 20 questions):**

```
You are generating CCA-F exam practice questions.

DOMAIN DISTRIBUTION:
- Agentic Architecture & Orchestration: 5 questions
- Claude Code Configuration & Workflows: 4 questions
- Prompt Engineering & Structured Output: 4 questions
- Tool Design & MCP Integration: 4 questions
- Context Management & Reliability: 3 questions

QUESTION TYPE MIX (Anthropic-Grade):
- Scenario-based: 8 questions (40%)
- Anti-pattern recognition: 5 questions (25%)
- Concept + application: 5 questions (25%)
- Definition / recall: 2 questions (10%)

CURRICULUM REFERENCE:
{extracted CURRICULUM.md sections for all domains}

DO NOT REPEAT these question stems:
{last 50 stems from stems_log.txt}

DISTRACTOR QUALITY (Anthropic-Grade):
- All four answer options must be plausible to a developer who has studied the domain
- Wrong answers must be wrong for a specific architectural reason, not obviously absurd
- Scenario stems are 2–4 sentences describing a real system design decision

OUTPUT FORMAT:
Return ONLY a valid JSON array. Do not wrap it in code fences. Do not add any text before or after the array.
Each element: {"domain": "...", "domain_num": N, "question_type": "...", "stem": "...", "options": {"A": "...", "B": "...", "C": "...", "D": "..."}, "correct_answer": "X", "explanation": "X is correct because... [wrong answer] is wrong because..."}
```

### 6.4 Question Object Schema

```json
{
  "domain": "Agentic Architecture & Orchestration",
  "domain_num": 1,
  "question_type": "scenario | anti-pattern | application | recall",
  "stem": "Full question text here...",
  "options": {
    "A": "Option A text",
    "B": "Option B text",
    "C": "Option C text",
    "D": "Option D text"
  },
  "correct_answer": "B",
  "explanation": "B is correct because... A is wrong because..."
}
```

The renderer reads this JSON and outputs the HTML. The JSON is not shown to the user — only the rendered questions are visible.

### 6.5 Error Handling

| Error condition | Behaviour |
|---|---|
| Claude Code not in PATH | Print: "Claude Code not found. Ensure `claude` is installed and in your PATH." — exit. |
| Claude output wrapped in code fences | Strip fences deterministically before parsing (not a retry condition). Rule: if response starts with ` ``` `, remove first and last fence lines, then parse. |
| Claude returns malformed JSON after fence stripping | Retry once with an explicit schema reminder appended to the prompt: "Your previous response was not valid JSON. Return ONLY a raw JSON array, nothing else." If second attempt fails, write `sessions/diagnostic_YYYYMMDD_HHMMSS.txt` with the raw response and exit with a message. |
| N > 30 questions | Split into two calls of ceil(N/2) each. Merge results and shuffle before rendering. Transparent to user. |
| Requested N > 60 | Cap at 60 with a warning printed to the terminal. |
| Duration < 5 minutes entered | Enforce minimum 5 questions; print: "Minimum session is 5 questions (10 minutes)." |
| `CURRICULUM.md` not found at expected path | Print the expected absolute path and exit. Do not silently proceed with no curriculum context. |
| `stems_log.txt` missing | Create it empty and proceed. First session has no deduplication history — this is expected. |

---

## 7. Success Criteria

The application is working correctly when all of the following are true:

1. **Fresh questions every run.** Running `mcq_launcher.py` twice in a row with identical settings produces two distinct question sets (no question stem is repeated verbatim).

2. **Correct domain distribution.** For a 40-question full-exam run, domain counts are within ±1 of the proportional target (11/8/8/7/6).

3. **Question type mix respected.** In an Anthropic-Grade run of 20 questions, at least 7 are scenario-based and at least 4 are anti-pattern (±1 tolerance).

4. **Score tracking is accurate.** Submitting all correct answers yields 100%. Submitting all wrong answers yields 0%.

5. **Wrong-answer explanations appear.** Every incorrectly submitted answer shows an explanation before the learner moves to the next question.

6. **Final summary identifies weakest domain.** The summary page correctly computes per-domain percentage and labels the lowest-scoring domain.

7. **HTML file is self-contained.** Opening the generated HTML file in a browser with no internet connection works fully — all interactivity functions offline.

8. **Sessions are preserved.** Re-running the launcher does not overwrite or delete prior session files.

9. **Duration mode converts correctly.** Selecting 30 minutes yields exactly 15 questions.

10. **Per-Chapter mode scopes correctly.** Selecting "Domain 4 — Prompt Engineering" yields zero questions from any other domain.

---

## Appendix A — Exam Scenario Reference

The CCA-F exam draws 4 of these **6** scenarios per sitting (per the official exam guide). MCQ questions reference these scenarios in their stems.

| # | Scenario | Primary Domains |
|---|---|---|
| 1 | Customer Support Resolution Agent | D1 + D5 |
| 2 | Code Generation with Claude Code | D3 |
| 3 | Multi-Agent Research System | D1 + D2 |
| 4 | Developer Productivity with Claude | D2 |
| 5 | Claude Code for Continuous Integration | D3 + D4 |
| 6 | Structured Data Extraction | D4 |

The generator should reference these scenario names in scenario-based questions where appropriate — this familiarises the learner with the exact scenario vocabulary that will appear on the real exam.

---

## Appendix B — Anti-Pattern Reference (Top Patterns by Domain)

These anti-patterns appear frequently in exam questions. The generator should draw on these when producing anti-pattern recognition questions.

| Domain | Key Anti-Patterns |
|---|---|
| D1 — Agentic Architecture | Orchestrator calling tools directly for work (not just coordination); infinite loop from missing stop condition; hallucinated tool outputs silently accepted |
| D2 — Tool Design & MCP | One mega-tool that does everything; credentials in tool descriptions; SSE chosen for local single-process workload |
| D3 — Claude Code | CLAUDE.md at wrong scope level; plan mode required but not enforced; Bash used as first resort instead of last |
| D4 — Prompt Engineering | Malformed JSON silently swallowed (no validation loop); all few-shot examples are edge cases; schema has no `additionalProperties: false` |
| D5 — Context Management | Compaction that loses the original user intent; `cache_control` placed mid-conversation instead of at stable prefix; no token budget enforcement in production |
