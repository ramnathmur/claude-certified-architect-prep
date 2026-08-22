# Source Pack B — Chapters 11, 13, 16

**Built:** 2026-08-22 · **For:** CCDV-F course regeneration · **Status:** research only, not teaching prose

**All facts below were read on 2026-08-22 by fetching the URL given.** Nothing here is from memory.
Where a page did not answer a question, that is recorded in the gap list at the end rather than filled in.

**Exam frame applied throughout** (from `EXAM-FACTS_v1.md` §1, §2, §5): 53 items, closed book,
multiple-choice / multiple-response, each item states how many responses to select. All three official
sample items are short scenarios that state a constraint, then four options, **no code anywhere**, every
wrong option a legitimate technique that does not match the constraint. So this pack privileges facts
that **discriminate between two plausible options** and marks volatile specifics `[VOLATILE]` rather
than treating them as content.

Chapter coverage against the blueprint: ch11 → Domain 8 / Tool Implementation (4.4%);
ch13 → Domain 8 / Agentic Customization (4.1%); ch16 → Domain 1 / Agent Construction with Claude (5.3%)
and Agent Patterns and Frameworks (4.9%).

---

## CHAPTER 11 — "Why Claude picked the wrong tool"

### Q11.1 — What does Anthropic document about writing tool descriptions?

**Fact 1 — the description is named as the single most important factor.** Under "Best practices for
tool definitions": *"Provide extremely detailed descriptions. This is by far the most important factor
in tool performance."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 2 — the four things a description must cover.** The same bullet enumerates them: what the tool
does; when it should be used **(and when it shouldn't)**; what each parameter means and how it affects
behaviour; and *"Any important caveats or limitations, such as what information the tool does not
return."* Closing line: *"The more context you can give Claude about your tools, the better it will be
at deciding when and how to use them."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

> **Discriminator for the chapter.** "When it shouldn't be used" and "what the tool does *not* return"
> are the two clauses candidates omit. A stem that says "Claude keeps calling the wrong one of two
> similar tools" is answered by negative scope in the description, not by a longer schema, not by
> `tool_choice`, and not by a bigger model.

**Fact 3 — a stated length floor.** *"Aim for at least 3–4 sentences for each tool description, more if
the tool is complex."* `[VOLATILE]` — this is a specific number in a best-practices list.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 4 — the `description` field is defined as prose about behaviour, not a label.** The parameter
table defines `description` as *"A detailed plaintext description of what the tool does, when it should
be used, and how it behaves."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 5 — descriptions outrank examples; examples are the fallback for complex inputs.** *"Prioritize
descriptions, but consider using `input_examples` for complex tools."* Examples are for *"tools with
complex inputs, nested objects, or format-sensitive parameters."* `input_examples` is **not supported
on server tools** or on the computer-use / browser-use client toolsets. `[VOLATILE]` — field name.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 6 — Anthropic ships a worked good/bad pair.** The good `get_stock_price` description states the
valid input domain (a ticker on a major US exchange), the return (latest trade price in USD), the
trigger (user asks for current or most recent price), and the negative scope (*"It will not provide any
other information about the stock or company."*). The poor one is *"Gets the stock price for a
ticker."* Anthropic's own gloss: the poor description *"is too brief and leaves Claude with many open
questions about the tool's behavior and usage."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 7 — engineering-blog reinforcement, with a mental model.** *"Even small refinements to tool
descriptions can yield dramatic improvements."* Advice: think about *"how you would describe your tool
to a new hire"* and make implicit context explicit. Parameter names must be unambiguous — `user_id`
rather than `user`.
Source: https://www.anthropic.com/engineering/writing-tools-for-agents · fetched 2026-08-22

**Fact 8 — tool descriptions are what Claude matches against, restated at the API level.** *"Claude
determines when to call a tool based on the user's request and the tool's description."* And, with the
default `tool_choice` of `auto`: *"It calls a tool when the request maps to that tool's described
capability and the answer isn't already in context."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · fetched 2026-08-22

**Fact 9 — descriptions enter the context window and cost tokens.** The API *"constructs a special
system prompt from the tool definitions"*, and additional tokens come from *"the `tools` parameter in
API requests (tool names, descriptions, and schemas)"*. So description quality trades against context
cost — the real design tension.
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · both fetched 2026-08-22

**Fact 10 — a lever adjacent to description: steering by system prompt.** *"This boundary is steerable
through your system prompt."* Documented example escalation: `"Use the tools to investigate before
responding."` → `"Always call a tool first before responding."` → conservative:
`"Use your judgment about whether to call a tool or respond directly."`
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · fetched 2026-08-22

**Fact 11 — the deterministic alternative to prompting.** *"To require a tool call rather than rely on
prompting, set `tool_choice`."* Four values, verbatim behaviours:
- `auto` — Claude decides whether to call any provided tools. **Default when `tools` are provided.**
- `any` — Claude *"must use one of the provided tools, but doesn't force a particular tool."*
- `tool` — *"forces Claude to always use a particular tool."*
- `none` — *"prevents Claude from using any tools."* **Default when no `tools` are provided.**

Side effect worth a distractor: with `any` or `tool`, *"the API prefills the assistant message to force
a tool to be used... the models will not emit a natural language response or explanation before
`tool_use` content blocks, even if explicitly asked to do so."* `[VOLATILE]` — parameter names.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

> **Discriminator.** `tool_choice` controls *whether* a tool is called. It does not control *which of
> several similar tools* Claude picks, except in the degenerate `tool` case that names one. A scenario
> about picking the wrong tool among four is a description problem; a scenario about not calling any
> tool is a `tool_choice` / system-prompt problem.

**Fact 12 — schema conformance is a separate control from selection.** *"Add `strict: true` to your
custom tool definitions to ensure Claude's tool calls always match your schema exactly."* And the
combination: *"Combine `tool_choice: {"type": "any"}` with strict tool use to guarantee both that one of
your tools will be called AND that the tool inputs strictly follow your schema."* `[VOLATILE]`
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

**Fact 13 — missing-parameter behaviour differs by model.** *"If the user's prompt doesn't include
enough information to fill all the required parameters for a tool, Claude Opus is much more likely to
recognize that a parameter is missing and ask for it. Claude Sonnet might ask... But it might also
infer a reasonable value."* Model-selection guidance on the same page: *"Use the latest Claude Opus
model... for complex tools and ambiguous queries; it handles multiple tools better and seeks
clarification when needed. Use Claude Haiku models for straightforward tools, but note they may infer
missing parameters."* `[VOLATILE]` — model naming.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22

---

### Q11.2 — What exactly is the client-side vs server-side tool distinction?

**Fact 14 — the axis is stated explicitly, twice.** *"Tools differ primarily by where the code
executes."* And on the concepts page: *"The primary axis along which tools differ is where the code
executes. Every tool falls into one of three buckets, and the bucket determines what your application
is responsible for."*
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · both fetched 2026-08-22

**Fact 15 — the three buckets, named.** From the how-it-works page:
1. **User-defined tools (client-executed).** *"You write the schema, you execute the code, you return
   the results... the vast majority of tool-use traffic is user-defined tools calling into
   application-specific logic."*
2. **Anthropic-schema tools (client-executed).** *"Anthropic publishes the tool schema and your
   application handles execution."*
3. **Server-executed tools.** *"Anthropic runs the code. You enable the tool in your request and the
   server handles everything else. You never construct a `tool_result` block for these tools."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

> **The trap this sets.** "Client-side" does **not** mean "you wrote it." Bash, text editor, memory,
> computer use and browser use are Anthropic-authored schemas that are still **client** tools, because
> your application executes every call. The 2×2 the exam can exploit is *who wrote the schema* ×
> *who runs the code*, and only the second axis defines client vs server.

**Fact 16 — the current membership of each bucket** (from the Tool reference directory table):

| Tool | Execution |
|---|---|
| Web search | **Server** |
| Web fetch | **Server** |
| Code execution | **Server** |
| Advisor | **Server** (beta header) |
| Tool search | **Server** |
| MCP connector (`mcp_toolset`) | **Server** (beta header) |
| Memory | **Client** |
| Bash | **Client** |
| Text editor | **Client** |
| Computer use | **Client** (client toolset) |
| Browser use | **Client** (client toolset) |

Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference · fetched 2026-08-22
`[VOLATILE]` — the dated `type` strings on that page (e.g. `web_search_20260318`,
`code_execution_20260521`, `memory_20250818`, `computer_toolset_20260801`) and their beta headers. The
**membership of each column is the examinable fact**; the date suffixes are not.

**Fact 17 — the wire-level difference.** Client tools: *"Claude responds with `stop_reason: "tool_use"`
and one or more `tool_use` blocks. Your code executes the operation and sends back a `tool_result`."*
Server tools: *"run on Anthropic's infrastructure: you see the results directly without handling
execution."* Server calls appear as `server_tool_use` blocks whose `id` carries the `srvtoolu_` prefix,
*"to distinguish it from client tool calls"*, and *"Unlike client `tool_use` blocks, you don't need to
respond with a `tool_result`."*
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools · both fetched 2026-08-22

**Fact 18 — two loops, not one.** Client tools require the application to drive the loop: *"The model
can't run your code, so every tool call is a round trip."* The canonical shape is *"a `while` loop keyed
on `stop_reason`"*, repeating while `stop_reason` is `"tool_use"` and exiting on `"end_turn"`,
`"max_tokens"`, `"stop_sequence"` or `"refusal"`. Server tools run *"their own loop inside Anthropic's
infrastructure. A single request from your application might trigger several web searches or code
executions before a response comes back."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

**Fact 19 — `pause_turn` is the server loop's iteration cap, and it is not an error.** *"This internal
loop has an iteration limit. If the model is still iterating when it hits the cap, the response comes
back with `stop_reason: "pause_turn"` instead of `"end_turn"`."* Handling: pass the paused response back
as-is, keep the same tools in the continuation (*"the API returns a validation error if that tool is
missing from the continuation"*), and *"A continued turn can pause again."*
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools · both fetched 2026-08-22

**Fact 20 — the mixed-turn case, which is the one that breaks naive integrations.** When Claude calls a
server tool and a client tool in the same group of parallel calls, *"the API does not run the server
tool. It returns immediately so that you can run the client tool first."* Then `stop_reason` is
`"tool_use"`, **not** `pause_turn`; the `server_tool_use` block appears **with no result block**; and
*"There is no other marker. Detect the state by looking for a `server_tool_use` block whose `id` has no
matching result block in the response."* The follow-up user message *"must contain nothing except
`tool_result` blocks"* — adding text after them tells the API the assistant turn is over and the request
fails.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools · fetched 2026-08-22

**Fact 21 — the billing difference, which is a clean discriminator.** *"Client-side tools are priced the
same as any other Claude API request, although server-side tools can incur additional charges based on
their specific usage."* Named examples: web search charges per search; code execution has its own rate.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · fetched 2026-08-22

**Fact 22 — the compliance difference.** The basic versions of web search and web fetch are
*"eligible for Zero Data Retention (ZDR)"*; the newer versions with dynamic filtering are *"**not**
ZDR-eligible by default because dynamic filtering relies on code execution internally."* `[VOLATILE]` —
version-specific.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools · fetched 2026-08-22

**Fact 23 — why you would use an Anthropic-schema client tool instead of writing your own.** *"these
schemas are trained-in. Claude has been optimized on thousands of successful trajectories that use
these exact tool signatures, so it calls them more reliably and recovers from errors more gracefully
than it would with a custom tool that does the same thing. The schema is the interface the model
already expects."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

> **Chapter-level discriminator.** "Reimplement bash yourself as a custom tool" vs "declare the
> Anthropic bash tool" is a real exam-shaped fork, and the documented reason to prefer the second is
> reliability from training, not capability — both execute in your application either way.

**Fact 24 — Anthropic's own three-row choosing table**, verbatim columns:

| Approach | When to use it | What to expect |
|---|---|---|
| User-defined client tools | Custom business logic, internal APIs, proprietary data | You handle execution and the agentic loop |
| Anthropic-schema client tools | Standard dev operations (bash, file editing, desktop and browser control) | You handle execution; Claude calls the tool reliably because the schema is trained-in |
| Server-executed tools | Web search, code sandbox, web fetch | Anthropic handles execution; you read the results instead of producing them |

Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

**Fact 25 — a fourth position: the MCP connector is a server tool.** *"Claude's Model Context Protocol
(MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API
without a separate MCP client."* Its limits: *"only tool calls are currently supported"*, and *"The
server must be publicly exposed through HTTP... Local STDIO servers cannot be connected directly."*
`[VOLATILE]` — beta status.
Source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector · fetched 2026-08-22

---

### Q11.3 — What approval patterns are documented for tool execution?

**Finding first: there is no approval mechanism in the Messages API itself.** Approval on the raw
Messages API is *structural*, not a feature — because a client tool's `tool_use` block is returned to
your code and nothing executes until you send a `tool_result`, the approval point already exists in
your loop. I found no Messages API parameter that gates execution. The documented approval machinery
lives in the **Agent SDK** and in **Claude Managed Agents**, and they are different mechanisms. That
distinction is itself examinable.

**Fact 26 — Agent SDK: six-step evaluation order, in this order.** *"When Claude requests a tool, the
SDK checks permissions in this order"*:
1. **Hooks** — *"A hook can deny the call outright or pass it on. A hook that returns `allow` does not
   skip the deny and ask rules below."*
2. **Deny rules** — *"If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode."*
3. **Ask rules** — *"If an ask rule matches, the call falls through to your `canUseTool` callback for
   confirmation, even in `bypassPermissions` mode."*
4. **Permission mode**
5. **Allow rules** — *"If a rule matches, the tool is approved."*
6. **`canUseTool` callback** — *"If not resolved by any of the above."*

Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

> **The single most discriminating fact here:** deny beats allow, and hooks run before everything.
> *"For checks that must run on every tool call, use a `PreToolUse` hook: hooks run before every other
> step, and a hook deny applies even in `bypassPermissions` mode."*
> Corollary, stated as a warning: *"**Auto-approved tools never reach `canUseTool`.** A tool call
> approved at any earlier step... skips your `canUseTool` callback, so permission checks you put there
> are silently bypassed for that tool."*

**Fact 27 — Agent SDK permission modes**, verbatim behaviours:

| Mode | Behaviour |
|---|---|
| `default` | *"No auto-approvals; unmatched tools trigger your `canUseTool` callback"* |
| `dontAsk` | *"Anything not pre-approved... is denied... `canUseTool` is never called"* |
| `acceptEdits` | *"File edits and filesystem operations (`mkdir`, `rm`, `mv`, etc.) are automatically approved"* |
| `bypassPermissions` | *"Tools run without permission prompts, except for the actions no mode auto-approves"* |
| `plan` | *"Claude explores and plans without editing your source files; file edits are never auto-approved and prompt through your `canUseTool` callback"* |
| `auto` | *"A model classifier approves or denies permission prompts"* |

`[VOLATILE]` — mode names are SDK API surface. The **shape** (a spectrum from prompt-everything to
deny-everything to bypass-everything, with a planning mode that is read-only by construction) is the
durable fact.
Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

**Fact 28 — the documented locked-down recipe.** *"For a locked-down agent, pair `allowedTools` with
`permissionMode: "dontAsk"`. Listed tools are approved... anything else is denied outright instead of
prompting."* And the trap: *"**`allowed_tools` does not constrain `bypassPermissions`.**... Setting
`allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool."*
Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

**Fact 29 — removing a tool is different from denying it.** *"`disallowed_tools=["Bash"]` — The `Bash`
tool definition is removed from the request. Claude does not see the tool and cannot attempt it."*
Versus `disallowed_tools=["Bash(rm *)"]`: *"`Bash` stays available. Calls matching `rm *` are denied in
every permission mode."*
Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

> **Discriminator.** Scope-out (remove the definition) vs gate (deny a pattern) vs prompt (ask rule) are
> three different answers to "stop the agent doing X", and they differ in whether Claude can still see
> and attempt the tool. Removing it also saves the context the definition would occupy.

**Fact 30 — some calls always prompt, regardless of allow rules.** `AskUserQuestion`, MCP tools whose
server sets `_meta["anthropic/requiresUserInteraction"]`, and connector tools an organization has set to
`ask` *"always fall through to the callback, even when an allow rule matches."* In `dontAsk` mode they
are denied instead, *"because that mode never prompts."* `rm`/`rmdir` removals targeting a critical path
are *"never approved by an allow rule."* `[VOLATILE]` — the `_meta` key.
Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

**Fact 31 — subagent inheritance is a real security fact.** *"Subagents inherit the parent session's
permission mode."* A subagent definition's own `permissionMode` cannot override a parent using
`bypassPermissions`, `acceptEdits`, or `auto`. *"Subagents may have different system prompts and less
constrained behavior than your main agent, so inheriting `bypassPermissions` grants them full,
autonomous system access."*
Source: https://code.claude.com/docs/en/agent-sdk/permissions · fetched 2026-08-22

**Fact 32 — Managed Agents: only two policies, with asymmetric defaults.** *"Permission policies control
whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically or wait
for your approval."*
- `always_allow` — *"The tool executes automatically with no confirmation."*
- `always_ask` — *"The session pauses and waits for your approval before executing."*

*"Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets
default to `always_ask`."* The stated reason for the MCP default: *"This ensures that new tools added to
an MCP server do not execute in your application without approval."*
Source: https://platform.claude.com/docs/en/managed-agents/permission-policies · fetched 2026-08-22

> **Best single discriminator in the whole approval topic.** Anthropic runs the built-in toolset and
> trusts it by default; a third party runs the MCP server and can change its tool list underneath you,
> so that side asks by default. The asymmetry follows from *who can change the capability*, which is the
> exact spine of Chapter 13.

**Fact 33 — Managed Agents approval flow, four steps as documented.** (1) session emits
`agent.tool_use` or `agent.mcp_tool_use`; (2) *"The session pauses with a `session.status_idle` event
whose `stop_reason.type` is `requires_action`... The session waits indefinitely for a response."*;
(3) you send a `user.tool_confirmation` event per blocking event with `result` of `"allow"` or
`"deny"`, optionally a `deny_message`; (4) *"Denied tools do not run, and the agent receives a tool
result saying the call was rejected, including your `deny_message`."* `[VOLATILE]` — event names.
Source: https://platform.claude.com/docs/en/managed-agents/permission-policies · fetched 2026-08-22

**Fact 34 — custom tools are outside the policy system entirely.** *"Permission policies do not apply to
custom tools. When the agent invokes a custom tool, your application receives an
`agent.custom_tool_use` event and is responsible for deciding whether to execute it."* And on the tools
page: *"Custom tools are executed by your application and controlled by you, so they are not governed by
permission policies."*
Sources: https://platform.claude.com/docs/en/managed-agents/permission-policies ·
https://platform.claude.com/docs/en/managed-agents/tools · both fetched 2026-08-22

**Fact 35 — denial is a first-class outcome, not an exception.** *"When a tool is denied, Claude
receives a rejection message as the tool result and typically attempts a different approach or reports
that it couldn't proceed."*
Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22

**Fact 36 — hooks are the enforcement layer; prompts are not.** *"Put guardrails in hooks. An
instruction like 'never edit `.env`' in CLAUDE.md or a skill is a request, not a guarantee. A
`PreToolUse` hook that blocks the edit is enforcement. If a rule must hold every time, make it a hook
rather than a prompt instruction."* This lines up with the blueprint's Domain 7 skill "Claude Hooks —
hooks as guardrails to prevent destructive actions."
Source: https://code.claude.com/docs/en/features-overview · fetched 2026-08-22

**Fact 37 — a coarser approval pattern: never expose the tool.** In the MCP connector, *"Denylisting
write or destructive tools is recommended when building read-only assistants, or when you want a human
confirmation step before state changes."*
Source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector · fetched 2026-08-22

---

### Q11.4 — How many tools, and what about overlapping or ambiguous tool sets?

**Fact 38 — the number that matters most, and it is quantified.** *"Claude's ability to pick the right
tool degrades once you exceed 30–50 available tools."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool · fetched 2026-08-22
`[VOLATILE]` as an exact range, but this is the closest thing Anthropic publishes to an answer for
"how many tools is too many", and it is worth teaching as an order of magnitude.

**Fact 39 — the context cost of a realistic tool set.** *"A typical multiserver setup (GitHub, Slack,
Sentry, Grafana, and Splunk) can consume ~55k tokens in definitions before Claude does any work. Tool
search typically reduces this by over 85 percent, loading only the 3–5 tools Claude needs for a given
request."* `[VOLATILE]` — figures.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool · fetched 2026-08-22

**Fact 40 — the documented decision rule for tool search, both directions.** Use tool search when
*"You have 10 or more tools available"*, *"Your tool definitions consume more than 10k tokens"*, *"Tool
selection accuracy drops as your toolset grows"*, *"You aggregate multiple MCP servers (200+ tools)"*,
or *"Your tool library grows over time."* Do **not** use it when *"you have fewer than 10 tools, every
tool is used in every request, or your tool definitions are small (less than 100 tokens total)."*
`[VOLATILE]` — thresholds.
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool · fetched 2026-08-22

> **Discriminator.** Tool search is the answer to *context bloat and selection accuracy at scale*, not
> to a single ambiguous pair of tools. For two overlapping tools, the fix is consolidation or clearer
> negative scope in the description.

**Fact 41 — consolidate rather than proliferate.** *"Consolidate related operations into fewer tools.
Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them
into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and
make your tool surface easier for Claude to navigate."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools · fetched 2026-08-22
Restated identically for Managed Agents custom tools at
https://platform.claude.com/docs/en/managed-agents/tools · fetched 2026-08-22

**Fact 42 — namespacing is a named remedy for ambiguity.** *"Use meaningful namespacing in tool names.
When your tools span multiple services or resources, prefix names with the service (for example,
`github_list_prs`, `slack_send_message`). This makes tool selection unambiguous as your library grows,
and is especially important when using tool search."* The engineering post gives both axes: by service
(`asana_search`, `jira_search`) or by resource (`asana_projects_search`, `asana_users_search`).
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools ·
https://www.anthropic.com/engineering/writing-tools-for-agents · both fetched 2026-08-22

**Fact 43 — the harm from overlap, in Anthropic's own words.** *"More tools don't always lead to better
outcomes."* *"When tools overlap in function or have a vague purpose, agents can get confused about
which ones to use."* *"Too many tools or overlapping tools can also distract agents from pursuing
efficient strategies."* Prescription: build *"a few thoughtful tools targeting specific high-impact
workflows"* rather than wrapping every API endpoint.
Source: https://www.anthropic.com/engineering/writing-tools-for-agents · fetched 2026-08-22

> **This is the sharpest anti-pattern statement available and it contradicts the instinct the exam
> tests** — "wrap every endpoint as a tool so Claude has full coverage" is the plausible-sounding wrong
> answer.

**Fact 44 — tool *responses* are part of tool-set design, not an afterthought.** *"Design tool responses
to return only high-signal information. Return semantic, stable identifiers (for example, slugs or
UUIDs) rather than opaque internal references... Bloated responses waste context and make it harder for
Claude to extract what matters."* Engineering post adds *"pagination, range selection, filtering, and/or
truncation with sensible default parameter values"*, and notes responses are truncated to 25,000 tokens
by default `[VOLATILE]`, with a preference for *"many small and targeted searches instead of a single,
broad search."*
Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools ·
https://www.anthropic.com/engineering/writing-tools-for-agents · both fetched 2026-08-22

**Fact 45 — the framing sentence for the whole chapter.** *"Tools are a new kind of software which
reflects a contract between deterministic systems and non-deterministic agents."* Traditional software
guarantees identical outputs; agents may misunderstand tools, so tools must be *"optimized for agent
reasoning rather than developer convenience."*
Source: https://www.anthropic.com/engineering/writing-tools-for-agents · fetched 2026-08-22

**Fact 46 — a supporting statement of the same contract from the docs.** *"Tool use is a contract
between your application and the model. You specify what operations are available and what shape their
inputs and outputs take; Claude determines when and how to call them. The model never executes anything
on its own."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

**Fact 47 — when a tool is the wrong answer at all.** Tools fit for *"Actions with side effects"*,
*"Fresh or external data"*, *"Structured, guaranteed-shape outputs"*, and *"Calling into existing
systems"*. Tools do not fit when *"The model can answer from training alone"*, *"The interaction is
one-shot Q&A with no side effects"*, or *"Tool-calling latency would dominate a trivial response."*
Diagnostic line worth teaching: *"if you're writing a regex to extract a decision from model output,
that decision should have been a tool call."*
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · fetched 2026-08-22

**Fact 48 — MCP-specific restatement.** *"With many tools available, Claude selects based on tool names
and descriptions. Clear, specific tool descriptions improve selection accuracy. For large tool sets
(dozens of tools across several servers), consider enabling `defer_loading` with the Tool search tool."*
And a discriminator on when an MCP tool is *not* called: *"Claude does not call an MCP tool for general
knowledge questions about a connected service. Asking 'how do Notion databases work?' with a Notion
server attached is answered directly; asking 'what's in my Projects database?' triggers the tool."*
Source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector · fetched 2026-08-22

---

## CHAPTER 13 — "Four ways to hand Claude a capability"

### Q13.1 — What built-in / server-side tools does Anthropic currently ship and run?

**Fact 49 — the Messages API server tools, named.** Server-executed (Anthropic runs the code):
**web search · web fetch · code execution · advisor · tool search · MCP connector**.
Source (directory table): https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference ·
fetched 2026-08-22

One-line purposes as Anthropic states them on the overview page:
- **Web search** — *"Search the web for information beyond the knowledge cutoff, with cited sources."*
- **Web fetch** — *"Retrieve the full content of specified web pages and PDF documents."*
- **Code execution** — *"Run Python and bash code in a sandboxed container to analyze data and generate files."*
- **Advisor** — *"Let a faster executor model consult a higher-intelligence advisor model mid-generation."*
- **Tool search** — *"Work with thousands of tools by discovering and loading them on demand."*
- **MCP connector** — *"Connect to remote MCP servers from the Messages API without a separate MCP client."*

Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · fetched 2026-08-22

**Fact 50 — the Anthropic-schema *client* tools, named.** **memory · bash · text editor · computer use ·
browser use.** These ship with Anthropic's schema but *"your application handles execution."* One-line
purposes:
- **Memory** — *"Store and retrieve information across conversations in files you control."*
- **Bash** — *"Run shell commands in a persistent session that maintains state."*
- **Text editor** — *"View and modify text files to debug, fix, and improve code."*
- **Computer use** — *"Take screenshots and control the mouse and keyboard in a desktop environment."*
- **Browser use** — *"Navigate, read, and interact with webpages in your own browser environment."*

Sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works · both fetched 2026-08-22

> **Chapter 13 discriminator.** "Built-in tool" is not one category. Six run on Anthropic's servers and
> five are Anthropic-schema tools your application runs. A scenario that says "we cannot let anything
> execute outside our VPC" rules out the server six and keeps the client five.

**Fact 51 — computer use and browser use are *toolsets*, not single tools.** *"one entry in `tools`
declares a fixed set of member tools whose names, descriptions, and input schemas Anthropic defines, and
your application executes every call. The entry takes no `name`, because the dated `type` fixes the
member names."* They reject `strict: true` and `input_examples`, and *"A `tool_choice` of type `tool`
that names the toolset or a member"* is rejected. `[VOLATILE]`
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference · fetched 2026-08-22

**Fact 52 — Managed Agents ships a *different* built-in toolset.** Eight tools, all enabled by default:
`bash`, `read`, `write`, `edit`, `glob`, `grep`, `web_fetch`, `web_search`. Enabled as a single
`agent_toolset_20260401` entry `[VOLATILE]`. Explicit note: *"Client toolsets are Messages API tools.
They aren't currently available as agent tools in Claude Managed Agents, which provides its own built-in
agent toolset, MCP toolsets, and custom tools."*
Sources: https://platform.claude.com/docs/en/managed-agents/tools ·
https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference · both fetched 2026-08-22

**Fact 53 — the Agent SDK ships a third built-in tool list.** *"The SDK includes the same tools that
power Claude Code"*: file operations `Read`, `Edit`, `Write`; search `Glob`, `Grep`; execution `Bash`;
web `WebSearch`, `WebFetch`; discovery `ToolSearch`; orchestration `Agent`, `Skill`, `AskUserQuestion`,
`TaskCreate`, `TaskUpdate`. `[VOLATILE]` — tool names.
Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22

> **The exam-relevant shape:** "built-in tools" means three different lists depending on which surface
> you are on — Messages API, Managed Agents, Agent SDK. They overlap (bash, web search, web fetch appear
> in all three) but they are not the same set and are not configured the same way.

---

### Q13.2 — What is a Skill, precisely?

**Fact 54 — the definition.** *"Agent Skills are modular capabilities that extend Claude's
functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates)
that Claude uses automatically when relevant."* And: *"Skills are reusable, filesystem-based resources
that give Claude domain-specific expertise: workflows, context, and best practices that turn a
general-purpose agent into a specialist."*
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

Engineering-blog phrasing: *"organized folders of instructions, scripts, and resources that agents can
discover and load dynamically to perform better at specific tasks."*
Source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ·
fetched 2026-08-22

**Fact 55 — what a Skill contains.** *"Every Skill requires a `SKILL.md` file with YAML frontmatter."*
Required frontmatter fields are **`name` and `description`**, and nothing else is required. Constraints:
`name` max 64 characters, lowercase letters/numbers/hyphens only, no XML tags, and *"Cannot contain
reserved words: 'anthropic', 'claude'"*; `description` non-empty, max 1024 characters, no XML tags.
`[VOLATILE]` — limits. Optional bundled content: extra markdown files, executable scripts, and reference
resources such as schemas or templates.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 56 — how a Skill is loaded: three levels of progressive disclosure.**

| Level | When loaded | Token cost | Content |
|---|---|---|---|
| 1 · Metadata | Always, at startup | *"~100 tokens per Skill"* | `name` and `description` from frontmatter |
| 2 · Instructions | When the Skill is triggered | *"Under 5k tokens"* | The SKILL.md body |
| 3+ · Resources | As needed | *"None until accessed"* | Bundled files; *"Scripts run through bash, and only their output enters context"* |

`[VOLATILE]` — the token figures.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 57 — the loading mechanism is literally the filesystem.** *"Skills run in a code execution
environment where Claude has filesystem access, bash commands, and code execution capabilities... When a
Skill is triggered, Claude uses bash to read SKILL.md from the filesystem, bringing its instructions into
the context window."* Worked sequence given: startup → user request → `bash: cat pdf-processing/SKILL.md`
→ Claude decides FORMS.md is not needed → executes.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 58 — the description is the trigger, and this mirrors Chapter 11 exactly.** *"The `description` is
what Claude matches your request against when determining whether to trigger the Skill, so it must say
both what the Skill does and when to use it."* Consequence: *"This lightweight approach means you can
install many Skills without context penalty: until a Skill is triggered, only its name and description
occupy context."*
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

> **Cross-chapter link worth teaching once:** the failure mode is identical for tools and for Skills —
> a vague description means the wrong one is selected. Claude Code docs say it outright: *"If
> descriptions are vague or overlap, Claude may load the wrong skill or miss one that would help."*
> (https://code.claude.com/docs/en/features-overview · fetched 2026-08-22)

**Fact 59 — what a Skill cannot do #1: it needs code execution.** *"Using Skills through the API requires
the code execution tool, whose container Skills run in."* A Skill is invoked by specifying a `skill_id`
in the `container` parameter alongside the code execution tool. `[VOLATILE]` — parameter names.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 60 — what a Skill cannot do #2: on the API, no network and no package installs.** Claude API
runtime constraints, verbatim: *"**No network access:** Skills cannot make external API calls or access
the internet."* · *"**No runtime package installation:** Only pre-installed packages are available."* ·
*"**Pre-configured dependencies only.**"* By contrast, in **Claude Code** Skills have *"Full network
access... the same network access as any other program on the user's computer"*, and on claude.ai
network access varies by user/admin settings.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

> **This is the single hardest discriminator in Chapter 13 and it is directly examinable.** "Package our
> internal API integration as a Skill" fails on the Claude API, because the Skill sandbox has no network.
> An integration that must reach an external or internal system needs a **tool** or an **MCP server**,
> not a Skill. The same Skill would work in Claude Code, where the sandbox is the user's machine.

**Fact 61 — what a Skill cannot do #3: it does not sync across surfaces.** *"**Custom Skills do not sync
across surfaces**. Skills uploaded to one surface are not automatically available on others."* Sharing
scope differs too: claude.ai is **individual user only** with *"no centralized admin management or
org-wide distribution"*; the Claude API is **workspace-wide**; Claude Code is personal
(`~/.claude/skills/`) or project (`.claude/skills/`), and can be shared through plugins.
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 62 — what a Skill cannot do #4: it is not a security boundary; it is an attack surface.** *"Use
Skills only from trusted sources... a malicious Skill can direct Claude to invoke tools or execute code
in ways that don't match the Skill's stated purpose."* And *"Treat like installing software."* Skills are
also *"not covered by ZDR arrangements."*
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

**Fact 63 — the pre-built Skills Anthropic ships.** PowerPoint (`pptx`), Excel (`xlsx`), Word (`docx`),
PDF (`pdf`) — available on the Claude API, Claude Platform on AWS, Microsoft Foundry, and claude.ai.
*"The pre-built document Skills (PowerPoint, Excel, Word, PDF) are not available in Claude Code."*
Open-source: the Claude API skill, *"Bundled with Claude Code."* `[VOLATILE]`
Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · fetched 2026-08-22

---

### Q13.3 — What distinguishes a Skill from a tool in Anthropic's own framing?

**Fact 64 — the one-sentence version Anthropic publishes.** *"MCP connects Claude to data; Skills teach
Claude what to do with that data."*
Source: https://claude.com/blog/skills-explained · fetched 2026-08-22

**Fact 65 — the same split, restated with the choosing rule.** *"If you're explaining how to use a tool
or follow procedures... that's a Skill. If you need Claude to access the database or Excel files in the
first place, that's MCP."* Use both: *"MCP for connectivity, Skills for procedural knowledge."*
Source: https://claude.com/blog/skills-explained · fetched 2026-08-22

**Fact 66 — the docs' table version.** *"MCP connects Claude to external services. Skills extend what
Claude knows, including how to use those services effectively."*

| Aspect | MCP | Skill |
|---|---|---|
| What it is | Protocol for connecting to external services | Knowledge, workflows, and reference material |
| Provides | Tools and data access | Knowledge, workflows, reference material |
| Examples | Slack integration, database queries, browser control | Code review checklist, deploy workflow, API style guide |

Plus the pairing pattern: *"MCP connects to your database, a skill documents your schema and query
patterns."*
Source: https://code.claude.com/docs/en/features-overview · fetched 2026-08-22

**Fact 67 — Skills are complementary to MCP, not a replacement, stated by Anthropic Engineering.**
*"Skills can complement Model Context Protocol (MCP) servers by teaching agents more complex workflows
that involve external tools and software."*
Source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ·
fetched 2026-08-22

**Fact 68 — Skill vs prompt.** *"Unlike prompts (conversation-level instructions for one-off tasks),
Skills load on demand, so you don't have to repeat the same guidance across conversations."* Blog
version: *"If you find yourself typing the same prompt repeatedly across multiple conversations, it's
time to create a Skill."*
Sources: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview ·
https://claude.com/blog/skills-explained · both fetched 2026-08-22

**Fact 69 — Skill vs Project (claude.ai framing) and Skill vs subagent.**
*"Projects say 'here's what you need to know.' Skills say 'here's how to do things.'"*
*"Use Skills when you want capabilities that any Claude instance can load. Use subagents when you need
complete, self-contained agents designed for specific purposes."*
Source: https://claude.com/blog/skills-explained · fetched 2026-08-22

**Fact 70 — Skill vs hook, which is the determinism axis.**

| Aspect | Hook | Skill |
|---|---|---|
| Triggered by | Lifecycle events such as `PostToolUse` or `SessionStart` | You typing `/<name>`, or Claude matching the description to your task |
| Determinism | *"Always fires on its event; the trigger is guaranteed"* | *"Claude interprets the instructions; outcome can vary"* |
| Context cost | *"Zero unless the hook returns output"* | *"Description loads each session; full content loads when used"* |

Source: https://code.claude.com/docs/en/features-overview · fetched 2026-08-22

**Fact 71 — context cost by mechanism, the table that makes the four-way comparison teachable.**

| Feature | When it loads | Context cost |
|---|---|---|
| CLAUDE.md | Session start | *"Every request"* |
| Skills | Session start + when used | *"Low (descriptions every request)"* |
| MCP servers | Session start | *"Low until a tool is used"* — tool names load, *"full schemas on demand"* |
| Subagents | When spawned | *"Isolated from main session"* |
| Hooks | On trigger | *"Zero, unless hook returns additional context"* |

Source: https://code.claude.com/docs/en/features-overview · fetched 2026-08-22
`[VOLATILE]` — this table is Claude Code-scoped, and MCP tool search being on by default is a
current-behaviour statement.

---

### Q13.4 — Is there official guidance comparing all four options for a use case?

**Finding — and this is itself a result.** **No single Anthropic page compares built-in tool vs custom
tool vs Skill vs MCP server as a four-way choice for a use case.** I searched
`platform.claude.com`, `docs.claude.com`, `code.claude.com`, `anthropic.com` and `claude.com` and found
four partial comparisons instead, each covering a different subset:

1. **Three tool types only** (user-defined client / Anthropic-schema client / server-executed) — the
   "Choosing between approaches" table at
   https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works. No Skills, no MCP.
   Fetched 2026-08-22. Reproduced above as Fact 24.
2. **Skills vs prompts vs Projects vs MCP vs subagents** — https://claude.com/blog/skills-explained.
   Consumer/product framing; does not distinguish built-in from custom tools. Fetched 2026-08-22.
3. **CLAUDE.md vs Skills vs subagents vs MCP vs hooks vs plugins** —
   https://code.claude.com/docs/en/features-overview. Claude Code-scoped, not API-scoped; treats "tools"
   as the built-in baseline rather than as a choice. Fetched 2026-08-22.
4. **A blog post explicitly on choosing** — *"Steering Claude Code: when to use CLAUDE.md, skills, hooks,
   and subagents"*, linked from the features overview at
   https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more. **I did not fetch
   this page** — recorded in the gap list.

**Consequence for the chapter:** the four-way comparison must be **derived** from the primitives, not
cited. The derivation the sources support is the ownership question the chapter title already poses —
*who owns the capability when it changes*:

| Option | Who writes it | Who executes it | Who must ship a change | Reach beyond the sandbox |
|---|---|---|---|---|
| Built-in server tool | Anthropic | **Anthropic** | Anthropic (you pick a version) | Yes, by design (web) |
| Built-in client tool (Anthropic schema) | Anthropic | **Your application** | Anthropic for the schema; you for the handler | Whatever your handler can reach |
| Custom tool | You | **Your application** | You, in your app deploy | Whatever your app can reach |
| Skill | You (or Anthropic, for pre-built) | Claude, inside a code-execution sandbox | You, by editing a file — no app deploy | **No network on the Claude API** (Fact 60) |
| MCP server | You or a third party | **The MCP server**, independently hosted | Whoever maintains the server — independently of your app | Yes, whatever the server can reach |

Every row is sourced above: server/client execution split (Facts 14–16), custom tools as your app's
responsibility (Fact 15, Fact 34), Skills as filesystem-loaded instructions in the code-execution
container with no API network access (Facts 57, 59, 60), MCP as an independently maintained connection
layer (Facts 25, 66, 72–76).

**Fact 72 — the exam's own worked instance of this decision.** Official sample question 3, recorded in
`EXAM-FACTS_v1.md` §5: an internal REST service, reusable across apps, independently maintained →
**build an MCP server**, over prompt hard-coding, pasting data, or a built-in tool. The discriminators
in that stem are *reusable across applications* and *independently maintained*, which map to the last
two columns of the table above.
Source (local, verified): `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude Certified Developer Foundations\EXAM-FACTS_v1.md` §5 · read 2026-08-22

---

### Q13.5 — Supporting MCP facts the chapter needs

**Fact 73 — what MCP is.** *"MCP (Model Context Protocol) is an open-source standard for connecting AI
applications to external systems."* The analogy Anthropic and the spec both use: *"Think of MCP like a
USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices,
MCP provides a standardized way to connect AI applications to external systems."* Benefit stated for
developers: *"MCP reduces development time and complexity when building, or integrating with, an AI
application or agent"*, and for the ecosystem, *"build once and integrate everywhere."*
Source: https://modelcontextprotocol.io/docs/getting-started/intro · fetched 2026-08-22

**Fact 74 — host / client / server, and the one-client-per-server rule.** *"MCP follows a client-server
architecture where an MCP host — an AI application like Claude Code or Claude Desktop — establishes
connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP client for
each MCP server."* Definitions: **Host** = *"The AI application that coordinates and manages one or
multiple MCP clients"*; **Client** = *"A component that maintains a connection to an MCP server"*;
**Server** = *"A program that provides context to MCP clients."*
Source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture · fetched 2026-08-22

**Fact 75 — the three server primitives.** *"MCP defines three core primitives that servers can
expose"*:
- **Tools** — *"Executable functions that AI applications can invoke to perform actions (e.g., file
  operations, API calls, database queries)"*
- **Resources** — *"Data sources that provide contextual information to AI applications (e.g., file
  contents, database records, API responses)"*
- **Prompts** — *"Reusable templates that help structure interactions with language models (e.g., system
  prompts, few-shot examples)"*

Each has `*/list` for discovery, `*/get` for retrieval, and `tools/call` for execution.
Source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture · fetched 2026-08-22

**Fact 76 — the two transports, and which is which.** *"**Stdio transport**: Uses standard input/output
streams for direct process communication between local processes on the same machine, providing optimal
performance with no network overhead."* · *"**Streamable HTTP transport**: Uses HTTP POST for
client-to-server messages with optional Server-Sent Events for streaming... This transport enables
remote server communication and supports standard HTTP authentication methods including bearer tokens,
API keys, and custom headers. MCP recommends using OAuth to obtain authentication tokens."* And the
cardinality: *"Local MCP servers that use the STDIO transport typically serve a single MCP client,
whereas remote MCP servers that use the Streamable HTTP transport will typically serve many MCP
clients."*
Source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture · fetched 2026-08-22

> Matches the blueprint's Domain 8 skill wording exactly: *"communication patterns — stdio, sockets,
> client vs server."*

**Fact 77 — two layers, and MCP's deliberate non-scope.** *"MCP consists of two layers"*: a **data
layer** (*"the JSON-RPC based protocol... including capability and version discovery, and core
primitives"*) and a **transport layer** (*"the communication mechanisms and channels"*). Scope note:
*"MCP focuses solely on the protocol for context exchange — it does not dictate how AI applications use
LLMs or manage the provided context."*
Source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture · fetched 2026-08-22

**Fact 78 — client primitives, with a live deprecation.** **Elicitation** — *"Allows servers to request
additional information from users... or ask for confirmation of an action."* **Sampling** and
**logging** are *"deprecated as of protocol version `2026-07-28`"*; for sampling, *"New implementations
should integrate directly with LLM provider APIs."* `[VOLATILE]` — and note `EXAM-FACTS_v1.md` §2 records
that **no MCP specification revision is named anywhere in the exam guide v1.0**, and treats
revision-specific detail as out of scope. Teach elicitation as a concept; do not teach the deprecation
as examinable.
Source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture · fetched 2026-08-22

---

## CHAPTER 16 — "Who runs the loop"

### Q16.1 — What is the Claude Agent SDK and what does it give you over a hand-written loop?

**Fact 79 — the definition, in one line.** *"The Agent SDK gives you the same tools, agent loop, and
context management that power Claude Code, programmable in Python and TypeScript."* Tagline: *"Build
production AI agents with Claude Code as a library."*
Source: https://code.claude.com/docs/en/agent-sdk/overview · fetched 2026-08-22

**Fact 80 — Anthropic's own four-way placement table**, which is the spine of this chapter:

| If you're... | Use | Why |
|---|---|---|
| Building an agent without implementing the tool loop yourself | **Agent SDK** | *"A library that runs the agent loop in your own process, in Python or TypeScript."* |
| Doing interactive development or running one-off tasks from a terminal | **Claude Code CLI** | *"The terminal interface, built for daily interactive use."* |
| Calling the API directly and implementing the tool loop yourself | **Client SDK** | *"Direct access to the Anthropic API rather than to Claude Code. You implement the tool loop yourself."* |
| Running long-running or asynchronous agents without managing your own sandbox or session infrastructure | **Managed Agents** | *"Hosted REST API, a separate product from the Agent SDK. **Anthropic runs the agent and the sandbox.**"* |

Source: https://code.claude.com/docs/en/agent-sdk/overview · fetched 2026-08-22

> **This table answers the chapter title directly.** Raw loop → your process, your code. Agent SDK →
> your process, Anthropic's loop implementation. Managed Agents → Anthropic's process, Anthropic's loop.

**Fact 81 — languages, and the escape hatch.** *"The SDK is available as a library for Python and
TypeScript only. To drive the same agent loop from another language, run the CLI as a subprocess with
the `-p` flag and `--output-format json`."* Both SDKs *"bundle a native Claude Code binary, so most
installs need no separate Claude Code install."*
Sources: https://code.claude.com/docs/en/agent-sdk/overview ·
https://code.claude.com/docs/en/agent-sdk/agent-loop · both fetched 2026-08-22

**Fact 82 — the capability list, verbatim.** *"Everything that makes Claude Code powerful is available in
the SDK."*
- **Built-in tools** — *"Read, write, edit files, run commands, and search the web"*
- **Hooks** — *"Run custom code at key points in the agent lifecycle"*
- **Subagents** — *"Spawn specialized agents for focused subtasks"*
- **MCP** — *"Connect external tools and data sources via the Model Context Protocol"*
- **Permissions** — *"Control which tools run automatically, which need approval"*
- **Sessions** — *"Maintain context across exchanges, resume or fork later"*
- **Skills, commands, and memory** — *"Load automatically from your project's `.claude/` and from
  `~/.claude/`, same as Claude Code"*
- **Plugins** — *"Package skills, agents, hooks, and MCP servers, and load them by local path"*

Source: https://code.claude.com/docs/en/agent-sdk/overview · fetched 2026-08-22

**Fact 83 — the five loop steps.** Receive prompt (with system prompt, tool definitions, history) →
evaluate and respond → execute tools → repeat → return result. *"Each full cycle is one turn... Claude
continues calling tools and processing results until it produces a response with no tool calls."* A turn
*"happens without yielding control back to your code."*
Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22

**Fact 84 — the four things the SDK does that a hand-written loop does not, all sourced.**

1. **Automatic compaction.** *"When the context window approaches its limit, the SDK automatically
   compacts the conversation: it summarizes older history to free space, keeping your most recent
   exchanges and key decisions intact."* With the caveat that matters for design: *"Compaction replaces
   older messages with a summary, so specific instructions from early in the conversation may not be
   preserved. Persistent rules belong in CLAUDE.md... because CLAUDE.md content is re-injected on every
   request."*
2. **Budget and turn caps.** `max_turns` / `maxTurns` (*"counts tool-use turns only"*) and
   `max_budget_usd` / `maxBudgetUsd`. *"Without limits, the loop runs until Claude finishes on its own,
   which is fine for well-scoped tasks but can run long on open-ended prompts... Setting a budget is a
   good default for production agents."* The budget cap covers subagents.
3. **Permission evaluation** (Facts 26–31) and **hooks** — *"Hooks run in your application process, not
   inside the agent's context window, so they don't consume context."*
4. **Session persistence** — *"When you resume, the full context from previous turns is restored... You
   can also fork a session to branch into a different approach."*

Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22 · `[VOLATILE]` on option names

**Fact 85 — parallelism is handled per tool kind.** *"Read-only tools (like `Read`, `Glob`, `Grep`, and
MCP tools marked as read-only) can run concurrently. Tools that modify state (like `Edit`, `Write`, and
`Bash`) run sequentially to avoid conflicts. Custom tools default to sequential execution."*
Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22

**Fact 86 — the documented context-management strategies, which are Domain 6 material reached through
Domain 1.** Use subagents for subtasks (*"Each subagent starts with a fresh conversation... only its
final response returns to the parent as a tool result. The main agent's context grows by that summary,
not by the full subtask transcript."*); be selective with tools (*"Every tool definition takes context
space."*); watch MCP server costs; use lower effort for routine tasks.
Source: https://code.claude.com/docs/en/agent-sdk/agent-loop · fetched 2026-08-22

**Fact 87 — a branding constraint that could plausibly appear in a partner-facing item.** For partners
integrating the SDK, permitted: *"Claude Agent"*, *"Claude"*, *"{YourAgentName} Powered by Claude"*. Not
permitted: *"Claude Code"* or *"Claude Code Agent"*, or Claude Code-branded visual elements. Also: *"Anthropic
does not allow third party developers to offer claude.ai login or rate limits for their products,
including agents built on the Claude Agent SDK. Use the API key authentication methods."*
Source: https://code.claude.com/docs/en/agent-sdk/overview · fetched 2026-08-22

---

### Q16.2 — What are Claude Managed Agents, and what is the self-hosted vs Anthropic-hosted distinction?

**Fact 88 — the definition and the two-way table Anthropic leads with.**

|  | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | *"Direct model prompting access"* | *"Pre-built, configurable agent harness that runs in managed infrastructure"* |
| Best for | *"Custom agent loops and fine-grained control"* | *"Long-running tasks and asynchronous work"* |

Expanded: *"Instead of building your own agent loop, tool execution, and runtime, you get a fully
managed environment where Claude can read files, run commands, browse the web, and run code securely.
The harness supports built-in prompt caching, compaction, and other performance optimizations."*
Source: https://platform.claude.com/docs/en/managed-agents/overview · fetched 2026-08-22

**Fact 89 — the four core concepts, and note that Environment is where the hosting question lives.**
- **Agent** — *"The model, system prompt, tools, MCP servers, and skills"*
- **Environment** — *"Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a
  self-hosted sandbox on your own infrastructure"*
- **Session** — *"A running agent instance within an environment"*
- **Events** — *"Messages exchanged between your application and the agent"*

Source: https://platform.claude.com/docs/en/managed-agents/overview · fetched 2026-08-22

**Fact 90 — when to use Managed Agents, as documented.** Long-running execution (*"minutes or hours with
multiple tool calls"*); cloud infrastructure; self-hosted execution *"for compliance or data-residency
requirements"*; minimal infrastructure (*"No need to build your own agent loop, sandbox, or tool
execution layer"*); stateful sessions (*"Persistent filesystems and conversation history"*); scheduled
execution on a cron schedule.
Source: https://platform.claude.com/docs/en/managed-agents/overview · fetched 2026-08-22

**Fact 91 — the self-hosted distinction, in one sentence.** *"Self-hosted sandboxes keep the
orchestration on Anthropic's side but move tool execution into infrastructure you control, so the
agent's code, filesystem, and network egress never leave your environment."*
Source: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes · fetched 2026-08-22

> **This is the fact the chapter is built around.** Self-hosted does **not** mean you run the agent. The
> model, the loop, and the session state stay with Anthropic in both modes. Only *tool execution* moves.
> The plausible-but-wrong option in an exam item is "self-hosted means running the whole agent
> yourself" — that is the Agent SDK, not Managed Agents.

**Fact 92 — what moves and what does not, as a table:**

| Aspect | Cloud (Anthropic-hosted) | Self-hosted |
|---|---|---|
| Tool execution | Anthropic sandboxes | **Your infrastructure** |
| Agent orchestration | Anthropic | **Anthropic** |
| Claude model | Anthropic | **Anthropic** |
| Network egress | Anthropic's controls | **Your network policy** |

And the data-flow caveat: *"Tool inputs and outputs still flow to Anthropic's control plane (where
Claude runs) so the model can see results and determine what to do next."*
Source: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes · fetched 2026-08-22

**Fact 93 — what self-hosting costs you.** You provide a Linux host with `/bin/bash`, and an
**environment worker**: a process that polls Anthropic's work queue, claims sessions assigned to your
environment, downloads the agent's skills, executes tool calls locally, and posts results back. You are
also responsible for containerization/sandboxing, network and egress policy, credential management, and
staging files into the sandbox. Claiming can be done by *"an always-on worker that polls continuously,
or a webhook-triggered handler that wakes on `session.status_run_started`."* `[VOLATILE]` — event name.
Source: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes · fetched 2026-08-22

**Fact 94 — the documented reason to choose self-hosted.** *"Self-hosting is a good fit when the agent
needs to operate on data that cannot leave your network boundary, reach internal services that are not
publicly routable, or run under your organization's own compliance and audit controls."*
Source: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes · fetched 2026-08-22

> **Three discriminators, cleanly separable:** data residency · non-routable internal services ·
> own compliance/audit controls. An exam stem that names any one of these points at self-hosted; a stem
> about *latency* or *cost* does not.

**Fact 95 — a compliance consequence of statefulness.** *"Claude Managed Agents is stateful by design:
sessions are long-running, resume cleanly after pauses, and store conversation history, sandbox state,
and outputs server-side. Because of this, Managed Agents is not currently eligible for Zero Data
Retention (ZDR) or HIPAA Business Associate Agreement (BAA) coverage."* You can delete sessions and
uploaded files through the API at any time. `[VOLATILE]` — eligibility can change.
Source: https://platform.claude.com/docs/en/managed-agents/overview · fetched 2026-08-22

**Fact 96 — a boundary that catches people out.** Web search and web fetch on Managed Agents *"run on
Anthropic's servers whether the environment is a cloud or self-hosted sandbox."* An environment's
`networking` settings govern the sandbox's own outbound traffic and *"do not affect `web_search` or
`web_fetch`."* Restricting those requires per-tool `allowed_domains` / `blocked_domains`.
Source: https://platform.claude.com/docs/en/managed-agents/tools · fetched 2026-08-22

**Fact 97 — self-hosted also unlocks tool reach.** *"If your sessions run in a self-hosted sandbox, the
environment worker can serve custom tools from your sandbox, including tools that wrap an MCP server
inside your network."*
Source: https://platform.claude.com/docs/en/managed-agents/tools · fetched 2026-08-22

**Fact 98 — beta status.** *"Claude Managed Agents is in beta. All Managed Agents endpoints require the
`managed-agents-2026-04-01` beta header."* Within the beta, MCP tunnels and "dreaming" are in a more
limited research preview. `[VOLATILE]` — header and beta state.
Source: https://platform.claude.com/docs/en/managed-agents/overview · fetched 2026-08-22

---

### Q16.3 — Strands Agents

**Who makes it.** AWS. *"AWS created Strands Agents, with multiple internal teams already using it in
production, including Amazon Q Developer, AWS Glue, and VPC Reachability Analyzer."* The project site
describes it as *"Built from production systems inside Amazon"* and *"The open source toolkit for
building production agents."*
Sources: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ ·
https://strandsagents.com/ · both fetched 2026-08-22

**What layer it occupies.** An open-source agent SDK for Python and TypeScript, sitting between model
providers and deployment targets — the same layer as the Claude Agent SDK, but provider-neutral. It
*"handles context management, execution limits, and observability before you write a line of config."*
Source: https://strandsagents.com/ · fetched 2026-08-22

**Central abstraction: the model-driven approach.** *"In a model-driven approach, the agent uses the
model to dynamically direct its own steps and to use tools in order to accomplish the specified task."*
An agent is three things — **model, tools, prompt** — and Strands runs the loop: *"In each loop, Strands
invokes the LLM with the prompt and agent context, along with a description of your agent's tools."* The
model may respond in natural language, plan, reflect, or select tools; Strands executes selected tools
and returns results, repeating until the task completes. What it removes: developers do not build
*"complex orchestration logic"* or *"parsers for the model's responses."*
Source: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ ·
fetched 2026-08-22

**Model support.** *"Amazon Bedrock, Anthropic Claude, Llama API, Ollama, and many other model providers
such as OpenAI through LiteLLM."* The project site's phrasing: *"any model, any cloud."*
Sources: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ ·
https://strandsagents.com/ · both fetched 2026-08-22

**MCP and multi-agent.** Integrates with *"thousands of published Model Context Protocol (MCP) servers to
use as tools"* and publishes a Strands MCP server itself. Built-in multi-agent patterns include
**Agent-as-Tool** and **Swarm**.
Sources: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ ·
https://strandsagents.com/ · both fetched 2026-08-22

**Deployment options documented.** Local client applications; behind an API (Lambda, Fargate, EC2);
separated agent and tool environments; mixed local and backend tool execution.
Source: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ ·
fetched 2026-08-22

**When you would choose it.** The sources support: you want a **model-driven** rather than
graph-orchestrated agent; you want to stay **provider-neutral** while defaulting to AWS-native
integration (Bedrock, AgentCore); you want the loop, tool execution and observability handled without
hand-writing orchestration.

---

### Q16.4 — LangGraph

**Who makes it.** *"LangGraph is built by LangChain Inc, the creators of LangChain, but can be used
without LangChain."*
Source: https://docs.langchain.com/oss/python/langgraph/overview · fetched 2026-08-22

**What layer it occupies.** *Below* LangChain, not beside it. *"While LangChain provides agent
abstractions and integrations, LangGraph functions as 'the orchestration runtime: durable execution,
streaming, human-in-the-loop, and persistence.'"* Self-described as *"a low-level orchestration framework
for building stateful agents."*
Source: https://docs.langchain.com/oss/python/langgraph/overview · fetched 2026-08-22

**Central abstraction.** Graphs of **nodes and edges over shared state**. The distinguishing capability
is that it *"enables developers to mix deterministic, hand-coded steps with LLM-driven agentic steps in
the same graph."* Supporting features: persistence — agents *"persist through failures and can run for
extended periods, resuming from where they left off"* — human-in-the-loop interrupts for *"inspecting and
modifying agent state at any point"*, and memory systems.
Source: https://docs.langchain.com/oss/python/langgraph/overview · fetched 2026-08-22

**When you would choose it.** *"Precise control over every part of your agent's behavior."* The docs
route beginners elsewhere: if you are *"just getting started with agents or want a higher-level
abstraction"*, use LangChain's prebuilt agent architectures instead.
Source: https://docs.langchain.com/oss/python/langgraph/overview · fetched 2026-08-22

> **Placement discriminator vs Strands.** LangGraph is **graph-orchestrated**: the developer specifies
> the control flow, and the LLM fills in the reasoning inside it. Strands is **model-driven**: the model
> directs its own steps. That is the cleanest exam-shaped contrast between the two, and it is drawn from
> each project's own words — *"mix deterministic, hand-coded steps with LLM-driven agentic steps in the
> same graph"* versus *"the agent uses the model to dynamically direct its own steps."*

---

### Q16.5 — Pydantic AI

**Who makes it.** *"Built by the Pydantic team."* Positioning claim from the same page: *"Pydantic
Validation is the validation layer of the OpenAI SDK, the Anthropic SDK, the Google ADK, LangChain, and
most of the AI ecosystem (and the foundation FastAPI was built on)."*
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22 (reached via a 301 from
https://ai.pydantic.dev/)

**What it is.** *"the Python AI SDK: a typed, extensible agent loop with every model a string swap
away."*
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22

**Central abstraction: types all the way through.** *"Typed end to end"* — structured outputs
*"validated on every run"* via Pydantic models, typed dependency injection, and typed tools. A
**capability** primitive *"bundles tools, instructions, hooks, and model settings into reusable units."*
Model agnosticism is a first-class claim: *"Virtually every model and provider... swappable with a
string."*
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22

**Provider support.** *"OpenAI, Anthropic, Google, Bedrock, Azure AI Foundry, Groq, Mistral, xAI, Ollama,
and dozens more"*, either with individual keys or through the Pydantic AI Gateway (*"one key for all of
them, with failover and cost monitoring built in"*). `[VOLATILE]` — provider list.
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22

**Durable execution.** *"First-party, co-maintained durable execution on Temporal, DBOS, or Prefect, with
Restate, Kitaru, and Airflow integrations"*, so agents *"survive restarts and run for days on the engine
you already operate."* `[VOLATILE]`
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22

**When you would choose it.** The docs span *"simple typed data extraction to complex, long-running
multi-agent collaboration."* The discriminating case is the first half: **when the output contract
matters more than the orchestration** — validated, typed structured outputs on every run, in a Python
codebase that already uses Pydantic or FastAPI conventions.
Source: https://pydantic.dev/docs/ai/overview/ · fetched 2026-08-22

> **Three-way placement summary the chapter can teach**, each half sourced above:
> **Strands** — model-driven loop, provider-neutral, AWS-origin, multi-agent patterns built in.
> **LangGraph** — graph/state-machine orchestration runtime, deterministic and agentic steps mixed,
> durable execution and human-in-the-loop interrupts, chosen for control.
> **Pydantic AI** — typed agent loop, validated structured outputs and dependency injection, chosen for
> the output and integration contract.
> All three sit at the **same layer as the Claude Agent SDK** — a library running the loop in your own
> process — and all three are provider-neutral where the Agent SDK is Claude-specific. That relationship
> is my inference from the four sources, not a sentence any of them writes; see the inference list below.

---

## WHAT I COULD NOT ESTABLISH

1. **No four-way official comparison of built-in tool / custom tool / Skill / MCP server.** Searched
   `platform.claude.com`, `docs.claude.com`, `code.claude.com`, `anthropic.com`, `claude.com` on
   2026-08-22. The four partial comparisons found are listed under Q13.4. The chapter must derive the
   comparison. **This is a finding, not a hole.**
2. **`https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more` — not
   fetched.** It is linked from https://code.claude.com/docs/en/features-overview as the deeper
   walkthrough on choosing between mechanisms, and is on an authoritative domain. It may contain the
   nearest thing to explicit selection guidance. **Recommend fetching before Chapter 13 is written.**
3. **No approval mechanism found in the Messages API itself.** I found none, and I could not find a page
   that states there is none. My reading — that approval on the Messages API is structural, because your
   code holds the `tool_result` — is an inference from Facts 15 and 17, not a quoted claim.
4. **Whether Anthropic publishes a recommended maximum number of tools per request.** The 30–50
   degradation range (Fact 38) and the 10-tool tool-search threshold (Fact 40) are the closest published
   figures. I found no statement of a hard cap for ordinary tool use. (There is a documented cap of
   10,000 deferred tools per request under tool search.)
5. **Strands' license.** A search-result summary said Apache-2.0; I did not see it on
   `strandsagents.com` or in the AWS Open Source Blog post I fetched. **Do not state a license.**
6. **Strands' own deeper documentation pages.** `https://strandsagents.com/latest/` returned **HTTP 404**
   on 2026-08-22. Everything in Q16.3 comes from the site root plus the AWS Open Source Blog. Depth on
   the Strands agent loop is thinner than for LangGraph and Pydantic AI.
7. **LangGraph's own primary docs site under its old URL.** `https://langchain-ai.github.io/langgraph/`
   now serves only a redirect notice to `docs.langchain.com`; the content in Q16.4 comes from
   `docs.langchain.com`, which is the current official documentation.
8. **Managed Agents Skills page not fetched** (`/managed-agents/skills`). Skills are listed as part of an
   Agent's definition (Fact 89) and self-hosted workers download them (Fact 93), but I did not verify how
   Skills behave inside Managed Agents specifically — in particular whether the API's no-network Skill
   constraint (Fact 60) applies there.
9. **The Agent SDK Skills page** (`/agent-sdk/skills`) not fetched. Skill loading in the SDK is
   established only at the summary level (Fact 82, Fact 71).
10. **Whether the exam's own vocabulary matches Anthropic's.** The blueprint says *"client- vs
    server-side tools"* and *"built-in Tools, custom Tools, Skills, and MCPs."* Anthropic's current docs
    say *"client tools"* / *"server tools"* and split client tools into *user-defined* and
    *Anthropic-schema*. The three-bucket model (Fact 15) is finer than the blueprint's two-way split. I
    could not establish which vocabulary the item writers used.

---

## WHAT CAME ONLY FROM NON-AUTHORITATIVE SOURCES

Short list, because I stayed on the authoritative domains.

1. **Strands' Apache-2.0 license** — from a WebSearch result summary referencing `tooldirectory.ai` and
   a Medium post. **Not verified on an official source. Do not teach it.**
2. **The Strands user quote** *"cut my setup from 40 lines to 3"* — appears on `strandsagents.com` as a
   testimonial. It is on the project's own site but it is marketing, not documentation.
   **Do not teach it as a fact about the framework.**
3. **WebSearch answer summaries** were used to *locate* pages (for approval patterns, for Skills-vs-MCP,
   for Strands). Every fact stated in this pack was then read on the page itself and carries that page's
   URL. No fact in the numbered list rests on a search snippet alone.

---

## VERIFIED BY FETCHING vs INFERRED — stated plainly

**Verified by fetching, on 2026-08-22.** Every numbered Fact 1–98. Each carries the URL it was read on.
The pages fetched, in full:

- platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
- platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools
- platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
- platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference
- platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
- platform.claude.com/docs/en/agents-and-tools/mcp-connector
- platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- platform.claude.com/docs/en/managed-agents/overview
- platform.claude.com/docs/en/managed-agents/tools
- platform.claude.com/docs/en/managed-agents/permission-policies
- platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes
- code.claude.com/docs/en/agent-sdk/overview
- code.claude.com/docs/en/agent-sdk/agent-loop
- code.claude.com/docs/en/agent-sdk/permissions
- code.claude.com/docs/en/features-overview
- www.anthropic.com/engineering/writing-tools-for-agents
- www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- claude.com/blog/skills-explained
- modelcontextprotocol.io/docs/getting-started/intro
- modelcontextprotocol.io/docs/2026-07-28/learn/architecture
- strandsagents.com/
- aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/
- docs.langchain.com/oss/python/langgraph/overview
- pydantic.dev/docs/ai/overview/

Failed: `strandsagents.com/latest/` (404) · `langchain-ai.github.io/langgraph/` (redirect notice only) ·
`platform.claude.com/docs/en/api/agent-sdk/overview` (307 to code.claude.com, followed).

**Inferred, and labelled as such wherever it appears:**
- That the Messages API has no built-in approval mechanism, and that approval there is structural.
- That the three third-party frameworks occupy the same layer as the Claude Agent SDK. Each project
  describes its own layer; none of them draws the comparison to the Agent SDK.
- The ownership table in Q13.4. Every cell traces to a quoted fact, but the table itself is my synthesis.
- The "model-driven vs graph-orchestrated" contrast between Strands and LangGraph. Both halves are
  quoted from the respective projects; the contrast is mine.
- All the blockquoted "Discriminator" notes. These are teaching judgements about what would separate two
  plausible options, not documented claims.
