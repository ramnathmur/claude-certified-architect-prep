# Agent-SDK Tool Mechanics — OPTIONAL Supplementary Practice

> ⛔ **NOT AN OFFICIAL EXAM SCENARIO.** The official exam guide (`CCA-F_Official-Exam-Guide_v0.1.pdf`) confirms the exam has **6 scenarios** — there is no "Scenario 8 / Agentic AI Tools." The earlier community guide that listed 8 scenarios was wrong. This file is **retained only as optional extra practice** on Agent-SDK tool mechanics, which is genuinely tested under official **Domain 1 (Agentic Architecture)** and **Domain 2 (Tool Design & MCP)** — just not as a standalone scenario. It is NOT part of the readiness gate and does not affect Go/No-Go. Treat the items below as supplementary drills, not exam scenarios.

---

## 1. What Scenario 8 most plausibly tests

Scenario 8 appears to be the **tool / integration substrate of agent-building itself** — how an agent's tools are defined, named, scoped, permissioned, and wired (custom tools, MCP servers, hooks, Skills, subagents), independent of any single application domain. It is the "how do you *build and expose* the tools an agent uses" angle.

**How it differs from the tool/agent-adjacent scenarios:**

| Scenario | System being built | Primary lens |
|---|---|---|
| 3 — Multi-Agent Research | Coordinator delegates to named subagents to produce a cited report | **Orchestration** (fan-out/fan-in, aggregation) |
| 4 — Developer Productivity Tools | Agent helps engineers explore code / generate boilerplate / automate dev tasks | **Applying** the agent to software work |
| **8 — Agentic AI Tools** | The **tool & integration layer** — defining tools, wiring MCP, hooks, Skills, subagent config | **Tool design & agent mechanics** (the substrate) |

**Confidence:** the *name exists and candidates reported it* is documented fact; the *tool-mechanics focus* is reasoned inference. Treat as working hypothesis.

## 2. Domain stress map (this project's numbering)

This supplementary material draws on, in order (official domain numbering):
1. **D2 — Tool Design & MCP Integration (18%)** — most likely primary home (tool definitions, MCP wiring, `isError`, tool scoping).
2. **D1 — Agentic Architecture & Orchestration (27%)** — heavy overlap (agentic loop, subagents, `AgentDefinition`, when to fan out, hooks).
3. **D5 — Context Management & Reliability (15%)** — context isolation between agents, retry ownership, hooks for audit/reliability.
4. Lighter: **D3** (Skills, CLAUDE.md, permissions) and **D4** (structured output from tools).

**Implication for prep:** if Ram is solid on D1 + D4, Scenario 8 is mostly already covered. This module sharpens the specific mechanics below.

## 3. The mechanics to teach (doc-grounded, testable)

> Docs now live at `code.claude.com/docs` and `platform.claude.com/docs` (old `docs.anthropic.com` links redirect).

**Agent SDK vs Client SDK** — the Agent SDK is "Claude Code as a library"; it owns the agent loop + tool execution. With the raw Client SDK you hand-write the `while stop_reason == "tool_use"` loop yourself. Knowing which owns the loop is a likely question. *(Agent SDK Overview.)*

**Subagents & `AgentDefinition`** — the densest Scenario-8 vein:
- Key fields: `description` (required — drives auto-delegation), `prompt` (required), `tools` / `disallowedTools`, `model`, `skills`, `mcpServers`, `maxTurns`, `permissionMode`.
- **Context isolation (single most-tested fact):** a subagent starts fresh — it receives only its own system prompt + the spawn tool's prompt string (+ project CLAUDE.md). It does **NOT** inherit parent history, parent system prompt, or parent tool results. All context must be passed explicitly.
- **★ Version gotcha — the spawn tool was renamed `Task` → `Agent` in Claude Code v2.1.63.** Current SDKs emit `"Agent"` in `tool_use` blocks but still list `"Task"` in the `system:init` tools list. **Both names are correct depending on version** — a question may hinge on this. (Older materials, including parts of this academy, say "Task tool" — read it as "Task/Agent.")
- Benefits: context isolation, parallelization, specialized instructions, tool restriction (least privilege).

**Hooks** — `PreToolUse` (can inspect, block, or modify a call BEFORE it runs — use for hard governance/compliance) vs `PostToolUse` (transforms/observes a result AFTER — use for audit logging, normalization, trimming). Deterministic guarantee vs a prompt's probabilistic compliance. Also `Stop`, `SessionStart/End`, `UserPromptSubmit`.

**MCP wiring** — connect external systems (DBs, browsers, APIs) via `mcpServers`; tool names surface as `mcp__server__*`. `isError: true` is a tool-execution error inside a *successful* JSON-RPC response (distinct from a JSON-RPC protocol error). Prefer community MCP servers for standard integrations.

**Agent Skills** — `.claude/skills/*/SKILL.md`; auto-invoked or `/name`; packaged, reusable capabilities; can be preloaded into a subagent via `AgentDefinition.skills`. The modern replacement for legacy slash-commands.

**Managed Agents vs Agent SDK** — Agent SDK runs in *your* process/infra; Managed Agents = Anthropic-hosted REST API + sandbox. A plausible "which deployment model" question.

**Scaling beyond a few subagents** — turn-by-turn subagent delegation is the default; a script-driven workflow orchestrates dozens–hundreds of agents outside the conversation context when subagents don't scale.

## 4. Anti-patterns (high-yield)

- Letting an agent resolve genuine ambiguity autonomously instead of escalating / asking (the rewarded answer is usually clarify/escalate — the `AskUserQuestion` instinct).
- Assuming a subagent inherits the parent's history/tools — it does not.
- Giving a subagent every tool "just in case" (violates least privilege; degrades tool selection).
- Using a prompt instruction where a hook is required for a hard compliance/audit guarantee.
- Putting retry logic in the wrong layer — orchestration-level retries belong to the coordinator; local transient retries belong in the tool/subagent.
- Treating `isError: true` as a protocol failure (it is a tool-execution failure inside a successful response).

## 5. Practice questions (AUTHORED for inferred coverage — not real exam items)

> Use these in Session 33A. They follow the adjacent agentic-tool question patterns and are grounded in Agent SDK docs. Held-out from the mock banks. Verify framing against the live exam.

### S8-01 · Type: scenario · Difficulty: med
You're building an agent whose coordinator spawns a specialized "data-extraction" subagent in the Claude Agent SDK. The subagent keeps acting as if it has no idea what document to process. What is the correct fix?

A. Increase the coordinator's `max_tokens` so more history fits
B. Pass the document and task explicitly in the spawn tool's prompt — subagents do not inherit the parent's conversation history
C. Enable a shared-memory flag so the subagent reads the parent's transcript
D. Move the document into the coordinator's system prompt

### S8-02 · Type: recall · Difficulty: med
In recent Claude Code/SDK versions, which is true about the tool used to spawn a subagent?

A. It is always called `Task` in every version and surface
B. It was renamed from `Task` to `Agent` (v2.1.63); current SDKs emit `"Agent"` in tool_use but may still list `"Task"` in the init tools list
C. It was renamed from `Agent` to `Task`
D. Subagents cannot be spawned via a tool; only via CLAUDE.md

### S8-03 · Type: scenario · Difficulty: hard
A financial agent must guarantee that no `transfer_funds` call above $10,000 ever executes without a second approval. Where do you enforce this?

A. A strongly-worded instruction in the system prompt
B. A `PreToolUse` hook that inspects the call and blocks/redirects it before execution — deterministic, unlike a prompt
C. A `PostToolUse` hook that logs the transfer after it runs
D. A few-shot example showing the agent declining large transfers

### S8-04 · Type: anti-pattern · Difficulty: med
A subagent is configured with all 20 of the system's tools "so it's flexible." Tool selection has become unreliable. Best fix?

A. Add few-shot examples of correct tool choice to the subagent prompt
B. Scope the subagent's `tools` (or `disallowedTools`) to only the 3–5 it needs for its role — least privilege improves selection reliability
C. Switch the subagent to a larger model
D. Merge the 20 tools into one general-purpose tool

### S8-05 · Type: scenario · Difficulty: med
An MCP tool that calls an orders API returns `{"isError": true, "content": {...}}` with HTTP 200. How should the agent interpret this?

A. As a JSON-RPC protocol error — the request itself was malformed
B. As a tool-execution error reported inside a successful response — the tool ran but failed (e.g., timeout/business rule); decide retry vs escalate from the structured detail
C. As a network failure requiring a new MCP connection
D. As success, since the HTTP status is 200

### S8-06 · Type: concept · Difficulty: med
You want a reusable, packaged capability (multi-step procedure) that an agent — including a subagent — can invoke on demand. Which primitive fits best?

A. A CLAUDE.md section
B. An Agent Skill (`.claude/skills/*/SKILL.md`), optionally preloaded via `AgentDefinition.skills`
C. A `PostToolUse` hook
D. A larger system prompt

### S8-07 · Type: scenario · Difficulty: hard
Your team must run the agent inside your own VPC with full control of the runtime, libraries, and data path. Which deployment model fits?

A. Managed Agents (Anthropic-hosted REST API + sandbox)
B. The Agent SDK, which runs in your own process/infrastructure
C. The Batch API
D. The Client SDK with no agent loop

### S8-08 · Type: scenario · Difficulty: hard
In a coordinator → subagent design, a subagent's API call hits a transient 503. Where should retry logic live, and why?

A. Only in the coordinator, which should retry the entire subagent task from scratch
B. A local 1–2 retry with backoff inside the tool/subagent for the transient failure; escalate to the coordinator only if unresolved, with structured error context
C. Nowhere — fail the whole workflow on first error to stay deterministic
D. In a `PostToolUse` hook that re-invokes the tool indefinitely

## 6. Answer key

- **S8-01 — B.** Subagents have isolated context; all needed context must be in the spawn prompt. A/D don't address isolation; C misstates the model (no automatic transcript sharing).
- **S8-02 — B.** The `Task`→`Agent` rename (v2.1.63) with the init-list lag is the precise current fact. A ignores the rename; C reverses it; D is false.
- **S8-03 — B.** Hard financial/compliance rules need a deterministic `PreToolUse` block, not probabilistic prompt guidance (A/D) or after-the-fact logging (C).
- **S8-04 — B.** Least privilege (scoped `tools`) is the root-cause fix for unreliable selection. A adds tokens without fixing scope; C is costly and orthogonal; D creates a god-tool anti-pattern.
- **S8-05 — B.** `isError: true` in a 200 response is a tool-execution error, distinct from a JSON-RPC protocol error (A). C/D misread the channel.
- **S8-06 — B.** Skills are the packaged, on-demand, subagent-preloadable capability. A is always-on context; C is a lifecycle interceptor; D is unfocused.
- **S8-07 — B.** Agent SDK runs in your infrastructure (full control); Managed Agents (A) is Anthropic-hosted; C/D are not deployment models for a running agent.
- **S8-08 — B.** Local recovery for transient failures, escalate unresolved with structured context. A wastes work; C is brittle; D risks infinite retries / duplicates.

## 7. Sources & verification

Built from: Anthropic Agent SDK docs (Overview, Subagents, Hooks, Skills, MCP, Managed Agents), the `paullarionov/claude-certified-architect` guide (Scenario 8 placeholder), and adjacent agentic-tool patterns in the community `cca-f-mock-exam` repo. **Verify before relying on this:** the live exam's scenario list/count may differ (some post-launch reports claim a larger pool); confirm on the Skilljar exam page, and re-check version-sensitive facts (the Task/Agent rename, hook roster, SDK fields) against current docs.
