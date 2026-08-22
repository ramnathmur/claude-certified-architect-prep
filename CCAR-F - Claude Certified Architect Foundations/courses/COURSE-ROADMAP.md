# Course Conversion Roadmap

**Pipeline:** `prompts/Academy-Course-to-HTML_Prompt_v1.md` · **Plan:** `COURSE-CONVERSION-PLAN.md`
**Scope (current):** Claude 101 only (Ram's decision 2026-06-04). Remaining courses pending a scope decision after reviewing the Claude 101 output.

**Landing page:** `Launchpad.html` (project root) — single dashboard that launches all course + extension files. Built by Claude Design from `prompts/`-vetted spec; installed & QA'd 2026-06-05. Gate 2 PASS (0 blk / 0 maj after a11y fix / minors). Companions: `Launchpad-DESIGN-NOTES.md`, `Launchpad-WRAPPER-PROMPT.md`, `Launchpad-QA-gate2.md`. To add a card when a queued extension ships: flip `status:'queued'`→`'live'` + add `href` in the `DATA` array (see design notes §5).

| Order | Course | Difficulty | Status | Gate 1 | Gate 2 |
|---|---|---|---|---|---|
| 1 | **Claude 101** | Beginner | ✅ Shipped | PASS (0 blk/0 maj/3 min) | PASS (0 blk/0 maj/4 min) |
| 2 | **Introduction to subagents** | 200 | ✅ Shipped | PASS (0 blk/0 maj/0 min) | PASS (0 blk/0 maj/4 min) |
| 3 | Introduction to agent skills | 200 | ⬜ Next | — | — |
| — | Introduction to Model Context Protocol | 200 | ⬜ Queued | — | — |
| — | Building with the Claude API | 100/200 | ⬜ Queued | — | — |
| — | Claude Code in Action | 200 | ⬜ Queued | — | — |

## Extension files (level-up material — researched, source-cited, cross-linked)

Two-stage plan in `EXTENSION-RECOMMENDATION.md`. Decision: both pilots first → full 8-file set. Extensions follow a stricter grounding rule — each has a `extensions/source/<slug>_citations.md` notes file that Gate 1 diffs against.

| # | Extension | Base course | Domain | Status | Gate 1 | Gate 2 |
|---|---|---|---|---|---|---|
| S-E1 | The Five Orchestration Patterns | Subagents | D1 (27%) | ✅ Shipped (pilot) | PASS (0/0/2) | PASS (0/0/3) |
| C-E1 | The Tool-Use Agent Loop | Claude 101 | D2 (18%)+D1 | ✅ Shipped (pilot) | PASS (0/0/0) | PASS (0/0/3) |
| C-E2 | Context Management & Reliability | Claude 101 | D5 (15%) | ✅ Shipped | PASS (0/0/3) | PASS (0/0/2) |
| C-E3 | MCP at a Builder Level | Claude 101 | D2 (18%) | ✅ Shipped | PASS (0/0/3) | PASS (0/0/3) |
| C-E4 | Prompt Caching Economics | Claude 101 | D5 (15%) | ✅ Shipped | PASS (0/0/3) | PASS (0/0/2) |
| C-E5 | Prompt Engineering Depth + Model Selection | Claude 101 | D4 (20%) | ✅ Shipped | PASS (0/0/3) | PASS (0/0/1) |
| S-E2 | Subagents as a Programmable Primitive (SDK) | Subagents | D1+D3 | ✅ Shipped | PASS (0/0/3) | PASS (0/0/3) |
| S-E3 | Orchestrator-Worker at Scale + Failure Modes | Subagents | D1+D5 | ✅ Shipped | PASS (0/0/2) | PASS (0/0/3) |

**Pilot artifacts:**
- `courses/introduction-to-subagents/extensions/orchestration-patterns.html` (~108 KB, 11 SVGs, 23 MCQs) + `source/orchestration-patterns_citations.md` + `qa/gate1-…`, `qa/gate2-…`
- `courses/claude-101/extensions/tool-use-agent-loop.html` (~99 KB, 5 SVGs, 19 MCQs) + `source/tool-use-agent-loop_citations.md` + `qa/gate1-…`, `qa/gate2-…`

> Note: forward "what's next" links in the pilots point to not-yet-built files (resolve as the queued set ships).

## Introduction to Subagents — artifacts
- HTML: `courses/introduction-to-subagents/introduction-to-subagents.html` (~94 KB, self-contained, 4 lessons, 8 SVGs)
- Source of truth: `courses/introduction-to-subagents/source/introduction-to-subagents_source.md` (4/4 lessons, 0 gaps)
- QA Gate 1: `courses/introduction-to-subagents/qa/gate1.md` · QA Gate 2: `courses/introduction-to-subagents/qa/gate2.md`
- **CCA-F mapping:** Domain 1 Agentic Architecture & Orchestration (27%) — subagent delegation, context/session management, multi-agent orchestration, anti-patterns; Domain 3 Claude Code Config (20%) — `/agents` command, config files, scope.
- Post-QA fixes applied: diagram-count label 7→8; `aria-live` on MCQ feedback. Logged minors left: quiz retry-on-reload (feature), final-check nav scroll-spy highlight (cosmetic).

## Claude 101 — artifacts
- HTML: `courses/claude-101/claude-101.html` (~141 KB, self-contained, 14 lessons)
- Source of truth: `courses/claude-101/source/claude-101_source.md` (14 lessons captured)
- QA Gate 1 (content fidelity): `courses/claude-101/qa/gate1.md`
- QA Gate 2 (build/usability): `courses/claude-101/qa/gate2.md`

## CCA-F domain mapping (Claude 101 → exam domains)
Claude 101 is foundational/product-level (claude.ai usage). It primarily reinforces:
- **Context Management** (15%) — context window, 1M tokens, RAG in Projects, Memory
- **Tool Design & MCP** (18%) — Connectors, MCP as "USB-C for AI", Enterprise Search
- **Prompt Engineering** (20%) — prompt anatomy, iteration, evals, 4D framework
- **Agentic Architecture** (27%) — Research mode (agentic multi-step), Cowork subagents, Claude Code
- **Claude Code Config** (20%) — Claude Code / Cowork / Code modes (Ask/Code/Plan)

> Deeper architect-level coverage comes from the 200-level courses. Claude 101 builds the vocabulary the exam assumes.
