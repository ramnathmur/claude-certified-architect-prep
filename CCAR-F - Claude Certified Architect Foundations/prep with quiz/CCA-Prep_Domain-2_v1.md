# Domain 2: Tool Design & MCP Integration (18%)

**Source:** guide_en.MD — Chapters 4–5, Scenarios: Multi-agent Research System, Customer Support Agent, Code Generation  
**Version:** 1.0 | 2026-06-27

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

### Structured Error Response Design
Tool errors should include:
```json
{
  "isError": true,
  "errorCategory": "timeout | syntax_error | not_found | auth_failure",
  "isRetryable": true,
  "description": "Patent database connection timed out after 30s",
  "partialResults": [...],
  "alternatives": ["Try with shorter query", "Use alternate endpoint"]
}
```

**Exam principle:** Returning a `retryable` boolean flag is BETTER than forcing the agent to guess from error text, but WORSE than handling transient errors internally and only surfacing the ones requiring coordinator decision.

### Error Handling at the Right Level
- **Inside the tool:** Handle transient failures (retry + backoff) before surfacing
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

## 2.5 Model Context Protocol (MCP)

### Three MCP Primitives
| Primitive | Purpose | Analogous to |
|---|---|---|
| **Tools** | Actions Claude can call | API endpoints |
| **Resources** | Read-only data Claude can access | Files/databases |
| **Prompts** | Pre-built prompt templates | Reusable instructions |

### Configuration Files
| File | Scope | Purpose |
|---|---|---|
| `.mcp.json` (project root) | Project-wide, version-controlled | Shared team MCP configuration |
| `~/.claude.json` (user home) | User-specific | Personal overrides, personal auth |

**Exam pattern:** Team uses shared MCP server. Each developer has their own GitHub token.
- ✅ Add server to `.mcp.json` with `${GITHUB_TOKEN}` environment variable substitution; document the variable in README
- ❌ Each developer adds server in user scope (inconsistent tooling)
- ❌ Commit a placeholder token (security risk)

### Environment Variable Substitution
`.mcp.json` supports `${VAR_NAME}` syntax. At runtime, Claude Code substitutes the variable from the environment. This lets project config be version-controlled while credentials stay out of the repo.

---

## 2.6 Hooks: PostToolUse and PreToolUse

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

## 2.7 Least Privilege in Tool Design

Each agent or component should have **only the tools it needs** for its scope. Giving broader tools leads to scope creep and unintended behavior.

**Exam scenario:** Document analysis agent has `fetch_url` → starts downloading search engine results pages.
- ✅ Replace with `load_document` that validates URL points to document format (enforces constraint at interface level)
- ❌ Add prompt instruction (probabilistic)
- ❌ Block known search-engine domains (fragile, not future-proof)

**Exam scenario:** Synthesis agent needs simple fact verification.
- ✅ `verify_fact` tool scoped to simple lookups
- ❌ Full `web_search` tool access

---

## 2.8 Tool Bundling / Composite Tools

When agents frequently call multiple tools in sequence for the same operation, consider creating composite tools.

**But:** The preferred approach (from practice test) is to **prompt the agent to bundle tool requests into one turn** rather than creating composite tools, as the agent can naturally request multiple tools simultaneously.

**Exam scenario:** Support agent calls `get_customer` and `lookup_order` in separate sequential turns even when both are needed.
- ✅ Instruct Claude in prompt to bundle related tool requests into one turn
- Not preferred: Create `get_customer_with_orders` composite tool (hides the composition)
