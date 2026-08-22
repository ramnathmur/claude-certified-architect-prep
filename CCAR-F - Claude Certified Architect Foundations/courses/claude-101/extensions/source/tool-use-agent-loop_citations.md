# The Tool-Use Agent Loop — Source-of-Truth Citations

> Extension lesson for the CCA-F exam-prep course. Extends "Claude 101" into the builder/API layer.
> This file is the ground truth for a later HTML build + QA fidelity gate. Every substantive claim carries an inline source URL. No fabrication.

## Manifest

- **Compiled:** 2026-06-05 · **Re-verified 2026-06-09** (both [VERIFY] flags confirmed current; additive drifts in the addendum at the end. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
- **Researcher:** Senior Research Analyst (live web research)
- **Primary sources (all Anthropic):**
  - Tool use overview — https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview
  - How tool use works — https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works
  - Define tools — https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
  - Handle tool calls — https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
  - Parallel tool use — https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use
  - Building Effective Agents — https://www.anthropic.com/engineering/building-effective-agents
- **CCA-F domains reinforced:** Domain 4 (Tool Design & MCP, 18%) primary; Domain 1 (the agent loop) secondary.
- **Currency note:** Docs reference current models (Claude Opus 4.8 etc.). All facts pulled live 2026-06-05; treat as current. Items below marked `[VERIFY]` are model-version-specific numbers that drift.

---

## Section 1 — The Tool-Use Loop, Step by Step

Tool use is described as **a contract**: "You specify what operations are available and what shape their inputs and outputs take; Claude decides when and how to call them. The model never executes anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation, and the result flows back into the conversation." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

The framing: "This contract makes the model behave less like a text generator and more like a function you call... define the schema, handle the callback, return a result. The difference is that the caller on the other side is a language model choosing which function to invoke based on the conversation." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### The canonical client-tool loop (verbatim 5 steps)

"The canonical shape is a `while` loop keyed on `stop_reason`:

1. Send a request with your `tools` array and the user message.
2. Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks.
3. Execute each tool. Format the outputs as `tool_result` blocks.
4. Send a new request containing the original messages, the assistant's response, and a user message with the `tool_result` blocks.
5. Repeat from step 2 while `stop_reason` is `"tool_use"`."
(source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### Stop conditions (loop exit)

"The loop exits on any other stop reason (`"end_turn"`, `"max_tokens"`, `"stop_sequence"`, or `"refusal"`), which means Claude has either produced a final answer or stopped for another reason that your application should handle." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### Message-role flow (critical for QA)

The Claude API does **not** use a dedicated `tool` or `function` role. "Unlike APIs that separate tool use or use special roles like `tool` or `function`, the Claude API integrates tools directly into the `user` and `assistant` message structure. Messages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client content and `tool_result`, while `assistant` messages contain AI-generated content and `tool_use`." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

Therefore:
- **assistant** message → carries `text` and `tool_use` blocks.
- **user** message → carries the matching `tool_result` blocks (and any client content).

### Server-side loop (no developer round trips)

"Server-executed tools run their own loop inside Anthropic's infrastructure. A single request from your application might trigger several web searches or code executions before a response comes back... all without your application participating." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

The server loop has an iteration cap: "If the model is still iterating when it hits the cap, the response comes back with `stop_reason: "pause_turn"` instead of `"end_turn"`. A paused turn means the work isn't finished; re-send the conversation (including the paused response) to let the model continue where it left off." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

---

## Section 2 — Client Tools vs. Server Tools

"Tools differ primarily by where the code executes." There are **three buckets**, and "the bucket determines what your application is responsible for." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### (a) User-defined tools (client-executed)

"You write the schema, you execute the code, you return the results. This is the main event: the vast majority of tool-use traffic is user-defined tools calling into application-specific logic." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

"When Claude decides to use one of your tools, the API response contains a `tool_use` block with the tool name and a JSON object of arguments. Your application extracts those arguments, runs the operation... and sends the output back in a `tool_result` block on the next request. Claude never sees your implementation; it only sees the schema you provided and the result you returned." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### (b) Anthropic-schema tools (client-executed)

"For a handful of common operations (running shell commands, editing files, controlling a browser, managing scratchpad memory), Anthropic publishes the tool schema and your application handles execution. The tools in this category are `bash`, `text_editor`, `computer`, and `memory`." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

"The execution model is identical to user-defined tools." The advantage: "these schemas are trained-in. Claude has been optimized on thousands of successful trajectories that use these exact tool signatures, so it calls them more reliably and recovers from errors more gracefully than it would with a custom tool that does the same thing." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### (c) Server-executed tools

"For `web_search`, `web_fetch`, `code_execution`, and `tool_search`, Anthropic runs the code. You enable the tool in your request and the server handles everything else. **You never construct a `tool_result` block for these tools** because the server-side loop executes the operation and feeds the output back to the model before the response reaches you." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

"The response you receive contains `server_tool_use` blocks showing what ran and what came back, but by the time you see them, execution is already complete. Your application's job is to enable the tool and read the final answer, not to participate in the execution loop." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

Server tool errors are handled transparently: "Unlike client tools, you do not need to handle `is_error` results for server tools." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Summary contrast (what the developer must handle)

| Approach | Who executes | Developer responsibility |
| --- | --- | --- |
| User-defined client tools | Your application | Schema + execution + drive the agentic loop |
| Anthropic-schema client tools (`bash`, `text_editor`, `computer`, `memory`) | Your application | Execution + loop; schema is provided & trained-in |
| Server tools (`web_search`, `web_fetch`, `code_execution`, `tool_search`) | Anthropic infra | Just enable the tool and read the result; no `tool_result`, no `is_error` |
(source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works ; https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Simplest server-tool request (verbatim shape)

```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 1024,
  "tools": [{"type": "web_search_20260209", "name": "web_search"}],
  "messages": [{"role": "user", "content": "What's the latest on the Mars rover?"}]
}
```
Note server tools use a versioned `type` plus a `name`. (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview)

---

## Section 3 — `tool_choice` Options

Set in the `tool_choice` field of the API request. "When working with the tool_choice parameter, there are four possible options:

- `auto` allows Claude to decide whether to call any provided tools or not. This is the default value when `tools` are provided.
- `any` tells Claude that it must use one of the provided tools, but doesn't force a particular tool.
- `tool` forces Claude to always use a particular tool.
- `none` prevents Claude from using any tools. This is the default value when no `tools` are provided."
(source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

To force a specific tool: `tool_choice = {"type": "tool", "name": "get_weather"}`. (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

**Prefill behavior with `any`/`tool`:** "when you have `tool_choice` as `any` or `tool`, the API prefills the assistant message to force a tool to be used. This means that the models will not emit a natural language response or explanation before `tool_use` content blocks, even if explicitly asked to do so." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

**When to use which:**
- `auto` (default) — let Claude decide; combine with system-prompt nudges ("Use the tools to investigate before responding.") to increase tool use. (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview)
- `auto` + explicit user instruction — if you want a natural-language preface AND a specific tool, keep `auto` and instruct in a user message. (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- `any` / `tool` — hard guarantee a tool call. Combine with `strict: true` "to guarantee both that one of your tools will be called AND that the tool inputs strictly follow your schema." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- `none` — turn tools off for a turn.

**Constraints / caveats:**
- Extended thinking: "`tool_choice: {"type": "any"}` and `tool_choice: {"type": "tool", "name": "..."}` are not supported and will result in an error. Only `tool_choice: {"type": "auto"}` (the default) and `tool_choice: {"type": "none"}` are compatible with extended thinking." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- Prompt caching: "changes to the `tool_choice` parameter will invalidate cached message blocks. Tool definitions and system prompts remain cached, but message content must be reprocessed." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### `disable_parallel_tool_use`

"By default, Claude may use multiple tools to answer a user query. You can disable this behavior by:
- Setting `disable_parallel_tool_use=true` when `tool_choice` type is `auto`, which ensures that Claude uses **at most one** tool
- Setting `disable_parallel_tool_use=true` when `tool_choice` type is `any` or `tool`, which ensures that Claude uses **exactly one** tool"
(source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)

Parallel-call semantics: "Tool calls in a single assistant turn are unordered. You can run them concurrently... sequentially, or in any order. Claude doesn't assume one call in the batch has completed before another. Claude issues dependent calls across separate turns." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)

---

## Section 4 — Tool Definition Anatomy

Client tools are specified in the top-level `tools` parameter. Each definition includes: (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

| Parameter | Description (verbatim) |
| --- | --- |
| `name` | "The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`." |
| `description` | "A detailed plaintext description of what the tool does, when it should be used, and how it behaves." |
| `input_schema` | "A JSON Schema object defining the expected parameters for the tool." |
| `input_examples` | "(Optional) An array of example input objects to help Claude understand how to use the tool." |

Other optional properties live in the Tool reference: `cache_control`, `strict`, `defer_loading`, `allowed_callers`. (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### Why the description matters most (verbatim)

"Provide extremely detailed descriptions. This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including: What the tool does; When it should be used (and when it shouldn't); What each parameter means and how it affects the tool's behavior; Any important caveats or limitations... Aim for at least 3-4 sentences per tool description, more if the tool is complex." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

Other best practices (verbatim headers): "Consolidate related operations into fewer tools" (group actions under an `action` parameter rather than `create_pr`/`review_pr`/`merge_pr`); "Use meaningful namespacing in tool names" (e.g., `github_list_prs`, `slack_send_message`); "Design tool responses to return only high-signal information." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### Canonical simple definition (verbatim)

```json
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
      }
    },
    "required": ["location"]
  }
}
```
"expects an input object with a required `location` string and an optional `unit` string that must be either 'celsius' or 'fahrenheit'." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### Good vs. poor description (teaching contrast)

GOOD `get_stock_price` description: "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

POOR: "Gets the stock price for a ticker." — "too brief and leaves Claude with many open questions about the tool's behavior and usage." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### Strict schema conformance

"Add `strict: true` to your tool definitions to ensure Claude's tool calls always match your schema exactly." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview)

"To eliminate invalid tool calls entirely, use strict tool use with `strict: true` on your tool definitions. This guarantees that tool inputs will always match your schema exactly, preventing missing parameters and type mismatches." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### The auto-injected tool-use system prompt

"When you call the Claude API with the `tools` parameter, the API constructs a special system prompt from the tool definitions, tool configuration, and any user-specified system prompt." This adds token cost. `[VERIFY]` Per-model token counts (model-version-specific, drifts): e.g. Claude Opus 4.8 — 290 tokens for `auto`/`none`, 410 tokens for `any`/`tool`. (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview)

---

## Section 5 — The Observe–Think–Act Agent Loop (Building Effective Agents)

### Agents vs. workflows (verbatim definitions)

- **Workflows:** "systems where LLMs and tools are orchestrated through predefined code paths."
- **Agents:** "systems where LLMs dynamically direct their own processes and tool usage, maintaining control."
(source: https://www.anthropic.com/engineering/building-effective-agents)

### The augmented LLM (the building block)

The foundational component combines "retrieval, tools, and memory." Modern models can "actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain." (source: https://www.anthropic.com/engineering/building-effective-agents)

### How a single tool call fits the broader loop

Agents begin with "a command from, or interactive discussion with, the human user." Once the task is clear, they "plan and operate independently," gaining "ground truth from the environment at each step (such as tool call results or code execution)." This environmental feedback lets the agent assess its progress. (source: https://www.anthropic.com/engineering/building-effective-agents)

Net characterization: agents are "typically just LLMs using tools based on environmental feedback in a loop," which makes "toolsets and their documentation" crucial. (source: https://www.anthropic.com/engineering/building-effective-agents)

This maps directly to observe → think → act → repeat: the model **acts** (emits a `tool_use`), **observes** ground truth (the `tool_result` it gets back), **thinks** (reasons over results), and repeats — exactly the API `while stop_reason == "tool_use"` loop in Section 1.

### Stop conditions (agent-level)

"The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control." (source: https://www.anthropic.com/engineering/building-effective-agents) Pair this with the API-level stop reasons from Section 1 — impose your own iteration cap as a guardrail.

---

## Section 6 — One Full Loop Turn (Worked Example, Real JSON Shapes)

### Step 1 — Request: tools + user message

```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 1024,
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The unit of temperature"}
        },
        "required": ["location"]
      }
    }
  ],
  "messages": [
    {"role": "user", "content": "What's the weather like in San Francisco?"}
  ]
}
```
(source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)

### Step 2 — Assistant response: `stop_reason: "tool_use"` (verbatim)

```json
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-opus-4-8",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll check the current weather in San Francisco for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": { "location": "San Francisco, CA", "unit": "celsius" }
    }
  ]
}
```
(source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

The `tool_use` block fields: "`id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later. `name`: The name of the tool being used. `input`: An object containing the input being passed to the tool, conforming to the tool's `input_schema`." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Step 3 — Your code executes the tool

"1. Extract the `name`, `id`, and `input` from the `tool_use` block. 2. Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`. 3. Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Step 4 — Return the `tool_result` (user message, verbatim)

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
    }
  ]
}
```
(source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

`tool_result` fields: "`tool_use_id`: The `id` of the tool use request this is a result for. `content` (optional): The result of the tool... `is_error` (optional): Set to `true` if the tool execution resulted in an error." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

**Strict ordering rules (QA-critical):** "Tool result blocks must immediately follow their corresponding tool use blocks in the message history. You cannot include any messages between the assistant's tool use message and the user's tool result message." AND "In the user message containing tool results, the tool_result blocks must come FIRST in the content array. Any text must come AFTER all tool results." Violating either causes a **400 error**. (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

**Error case** — return error content with `is_error: true`:
```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
    }
  ]
}
```
"If a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Step 5 — Continue: assistant returns final answer (`stop_reason: "end_turn"`)

"After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) When Claude has the answer, it responds with text and `stop_reason: "end_turn"`, exiting the loop. (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### Parallel variant (one turn, multiple tools)

For "What's the weather in SF and NYC, and what time is it there?", Claude may emit multiple `tool_use` blocks in one assistant turn. **All `tool_result` blocks must go back in a single user message** — splitting them across separate user messages "teaches" Claude to stop calling tools in parallel. (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)

---

## Section 7 — When to Use Tools (and When Not To)

Use tools for: "Actions with side effects" (send email, write file, update record); "Fresh or external data" (current prices, today's weather, a database's contents); "Structured, guaranteed-shape outputs" (JSON with specific fields, enforced by the schema); "Calling into existing systems" (databases, internal APIs, file systems). (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

Heuristic: "if you're writing a regex to extract a decision from model output, that decision should have been a tool call." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

Don't use tools when: "The model can answer from training alone"; "The interaction is one-shot Q&A with no side effects"; "Tool-calling latency would dominate a trivial response" — "Every tool call is at least one extra round trip." (source: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works)

### Security note (Domain 4 relevance)

"Tool results often carry content from sources outside your control... Treat that content as untrusted: an attacker who can influence it may embed instructions that try to redirect Claude (indirect prompt injection). Keep untrusted content inside `tool_result` blocks rather than `system` prompts or plain user `text` blocks." (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

---

## Sources

1. Tool use overview — https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview
2. How tool use works — https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/how-tool-use-works
3. Define tools — https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
4. Handle tool calls — https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
5. Parallel tool use — https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use
6. Building Effective Agents — https://www.anthropic.com/engineering/building-effective-agents

---

## [VERIFY] flags
1. Per-model tool-use system-prompt token counts (e.g., Opus 4.8 = 290/410) — model-version-specific, drifts with new releases. **✓ Re-confirmed 2026-06-09:** Opus 4.8 = 290/410 still correct; the per-model table has since GROWN (new model rows added) — re-pull the full table at build time.
2. Model name `claude-opus-4-8` and server-tool version string `web_search_20260209` — current as fetched 2026-06-05; re-verify at build/publish time.

---

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`)*

- **Claude Mythos Preview rejects forced `tool_choice`** (`{"type": "tool"}` / `"any"`) with a **400 error** — only auto tool selection is supported on that model. Relevant to any lesson claim that `tool_choice` forcing is universally available.
