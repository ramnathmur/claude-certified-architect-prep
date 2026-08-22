# CCA-F Full Curriculum Map

**Version:** 1.0
**Built:** 2026-06-26
**Based on:** Official CCA-F study guide (guide_en.MD) + anthropic.skilljar.com verification + 12-file existing course audit

---

## Exam Quick Reference

| Parameter | Value |
|---|---|
| Exam name | Claude Certified Architect — Foundations (CCA-F) |
| Platform | anthropic.skilljar.com |
| Questions | 60 scenario-driven MCQs |
| Duration | 120 minutes, closed-book, no AI assistance |
| Passing score | 720 / 1000 scaled |
| Cost | $99 per attempt (verify free attempt via Infosys/Claude Partner status first) |
| Scenarios | 4 of 6 possible scenarios appear per exam (randomly selected) — per the official exam guide |

---

## Domain Map

| Code | Domain | Weight | Sessions |
|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | 8 |
| D2 | Tool Design & MCP Integration | 18% | 5 |
| D3 | Claude Code Configuration & Workflows | 20% | 6 |
| D4 | Prompt Engineering & Structured Output | 20% | 7 |
| D5 | Context Management & Reliability | 15% | 5 |

---

## Prerequisite Graph

```
API fundamentals (Chapter 1)
    ↓
Tool use mechanics (Chapter 2)
    ↓                    ↓
Agentic loop (D1)    MCP concepts (D2)
    ↓                    ↓
Coordinator/subagent  Tool design (D2)
pattern (D1)              ↓
    ↓              CLAUDE.md + CI/CD (D3)
Hooks (D1)
    ↓
Escalation + handoff (D1)
    ↓
Session management (D1)
    ↓
Task decomposition (D1)
         \
          → Prompt patterns (D4)
          → JSON schemas + tool_choice (D4)
          → Validation/retry (D4)
          → Batch API (D4)
                    ↓
Context accumulation (D5)
    ↓
Trimming + persistent blocks (D5)
    ↓
Scratchpad + state persistence (D5)
    ↓
Confidence calibration + provenance (D5)
                ↓
        INTEGRATION SCENARIOS (all domains)
                ↓
           MOCK EXAMS
```

---

## Domain 1 — Agentic Architecture & Orchestration (27%)

### Coverage of existing material
- Orchestration patterns HTML: **Full** — 5 named patterns, workflow vs agent distinction
- Subagents-as-SDK-primitive HTML: **Full** — AgentDefinition, Task tool, context isolation
- Orchestrator-worker HTML: **Full** — coordinator pattern, multi-agent research reference architecture, failure modes
- Introduction-to-subagents HTML: **Partial** — single-agent CLI, lacks SDK generalization
- **Gaps (no existing coverage):** Hooks, escalation triggers, structured handoff protocols, fork_session, task decomposition strategies

### Complete topic list

**Sub-domain D1.1 — Agentic Loop Fundamentals**
- API request anatomy: model, max_tokens, system, messages, tools, tool_choice
- Message roles: user, assistant, tool (tool_result content block)
- Why full history must be sent on every request (model is stateless)
- `stop_reason` field values and what each requires:
  - `"end_turn"` → show result to user
  - `"tool_use"` → execute tool, append result, loop
  - `"max_tokens"` → response truncated, increase limit
  - `"stop_sequence"` → handle per application logic
- The agentic loop pattern: send → check stop_reason → execute → return result → repeat
- Model-driven vs hard-coded decision trees: why the model chooses the next tool
- Anti-patterns: parsing assistant text for completion, using arbitrary `max_iterations` as primary stop condition, checking for textual content as completion signal
- Correct stop signal: `stop_reason == "end_turn"` is the ONLY reliable completion signal

**Sub-domain D1.2 — AgentDefinition Configuration**
- `AgentDefinition` parameters: name, description, system_prompt, allowed_tools
- Principle of least privilege in tool assignment
- Description and system_prompt best practices
- When to use a coordinator's `allowed_tools` to include `"Task"`

**Sub-domain D1.3 — Hub-and-Spoke Multi-Agent Architecture**
- Hub-and-spoke topology: coordinator owns all inter-agent communication
- Coordinator responsibilities: task decomposition, delegation, result aggregation, error handling, user communication
- Subagent context isolation: subagents do NOT automatically inherit coordinator's conversation history
- All required context must be explicitly passed in the subagent prompt
- Subagents do not share memory across calls
- All communication flows through the coordinator (for observability)
- Risk of overly narrow decomposition by the coordinator

**Sub-domain D1.4 — The Task Tool and Parallel Spawning**
- `Task` tool: how to spawn subagents
- ★ Renamed `Task` → `Agent` in Claude Code v2.1.63 (SDKs emit `"Agent"` in tool_use but may still list `"Task"` in `system:init`); both correct by version — treat "Task" as "Task/Agent."
- Coordinator's `allowed_tools` must include `"Task"`
- Explicit context passing — the bad pattern vs the good pattern:
  - Bad: "Analyze the document" (no context)
  - Good: full document + prior results + output schema in the prompt
- Parallel spawning: coordinator calls multiple `Task`s in one response → subagents run concurrently
- Context budget constraints for subagents: minimal context, structured output required

**Sub-domain D1.5 — Hooks: PreToolUse and PostToolUse** ★ GAP
- What hooks are: interception points in the agent lifecycle
- ★ The lifecycle has ~18 hook types (exam may name beyond Pre/Post): `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `PreCompact`, `SubagentStart`/`Stop`, `PermissionRequest`. Hook permission outcomes: `allow`/`deny`/`ask`/`defer` — `defer` ends the query for later resumption (≠ `ask`); parallel hooks resolve most-restrictive-first (deny > defer > ask > allow).
- `PostToolUse` hook: intercepts tool result BEFORE model consumes it
  - Use case: normalize date formats (Unix timestamp → ISO 8601)
  - Use case: trim verbose tool results to relevant fields
- `PreToolUse` (outgoing-call interception): blocks actions that violate policy
  - Use case: block refunds above $500
  - Redirects to escalation instead of blocking silently
- The fundamental distinction:
  - Hooks = **deterministic guarantees** (100%)
  - Prompt instructions = **probabilistic compliance** (>90%, not 100%)
- Rule: when failure has financial, legal, or safety consequences → use hooks, not prompts
- Examples of each category:
  - Hook territory: refund limits, financial thresholds, compliance rules
  - Prompt territory: general preferences, formatting, style guidance

**Sub-domain D1.6 — Escalation Patterns** ★ GAP
- When to escalate immediately (explicit request: "get me a manager" → escalate, do not attempt to solve first)
- When to attempt-then-escalate (within-scope issues: try resolution first)
- Nuanced pattern: acknowledge emotion → propose concrete solution → escalate only if customer reiterates desire for human
- Policy gap escalation: when policy is silent on the request, escalate (do not guess)
- Multiple customer matches: ask for additional identifiers, never heuristically guess
- Unreliable escalation triggers:
  - Sentiment analysis (mood ≠ case complexity)
  - Model self-rated confidence (1–10) — model can be confidently wrong
  - Automated classifiers — overengineering requiring training data
- Structured handoff protocol: what the escalation summary must contain
  - customer_id, issue_summary, order_id, root_cause, actions_taken, refund_amount, recommended_action, escalation_reason
  - Human operator sees only this summary — it must be complete and self-contained

**Sub-domain D1.7 — Session Management** ★ GAP
- `--resume <session-name>`: resumes named sessions with saved context
  - Use case: long investigations across multiple sessions
  - Risk: if files changed since prior session, tool results may be stale
- `fork_session`: creates an independent branch from shared context
  - Use case: compare approaches (Redux vs Context API) from a common starting point
  - Both forks inherit context up to the branch point; afterwards they diverge independently
- When to resume vs when to start fresh:
  - Resume: context still current (files unchanged, results still valid)
  - Start fresh: results stale, significant time passed, better to summarize and restart
  - "Here is a short summary of what we found: ..." is more reliable than resuming with old tool data

**Sub-domain D1.8 — Task Decomposition Strategies**
- Fixed pipelines (prompt chaining): steps defined in advance
  - When to use: predictable task structure, all steps known upfront, stability required
  - Example: metadata extraction → data extraction → validation → enrichment → output
- Dynamic adaptive decomposition: subtasks generated from intermediate results
  - When to use: open-ended investigative tasks, full scope unknown upfront, each step depends on prior results
  - Example: "add tests for legacy codebase" → map structure → prioritize → adapt when dependency discovered
- Multi-pass code review: per-file local analysis pass + separate cross-file integration pass
  - Why single pass over 14 files fails: attention dilution, inconsistent comments, missed bugs
  - Correct approach: file-by-file analysis (parallel subagents) then integration pass (coordinator)

---

## Domain 3 — Claude Code Configuration & Workflows (20%)

### Coverage of existing material
- claude-code-configuration HTML: **Partial** — CLAUDE.md hierarchy, .claude/rules/, custom commands basics
- subagents-as-sdk-primitive HTML: **Partial** — /agents command, config files, scope
- **Gaps:** Skills frontmatter parameters in depth, CI/CD -p flag + JSON output, @path syntax detail, path-specific rules detail

### Complete topic list

**Sub-domain D3.1 — CLAUDE.md Hierarchy**
- Three levels of CLAUDE.md:
  1. User-level: `~/.claude/CLAUDE.md` — applies only to that user, NOT VCS-shared, personal preferences
  2. Project-level: `.claude/CLAUDE.md` or root `CLAUDE.md` — applies to all contributors, managed via VCS, coding standards
  3. Directory-level: `CLAUDE.md` in subdirectories — applies when working with files in that directory
- Common mistake: new team member misses instructions because they were placed in user-level instead of project-level
- `@path` syntax for file imports:
  - Use `@` immediately before the file path (no space): `@./standards/coding-style.md`
  - Relative paths resolved relative to the file containing the import
  - Maximum import nesting depth: 5
  - Use case: modular configuration across a monorepo (each package includes only relevant standards)

**Sub-domain D3.2 — Path-Specific Rules (.claude/rules/)**
- `.claude/rules/` directory: organizes rules by topic instead of monolithic CLAUDE.md
  - Files: `testing.md`, `api-conventions.md`, `deployment.md`, `react-patterns.md`
- YAML frontmatter with `paths:` for conditional loading:
  ```yaml
  ---
  paths: ["src/api/**/*"]
  ---
  ```
- A rule is loaded ONLY when Claude Code edits a file matching the pattern
- Glob patterns apply conventions by file type regardless of location (ideal for tests scattered across codebase)
- When to use `.claude/rules/` with `paths` vs directory-level CLAUDE.md:
  - `paths` rules: conventions that apply to files spread across many directories (tests, migrations)
  - Directory CLAUDE.md: conventions tied to a specific directory, not needed elsewhere

**Sub-domain D3.3 — Custom Slash Commands and Skills** ★ GAP
- Slash commands are reusable prompt templates invoked via `/name`
- Two directory conventions (both supported):
  - `.claude/commands/` format (legacy, still supported): `review.md` → `/review`
  - `.claude/skills/` format (current): `review/SKILL.md` → `/review`
- Project commands (`.claude/commands/` or `.claude/skills/`): stored in VCS, available to everyone on clone
- User commands (`~/.claude/commands/` or `~/.claude/skills/`): personal, not VCS-shared
- Skills frontmatter parameters:
  - `context: fork` — runs skill in isolated subagent; verbose output does NOT pollute main session
  - `allowed-tools` — ★ pre-approves (auto-approves) the listed tools while the skill is active; does NOT restrict the others (common misconception — the name sounds restrictive but is permissive). Use `disallowed-tools` to actually remove tools from the pool.
  - `argument-hint` — asks for an argument when invoked without parameters
- When to use a skill vs CLAUDE.md:
  - Skill: on-demand invocation for a specific task (review, analysis, generation)
  - CLAUDE.md: always-loaded general standards and conventions
- Personal skill variants: create under different names in `~/.claude/skills/` to avoid affecting teammates

**Sub-domain D3.4 — Planning Mode vs Direct Execution**
- Planning mode:
  - Model only investigates and plans; it does NOT make changes
  - Uses Read, Grep, Glob to explore; produces an implementation plan for user approval
  - Safe exploration with no side effects
- When to use planning mode:
  - Large changes (dozens of files)
  - Multiple plausible approaches (e.g., microservices boundary design)
  - Architectural decisions (which framework, what structure)
  - Unfamiliar codebase
  - Library migrations affecting 45+ files
- When to use direct execution:
  - Single-file fix with clear stack trace
  - Adding one validation check
  - Well-understood, unambiguous changes
- Combined approach: planning mode for investigation → user approves → direct execution for implementation
- Explore subagent: isolates verbose discovery output from main context; returns only a summary

**Sub-domain D3.5 — Context Commands**
- `/compact` command:
  - Compresses prior history to free context window
  - Used in long investigation sessions when context fills with verbose tool output
  - Risk: exact numeric values, dates, and specific details can be lost during summarization
- `/memory` command:
  - Opens CLAUDE.md for editing; saves notes, preferences, context between sessions
  - Information persists across sessions and is automatically loaded on startup
  - Alternative to re-explaining same instructions every session

**Sub-domain D3.6 — Claude Code CLI for CI/CD** ★ GAP
- The `-p` (or `--print`) flag:
  ```bash
  claude -p "Analyze this pull request for security issues"
  ```
  - Non-interactive mode: processes prompt, prints to stdout, exits
  - Does NOT wait for user input
  - The ONLY correct way to run Claude in CI/CD pipelines
  - ★ `--bare` (EXAM TRAP): skips auto-loading of ALL local config (hooks, CLAUDE.md, skills, plugins, MCP, auto-memory); plain `-p` does NOT. `claude -p "..."` ≠ `claude -p --bare "..."`. Recommended for scripted/SDK calls; will become the `-p` default in a future release.
- Structured output for CI:
  ```bash
  claude -p "Review this PR" --output-format json --json-schema '{"type":"object",...}'
  ```
  - `--output-format json` → output in JSON
  - `--json-schema` → validate output against a schema
  - Result can be parsed to automatically post inline PR comments
- Session context isolation:
  - The same Claude session that generated code is less effective at reviewing it
  - The model retains its reasoning context and is less likely to challenge its own decisions
  - Use an independent instance for review
- Preventing duplicate comments when re-reviewing after new commits:
  - Include prior review results in context
  - Instruct Claude to report only new or unresolved issues

---

## Domain 4 — Prompt Engineering & Structured Output (20%)

### Coverage of existing material
- prompt-engineering-depth HTML: **Partial** — few-shot, CoT, XML, prefilling, model selection
- **Gaps:** Batch API, validation/retry loops, multi-instance review architectures, self-correction patterns

### Complete topic list

**Sub-domain D4.1 — Few-Shot Prompting**
- Why few-shot beats textual descriptions: examples demonstrate format AND decision logic unambiguously
- The 5 types of few-shot examples and when to use each:
  1. Ambiguous scenarios — shows tool selection rationale for edge cases
  2. Output formatting — demonstrates expected output shape
  3. Acceptable vs problematic code — shows what to flag vs what to ignore
  4. Extraction from different document formats — inline citations vs bibliography references
  5. Informal measurements — "two handfuls of rice" → `{"amount": "~100g", "precision": "approximate"}`
- Few-shot is especially effective for informal/non-standard measurements that are too diverse for rules
- Format normalization rules in prompts (when using strict JSON schemas):
  - Dates: always ISO 8601; relative dates ("yesterday") → compute absolute date
  - Currency: numeric amount + currency code; "five bucks" → `{"amount": 5, "currency": "USD"}`
  - Percentages: decimal fraction; "half" → 0.5

**Sub-domain D4.2 — Explicit Criteria vs Vague Instructions**
- Bad (vague): "Check code comments for accuracy. Be conservative."
- Good (explicit): "Flag a comment ONLY if: (1) it describes behavior that CONTRADICTS the actual code behavior, (2) references a non-existent function or variable, (3) TODO/FIXME refers to a bug already fixed. Do NOT flag: stylistically outdated comments, minor wording inaccuracies, missing comments."
- Define severity criteria with examples per level (CRITICAL, HIGH, MEDIUM, LOW)
- The effect of false positives on developer trust: high FP rates in some categories undermine trust in accurate categories

**Sub-domain D4.3 — Prompt Chaining**
- Breaks complex tasks into a sequence of focused steps
- Prevents attention dilution when analyzing multiple files simultaneously
- Ensures consistent analysis quality per file
- Allows separate analysis of cross-file interactions
- When to use prompt chaining vs dynamic decomposition:
  - Prompt chaining: predictable, repeatable tasks (code review, file migrations)
  - Dynamic decomposition: open-ended investigations where subtasks emerge during execution

**Sub-domain D4.4 — The "Interview" Pattern**
- Before implementing, Claude asks clarifying questions to surface non-obvious design considerations
- When useful: unfamiliar domain, tasks with non-obvious implications, multiple viable approaches

**Sub-domain D4.5 — tool_use with JSON Schemas**
- `tool_use` + JSON schema is the MOST RELIABLE way to get structured output
- Guarantees syntactically valid JSON (no missing braces, no trailing commas)
- Enforces required structure (required fields present)
- Does NOT guarantee semantic correctness (values can still be wrong)
- Schema design rules:
  - `required` vs optional: only mark required if information is ALWAYS available; required fields push model to fabricate when data is missing
  - Nullable fields: `"type": ["string", "null"]` — model can return null instead of hallucinating
  - Enums with `"other"` + detail string: avoids losing data outside predefined categories
  - Enum `"unclear"`: for cases where model cannot confidently pick — honest `"unclear"` beats wrong category

**Sub-domain D4.6 — tool_choice Parameter**
- `{"type": "auto"}` — model decides whether to call a tool or answer in text (default)
- `{"type": "any"}` — model MUST call some tool (guarantees structured output)
- `{"type": "tool", "name": "extract_metadata"}` — model MUST call specific tool (guaranteed first step / execution order)
- `tool_choice: "any"` + multiple extraction tools → model picks best one, but structured output guaranteed
- Forced selection → when you must guarantee a specific first action

**Sub-domain D4.7 — Syntax vs Semantic Errors**
- Syntax errors (invalid JSON, wrong field type) → eliminated by `tool_use` with JSON schema
- Semantic errors (totals don't add up, value in wrong field, hallucination) → require validation checks, retry with feedback, self-correction

**Sub-domain D4.8 — Validation, Retry-with-Feedback, and Self-Correction** ★ GAP
- Retry-with-feedback pattern:
  1. Extract data from document
  2. Validate (Pydantic, JSON Schema, business rules)
  3. If error: retry with original document + previous incorrect extraction + specific error message
  - Example: "Field 'total' = 150, but sum(line_items) = 145. Re-check values."
- When retry IS effective: format errors, structural errors, arithmetic inconsistencies
- When retry will NOT help: information is absent from source document; required context is in a different document
- Pydantic as validation tool:
  - Structural validation: types, requiredness, enum constraints checked after receiving JSON
  - Semantic validation: custom validators enforce business logic (sum check, date ordering)
  - Validate-retry loops: on Pydantic failure, construct error message and re-prompt
  - JSON Schema generation: Pydantic models can generate JSON Schema for tool_use (single source of truth)
- Self-correction pattern: extract both `stated_total` AND `calculated_total`; include `conflict_detected: true` when they differ

**Sub-domain D4.9 — Message Batches API** ★ GAP
- Savings: 50% compared to synchronous calls
- Processing window: up to 24 hours (no latency SLA guarantee)
- Multi-turn tool calling: NOT supported (one request = one response)
- `custom_id` field: links request to response; enables re-submitting only failed documents
- When to use Batch API vs synchronous:
  - Synchronous: pre-merge PR check (developer waiting), interactive code review (immediate response required)
  - Batch API: overnight tech-debt report, weekly security audit, processing 10,000 documents
- SLA planning: if result needed in 30 hours and batch can take up to 24 hours → must submit no later than 6 hours before deadline
- Handling failures: identify by custom_id, modify strategy (e.g., split long documents), re-submit only failures

**Sub-domain D4.10 — Multi-Instance Review Architectures** ★ GAP
- Self-review limitation: model retains its reasoning context and is less likely to challenge its own decisions
- Independent review instance (without generation context) finds subtle issues the generating instance misses
- Multi-pass review: per-file local analysis + separate cross-file integration pass (avoids attention dilution)
- Verification passes with self-rated confidence to route reviews appropriately

---

## Domain 2 — Tool Design & MCP Integration (18%)

### Coverage of existing material
- tool-use-agent-loop HTML: **Solid** — stop_reason cycle, tool_choice, client/server tools
- mcp-at-a-builder-level HTML: **Solid** — tools/resources/prompts primitives, JSON-RPC, stdio vs SSE
- **Gaps:** Tool description as the selection mechanism (depth), isError structured responses, tool count per agent problem, built-in tool selection guide

### Complete topic list

**Sub-domain D2.1 — Tool Description as the Selection Mechanism** ★ GAP
- The description is the PRIMARY mechanism an LLM uses to select tools
- Minimal descriptions ("Retrieves customer information") lead to mistakes when tools overlap
- What a good tool description must include:
  - What the tool does and what it returns
  - Input formats and example values
  - Edge cases and constraints
  - When to use THIS tool vs similar alternatives
- Common mistakes:
  - Identical or overlapping descriptions → model confuses them
  - `analyze_content` and `analyze_document` with nearly identical descriptions → misrouting
  - Fix: rename to eliminate functional overlap → `extract_web_results` vs `extract_document_text`
- System prompt wording can create unintended tool associations:
  - "Always verify the customer" → model overuses `get_customer` even when unnecessary
- Built-in tools vs MCP tools: agents prefer built-in tools (Read, Grep) over MCP tools with similar functionality
  - Fix: strengthen MCP tool descriptions — highlight concrete advantages, unique data, context built-ins can't provide

**Sub-domain D2.2 — MCP Fundamentals**
- MCP = open protocol for connecting external systems to Claude
- Three primary resource types:
  1. **Tools** — functions the agent can call (CRUD operations, API calls, command execution)
  2. **Resources** — data the agent can read for context (documentation, schemas, catalogs)
  3. **Prompts** — predefined prompt templates for common tasks
- MCP server: a process that implements the protocol and provides tools/resources
- When connected: all tools are auto-discovered; all tools from all servers are available simultaneously
- Resource advantage: agent does NOT need exploratory tool calls to understand what data exists; a resource provides an immediate "map"

**Sub-domain D2.3 — MCP Server Configuration**
- Project configuration (`.mcp.json`) — stored at project root, version-controlled, for team usage:
  ```json
  {
    "mcpServers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
      }
    }
  }
  ```
- Environment variable substitution (`${GITHUB_TOKEN}`) — secrets are NOT committed
- User configuration (`~/.claude.json`) — personal/experimental servers; not VCS-shared
- Choosing servers: prefer existing community servers for standard integrations (Jira, GitHub, Slack); build custom only for unique team-specific workflows

**Sub-domain D2.4 — isError Structured Error Responses** ★ GAP
- When an MCP tool fails, it uses `isError: true` in the response
- ★ Two error channels (EXAM TRAP): a JSON-RPC **protocol error** = the request itself failed (unknown tool, bad args) → the JSON-RPC response IS an error; `isError: true` = a **tool-execution** error carried INSIDE a *successful* JSON-RPC response. Timeout → `isError: true`; unknown tool → protocol error.
- Structured error (good):
  ```json
  {
    "isError": true,
    "content": {
      "errorCategory": "transient",
      "isRetryable": true,
      "message": "Service temporarily unavailable. Timeout while calling orders API.",
      "attempted_query": "order_id=12345",
      "partial_results": null
    }
  }
  ```
- Generic error (anti-pattern): `{"isError": true, "content": "Operation failed"}` — agent has no information for decision-making
- Four error categories:
  - **Transient** (timeout, 503, network failure) → retry with exponential backoff
  - **Validation** (invalid input format, missing required field) → fix input and retry
  - **Business** (policy violation, threshold exceeded) → explain to user, propose alternative
  - **Permission** (access denied) → escalate
- Error-handling anti-patterns:
  - Generic status "search unavailable" → coordinator can't decide how to recover
  - Silent suppression (empty result treated as success) → coordinator thinks no matches, but it was a failure
  - Aborting whole workflow on one failure → lose all partial results
  - Infinite retries inside a subagent → latency and wasted resources
- Correct approach: local recovery (1–2 retries) for transient failures, then propagate to coordinator

**Sub-domain D2.5 — Tool Allocation and tool_choice** ★ GAP
- Too many tools per agent (e.g., 18 instead of 4–5) REDUCES tool selection reliability
- Agents with tools outside their specialization tend to misuse them
- Scoped tool access: only role-relevant tools plus limited cross-role utilities
- `tool_choice` strategies:
  - `"auto"` — model decides; default for most cases
  - `"any"` — model MUST call some tool; use when guaranteed structured output is required
  - `{"type": "tool", "name": "X"}` — model MUST call specific tool; use to guarantee execution order

**Sub-domain D2.6 — Built-in Tool Selection Guide** ★ GAP
- **Grep** — search within file contents (function names, error messages, imports)
- **Glob** — find files by name/extension patterns
- **Read** — full-file operations: load a file for analysis
- **Write** — create a new file from scratch
- **Edit** — precise changes via unique text matches; if Edit fails due to non-unique matches → fallback to Read + Write
- **Bash** — shell commands (git, npm, run tests, build)
- Incremental investigation strategy (do NOT read all files at once):
  1. Grep: find entry points (function definition, export)
  2. Read: read the found files
  3. Grep: find usages (import, calls)
  4. Read: read consumer files
  5. Repeat until complete picture

---

## Domain 5 — Context Management & Reliability (15%)

### Coverage of existing material
- context-management-reliability HTML: **Solid** — context window, accumulation, lost-in-middle, compaction
- prompt-caching-economics HTML: **Solid** — cache_control, breakpoint order, multipliers
- orchestrator-worker HTML: **Solid** — reliability patterns, failure modes, coverage annotations
- **Gaps:** Scratchpad files, structured state persistence for crash recovery, confidence calibration, provenance preservation details

### Complete topic list

**Sub-domain D5.1 — Context Window Composition and Risks**
- Context window includes: system prompt + full message history + tool definitions + tool results
- Three key context-window problems:
  1. **Lost-in-the-middle effect** — models reliably process info at start and end of long input; miss details in the middle. Mitigation: place key information near beginning or end.
  2. **Accumulation of tool results** — every tool call adds output. If tool returns 40+ fields but only 5 matter, most context is wasted.
  3. **Progressive summarization risk** — when compressing history, numeric values, percentages, and dates become vague ("about", "roughly", "a few")
- Why you must send full history on every API request: model has no persistent state between calls

**Sub-domain D5.2 — Extracting Facts and Trimming Results**
- Extract key facts into a persistent "case facts" block outside the summarized history:
  ```
  === CASE FACTS (updated whenever a new fact appears) ===
  Customer ID: CUST-12345
  Order Amount: $89.99
  Issue: Damaged item on delivery
  ===
  ```
- Include this block in every prompt regardless of how history is summarized
- Trimming tool results via `PostToolUse` hook: keep only relevant fields
  - Example: `lookup_order` returns 40+ fields; hook filters to 5 relevant ones
- Position-aware input: KEY FINDINGS at top, detailed results in middle, ACTION ITEMS at end

**Sub-domain D5.3 — Scratchpad Files and State Persistence** ★ GAP
- Scratchpad file pattern: agent writes key findings to a file during long investigations
  ```markdown
  ## Key findings
  - PaymentProcessor in src/payments/processor.ts inherits from BaseProcessor
  - refund() called from 3 places: OrderController, AdminPanel, CronJob
  - External PaymentGateway API rate limit: 100 req/min
  ```
- When context degrades or in a new session: agent consults scratchpad instead of re-running discovery
- Delegating to subagents to protect context:
  - Subagent reads 15 files, traces imports; returns 1-line summary to coordinator
  - Coordinator keeps ONE line instead of 15 files
- Structured state persistence for crash recovery:
  - Each agent exports state to a known location: `agent-state/{agent-id}.json`
  - Coordinator loads a manifest on resume: `agent-state/manifest.json` with status per agent
  - Fields: status, queries_executed, results_count, key_findings, gaps
- Constrained context budgets for subagents: send minimal context; structured return only; limit `allowed_tools`

**Sub-domain D5.4 — Confidence Calibration and Human Oversight** ★ GAP
- Field-level confidence scores: model outputs a confidence score per extracted field
- Calibration: use labeled validation sets to tune thresholds
- Routing based on confidence:
  - High confidence + stable accuracy → automated processing
  - Low confidence or ambiguous sources → human review
- Stratified random sampling: even for high-confidence extractions, regularly audit a sample
  - Why: aggregate 97% accuracy can hide 40% errors for a particular document type
  - Analyze accuracy by document type and field, not only overall

**Sub-domain D5.5 — Provenance Preservation** ★ GAP
- Attribution loss problem: claim → source link gets lost during summarization
- Structured claim-source mapping:
  ```json
  {
    "claim": "The AI music market is estimated at $3.2B.",
    "source_url": "https://example.com/report",
    "publication_date": "2024-06-15",
    "confidence": 0.9
  }
  ```
- Handling conflicting data: when two sources give different values, preserve BOTH with full attribution; never arbitrarily choose one
- Include publication dates: temporal differences misread as contradictions without dates
  - Bad: "Source A says 10%, source B says 15%. Contradiction."
  - Good: "Source A (2023) says 10%, source B (2024) says 15%. Likely +5% growth."
- Render content by type: financial data → tables; news/analysis → prose; technical findings → structured lists

---

## Integration Scenarios (Post-Domain Synthesis)

> **Reconciliation (with SESSION-PLAN Phase 6 and `practice/`):** there are THREE integration checkpoints. Customer Support is delivered early (Session 9 drill + Checkpoint A); Multi-Agent Research (Session 32 / Checkpoint C) and Conversational AI (Session 33 / Checkpoint B) are the two live Phase-6 sessions. Cross-domain mini-cases are ALSO embedded in every domain drill (Sessions 9/15/21/26/31). (The official exam has 6 scenarios; "Conversational AI" is our cross-domain integration exercise, not an official scenario.)

After all five domains are taught, three integration scenarios test cross-domain application:

| Scenario | Domains tested | Key skills tested |
|---|---|---|
| Customer Support Agent | D1 + D2 + D5 | Agentic loop, tool descriptions, escalation, context trimming, structured handoff |
| Multi-Agent Research System | D1 + D4 + D5 | Orchestration, provenance, batch API, error propagation, coverage annotations |
| Conversational AI Architecture | All 5 | Cross-domain synthesis; the hardest exam scenario type |

---

## Coverage Summary

| Domain | Weight | Existing HTML coverage | Professor sessions needed | Gap topics |
|---|---|---|---|---|
| D1 | 27% | ~55% | 7 teaching + 1 drill | Hooks, escalation, fork_session, handoff protocols |
| D3 | 20% | ~50% | 5 teaching + 1 drill | Skills frontmatter, CI/CD -p flag |
| D4 | 20% | ~50% | 6 teaching + 1 drill | Batch API, retry loops, multi-instance review |
| D2 | 18% | ~55% | 4 teaching + 1 drill | isError structured errors, tool count problem |
| D5 | 15% | ~65% | 4 teaching + 1 drill | Scratchpad, state persistence, confidence calibration |

**All gaps are covered by dedicated Professor sessions. No existing HTML is assigned as required reading.**

> **✅ Coverage confirmed against the official exam guide (`academy/CCA-F_Official-Exam-Guide_v0.1.pdf`):** all 5 domains and all **6** official scenarios are covered (Customer Support, Code Generation, Multi-Agent Research, Developer Productivity, Claude Code CI/CD, Structured Data Extraction). There is no Scenario 7 or 8 — the earlier community guide was wrong. (`SCENARIO-8_Agentic-AI-Tools.md` is retained only as optional Agent-SDK practice, NOT an exam scenario.)
