# Ground-Truth Research Notes — Context Management & Reliability (CCA-F Extension C-E2)

**Date:** 2026-06-05 · **Re-verified 2026-06-09** ([VERIFY] #2 resolved — 1M needs no beta header; #6/#7/#8 remain unverifiable. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
**Course:** Claude Certified Architect — Foundations (CCA-F)
**Primary domain:** Domain 5 — Context Management & Reliability (15% of exam)
**Secondary domain:** Domain 1 — reliability/architecture themes
**Builds on:** Claude 101 base course

> Scope note: This is a grounding artifact for an architect-level HTML lesson. Every substantive claim carries an inline `(source: URL)`. Version-sensitive facts (model names, context sizes, prices, beta header dates) are tagged `[VERIFY]` and re-listed at the end. Prompt caching is covered briefly here; full treatment belongs to extension C-E4.

### Source manifest (every URL used)
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://platform.claude.com/docs/en/build-with-claude/compaction
- https://platform.claude.com/docs/en/build-with-claude/context-editing
- https://platform.claude.com/docs/en/build-with-claude/token-counting
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- https://code.claude.com/docs/en/costs

---

## 1. Context windows — what they are, 200K standard, 1M tier, shared budget
*(Reinforces Domain 5; Domain 1 capacity planning)*

**Definition (verbatim):** "The 'context window' refers to all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a 'working memory' for the model." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**More tokens is not automatically better (verbatim):** "A larger context window allows the model to handle more complex and lengthy prompts, but more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as *context rot*. This makes curating what's in context just as important as how much space is available." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Shared budget — input + output + tools + thinking all consume the same window:**
- "The total available context window (up to 1M tokens) represents the maximum capacity for storing conversation history and generating new output from Claude." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Each turn's input phase "contains all previous conversation history plus the current user message"; the output phase "generates a text response that becomes part of a future input." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Extended thinking: "all input and output tokens, including the tokens used for thinking, count toward the context window limit." Thinking budget tokens "are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Tool configuration counts as input tokens; tool-use requests, results, and the accompanying thinking blocks all count toward the window. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Current model context sizes (June 2026)** `[VERIFY — model lineup changes fast]`:

| Model | Context window | Max output | API ID | Input/Output price (per MTok) |
|---|---|---|---|---|
| Claude Opus 4.8 | **1M tokens** | 128k | `claude-opus-4-8` | $5 / $25 |
| Claude Sonnet 4.6 | **1M tokens** | 64k | `claude-sonnet-4-6` | $3 / $15 |
| Claude Haiku 4.5 | **200k tokens** | 64k | `claude-haiku-4-5-20251001` | $1 / $5 |

(source: https://platform.claude.com/docs/en/about-claude/models/overview)

**Which models support 1M (verbatim):** "Claude Opus 4.8, Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a 1M-token context window on the Claude API, Amazon Bedrock, and Vertex AI. On Microsoft Foundry, Claude Opus 4.8 has a 200k-token context window. Other Claude models, including Claude Sonnet 4.5 and Sonnet 4 (deprecated), have a 200k-token context window." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows) `[VERIFY]`

> Note: Unlike earlier generations where 1M on Sonnet was a separate beta tier behind a `context-1m` header, in the current (June 2026) docs the 1M window is presented as the native window for Opus 4.6+/4.7/4.8 and Sonnet 4.6. Haiku 4.5 remains 200k. `[VERIFY — confirm whether any 1M beta header is still required for billing tier]`

**Other capacity facts:**
- A single request can include up to 600 images or PDF pages (100 for 200k-token models). (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Tooltip word equivalents: Opus 4.8 1M ≈ ~555k words; Sonnet 4.6 1M ≈ ~750k words; 200k ≈ ~150k words. (source: https://platform.claude.com/docs/en/about-claude/models/overview)
- On the Message Batches API, Opus 4.8/4.7/4.6 and Sonnet 4.6 support up to **300k output tokens** via the `output-300k-2026-03-24` beta header. (source: https://platform.claude.com/docs/en/about-claude/models/overview) `[VERIFY]`

**Extended-thinking nuance — previous thinking is auto-stripped:** "Extended thinking blocks ... are not carried forward as input tokens for subsequent turns. You do not need to strip the thinking blocks yourself. The Claude API automatically does this for you if you pass them back." Effective calc: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Exception — tool use cycle:** during a tool-use turn "the extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks." The API uses cryptographic signatures to verify thinking-block authenticity; modifying them returns an error. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Context awareness (Sonnet 4.6, Sonnet 4.5, Haiku 4.5):** these models "track their remaining context window (that is, 'token budget') throughout a conversation." At conversation start Claude receives `<budget:token_budget>1000000</budget:token_budget>` (200k for smaller-window models), and after each tool call gets `<system_warning>Token usage: 35000/1000000; 965000 remaining</system_warning>`. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows) `[VERIFY — Opus 4.8 is NOT listed as context-aware]`

**Overflow behavior:** "On Claude 4.5 models and newer, if input tokens plus `max_tokens` exceeds the context window size, the API accepts the request. If generation then reaches the context window limit, it stops with `stop_reason: 'model_context_window_exceeded'`." Earlier models return a validation error unless you opt in via the `model-context-window-exceeded-2025-08-26` beta header. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

---

## 2. Linear token accumulation in multi-turn agents
*(Reinforces Domain 5; Domain 1 cost/latency planning)*

**Mechanism (verbatim):**
- "Progressive token accumulation: As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely."
- "Linear growth pattern: The context usage grows linearly with each turn, with previous turns preserved completely." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Why cost/latency grows worse than linear (the "accumulation/quadratic" problem):** Because every turn re-sends the entire prior history as input, total tokens *billed across a session* grow roughly quadratically with the number of turns even though the window itself grows linearly per turn (turn N pays for ~N turns of history). Anthropic frames the underlying model cost as quadratic at the attention level: the transformer creates "n² pairwise relationships for n tokens," which stretches thin as context lengthens. (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**When-to-use guidance:** For long-running conversations and agentic workflows, "server-side compaction is the primary strategy for context management." For finer control, context editing clears old tool results / thinking blocks. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows) Prompt caching mitigates the *cost* of re-sending a stable prefix (Section 9), but does not stop the window from filling.

---

## 3. Context rot / degradation as windows fill
*(Reinforces Domain 5)*

**Context rot definition (verbatim):** "As token count increases, the model's ability to accurately recall information from that context decreases." "This constraint applies across all models, though some degrade more gradually." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Attention budget (verbatim):** LLMs possess "an 'attention budget' that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Architectural cause (verbatim):** the transformer creates "n² pairwise relationships for n tokens," and models have "less experience with, and fewer specialized parameters for, context-wide dependencies" because training sequences are typically shorter than max context. (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Docs corroboration:** "context is a finite resource with diminishing returns, and irrelevant content degrades model focus." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**"Lost in the middle" / benchmark anchor:** Anthropic measures long-context capability on needle-in-a-haystack benchmarks (MRCR v2, GraphWalks). The docs note gains "depend on what's in context, not just how much fits." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows) Comparative datapoint from launch material: on the 8-needle 1M MRCR v2 variant, Opus 4.6 scored 76% vs Sonnet 4.5 at 18.5% — illustrating that newer models degrade far more gracefully at depth, but degradation still exists. `[VERIFY — this stat came from search-summary launch material, not a fetched primary page]`

**Takeaway for architects:** more tokens ≠ better. Curating *what* is in context is "just as important as how much space is available." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

---

## 4. Compaction (server-side summarization)
*(Reinforces Domain 5; Domain 1 long-running architecture)*

**What it is / how it works (verbatim mechanism):** When enabled, Claude automatically summarizes the conversation as it approaches the configured threshold. It: (1) **Detects** when input tokens exceed the trigger threshold; (2) **Generates** a summary of the current conversation; (3) **Creates** a `compaction` block containing the summary; (4) **Continues** the response with the compacted context. On subsequent requests, "The API automatically drops all message blocks prior to the `compaction` block, continuing from the summary." (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Trigger threshold:** Default **150,000** input tokens; configurable but must be at least **50,000** tokens. (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Supported models:** Claude Mythos Preview, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6 (beta). (source: https://platform.claude.com/docs/en/build-with-claude/compaction) `[VERIFY]`

**Beta header:** `anthropic-beta: compact-2026-01-12` (must be in all requests using compaction). (source: https://platform.claude.com/docs/en/build-with-claude/compaction) `[VERIFY — dated header]`

**Request shape:**
```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 4096,
  "messages": [{"role": "user", "content": "Help me build a website"}],
  "context_management": {
    "edits": [
      {
        "type": "compact_20260112",
        "trigger": {"type": "input_tokens", "value": 150000},
        "pause_after_compaction": false,
        "instructions": null
      }
    ]
  }
}
```
(source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Response shape (note the `compaction` content block + `iterations` usage):**
```json
{
  "content": [
    {"type": "compaction", "content": "Summary of the conversation: ..."},
    {"type": "text", "text": "Based on our conversation so far..."}
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 23000,
    "output_tokens": 1000,
    "iterations": [
      {"type": "compaction", "input_tokens": 180000, "output_tokens": 3500},
      {"type": "message", "input_tokens": 23000, "output_tokens": 1000}
    ]
  }
}
```
(source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Parameters:** `type` (required, `"compact_20260112"`); `trigger` (default 150,000 input_tokens); `pause_after_compaction` (default `false`); `instructions` (default `null` — custom summarization prompt replaces the default). (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Default summarization prompt (verbatim):** "You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context, where the raw history above may not be accessible and will be replaced with this summary. Write down anything that would be helpful, including the state, next steps, learnings etc. You must wrap your summary in a `<summary></summary>` block." (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**What's preserved:** the `compaction` block (must be passed back), messages after the compaction point, plus recent context when using `pause_after_compaction`. Everything prior to the compaction block is summarized and auto-dropped on the next request. (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Billing nuance:** top-level `input_tokens`/`output_tokens` do **not** include compaction-iteration usage — "Sum across all `iterations` array entries for total tokens consumed." (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Tradeoffs (verbatim):** Benefits — extends effective context, automatic, minimal integration, keeps active context focused, ideal for chat/multi-turn agents. Costs — "Additional sampling step for summarization (contributes to rate limits and billing)"; "Cannot use cheaper model for summarization—uses same model as request"; "May fail when `tools` are defined (model calls tool during summarization instead of summarizing)." (source: https://platform.claude.com/docs/en/build-with-claude/compaction)

**Compaction craft (engineering guidance):** "The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later." Recommended: "Start by maximizing recall ... then iterate to improve precision by eliminating superfluous content." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Claude Code auto-compaction (product-level):** Claude Code "automatically optimizes costs through prompt caching ... and auto-compaction, which summarizes conversation history when approaching context limits." You can steer it: `/compact Focus on code samples and API usage`, or add a `# Compact instructions` section to CLAUDE.md. (source: https://code.claude.com/docs/en/costs) `[VERIFY — the ~83.5%/~167K auto-compact trigger figure circulating in third-party blogs is NOT confirmed on this official page; treat as unverified]`

---

## 5. Context editing / context-management API
*(Reinforces Domain 5)*

**What it is (verbatim):** "Context editing allows you to selectively clear specific content from conversation history as it grows. Beyond optimizing costs and staying within limits, this is about actively curating what Claude sees." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**When to use vs compaction:** "For most use cases, server-side compaction is the primary strategy ... The strategies on this page are useful for specific scenarios where you need more fine-grained control over what content is cleared." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Beta header:** `context-management-2025-06-27`. Supported on all supported Claude models. (source: https://platform.claude.com/docs/en/build-with-claude/context-editing) `[VERIFY — dated header]`

**Two server-side strategies + one client-side:**
| Strategy | Type string | Purpose |
|---|---|---|
| Tool result clearing | `clear_tool_uses_20250919` | Clear old tool results in heavy tool-use workflows |
| Thinking block clearing | `clear_thinking_20251015` | Manage thinking blocks with extended thinking |
| Client-side compaction (SDK) | — | Summary-based, in Python/TS/Ruby SDKs via `tool_runner` |
(source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Tool result clearing mechanism (verbatim):** "When activated, the API automatically clears the oldest tool results in chronological order. The API replaces each cleared result with placeholder text so Claude knows it was removed. By default, only tool results are cleared. You can optionally clear both tool results and tool calls (the tool use parameters) by setting `clear_tool_inputs` to true." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Tool-result-clearing config (full shape):**
```json
{
  "type": "clear_tool_uses_20250919",
  "trigger": {"type": "input_tokens", "value": 30000},
  "keep": {"type": "tool_uses", "value": 3},
  "clear_at_least": {"type": "input_tokens", "value": 5000},
  "exclude_tools": ["web_search"]
}
```
- `trigger` — clearing fires when input tokens exceed this value.
- `keep` — number of recent tool uses to retain after clearing.
- `clear_at_least` — guarantees a minimum number of tokens cleared each time (used to make prompt-cache invalidation worthwhile).
- `exclude_tools` — tools whose results are never cleared.
- `clear_tool_inputs` — when `true`, also clears the tool-call parameters (default clears only results).
(source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Thinking block clearing (`clear_thinking_20251015`):** "manages `thinking` blocks ... you can choose to keep more thinking blocks to maintain reasoning continuity, or clear them more aggressively to save context space." Config option `keep` = `{type: "thinking_turns", value: N}` (N > 0) or `"all"`. Per-model defaults:
| Model class | Keep ALL prior thinking | Keep ONLY last turn's thinking |
|---|---|---|
| Opus | Opus 4.5 and later | Opus 4.1 and earlier |
| Sonnet | Sonnet 4.6 and later | Sonnet 4.5 and earlier |
| Haiku | (none) | all through Haiku 4.5 |

"If your code runs across multiple model tiers, set `keep` explicitly." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Combining strategies:** Both can run together, but "the `clear_thinking_20251015` strategy must be listed first in the `edits` array." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Server-side, no client sync needed (verbatim):** "Context editing is applied server-side before the prompt reaches Claude. Your client application maintains the full, unmodified conversation history. You do not need to sync your client state with the edited version." (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

**Cache interaction:** Tool-result clearing "invalidates cached prompt prefixes when content is cleared ... clear enough tokens to make the cache invalidation worthwhile. Use the `clear_at_least` parameter." For thinking-block clearing: kept thinking preserves the cache; cleared thinking invalidates the cache at the clearing point. (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

> `[VERIFY]` The response `context_management.applied_edits` object (number of tool uses cleared, tokens freed) is referenced in product summaries; the exact JSON shape was not captured in the fetched section of the docs page. Confirm against the live page before quoting field names.

---

## 6. Effective context engineering — Anthropic's guidance
*(Reinforces Domain 5; Domain 1 design principles)*

**Context engineering vs prompt engineering (verbatim):** Context engineering is "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts." Prompt engineering is "writing and organizing LLM instructions"; context engineering addresses "the entire context state (system instructions, tools, Model Context Protocol, external data, message history, etc)" across multiple turns. (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Guiding maxim (verbatim):** find "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." Overall guidance: "be thoughtful and keep your context informative, yet tight." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**System prompt hygiene (verbatim):** Prompts should strike the right "altitude" — avoiding both "brittle if-else hardcoded prompts" and "prompts that are overly general or falsely assume shared context." Organize with XML tags or Markdown headers, pursuing "the minimal set of information that fully outlines your expected behavior." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Tool curation (verbatim):** Tools should be "self-contained, robust to error, and extremely clear with respect to their intended use." Avoid "bloated tool sets that cover too much functionality or lead to ambiguous decision points about which tool to use." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Just-in-time retrieval vs pre-loading (verbatim):** Maintain "lightweight identifiers (file paths, stored queries, web links, etc.)" and "dynamically load data into context at runtime using tools" rather than pre-processing everything upfront. Trade-off: "Runtime exploration is slower than retrieving pre-computed data," requiring "opinionated and thoughtful engineering" to keep agents from "wasting context by misusing tools, chasing dead-ends, or failing to identify key information." (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Product-level analogs in Claude Code (concrete tactics that embody the above):**
- MCP tool definitions are deferred by default — "only tool names enter context until Claude uses a specific tool." (source: https://code.claude.com/docs/en/costs)
- Prefer CLI tools (`gh`, `aws`, `gcloud`) over MCP servers for context efficiency; disable unused MCP servers. (source: https://code.claude.com/docs/en/costs)
- Move specialized instructions out of CLAUDE.md into on-demand skills; "Aim to keep CLAUDE.md under 200 lines." (source: https://code.claude.com/docs/en/costs)
- Use hooks to preprocess verbose data (e.g., grep a 10,000-line log to only `ERROR` lines) "reducing context from tens of thousands of tokens to hundreds." (source: https://code.claude.com/docs/en/costs)
- Delegate verbose operations to subagents so "verbose output stays in the subagent's context while only a summary returns to your main conversation." (source: https://code.claude.com/docs/en/costs)
- `/clear` between unrelated tasks; "Stale context wastes tokens on every subsequent message." (source: https://code.claude.com/docs/en/costs)

---

## 7. Token budgeting in practice
*(Reinforces Domain 5; Domain 1 cost engineering)*

**The `usage` object fields (from prompt-caching/messages responses):**
```json
{
  "input_tokens": 2048,
  "output_tokens": 503,
  "cache_creation_input_tokens": 5120,
  "cache_read_input_tokens": 1800
}
```
- `input_tokens` — "Tokens after the last cache breakpoint (not eligible for cache)."
- `output_tokens` — generated tokens (includes thinking tokens, billed as output).
- `cache_creation_input_tokens` — "Number of tokens written to cache (new entries)."
- `cache_read_input_tokens` — "Number of tokens retrieved from cache."
- **Total input** = `cache_read_input_tokens + cache_creation_input_tokens + input_tokens`.
(source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Token-counting API (plan a budget before sending):**
- Endpoint: `POST https://api.anthropic.com/v1/messages/count_tokens` — accepts the same structured inputs as message creation (system, tools, images, PDFs). (source: https://platform.claude.com/docs/en/build-with-claude/token-counting)
- Response is just `{ "input_tokens": N }`. Examples: basic message → `14`; message + one tool → `403`; message + image → `1551`; message + PDF → `2188`. (source: https://platform.claude.com/docs/en/build-with-claude/token-counting)
- "The token count should be considered an **estimate** ... the actual number ... may differ by a small amount." System-added optimization tokens are not billed. (source: https://platform.claude.com/docs/en/build-with-claude/token-counting)
- **Free**, but rate-limited separately from message creation: tier 1 = 100 RPM, tier 2 = 2,000, tier 3 = 4,000, tier 4 = 8,000. Token counting does not use caching logic. (source: https://platform.claude.com/docs/en/build-with-claude/token-counting)
- Thinking nuance: "Thinking blocks from **previous** assistant turns are ignored and **do not** count," but "**Current** assistant turn thinking **does** count." (source: https://platform.claude.com/docs/en/build-with-claude/token-counting)

**Budgeting model for an architect:** allocate the window across (a) system prompt + tool definitions (stable → cache it), (b) message history (grows linearly → compact/clear it), (c) just-in-time retrieved data, and (d) reserved `max_tokens` for output + thinking. Use `count_tokens` pre-flight to avoid `model_context_window_exceeded`, and the Models API (`max_input_tokens`, `max_tokens`, `capabilities`) to size against the chosen model. (sources: https://platform.claude.com/docs/en/build-with-claude/token-counting ; https://platform.claude.com/docs/en/about-claude/models/overview ; https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Programmatic budget signal (context awareness):** Sonnet 4.6 / 4.5 / Haiku 4.5 receive `<budget:token_budget>` at start and `<system_warning>Token usage: X/Y; Z remaining</system_warning>` after each tool call — the model can self-manage its remaining budget. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Claude Code cost telemetry:** `/usage` shows session token stats and a local cost estimate; `/context` shows what's consuming the window; status line can display context-window usage continuously. (source: https://code.claude.com/docs/en/costs)

---

## 8. Reliability patterns tied to context
*(Reinforces Domain 5 AND Domain 1 — reliability/recovery)*

**Structured state outside the window (external memory/files):** For agents spanning multiple sessions, "design your state artifacts so that context recovery is fast when a new session starts." (source: https://platform.claude.com/docs/en/build-with-claude/context-windows) Concrete artifacts used in Anthropic's long-running-agent harness:
- A `claude-progress.txt` log "that keeps a log of what agents have done."
- A structured feature-requirements JSON file with per-item completion status.
- An initial git commit "that shows what files were added" as a recovery mechanism.
(source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

**Checkpointing & recovery (verbatim guidance):**
- Session init: "Read the git logs and progress files to get up to speed on what was recently worked on."
- State verification: "run a basic test on the development server to catch any undocumented bugs" before new work.
- Clean handoffs: "leave the environment in a clean state at the end of a session" — commit with descriptive messages and write progress summaries.
(source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

**Incremental progress to avoid context exhaustion:** "work on only one feature at a time" prevents context exhaustion and incomplete implementations across sessions. (source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

**Multi-context-window pattern:** an initializer agent "set up the initial environment: an `init.sh` script" with scaffolding; subsequent coding agents "make incremental progress towards [the] goal." (source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) The docs also cite the memory tool's "multi-session software development pattern" for fast context recovery. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Recovery from mid-session failure (Claude Code):** `/rewind` or double-tap Escape "to restore conversation and code to a previous checkpoint"; press Escape to stop a wrong direction early; use plan mode (Shift+Tab) before implementation to prevent expensive re-work. (source: https://code.claude.com/docs/en/costs)

**Overflow as a reliability signal:** on 4.5+ models, hitting the limit yields `stop_reason: "model_context_window_exceeded"` rather than a hard validation failure — handle this stop reason to trigger compaction/checkpoint-and-continue instead of crashing. (source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

> `[VERIFY]` Retries and idempotency: the scope asks for explicit retry/idempotency patterns. The fetched reliability page emphasizes external-state/checkpointing rather than HTTP-level retries or idempotency keys. Architect-level guidance to convey: make tool calls idempotent and persist state externally so a retried/restarted session reconstructs from durable artifacts (git, progress file, memory tool) rather than from in-window history. Confirm any dedicated Anthropic page on idempotency keys before citing specifics.

---

## 9. How prompt caching intersects (brief — full treatment in C-E4)
*(Reinforces Domain 5; full coverage = extension C-E4)*

**Role:** Caching is "a way to manage cost of large stable context" — it reduces the per-turn cost of re-sending a stable prefix (system prompt, tool defs, long background docs) but does **not** reduce window occupancy. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Mechanism:** on a request the system checks whether a prompt prefix up to a cache breakpoint is already cached; if so it reuses it, otherwise it caches the prefix once the response begins. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**`cache_control` shape:**
```json
{ "cache_control": { "type": "ephemeral", "ttl": "5m" } }
```
(`"1h"` for the 1-hour cache; top-level placement = automatic caching, block-level = explicit breakpoints.) (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Minimum cacheable prefix (by model):** Opus 4.8 / Sonnet 4.6 / Sonnet 4.5 / Opus 4.1 = **1,024 tokens**; Opus 4.7 / Opus 4.6 / Opus 4.5 / Haiku 4.5 = **4,096 tokens**; Haiku 3.5 = 2,048. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching) `[VERIFY]`

**Pricing multipliers (× base input):** 5-min cache write = **1.25×**; 1-hour cache write = **2×**; cache reads (both TTLs) = **0.1×**. E.g., Opus 4.8 ($5 base): 5-min write $6.25, 1-hr write $10, read $0.50 per MTok. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching) `[VERIFY — prices]`

**Caching ↔ context editing interaction:** clearing tool results invalidates the cached prefix at the clear point (use `clear_at_least` to make it worthwhile); keeping thinking blocks preserves the cache. (source: https://platform.claude.com/docs/en/build-with-claude/context-editing)

---

## Key numbers & shapes — quick reference

| Item | Value | Source |
|---|---|---|
| Standard context window | 200K tokens (Haiku 4.5, Sonnet 4.5, legacy) | context-windows |
| Large window | 1M tokens (Opus 4.8/4.7/4.6, Sonnet 4.6) | context-windows |
| Opus 4.8 max output | 128k (300k via batch beta) | models/overview |
| Sonnet 4.6 / Haiku 4.5 max output | 64k | models/overview |
| Microsoft Foundry Opus 4.8 window | 200k | context-windows |
| Images/PDF pages per request | 600 (100 on 200k models) | context-windows |
| Compaction default trigger | 150,000 input tokens (min 50,000) | compaction |
| Compaction beta header | `compact-2026-01-12` | compaction |
| Compaction edit type | `compact_20260112` | compaction |
| Context-editing beta header | `context-management-2025-06-27` | context-editing |
| Tool-clear strategy | `clear_tool_uses_20250919` | context-editing |
| Thinking-clear strategy | `clear_thinking_20251015` | context-editing |
| Overflow stop reason (4.5+) | `model_context_window_exceeded` | context-windows |
| Cache min prefix (Opus 4.8/Sonnet 4.6) | 1,024 tokens | prompt-caching |
| Cache min prefix (Opus 4.6/4.7/Haiku 4.5) | 4,096 tokens | prompt-caching |
| Cache write / read pricing | 1.25× (5m) / 2× (1h) write; 0.1× read | prompt-caching |
| Token-count endpoint | `/v1/messages/count_tokens` (free) | token-counting |
| `usage` fields | `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` | prompt-caching |

**Context-aware budget signal:**
```xml
<budget:token_budget>1000000</budget:token_budget>
<system_warning>Token usage: 35000/1000000; 965000 remaining</system_warning>
```
(source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

**Effective-window formulas:**
- Extended thinking (general): `context_window = (input_tokens − previous_thinking_tokens) + current_turn_tokens`
- Extended thinking + tool use: `context_window = input_tokens + current_turn_tokens`
(source: https://platform.claude.com/docs/en/build-with-claude/context-windows)

---

## [VERIFY] list — version-sensitive / uncertain facts

1. **Model lineup & context sizes (June 2026):** Opus 4.8 (1M), Sonnet 4.6 (1M), Haiku 4.5 (200k); 1M set = Opus 4.8/4.7/4.6 + Sonnet 4.6 + Mythos Preview. Models change fast. (models/overview, context-windows)
2. **[RESOLVED 2026-06-09] No beta header is required for 1M context** on the listed 1M-capable models — 1M is native/no-header; the old `context-1m` beta path is retired for these models. (Confirmed live; `QA-VERIFY-SWEEP_2026-06-09.md`.)
3. **Opus 4.8 excluded from context awareness** — only Sonnet 4.6 / 4.5 / Haiku 4.5 are listed. Confirm Opus has no context-awareness signal. (context-windows)
4. **Compaction beta header `compact-2026-01-12`** and edit type `compact_20260112` — dated, may rev. (compaction)
5. **Context-editing beta header `context-management-2025-06-27`**, strategy strings `clear_tool_uses_20250919` / `clear_thinking_20251015` — dated. (context-editing)
6. **`applied_edits` / `context_management` response object** exact field names (tool uses cleared, tokens freed) — not captured in fetched section; confirm on live page. (context-editing)
7. **Claude Code auto-compact trigger percentage** (~83.5% / ~167K on a 200K window) — circulating in third-party blogs, NOT confirmed on the official `code.claude.com/docs/en/costs` page. Treat as unverified. (code.claude.com/costs)
8. **MRCR v2 8-needle stat** (Opus 4.6 76% vs Sonnet 4.5 18.5%) — from search-summary launch material, not a fetched primary page. (search snippet only)
9. **Prompt-caching minimum-prefix tokens and pricing multipliers** — model-specific and price-sensitive; re-verify against pricing page for C-E4. (prompt-caching)
10. **Batch API 300k output beta `output-300k-2026-03-24`** — dated header. (models/overview)
11. **Retries / idempotency keys** — no dedicated Anthropic page fetched; Section 8 guidance is inferred from the external-state/checkpointing pattern. Confirm before asserting an idempotency-key mechanism exists. (long-running-agents)
12. **Pricing snapshot** (Opus $5/$25, Sonnet $3/$15, Haiku $1/$5 per MTok) — verify against the live pricing page. (models/overview)
