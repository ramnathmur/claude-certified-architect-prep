# CCA-F Exam Mechanics

**Primary source:** `source/CCA-F-Official-Exam-Guide.pdf` — official Anthropic Exam Guide v0.2 (downloaded 2026-07-06 from the Skilljar certification page; plain-text mirror at `source/CCA-F-Official-Exam-Guide_text.txt`)
**Secondary source:** `source/guide_en.md` — community study guide (github.com/paullarionov/claude-certified-architect); depth and practice-test source, NOT authoritative for exam facts
**Version:** 2.0 | 2026-07-06
**Changelog v1→v2:** re-grounded on the official PDF (v1 cited the community guide as "official"); added 60 Q / 120 min / validity / delivery / fee / retake facts; corrected scenario pool to the official 4-of-6 (v1 said "8 exist" and Corpus-Index said 5+1 — both wrong); added the two previously missing official scenarios; corrected practice-test arithmetic; added official In-Scope and Technologies appendices; added style-calibration pointer.

---

## Format (official, Exam Guide v0.2 p.2)

| Attribute | Value |
|---|---|
| Credential | Claude Certified Architect – Foundations |
| Number of questions | **60** |
| Time limit | **120 minutes** (~2 min/question) |
| Response format | Multiple choice — 1 correct + 3 incorrect options, single answer |
| Exam structure | **4 scenarios drawn at random from a bank of 6** |
| Content domains | 5 (weights below) |
| Delivery | Online proctored or at a test center (Pearson VUE administers, effective 2026-06-30) |
| Exam fee | $125 USD |
| Scoring | Scaled 100–1,000; **minimum passing score 720** |
| Validity | **12 months** from award date |
| Result reporting | Pass / fail |
| Answering | The platform **requires an answer to every question before advancing** — no skip, no penalty for wrong answers, so an unsure answer is always submitted |
| Retakes | Max 4 attempts per rolling 12 months; waiting periods apply between attempts (per Pearson VUE policy pages, retrieved 2026-07-06) |

## Domain weights (official)

| Domain | Weight |
|---|---|
| D1 Agentic Architecture & Orchestration | 27% |
| D2 Tool Design & MCP Integration | 18% |
| D3 Claude Code Configuration & Workflows | 20% |
| D4 Prompt Engineering & Structured Output | 20% |
| D5 Context Management & Reliability | 15% |

Domain-weighted scoring: D1 questions collectively carry the most scored content. No partial credit per question. Scaled scoring equates difficulty across exam forms.

---

## Scenario Bank — the official 6 (Exam Guide v0.2 pp.4–5)

Every exam sitting presents 4 of these 6, at random. Each scenario frames a block of questions (~15 per scenario at 60 questions / 4 scenarios).

### Scenario 1: Customer Support Resolution Agent
Agent SDK agent for high-ambiguity requests (returns, billing disputes, account issues); custom MCP tools `get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`; target 80%+ first-contact resolution while knowing when to escalate.
**Primary domains:** D1, D2, D5.

### Scenario 2: Code Generation with Claude Code
Claude Code for code generation, refactoring, debugging, documentation; custom slash commands, CLAUDE.md configurations, plan mode vs direct execution.
**Primary domains:** D3, D5.

### Scenario 3: Multi-Agent Research System
Coordinator delegates to web-search, document-analysis, synthesis, and report-generation subagents; produces comprehensive cited reports.
**Primary domains:** D1, D2, D5.

### Scenario 4: Developer Productivity with Claude *(was missing from corpus v1)*
Agent SDK tools helping engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate, automate repetitive tasks; uses **built-in tools (Read, Write, Bash, Grep, Glob)** and MCP servers.
**Primary domains:** D2, D3, D1.
**Key themes:** built-in tool selection (Grep vs Glob vs Read/Write/Edit), incremental investigation strategy, Edit→Read+Write fallback, MCP tool descriptions vs built-in preference — see `CCA-Prep_Domain-2_v2.md` §2.9.

### Scenario 5: Claude Code for Continuous Integration
Claude Code in CI/CD: automated code reviews, test generation, PR feedback; actionable feedback with minimal false positives.
**Primary domains:** D3, D4.

### Scenario 6: Structured Data Extraction *(was missing from corpus v1)*
Extraction from unstructured documents, JSON-schema validation, high accuracy, graceful edge-case handling, downstream integration.
**Primary domains:** D4, D5.
**Key themes:** tool_use + JSON schema as the output guarantee, tool_choice "any"/forced, nullable fields to prevent fabrication, retry-with-feedback and its limits, batch strategies with custom_id, confidence calibration and human-review routing — see `CCA-Prep_Domain-4_v2.md` and `CCA-Prep_Domain-5_v2.md`.

**Non-official scenarios:** the community guide documents a "Conversational AI Architecture Patterns" scenario (its #7) and an "Agentic AI Tools" placeholder (its #8). These are candidate-reported, NOT in the official bank of 6. Content under them remains useful study material (it maps to D1/D5 task statements) but the generator must not present them as exam scenarios.

---

## Answer Pattern Heuristics

From practice-test analysis (v1, retained) plus the official sample-question rationales (Exam Guide pp.24–31):

| Heuristic | When it applies |
|---|---|
| Fix the root cause, not the symptom | Misrouting → fix tool descriptions, not add a classifier |
| Proportionate first response | Try the prompt/description fix before adding infrastructure (classifiers, routing layers, bigger models) |
| Programmatic enforcement for critical sequences | Identity-verification-before-refund → hook/precondition, never prompt-only (prompt compliance is probabilistic) |
| Least privilege | Scoped verify_fact for synthesis agent, not full web-search access |
| Deterministic over probabilistic | Hooks/gates for guaranteed compliance; prompts for guidance |
| Structured error context > generic failure | Return failure type, attempted query, partial results, alternatives |
| Parallel with shared context > sequential | Multi-issue requests: decompose and parallelize |
| Coordinator as hub | Subagents never talk to each other directly |
| Independence for review passes | Second instance without the generator's reasoning context |
| Match the API to the latency requirement | Blocking pre-merge → synchronous; overnight reports → batch |
| Coverage gaps trace upstream | Complete-looking subagent outputs + missing topics → check the coordinator's decomposition |
| Attention dilution → split passes | Inconsistent 14-file review → per-file passes + integration pass, not a bigger context window |

---

## Question Style Calibration

The register reference for generated questions is twofold:
1. **Official sample questions** — 12 samples with answer rationales, Exam Guide pp.24–31 (drawn from the practice test). Stem shape: 2–5 sentence Situation with concrete telemetry ("12% of cases", "55% first-contact resolution", "14 files"), then a single decision question ("What change would most effectively address...", "What's the most likely root cause?", "How should you evaluate this proposal?"). Options are full clauses, grammatically parallel, each plausible to a candidate with incomplete knowledge; rationales explain why each wrong option fails (symptom-level fix, over-engineering, wrong problem, non-existent feature).
2. **`PRACTICE-TEST-STEMS_v1.md` §3** — quantitative style profile of the full community practice test (stem lengths, option forms, question-form distribution, distractor patterns).

**Dedup constraint:** every stem in `PRACTICE-TEST-STEMS_v1.md` §2 (which includes all official samples, since samples are drawn from the practice test) is off-limits for generated exams — Ram will take that practice test himself.

---

## Official In-Scope Topics (Exam Guide v0.2 Appendix — generator's topic whitelist)

Agentic loop implementation (stop_reason control flow, tool result handling, termination) · multi-agent orchestration (coordinator-subagent, decomposition, parallel execution, iterative refinement) · subagent context management (explicit passing, state persistence, crash-recovery manifests) · tool interface design (descriptions, split vs consolidate, naming) · MCP tool and resource design (resources as catalogs, tools as actions) · MCP server configuration (project vs user scope, env-var expansion, multi-server) · error handling and propagation (structured responses, transient/business/permission, local recovery) · escalation decision-making (explicit criteria, honoring customer preference, policy gaps) · CLAUDE.md configuration (hierarchy, @import, .claude/rules/ globs) · custom commands and skills (scopes, context: fork, allowed-tools, argument-hint) · plan mode vs direct execution · iterative refinement (I/O examples, test-driven, interview pattern, sequential vs batch issue fixing) · structured output via tool_use (schema design, tool_choice, nullable fields) · few-shot prompting (ambiguity targeting, format consistency, false-positive reduction) · batch processing (appropriateness, latency tolerance, custom_id failure handling) · context window optimization (trimming tool outputs, fact extraction, position-aware ordering) · human review workflows (confidence calibration, stratified sampling, per-segment accuracy) · information provenance (claim-source mappings, temporal data, conflict annotation, coverage gaps).

### Technologies list (Appendix "Technologies and Concepts")
Claude Agent SDK (AgentDefinition, agentic loops, stop_reason, PostToolUse + interception hooks, Task tool, allowedTools) · MCP (servers, tools, resources, isError, .mcp.json, env-var expansion) · Claude Code (CLAUDE.md hierarchy, .claude/rules/, .claude/commands/, .claude/skills/ frontmatter, plan mode, /memory, /compact, --resume, fork_session, Explore subagent) · CLI (-p/--print, --output-format json, --json-schema) · Claude API (tool_use, tool_choice auto/any/forced, stop_reason values, max_tokens, system prompts) · Message Batches API (50% savings, 24h window, custom_id, polling, no multi-turn tool calling within a request) · JSON Schema (required/optional, enums, nullable, "other"+detail) · Pydantic (validation, retry loops) · built-in tools (Read, Write, Edit, Bash, Grep, Glob) · few-shot · prompt chaining · context management (token budgets, summarization, lost-in-the-middle, scratchpads) · session management · confidence scoring (field-level, calibration, stratified sampling).

---

## Out-of-Scope Topics (official — will NOT appear; generator hard constraint)

- Fine-tuning or training custom Claude models
- Claude API authentication, billing, or account management
- Language/framework-specific implementation details (beyond tool/schema config)
- Deploying or hosting MCP servers (infrastructure, networking, containers)
- Claude's internal architecture, training process, or model weights
- Constitutional AI, RLHF, or safety training methodologies
- Embedding models or vector database implementation details
- Computer use (browser automation, desktop interaction)
- Image analysis / Vision capabilities
- Streaming API or server-sent events
- Rate limiting, quotas, or detailed API cost calculations
- OAuth, API key rotation, or authentication protocol details
- Cloud-provider-specific configurations (AWS, GCP, Azure)
- Performance benchmarks or model comparison metrics
- Prompt caching implementation details (beyond knowing it exists)
- Token counting algorithms or tokenization specifics

---

## Scoring Context

- Scale 100–1,000; pass 720; pass/fail reporting only
- Scaled scoring equates across exam forms of slightly different difficulty — a raw-percentage → scaled conversion is therefore an approximation; the generator's estimate formula must carry that caveat
- No partial credit; platform forces an answer on every question (guessing costs nothing)
- Domain-weighted: getting D1 wrong hurts most (27%), D5 least (15%)

## Docs Currency

Product behavior facts in the corpus are periodically re-verified against live Anthropic docs — divergences and the exam-vs-current-docs posture per item live in `CURRENT-DOCS-DELTA_v1.md`. Generator rule: where the official Exam Guide and current docs conflict, the official guide's framing wins for question authoring.
