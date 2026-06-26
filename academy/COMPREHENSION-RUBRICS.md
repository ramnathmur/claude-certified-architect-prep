# Comprehension Rubrics (per concept)

**Audience:** the Professor (and Exam Coach), at teaching time.
**Purpose:** make the strong / partial / surface / absent judgement **consistent across sessions** instead of improvised. Per `ENGAGEMENT-PROTOCOL.md → Per-concept rubric`, hold the 3-part rubric BEFORE asking the open question.

Each concept has:
- **Minimum acceptable answer** — the core idea the learner must state, in their own words, to count as "strong."
- **Common wrong answer** — the predictable misconception (often the exam's tempting distractor) to watch for.
- **Diagnostic follow-up** — one question that separates real understanding from echoing.

When a learner lands on the "common wrong answer," log a one-line note in `LEARNER-MODEL.md` — it is a high-value gap/interlink signal. One rubric per sub-domain (35 total).

---

## Domain 1 — Agentic Architecture & Orchestration

### D1.1 — Agentic loop fundamentals (`stop_reason`, stateless model)
- **Minimum acceptable:** the loop sends a request, checks `stop_reason`; `tool_use` → run the tool, append the result, loop; `end_turn` → done. The model is stateless, so full history is re-sent each call.
- **Common wrong answer:** treating textual content ("Task complete") or a fixed `max_iterations` as the completion signal.
- **Diagnostic follow-up:** "If the model returns text AND a tool call, what does your loop do next, and what is the ONLY reliable stop signal?"

### D1.2 — `AgentDefinition` + least privilege
- **Minimum acceptable:** an agent is configured by name, description, system_prompt, and `allowed_tools`; give it only the tools its role needs (least privilege) to improve reliability.
- **Common wrong answer:** "give it all the tools so it's flexible."
- **Diagnostic follow-up:** "Why does adding 15 tools to one agent usually make it *worse*, not more capable?"

### D1.3 — Hub-and-spoke / coordinator
- **Minimum acceptable:** the coordinator owns decomposition, delegation, aggregation, error handling, and user comms; all inter-agent communication flows through it for observability and control.
- **Common wrong answer:** letting subagents talk to each other directly to "save a hop."
- **Diagnostic follow-up:** "Two subagents need each other's output. Why route it through the coordinator instead of agent-to-agent?"

### D1.4 — Task/Agent tool + explicit context passing + parallel spawn
- **Minimum acceptable:** subagents are spawned via the Task tool (renamed **Agent** in v2.1.63); they do NOT inherit parent context, so all needed context goes in the spawn prompt; multiple spawns in one turn run in parallel.
- **Common wrong answer:** assuming the subagent can see the parent's history / tool results.
- **Diagnostic follow-up:** "Your subagent acts like it doesn't know the document. What's the fix — and what does it tell you about subagent context?"

### D1.5 — Hooks (Pre/PostToolUse; deterministic vs probabilistic)
- **Minimum acceptable:** hooks intercept the lifecycle; `PreToolUse` can block/modify a call before it runs, `PostToolUse` transforms/observes the result; hooks are deterministic (code), prompts are probabilistic — use hooks for financial/legal/safety rules.
- **Common wrong answer:** enforcing a hard money/compliance limit with a strongly-worded prompt.
- **Diagnostic follow-up:** "Block every refund over $500, guaranteed. Prompt or hook — and which hook?"

### D1.6 — Escalation patterns + structured handoff
- **Minimum acceptable:** escalate by **category/impact** (explicit request for a human, policy gap, lack of authority, no progress), not a fail-counter; immediate vs attempt-then-escalate; the handoff is a structured summary (customer_id, issue, root cause, actions taken, recommended action), not the transcript.
- **Common wrong answer:** "escalate after N failed tool calls" or escalating on first sign of frustration.
- **Diagnostic follow-up:** "Why is 'escalate after 3 failed calls' a worse rule than judging category and impact?"

### D1.7 — Session management (`--resume`, `fork_session`)
- **Minimum acceptable:** `--resume` continues a named session with saved context; `fork_session` branches independent lines from a shared point; start fresh (with a summary) when prior results are stale.
- **Common wrong answer:** resuming an old session whose files/results have since changed and trusting the stale tool output.
- **Diagnostic follow-up:** "Files changed since yesterday's session. Resume, or start fresh — and why?"

### D1.8 — Task decomposition (fixed vs dynamic; multi-pass)
- **Minimum acceptable:** fixed pipelines (prompt chaining) for predictable work; dynamic decomposition when each step depends on prior findings; multi-file review = per-file passes + a cross-file integration pass (avoids attention dilution).
- **Common wrong answer:** one pass over 14 files at once "because the context fits."
- **Diagnostic follow-up:** "A 14-file PR review gives inconsistent depth. Why does splitting into passes fix it — and what does the extra pass catch?"

---

## Domain 3 — Claude Code Configuration & Workflows

### D3.1 — CLAUDE.md hierarchy + `@path`
- **Minimum acceptable:** user (`~/.claude`) vs project (`.claude/`/root) vs directory-level; team standards belong at project level (VCS-shared); `@path` imports modularize config (no space, ≤5 nesting).
- **Common wrong answer:** putting team coding standards in the user-level file (new teammates never get them).
- **Diagnostic follow-up:** "A new hire isn't getting the project's standards. Where did they likely live, and where should they?"

### D3.2 — Path-specific rules (`.claude/rules/` with `paths:`)
- **Minimum acceptable:** rule files load only when editing files matching their `paths:` glob — ideal for conventions spread across many directories (tests, migrations); saves context.
- **Common wrong answer:** using a directory-level CLAUDE.md for test rules when tests are scattered everywhere.
- **Diagnostic follow-up:** "Test conventions apply to `*.test.ts` in 8 packages. `.claude/rules/` with `paths:` or a CLAUDE.md per dir — why?"

### D3.3 — Skills frontmatter (`context:fork`, `allowed-tools`, `argument-hint`)
- **Minimum acceptable:** `context:fork` isolates verbose skill output in a subagent; `allowed-tools` **pre-approves** the listed tools (does NOT restrict the rest — `disallowed-tools` restricts); `argument-hint` prompts for a missing arg.
- **Common wrong answer:** believing `allowed-tools` *restricts* the skill to only those tools.
- **Diagnostic follow-up:** "Does `allowed-tools: [Read]` stop the skill from calling Bash? What actually removes a tool?"

### D3.4 — Planning mode vs direct + Explore subagent
- **Minimum acceptable:** planning mode = read-only explore + a plan to approve, for large/multi-approach/architectural/unfamiliar changes; direct execution for clear single-file fixes; Explore subagent isolates verbose discovery.
- **Common wrong answer:** direct execution on a monolith→microservices split "and switch to planning if it gets hard."
- **Diagnostic follow-up:** "Restructure a monolith touching dozens of files — which mode, and why is reactive switching worse?"

### D3.5 — `/compact` and `/memory`
- **Minimum acceptable:** `/compact` compresses history to free the window (risk: exact numbers/dates lost); `/memory` edits CLAUDE.md to persist notes across sessions.
- **Common wrong answer:** assuming `/compact` is lossless / safe for precise figures.
- **Diagnostic follow-up:** "After `/compact`, why might the agent suddenly be vague about a specific amount it knew earlier?"

### D3.6 — CI/CD (`-p` / `--bare` / `--output-format json`)
- **Minimum acceptable:** `-p`/`--print` runs non-interactive (the correct CI flag); `--bare` additionally skips ALL local config (hooks, CLAUDE.md, skills, MCP, memory) — `-p` alone does NOT; `--output-format json` + `--json-schema` for parseable output.
- **Common wrong answer:** thinking `claude -p "…"` already runs clean/config-free, or that CI just needs the default invocation.
- **Diagnostic follow-up:** "Your CI run unexpectedly picked up a CLAUDE.md rule. Which flag was missing, and what does it skip?"

---

## Domain 4 — Prompt Engineering & Structured Output

### D4.1 — Few-shot prompting
- **Minimum acceptable:** 2–4 examples teach format AND decision logic better than prose; especially powerful for ambiguous cases and informal/edge inputs; the model generalizes the pattern.
- **Common wrong answer:** adding more abstract instructions instead of examples when output is inconsistent.
- **Diagnostic follow-up:** "Instructions keep producing variable formatting. Why are 3 examples more reliable than a longer instruction?"

### D4.2 — Explicit criteria vs vague instructions
- **Minimum acceptable:** "flag ONLY if it contradicts the code" beats "be conservative"; define severity levels with examples; high false-positive categories erode trust in accurate ones.
- **Common wrong answer:** fixing false positives by saying "be more careful / conservative."
- **Diagnostic follow-up:** "Reviews flag acceptable patterns. What's more effective than 'be conservative,' and why?"

### D4.3 — Prompt chaining
- **Minimum acceptable:** break a complex task into focused sequential steps to avoid attention dilution; use for predictable, repeatable work (vs dynamic decomposition for open-ended).
- **Common wrong answer:** conflating prompt chaining (fixed) with dynamic decomposition (emergent).
- **Diagnostic follow-up:** "When is a fixed chain right, and when do you need dynamic decomposition instead?"

### D4.4 — The "interview" pattern
- **Minimum acceptable:** ask clarifying questions before building when interpretations diverge, the action is costly/irreversible, or approaches differ — one question at a time.
- **Common wrong answer:** proceeding on an assumption (or averaging conflicting preferences) instead of disambiguating which entity/approach.
- **Diagnostic follow-up:** "Two readings of the request both seem plausible. Ask or assume — and how many questions at once?"

### D4.5 — `tool_use` + JSON Schema
- **Minimum acceptable:** tool_use with a JSON schema is the most reliable structured output; guarantees syntax/required fields but NOT semantic correctness; mark genuinely-optional fields nullable to avoid fabrication.
- **Common wrong answer:** assuming valid-schema JSON means the *values* are correct; or making absent fields required.
- **Diagnostic follow-up:** "Schema-valid JSON came back with a wrong total. What did the schema guarantee, and what must you still check?"

### D4.6 — `tool_choice`
- **Minimum acceptable:** `auto` = optional, `any` = required-from-set, `{type:tool,name}` = that tool, `none` = off; only `any`/named **guarantee** a call.
- **Common wrong answer:** expecting `auto` to guarantee a tool call.
- **Diagnostic follow-up:** "You MUST get a structured tool call, not prose. Which `tool_choice`, and why not `auto`?"

### D4.7 — Syntax vs semantic errors
- **Minimum acceptable:** syntax errors (bad JSON/type) are eliminated by tool_use+schema; semantic errors (totals don't add up, wrong field) need validation/retry/self-correction.
- **Common wrong answer:** believing schemas catch logic errors.
- **Diagnostic follow-up:** "Which error type does a strict schema NOT fix, and how do you catch it?"

### D4.8 — Validation, retry-with-feedback, self-correction
- **Minimum acceptable:** Structured Outputs/constrained decoding is the source-level fix for malformed JSON (retry is the fallback); retry-with-feedback resends doc + bad extraction + the exact error; retry can't help when info is absent from the source.
- **Common wrong answer:** treating blind retries as the primary fix; or retrying when the data simply isn't in the document.
- **Diagnostic follow-up:** "Extraction fails validation. When will a feedback-retry help, and when is it pointless?"

### D4.9 — Message Batches API
- **Minimum acceptable:** ~50% cheaper, up to 24h, no latency SLA, no multi-turn tool calling; `custom_id` correlates results; use for overnight/bulk, not blocking pre-merge checks.
- **Common wrong answer:** putting a blocking, developer-waiting check on the Batch API to save 50%.
- **Diagnostic follow-up:** "Pre-merge check vs overnight tech-debt report — which goes on Batch, and why not both?"

### D4.10 — Multi-instance / multi-pass review
- **Minimum acceptable:** the generating instance is biased toward its own reasoning; use an independent instance (no generation context) to review; split multi-file review into per-file + integration passes.
- **Common wrong answer:** asking the same session that wrote the code to self-review it.
- **Diagnostic follow-up:** "Why does a fresh Claude instance catch issues the generating one rationalized away?"

---

## Domain 2 — Tool Design & MCP Integration

### D2.1 — Tool description as the selection mechanism
- **Minimum acceptable:** the description is the PRIMARY signal the model uses to pick a tool; it must state what/when-to-use/when-not/inputs/limits; overlapping descriptions cause misrouting (fix by renaming/differentiating); system-prompt wording can bias tool choice.
- **Common wrong answer:** "the model picks by tool name / schema" or "add few-shot routing" before fixing minimal descriptions.
- **Diagnostic follow-up:** "Agents call the wrong one of two similarly-described tools. Cheapest highest-impact first fix?"

### D2.2 — MCP fundamentals (tools / resources / prompts)
- **Minimum acceptable:** tools = model-controlled actions; resources = passive read-only context (schemas, catalogs — no tool call to use); prompts = reusable workflows. Resources for "what is true/stable," tools for "what actions can be taken."
- **Common wrong answer:** modeling a catalog/schema as a tool instead of a resource.
- **Diagnostic follow-up:** "An agent needs the product catalog for context. Tool or resource — and why?"

### D2.3 — MCP server config (`.mcp.json` vs `~/.claude.json`)
- **Minimum acceptable:** `.mcp.json` (project root, VCS-shared, team) with `${ENV}` secret substitution; `~/.claude.json` for personal/experimental; prefer community servers for standard integrations.
- **Common wrong answer:** committing tokens, or putting a team server in the user config.
- **Diagnostic follow-up:** "Six devs need a shared GitHub MCP server without committing tokens. Where, and how are secrets handled?"

### D2.4 — `isError` + two error channels
- **Minimum acceptable:** `isError:true` is a tool-EXECUTION error inside a *successful* JSON-RPC response (the tool ran but failed); a JSON-RPC PROTOCOL error means the request itself failed (unknown tool, bad args). Structured errors carry category/retryable/message; four categories (transient→retry, validation→fix input, business→explain, permission→escalate).
- **Common wrong answer:** treating `isError:true` as a protocol/transport failure, or returning a generic "operation failed."
- **Diagnostic follow-up:** "A timed-out orders API vs a call to a non-existent tool — which channel carries each?"

### D2.5 — Tool allocation + `tool_choice` (too-many-tools)
- **Minimum acceptable:** too many tools per agent (≈18 vs 4–5) degrades selection; scope each agent to role-relevant tools; replace general tools with constrained ones; use `tool_choice` to force order/structured calls.
- **Common wrong answer:** judging "8 tool calls in one turn" as a smell by count (parallel calls to *independent* tools is good — the dependency structure is the tell).
- **Diagnostic follow-up:** "When is calling many tools in one turn good design, and when is it a smell?"

### D2.6 — Built-in tools + incremental investigation
- **Minimum acceptable:** Grep = content inside files, Glob = filenames/paths, Read/Write = whole files, Edit = targeted unique-match (fallback Read+Write), Bash = last resort; investigate incrementally (Grep entry points → Read → Grep usages → Read).
- **Common wrong answer:** using filename search to find in-file references, or reading everything up front.
- **Diagnostic follow-up:** "Find every caller of `refund()` across the repo. Which tool first, and why not Glob?"

---

## Domain 5 — Context Management & Reliability

### D5.1 — Context window risks / lost-in-the-middle
- **Minimum acceptable:** the window = system + history + tool defs + tool results; capacity ≠ attention; the middle of long input is missed (put key info at start/end); summarization loses exact numbers/dates; accumulation wastes the window.
- **Common wrong answer:** "a 200K window means all details are equally available."
- **Diagnostic follow-up:** "Synthesis reliably cites the first and last chunks but misses the middle. Cause, and fix?"

### D5.2 — Fact extraction + trimming + position-aware input
- **Minimum acceptable:** keep a persistent "case facts" block outside summarized history; trim verbose tool results (PostToolUse) to relevant fields; key findings at top, action items at bottom.
- **Common wrong answer:** trusting summarization to preserve precise figures, or raising the summarization threshold to "fix" lost numbers.
- **Diagnostic follow-up:** "The agent garbles a discount mentioned 20 turns ago. What structure preserves it regardless of summarization?"

### D5.3 — Scratchpad files + structured state persistence
- **Minimum acceptable:** write key findings to a scratchpad during long investigations; delegate discovery to subagents (return a summary line, not 15 files); persist structured state (manifest) for crash recovery; constrain subagent context budgets.
- **Common wrong answer:** re-running discovery after context degrades instead of consulting a scratchpad/state file.
- **Diagnostic follow-up:** "A 3-hour investigation's context degraded. What should have been in place so you don't re-discover everything?"

### D5.4 — Confidence calibration + stratified sampling
- **Minimum acceptable:** field-level confidence calibrated against a labeled set; route low-confidence to humans; aggregate accuracy hides per-type/per-field rot → stratified random sampling by document type/field.
- **Common wrong answer:** trusting a 97% aggregate accuracy as proof the system is safe to automate.
- **Diagnostic follow-up:** "97% overall accuracy — why might that still be dangerous, and what measurement exposes it?"

### D5.5 — Provenance + conflicting data
- **Minimum acceptable:** preserve claim→source mappings (url, name, quote, date) through aggregation; on conflicting values keep BOTH with attribution (don't pick arbitrarily); include dates so temporal change isn't read as contradiction.
- **Common wrong answer:** picking the "more credible" number and footnoting the discrepancy, or dropping source/date.
- **Diagnostic follow-up:** "Two credible sources give 12% and 8% for the same metric. What does the agent output — and why not just choose one?"
