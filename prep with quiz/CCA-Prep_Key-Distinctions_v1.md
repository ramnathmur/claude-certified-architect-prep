# CCA-F Key Distinctions — High-Yield Exam Traps

**Source:** guide_en.MD — all practice questions and explanations  
**Version:** 1.0 | 2026-06-27  
**Purpose:** Each entry is a documented exam trap — a pair of options that look similar but have a decisive difference. Understand the WHY, not just the answer.

---

## Configuration & File Location

### 1. Project scope vs User scope for CLAUDE.md

| | Project scope | User scope |
|---|---|---|
| Location | `.claude/CLAUDE.md` or root `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Version-controlled | ✅ Yes | ❌ No |
| Available to all team members | ✅ Yes | ❌ Only that user |
| Use for | Shared conventions, team standards | Personal preferences, personal workflow |

**Exam trap:** New team member doesn't follow convention that existing members do → convention is in `~/.claude/CLAUDE.md`, not the project file.

---

### 2. `.mcp.json` vs `~/.claude.json`

| | `.mcp.json` | `~/.claude.json` |
|---|---|---|
| Location | Project root | User home directory |
| Scope | Project | User across all projects |
| Version-controlled | ✅ Yes | ❌ No |
| Use for | Shared MCP server config | Personal auth, personal overrides |

**Exam pattern:** Team shares MCP server, each developer has their own token → `.mcp.json` with `${GITHUB_TOKEN}` env var substitution.

---

### 3. `.claude/rules/` vs CLAUDE.md vs Skills

| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---

### 4. Project skills vs Personal skills (same name)

Personal skill at `~/.claude/skills/commit/SKILL.md` **overrides** project skill `.claude/skills/commit/SKILL.md` when they share a name.

**Why:** Allows individual customization without forking the team command or creating an unfamiliar command name.

---

## Agent Architecture

### 5. `stop_reason: "tool_use"` vs `stop_reason: "end_turn"`

| | `tool_use` | `end_turn` |
|---|---|---|
| Meaning | Claude wants to call a tool | Claude finished response |
| Action | Execute tool, append result, continue loop | Stop loop, return response to user |

**Exam trap:** "Parse Claude's text for 'I'm done'" → Wrong. Use structured `stop_reason`, not natural language parsing.

---

### 6. Coordinator pattern vs Direct subagent communication

| | Coordinator hub | Direct inter-agent |
|---|---|---|
| Visibility | Coordinator sees all | Blind to other agents' exchanges |
| Error handling | Centralized, uniform | Each agent handles its own |
| Information control | Coordinator decides what each agent sees | Each agent sees only what was sent directly |
| Correctness | ✅ Correct pattern | ❌ Breaks hub-and-spoke |

---

### 7. Root cause: narrow decomposition vs subagent performance

When all subagents succeed but output is incomplete/wrong-domain → **coordinator's task decomposition**, not subagent capability.

Research system finds only visual art content even though subagents work correctly → coordinator decomposed into visual art subtasks only. Fix the coordinator prompt, not the subagents.

---

### 8. Structured error context vs Generic failure status

| | Structured error context | Generic "search unavailable" |
|---|---|---|
| Includes | Failure type + attempted query + partial results + alternatives | Only: "failed" |
| Enables | Intelligent coordinator recovery (retry with modified query? continue partial?) | Only: retry or abort |
| Correct choice | ✅ Always | ❌ Never return generic status |

---

### 9. Transient vs Permanent errors (MCP tool design)

| | Transient (timeout, network) | Permanent (syntax error, not found) |
|---|---|---|
| Retry? | ✅ Yes, with backoff | ❌ No — will always fail |
| Handle where? | Inside the tool before surfacing | Immediately return error with details |
| "0 results" | Valid result (NOT an error) | — |
| Timeout | Access failure (needs coordinator decision) | — |

**Exam trap:** "0 results" and "timeout" look similar but require completely different responses. Distinguish them explicitly.

---

## Tool Design

### 10. Fix tool descriptions vs Add routing layer

When tool misrouting occurs:
- ✅ Fix tool descriptions first (root cause: descriptions don't distinguish similar tools)
- ❌ Add pre-routing classifier (adds infrastructure without fixing the underlying ambiguity)

**Rule:** Fix the signal (description) before adding a new layer that compensates for the bad signal.

---

### 11. Prompt instructions vs Programmatic preconditions for critical sequencing

| | Prompt instruction | Programmatic precondition |
|---|---|---|
| Reliability | Probabilistic (LLM may not follow) | Deterministic (code enforces) |
| When to use | Default for general guidance | When sequencing is safety/security critical |
| Example | "Always call get_customer first" | Block `lookup_order` until `get_customer` succeeds |

---

### 12. Two-tool token-binding vs `dry_run` boolean parameter

| | Two-tool token-binding | Single tool with `dry_run: bool` |
|---|---|---|
| Can skip preview? | ❌ Architecturally impossible — no token without preview | ✅ Agent can call with `dry_run=false` directly |
| Enforcement | Code-level guarantee | Prompt-level hope |
| Correct for mandatory preview | ✅ Yes | ❌ No |

---

### 13. `context: fork` in skills vs Running in main session

| | `context: fork` | Main session |
|---|---|---|
| Output stored | Isolated subagent context | Main conversation |
| Effect on subsequent turns | None — isolation prevents contamination | Large output or rejected alternatives bleed into next responses |
| Use for | Discovery, analysis, exploration, brainstorming | Implementation, design, conversation |

---

## API and Integration

### 14. Message Batches API vs Synchronous API

| | Synchronous | Batches API |
|---|---|---|
| Cost | Standard | 50% savings |
| Latency | Immediate | Up to 24 hours (no SLA) |
| Multi-turn tool calls | ✅ Supported | ❌ Not supported — fire-and-forget |
| Use for | Blocking checks, interactive use | Scheduled, non-blocking tasks |

**Exam trap:** Iterative code review (fetches related files mid-review via tool calls) → **cannot use batch API**. Batch is fire-and-forget; it cannot execute tools during a request and return results to Claude.

---

### 15. `-p` / `--print` flag vs Other approaches for CI/CD

| | `-p` flag | `CLAUDE_HEADLESS=true` | `--batch` | `stdin < /dev/null` |
|---|---|---|---|---|
| Makes Claude non-interactive? | ✅ Yes — documented approach | ❌ Does not exist | ❌ Does not exist | Workaround, not documented |
| Print output to stdout? | ✅ Yes | — | — | — |

---

## Prompt Engineering

### 16. Few-shot examples vs Instruction refinement for format consistency

When instructions produce inconsistent output format:
- ✅ Few-shot examples showing exact required format (gives model a concrete pattern)
- ❌ More detailed / explicit instructions (already failing; adding more text doesn't help)

---

### 17. Per-file review passes vs Single-pass full-PR review

| | Per-file + integration pass | Single-pass all files |
|---|---|---|
| Attention quality | High per file | Diluted across all files |
| Local issue detection | Consistent depth | Variable — some files shallow, some deep |
| Cross-file issues | Separate integration pass | Included but may be missed |
| Correct for large PRs | ✅ Yes | ❌ No |

**Exam trap:** "Use a larger model with bigger context window" → Wrong. Larger context does not fix attention quality. More tokens available ≠ consistent attention per token.

---

### 18. Target ambiguous examples vs Generic examples for misrouting

- ✅ 4–6 examples targeted at the specific ambiguous cases where misrouting occurs, with rationale
- ❌ 10–15 examples of clear, unambiguous requests for each tool (doesn't address the ambiguous edge cases)

---

### 19. State explicit assumptions vs Ask multiple clarifying questions

For vague user requests:
- ✅ Proceed with stated reasonable assumptions, invite corrections (eliminates abandonment)
- ❌ Ask 4+ clarifying questions (causes 35–40% abandonment rate)
- ❌ Use hidden defaults without stating them (user confused when response doesn't match intent)

---

## Context Management

### 20. "Lost in the middle" mitigation

- ✅ Key-findings summary at the start + explicit section headings
- ❌ Rotation of which agent's output appears first (doesn't fix the attention pattern)
- ❌ Summarize everything to under 20K (may lose critical information)

---

### 21. Persistent case-facts block vs Summarization improvements

For preserving precise numbers/amounts across long conversations:
- ✅ Extract transactional facts into a case-facts block outside summarized history (survives compression)
- ❌ Revise summarization prompt to preserve numbers (still relies on perfect execution)
- ❌ Increase summarization threshold (buys time but doesn't fix the fundamental precision loss)

---

### 22. Subagent isolation for discovery vs Main-session discovery

For verbose discovery that would exhaust main context:
- ✅ Explore subagent: isolates verbose output, returns concise summary to main session
- ❌ Use `/compact` mid-task (loses precision needed for implementation phase)

---

### 23. Behavioral drift: accumulated responses vs Context window overflow

When system prompt behavior degrades across turns at short token counts (2,500 tokens, 7 turns):
- Root cause: ✅ Accumulated assistant responses dilute system prompt influence
- Not: context window overflow (impossible at 2,500 tokens)
- Not: system prompt "only applies to the first turn" (false — it's included in every request)

---

### 24. Semantic retrieval vs Progressive summarization for long-term recall

For specific recall from months of conversation history (85K tokens):
- ✅ Semantic embeddings with retrieval of relevant exchanges
- ❌ Progressive summarization (compresses specific conclusions into abstractions that can't be recalled precisely)

---

### 25. Stateless API memory pattern

Claude has **no server-side memory**. The only way Claude "remembers" prior conversation is because the application includes prior messages in the `messages[]` array.

**Exam trap:** "Claude needs a `session_id` parameter" → False. The API is stateless; the application manages conversation state.

**Exam trap:** "Claude needs a vector database to maintain conversation memory" → False. Simple conversation memory is the `messages[]` array. Vector databases are for retrieval over long histories (months), not standard multi-turn conversations.
