# Ground-Truth Research Notes — S-E2: Subagents as a Programmable Primitive (CLI → Agent SDK)

**Manifest**
- **Date compiled:** 2026-06-05 · **Re-verified 2026-06-09** ([VERIFY] #4 resolved — no per-turn cap outside Workflow; additive drifts in the addendum at the end. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
- **Extension:** S-E2 (builds on "Introduction to Subagents" base + S-E1 five orchestration patterns)
- **CCA-F Domains reinforced:** Domain 1 — Agentic Architecture & Orchestration (27%, primary); Domain 2 — Claude Code Configuration (20%, secondary)
- **Naming caveat:** The "Claude Agent SDK" was formerly the "Claude Code SDK"; renamed to reflect non-coding use (source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk). `docs.anthropic.com` and `platform.claude.com/docs/en/agent-sdk/*` now 307-redirect to `code.claude.com/docs/en/agent-sdk/*`; the `anthropic.com/engineering/*` posts 308-redirect to `claude.com/blog/*`. Cite the live hosts.

**Flat source list (every URL used):**
1. https://code.claude.com/docs/en/agent-sdk/subagents
2. https://code.claude.com/docs/en/agent-sdk/typescript
3. https://code.claude.com/docs/en/agent-sdk/python
4. https://code.claude.com/docs/en/sub-agents
5. https://code.claude.com/docs/en/workflows
6. https://claude.com/blog/building-agents-with-the-claude-agent-sdk
7. https://www.anthropic.com/engineering/building-effective-agents

---

## 1. The `AgentDefinition` object — every field [D1 primary / D2 secondary]

**Mechanism.** A subagent is declared as an `AgentDefinition`: a record/dataclass holding the subagent's routing description, system prompt, tool allow-list, model, and operational flags. The orchestrator decides whether to invoke it based on the `description` field (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Exact TypeScript shape (verbatim from the TS reference):**

```typescript
type AgentDefinition = {
  description: string;
  tools?: string[];
  disallowedTools?: string[];
  prompt: string;
  model?: string;
  mcpServers?: AgentMcpServerSpec[];
  skills?: string[];
  initialPrompt?: string;
  maxTurns?: number;
  background?: boolean;
  memory?: "user" | "project" | "local";
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | number;
  permissionMode?: PermissionMode;
  criticalSystemReminder_EXPERIMENTAL?: string;
};
```
(source: https://code.claude.com/docs/en/agent-sdk/typescript)

**Exact Python shape (verbatim from the Python reference):**

```python
@dataclass
class AgentDefinition:
    description: str
    prompt: str
    tools: list[str] | None = None
    disallowedTools: list[str] | None = None
    model: str | None = None
    skills: list[str] | None = None
    memory: Literal["user", "project", "local"] | None = None
    mcpServers: list[str | dict[str, Any]] | None = None
    initialPrompt: str | None = None
    maxTurns: int | None = None
    background: bool | None = None
    effort: EffortLevel | int | None = None
    permissionMode: PermissionMode | None = None
```
(source: https://code.claude.com/docs/en/agent-sdk/python)

**CRITICAL Python gotcha — camelCase fields.** `AgentDefinition` field names use **camelCase** (`disallowedTools`, `permissionMode`, `maxTurns`, `initialPrompt`) to match the wire format shared with the TS SDK. This differs from `ClaudeAgentOptions`, which uses Python snake_case (`disallowed_tools`, `permission_mode`). "Because `AgentDefinition` is a dataclass, passing a snake_case keyword raises a `TypeError` at construction time." (source: https://code.claude.com/docs/en/agent-sdk/python)

**Field-by-field (from the subagents doc table):**

| Field | Type | Required | Meaning |
|---|---|---|---|
| `description` | `string` | **Yes** | Natural-language description of *when to use* this agent; drives orchestrator routing |
| `prompt` | `string` | **Yes** | The subagent's system prompt (role + behavior) |
| `tools` | `string[]` | No | Allow-list of tool names. **If omitted, inherits all tools** |
| `disallowedTools` | `string[]` | No | Tool names to remove from the agent's set |
| `model` | `string` | No | Override: alias `'sonnet'`/`'opus'`/`'haiku'`/`'inherit'`, or full model ID (e.g. `claude-opus-4-8`). Defaults to main model if omitted |
| `skills` | `string[]` | No | Skill names to **preload** into context at startup; unlisted skills still invocable via Skill tool |
| `memory` | `'user'\|'project'\|'local'` | No | Persistent-memory source/scope for this agent |
| `mcpServers` | `(string\|object)[]` | No | MCP servers by name or inline config |
| `maxTurns` | `number` | No | Max agentic turns before the agent stops |
| `background` | `boolean` | No | Run as non-blocking background task when invoked |
| `effort` | `'low'\|'medium'\|'high'\|'xhigh'\|'max'\|number` | No | Reasoning-effort level |
| `permissionMode` | `PermissionMode` | No | Permission mode for tool execution within this agent |
| `initialPrompt` (TS/Py only) | `string` | No | Auto-submitted as first user turn **when the agent runs as the main thread** (via `--agent` / `agent` setting) |
| `criticalSystemReminder_EXPERIMENTAL` (TS) | `string` | No | Experimental critical reminder appended to system prompt |

(table source: https://code.claude.com/docs/en/agent-sdk/subagents; `initialPrompt`/`criticalSystemReminder_EXPERIMENTAL` source: https://code.claude.com/docs/en/agent-sdk/typescript)

> Note: the SDK subagents doc lists `background` and `effort`; the base scope asked about `mode`/`source` — **there is no `mode` or `source` field** in the current `AgentDefinition`. The closest analogs are `permissionMode` (tool-permission mode) and, at the filesystem level, the scope/location of the definition file. [VERIFY — see list.]

**When to use.** Use `AgentDefinition` for SDK applications where you want subagents created/parameterized in code (this is the documented recommended approach for SDK apps) (source: https://code.claude.com/docs/en/agent-sdk/subagents).

---

## 2. The `agents` parameter — passing programmatic subagents [D1 primary / D2 secondary]

**Mechanism.** Subagents can be created three ways: **programmatically** (the `agents` parameter in `query()` options — recommended for SDK apps), **filesystem-based** (`.claude/agents/*.md`), or via the **built-in `general-purpose`** subagent Claude can invoke without any definition (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Exact `agents` type.** On the TS `Options`: `agents?: Record<string, AgentDefinition>` (source: https://code.claude.com/docs/en/agent-sdk/typescript). On Python `ClaudeAgentOptions`: `agents: dict[str, AgentDefinition] | None = None` ("Programmatically defined subagents") (source: https://code.claude.com/docs/en/agent-sdk/python). The **key is the agent's name**; the value is its definition.

**Verbatim invocation example (Python):**

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Review the authentication module for security issues",
        options=ClaudeAgentOptions(
            # Auto-approve these tools, including Agent for subagent invocation
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            agents={
                "code-reviewer": AgentDefinition(
                    description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                    prompt="""You are a code review specialist...""",
                    tools=["Read", "Grep", "Glob"],
                    model="sonnet",
                ),
                "test-runner": AgentDefinition(
                    description="Runs and analyzes test suites. Use for test execution and coverage analysis.",
                    prompt="""You are a test execution specialist...""",
                    tools=["Bash", "Read", "Grep"],
                ),
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```
(source: https://code.claude.com/docs/en/agent-sdk/subagents)

**TS equivalent** uses `allowedTools: [..., "Agent"]` and `agents: { "code-reviewer": { description, prompt, tools, model } }` (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Precedence — programmatic vs. filesystem.** "**Programmatically defined agents take precedence over filesystem-based agents with the same name.**" (source: https://code.claude.com/docs/en/agent-sdk/subagents). The full filesystem scope precedence ladder (highest→lowest): Managed settings → `--agents` CLI flag → `.claude/agents/` (project) → `~/.claude/agents/` (user) → plugin `agents/` (source: https://code.claude.com/docs/en/sub-agents).

**When to use each.** Programmatic = SDK apps, dynamic/runtime-parameterized agents (e.g. a factory returning a stricter agent with a more capable model) (source: https://code.claude.com/docs/en/agent-sdk/subagents). Filesystem = reusable, version-controlled team agents, complex/long prompts (also a Windows workaround: long programmatic prompts can hit the 8191-char command-line limit; use file-based instead) (source: https://code.claude.com/docs/en/agent-sdk/subagents).

---

## 3. Runtime invocation — delegation via the Agent (formerly Task) tool [D1 primary]

**Mechanism.** The main agent delegates by calling the **`Agent` tool** (built-in subagent/Task tool). The subagent then runs in **its own fresh conversation**; "Intermediate tool calls and results stay inside the subagent; **only its final message returns to the parent**." (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Tool renamed Task → Agent.** "The tool name was renamed from `"Task"` to `"Agent"` in Claude Code v2.1.63." Current SDK releases emit `"Agent"` in `tool_use` blocks but still use `"Task"` in the `system:init` tools list and in `result.permission_denials[].tool_name` — check both `"Task"` and `"Agent"` for compatibility (source: https://code.claude.com/docs/en/agent-sdk/subagents). At the filesystem/CLI level: "In version 2.1.63, the Task tool was renamed to Agent. Existing `Task(...)` references in settings and agent definitions still work as aliases." (source: https://code.claude.com/docs/en/sub-agents).

**To auto-approve delegation, include `Agent` in `allowedTools`.** Without it, Agent invocations fall through to the `canUseTool` callback, or are denied in `dontAsk` mode — a common cause of "Claude won't delegate" (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Automatic vs. explicit invocation.** Automatic: Claude matches the task to a subagent's `description`. Explicit: name it in the prompt — e.g. `"Use the code-reviewer agent to check the authentication module"` — which bypasses automatic matching (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Detection.** Subagent invocations appear as `tool_use` blocks where `name` is `"Agent"` (or legacy `"Task"`); messages originating inside a subagent carry a `parent_tool_use_id` field; `block.input.subagent_type` names the agent (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**"Fresh but not empty."** The subagent's context starts fresh (no parent history) but inherits its own system prompt + the Agent tool's prompt string, project CLAUDE.md (via `settingSources`), and tool definitions per its definition (source: https://code.claude.com/docs/en/agent-sdk/subagents). See §4 inheritance table below.

---

## 4. The prompt string is the ONLY channel into a subagent [D1 primary]

**Mechanism.** "The only channel from parent to subagent is the Agent tool's prompt string, so include any file paths, error messages, or decisions the subagent needs directly in that prompt." (source: https://code.claude.com/docs/en/agent-sdk/subagents). There is no shared memory between parent and subagent within a single delegation.

**What the subagent receives vs. does NOT receive (verbatim table):**

| The subagent **receives** | The subagent **does not receive** |
|---|---|
| Its own system prompt (`AgentDefinition.prompt`) + the Agent tool's prompt | The parent's conversation history or tool results |
| Project CLAUDE.md (loaded via `settingSources`) | Preloaded skill content, unless listed in `AgentDefinition.skills` |
| Tool definitions (inherited from parent, or the subset in `tools`) | The parent's system prompt |

(source: https://code.claude.com/docs/en/agent-sdk/subagents)

**Fuller startup inventory (filesystem doc).** A non-fork subagent's initial context contains: its own system prompt + appended environment details (not the full Claude Code system prompt); the task/delegation message Claude writes; CLAUDE.md + the full memory hierarchy (`~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy) — **except** built-in Explore and Plan agents skip CLAUDE.md and git status; a git-status snapshot; and any preloaded skills (source: https://code.claude.com/docs/en/sub-agents).

**Design implications.** Self-contain every delegation: pass concrete file paths, exact error strings, and prior decisions in the invocation prompt. If a rule must reach the subagent (e.g. "ignore `vendor/`"), restate it in the delegation prompt — the subagent does not see the parent's earlier context (source: https://code.claude.com/docs/en/sub-agents).

**Return-value caveat.** "The parent receives the subagent's final message verbatim as the Agent tool result, but may summarize it in its own response." To preserve subagent output verbatim in the user-facing answer, instruct so in the **main** `query()` prompt/`systemPrompt` (source: https://code.claude.com/docs/en/agent-sdk/subagents).

---

## 5. Context isolation — why subagents save the main thread's context [D1 primary]

**Mechanism.** "Each subagent runs in its own fresh conversation. Intermediate tool calls and results stay inside the subagent; only its final message returns to the parent." Example: a `research-assistant` can "explore dozens of files without any of that content accumulating in the main conversation. The parent receives a concise summary, not every file the subagent read." (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Engineering framing.** "Subagents use their own isolated context windows, and only send relevant information back to the orchestrator" — ideal for "tasks requiring filtering through large datasets where most information won't be useful" (source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk). Ties to the agent loop: **gather context → take action → verify work → repeat** (source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk).

**Persistence detail.** Subagent transcripts are stored in **separate files** and are unaffected by main-conversation compaction; they persist within their session and are cleaned up per `cleanupPeriodDays` (default 30 days). Subagents support auto-compaction at ~95% capacity (override via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`) (sources: https://code.claude.com/docs/en/agent-sdk/subagents; https://code.claude.com/docs/en/sub-agents).

**When to use.** Use a subagent "when a side task would flood your main conversation with search results, logs, or file contents you won't reference again" — e.g. "run the test suite and report only the failing tests with their error messages" (source: https://code.claude.com/docs/en/sub-agents).

---

## 6. Constraints & guardrails [D1 primary / D2 secondary]

**No nested subagents (the core rule).** "**Subagents cannot spawn their own subagents. Don't include `Agent` in a subagent's `tools` array.**" (source: https://code.claude.com/docs/en/agent-sdk/subagents). Restated in the filesystem doc: "Subagents cannot spawn other subagents. If your workflow requires nested delegation, use Skills or chain subagents from the main conversation." This is also why plan mode uses the read-only **Plan** subagent — "This prevents infinite nesting (subagents cannot spawn other subagents)" (source: https://code.claude.com/docs/en/sub-agents). Note: `Agent(agent_type)` allow-listing only matters for an agent running as the *main thread* via `claude --agent`; it "has no effect in subagent definitions" (source: https://code.claude.com/docs/en/sub-agents).

**Tool restriction (least privilege).** Omit `tools` → inherits all; specify `tools` → allow-list only. `disallowedTools` is a denylist applied **first**, then `tools` resolves against the remainder; a tool in both is removed (source: https://code.claude.com/docs/en/sub-agents). Documented combos:

| Use case | Tools |
|---|---|
| Read-only analysis | `Read`, `Grep`, `Glob` |
| Test execution | `Bash`, `Read`, `Grep` |
| Code modification | `Read`, `Edit`, `Write`, `Grep`, `Glob` |
| Full access | omit `tools` |

(source: https://code.claude.com/docs/en/agent-sdk/subagents). Some UI/session tools are **never** available to subagents even if listed: `Agent`, `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode` (unless `permissionMode: plan`), `ScheduleWakeup`, `WaitForMcpServers` (source: https://code.claude.com/docs/en/sub-agents).

**Per-subagent model selection.** Set `model` to `sonnet`/`opus`/`haiku`/`inherit` or a full ID; defaults to `inherit` if omitted (filesystem). Resolution order: `CLAUDE_CODE_SUBAGENT_MODEL` env var → per-invocation `model` param → definition `model` frontmatter → main model (source: https://code.claude.com/docs/en/sub-agents). Cost lever: route routine work to Haiku (source: https://code.claude.com/docs/en/sub-agents).

**Parallelism.** Subagents "can run concurrently" and "work well for a few delegated tasks per turn"; no hard concurrency cap is documented for ordinary subagent delegation (source: https://code.claude.com/docs/en/agent-sdk/subagents). Caps **do** apply to the Workflow runtime: **up to 16 concurrent agents** (fewer on limited cores) and **1,000 agents total per run** (source: https://code.claude.com/docs/en/workflows). [VERIFY whether any per-turn subagent concurrency cap exists outside workflows.]

**maxTurns / timeout.** `maxTurns` caps agentic turns before the subagent stops (source: https://code.claude.com/docs/en/agent-sdk/subagents). No explicit wall-clock timeout field is documented for `AgentDefinition`. [VERIFY timeout behavior.]

**Permission-mode precedence.** A subagent may override `permissionMode`, **except** a parent in `bypassPermissions` or `acceptEdits` takes precedence and cannot be overridden; under parent `auto` mode the subagent inherits auto and its frontmatter `permissionMode` is ignored (source: https://code.claude.com/docs/en/sub-agents).

---

## 7. The "Workflow tool" graduation [D1 primary]

**Mechanism / what it is.** "A dynamic workflow is a JavaScript script that orchestrates subagents at scale. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive." The orchestration loop, branching, and intermediate results live in **script variables**, not Claude's context — "so Claude's context holds only the final answer." (source: https://code.claude.com/docs/en/workflows).

**When to graduate from a single Task delegation.** "Subagents work well for a few delegated tasks per turn. For runs that coordinate dozens to hundreds of agents, use the `Workflow` tool, which moves the orchestration into a script the runtime executes outside the conversation context." (source: https://code.claude.com/docs/en/agent-sdk/subagents). Reach for it "when a task needs more agents than one conversation can coordinate, or when you want the orchestration codified as a script you can read and rerun" — e.g. codebase-wide bug sweep, 500-file migration, cross-checked research, multi-angle planning (source: https://code.claude.com/docs/en/workflows).

**Who holds the plan (the decisive distinction — verbatim table excerpt):**

| | Subagents | Workflows |
|---|---|---|
| What it is | A worker Claude spawns | A script the runtime executes |
| Who decides what runs next | Claude, turn by turn | The script |
| Where intermediate results live | Claude's context window | Script variables |
| What's repeatable | The worker definition | The orchestration itself |
| Scale | A few delegated tasks per turn | Dozens to hundreds of agents per run |
| Interruption | Restarts the turn | Resumable in the same session |

(source: https://code.claude.com/docs/en/workflows)

**Fan-out / pipeline / barriers / quality patterns.** A workflow "can have independent agents adversarially review each other's findings before they're reported, or draft a plan from several angles and weigh them against each other." The bundled `/deep-research` workflow "fans out web searches across several angles, fetches and cross-checks the sources it finds, votes on each claim" — i.e. fan-out + cross-check barrier + voting (sources: https://code.claude.com/docs/en/workflows). This maps to the **orchestrator-workers** and **parallelization (sectioning/voting)** patterns from "Building effective agents" (source: https://www.anthropic.com/engineering/building-effective-agents).

**Workflow runtime constraints (verbatim):** No mid-run user input; no direct filesystem/shell access from the script itself (agents do the I/O, the script coordinates); **up to 16 concurrent agents** (fewer on limited cores); **1,000 agents total per run** (source: https://code.claude.com/docs/en/workflows). Subagents a workflow spawns always run in `acceptEdits` mode and inherit the tool allowlist regardless of session mode (source: https://code.claude.com/docs/en/workflows).

**Version / availability gating.** The `Workflow` *tool* is in the **TypeScript Agent SDK v0.3.149+**; include `Workflow` in `allowedTools` to auto-approve (source: https://code.claude.com/docs/en/agent-sdk/subagents). The *dynamic workflows feature* in the CLI is a **research preview requiring Claude Code v2.1.154+**, on all paid plans (source: https://code.claude.com/docs/en/workflows). Saved workflows live in `.claude/workflows/` (project) or `~/.claude/workflows/`; project wins on name clash; input is passed via the `args` global (source: https://code.claude.com/docs/en/workflows). [VERIFY both version numbers — fast-moving.]

---

## 8. CLI ↔ SDK mapping [D2 primary / D1 secondary]

**Mechanism.** The `/agents` command opens a tabbed UI (Running / Library tabs) to create, edit, delete, and inspect subagents; it writes Markdown files with YAML frontmatter (source: https://code.claude.com/docs/en/sub-agents). The same fields map 1:1 to the SDK's `AgentDefinition`.

**Verbatim `.claude/agents/<name>.md` frontmatter example:**

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```
(source: https://code.claude.com/docs/en/sub-agents)

**Frontmatter fields (only `name` and `description` required):** `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation` (`worktree`), `color`, `initialPrompt` (source: https://code.claude.com/docs/en/sub-agents). The markdown **body** = the system prompt (= SDK `prompt`).

**`--agents` CLI flag** passes JSON inline (session-only, not saved) with the same fields as file frontmatter: `description`, `prompt`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `skills`, `initialPrompt`, `memory`, `effort`, `background`, `isolation`, `color` (source: https://code.claude.com/docs/en/sub-agents).

**Mapping table:**

| CLI / filesystem concept | SDK equivalent |
|---|---|
| `/agents` UI | (no SDK equivalent — code defines agents directly) |
| `.claude/agents/<name>.md` file | one entry in `agents: { "<name>": {...} }` |
| frontmatter `name` (file identity) | the **key** in the `agents` record/dict |
| markdown body | `AgentDefinition.prompt` |
| frontmatter `description` | `description` |
| frontmatter `tools` (comma list) | `tools` (string array) |
| frontmatter `disallowedTools` | `disallowedTools` |
| frontmatter `model` | `model` |
| frontmatter `skills` / `memory` / `mcpServers` / `maxTurns` / `background` / `effort` / `permissionMode` / `initialPrompt` | same-named `AgentDefinition` fields (camelCase in Python) |
| frontmatter `hooks` / `isolation` / `color` | **filesystem-only** — not in the SDK `AgentDefinition` type |
| `--agents '{...}'` JSON | the same shape as the `agents` param, session-scoped |

(sources: https://code.claude.com/docs/en/sub-agents; https://code.claude.com/docs/en/agent-sdk/typescript; https://code.claude.com/docs/en/agent-sdk/python)

Note: `hooks`, `isolation`, and `color` appear in **filesystem/CLI** frontmatter but are **not** in the documented SDK `AgentDefinition` type. [VERIFY whether the SDK type silently accepts them.]

---

## 9. Design heuristics [D1 primary]

**Subagent vs. a single longer prompt.** Use a subagent when "the task produces verbose output you don't need in your main context," you want tool restrictions/permissions enforced, or "the work is self-contained and can return a summary." Stay in the **main conversation** when the task needs frequent back-and-forth, when multiple phases share significant context (planning → implementation → testing), for quick targeted changes, or when latency matters ("Subagents start fresh and may need time to gather context") (source: https://code.claude.com/docs/en/sub-agents). For a quick question about existing context, prefer `/btw` over a subagent (source: https://code.claude.com/docs/en/sub-agents).

**One responsibility per subagent.** "Design focused subagents: each subagent should excel at one specific task." Define a custom subagent "when you keep spawning the same kind of worker with the same instructions." (sources: https://code.claude.com/docs/en/sub-agents).

**Description-writing for correct routing.** "Claude uses each subagent's description to decide when to delegate tasks... write a clear description so Claude knows when to use it." Add "use proactively" to encourage delegation; write "detailed descriptions" so Claude matches tasks correctly (source: https://code.claude.com/docs/en/sub-agents). If Claude won't delegate: (1) include `Agent` in `allowedTools`; (2) name the subagent explicitly; (3) sharpen the `description` (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Least privilege.** "Limit tool access: grant only necessary permissions for security and focus." (source: https://code.claude.com/docs/en/sub-agents).

**Pattern ladder (single Task → workflow).** Chain subagents from the main conversation for sequential multi-step work; run parallel research with separate subagents for independent paths; graduate to a Workflow when you need dozens–hundreds of coordinated agents or a rerunnable, codified orchestration (sources: https://code.claude.com/docs/en/sub-agents; https://code.claude.com/docs/en/workflows). Maps to "Building effective agents": **orchestrator-workers** = "a central LLM to dynamically break down tasks and delegate to worker LLMs, then synthesize results... Suits unpredictable subtask scenarios"; choose a **workflow** (predefined code paths) for predictable tasks and an **agent** (LLM directs its own process) for open-ended ones (source: https://www.anthropic.com/engineering/building-effective-agents).

---

## Key shapes & rules — quick reference

**`AgentDefinition` required vs. optional:** required = `description`, `prompt`. Optional = `tools`, `disallowedTools`, `model`, `skills`, `memory`, `mcpServers`, `initialPrompt`, `maxTurns`, `background`, `effort`, `permissionMode` (+ TS `criticalSystemReminder_EXPERIMENTAL`) (source: https://code.claude.com/docs/en/agent-sdk/typescript).

**The `agents` param:** TS `Record<string, AgentDefinition>`; Python `dict[str, AgentDefinition]`; key = agent name (source: https://code.claude.com/docs/en/agent-sdk/typescript; https://code.claude.com/docs/en/agent-sdk/python).

**The no-nesting rule:** Subagents cannot spawn subagents. Never put `Agent` in a subagent's `tools`. For nested delegation use Skills or chain from the main conversation (source: https://code.claude.com/docs/en/agent-sdk/subagents; https://code.claude.com/docs/en/sub-agents).

**Single channel in:** the Agent tool's prompt string is the only parent→subagent channel; no shared memory (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Single channel out:** only the subagent's final message returns; intermediate work stays isolated (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Auto-approve delegation:** add `Agent` to `allowedTools`/`allowed_tools` (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Tool name:** `Task` → `Agent` since v2.1.63; `Task` still aliased (source: https://code.claude.com/docs/en/agent-sdk/subagents).

**Precedence:** programmatic `agents` > filesystem agents of the same name; filesystem ladder: managed > `--agents` > project > user > plugin (source: https://code.claude.com/docs/en/agent-sdk/subagents; https://code.claude.com/docs/en/sub-agents).

**Workflow caps:** ≤16 concurrent agents; 1,000 agents/run; runs outside conversation context (source: https://code.claude.com/docs/en/workflows).

**Python field-naming trap:** `AgentDefinition` fields are camelCase even in Python; snake_case raises `TypeError` (source: https://code.claude.com/docs/en/agent-sdk/python).

---

## [VERIFY] list — version-sensitive / uncertain facts

1. **`AgentDefinition` field roster** — confirm against the live TS/Python reference; `background`, `effort`, `initialPrompt`, `criticalSystemReminder_EXPERIMENTAL` are newer/experimental and may change (check: https://code.claude.com/docs/en/agent-sdk/typescript, https://code.claude.com/docs/en/agent-sdk/python).
2. **No `mode` / `source` fields** — base scope mentioned `mode`/`source`; current type has neither (closest = `permissionMode`, plus file scope/location). Confirm no such fields exist.
3. **No-nesting rule** — verified in two docs; reconfirm it still holds in the current SDK (the Plan-agent rationale also depends on it).
4. **[RESOLVED 2026-06-09] Concurrency caps** — confirmed: **NO per-turn cap** applies to ordinary subagent parallelism outside workflows; the 16-concurrent / 1,000-total limits are *Workflow-runtime-only*. (`QA-VERIFY-SWEEP_2026-06-09.md`)
5. **maxTurns vs. timeout** — `maxTurns` documented; **no explicit wall-clock timeout field** found for `AgentDefinition`. Verify timeout behavior.
6. **Tool rename Task→Agent (v2.1.63)** — confirm current emit behavior (Agent in `tool_use`, Task still in `system:init` and `permission_denials`).
7. **Workflow version gates** — `Workflow` tool in **TS SDK v0.3.149+**; dynamic-workflows feature needs **Claude Code v2.1.154+** (research preview). Both fast-moving — reverify exact numbers.
8. **SDK naming** — "Claude Code SDK" → "Claude Agent SDK"; npm package `@anthropic-ai/claude-agent-sdk`, Python `claude_agent_sdk`. Confirm no further rename.
9. **Host redirects** — `platform.claude.com/docs/en/agent-sdk/*` → `code.claude.com/...`; `anthropic.com/engineering/*` → `claude.com/blog/*`. Cite live hosts; reverify if URLs move again.
10. **Filesystem-only fields (`hooks`, `isolation`, `color`)** — present in frontmatter but absent from the documented SDK `AgentDefinition` type; verify whether the SDK accepts/ignores them.
11. **`general-purpose` built-in subagent** — always invocable via the Agent tool without definition; confirm it still ships and that `Agent` in `allowedTools` is the auto-approve path.

(Primary verification targets, in priority order: https://code.claude.com/docs/en/agent-sdk/subagents · /typescript · /python · https://code.claude.com/docs/en/sub-agents · https://code.claude.com/docs/en/workflows)

---

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`)*

- **Fork subagents** (Claude Code v2.1.117+, `/fork` default from v2.1.161) **inherit the FULL parent conversation context** — qualifies any "subagents always start fresh" claim (still true for standard Agent-tool / `agents`-param spawns).
- **Built-in subagent roster grew:** `statusline-setup` and `claude-code-guide` now ship alongside Explore / Plan / General-purpose.
- **Agent teams** now exist as a higher-level multi-agent construct above single-parent subagent delegation.
- **`criticalSystemReminder_EXPERIMENTAL`** ([VERIFY] #1) — still unverifiable on the live TS reference; leave flagged.
