# CCA-F Exam Digest — Condensed Cram Sheet

**Last updated:** 2026-06-09
**Source:** Distilled from `daronyondem/claude-architect-exam-guide` v1.0.1 (26 May 2026, **CC BY 4.0 — attribution: Daron Yöndem**), cross-checked against this project's own web-researched citations (`courses/.../source/*_citations.md`) and the Anthropic docs.
**How to use:** This is the single-source crammer for the days before the exam. The guide's **11 knowledge areas** are mapped here onto the **5 official exam domains**. Study the *anti-patterns* hardest — the exam weights scenario + "what's wrong with this design?" questions above recall. Pair this with `GAPS.md` (your weak spots) and the 8-extension HTML course (mechanism-level depth).

> **KA→Domain map.** The community guide's 11 knowledge areas (KA1–KA11) don't line up 1:1 with Anthropic's 5 domains. The mapping below is the reconciliation.

---

## Domain 1 — Agentic Architecture & Orchestration · 27% (heaviest)
*Covers guide KA8 (agentic patterns), KA9 (customer-service workflows), agent-handoff parts of KA5.*

### Must-know
- **The five core patterns:** **prompt chaining** (fixed sequence) · **routing** (distinct input categories) · **orchestrator-workers** (coordinator picks + delegates to specialists) · **dynamic decomposition** (investigation where the next step only becomes clear after the current finding — debugging/root-cause; set step caps) · **parallel subagents** (independent workstreams).
- **Parallel subagents:** partition a large *uniform* task → spawn N → synthesize. **Elapsed time = max(subagent durations)**, not sum. Balance chunks by expected effort. Don't parallelize when task B needs task A's output.
- **Common phasing:** serial decomposition → parallel execution → serial synthesis.
- **Multi-agent context passing:** a subagent sees **only what the parent explicitly puts in its constructed prompt** — NOT the parent's prior turns, tool results, or memory. Pass structured summaries + source indexes, never raw 100K-token dumps.
- **When the coordinator should NOT delegate:** when the work is small and the coordinator already has the context — delegation costs a tool call + fresh context + separate invocation.
- **Escalation (customer service):** escalate when the user asks for a human, the issue needs authority the agent lacks, a policy exception / regulated approval / high-value transaction is involved, the agent can't make progress, or a tool reports an uncertain/unsafe state. **Do NOT use a simple "escalate after N failed tool calls" counter** — category and impact matter more than count.
- **Structured handoff payload:** `customer_id, issue_type, root_cause, relevant_records, amount, actions_taken, recommended_next_action` — NOT the full transcript.
- **Compliance / hard rules must be enforced in CODE, not the prompt.** Threshold checks live inside the tool, reading a server-controlled source — not a parameter the model passes. **Defense-in-depth:** prompt rules bias → tools enforce → audit logs detect.
- **Graceful degradation:** state what was verified, what couldn't complete, offer next steps. **Partial completion > fake success or a generic error.** Never claim a side effect happened if it didn't.

### Anti-patterns (high-yield)
- Using the full pipeline for a simple fact lookup.
- One-pass research that ignores gaps (findings should trigger targeted follow-up).
- Passing raw mega-outputs between agents instead of structured summaries.
- Over-prescribing subagents with brittle step-by-step instructions.
- Escalating with no useful handoff; dumping the transcript.
- Processing high-risk actions on prompt rules alone; retrying uncertain writes (→ duplicates).
- **Judging "8 tools in one turn" as a smell by count.** Parallel calls to *independent* tools is *good*; it's a smell only when calls are interdependent/need sequencing, or the orchestrator is doing worker grunt-work, or it's runaway. *(Your logged Module-1 gap.)*

---

## Domain 2 — Claude Code Configuration & Workflows · 20%
*Covers guide KA10 (Claude Code & Agent SDK). Deep treatment in the new C-E6 lesson + its citations file.*

### Must-know
- **Built-in tools:** Grep (text *inside* files) · Glob (filenames/paths) · Read · Edit/MultiEdit (targeted) · Write (full replace) · Bash (last resort) · Task/Agent (delegation). **Use Grep, not filename search, to find code references inside files.**
- **CLAUDE.md hierarchy** (all discovered files **concatenated**, broad→specific, local last; it's *context, not enforcement*): Managed policy (OS path, cannot be excluded) → User `~/.claude/CLAUDE.md` → Project `./CLAUDE.md` or `./.claude/CLAUDE.md` → Local `./CLAUDE.local.md` (gitignored). Ancestors load fully; subdirectory CLAUDE.md loads on demand. `claudeMdExcludes` skips other teams' ancestors (but not managed policy).
- **The four extension surfaces — pick by need:** **CLAUDE.md** = every session, soft guidance (project conventions) · **Rules** (`.claude/rules/`, scope via `paths:` frontmatter) = soft, topic-scoped · **Skills** = on-demand multi-step procedures · **Hooks** = lifecycle events, **HARD enforcement** (allow/deny, formatters, mandatory approvals). → *Automations = hooks; preferences = memory.* (Your logged Module-2 gap.)
- **Permissions:** rules evaluate **deny → ask → allow** (deny is absolute, can't be re-allowed). Bare tool name removes the tool from context; scoped pattern `Bash(rm *)` leaves it but blocks matching calls. **Settings override by precedence (Managed > CLI > Local > Project > User); permission RULES merge across scopes** — the classic trap.
- **Permission modes:** `default`, `acceptEdits`, `plan`, `auto` (research preview), `dontAsk`, `bypassPermissions`.
- **Plan mode** (`--permission-mode plan`) = read-only explore + propose before edits; for multi-file / architecture / breaking changes. **Plan mode ≠ Extended Thinking** — plan = workflow control (gate thinking→doing), extended thinking = reasoning quality; they combine.
- **Hooks:** ~30 lifecycle events; **only exit code 2 blocks** (exit 1 is non-blocking, even though Unix-conventional). PreToolUse can return `permissionDecision: allow|deny|ask`. Stop hook can gate "turn can't end until the check passes."
- **Sessions** = stored transcripts (not filesystem state): `--continue` (most recent), `--resume`/`-r` (specific), `--session-id <UUID>`, `--fork-session` (branch). Use git branches/worktrees for *file* isolation. Don't resume one session in two terminals.
- **Headless / Agent SDK:** `claude -p "..." --allowedTools "..."`; `--output-format json|stream-json` (`json` includes `total_cost_usd`); `--bare` skips auto-discovery for reproducible CI. CI auth via `claude setup-token` → `CLAUDE_CODE_OAUTH_TOKEN`.
- **Fresh review context:** review high-stakes code in a *new* session / dedicated subagent / CI — never with the same context that wrote it.

### Anti-patterns
- Filename search to find in-file references (use Grep). Bash when a structured tool exists.
- Workflow-specific checklists in global memory. Expecting CLAUDE.md to *enforce* anything (it's context). Reviewing code with the same session that wrote it. Treating exit 1 as a blocking hook.

---

## Domain 3 — Prompt Engineering & Structured Output · 20%
*Covers guide KA1 (API/output control), KA4 (extraction/validation), KA6 (system-prompt engineering), KA11 (eval/batch). Deep treatment in C-E5.*

### Must-know
- **Messages API is STATELESS** — no memory between calls; full history must be re-sent each request. `session_id` alone is NOT memory. System prompt goes in the top-level `system` param, not a message role.
- **`tool_choice`:** `auto` = optional · `any` = required from the set · `{"type":"tool","name":"X"}` = that tool · `none` = disabled. **Only `any` or a named tool *guarantees* a tool call** (the `auto` trap).
- **Structured Outputs (constrained decoding) = the source-level fix for malformed JSON** — `output_config.format` (JSON schema) or strict tool use makes invalid output impossible. **Retry/dead-letter is the fallback, not the primary fix.** (Your logged Module-3 gap.) First-call grammar compile adds latency; schemas cache (~24h).
- **Schema rules:** required vs optional vs **nullable** vs empty-array vs an `other_detail` escape hatch all mean different things. `additionalProperties:false`. NOT supported by Structured Outputs: recursive schemas, external `$ref`, numeric/string length constraints.
- **Reduce fabrication:** allow `null`, mark absent fields optional, give few-shot **edge-case** examples (missing data, ambiguity, informal units), preserve informal values verbatim, add source grounding (`source_location`, `source_quote`). **Making an absent source field *required* creates hallucination pressure.**
- **Valid JSON ≠ correct data.** Schema catches syntax; **semantic validation** catches logic (line-item sums, date ranges, ID formats). **Correction loop** (resend doc + prior extraction + exact errors) beats blind retries.
- **System prompt:** attention to it *weakens* as the conversation grows (not dropped — competed for); reinforce key rules at phase breakpoints. Use XML-tagged sections for salience. **Principles for judgment** ("adapt depth to expertise"); **conditionals for safety bright-lines** ("if emergency, call 911"). **Few-shot > prose** for teaching distinctions.
- **Clarifying questions:** ask when interpretations diverge materially, the action is irreversible/costly, goals conflict, or info is truly missing — **one at a time**, prefer disambiguating *which entity* over averaging conflicting preferences.
- **Batch API:** async, cost-reduced, `custom_id` per request; results may be out of order — join by `custom_id`; resubmit failures with refined prompts. Long docs → staged extraction.
- **Confidence** must be calibrated per segment (doc type, field, source) against a labeled set; aggregate accuracy hides per-field rot.

### Anti-patterns
- `session_id` as memory; assuming Claude remembers prior calls. Forcing text JSON via prompt when tool use is available. "IMPORTANT/NEVER" as a *reliability* mechanism (helps salience, not guarantee). Endless conditionals bloating the prompt. Strict enums with no escape hatch in evolving domains. Relying only on aggregate accuracy. One extraction call for a long scattered document.

---

## Domain 4 — Tool Design & MCP Integration · 18%
*Covers guide KA2 (tool interfaces), KA3 (error handling), KA7 (MCP).*

### Must-know
- **MCP's three primitives:** **Tools** = model-controlled *actions* (search/update/create/send) · **Resources** = application-controlled *passive context* (schemas, docs, catalogs — read like context, no tool call to *use*) · **Prompts** = user/app-controlled reusable *workflows* (surface as slash commands). *Resources for "what is true & stable," tools for "what actions can be taken."*
- **MCP does NOT auto-solve** auth, rate-limiting, retries, caching, authorization, or performance — you build those.
- **Tool annotations** (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) are **untrusted UI hints, NOT security boundaries**. Security belongs in code.
- **Two MCP error tiers:** **protocol errors** (JSON-RPC, *pre-execution* — unknown tool, malformed JSON, missing param) vs **tool execution errors** (`isError:true` — the tool ran but failed: 404/503/business-rule/permission/rate-limit).
- **Error handling by category:** transient infra → retry *inside the tool* (reads); validation → return structured details for the *model* to fix; business-rule/permission → non-retryable; **uncertain write state → report uncertainty, do NOT auto-retry (duplicates).** Return structured errors (`category`, `retryable`, `message`), never throw exceptions for expected business errors. **Recoverable-vs-escalate is an architectural decision encoded in the error surface — not "Claude just retries."** (Your logged Module-4 gap.)
- **Tool design:** descriptions state what / when-to-use / when-NOT / inputs / outputs / limits. Enums for stable closed sets; lookup-then-act for ambiguous entities; prefer stable IDs. **Split tools when params have interdependent constraints.** Results: structured, compact, include downstream IDs. **Empty array ≠ error.** Pagination: first page + `total_count` + cursor.
- **Destructive ops:** preview-then-execute with a **one-time confirmation token bound to the previewed payload** — NOT a `dry_run` flag the model can skip. Re-verify authority server-side on every call.
- **Large tool sets:** progressive availability — a discovery tool returns a shortlist, then dynamic registration.

### Anti-patterns
- Using a tool where a resource fits (catalogs/schemas are usually resources). Assuming MCP handles auth/retries. Trusting self-reported annotations as security. Minimal descriptions ("Analyzes code"). Format hints in parameter *names*. Everything free-text string. Returning only prose (no IDs). Composite `do_thing(action, params)` god-tools. Returning empty data for a backend failure.

---

## Domain 5 — Context Management & Reliability · 15%
*Covers guide KA5 (conversation context), KA11 (caching/batch/cost). Deep treatment in C-E2 + C-E4.*

### Must-know
- **CALM = Compress, Anchor, Layer, Monitor.** The **L is Layer** (system vs history vs injected context), not "Limit." (Your logged Module-5 gap.)
- **Context capacity ≠ attention.** A 200K window does NOT make all details equally salient.
- **Strategies by what must survive:** **sliding window** (drop old; aggressive on RAG results) · **progressive summarization** (replace old blocks with a structured summary — Decisions/Preferences/Open-questions/Facts — keep recent turns verbatim) · **persistent reference section** (allergies, counts, definitions kept stable) · **structured state object** (canonical JSON updated on change — more reliable than inferring from a long transcript) · **retrieval/fact stores** (for exact p-values, quotes, thresholds — summaries lose precision) · **tool-result compression** (extract relevant fields, drop the rest).
- **Returning users:** open with a structured summary + fetch *fresh* state — never resume with stale embedded tool results.
- **External updates mid-conversation:** inject fresh state into the system prompt / a context block — NOT as an unsolicited assistant message.
- **Prompt caching:** `cache_control` goes **after the stable prefix, before the variable per-turn content**. Check `cache_read_input_tokens` / `cache_creation_input_tokens` in `usage`. ~5-min TTL (refreshes on hit).
- **Reliability patterns:** retry with backoff, fallback models, circuit breakers, graceful degradation.

### Anti-patterns
- Confusing capacity with attention. Summarizing *exact facts* into vague prose. Keeping every RAG result forever. Resuming old transcripts with stale tool results. Placing `cache_control` before content that changes every turn.

---

## ⚡ Rapid-fire memorization (last-hour scan)

- **`tool_choice`:** `auto`=optional, `any`=required-from-set, named=that tool, `none`=off. Only `any`/named **guarantees** a call.
- **Messages API = stateless.** `session_id` ≠ memory. System prompt = top-level `system` param.
- **MCP primitives:** Tools=actions, Resources=passive context, Prompts=workflows. Annotations = untrusted hints.
- **MCP errors:** protocol (JSON-RPC, pre-exec) vs execution (`isError:true`, ran-but-failed).
- **Never retry uncertain writes** (duplicates). Structured errors > exceptions.
- **5 agentic patterns:** chaining / routing / orchestrator-workers / dynamic-decomposition / parallel-subagents. Parallel elapsed = **max**, not sum.
- **Subagent sees only the constructed prompt** — not parent turns/tools/memory.
- **CLAUDE.md = concatenated context, not enforcement.** Managed > User > Project > Local. **Hooks = hard enforcement; only exit 2 blocks.**
- **Permissions evaluate deny→ask→allow.** Settings override; permission rules **merge**.
- **Sessions:** `--continue` (recent), `--resume` (specific), `--fork-session` (branch), `--session-id`. Sessions = transcripts; git = file isolation.
- **Structured Outputs** = fix malformed JSON at the source; retry is the fallback.
- **Schema:** allow `null` + optional + escape hatch to kill fabrication. Valid JSON ≠ correct data → semantic validation.
- **System prompt** attention weakens over a long convo; reinforce at phase changes. Principles for judgment, conditionals for safety. Few-shot > prose.
- **CALM** = Compress, Anchor, **Layer**, Monitor. `cache_control` after the stable prefix.
- **Escalation:** category & impact, not a fail-counter. Structured handoff, not a transcript dump.
- **Compliance enforced in code**, read from a server-controlled source; preview-then-execute with a bound one-time token.
- **Exam scoring:** scaled (720/1000) — scenario + anti-pattern questions dominate. **Study judgment, not coverage.**

---

## Provenance & gaps
- Primary source: `daronyondem/claude-architect-exam-guide` (CC BY 4.0). Corroborated against this project's web-researched citation files and Anthropic docs (`code.claude.com/docs`, `platform.claude.com`).
- The community guide does **not** publish per-domain weights — the 27/20/20/18/15 split here comes from `PREP-MATERIAL-INDEX.md` (Anthropic blueprint).
- Volatile facts (model IDs, hook roster, permission-mode names, MCP scope renames) carry `[VERIFY]` flags in the lesson citation files — re-check against live docs before exam day.
- Your personal weak spots are in `GAPS.md`; every one of them is reinforced inline above.
