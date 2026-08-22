# The Five Orchestration Patterns — Decision Framework
## Source-of-Truth Citation Notes (Extension Lesson, Introduction to Subagents)

**CCA-F Domain reinforced:** Domain 1 — Agentic Architecture & Orchestration (27% of exam).
**Compiled:** 2026-06-05 · **Re-verified 2026-06-09** (core claims confirmed; additive subagent drifts in the addendum at the end. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
**Research method:** Live fetch of Anthropic primary sources (engineering posts + Claude Code / Agent SDK docs).

### Primary sources (fetched)
- Anthropic, "Building Effective AI Agents" — https://www.anthropic.com/engineering/building-effective-agents (published Dec 19, 2024)
- Anthropic, "How we built our multi-agent research system" — https://www.anthropic.com/engineering/multi-agent-research-system (published June 13, 2025)
- Claude Agent SDK, "Subagents in the SDK" — https://code.claude.com/docs/en/agent-sdk/subagents
- Claude Code, "Create custom subagents" — https://code.claude.com/docs/en/sub-agents

> NOTE ON AGES: "Building Effective Agents" (Dec 2024) and the multi-agent post (June 2025) are older than 6 months as of compile date. The conceptual patterns are stable canon; the *numbers* in the multi-agent post are tied to Claude Opus 4 / Sonnet 4 and that specific eval, so treat them as point-in-time facts, not perpetual benchmarks. [VERIFY] if reused in a context that implies current model performance.

---

## Section 1 — Workflows vs. Agents (the foundational distinction)

Anthropic groups everything under the umbrella term **"agentic systems"** but draws a hard architectural line between two sub-types:

- **Workflows** — "Workflows are systems where LLMs and tools are orchestrated through predefined code paths." (source: https://www.anthropic.com/engineering/building-effective-agents)
- **Agents** — "Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." (source: https://www.anthropic.com/engineering/building-effective-agents)

Teaching takeaway: the dividing question is *who controls the path* — the developer's code (workflow) or the model itself at runtime (agent). The five named patterns below are **workflows** (predefined orchestration); the autonomous loop in Section 8 is the **agent** case.

**CCA-F relevance:** Domain 1 expects you to classify a given architecture as workflow vs. agent and justify the choice.

---

## Section 2 — The Augmented LLM (the building block under every pattern)

Every pattern is composed from one repeated unit: the **augmented LLM** — "an LLM enhanced with augmentations such as retrieval, tools, and memory." Anthropic notes current models "can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain." (source: https://www.anthropic.com/engineering/building-effective-agents)

Teaching takeaway: before reaching for any multi-step pattern, make sure the single augmented LLM call is well-built (good tooling, retrieval, and a tailored interface). The patterns *compose* augmented LLMs; they don't replace the need to get one right.

**CCA-F relevance:** Domain 1 — recognizing retrieval/tools/memory as the primitives that orchestration patterns assemble.

---

## Section 3 — Pattern 1: Prompt Chaining

**Definition:** Prompt chaining "decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Gate checks:** "You can add programmatic checks (see 'gate' in the diagram) on any intermediate steps to ensure that the process is still on track." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** "ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks," trading "off latency for higher accuracy by making each LLM call an easier task." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Concrete examples (verbatim):**
- "Generating marketing copy, then translating it into a different language."
- "Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Maps to subagents:** A chain is typically implemented in *code paths* (predefined sequence), not by delegation, but each step can be a tool-restricted subagent if a step needs context isolation.

**CCA-F relevance:** Domain 1 — fixed sequential decomposition; recognizing latency/accuracy tradeoff.

---

## Section 4 — Pattern 2: Routing

**Definition:** Routing "classifies an input and directs it to a specialized followup task." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Why it helps:** "This workflow allows for separation of concerns, and building more specialized prompts." Without routing, optimizing for one kind of input can hurt others. (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** "complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Concrete example (verbatim):** "Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools." A second example: routing easy/common questions to a smaller model and hard/unusual ones to a more capable model to optimize cost and speed. (source: https://www.anthropic.com/engineering/building-effective-agents)

**Maps to subagents:** This is exactly how Claude decides *which* subagent to invoke — "Claude determines whether to invoke them based on each subagent's `description` field" / "Claude uses each subagent's description to decide when to delegate tasks." A well-written `description` is a router classifier. (source: https://code.claude.com/docs/en/agent-sdk/subagents ; https://code.claude.com/docs/en/sub-agents)

**CCA-F relevance:** Domain 1 — classification-then-dispatch; cost/latency optimization via model routing.

---

## Section 5 — Pattern 3: Parallelization (Sectioning + Voting)

**Definition:** "LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically." Two key variations: (source: https://www.anthropic.com/engineering/building-effective-agents)

- **Sectioning:** "Breaking a task into independent subtasks run in parallel." (source: https://www.anthropic.com/engineering/building-effective-agents)
- **Voting:** "Running the same task multiple times to get diverse outputs." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** Effective "when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Concrete examples (verbatim):**
- *Sectioning:* implementing guardrails where one model instance processes the user query while another screens it for inappropriate content (separate attention per concern); also automating evals where each LLM call assesses a different aspect of performance.
- *Voting:* "Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Maps to subagents (SDK + Claude Code):**
- "Multiple subagents can run concurrently, dramatically speeding up complex workflows." Example given: running `style-checker`, `security-scanner`, and `test-coverage` subagents simultaneously, "reducing review time from minutes to seconds." (source: https://code.claude.com/docs/en/agent-sdk/subagents)
- Each parallel worker gets isolation: "Each subagent runs in its own fresh conversation" / "Each subagent runs in its own context window." (source: https://code.claude.com/docs/en/agent-sdk/subagents ; https://code.claude.com/docs/en/sub-agents)

**CCA-F relevance:** Domain 1 — distinguishing sectioning (split work) from voting (redundancy for confidence); mapping to concurrent subagents.

---

## Section 6 — Pattern 4: Orchestrator-Workers

**Definition:** "In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Key difference vs. parallelization:** "the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** "well-suited for complex tasks where you can't predict the subtasks needed." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Concrete example (verbatim):** "Coding products that make complex changes to multiple files each time"; also search tasks that gather and synthesize information from multiple sources. (source: https://www.anthropic.com/engineering/building-effective-agents)

**Maps to subagents:** This is the native shape of Claude Code / Agent SDK subagent delegation — a main agent spawns focused workers via the `Agent` tool and receives "the subagent's final message verbatim as the Agent tool result." (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**CCA-F relevance:** Domain 1 — dynamic (not pre-defined) decomposition; orchestrator synthesizes worker outputs. This is the most exam-relevant pattern for subagents.

---

## Section 7 — Pattern 5: Evaluator-Optimizer

**Definition:** "In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** "particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value." Two fit signals: LLM responses can be demonstrably improved by feedback, and the LLM can provide that feedback (analogous to a human writer's revision process). (source: https://www.anthropic.com/engineering/building-effective-agents)

**Concrete example (verbatim):** "Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques." Also: complex search tasks requiring multiple rounds of searching and analysis, where the evaluator decides whether further searches are warranted. (source: https://www.anthropic.com/engineering/building-effective-agents)

**Maps to subagents:** Implement the evaluator as a separate tool-restricted subagent (e.g., read-only reviewer) that critiques the generator's output before the loop continues.

**CCA-F relevance:** Domain 1 — generate/critique loop; the role of explicit, clear evaluation criteria.

---

## Section 8 — Autonomous Agents (the loop, distinct from the five workflows)

**Definition / how they operate:** Agents "begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement." Critically: "During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step (such as tool call results or code execution) to assess its progress." (source: https://www.anthropic.com/engineering/building-effective-agents)

**When to use:** "Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Cost / autonomy caution:** Agents' autonomy means higher costs and potential for compounding errors; Anthropic recommends extensive testing in sandboxes plus appropriate guardrails. (source: https://www.anthropic.com/engineering/building-effective-agents)

**CCA-F relevance:** Domain 1 — recognizing when a dynamic agent loop is warranted over a fixed workflow, and the ground-truth/guardrail requirements.

---

## Section 9 — The Decision Framework (simplicity-first)

**Core rule (verbatim):** "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Single-call default:** "For many applications... optimizing single LLM calls with retrieval and in-context examples is usually enough." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Escalation guidance (verbatim):** "Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Workflow vs. agent tradeoff:** "Workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale." (source: https://www.anthropic.com/engineering/building-effective-agents)

**Suggested decision ladder for the lesson (synthesized from the above guidance):**
1. Single augmented LLM call (retrieval + tools + examples) → use if it suffices.
2. Prompt chaining → fixed, cleanly decomposable steps.
3. Routing → distinct input categories handled best separately.
4. Parallelization (sectioning/voting) → independent subtasks or multi-attempt confidence.
5. Orchestrator-workers → subtasks unpredictable, determined at runtime.
6. Evaluator-optimizer → clear criteria + iterative refinement adds measurable value.
7. Autonomous agent loop → open-ended, unpredictable step count, no hardcodable path.

**CCA-F relevance:** Domain 1 — choosing the *least complex* pattern that solves the problem; justifying escalation.

---

## Section 10 — Orchestrator-Workers at Scale: the Multi-Agent Research System

This post is the production reference architecture for Pattern 4.

**Reference architecture (orchestrator-worker):**
- A **lead agent** analyzes the query, develops a strategy, and spawns subagents. (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- **Subagents operate in parallel**, each with its own context window: "Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- Subagents perform web searches, use interleaved thinking to evaluate results, and return findings to the lead agent, which synthesizes and decides whether more research is needed.
- A dedicated **CitationAgent** then "processes the documents and research report to identify specific locations for citations," ensuring proper attribution (the citation pass). (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**Why multi-agent works:** "The essence of search is compression: distilling insights from a vast corpus." Parallel subagents with separate context windows each compress a slice, exceeding a single context window's capacity. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**Effort-scaling heuristics (verbatim, given to the lead agent):**
- Simple fact-finding: "1 agent with 3-10 tool calls."
- Direct comparisons: "2-4 subagents with 10-15 calls each."
- Complex research: "more than 10 subagents with clearly divided responsibilities."
- Purpose: "These guidelines help the lead agent allocate resources efficiently and prevent overinvestment in simple queries." (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**Headline performance / cost facts (quote numbers exactly):**
- "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- Token economics: "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- In the BrowseComp analysis, "token usage by itself explains 80% of the variance" (with model choice and number of tool calls as the next two factors). (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- Parallelism speedup: having the lead agent spawn subagents in parallel and the subagents "use 3+ tools in parallel... cut research time by up to 90% for complex queries." (source: https://www.anthropic.com/engineering/multi-agent-research-system)
- Tooling impact: an improved tool-description rewrite produced "a 40% decrease in task completion time." [VERIFY — confirm this 40% figure refers to the tool-description experiment specifically.] (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**Economic gate (when multi-agent is worth it):** "there's a real tension between autonomy and reliability"; multi-agent systems "require tasks where the value of the task is high enough to pay for the increased performance." They excel at "valuable tasks that involve heavy parallelization, information that exceeds single context windows." Not suited to tasks where all agents need to share the same context or have many tight dependencies between agents. (source: https://www.anthropic.com/engineering/multi-agent-research-system)

**CCA-F relevance:** Domain 1 — production orchestrator-worker design, effort/resource scaling, and the cost-vs-value decision for multi-agent architectures.

---

## Section 11 — How Subagents Implement These Patterns (Claude Code + Agent SDK)

**What a subagent is:**
- SDK: "Subagents are separate agent instances that your main agent can spawn to handle focused subtasks." Use them to "isolate context for focused subtasks, run multiple analyses in parallel, and apply specialized instructions without bloating the main agent's prompt." (source: https://code.claude.com/docs/en/agent-sdk/subagents)
- Claude Code: "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions." (source: https://code.claude.com/docs/en/sub-agents)

**Three ways to create subagents (SDK):** programmatically via the `agents` parameter in `query()`; filesystem-based as markdown in `.claude/agents/`; or the built-in `general-purpose` subagent invoked via the Agent tool without any definition. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**Filesystem definition (Claude Code) — YAML frontmatter + markdown body:**
```
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---
You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```
"The frontmatter defines the subagent's metadata and configuration. The body becomes the system prompt." (source: https://code.claude.com/docs/en/sub-agents)

**Managing subagents — the `/agents` command:** "The `/agents` command opens a tabbed interface for managing subagents." The **Running** tab shows live subagents; the **Library** tab creates/edits/deletes them. "This is the recommended way to create and manage subagents." (source: https://code.claude.com/docs/en/sub-agents)

**Scope & precedence (highest → lowest):** Managed settings (org) → `--agents` CLI flag (session) → `.claude/agents/` (project) → `~/.claude/agents/` (user) → plugin `agents/` directory. (source: https://code.claude.com/docs/en/sub-agents)

**Key `AgentDefinition` fields (SDK):** `description` (required — drives routing), `prompt` (required — system prompt), `tools` / `disallowedTools` (capability restriction), `model` (alias `sonnet`/`opus`/`haiku`/`inherit` or full ID), plus `skills`, `memory`, `mcpServers`, `maxTurns`, `background`, `effort`, `permissionMode`. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**How subagents realize each pattern:**
- *Routing* → Claude matches a task to a subagent's `description`; or invoke explicitly by name ("Use the code-reviewer agent to..."). (source: https://code.claude.com/docs/en/agent-sdk/subagents)
- *Parallelization* → "Multiple subagents can run concurrently"; each runs in an isolated context window so parallel work doesn't pollute the main conversation. (source: https://code.claude.com/docs/en/agent-sdk/subagents)
- *Orchestrator-workers* → main agent delegates via the `Agent` tool and synthesizes the verbatim final messages returned by workers. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**Context isolation (what crosses the boundary):** "A subagent's context window starts fresh (no parent conversation)... The only channel from parent to subagent is the Agent tool's prompt string." The subagent receives its own system prompt + the Agent tool prompt + project CLAUDE.md (if `settingSources` loads it) + tool defs; it does NOT receive the parent's conversation history, tool results, or system prompt. (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**Critical orchestration constraint:** "Subagents cannot spawn their own subagents." (source: https://code.claude.com/docs/en/agent-sdk/subagents) The orchestration tree is therefore one level deep by default — a main agent and its workers, not arbitrarily nested agents.

**Scaling beyond a few workers:** "Subagents work well for a few delegated tasks per turn. For runs that coordinate dozens to hundreds of agents, use the `Workflow` tool, which moves the orchestration into a script the runtime executes outside the conversation context." (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**Built-in subagents (Claude Code):** **Explore** (Haiku, read-only, codebase search), **Plan** (inherits model, read-only, used in plan mode), **General-purpose** (inherits model, all tools, complex multi-step work). (source: https://code.claude.com/docs/en/sub-agents)

**Naming note for the lesson:** The delegation tool was "renamed from `Task` to `Agent` in Claude Code v2.1.63"; current SDK emits `Agent` in `tool_use` blocks but still uses `Task` in the `system:init` tools list. [VERIFY against current version if the lesson cites a specific version number.] (source: https://code.claude.com/docs/en/agent-sdk/subagents)

**CCA-F relevance:** Domain 1 — concrete implementation of orchestration patterns via subagents; context isolation, tool restriction, model routing, and the no-nesting constraint are all architecture-decision points.

---

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`)*

- **Fork subagents qualify the "context window starts fresh" claim (Section 11).** Claude Code v2.1.117+ supports **fork subagents** (`/fork`, default behavior from v2.1.161) which **inherit the FULL parent conversation context**. The "starts fresh / only channel is the Agent-tool prompt string" model remains true for standard Agent-tool spawns — but is no longer universally true of all subagents.
- **Built-in subagent roster grew:** in addition to Explore / Plan / General-purpose, Claude Code now ships `statusline-setup` and `claude-code-guide` built-ins.
- **Agent teams** now exist as a higher-level multi-agent construct above single-parent subagent delegation.
- **No per-turn subagent concurrency cap** outside the Workflow runtime (the 16-concurrent / 1,000-total limits are Workflow-only).

---

## Sources
1. Anthropic — Building Effective AI Agents: https://www.anthropic.com/engineering/building-effective-agents (Dec 19, 2024)
2. Anthropic — Building Effective AI Agents (research mirror): https://www.anthropic.com/research/building-effective-agents
3. Anthropic — How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system (June 13, 2025)
4. Claude Agent SDK — Subagents in the SDK: https://code.claude.com/docs/en/agent-sdk/subagents
5. Claude Code — Create custom subagents: https://code.claude.com/docs/en/sub-agents
