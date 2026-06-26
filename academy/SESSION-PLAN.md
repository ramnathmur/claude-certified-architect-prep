# CCA-F Session Delivery Plan

**Total sessions:** 37 (Phase 0–7; see Session Log Summary)
**Estimated total time:** ~29 hours
**Timeline at 1 session/day:** ~5 weeks | At 2 sessions/day: ~2.5 weeks

**Symbols:**
- ★ = concept not in existing HTML (gap-fill required; Professor must teach from scratch)
- [P] = Professor persona
- [EC] = Exam Coach persona

---

## Phase 0 — Orientation (1 session)

### Session 1 · Orientation + Baseline Diagnostic · [EC] · 30 min

**What happens:**
1. Exam logistics: 60 MCQs, 120 min, 720/1000 pass, `anthropic.skilljar.com`, Infosys partner free attempt (verify access first)
2. Domain weights reviewed and discussed
3. **Genuine cold diagnostic — 10 questions** (2 per domain, no hints), weighted toward D1 and D4, with at least 2 scenario/anti-pattern items. This, not a 5-question skim, is the real baseline — no mastery state in LEARNER-MODEL.md is trusted until it runs.
4. Results shared honestly and written to LEARNER-MODEL.md as the first genuine mastery reads → seeds the Reinforcement Queue.
5. **Adaptive-path decision:** if the learner already explains a concept cold (own words + correct diagnostic), the Professor may COMPRESS it to an assessment-first check instead of full teaching. Ram has 6+ months hands-on experience, so the 37-session path is a ceiling, not a floor — compress what's already known and reinvest the time in weak/gap concepts and held-out mocks. Never compress a concept the learner cannot explain cold.
6. **Set a provisional exam booking target date** right after the diagnostic, as a commitment device tied to the pass goal. Record it in PROGRESS.md (Completion Health).
7. Verify Skilljar/partner free attempt for Infosys employees before booking.

**No pre-read required.**

---

## Phase 1 — Domain 1: Agentic Architecture & Orchestration (27%)

### Session 2 · Agentic Loop Fundamentals · [P] · 35 min

**Topics taught by Professor:**
- API request anatomy: model, max_tokens, system, messages, tools, tool_choice
- Message roles: user, assistant, tool_result
- Why full history must be sent every request (model is stateless)
- The `stop_reason` field: `"end_turn"`, `"tool_use"`, `"max_tokens"`, `"stop_sequence"` — what each means and what you must do
- The correct completion signal: `stop_reason == "end_turn"` ONLY

**Teaching approach:** Opens with an analogy about sending letters to someone with amnesia. The model forgets everything between calls. This makes `stop_reason` the only communication channel.

---

### Session 3 · The Agentic Loop as a Pattern · [P] · 35 min

**Topics taught by Professor:**
- The full agentic loop: send → check stop_reason → execute tool → return result → loop → until end_turn
- Why this is model-driven (Claude decides next tool) vs hard-coded decision trees
- Anti-patterns:
  - Parsing assistant text for completion ("Task completed") → unreliable
  - Using `max_iterations=5` as primary stop condition → arbitrary
  - Checking for textual content as completion signal → wrong signal
- The ONLY reliable loop: continue when `"tool_use"`, stop when `"end_turn"`

**Teaching approach:** Analogy — a relay race where each runner decides who passes the baton next, based on who is closest to the finish. You don't pre-assign the handoffs.

---

### Session 4 · AgentDefinition + Hub-and-Spoke Architecture · [P] · 40 min

**Topics taught by Professor:**
- `AgentDefinition`: name, description, system_prompt, allowed_tools
- Principle of least privilege in tool assignment
- Hub-and-spoke topology: the coordinator owns everything
- What the coordinator is responsible for: decomposition, delegation, aggregation, error handling, user communication
- **Critical insight:** subagents have isolated context — they do NOT inherit the coordinator's history
- All required context must be explicitly passed in the subagent prompt
- All communication flows through the coordinator

**Teaching approach:** Analogy — a project manager who never lets two contractors talk to each other directly. Every update goes through the PM. Why? Observability, control, and error handling.

---

### Session 5 · The Task Tool and Explicit Context Passing · [P] · 35 min

**Topics taught by Professor:**
- `Task` tool: the mechanism for spawning subagents
- ★ Version note: the spawn tool was **renamed `Task` → `Agent` in Claude Code v2.1.63**. Current SDKs emit `"Agent"` in `tool_use` blocks but may still list `"Task"` in the `system:init` tools list — both names are correct depending on version. Read "Task" throughout this academy as "Task/Agent."
- Coordinator's `allowed_tools` must include `"Task"` (a.k.a. `"Agent"`)
- Explicit context passing — bad vs good:
  - Bad: `Task: "Analyze the document"` — subagent has no idea what document
  - Good: `Task: "Analyze the following document.\nDocument: [full text]\nPrior results: [...]\nOutput schema: [...]"`
- Parallel spawning: coordinator calls multiple Tasks in one response → all run concurrently
- Context budget discipline: send minimal context, require structured output, limit allowed_tools

**Teaching approach:** Analogy — briefing a freelancer. You can't say "do the design." You have to send the assets, the brief, the constraints, and the output format. Freelancers have no prior context.

---

### Session 6 · ★ Hooks: PreToolUse and PostToolUse · [P] · 40 min

**Topics taught by Professor:**
- What hooks are: interception points in the agent lifecycle
- `PostToolUse` hook: transforms a tool result BEFORE the model sees it
  - Example: normalize dates from three different MCP tools into ISO 8601
  - Example: trim 40-field order result to 5 relevant fields
- `PreToolUse` hook (outgoing-call interception): can inspect AND block a call before it executes
  - Example: block `process_refund` if amount > $500; redirect to `escalate_to_human` instead
- The fundamental distinction — hooks vs prompt instructions:
  - Hooks = **deterministic** (100% — code runs regardless of model reasoning)
  - Prompt instructions = **probabilistic** (>90% — model can still reason around them in edge cases)
- Rule: if failure has financial, legal, or safety consequences → hook, not prompt
- Examples of each category:
  - Hook territory: refund limits, PII filtering, compliance logging
  - Prompt territory: formatting preferences, general communication style
- ★ Beyond Pre/PostToolUse — the lifecycle has ~18 hook types; the exam may name `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `PreCompact`, `SubagentStart`/`SubagentStop`, `PermissionRequest`. You don't need all 18 in depth — just recognise that hooks span the WHOLE lifecycle, not only tool calls.
- ★ Hook permission outcomes: `allow` / `deny` / `ask` / `defer`. `defer` ENDS the query so it can be resumed later (distinct from `ask`, which pauses in-line for an answer). When multiple hooks fire for one event they run in parallel and the most restrictive wins: deny > defer > ask > allow.

**Teaching approach:** Analogy — a hotel concierge vs a hotel policy. The policy says "no pets." The concierge might forget to ask. The locked door doesn't forget. Hooks are the locked door.

---

### Session 7 · ★ Escalation Patterns and Structured Handoffs · [P] · 40 min

**Topics taught by Professor:**
- Three escalation patterns:
  1. **Immediate** — customer says "get me a manager" → escalate now, do not attempt to solve first
  2. **Attempt-then-escalate** — within scope; try resolution; if customer unsatisfied → escalate
  3. **Nuanced** — acknowledge emotion → propose concrete solution → escalate ONLY if customer reiterates desire for human
- Policy gap escalation: when policy is silent on the request → escalate (never guess or invent policy)
- Multiple customer matches: ask for additional identifiers; never heuristically pick one
- Unreliable escalation triggers (exam trap):
  - Sentiment analysis — mood does not predict case complexity
  - Model self-rated confidence (1–10) — model can be confidently wrong; calibration is poor
  - Automated classifier — overengineering; may require training data you don't have
- Structured handoff protocol — what must be in the escalation summary:
  - customer_id, customer_name, issue_summary, order_id, root_cause, actions_taken, refund_amount, recommended_action, escalation_reason
  - Why: human operator sees ONLY this summary, not the conversation transcript

**Teaching approach:** Analogy — a doctor handing off a patient to a specialist. The referral letter must be complete. "Patient has a problem" is not a referral. The specialist has no context and cannot ask follow-up questions.

---

### Session 8 · ★ Session Management + Task Decomposition · [P] · 35 min

**Topics taught by Professor:**
- `--resume <session-name>`: resumes a named session with saved context
  - Risk: if files changed since the prior session, tool results are stale
- `fork_session`: creates an independent branch from shared context at a point in time
  - Use case: "Let's try Redux vs Context API from where we are now" — both forks inherit up to the branch point
- When to resume vs start fresh:
  - Resume: files unchanged, results still valid
  - Fresh start: results stale, time passed — better to summarize and restart ("Here is what we found: ...")
- Fixed pipelines (prompt chaining): steps defined in advance; use for predictable repeatable tasks
- Dynamic adaptive decomposition: subtasks generated from intermediate results; use for open-ended investigations
- Multi-pass code review: why one pass over 14 files fails (attention dilution, inconsistent flags, missed bugs); correct approach is per-file passes then one integration pass

---

### Session 9 · Domain 1 Comprehension Check + Scenario Drill · [P → EC] · 45 min

**Comprehension check [P] — 3 cold questions (no hints):**
1. Your agent called `process_refund` in 8% of cases without first verifying the customer. What is the most effective fix and why?
2. A subagent needs to analyze a document. Write the correct Task invocation vs the wrong one.
3. Your escalation rate is 60% but target is 20%. The prompt says "try to solve before escalating." What's the structural problem?

**Scenario drill [EC] — Customer Support Agent (15 min):**
Full scenario presented. Learner proposes decisions. Structured feedback. Then 5 exam-style MCQs.

---

## Phase 2 — Domain 3: Claude Code Configuration & Workflows (20%)

### Session 10 · CLAUDE.md Hierarchy and @path Imports · [P] · 35 min

**Topics taught by Professor:**
- Three-level hierarchy: user (`~/.claude/CLAUDE.md`), project (`.claude/CLAUDE.md`), directory (`subdir/CLAUDE.md`)
- What each level governs and who it applies to
- Common team failure: new team member misses project coding standards because they're in the user-level file
- `@path` syntax: `@./standards/coding-style.md` — relative path, no space after `@`, max 5 nesting levels
- Use case for `@path`: monorepo where each package CLAUDE.md imports only its relevant standards

---

### Session 11 · Path-Specific Rules and Conditional Loading · [P] · 30 min

**Topics taught by Professor:**
- `.claude/rules/` directory: topic-organized rule files instead of one monolithic CLAUDE.md
- YAML frontmatter with `paths:` key:
  - Rule only loads when editing a file matching the glob pattern
  - Saves context and tokens — irrelevant rules are not loaded
  - Example: `paths: ["**/*.test.tsx", "**/*.test.ts"]` — test-only rules
- Decision rule: use `paths:` rules for conventions that span many directories (tests, migrations); use directory CLAUDE.md for conventions tied to one specific directory

---

### Session 12 · ★ Skills: context:fork, allowed-tools, argument-hint · [P] · 40 min

**Topics taught by Professor:**
- Two slash command formats:
  - `.claude/commands/review.md` → `/review` (legacy, supported)
  - `.claude/skills/review/SKILL.md` → `/review` (current)
- Project vs user scope: project commands in `.claude/` are VCS-shared; user commands in `~/.claude/` are personal
- SKILL.md frontmatter parameters:
  - `context: fork` — runs skill in an isolated subagent; verbose output does NOT pollute main session
  - `allowed-tools: ["Read", "Grep", "Glob"]` — ★ EXAM TRAP: this **pre-approves** (auto-approves) the listed tools while the skill is active; it does NOT restrict the others. Every other tool stays callable, subject to existing permission settings. The name sounds restrictive but the behaviour is permissive. To actually REMOVE tools, use `disallowed-tools` (which clears on the next user message).
  - `disable-model-invocation: true` / `user-invocable: false` — control who can fire the skill (user-only vs Claude-only); `disable-model-invocation` also keeps the skill out of subagent preload
  - `argument-hint: "Path to the directory to analyze"` — prompts the user when no argument given
- When skill vs CLAUDE.md: skill = on-demand invocation; CLAUDE.md = always-loaded standards
- Personal variants: create under a different name in `~/.claude/skills/` to avoid affecting teammates

---

### Session 13 · Planning Mode, Explore Subagent, /compact, /memory · [P] · 30 min

**Topics taught by Professor:**
- Planning mode: investigation-only; no changes; produces an approved plan first
  - When to use: large changes (dozens of files), multiple viable approaches, architectural decisions, unfamiliar codebase
  - Combined approach: plan → approve → direct execution
- Explore subagent: isolates verbose discovery output; returns only a summary to the main agent
  - Why: prevents context-window exhaustion in multi-phase tasks
- `/compact`: compresses prior history; risk is loss of exact numbers and dates
- `/memory`: opens CLAUDE.md for editing; persists notes across sessions

---

### Session 14 · ★ Claude Code CLI for CI/CD · [P] · 35 min

**Topics taught by Professor:**
- The `-p` / `--print` flag: non-interactive mode; the ONLY correct way to use Claude in CI pipelines
- ★ The `--bare` flag (EXAM TRAP): `-p` alone STILL auto-loads all local config — hooks, CLAUDE.md, skills, plugins, MCP servers, auto-memory. `--bare` SKIPS all of it. So `claude -p "..."` is NOT equivalent to `claude -p --bare "..."`. `--bare` is the recommended mode for scripted/SDK calls and is slated to become the default for `-p` in a future release. If a CI question hinges on "why did my pipeline pick up an unexpected CLAUDE.md rule / hook?", the answer is the missing `--bare`.
- `--output-format json` + `--json-schema`: structured output for automated processing (inline PR comments)
- Session context isolation: the Claude instance that generated code is less effective at reviewing it
  - Why: the model retains its reasoning context and is unlikely to challenge its own decisions
  - Fix: use an independent Claude instance for review
- Preventing duplicate comments on re-review: include prior review results in context; report only new or unresolved issues

---

### Session 15 · Domain 3 Comprehension Check + Scenario Drill · [P → EC] · 35 min

**Comprehension check [P] — 3 cold questions:**
1. A new team member joined and is not getting the project's coding standards. Where did those standards likely get stored, and where should they be?
2. You have test-convention rules that apply to test files in 8 different packages. Which mechanism is best: directory CLAUDE.md per package or a single `.claude/rules/` file with `paths:`?
3. Your CI/CD pipeline hangs waiting for user input when running Claude. What flag is missing?

**Scenario drill [EC] — Claude Code CI Pipeline (15 min):**
Full scenario. Learner proposes architecture. 5 MCQs.

---

## Phase 3 — Domain 4: Prompt Engineering & Structured Output (20%)

### Session 16 · Few-Shot Prompting and Explicit Criteria · [P] · 40 min

**Topics taught by Professor:**
- Why examples beat textual descriptions: they demonstrate decision logic, not just format
- The 5 types of few-shot examples with worked examples for each
- Explicit criteria vs vague instructions: "flag ONLY if" vs "be conservative"
- Defining severity levels with code examples per level
- The false-positive effect on developer trust: high FP in one category destroys trust in accurate categories
- Prompt chaining: breaking complex tasks into focused sequential steps; prevents attention dilution

---

### Session 17 · tool_use with JSON Schemas · [P] · 40 min

**Topics taught by Professor:**
- `tool_use` + JSON schema = the most reliable structured output mechanism
- What it guarantees: syntactically valid JSON, required fields present
- What it does NOT guarantee: semantic correctness (values can still be wrong)
- Schema design rules:
  - `required` only for fields that are ALWAYS available
  - `"type": ["string", "null"]` for optional information
  - Enums with `"other"` + detail string
  - Enum `"unclear"` for ambiguous cases
- `tool_choice`: auto (default), any (guaranteed tool call), specific (forced first action)
- Syntax vs semantic errors: what tool_use eliminates vs what still requires validation

---

### Session 18 · ★ Validation, Retry-with-Feedback, Self-Correction · [P] · 40 min

**Topics taught by Professor:**
- The retry-with-feedback pattern: what to include in the retry prompt
  - Original document + previous extraction + specific error: "Field 'total' = $150 but sum(items) = $145"
- When retry helps: format errors, structural errors, arithmetic inconsistencies
- When retry will NOT help: information absent from source; context in a different document
- Pydantic: structural validation + semantic validation + JSON Schema generation for tool_use
- Self-correction pattern: extract `stated_total` AND `calculated_total`; flag `conflict_detected: true` when they differ

---

### Session 19 · ★ Message Batches API · [P] · 30 min

**Topics taught by Professor:**
- 50% cost savings vs synchronous calls
- Up to 24-hour processing window — no latency SLA guarantee
- Multi-turn tool calling: NOT supported in Batch API
- `custom_id`: links request to response; enables targeted re-submission of failed documents
- Synchronous vs batch: decision table (pre-merge check → sync; overnight audit → batch; 10,000 documents → batch)
- SLA planning: 30-hour deadline, 24-hour max processing → must submit within 6 hours of target time
- Failure handling: identify failures by custom_id; modify strategy; re-submit only failures

---

### Session 20 · ★ Multi-Instance Review and The Interview Pattern · [P] · 30 min

**Topics taught by Professor:**
- Self-review limitation: generating model is biased toward its own reasoning; unlikely to find its own mistakes
- Independent review instance: no access to generation context; finds subtle issues the generating instance misses
- Multi-pass review architecture: per-file analysis (parallel) + cross-file integration pass (sequential)
- Verification passes with self-rated confidence to route reviews calibrated to uncertainty
- The "interview" pattern: Claude asks clarifying questions before implementing
  - When to use: unfamiliar domain, tasks with non-obvious implications, multiple viable approaches

---

### Session 21 · Domain 4 Comprehension Check + Scenario Drill · [P → EC] · 35 min

**Comprehension check [P] — 3 cold questions:**
1. Your extraction tool returns `{"category": "unclear"}` but you need a more specific value. What are two different interventions, and when is each appropriate?
2. You're processing 5,000 invoices nightly. Each invoice extraction takes 4 seconds synchronously. What's the better approach and why?
3. A validation check shows `stated_total = $150` but `sum(line_items) = $145`. What schema design enables detecting this automatically?

**Scenario drill [EC] — Structured Data Extraction (15 min):**
Full scenario. Learner proposes design. 5 MCQs.

---

## Phase 4 — Domain 2: Tool Design & MCP Integration (18%)

### Session 22 · ★ Tool Description as the Selection Mechanism · [P] · 40 min

**Topics taught by Professor:**
- The description is the PRIMARY mechanism Claude uses to select tools — not the name, not the schema
- What happens with minimal descriptions: tool overlap → misrouting → wrong calls
- What a good description must include:
  - What it does and returns
  - Input formats and example values
  - Edge cases and constraints
  - When to use THIS tool vs similar alternatives
- Common failure: `analyze_content` and `analyze_document` with near-identical descriptions
- Fix: rename + differentiate: `extract_web_results` vs `extract_document_text` with explicit "use this when..."
- System prompt unintended associations: "always verify the customer" → model overuses `get_customer`
- Built-in vs MCP tool preference: agents prefer Read/Grep over MCP tools with similar names → strengthen MCP descriptions

---

### Session 23 · MCP Architecture and Server Configuration · [P] · 35 min

**Topics taught by Professor:**
- MCP three primitives: tools (actions), resources (read-only context), prompts (templates)
- MCP resources: the "map" that eliminates exploratory tool calls — catalog of available data
- Server auto-discovery: all tools from all connected servers become available on connection
- `.mcp.json` (project, VCS-tracked, team-shared) vs `~/.claude.json` (user, personal)
- Environment variable substitution in `.mcp.json` for secret management
- Community servers vs custom: prefer community for standard integrations; build custom only for unique workflows

---

### Session 24 · ★ isError Structured Errors and Tool Allocation · [P] · 35 min

**Topics taught by Professor:**
- `isError: true` signal in MCP responses
- ★ EXAM TRAP — two different error channels: (1) a JSON-RPC **protocol error** means the request itself failed (unknown tool, malformed args) and the JSON-RPC response IS an error; (2) `isError: true` is a **tool-execution** error that lives INSIDE a *successful* (HTTP 200, valid JSON-RPC) response body. A timed-out orders API → `isError: true` in a good response. A call to a tool that doesn't exist → JSON-RPC protocol error. Knowing which channel carries which failure is the architect-level distinction.
- Four error categories with correct agent response for each:
  - Transient → retry with backoff
  - Validation → fix input, retry
  - Business → explain to user, propose alternative
  - Permission → escalate
- The generic error anti-pattern: "Operation failed" — agent has no information for recovery
- Anti-patterns: silent suppression (empty = success), aborting whole workflow on one failure, infinite retries in subagent
- Tool count problem: 18 tools → model cannot reliably distinguish among them; 4–5 = reliable
- Local recovery: subagent tries 1–2 times for transient errors; propagates structured error (with partial results) if unresolved

---

### Session 25 · Built-in Tool Selection and Incremental Investigation · [P] · 30 min

**Topics taught by Professor:**
- When to use each built-in tool:
  - Grep: searching content inside files
  - Glob: finding files by name/pattern
  - Read: loading a full file
  - Write: creating a new file
  - Edit: targeted change via unique text match
  - Bash: shell commands (git, npm, tests, build)
- Edit fallback: if Edit fails (non-unique match) → Read + modify programmatically + Write
- Incremental investigation strategy: Grep entry points → Read → Grep usages → Read consumers → repeat

---

### Session 26 · Domain 2 Comprehension Check + Scenario Drill · [P → EC] · 35 min

**Comprehension check [P] — 3 cold questions:**
1. You have two MCP tools: `get_customer_profile` and `get_customer_data`. Agents are calling the wrong one. What is the root cause and the correct fix?
2. An MCP tool returns `{"isError": true, "content": "database unavailable"}`. What is wrong with this response and how should it be structured?
3. You're building a subagent with 15 tools. What problem does this create and what is the correct pattern?

**Scenario drill [EC] — Tool Design Decisions (15 min):**
Full scenario. Learner proposes redesign. 5 MCQs.

---

## Phase 5 — Domain 5: Context Management & Reliability (15%)

### Session 27 · Context Window Risks and Lost-in-the-Middle · [P] · 35 min

**Topics taught by Professor:**
- Context window composition: system prompt + history + tool definitions + tool results = total
- Lost-in-the-middle effect: start and end are reliable; middle gets skipped
  - Mitigation: key findings at the top, action items at the bottom
- Progressive summarization risk: what gets lost (exact numbers, dates, percentages → "about", "roughly")
- Tool result accumulation: 40 fields returned, 5 needed → 35 fields wasted context per call
- Why full history must be sent on every request: stateless model

---

### Session 28 · Trimming, Persistent Fact Blocks, and Position-Aware Input · [P] · 30 min

**Topics taught by Professor:**
- `PostToolUse` hook for trimming: keep only relevant fields before model consumes result
- Persistent "case facts" block: extracted key facts maintained outside summarized history
  - Template: `=== CASE FACTS === Customer ID: ... Order Amount: ... Issue: ... ===`
  - Include in every prompt regardless of how history is summarized
- Position-aware input structure: KEY FINDINGS at top (never in middle), DETAILS in middle, ACTION ITEMS at end

---

### Session 29 · ★ Scratchpad Files and Structured State Persistence · [P] · 35 min

**Topics taught by Professor:**
- Scratchpad file pattern: agent writes `investigation-scratchpad.md` with key findings during long sessions
  - On context degradation: consult scratchpad instead of re-running discovery
- Delegating to subagents to protect context: subagent reads 15 files, returns 1 summary line to coordinator
  - Coordinator keeps summary; not 15 files
- Structured state persistence for crash recovery:
  - `agent-state/{agent-id}.json`: status, queries_executed, key_findings, gaps
  - `agent-state/manifest.json`: coordinator loads this on resume to know which agents completed
- Constrained context budgets for subagents: minimal context in, structured output out, limited tool scope

---

### Session 30 · ★ Confidence Calibration, Provenance, and Human Oversight · [P] · 35 min

**Topics taught by Professor:**
- Field-level confidence scores per extracted value; thresholds calibrated with labeled validation sets
- Routing based on confidence: high confidence → automate; low confidence → human review
- Stratified random sampling: audit high-confidence extractions to detect failure modes in specific document types
- Provenance — "claim → source" structured mappings must be preserved through aggregation
- Attribution loss problem: how claim-source links get lost during summarization
- Conflicting data: preserve BOTH values with full attribution; never choose arbitrarily
- Publication dates: include to avoid misreading temporal change as contradiction

---

### Session 31 · Domain 5 Comprehension Check + Scenario Drill · [P → EC] · 35 min

**Comprehension check [P] — 3 cold questions:**
1. A long investigation session has run for 3 hours. The agent starts giving vague answers like "there are some authentication methods used." What caused this and what should you have done?
2. Your system shows 97% aggregate extraction accuracy. Why might this still be dangerous? What's the right metric approach?
3. Your multi-agent research report will be read by an executive. Source A says 12%, Source B says 8% for the same metric. How should your agent handle this in the output?

**Scenario drill [EC] — Reliability and Recovery (15 min):**
Full scenario. 5 MCQs.

---

## Phase 6 — Cross-Domain Integration

> **Integration coverage = 3 scenarios, delivered in two places (reconciled with `CURRICULUM.md` and `practice/`):** Customer Support (D1×D5) is delivered earlier as the Session 9 drill + practice Checkpoint A; Multi-Agent Research (Session 32 / Checkpoint C) and a Conversational-AI cross-domain integration (Session 33 / Checkpoint B) are the two Phase-6 integration sessions below. Cross-domain mini-cases are ALSO embedded in every domain drill (Sessions 9/15/21/26/31). (Note: the official exam has 6 scenarios — "Conversational AI" is our cross-domain integration exercise, not an official scenario.)

### Session 32 · Integration Scenario A: Multi-Agent Research System · [EC] · 45 min

**Domains tested:** D1 + D4 + D5
**Topics under test:** Coordinator-subagent delegation, explicit context passing, provenance preservation, error propagation, coverage annotations, batch API, self-correction

Full multi-page scenario. Learner works through decisions. 8 MCQs. Exam Coach scores by domain and identifies weak spots.

---

### Session 33 · Integration Scenario B: Conversational AI Architecture · [EC] · 45 min

**Domains tested:** All 5
**Topics under test:** Context window management, instruction persistence across turns, memory strategies, tool design for safe execution, escalation when ambiguity arises, hooks for compliance enforcement

This is the hardest integration scenario type. All 5 domains must compose correctly. 8 MCQs.

---

### Session 34 · Gap Remediation (conditional) · [P or EC] · Variable

**What happens:** Based on Scenarios A and B performance, Exam Coach identifies the two weakest domain areas. Professor re-teaches those specific sub-topics. Exam Coach runs a targeted 10-question drill.

**Skip if:** Both integration scenarios passed with strong performance.

---

## Phase 7 — Mock Exams and Go/No-Go

### Session 35 · Mock Exam #1 · [EC] · 120 min

60 questions, timed, **held-out** (no reuse of taught examples or `practice/` bank items), **scenario-balanced** across the 6 scenarios. **Prefer the official Skilljar practice exam** (it exists — same scenarios/format as the real exam); otherwise use the held-out bank authored for this purpose (see the PROGRESS.md build task). No assistance, no discussion during exam.
After exam: Exam Coach produces a domain-AND-scenario gap report scored against the Go/No-Go floors (≥720 total, no domain <70%, no scenario <70%).

---

### Session 36 · Mock #1 Analysis + Targeted Re-Drill · [P + EC] · 45 min

Professor re-teaches the 2–3 specific sub-topics where Mock #1 showed weakest performance.
Exam Coach runs a 15-question targeted drill on those sub-topics.

---

### Session 37 · Mock Exam #2 + Go/No-Go Decision · [EC] · 130 min

60 questions, timed, **fresh and held-out** — no item reused from teaching, drills, the practice banks, or Mock #1. Scenario-balanced across all 6 scenarios.
After exam, apply the full Go/No-Go gate (see ENGAGEMENT-PROTOCOL.md): book ONLY if scaled-equivalent ≥ 720 AND no domain < 70% AND no scenario family < 70%. A passing total with a failing floor → targeted remediation on that segment, then re-test it. Below 720 → plan one more remediation cycle.

---

## Session Log Summary

| Phase | Sessions | Personas | Est. time |
|---|---|---|---|
| Orientation | 1 | EC | 30 min |
| D1 Teaching | 7 | P | ~270 min |
| D1 Drill | 1 | P+EC | 45 min |
| D3 Teaching | 5 | P | ~170 min |
| D3 Drill | 1 | P+EC | 35 min |
| D4 Teaching | 6 | P | ~210 min |
| D4 Drill | 1 | P+EC | 35 min |
| D2 Teaching | 4 | P | ~140 min |
| D2 Drill | 1 | P+EC | 35 min |
| D5 Teaching | 4 | P | ~135 min |
| D5 Drill | 1 | P+EC | 35 min |
| Integration | 2–3 | EC | ~90 min |
| Mock Exams | 3 | EC | ~295 min |
| **Total** | **37** | | **~29 hrs** |
