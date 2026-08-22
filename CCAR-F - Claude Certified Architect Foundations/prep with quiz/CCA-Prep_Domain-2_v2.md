# Domain 2: Tool Design & MCP Integration (18%)

**Source:** guide_en.MD — Chapters 2, 4–5, 13, Domain 2 exam notes; CCA-F Official Exam Guide task statements 2.1–2.5; Scenarios: Multi-agent Research System, Customer Support Agent, Code Generation
**Version:** 2.0 | 2026-07-06
**Changelog v2:** Added §2.9 Built-in Tools (official task 2.5 — previously missing entirely); new §2.5 Tool Distribution Across Agents & tool_choice Configuration (absorbs v1 §2.7 Least Privilege, adds tool-count reliability, cross-role tools, tool_choice depth); expanded §2.3 with the four error categories, business-rule errors, and empty-results-vs-access-failures; expanded §2.6 (formerly §2.5 MCP) with MCP resources as content catalogs, community-vs-custom server selection, and MCP-vs-built-in tool description competition. All v1 content retained; §2.5–2.8 renumbered.

---

## 2.1 Claude API Tool Use

### How Tool Calling Works
1. Define tools in API request with `name`, `description`, and `input_schema` (JSON Schema)
2. Claude returns a response with `stop_reason: "tool_use"` and a `tool_use` content block
3. Application executes the tool
4. Application appends a `tool_result` content block to the conversation
5. Claude continues from the result

### `tool_use` Content Block Structure
```json
{
  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "lookup_order",
  "input": {"order_id": "12345"}
}
```
Key fields: `id` (for matching to `tool_result`), `name`, `input`

### `tool_choice` Parameter
| Value | Behavior |
|---|---|
| `{"type": "auto"}` | Claude decides whether to use a tool (default) |
| `{"type": "any"}` | Claude must use at least one tool |
| `{"type": "tool", "name": "X"}` | Claude must use tool X specifically |

Configuration depth — when to use each value — is covered in §2.5.

---

## 2.2 Tool Description Design

### The Primary Lever for Tool Selection
Tool descriptions are the **primary input** Claude uses to decide which tool to call. When misrouting occurs, **check descriptions first** before adding classifiers or few-shot examples.

### Description Quality Requirements
A good tool description specifies:
- **What it does** (purpose, not just name)
- **What input it accepts** (formats, ID types, examples)
- **When to use it** vs similar tools
- **When NOT to use it** (boundary cases)

**Exam scenario:** `analyze_content` (web-search agent) vs `analyze_document` (doc-analysis agent) — names nearly identical → misrouting 45% of time.
- ✅ Rename web-search tool to `extract_web_results`, update description to explicitly reference "web search and URLs"
- ❌ Add pre-routing classifier (adds infrastructure without fixing root cause)

**Exam scenario:** `get_customer` vs `lookup_order` both have 1-line descriptions, similar ID formats → `get_customer` called for order queries.
- ✅ Expand both descriptions with input formats, example queries, edge cases, and boundaries
- ❌ Combine into single `lookup_entity` tool (loses semantic precision)

---

## 2.3 Structured Tool Errors

### `isError` Flag in MCP
MCP tools return results with an optional `isError: true` flag to signal failure. The agent receives this and decides how to proceed.

### The Four Error Categories
The exam distinguishes four categories of tool error — each demands a different agent response:

| Category | Example | Retryable? | Correct agent response |
|---|---|---|---|
| **Transient** | Timeout, service temporarily unavailable | Yes | Retry (ideally handled inside the tool/subagent first) |
| **Validation** | Invalid input, malformed ID | No (as-is) | Fix the input and re-call |
| **Business** | Policy violation (e.g., refund exceeds policy limit) | **No** | Explain the policy outcome to the user — never retry |
| **Permission** | Auth failure, access denied | No | Escalate or switch credentials — retrying is wasted effort |

### Structured Error Response Design
Tool errors should include:
```json
{
  "isError": true,
  "errorCategory": "transient | validation | business | permission",
  "isRetryable": true,
  "description": "Patent database connection timed out after 30s",
  "partialResults": [...],
  "alternatives": ["Try with shorter query", "Use alternate endpoint"]
}
```

**Exam principle:** Returning a `retryable` boolean flag is BETTER than forcing the agent to guess from error text, but WORSE than handling transient errors internally and only surfacing the ones requiring coordinator decision.

### Business-Rule Errors: A Distinct Category
A business-rule violation (policy limit exceeded, action not allowed for this account tier) is **not a failure of the tool** — it is a valid answer that the requested action is disallowed. Structure it as:
- `retriable: false` — signals the agent that re-invoking cannot change the outcome
- A **customer-friendly explanation** in the payload — so the agent can communicate the policy outcome appropriately without paraphrasing internal jargon

**Exam scenario:** Support agent's `process_refund` tool rejects a refund because it exceeds the 30-day policy window. The agent keeps retrying the call.
- ✅ Return `retriable: false` + customer-friendly explanation ("Refunds are available within 30 days of purchase; this order is outside that window") so the agent stops retrying and explains the policy to the customer
- ❌ Return a generic `"Operation failed"` — the agent cannot distinguish policy denial from a transient outage, so it retries or escalates incorrectly
- ❌ Classify it as a transient error with `isRetryable: true` — wastes retry attempts on an outcome that can never change

### Valid Empty Results vs Access Failures
An **empty result is a successful query** with no matches — not an error. Conflating the two corrupts agent decision-making in both directions:

| Situation | Correct signal | Wrong signal causes |
|---|---|---|
| Query ran, zero matches | Success, empty result set (`isError` absent/false) | Agent retries or escalates a query that worked fine |
| Query could not run (DB down, access denied) | `isError: true` with category | Agent reports "no data found" when data may exist |

- ✅ `search_orders` returns `{"results": [], "isError": false}` when the customer genuinely has no orders — the agent confidently reports "no orders found"
- ❌ Return `isError: true` for zero matches (agent treats a valid answer as a failure and retries)
- ❌ Return an empty list when the database connection failed (agent tells the customer "you have no orders" — a false statement caused by masking an access failure)

### Error Handling at the Right Level
- **Inside the tool:** Handle transient failures (retry + backoff) before surfacing
- **Inside the subagent:** Local recovery for transient failures; propagate to the coordinator only errors it cannot resolve locally, along with partial results and what was attempted
- **Return to agent:** Only when the error requires a decision only the agent can make (skip? retry with different params? escalate?)
- **Never:** Return success with embedded error metadata — masks failures

---

## 2.4 Two-Tool Token-Binding Pattern

For operations that must always be preceded by a preview/dry-run:

**Problem:** `dry_run: boolean` parameter on a single tool — agent bypasses dry run by calling with `dry_run=false` directly.

**Solution:** Replace with two tools:
1. `preview_remove_member` → returns impact details + a **single-use confirmation token**
2. `execute_remove_member` → requires that token as a parameter

This makes it **architecturally impossible** to execute without a prior preview — the token only exists after a preview call.

**Why this beats alternatives:**
- Server-side timing heuristic (A) — fragile to timing conditions
- Orchestration-layer confirmation prompt (B) — requires extra infrastructure
- Prompt instruction + examples (C) — probabilistic, not guaranteed

---

## 2.5 Tool Distribution Across Agents & tool_choice Configuration

### Too Many Tools Degrades Selection Reliability
Giving an agent access to too many tools (the official guide's own numbers: **18 instead of 4–5**) degrades tool selection reliability by increasing decision complexity. Each additional tool is another candidate the model must discriminate between on every turn — more overlap, more near-miss descriptions, more misrouting.

**Exam scenario:** A subagent with 18 tools frequently calls the wrong one; a peer agent with 5 role-scoped tools selects correctly.
- ✅ Restrict each subagent's tool set to the 4–5 tools relevant to its role
- ❌ Keep all 18 tools and add more detailed descriptions to every one (descriptions help, but tool count itself is the root cause — reduce the decision space first)
- ❌ Give every agent the full tool catalog "for flexibility" (agents with tools outside their specialization tend to misuse them — e.g., a synthesis agent attempting web searches)

### Least Privilege in Tool Design
Each agent or component should have **only the tools it needs** for its scope. Giving broader tools leads to scope creep and unintended behavior.

**Exam scenario:** Document analysis agent has `fetch_url` → starts downloading search engine results pages.
- ✅ Replace with `load_document` that validates URL points to a document format (replacing a generic tool with a **constrained alternative** enforces the boundary at the interface level)
- ❌ Add prompt instruction (probabilistic)
- ❌ Block known search-engine domains (fragile, not future-proof)

### Scoped Cross-Role Tools for High-Frequency Needs
Strict role scoping has one sanctioned exception: when an agent has a **high-frequency need** that would otherwise force constant round-trips through the coordinator, give it a **narrowly scoped cross-role tool** — while **complex cases still route through the coordinator**.

**Exam scenario:** Synthesis agent frequently needs to confirm individual facts while writing its report.
- ✅ Give it a `verify_fact` tool scoped to simple lookups; complex research questions still go back through the coordinator to the research agents
- ❌ Give the synthesis agent full `web_search` access (cross-specialization misuse: it starts doing open-ended research instead of synthesizing)
- ❌ Route every single fact check through the coordinator (correct scoping, but the round-trip overhead on a high-frequency need is exactly what scoped cross-role tools exist to avoid)

### tool_choice Configuration Depth
| Value | Guarantees | When to use |
|---|---|---|
| `{"type": "auto"}` | Nothing — model may answer in plain text | Default for most agentic loops |
| `{"type": "any"}` | The model **will call some tool** — never returns conversational text | When you need guaranteed structured output; with multiple extraction tools, the model still picks the best one |
| `{"type": "tool", "name": "extract_metadata"}` | The model **will call that specific tool** | When a specific first step must be guaranteed (execution order) |

**Forced-first-step pattern:** Force `extract_metadata` on the first turn (`{"type": "tool", "name": "extract_metadata"}`), then process subsequent steps — enrichment tools, follow-ups — in **follow-up turns** where `tool_choice` is relaxed back to `"auto"` or `"any"`.

**Exam scenario:** A pipeline must always extract document metadata before any enrichment tool runs, but a prompt instruction is only followed ~90% of the time.
- ✅ Set `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first request, then continue with `"auto"` for the rest of the workflow
- ❌ Strengthen the prompt instruction ("ALWAYS call extract_metadata first") — probabilistic, not guaranteed
- ❌ Leave `tool_choice` forced on every turn — the model can then never call the enrichment tools at all

**Exam scenario:** An extraction agent sometimes replies with prose instead of calling any extraction tool.
- ✅ Set `tool_choice: {"type": "any"}` — guarantees a tool call instead of conversational text
- ❌ Set `tool_choice: {"type": "auto"}` and add "you must use a tool" to the prompt (auto permits text responses; the instruction is probabilistic)

---

## 2.6 Model Context Protocol (MCP)

### Three MCP Primitives
| Primitive | Purpose | Analogous to |
|---|---|---|
| **Tools** | Actions Claude can call | API endpoints |
| **Resources** | Read-only data Claude can access | Files/databases |
| **Prompts** | Pre-built prompt templates | Reusable instructions |

Tools from **all configured MCP servers are discovered at connection time** and are available to the agent simultaneously.

### Configuration Files
| File | Scope | Purpose |
|---|---|---|
| `.mcp.json` (project root) | Project-wide, version-controlled | Shared team MCP configuration |
| `~/.claude.json` (user home) | User-specific | Personal overrides, personal auth, experimental servers |

**Exam pattern:** Team uses shared MCP server. Each developer has their own GitHub token.
- ✅ Add server to `.mcp.json` with `${GITHUB_TOKEN}` environment variable substitution; document the variable in README
- ❌ Each developer adds server in user scope (inconsistent tooling)
- ❌ Commit a placeholder token (security risk)

### Environment Variable Substitution
`.mcp.json` supports `${VAR_NAME}` syntax. At runtime, Claude Code substitutes the variable from the environment. This lets project config be version-controlled while credentials stay out of the repo.

### MCP Resources as Content Catalogs
Resources expose **content catalogs** — issue summaries, documentation hierarchies, database schemas — giving the agent an immediate "map" of what data exists **without exploratory tool calls**.

**Exam scenario:** An agent working against a project tracker burns many turns calling `search_issues` with guessed queries just to discover what issues exist.
- ✅ Expose an issue-summary catalog as an MCP **resource** — the agent reads the catalog for visibility into available data, then makes targeted tool calls
- ❌ Add a `list_everything` tool the agent must remember to call first (a resource provides the map as readable context; a tool adds an LLM call and relies on the agent thinking to use it)
- ❌ Paste the full issue database into the system prompt (resources are requested on demand; a static dump bloats context and goes stale)

### Community Servers vs Custom Servers
- ✅ For **standard integrations** (Jira, GitHub, Slack), prefer **existing community MCP servers**
- ✅ Build **custom servers only for unique, team-specific workflows** that no existing server covers
- ❌ Build a custom Jira MCP server from scratch "for control" (reinvents a maintained standard integration; custom effort belongs on workflows unique to your team)

### MCP Tool Descriptions vs Built-in Tools
Agents may **prefer built-in tools (like Grep, Read) over MCP tools** with similar-sounding functionality, because tool selection runs on descriptions. If the MCP tool's description does not make its superior capability explicit, the agent falls back to the familiar built-in.

**Exam scenario:** A code-search MCP server offers semantic, index-backed search, but the agent keeps using built-in Grep instead.
- ✅ Enhance the MCP tool's description to explain its capabilities and outputs in detail — highlight concrete advantages, unique data, or context built-in tools cannot provide
- ❌ Remove or disable Grep so the agent has no alternative (breaks legitimate content-search use cases; the root cause is an under-specified description, not the built-in tool's existence)
- ❌ Add a system prompt rule "always prefer MCP tools" (blunt, keyword-sensitive instruction that can misroute cases where the built-in genuinely is the right tool)

---

## 2.7 Hooks: PostToolUse and PreToolUse

### What Hooks Do
Hooks are deterministic code that runs around tool calls. They intercept tool interactions without relying on the LLM.

| Hook | Fires | Use for |
|---|---|---|
| `PreToolUse` | Before tool executes | Validate, block, modify params |
| `PostToolUse` | After tool returns | Transform output, log, normalize |

### PostToolUse — Primary Use Case: Output Normalization
When multiple tools return different data formats (Unix timestamps, ISO 8601 dates, numeric status codes) from sources you cannot modify:
- ✅ Use `PostToolUse` hook to intercept and normalize all outputs centrally
- ❌ Modify tools you control + create wrappers for third-party tools (fragmented maintenance)
- ❌ Create a `normalize_data` tool the agent calls after every retrieval (adds LLM call overhead)
- ❌ Document formats in system prompt (relies on LLM interpretation)

### PreToolUse — Primary Use Case: Threshold Enforcement
Block operations above a defined threshold (e.g., bulk deletion affecting >50 records) and route to escalation. This is **deterministic** — it fires regardless of LLM behavior.

**Exam distinction:** Hooks are deterministic. System prompt instructions are probabilistic. For safety-critical enforcement, use hooks.

---

## 2.8 Tool Bundling / Composite Tools

When agents frequently call multiple tools in sequence for the same operation, consider creating composite tools.

**But:** The preferred approach (from practice test) is to **prompt the agent to bundle tool requests into one turn** rather than creating composite tools, as the agent can naturally request multiple tools simultaneously.

**Exam scenario:** Support agent calls `get_customer` and `lookup_order` in separate sequential turns even when both are needed.
- ✅ Instruct Claude in prompt to bundle related tool requests into one turn
- Not preferred: Create `get_customer_with_orders` composite tool (hides the composition)

---

## 2.9 Built-in Tools: Read, Write, Edit, Bash, Grep, Glob

### Tool Selection Reference
| Task | Tool | Example |
|---|---|---|
| Find files by name/extension pattern | **Glob** | `**/*.test.tsx`, `src/components/**/*.ts` |
| Search within file contents | **Grep** | Function names, error messages, import statements |
| Read a file in full | **Read** | Load a file for analysis |
| Write a new file (or full replacement) | **Write** | Create a file from scratch |
| Targeted modification of an existing file | **Edit** | Replace a specific snippet via **unique text match** |
| Run a shell command | **Bash** | git, npm, run tests, build |

### Grep vs Glob — The Core Distinction
- **Grep = content search.** Searches *inside* files for patterns: function names, error messages, import statements. "Find all callers of `processPayment`" → Grep.
- **Glob = file-path pattern matching.** Finds files *by name or extension pattern*: "Find all test files" → Glob `**/*.test.tsx`.

**Exam scenario:** Locate every file that references a deprecated `formatDate` function.
- ✅ Grep for `formatDate` across the codebase (the target is file *content*)
- ❌ Glob for `**/formatDate*` (Glob matches file *paths*, not what's inside files — this only finds files *named* formatDate)

**Exam scenario:** Apply a convention change to all TypeScript test files.
- ✅ Glob `**/*.test.tsx` to enumerate the files by naming pattern
- ❌ Grep for the word "test" in file contents (matches unrelated files mentioning "test"; misses test files that don't contain the literal word)

### Incremental Investigation Strategy
Build codebase understanding **incrementally** — never read all files upfront:

```
1. Grep: find entry points (function definition, export)
2. Read: read the found files
3. Grep: find usages (imports, call sites)
4. Read: read consumer files, follow imports, trace flows
5. Repeat until the picture is complete
```

- ✅ Start with Grep to locate entry points, then Read to follow imports and trace flows
- ❌ Read every file in the repository first to "get full context" (burns context window on irrelevant files; the exam treats upfront bulk reading as the anti-pattern)
- ❌ Glob the whole tree and Read each match before searching (same anti-pattern — discovery should be driven by content search, then targeted reads)

### Edit Failure on Non-Unique Matches → Read + Write Fallback
**Edit works by unique text matching.** If the anchor text appears more than once in the file, Edit fails — it cannot decide which occurrence to modify. The reliable fallback:

1. **Read** — load the full file content
2. Modify the content programmatically
3. **Write** — write the updated version

- ✅ When Edit cannot find a unique anchor, fall back to Read + Write for a reliable full-file modification
- ❌ Retry Edit with a shorter, more generic anchor string (shorter anchors are *more* likely to be non-unique, not less)
- ❌ Use Bash with `sed` to force the replacement (bypasses the tool designed for the job; the exam's sanctioned fallback is Read + Write)

### Tracing Function Usage Across Wrapper Modules
When a function is re-exported or wrapped by intermediate modules, searching only for the original name misses call sites that use the wrapper's name.

**Strategy:** first **identify all exported names** (the original plus every wrapper/re-export alias), then **search for each name** across the codebase.

**Exam scenario:** `calculateTax` is wrapped by `utils/tax.ts` as `getTax` and re-exported from `index.ts`. A rename must update every caller.
- ✅ First Grep/Read the wrapper modules to collect all exported names (`calculateTax`, `getTax`), then Grep for each name to find all call sites
- ❌ Grep only for `calculateTax` and conclude those are all the callers (misses every consumer that imports the `getTax` wrapper)

---

**Section count:** 9 major sections (§2.1–§2.9)
