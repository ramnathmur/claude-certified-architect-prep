# mcq-practice — Project Instructions

> **⚠️ STATUS: SPEC ONLY — NOT BUILT (as of 2026-06-26).** This folder contains the requirements + this instruction file + `index.html`, but the application (`mcq_launcher.py`, `prompt_builder.py`, `html_renderer.py`, `text_renderer.py`, `templates/`, `sessions/`) does **not** exist yet. Until implemented, this generator is **NOT** part of the exam-readiness path — do not count it toward mocks or Go/No-Go. The academy delivery system (`academy/`) does not depend on it.

**Purpose:** Reusable MCQ practice application for the CCA-F (Claude Certified Architect — Foundations) exam.  
**Requirements doc:** `The Requirements for Anthropic Exam MCQ Prep.md` — this is the source of truth. Read it before implementing or modifying anything.

---

## What this application does

Generates a fresh set of MCQ questions each run by invoking Claude Code in headless mode, then renders the output as an interactive HTML file or plain text. No question bank is stored. Every session is new.

The user configures four options at CLI launch: scope (full exam or per domain), difficulty (Anthropic-Grade or Prep Range), session size (N questions or duration), and output format (HTML or plain text).

---

## File map

| File | Role |
|---|---|
| `mcq_launcher.py` | Entry point. Collects config, orchestrates build/call/render pipeline. |
| `prompt_builder.py` | Assembles the Claude generation prompt from config + curriculum + stems log. |
| `html_renderer.py` | Parses question JSON, merges with `templates/session_template.html` via Jinja2. |
| `text_renderer.py` | Parses question JSON, formats as plain text (no template engine). |
| `templates/session_template.html` | Jinja2 scaffold — all CSS and JS inline, no external dependencies. |
| `sessions/stems_log.txt` | Running log of question stem prefixes for deduplication across runs. |
| `sessions/session_*.{html,txt}` | Generated session output files — never overwrite, never delete. |
| `README.md` | User-facing launch instructions. |

---

## Critical paths and constraints

### CURRICULUM.md path
The prompt builder reads the curriculum from the **parent project directory**, not from this folder:
```
C:\Claude Cowork\Projects\Claude Certified Architect Prep\CURRICULUM.md
```
Never hardcode a relative path. If the file is missing, exit with the absolute path in the error message.

### No external API key
The application calls Claude Code CLI in headless mode (`claude -p "..." --output-format text`). No `ANTHROPIC_API_KEY`. No `anthropic` Python SDK. The user's Claude Max plan covers this.

### No external CDN in HTML output
The generated HTML must be fully self-contained and work offline. Never reference an external URL in `session_template.html`. All CSS and JS are inlined.

### Never overwrite session files
Session filenames include a timestamp. Never write to an existing path. Never delete any file in `sessions/`.

---

## Domain weightages (used in prompt_builder.py)

| # | Domain | Weight |
|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% |
| 2 | Tool Design & MCP Integration | 18% |
| 3 | Claude Code Configuration & Workflows | 20% |
| 4 | Prompt Engineering & Structured Output | 20% |
| 5 | Context Management & Reliability | 15% |

Rounding rule: nearest integer; total must equal N exactly; remainder goes to Domain 1.

---

## Question type distribution

| Type | Anthropic-Grade | Prep Range |
|---|---|---|
| Scenario-based | 40% | 20% |
| Anti-pattern recognition | 25% | 20% |
| Concept + application | 25% | 30% |
| Definition / recall | 10% | 30% |

Enforce these as exact counts in the prompt, not as vague instructions.

---

## Key design rules (non-negotiable)

**Code fence stripping is deterministic, not a retry condition.**
Claude frequently wraps JSON in ` ```json ... ``` `. Strip fences before parsing: if the response starts with ` ``` `, remove the first and last fence lines. Only trigger retry logic if the result after stripping is still invalid JSON.

**Deduplication via stems log, not timestamps.**
A timestamp in the prompt does not prevent repeated questions — Claude has no cross-run memory. The stems log (`sessions/stems_log.txt`) is the real deduplication mechanism. At runtime, inject the last 50 stems as "do not generate questions beginning with any of these." After generation, append new stems to the log (first 12 words per stem).

**Chunking for large sessions.**
Any request for N > 30 questions is split into two calls of `ceil(N/2)` each. Results are merged and shuffled before rendering. This is transparent to the user.

**Plain text: answers at end, no tracking.**
Plain text sessions show all questions first, then answers + explanations in a separate block at the end. No score tracking, no weakest-domain analysis. Add a footer note directing the user to HTML mode for interactive scoring.

**HTML: fully interactive, offline.**
On answer submission: lock the selection, show green/red feedback with ✅/❌ symbols (never color alone), display wrong-answer explanation. Persistent score tracker at top. Final summary page with domain breakdown and weakest domain flagged.

---

## Python dependencies

| Package | Use |
|---|---|
| `jinja2` | HTML rendering only |
| Standard library | Everything else (`subprocess`, `json`, `pathlib`, `datetime`, `sys`) |

Do not introduce additional third-party packages without explicit approval.

---

## Session filename format

```
session_YYYYMMDD_HHMMSS_<scope>_<difficulty>_<N>q.<ext>
```

Examples:
- `session_20260606_053000_full_anthro_40q.html`
- `session_20260606_054500_d3_prep_20q.txt`

Scope codes: `full` / `d1` through `d5`. Difficulty codes: `anthro` / `prep`.

---

## Error handling rules

| Condition | Required behaviour |
|---|---|
| `claude` not in PATH | Print absolute path diagnostic, exit cleanly |
| Code fences in output | Strip deterministically — not a retry |
| Invalid JSON after stripping | Retry once with schema reminder. On second failure, write `sessions/diagnostic_YYYYMMDD_HHMMSS.txt` and exit |
| N > 30 | Chunk into two calls — not an error |
| N > 60 | Cap at 60, print warning |
| Duration < 5 min | Enforce 5 questions minimum, print note |
| `CURRICULUM.md` missing | Print absolute path, exit — do not proceed without curriculum context |
| `stems_log.txt` missing | Create empty, continue — expected on first run |

---

## What NOT to do

- Do not add a static question bank or hardcoded questions at any point.
- Do not store any session data outside `sessions/`.
- Do not modify `CURRICULUM.md` or any file in the parent project directory.
- Do not introduce a database, SQLite, or any persistent store beyond `stems_log.txt` and the session files.
- Do not call the Anthropic API directly — only via the `claude` CLI.
- Do not load external fonts, scripts, or stylesheets in the HTML template.
- Do not rewrite or simplify the deduplication mechanism without updating this CLAUDE.md and the requirements doc.

---

## Exam scenario vocabulary (use in scenario-based question stems)

The CCA-F exam draws 4 of these **6** scenarios per sitting (per the official exam guide). Scenario-based questions should reference these by name to familiarise Ram with the exact exam vocabulary:

1. Customer Support Resolution Agent
2. Code Generation with Claude Code
3. Multi-Agent Research System
4. Developer Productivity with Claude
5. Claude Code for Continuous Integration
6. Structured Data Extraction

---

## v2 features (do not build now, do not foreclose architecturally)

- Cross-session progress tracking (aggregate scores across all sessions by domain)
- Mixed-difficulty mode (Anthropic-Grade for weak domains, Prep Range for strong ones)
- Per-Academy-module scope (current scope is per exam domain)
