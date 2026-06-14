# CCA-F Training Curriculum — AI-First Learning Course

**Version:** 1.0  
**Created:** 2026-06-04  
**Target exam:** Claude Certified Architect — Foundations (CCA-F)  
**Methodology:** AI-first, active learning — see `CLAUDE.md` for full principles  
**Estimated total time:** 20–25 hours across 8 modules

---

## How This Course Works

Every module follows the same four-act structure — no exceptions:

1. **Orient** — Big picture first. Why does this domain exist? What problem does it solve? What would break without it?
2. **Explain** — Why before how. Mental model before API. Pattern name before implementation.
3. **Build** — A hands-on mini-exercise tied to one of the six exam scenarios. You write it; Claude coaches.
4. **Test** — 5 active-recall questions per module. No hints. Score recorded in `GAPS.md`.

Progress through modules in order. Domain 1 (Agentic Architecture) is the spine — every other domain references it.

---

## Module Map

| # | Module | Domain | Exam Weight | Est. Time | Status |
|---|---|---|---|---|---|
| 0 | Foundations & Exam Orientation | Cross-domain | — | 1h | ⬜ |
| 1 | Agentic Architecture & Orchestration | Domain 1 | 27% | 5h | ⬜ |
| 2 | Claude Code Configuration & Workflows | Domain 2 | 20% | 4h | ⬜ |
| 3 | Prompt Engineering & Structured Output | Domain 3 | 20% | 4h | ⬜ |
| 4 | Tool Design & MCP Integration | Domain 4 | 18% | 4h | ⬜ |
| 5 | Context Management & Reliability | Domain 5 | 15% | 3h | ⬜ |
| 6 | Scenario Simulation Lab | All domains | — | 3h | ⬜ |
| 7 | Mock Exam + Gap Review | All domains | — | 2h | ⬜ |

---

## Module 0 — Foundations & Exam Orientation

**Goal:** Understand what the exam is actually testing. Build the mental model for the whole course before touching any domain.

### Learning Objectives
- Explain the difference between a Claude API call, an agent, and a multi-agent system — in one sentence each
- Name the 5 exam domains, their weights, and why the weights are what they are
- Describe what "architect-level" thinking means versus developer-level thinking
- Understand exam scoring: why scenario and anti-pattern questions carry more weight

### Key Concepts
- The three Claude primitives: Messages API, Tool Use, Streaming
- What an agent loop is at the conceptual level
- Claude's role as an orchestrator vs. subagent vs. tool executor
- The difference between "using Claude" and "architecting with Claude"

### Session Exercise
Map the 6 exam scenarios to the 5 domains. For each scenario, predict: which domain is primary? Which is secondary? What would a bad architect do in this scenario?

### Module 0 Quiz (5 questions — active recall, no hints)
1. What is the passing score for CCA-F, and why does a scaled score matter more than raw percentage?
2. Which domain carries the highest exam weight, and why does it make sense that it does?
3. Name three differences between an agent and a simple API call.
4. What are the 6 exam scenarios? Name them from memory.
5. A client asks you to build "Claude-powered search." Is that AI-First by design? What clarifying questions would you ask before architecting it?

---

## Module 1 — Agentic Architecture & Orchestration

**Domain weight: 27% — the heaviest domain. Prioritise depth here.**

### Learning Objectives
- Draw the observe-think-act-respond cycle from memory and explain each phase
- Distinguish orchestrator agents from subagents — roles, boundaries, failure modes
- Design a multi-agent system for a given scenario (Scenario 3: Multi-Agent Research System)
- Identify the three most common agentic anti-patterns and explain why each fails
- Explain session management: what state to persist, what to discard, and where

### Key Concepts
| Concept | What to understand |
|---|---|
| Agent loop anatomy | `stop_reason` values: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence` — what each means architecturally |
| Orchestrator pattern | One agent coordinates; subagents execute. Orchestrator never calls tools directly for work — only for coordination |
| Subagent delegation | When to delegate: task isolation, parallelism, specialisation. When not to: simple sequential steps |
| Tool result injection | How tool results re-enter the conversation loop. Why tool results are not "responses" |
| Session management | Conversation history design: what to keep, what to summarise, what to discard |
| Failure modes | Infinite loops, runaway tool calls, context overflow, hallucinated tool outputs |
| Multi-agent handoff | How context is passed between agents. Stateless handoff vs. stateful continuation |

### Exam Scenarios Covered
- **Scenario 1:** Customer Support Resolution Agent — escalation logic, first-contact resolution
- **Scenario 3:** Multi-Agent Research System — coordinator/subagent architecture

### Session Exercise
Design a multi-agent research system on paper:
- A coordinator agent receives a research question
- It delegates to three specialist subagents (web search, document analysis, synthesis)
- Results flow back and the coordinator produces a final report
- Draw the message flow. Identify every `stop_reason` that will be hit. Define what happens on failure of any subagent.

### Module 1 Quiz
1. What are the four `stop_reason` values and what architectural decision does each one signal?
2. An orchestrator agent calls 8 tools in a single turn. Is this a design smell? Why or why not?
3. A subagent returns a hallucinated tool result. Where in the architecture should this be caught, and how?
4. Describe the difference between stateless and stateful multi-agent handoff. When would you use each?
5. A customer support agent is escalating too many tickets to humans. What are the three most likely architectural causes?

---

## Module 2 — Claude Code Configuration & Workflows

**Domain weight: 20%**

### Learning Objectives
- Write a production-quality `CLAUDE.md` from scratch for a given project context
- Explain the CLAUDE.md hierarchy: global → project → path-scoped
- Configure slash commands and explain when to use plan mode
- Design a Claude Code CI/CD integration for automated code review
- Identify the top 5 CLAUDE.md anti-patterns

### Key Concepts
| Concept | What to understand |
|---|---|
| CLAUDE.md hierarchy | Global (`~/.claude/`) → project root → subdirectory. How rules compose and override |
| Path-scoped rules | `[path]` blocks. When to use: different standards for `src/` vs `tests/` vs `scripts/` |
| Slash commands | What they are, how to register them, when they save time vs add complexity |
| Plan mode | When to require it: multi-file changes, architectural decisions, irreversible actions |
| Built-in tools | Read, Write, Edit, Bash, Glob, Grep — when each is right. Why Bash is the last resort |
| CI/CD integration | Non-interactive mode, `--output-format json`, exit codes, headless operation |
| Permissions model | allowedTools, deniedTools, project vs. user settings |

### Exam Scenarios Covered
- **Scenario 2:** Code Generation with Claude Code — CLAUDE.md setup, slash commands, plan mode
- **Scenario 5:** Claude Code in CI/CD — automated review, test generation, PR feedback

### Session Exercise
Write a `CLAUDE.md` for a Python FastAPI backend project with these constraints:
- TDD is mandatory — no code without tests first
- `src/` has different rules than `tests/` and `scripts/`
- A `/deploy` slash command should require explicit confirmation
- Plan mode must be on for any change touching the database layer
- Bash is restricted to git operations only

Then critique your own `CLAUDE.md` against the anti-pattern list.

### Module 2 Quiz
1. CLAUDE.md rules conflict between global and project level. Which wins, and why?
2. When should you use plan mode by default, and when does it create more friction than value?
3. A developer wants Claude Code to run `npm run build` after every file save. How do you configure this, and what are the risks?
4. You're integrating Claude Code into a GitHub Actions CI pipeline. What three flags/settings are non-negotiable?
5. What is the difference between `allowedTools` and `deniedTools` in settings? When would you use one over the other?

---

## Module 3 — Prompt Engineering & Structured Output

**Domain weight: 20%**

### Learning Objectives
- Write few-shot prompts that produce consistent, parseable JSON
- Design a JSON schema for a complex extraction task with nested types
- Build a validation loop that catches and corrects malformed output without crashing
- Identify the four most common structured output failure modes
- Explain why structured output for production differs from structured output in a notebook

### Key Concepts
| Concept | What to understand |
|---|---|
| Few-shot prompting | Example selection strategy: diverse, representative, edge-case-covering. How many is enough |
| JSON schema design | Required vs. optional fields. `enum` for controlled vocabularies. `$defs` for reuse. `additionalProperties: false` |
| Validation loops | Schema validation → retry with error context → escalate after N failures. Never silently swallow |
| Extraction vs. generation | Different failure modes. Extraction: hallucinated fields, missed fields. Generation: drift from schema |
| System prompt structure | Role → Context → Task → Constraints → Output format. Why order matters |
| Batch processing | How to maintain schema consistency across 1000 documents. Sampling strategy for spot-check |
| Hallucination prevention | Grounding techniques, citation anchoring, confidence fields in schema |

### Exam Scenarios Covered
- **Scenario 6:** Structured Data Extraction — JSON schemas, batch processing, hallucination prevention
- **Scenario 5:** Claude Code in CI/CD — structured output for automated PR feedback

### Session Exercise
Design a structured extraction pipeline for this task:
- Input: unstructured customer support ticket (freeform text)
- Output: JSON with fields: `issue_category` (enum), `urgency` (1–5), `customer_sentiment` (enum), `resolution_required` (bool), `summary` (max 100 words), `entities` (array of named entities)
- Write the JSON schema, the system prompt, and a 3-example few-shot block
- Write the validation loop pseudocode (what happens on each failure mode)

### Module 3 Quiz
1. A batch job extracts data from 5,000 documents. 3% return malformed JSON. What is your production strategy?
2. What is the difference between `required` fields and `additionalProperties: false` in a JSON schema? Why use both?
3. Write a system prompt structure (section headers only) for a contract clause extraction task.
4. Few-shot examples are all edge cases. What goes wrong, and how do you fix it?
5. A Claude extraction pipeline returns the right schema but wrong values. What are the three most likely causes?

---

## Module 4 — Tool Design & MCP Integration

**Domain weight: 18%**

### Learning Objectives
- Explain the three MCP primitives (tools, resources, prompts) and when to use each
- Choose between stdio and SSE transport for a given deployment context
- Write a tool description that Claude will actually use correctly
- Design authentication patterns for MCP servers in enterprise deployments
- Identify the three most common MCP integration anti-patterns

### Key Concepts
| Concept | What to understand |
|---|---|
| MCP server anatomy | `tools`, `resources`, `prompts` — what each is for. Server ↔ client protocol |
| stdio vs SSE transport | stdio: local, single-process, simple. SSE: networked, multi-client, stateful. Decision criteria |
| Tool description quality | The tool description IS the API contract for Claude. What makes a description usable vs. ambiguous |
| Tool input schema | Parameter typing, required vs. optional, description per parameter. Why this matters for reliability |
| Auth patterns | OAuth, API keys, service accounts. Where credentials live. Why they never go in tool descriptions |
| Tool granularity | Too coarse: Claude can't use it precisely. Too fine: combinatorial explosion. Finding the right grain |
| Error surface design | How tool errors reach Claude. What Claude can recover from vs. what needs human escalation |

### Exam Scenarios Covered
- **Scenario 4:** Developer Productivity Tools — built-in tools + MCP integration
- **Scenario 3:** Multi-Agent Research System — tool design for agent delegation

### Session Exercise
Design an MCP server for an internal knowledge base tool:
- Tool 1: `search_knowledge_base(query: string, top_k: int) → SearchResult[]`
- Tool 2: `get_article(article_id: string) → Article`
- Tool 3: `summarise_article(article_id: string, max_words: int) → Summary`
- Write the full tool description for Tool 1 (name, description, input schema with descriptions)
- Choose transport. Justify it.
- Define the auth pattern. Where do credentials live?
- Define the error surface: what errors can Claude recover from, what needs escalation?

### Module 4 Quiz
1. When do you choose SSE transport over stdio? Name three deployment signals that would push you to SSE.
2. A tool description says: "Gets data." What three things are wrong with this, and how do you fix each?
3. An MCP tool requires an API key. Where exactly does the key live in the architecture, and why?
4. A developer wants one tool that does everything: `do_thing(action: string, params: object)`. What is wrong with this design?
5. Claude calls a tool and receives a 500 error. What should happen next architecturally — and who decides?

---

## Module 5 — Context Management & Reliability

**Domain weight: 15%**

### Learning Objectives
- Apply the CALM framework to a multi-turn conversation design
- Implement prompt caching correctly using `cache_control` breakpoints
- Design a conversation compaction strategy that preserves critical context
- Set and enforce token budgets for a production agentic system
- Identify the three most common context management failures in production

### Key Concepts
| Concept | What to understand |
|---|---|
| CALM framework | Compress, Anchor, Layer, Monitor — the four levers for context health |
| Prompt caching | Where to place `cache_control` breakpoints. Cache TTL (5 min). What is and isn't cacheable |
| Conversation compaction | When to summarise history. What to preserve verbatim vs. summarise. How compaction affects tool use |
| Token budgeting | Input tokens vs. output tokens vs. cache read/write. Cost model. Budget enforcement patterns |
| Multi-turn design | What belongs in system prompt vs. conversation history vs. injected context |
| Context overflow | What happens when you hit the limit. Prevention vs. recovery strategies |
| Reliability patterns | Retry with backoff, fallback models, circuit breakers, graceful degradation |

### Exam Scenarios Covered
- **Scenario 1:** Customer Support Agent — multi-turn conversation management
- **Scenario 3:** Multi-Agent Research System — context passing across agents

### Session Exercise
A customer support agent handles 10-turn conversations and must:
- Remember the customer's issue throughout the conversation
- Cache the product knowledge base (doesn't change per conversation)
- Compac history after turn 5 without losing issue context
- Stay under 4,000 output tokens per turn
- Design: where does `cache_control` go? What gets compacted? What must never be lost? Draw the token budget.

### Module 5 Quiz
1. What are the four letters of the CALM framework and what does each one mean?
2. A system prompt has three sections: company policy, product catalogue, and conversation instructions. Which gets `cache_control` and why?
3. After compaction, a support agent loses track of the customer's original complaint. What went wrong in the compaction strategy?
4. An agentic pipeline costs $0.40/run in development but $4.00/run in production with the same prompts. Name three likely causes.
5. At what point in a conversation should you trigger compaction, and how do you decide what to preserve vs. summarise?

---

## Module 6 — Scenario Simulation Lab

**Goal:** Architect complete solutions for all 6 exam scenarios before mock exam conditions.

### Format
For each scenario: you design the architecture cold (no hints), then we compare against the exam-aligned pattern, then you identify the gaps.

### The Six Scenarios

| # | Scenario | Primary Domain | Time |
|---|---|---|---|
| 1 | Customer Support Resolution Agent | Domain 1 + 5 | 30 min |
| 2 | Code Generation with Claude Code | Domain 2 | 25 min |
| 3 | Multi-Agent Research System | Domain 1 + 4 | 30 min |
| 4 | Developer Productivity Tools | Domain 4 | 25 min |
| 5 | Claude Code in CI/CD | Domain 2 + 3 | 25 min |
| 6 | Structured Data Extraction | Domain 3 | 25 min |

### Anti-Pattern Recognition Drill
The exam weights anti-pattern recognition highly. Before each scenario architecture: name the three most common ways a bad architect would approach this scenario. Then design around them.

---

## Module 7 — Mock Exam + Gap Review

**Format:**
- 30 questions in 60 minutes (half-exam)
- Questions drawn proportionally from all 5 domains
- Scored and mapped back to domains
- Gaps logged in `GAPS.md`
- Targeted review of any domain below 70%
- Second 30-question mock if any domain is below 70%

### What to Expect
Mock questions will be scenario-based: "An architect made this decision — what is wrong with it?" not "Define this term." Study for reasoning, not recall.

---

## Pacing Guide

| Week | Modules | Focus |
|---|---|---|
| Week 1 | 0, 1 | Foundation + heaviest domain (Agentic Architecture) |
| Week 2 | 2, 3 | Claude Code + Prompt Engineering |
| Week 3 | 4, 5 | MCP/Tools + Context Management |
| Week 4 | 6, 7 | Scenario simulation + mock exam |

> Ram's best learning hours: 5–8 AM IST. One module per 60–90 min sprint. Don't run two modules in one session — the active recall needs time to consolidate.

---

## Progress Tracker

| Module | Started | Quiz Score | Notes |
|---|---|---|---|
| 0 — Foundations | 2026-06-06 | 4 / 5 ⚠ synthetic | Self-driven (Ram distracted) — modeled answers, not real recall. Re-run interactively for a true baseline. Gaps: scaled-scoring rationale, 1 scenario recall. |
| 1 — Agentic Architecture | 2026-06-06 | 4.5 / 5 ⚠ synthetic | Self-driven (Ram distracted) — modeled, not real recall. **Highest-value module to re-run interactively (27%).** Gap: parallel-tool-calls nuance (count ≠ smell). |
| 2 — Claude Code | 2026-06-06 | 4 / 5 ⚠ synthetic | Modeled, not real recall. Gap: automation = hook (settings.json), not CLAUDE.md memory. |
| 3 — Prompt Engineering | 2026-06-06 | 4.5 / 5 ⚠ synthetic | Modeled. Gap: Structured Outputs prevents malformed JSON at source > retry-after. Worth a real re-run (20%). |
| 4 — Tool Design & MCP | 2026-06-06 | 4.5 / 5 ⚠ synthetic | Modeled. Gap: recoverable-vs-escalate is an architectural decision, not "Claude retries." |
| 5 — Context Management | 2026-06-06 | 4.5 / 5 ⚠ synthetic | Modeled. Gap: CALM L = Layer (not Limit). |
| 6 — Scenario Lab | | / 6 scenarios | |
| 7 — Mock Exam | | / 30 | |

---

## How to Run a Module Session

When starting a module session, tell Claude:

> "Run Module [N] — [name]"

Claude will:
1. Open with the Orient act (big picture, why this domain exists)
2. Teach the key concepts (why before how, pattern names, real-world analogies)
3. Present the hands-on exercise
4. End with the 5-question quiz, score it, and log any misses to `GAPS.md`

Do not skip the quiz. The quiz is the learning, not a test of it.
