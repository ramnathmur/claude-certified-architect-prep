# CCA-F Trap Sheet — Plan & Full Content Draft (v1)

**Purpose:** checkpoint for the "how will this be tested, and where are the traps" cheat sheet Ram asked for on 2026-08-18. This file is the whole content draft, not a summary of it — every entry below carries the words that will land on the page. Approving it approves the words; generation is rendering + browser verification.
**Deliverable:** `Outputs/CCA-F_Trap-Sheet_v1.html` (name is changeable — "Cheat-Sheet" was avoided because `CCA-F_Professors-Cheat-Sheet_v1/v2.html` and `CCA-Guide2_CheatSheet_*` already exist and are a different cut).
**Date:** 2026-08-18 · **Exam:** Claude Certified Architect – Foundations (CCAR-F) · real sitting recorded as **today** in `prep with quiz/SESSION-STATE.md`.

---

## 1. What this is, and what it is not

Every earlier artifact in `Outputs/` answers *what is true* (Masterclass explains, Companion locates + drills, Atlas maps the guide's 288 bullets to 127 cards, Bible/Study-Guide/Professors-Cheat-Sheet restate the domains). This sheet answers a different question for each concept: **how would a setter turn this into a 4-option item, and which wrong option is built to catch a candidate who half-knows it.** It is the setter's-eye view — the same view the project's Professor's Notes take, applied to every concept at once.

Two lenses per entry, nothing else:

- **How it gets asked** — the situation-signal the stem will carry (the telemetry, the quoted message, the config token), the *form* of the ask, and the answer direction. Where the exam could come at the point from the mirror side, the reverse angle is listed too — both-directions testing is what closed `tool_choice` any-vs-auto for Ram, so it is built in everywhere.
- **Trap points** — the distractor the setter reaches for, one clause on why it fails, and the mold it belongs to (§4 below), so the same trap is recognisable under a new skin.

## 2. Sources (and what was deliberately left out)

Read in full for this draft: `CCA-Prep_Domain-1..5_v2.md` (73 sections), `CCA-Prep_Key-Distinctions_v1.md` (29), `CCA-Prep_Exam-Mechanics_v2.md`, `CURRENT-DOCS-DELTA_v1.md` (E1–E7, D1–D9), `PRACTICE-TEST-STEMS_v1.md` §3 (style profile + 7 distractor molds), `QUESTION-ARCHETYPE-BANLIST.md` (the shapes already over-used in the mocks — useful here as "shapes the setter has, and the re-frames a fresh paper would use"), the official guide text for one spot-check (§3.5 wording). Personal-miss badges (⚑) come from `SESSION-STATE.md`, `CCA-Prep_Mistake-Patterns_v1.html` headings and the memory file — **not** from mining the 630 KB `EXAM-LOG.md` (see open decision Q2).

Not sourced: mock-exam stems (dedup ledger content), `academy/` (stale), the community sites (depth only, and the corpus already holds every point they make).

## 3. Entry contract

Every corpus section becomes one entry (73 entries; multi-concept sections carry concept-tagged bullets — e.g. §2.5 splits into tool-count / least-privilege / cross-role / `tool_choice`). Each entry has:

| Field | Rule |
|---|---|
| **Rule** | One flat sentence — enough that the sheet stands without the corpus. |
| **How it gets asked** | 2–5 bullets. Each: `[FORM]` signal → answer. Forms use the practice-test distribution: **FIX** (best fix/approach, ~67% of items), **HOW** (how should you…, ~12%), **CAUSE** (root cause, ~9%), **WHICH** (which mode/situation/pattern, ~9%), **WHERE** (placement, ~3%), plus **REVERSE** = the mirror-image ask. |
| **Trap points** | 3–6 bullets. Each: ✗ distractor — why it fails `[MOLD]`. |
| **⚑ badge** | Only where Ram has missed the point in a scored paper; carries the exam numbers. Removable in one pass if Q2 = no. |
| **§ tag** | Small muted section number for jumping back to the corpus file (his own SESSION-STATE recommendations are §-keyed). Removable if he'd rather not see them. |
| **Exam≠docs flag** | Where `CURRENT-DOCS-DELTA` is [CONFLICT-RISK]: the posture is stated (answer per the guide). |

Prose rule (per the standing hard ban): a checkable fact gets one flat sentence; no manufactured misconception to negate; say each idea once.

## 4. The setter's toolkit — page 1 of the sheet

**How a stem is built (from 76 real practice-test items + 12 official samples):** 2–5 sentences of situation, always with operational evidence — a percentage ("45% of the time", "55% first-contact resolution vs 80% target"), a count ("14 files", "400+ lines", "12+ tool calls", "~75K tokens"), a quoted user line ("I love jazz", "I want a manager") or an inline token (`get_customer`, `context: fork`, `${GITHUB_TOKEN}`). It often ends by naming a constraint ("without affecting teammates", "without adding human oversight", "stakeholders rejected filtering findings"). Then one ask. No negative stems, no "why", no true/false in the samples. **v1.0 of the guide adds multiple-response items — each item states how many to select — and scoring is all-or-nothing** (Ram's four multi-response misses on Exam 14 were all majority-right; on these, every tick must be independently defensible, never a "probably").

**The ten distractor molds** (7 from the practice-test explanations, 3 from this project's own miss record):

| # | Mold | What it looks like | Tell |
|---|---|---|---|
| 1 | **SYMPTOM** | Fix downstream (post-process, dedupe after, regenerate, filter, remind) instead of at the source | "directly addresses the root cause" is the setter's justification for the key |
| 2 | **FAKE** | A flag/param/behaviour that does not exist: `--batch`, `CLAUDE_HEADLESS=true`, `override: true`, `session_id`, "Claude caches CLAUDE.md" | Plausible name, never in the docs |
| 3 | **PROMPT-NOT-CODE** | Instruction or few-shot offered where the requirement is a *guarantee* | Words like "must always", "never without", "15% wrong account" → hook / gate / token / schema / `tool_choice` |
| 4 | **OVERBUILD** | Classifier, routing layer, extra model, vector DB, intermediate agent, shared-state layer | A lighter fix (description, example, partition, scope) exists |
| 5 | **BIGGER-CONTEXT** | Larger model / wider window / raise the threshold | Delays the same problem; attention quality unchanged |
| 6 | **SILENT** | Swallow errors, return success with an error inside, hidden defaults, consensus voting to drop findings | Destroys the signal the system needs |
| 7 | **BURDEN** | Push the work to humans or upstream ("developers must split PRs", "customer must fill an intake form") | The system, not the person, should change |
| 8 | **DISCARD** ⚑ | Throw away a working mechanism (hook, session, tool) when a narrow adjustment fixes the side-effect | Exam 14 Q19/Q54 pattern |
| 9 | **OVERSPEC** ⚑ | Force a *specific* mechanism when the requirement only needs *a* mechanism — `tool_choice: tool` where `any`/`auto` is right; forced on every turn | Exam 19 Q23, Exam 20 Q48 |
| 10 | **EXAM≠DOCS** | Current-docs truth offered against the guide's framing | Answer per the guide: `allowed-tools` restricts; `Task` not `Agent`; import depth 5; two MCP scopes; `tool_choice` has three tested values |

Plus the corpus's own two look-alike families that recur everywhere: **LOOKALIKE** (a Key-Distinction pair — 0 results vs timeout, Grep vs Glob, `any` vs forced) and **REVERSE** (the right pattern applied in the wrong direction — plan mode for a one-line fix, dynamic decomposition for a fixed template, composite tool where bundling suffices, or vice versa).

**The twelve tie-breakers** (Exam-Mechanics heuristics, unchanged): fix the root cause · proportionate first response · programmatic enforcement for critical sequences · least privilege · deterministic over probabilistic · structured error > generic failure · parallel + shared context > sequential · coordinator is the hub · independence for review · match API to latency · coverage gaps trace upstream · attention dilution → split passes.

**When two options both "work":** take the one that fixes the signal at its source with the least new machinery — unless the stem asks for a guarantee, in which case take code (hook, gate, token, schema, `tool_choice`) over prompt.

**Out-of-scope = automatic distractor:** fine-tuning, auth/billing, MCP hosting/transport, model internals, RLHF, embeddings implementation, computer use, vision, streaming/SSE, rate limits, OAuth, cloud configs, benchmarks, prompt-caching internals, tokenizer details. An option that leans on any of these is not the key.

---

## 5. Content draft — Domain 1 · Agentic Architecture & Orchestration (27%)

### 1.1 · The agentic loop runs on `stop_reason`
**Rule.** After each call the orchestrator reads `stop_reason`: `tool_use` → run the tool, append a `tool_result` (matched by `tool_use_id`), call again; `end_turn` → stop and return; `max_tokens` → handle (may continue); `stop_sequence` → app-defined.
**How it gets asked**
- [CAUSE] Loop never terminates, or stops mid-task; the code checks for a phrase like "I'm done", or a fixed iteration cap → termination is keyed on text/count instead of `stop_reason`.
- [WHICH] "What determines when the loop should stop?" → `stop_reason == "end_turn"`.
- [HOW] Sequence after a `tool_use` response → execute the tool, append `tool_result`, call again with the full history.
- [REVERSE] `stop_reason: max_tokens` arrives → not "done"; continue/handle, don't return a truncated answer as final.
**Trap points**
- ✗ Parse the assistant text for a completion signal — natural language is not a control signal `[FAKE mechanism]`.
- ✗ Terminate after N iterations — a cap is a safety net, not the exit condition `[SYMPTOM]`.
- ✗ Treat `max_tokens` as `end_turn` `[LOOKALIKE]`.
- ✗ Forget to append the `tool_result` — the model re-requests the same tool `[SILENT]`.
- ✗ An option that says "there are exactly four `stop_reason` values" — current docs add `pause_turn`, `refusal`, `model_context_window_exceeded`; the exam only turns on `tool_use` vs `end_turn`, so don't let a value-count decide `[EXAM≠DOCS, safe]`.

### 1.2 · Hub-and-spoke, the `Task` tool, and context isolation
**Rule.** One coordinator routes everything; subagents never talk to each other; each `Task` call is an isolated context that sees only what its prompt contains; several `Task` calls in one response run in parallel.
**How it gets asked**
- [CAUSE] Synthesis agent "doesn't know" what web-search found → the coordinator never passed those results into its prompt; subagents inherit nothing.
- [WHICH] Proposal: let subagents message each other to save coordinator hops → reject; the hub gives visibility, uniform error handling, information control.
- [CAUSE] Coordinator does everything itself, never delegates → `"Task"` missing from its `allowedTools` (see 1.3).
- [HOW] Make three subagents run concurrently → emit all three `Task` calls in a single response (see 1.15).
**Trap points**
- ✗ Direct inter-agent messaging "for efficiency" — breaks the hub, coordinator goes blind `[REVERSE]`.
- ✗ Assume shared memory / inherited history between coordinator and subagents `[FAKE]`.
- ✗ Fix non-delegation with prompt wording — a prompt cannot grant a tool the config withholds `[PROMPT-NOT-CODE]`.
- ✗ Name game: current SDK calls the tool `Agent` (renamed in Claude Code v2.1.63); the guide says `Task`. Never let the name decide; if a stem names it, expect `Task` `[EXAM≠DOCS, conflict-risk]`.

### 1.3 · `AgentDefinition` — description, system prompt, tool restrictions
**Rule.** A subagent type is its `description`, `system_prompt` and `allowed_tools`; a coordinator's `allowed_tools` must include `"Task"` or it cannot spawn anything.
**How it gets asked**
- [CAUSE/FIX] "Coordinator attempts everything itself" → check `Task` in `allowedTools`; not the prompt, not the descriptions.
- [WHICH] Which lever enforces least privilege per subagent type → `allowed_tools`; which tells orchestration what the type is for → `description`.
- [REVERSE] "Give every subagent the full tool set for flexibility" → wrong; restriction *is* the separation-of-responsibilities mechanism.
**Trap points**
- ✗ Rewrite the coordinator prompt to "delegate more" `[PROMPT-NOT-CODE]`.
- ✗ Add subagent descriptions to the coordinator's system prompt — descriptions don't enable spawning `[FAKE mechanism]`.
- ✗ Full tool catalogue everywhere `[REVERSE of least privilege]`.
- ✗ Conflate `allowed_tools` (AgentDefinition, SDK) with `allowed-tools` (SKILL.md frontmatter, Claude Code) — same idea, different object `[LOOKALIKE]`.

### 1.4 · Coordinator prompts: goals + quality criteria, not procedures
**Rule.** The coordinator prompt states the research goal and what "good" looks like; a step-by-step script is brittle and stops subagents adapting.
**How it gets asked**
- [FIX] Research output is shallow and checklist-like → rewrite the prompt to goals + quality criteria (≥3 sources per claim, cover production/distribution/composition).
- [WHICH] Which prompt style lets subagents adapt as findings emerge → goal-oriented.
- [REVERSE] A review that must follow the same template every run → that is 1.7's fixed pipeline, not a reason to script the coordinator's *research* prompt.
**Trap points**
- ✗ Add more detailed steps — deepens the rigidity that caused it `[SYMPTOM]`.
- ✗ Add more subagents — more agents running a bad script `[OVERBUILD]`.
- ✗ Confuse goal-oriented prompting with dynamic decomposition (1.7) — same principle, different level `[LOOKALIKE]`.

### 1.5 · Structured context passing & attribution
**Rule.** Pass findings between agents as structured data with content and metadata (source URL, document, page, date) in separate fields; include complete upstream findings in the next agent's prompt; when sources conflict keep both values with attribution.
**How it gets asked**
- [CAUSE] Final report has claims with wrong/missing citations → content and metadata travelled as merged free text; attribution died in aggregation.
- [HOW] Two credible sources disagree (40% vs 12%) — what does the analysis agent do → complete the analysis with both values, annotate the conflict, coordinator decides (5.10).
- [FIX] Synthesis can't cite → structured claim→source mappings required from every subagent and preserved downstream (5.11).
**Trap points**
- ✗ "Remember to cite sources" instruction — it can't cite metadata it never received `[PROMPT-NOT-CODE]`.
- ✗ Re-search the web at the end to find sources — duplicate work, wrong attributions `[SYMPTOM]`.
- ✗ Pick the more credible number by heuristic `[SILENT]`.
- ✗ A bibliography at the end of the report — claims no longer traceable individually (5.11) `[SYMPTOM]`.

### 1.6 · Task decomposition & partitioning
**Rule.** When every subagent succeeds and the answer still covers the wrong ground, the coordinator's decomposition was too narrow; the coordinator must partition the space *before* delegating.
**How it gets asked**
- [CAUSE] "AI's impact on creative industries" returns only visual art; all subagents ran correctly → decomposition too narrow; fix the coordinator prompt.
- [FIX] Two agents research the same subtopics → partition before delegating.
- [WHERE] Where does the fix live → coordinator prompt, not the subagents.
**Trap points**
- ✗ Blame web-search query quality / synthesis gap detection / document filters `[wrong layer]`.
- ✗ Deduplicate after the fact `[SYMPTOM]`.
- ✗ Add more subagents to widen coverage `[OVERBUILD]`.

### 1.7 · Fixed pipeline vs dynamic adaptive decomposition; multi-pass review
**Rule.** Predictable structure → fixed sequential pipeline (prompt chaining); open-ended investigation → adaptive decomposition (map → prioritise → adapt as dependencies surface); a 10+ file PR → per-file passes plus a separate integration pass.
**How it gets asked**
- [WHICH] "Add comprehensive tests to a legacy codebase" → dynamic adaptive; first step = map structure with Glob/Grep.
- [WHICH] "A review that always follows the same template" → fixed pipeline / chaining.
- [FIX] 14-file PR review is deep on some files, shallow on others, contradicts itself → per-file passes + integration pass.
- [REVERSE] Predictable extraction pipeline offered "adaptive planning" → unnecessary complexity.
**Trap points**
- ✗ Fixed script for the open-ended task — can't react to discoveries `[REVERSE]`.
- ✗ Dynamic decomposition for a fixed template `[REVERSE / OVERBUILD]`.
- ✗ One giant single-pass prompt `[attention dilution]`.
- ✗ Bigger model / larger context window for the 14-file review `[BIGGER-CONTEXT]` (KD 17).
- ✗ "Require developers to split large PRs" `[BURDEN]`.

### 1.8 · Coordinator iterative refinement loop
**Rule.** The coordinator evaluates the synthesis for gaps, re-delegates *targeted* queries to search/analysis, re-invokes synthesis, and stops when its quality criteria are met — the coordinator owns gap evaluation and termination.
**How it gets asked**
- [HOW] Synthesis has coverage gaps and the sources are still reachable → refinement loop.
- [WHICH] Who decides "sufficient" → the coordinator, against criteria from 1.4.
- [LOOKALIKE] Gap is *unrecoverable* (a source is down) → coverage annotation (1.10), not another loop.
**Trap points**
- ✗ Let the synthesis agent search the web itself `[least privilege broken]`.
- ✗ Ship with "further research needed" while re-delegation is available `[SILENT-ish]`.
- ✗ Loop with no sufficiency criterion `[no termination]`.
- ✗ Annotate a recoverable gap instead of closing it `[REVERSE of 1.10]`.

### 1.9 · Error propagation in multi-agent systems
**Rule.** A failing subagent returns structured error context — failure type, what was attempted, partial results, alternatives; transient errors are retried locally, permanent ones are not retried, "0 results" is a valid finding, and one failure never kills the workflow.
**How it gets asked**
- [CAUSE] Coordinator can't decide retry vs skip vs continue → it received a generic "search unavailable".
- [WHICH] Patent DB timeout vs "0 results" from industry reports → different responses (retry-decision vs accept as finding).
- [WHERE] Where to retry a timeout with backoff → inside the subagent/tool, before surfacing.
- [HOW] One subagent fails → continue with partial results + context, never terminate everything.
**Trap points**
- ✗ Generic failure status `[SILENT]`.
- ✗ Treat empty results as an error and retry `[LOOKALIKE]` (KD 9).
- ✗ Retry a syntax/permission error `[wrong category]`.
- ✗ Catch and return success `[SILENT]`.
- ✗ Escalate every transient to the coordinator `[wrong level]`.

### 1.10 · Coverage annotations (graceful degradation)
**Rule.** With incomplete inputs, synthesise from what arrived, mark which conclusions are well-supported and where the gaps are, and propagate the uncertainty upward.
**How it gets asked**
- [HOW] Web search returned 3 of 5 source categories → structured output with coverage annotations.
- [LOOKALIKE] If the missing categories can still be fetched → 1.8 loop first.
**Trap points**
- ✗ Return an error because input is incomplete `[blocks pipeline]`.
- ✗ Proceed without noting gaps `[SILENT]`.
- ✗ Block and ask the coordinator about every gap (4.19) `[over-asking]`.

### 1.11 · Least privilege for subagent tools
**Rule.** Each subagent gets only its scope's tools; a high-frequency simple need gets a narrowly scoped cross-role tool while complex cases still route through the coordinator; a generic tool that gets misused is replaced by a constrained alternative.
**How it gets asked**
- [FIX] Synthesis agent needs 85% simple fact checks, 15% complex → scoped `verify_fact`; complex via coordinator.
- [FIX] Document-analysis agent with `fetch_url` starts web-searching → replace with `load_document` that validates document URLs.
- [REVERSE] "Route every fact check through the coordinator" → correct scoping, wrong cost; the round-trip overhead is what the scoped tool exists to remove.
**Trap points**
- ✗ Full `web_search` to the synthesis agent `[scope creep]`.
- ✗ Batch all verification to the end `[blocking]`.
- ✗ Prompt "don't use `fetch_url` for search" `[PROMPT-NOT-CODE]`.
- ✗ Block known search-engine domains `[fragile]`.

### 1.12 · When to escalate to a human
**Rule.** Escalate on a policy gap, an explicit request, inability to progress, or high-stakes ambiguity — and not otherwise.
**How it gets asked**
- [WHICH] Competitor price-match request; policy covers own-site drops only → escalate (policy interpretation is not the agent's to invent).
- [WHICH] "Which situation most justifies escalation?" → the policy-silent one, not the angry one.
- [REVERSE] Policy covers it, ambiguity is resolvable by asking (5.8) → resolve, don't escalate.
**Trap points**
- ✗ Apply own-site rules to competitors `[invented policy]`.
- ✗ Refuse citing a rule that isn't written `[invented policy]`.
- ✗ Escalate a multiple-match ambiguity instead of asking for another identifier `[REVERSE]`.
- ✗ Escalate on sentiment `[unreliable proxy]` (5.8).

### 1.13 · Structured handoff to a human
**Rule.** The human has no transcript, so the escalation carries a self-contained summary — customer ID, root cause, amount, actions taken, recommended action, escalation reason.
**How it gets asked**
- [CAUSE/FIX] Human agents keep re-asking customers for what the AI already collected → escalation passed a flag or free-text note; send the structured handoff.
- [WHICH] What must the payload include → the fields above.
**Trap points**
- ✗ Give humans the raw transcript `[no access by design; re-reading everything]`.
- ✗ Have the human re-run the agent's tools `[duplicate work]`.
- ✗ Escalate earlier so less context accumulates `[degrades autonomy, fixes nothing]`.

### 1.14 · Critical sequencing → programmatic preconditions
**Rule.** When an order must hold (identity before action), enforce it in code — a gate or `PreToolUse` hook — because prompt compliance is probabilistic.
**How it gets asked**
- [FIX] Agent skips `get_customer`, calls `lookup_order` with the customer-supplied number; wrong account 15% → block `lookup_order` until `get_customer` returns a verified identifier.
- [WHICH] Mechanism → precondition / `PreToolUse` (2.7).
- [REVERSE] Ordinary, non-critical guidance → the prompt is fine; hooks for everything is over-engineering.
**Trap points**
- ✗ "Always call `get_customer` first" in the system prompt `[PROMPT-NOT-CODE]`.
- ✗ Few-shot examples of the right order `[PROMPT-NOT-CODE]`.
- ✗ A confirmation prompt at the orchestration layer `[OVERBUILD]`.

### 1.15 · Parallel execution
**Rule.** Several `Task` calls emitted in one coordinator response run in parallel; a multi-issue request is decomposed and investigated in parallel with shared context, then answered once.
**How it gets asked**
- [HOW] Billing dispute: charged twice + discount missing + cancel → three parallel investigations sharing the customer context, one synthesis.
- [CAUSE] "My parallel subagents ran one after another" → the calls were issued across separate turns.
**Trap points**
- ✗ Sequential investigation `[tool-call bloat, redundant fetching]`.
- ✗ Parallel *without* shared context `[redundant fetching]`.
- ✗ A shared-state mechanism between subagents `[OVERBUILD]`.

### 1.16 · Sessions: `--resume`, `fork_session`, fresh + summary
**Rule.** `--resume <name>` when prior context is still valid (and tell it which files changed); `fork_session` to compare approaches from a shared, expensive baseline; a new session with an injected structured summary when tool results are stale.
**How it gets asked**
- [HOW] Yesterday's codebase analysis; three files refactored today → resume and name the three files for targeted re-analysis.
- [WHICH] Evaluate two refactoring strategies from one completed analysis → `fork_session`.
- [WHICH] Files changed massively / long gap / degraded context → fresh session + summary (conclusions without stale evidence).
- [WHICH] Named-flag recall: `--resume` / `-r`, `--continue` / `-c`, `--fork-session`.
**Trap points**
- ✗ Resume as-is with stale results `[stale evidence]`.
- ✗ Always start over `[waste]`.
- ✗ Run both strategies in one session `[second is biased by the first]`.
- ✗ Two brand-new sessions `[baseline redone twice]`.
- ✗ Discard a resumable session when a targeted "these files changed" note would do ⚑ `[DISCARD]` (Exam 14 Q19/Q54 pattern).

### 1.17 · Independent review instances
**Rule.** A second instance with no access to the generator's reasoning catches what the generator rationalised away; a second pass in the same conversation is not independent.
**How it gets asked**
- [FIX] Generated code passes its own edge-case check; bugs only found in PR review → independent reviewer instance.
- [WHICH] "Extended thinking on the generator?" → no, same anchored instance.
**Trap points**
- ✗ "Review your own work carefully" `[same context]`.
- ✗ Extended thinking `[more of the same reasoning]`.
- ✗ Second pass in the same conversation `[not independent]`.
- ✗ Report only findings seen in ≥2 runs `[SILENT — suppresses signal]`.

### 1.18 · Named patterns
**Rule.** The exam may ask you to name the pattern from its description; the list: hub-and-spoke · agentic loop · parallel execution · context isolation · evaluator-optimizer · structured error propagation · coverage annotation · least-privilege tooling · goal-oriented delegation · content/metadata separation · prompt chaining · dynamic adaptive decomposition · iterative refinement loop · structured handoff · session forking · fresh-plus-summary.
**How it gets asked** — [WHICH] a one-paragraph description → the name; or the reverse.
**Trap points** — ✗ evaluator-optimizer confused with prompt chaining (critic stage vs sequential stages); ✗ context isolation confused with least privilege (what an agent *sees* vs what it *can call*).

---

## 6. Content draft — Domain 2 · Tool Design & MCP Integration (18%)

### 2.1 · Tool-use mechanics and the `tool_choice` values
**Rule.** A tool is `name` + `description` + `input_schema`; Claude answers with `stop_reason: tool_use` and a `tool_use` block (`id`, `name`, `input`); the app runs it and appends a `tool_result` keyed by that `id`; `tool_choice` is `auto` (default), `any`, or `{"type":"tool","name":…}`.
**How it gets asked**
- [HOW] Order the five steps of a tool call.
- [WHICH] Which field links a result to its call → the `tool_use` `id`.
- [WHICH] What does `auto` guarantee → nothing; the model may answer in text.
**Trap points**
- ✗ Match results by tool name `[wrong key]`.
- ✗ Expect Claude to execute the tool `[FAKE]`.
- ✗ `{"type":"none"}` as an answer — it now exists in the docs, but the guide's task 2.3 names only auto/any/forced; it will not be the key `[EXAM≠DOCS, safe]`.

### 2.2 · Tool description design — the primary selection lever
**Rule.** Selection runs on descriptions: purpose, accepted inputs with examples, when to use, when not; misrouting → fix descriptions first; near-identical names → rename and rewrite; a keyword-binding phrase in the system prompt can override good descriptions.
**How it gets asked**
- [FIX] "analyze the uploaded quarterly report" routed to `analyze_content` (web) 45% instead of `analyze_document` → rename (`extract_web_results`) + rewrite for a distinct purpose.
- [FIX] `get_customer` / `lookup_order` with 1-line descriptions and similar ID formats → expand both with formats, examples, edge cases, boundaries.
- [WHICH] Selection still wrong after good descriptions → check the system prompt for keyword-bound wording.
- [LOOKALIKE] Description vs few-shot ⚑ — the description is the first lever for *tool selection*; few-shot (4.1) is for the residual ambiguous *requests* after descriptions are right (Exam 19 Q53).
**Trap points**
- ✗ Pre-routing classifier `[OVERBUILD]`.
- ✗ Merge into one `lookup_entity` `[loses precision]`.
- ✗ Few-shot before descriptions are fixed ⚑ `[wrong lever first]`.
- ✗ "Always prefer X" system-prompt rule `[blunt, keyword-sensitive]`.

### 2.3 · Structured tool errors — four categories, business errors, empty ≠ failure, right level
**Rule.** Return `isError` + `errorCategory` (transient / validation / business / permission) + `isRetryable` + description + partial results + alternatives; transient → retry (inside the tool first), validation → fix input, business → explain the policy with `retriable: false`, permission → escalate; an empty result is a *successful* query; only decisions the agent must make are surfaced.
**How it gets asked**
- [FIX] `process_refund` rejects (outside 30-day window) and the agent keeps retrying → `retriable: false` + customer-friendly explanation.
- [WHICH] Customer genuinely has no orders → `{"results": [], "isError": false}`; DB down → `isError: true` with category.
- [CAUSE] Agent tells customers "you have no orders" during an outage → the tool masked an access failure as an empty list.
- [WHICH] Rank: handle transient internally > return a `retryable` flag > make the agent guess from text.
**Trap points**
- ✗ Generic "Operation failed" `[SILENT]`.
- ✗ Business error tagged transient `[wasted retries]`.
- ✗ `isError: true` for zero matches `[LOOKALIKE]`.
- ✗ Empty list on connection failure `[SILENT — false statement to customer]`.
- ✗ Success payload with embedded error `[SILENT]`.
- ✗ Surface every transient to the agent `[wrong level]`.

### 2.4 · Two-tool token binding
**Rule.** `preview_*` returns the impact plus a single-use token; `execute_*` requires that token; skipping the preview becomes architecturally impossible.
**How it gets asked**
- [FIX] `dry_run: false` called directly on first attempt → split into preview + execute bound by a token. (This exact shape is banned in the mocks for over-use, so a fresh paper asks it sideways:)
- [WHICH] What property makes the guarantee hold → the token exists only after a preview, is single-use, server-issued, unguessable.
- [LOOKALIKE] Token binding vs `PreToolUse` hook (2.7) → token when *a preview must have happened*; hook when *a threshold must block*; both are code-level.
**Trap points**
- ✗ Server-side timing heuristic `[fragile]`.
- ✗ Orchestration-layer confirmation prompt `[OVERBUILD]`.
- ✗ Prompt + examples `[PROMPT-NOT-CODE]`.
- ✗ A reusable/guessable token — the guarantee leaks `[broken design]`.

### 2.5 · Tool count, least privilege, scoped cross-role tools, `tool_choice` depth
**Rule.** 4–5 role-scoped tools beat 18; a misused generic tool is replaced by a constrained one; a high-frequency simple need gets a scoped cross-role tool; `any` guarantees *some* tool call, `tool` guarantees *that* tool, `auto` guarantees nothing; force a first step then relax to `auto`.
**How it gets asked**
- [tool count · FIX] Subagent with 18 tools misfires; peer with 5 selects correctly → restrict to the role's 4–5.
- [tool_choice · FIX] Extraction agent sometimes replies in prose → `{"type":"any"}`.
- [tool_choice · FIX] Metadata must precede enrichment, prompt obeyed ~90% → force `extract_metadata` on the first call, then `auto`.
- [tool_choice · WHICH] `any` with three extraction tools → still picks the best-fitting one; output always structured.
- [REVERSE ⚑] Requirement is only "structured output" or "some tool" → `any` (or `auto` if text is acceptable); forcing a named tool is over-specification (Exam 19 Q23, Exam 20 Q48).
**Trap points**
- ✗ Keep 18 tools and write better descriptions for all `[count is the root cause]`.
- ✗ Full catalogue "for flexibility" `[misuse outside specialisation]`.
- ✗ Forced tool on *every* turn — enrichment tools can never run `[OVERSPEC]`.
- ✗ `auto` + "you must use a tool" in the prompt `[PROMPT-NOT-CODE]`.
- ✗ `any` when a *specific* tool must run first `[LOOKALIKE]`.
- ✗ `tool` when `any` suffices ⚑ `[OVERSPEC]`.

### 2.6 · MCP — primitives, config scopes, env vars, resources, community vs custom, MCP vs built-in
**Rule.** Tools act, resources are read-only catalogs, prompts are templates; all servers' tools are discovered at connection and available together; `.mcp.json` (project, version-controlled) vs `~/.claude.json` (user); `${VAR}` keeps secrets out of the repo; standard integrations use community servers; an MCP tool losing to Grep needs a description that states what Grep cannot do.
**How it gets asked**
- [config · FIX] Team shares a server, each dev has a GitHub token → `.mcp.json` + `${GITHUB_TOKEN}`, documented in README.
- [config · WHERE] Personal/experimental server → `~/.claude.json`.
- [resources · FIX] Agent burns turns guessing `search_issues` queries to learn what exists → expose an issue catalog as a *resource*.
- [resources · WHICH] Contrast resource vs a `list_everything` tool on staleness / context cost / reliability of invocation; "what can a resource *not* do" → act.
- [community · WHICH] Jira integration → community server; a genuinely team-specific workflow → custom.
- [built-in · FIX] Semantic code-search server exists, agent keeps using Grep → richer MCP description (unique capability, outputs, what built-ins can't provide).
- [WHICH] "Do multiple servers take turns?" → no, simultaneous.
**Trap points**
- ✗ Each developer adds the server in user scope `[inconsistent tooling]`.
- ✗ Commit a placeholder token `[secret in repo]`.
- ✗ `list_everything` tool the agent must remember to call `[LLM call + hope]`.
- ✗ Paste the catalog into the system prompt `[bloat, stale]`.
- ✗ Build a custom Jira server "for control" `[reinvents maintained work]`.
- ✗ Remove/disable Grep `[DISCARD]`; "always prefer MCP tools" rule `[blunt]`.
- ✗ Three-scope answer (local/project/user) — real in current docs; the exam frames two `[EXAM≠DOCS, safe]`.

### 2.7 · Hooks — `PreToolUse` and `PostToolUse`
**Rule.** `PreToolUse` runs before the call (validate, block, modify params); `PostToolUse` runs after (transform, normalise, log, trim); hooks are deterministic, prompts are probabilistic.
**How it gets asked**
- [FIX] Third-party tools return Unix timestamps, ISO dates, numeric codes → `PostToolUse` normalises centrally.
- [FIX] Bulk deletion >50 records must be blocked and escalated → `PreToolUse`.
- [FIX] Refund >$500 must be intercepted and redirected → `PreToolUse`.
- [WHICH] Trim 40-field tool output to 5 fields → `PostToolUse` (5.5); identity-before-refund gate → `PreToolUse` (1.14).
- [REVERSE ⚑] A hook is deployed and one downstream consumer lost a field it needed → adjust the hook's field list, don't remove the hook (Exam 14 Q19/Q54 pattern).
**Trap points**
- ✗ `normalize_data` tool the agent calls after each retrieval `[LLM overhead + hope]`.
- ✗ Document formats in the system prompt `[PROMPT-NOT-CODE]`.
- ✗ Per-tool wrappers `[fragmented maintenance]`.
- ✗ Threshold rule in the prompt `[PROMPT-NOT-CODE]`.
- ✗ Remove the hook when it has a side-effect ⚑ `[DISCARD]`.

### 2.8 · Bundling vs composite tools ⚑⚑⚑⚑⚑ (missed on Exams 5, 8, 10, 11, 14 — the oldest open trap)
**Rule.** When two tools are habitually called in sequence, first prompt the agent to bundle the calls into one turn (it can emit several `tool_use` blocks in one response); a composite tool is the fallback because it hides the composition.
**How it gets asked**
- [FIX] `get_customer` then `lookup_order` in separate turns on nearly every case → instruct bundling in one turn.
- [REVERSE] The team already built `get_customer_with_orders` and now sees a second-order cost → hidden composition, coupling, loss of independent reuse, one more description competing for selection.
- [WHICH] When *is* a composite justified → the sequence is invariant, atomicity or one transaction is required, or the composition must be *enforced* rather than hoped for — the corpus's own preference (bundling) can be the distractor when the stem demands a guarantee.
- [LOOKALIKE] Bundling (several tool calls in one turn) vs parallel subagents (several `Task` calls in one turn) — same mechanic, different object.
**Trap points**
- ✗ Composite by default `[hides composition]`.
- ✗ Bundling when the stem asks for atomicity/enforcement `[REVERSE]`.
- ✗ A hook to force ordering when the only problem is latency `[OVERBUILD]`.
- ✗ Reading "the agent can request multiple tools at once" as needing a new tool `[misreads the mechanic]`.

### 2.9 · Built-in tools — Grep, Glob, Read, Write, Edit, Bash
**Rule.** Grep searches content, Glob matches paths, Edit replaces via a *unique* anchor, Read+Write is the fallback for a non-unique anchor, Bash runs commands; investigate incrementally (Grep → Read → Grep → Read); when a function is wrapped/re-exported, collect every exported name first, then Grep each.
**How it gets asked**
- [WHICH] Every file referencing deprecated `formatDate` → Grep. All TypeScript test files → Glob `**/*.test.tsx`.
- [HOW] Understand an unfamiliar codebase → Grep entry points, Read them, Grep usages, Read consumers.
- [FIX] Edit failed, anchor appears twice → Read + Write.
- [HOW] Rename `calculateTax`, wrapped as `getTax` and re-exported → collect all names, then Grep each.
- [WHICH] Run the test suite / git → Bash.
**Trap points**
- ✗ Glob `**/formatDate*` `[matches names, not contents]`; Grep "test" `[matches prose, misses files]` `[LOOKALIKE]` (KD 26).
- ✗ Read every file first "for full context"; Glob the tree then Read each `[same anti-pattern]` (KD 28).
- ✗ Retry Edit with a *shorter* anchor `[more collisions, not fewer]`; `sed` via Bash `[bypasses the sanctioned fallback]` (KD 27).
- ✗ Grep only the original name `[misses wrapper callers]`.

---

## 7. Content draft — Domain 3 · Claude Code Configuration & Workflows (20%)

### 3.1 · CLAUDE.md hierarchy, shared vs personal, `@import`, `/memory`
**Rule.** User (`~/.claude/CLAUDE.md`), project (`CLAUDE.md` or `.claude/CLAUDE.md`), directory-level, and `.claude/rules/` all load; discovered files are *concatenated*, not overridden; project files are version-controlled and shared, user files are personal; `@path` imports (no space, relative to the importing file, nesting depth "5" in the corpus); `/memory` lists what is actually loaded.
**How it gets asked**
- [CAUSE] Three developers follow "comprehensive error handling", the new fourth doesn't → the rule is in their `~/.claude/CLAUDE.md`; move it to the project file.
- [HOW] Rule works in some sessions, not others → `/memory` to see which files loaded.
- [HOW] Standards per package without one giant global file → each package's CLAUDE.md `@import`s only its standards.
- [WHICH] "Does a subdirectory CLAUDE.md override the root?" → no; both are in context; resolve conflicts by editing.
- [EXAM≠DOCS] Import depth is contested (corpus 5, current docs 4, guide silent) — if forced, answer 5; the syntax rules are the stable part.
**Trap points**
- ✗ "Lower level overrides higher" `[EXAM≠DOCS, conflict-risk — not the key]`.
- ✗ `override: true` frontmatter; "Claude caches CLAUDE.md"; "Claude learns per-user preferences" `[FAKE]`.
- ✗ Repeat the instruction louder each session `[SYMPTOM]`.
- ✗ `CLAUDE.local.md` / managed-policy level as the answer — real, but outside the guide's three levels `[EXAM≠DOCS, safe]`.
- ✗ ⚑ The `.claude/rules/` reflex — reaching for `rules/` when the need is "always" (CLAUDE.md), "on demand" (skill), or "the context is missing" (put it in the prompt/CLAUDE.md) — six instances across Exams 12, 13, 17, 14.

### 3.2 · `.claude/rules/` — path-scoped rules
**Rule.** Markdown files with `paths:` YAML globs, loaded only when Claude works on matching files.
**How it gets asked**
- [FIX] React components / API handlers / DB models each have conventions; tests co-located → `rules/` with globs.
- [FIX] 500-line CLAUDE.md, hard to navigate → split into topic files under `rules/` (3.11).
- [REVERSE] Convention that applies always → root CLAUDE.md; workflow guidance → a skill; missing project context in CI → CLAUDE.md, not a glob rule.
**Trap points**
- ✗ Root CLAUDE.md under headings `[model inference, not path match]`.
- ✗ A CLAUDE.md in every subdirectory `[breaks when files are spread]`.
- ✗ ⚑ `rules/` as the answer to "where should this workflow live" or "what supplies the missing context" — the glob triggers on *paths*, nothing else `[the reflex]`.

### 3.3 · Skills — frontmatter, `allowed-tools`, `context: fork`
**Rule.** `SKILL.md` frontmatter: `description`, `argument-hint`, `context: fork` (isolated subagent context), `allowed-tools` (the exam's framing: restricts what the skill may do); fork for discovery, analysis, exploration, brainstorming — implementation stays in the main session.
**How it gets asked**
- [FIX] `/analyze-codebase` makes Claude lose the original task → `context: fork`.
- [FIX] `/explore-alternatives` — rejected approaches bleed into the implementation → `context: fork`.
- [WHERE] Limit a skill to safe file operations → `allowed-tools: [Write, Read]` in SKILL.md — not `.mcp.json`, CLAUDE.md, or a `config.json` commands array.
- [WHICH] Which key prompts the user for required arguments → `argument-hint`.
- [EXAM≠DOCS] Current docs: `allowed-tools` is a permission *pre-grant* and `disallowed-tools` is the restrictor; the exam still tests `allowed-tools` as the scoping key — answer per the guide.
**Trap points**
- ✗ Switch to a faster model `[irrelevant]`; compress results to a short summary `[loses analysis]`; split into two skills `[leak persists]`.
- ✗ `disallowed-tools` as the key `[EXAM≠DOCS]`.
- ✗ `context: fork` for the implementation step `[REVERSE]`.

### 3.4 · Custom slash commands
**Rule.** `.claude/commands/` (project, version-controlled) vs `~/.claude/commands/` (personal); text after the command arrives as `$ARGUMENTS`; commands and skills are unified — both create `/name`.
**How it gets asked**
- [WHERE] `/review` for everyone who clones → `.claude/commands/`.
- [WHICH] How the command receives its argument text → `$ARGUMENTS`.
**Trap points**
- ✗ `~/.claude/commands/` for a team command `[personal scope]`.
- ✗ A `config.json` commands array `[FAKE]`.

### 3.5 · Personal vs project skill customisation — two framings, flag for Ram
**Rule (corpus/KD 4).** A personal skill at `~/.claude/skills/commit/SKILL.md` with the *same name* overrides the project `/commit` for that user. **Rule (official guide, task 3.2, verbatim):** "creating personal variants in `~/.claude/skills/` with *different names* to avoid affecting teammates."
**How it gets asked**
- [HOW] Customise `/commit` without affecting teammates → a personal skill under `~/.claude/skills/`. Both framings agree on the *location*; they disagree on the *name*.
- **Posture (recommended, open decision Q-open-1):** if the options force a choice, prefer the option that keeps the change in personal scope; if two personal-scope options differ only by name, the guide's wording is "different names" — but the practice-test key (source of the official samples) is same-name override. Ram decides which to trust on the day.
**Trap points**
- ✗ Edit the project skill `[affects teammates]`.
- ✗ `override: true` frontmatter `[FAKE]`.

### 3.6 · Plan mode vs direct execution
**Rule.** Plan mode (read-only exploration → plan → approval → execute) for large scope, architectural choices, multiple valid approaches, many files; direct execution for clear, routine, well-specified changes; decide up front, not reactively.
**How it gets asked**
- [WHICH] Monolith → microservices; Slack support with several integration options; 45-file library migration → plan mode. Function with a clear I/O spec; one-file fix with a stack trace → direct.
- [WHICH] "Start direct and switch to plan when it gets hard" → wrong; reactive switching is the expensive path.
**Trap points**
- ✗ Reactive switching `[rework]`.
- ✗ Plan mode for a routine one-liner `[OVERBUILD]`.
- ✗ "Plan mode executes with confirmation prompts" `[it is read-only]`.

### 3.7 · Iterative refinement — four techniques
**Rule.** Interview pattern (Claude asks *you* first) for underspecified briefs in unfamiliar domains; test-driven iteration (tests first, feed failures); 2–3 concrete input/output pairs for transformations; batch *interacting* fixes in one message and *independent* fixes sequentially.
**How it gets asked**
- [interview · FIX] Caching layer in an unfamiliar domain; three versions each miss a different requirement → restart with "ask me what you need to know first".
- [TDI · FIX] Null-handling bug described in prose, partial fixes → hand it a failing test with sample input + expected output.
- [I/O · FIX] Transformation output shape differs each run → 2–3 concrete pairs.
- [batching · WHICH ⚑] Locking bug + retry bug that depends on it + unrelated typo → locking + retry together, typo separately or riding along (Exam 17, Exam 20 Q58 — the axis is *interaction*, not count).
- [LOOKALIKE] Interview pattern (developer brief, non-obvious implications) vs 4.19 proceed-with-assumptions (end-user vague request) — opposite advice, different situation.
**Trap points**
- ✗ Keep iterating one missed requirement at a time `[slow, fixes disturb each other]`.
- ✗ "Interviewing wastes a turn" `[misconception]`.
- ✗ Re-describe the bug more emphatically `[prose stays ambiguous]`.
- ✗ Tests written *after* generation `[verification, not TDI]`.
- ✗ "Examples make it copy instead of generalise" `[misconception]`.
- ✗ "Always one issue per message" / "always everything in one message" ⚑ `[wrong axis]`.

### 3.8 · CI/CD — `-p`, re-run consistency, isolation, context
**Rule.** `claude -p "…"` runs non-interactively; on re-runs feed the prior findings and ask for new/unresolved only; the session that wrote the code is a weak reviewer of it; CLAUDE.md gives CI-invoked Claude its project context; include existing tests when generating tests.
**How it gets asked**
- [FIX] Pipeline hangs waiting for input → `-p` / `--print`.
- [FIX] Near-duplicate comments on every follow-up push → include the previous run's findings; report only new/unresolved.
- [WHICH] Same session reviews its own changes → less effective; independent instance (1.17/4.13).
- [FIX] Suggested tests duplicate existing ones → put the existing test file in context (4.18).
- [WHICH] How does CI Claude know the fixture conventions → CLAUDE.md.
**Trap points**
- ✗ `--batch`, `CLAUDE_HEADLESS=true` `[FAKE]`; `stdin < /dev/null` `[workaround, not documented]`.
- ✗ Blank-slate re-run "for objectivity" `[re-litigates, floods]`.
- ✗ Report only findings seen in ≥2 runs `[SILENT]`.
- ✗ Ask for fewer tests `[SYMPTOM]`.

### 3.9 · Structured output from the CLI
**Rule.** `claude -p "…" --output-format json --json-schema schema.json` yields validated, parseable output (print mode).
**How it gets asked**
- [FIX] Post each finding as an inline PR comment (path, line, severity, fix) → `--output-format json` + `--json-schema`.
**Trap points**
- ✗ "Output Format" section in CLAUDE.md `[not guaranteed]`; format instruction in the prompt `[variable]`; regex post-processing `[SYMPTOM]`.
- ✗ `--json` `[FAKE flag]`; `stream-json` exists but isn't the answer.

### 3.10 · Batch API from the CI angle (full treatment in 4.11)
**Rule.** Blocking pre-merge checks → synchronous; overnight/weekly/nightly jobs → Batch (50% off, ≤24h, `custom_id`); a request cannot pause mid-processing for a tool result.
**How it gets asked** — [WHICH] which of several workloads belong on Batch (banned shape in the mocks; a fresh paper asks the SLA arithmetic, `custom_id`, selective re-submission, or the tool-support fact instead — see 4.11).
**Trap points** — ✗ Batch a blocking check for the discount `[latency]`; ✗ "iterative review that fetches related files mid-review can run on Batch" `[needs the interactive loop]`; ✗ "Batch can't use tools at all" ⚑ `[false — see 4.11]`.

### 3.11 · CLAUDE.md organisation
**Rule.** Universal standards stay in CLAUDE.md (loads every session); workflow guidance (PR review, deploy, migrations) becomes skills (on demand); topic modularisation uses `.claude/rules/` or `@import`.
**How it gets asked**
- [FIX] 400+ lines mixing standards, PR checklist, deploy, migrations → keep standards, move workflows to skills.
- [FIX] 500+ lines hard to navigate → topic files under `rules/`; `@import` if the content should stay in the concatenated context.
- [WHICH] Which loads every session / on invocation / on path match → CLAUDE.md / skill / rule.
**Trap points**
- ✗ Move everything to skills `[standards would need invoking]`.
- ✗ Split workflow content into `rules/` ⚑ `[rules are path-scoped, not workflow-scoped]`.
- ✗ One giant global file imported everywhere `[defeats the point]`.

### 3.12 · Session management in Claude Code
**Rule.** `--resume`, `fork_session`, `/compact` (compresses; risks exact numbers/dates), `/memory`; verbose discovery → Explore subagent, not `/compact`; stale tool results → new session + summary.
**How it gets asked**
- [FIX] Discovery phase fills the window before implementation → Explore subagent returns a summary.
- [WHICH] "Should I `/compact` mid-task?" → loses the precision implementation needs.
- [WHICH] What `/compact` risks → exact numeric values, dates, specifics.
**Trap points**
- ✗ `/compact` mid-task `[precision loss]`; multiple sessions with `--continue` `[coordination overhead]`; bigger window `[BIGGER-CONTEXT]`.
- ✗ Abandon a working session for a fresh one when a targeted note would do ⚑ `[DISCARD]`.

---

## 8. Content draft — Domain 4 · Prompt Engineering & Structured Output (20%)

### 4.1 · Few-shot prompting
**Rule.** Use examples when instructions produce inconsistent format, tool selection is ambiguous, requests need decomposition, or escalation needs calibration; target the 4–6 genuinely ambiguous cases with rationale, not 10–15 clear ones.
**How it gets asked**
- [FIX] "I need help with my recent purchase" misroutes between `get_customer` / `lookup_order` → 4–6 targeted examples with rationale.
- [FIX] Review feedback format inconsistent despite instructions → 3–4 examples of the exact format (issue, location, fix).
- [LOOKALIKE ⚑] Descriptions first for selection (2.2); few-shot for the residual ambiguity (Exam 19 Q53).
**Trap points**
- ✗ More detailed instructions `[already failing]`.
- ✗ 10–15 clear examples `[don't touch the edge]`.
- ✗ Examples when descriptions are the root cause ⚑ `[wrong lever]`.
- ✗ Classifier `[OVERBUILD]`.

### 4.2 · Reasoning cues
**Rule.** "Think step by step" for multi-step reasoning, comparisons, staged transformations; not for single-step tasks.
**How it gets asked** — [WHICH] which task warrants a reasoning cue.
**Trap points** — ✗ a reasoning cue as the fix for a *format* problem `[wrong tool]`; ✗ extended thinking as a substitute for independent review (4.13).

### 4.3 · System prompt design
**Rule.** Persistent behavioural constraints — tone, persona, rules for the whole conversation, response format — live in the system prompt.
**How it gets asked** — [WHERE] enthusiasm, reasoning transparency, clarifying-question rules → system prompt.
**Trap points** — ✗ first user message `[loses authority]`; ✗ environment variables `[no effect]`; ✗ first assistant message `[model deviates from its own text]`; ✗ prefill (4.4) for *persistent* rules `[prefill is per-response]`.

### 4.4 · Prefilling
**Rule.** Seed the assistant turn to suppress filler openings; prefix the *next user message* to inject a real-time event.
**How it gets asked** — [FIX] "Certainly!" openings → prefill a direct opening; [FIX] shipping webhook fires mid-chat → prefix the next user message.
**Trap points** — ✗ lower temperature `[randomness, not phrases]`; ✗ post-process greetings `[SYMPTOM]`; ✗ system-prompt instruction `[less reliable]`; ✗ modify the system prompt mid-session `[rebuild]`; ✗ synthetic user message `[breaks the dialogue]`.

### 4.5 · JSON schema design
**Rule.** `required` only when the value is always present; sometimes-absent → optional/nullable; `enum` + `"other"` + `detail`; `"unclear"` beats a confident wrong category; `field_confidence` per field; nullable prevents fabrication; format-normalisation rules go in the *prompt*, the schema constrains *shape*.
**How it gets asked**
- [CAUSE/FIX] Model invents values for missing fields → required non-nullable field; make it nullable.
- [FIX] Mixed date/currency formats in sources → normalisation rules in the prompt alongside the schema.
- [WHICH ⚑] Which decision belongs where: schema (shape, requiredness, enums, nullability) · prompt (mapping messy input) · code (business rules) — Exam 19 Q35 select-2 schema-scope.
- [REVERSE ⚑] Prevention at the source (schema) vs repair after (validate + retry) — Exam 17/19 prevention-vs-repair.
**Trap points**
- ✗ Make every field required "for completeness" `[fabrication]`.
- ✗ Normalisation in the schema `[wrong layer]`.
- ✗ Retry to fill an absent field (4.9) `[waste + fabrication]`.
- ✗ Tighten the schema to fix wrong values (4.7) `[semantics aren't shape]`.
- ✗ Read `"unclear"` as low quality `[it is the honest signal]`.

### 4.6 · `tool_use` + `tool_choice` as the structured-output guarantee ⚑⚑
**Rule.** A tool whose `input_schema` is the desired output makes the response schema-valid JSON with no syntax errors; `any` when the document type is unknown and several extraction tools exist; `tool` when a specific extraction must run (ordering); `auto` guarantees nothing.
**How it gets asked**
- [FIX] Pipeline must always get schema-valid JSON; invoices/receipts/contracts (three tools) → `any`.
- [FIX] Enrichment keeps running before metadata extraction → force `extract_metadata` on the first call.
- [REVERSE ⚑] Only "structured output" is required → `any`; naming a tool is over-specification; forcing on every turn locks out the other tools (Exam 19 Q23, Exam 20 Q48).
- [WHICH] "Schema compliance means the values are right?" → no (4.7).
**Trap points**
- ✗ `auto` + "respond with JSON" `[no guarantee]`.
- ✗ JSON-repair library `[SYMPTOM]`.
- ✗ `any` when a specific tool must run first `[LOOKALIKE]`.
- ✗ `tool` when `any` suffices ⚑ `[OVERSPEC]`.
- ✗ "The schema guarantees correctness" `[shape ≠ meaning]`.

### 4.7 · Syntax vs semantic errors
**Rule.** Schemas via `tool_use` eliminate the syntax class (malformed JSON, wrong types, missing required); semantic errors (wrong values, sums that don't add, wrong field, wrong category) need business-rule validation, cross-field checks, self-correction fields, sometimes humans.
**How it gets asked**
- [WHICH] Parse failures dropped to zero; reconciliation still finds bad totals → expected; the remainder is semantic → validation + feedback loop.
- [WHICH] Which validation belongs in code vs schema (4.8).
**Trap points**
- ✗ Tighten the schema `[can't check arithmetic]`.
- ✗ Revert to prompt JSON `[reintroduces syntax errors]`.
- ✗ "Validator passed = correct" `[structure only]`.

### 4.8 · Pydantic / typed validation
**Rule.** Validate in code after receipt — structure *and* business rules; validation errors become retry feedback; generate the tool's JSON Schema from the Pydantic model so contract and validator never drift.
**How it gets asked**
- [FIX] Hand-maintained schema and validator class drift → generate the schema from the model.
- [WHICH] "tool_use enforces the schema, so skip validation?" → no; semantics + defence in depth.
**Trap points**
- ✗ Code-review checklist item to keep both files in sync `[process patch]`.
- ✗ Skip validation `[semantic errors pass]`.
- ✗ Business rules in the schema `[can't express them]`.

### 4.9 · Retry-with-feedback and its limits
**Rule.** Retry with the original document + the failed extraction + the *specific* error; helps for format/structure/arithmetic; useless when the information is absent or lives in another document → nullable field, accept `null`, stop retrying; a `detected_pattern` field turns dismissals and repeated failures into aggregable data.
**How it gets asked**
- [FIX] `purchase_order_number` fails on 40 documents that never had one → nullable, accept null, stop.
- [WHICH] What goes in the retry request → document, previous extraction, exact error.
- [FIX] Findings frequently dismissed, team can't tell which types are noise → `detected_pattern` per finding; dismissal rate per pattern.
**Trap points**
- ✗ Raise max retries 3 → 10 `[absent stays absent]`.
- ✗ Strengthen the feedback text `[can't conjure data]`.
- ✗ Keep the field required "for data quality" `[fabrication]`.
- ✗ Free-text dismissal reason `[doesn't aggregate]`.
- ✗ "Retry always converges" `[misconception]`.

### 4.10 · Self-correction patterns
**Rule.** Build the re-derivation into the output — `stated_total`, `calculated_total`, `conflict_detected` — so contradictions surface as data at extraction time.
**How it gets asked** — [FIX] totals mismatch found weeks later in reconciliation → stated vs calculated + conflict flag, route at extraction time; [WHICH] "self-correction = ask 'are you sure?'" → no, structural.
**Trap points** — ✗ monthly reconciliation report `[weeks late]`; ✗ "be careful with totals" `[no mechanism]`; ✗ conversational are-you-sure `[optional, unmeasurable]`.

### 4.11 · Batch processing ⚑⚑ (Exam 20 Q42 + Q55: batch *does* support tool definitions)
**Rule.** 50% cheaper; up to 24h with no SLA; `custom_id` is the join key and results arrive in any order; requests may include tools and multi-turn histories, but each request is one shot — no pause to execute a tool mid-request; anything blocking stays synchronous; re-submit only the failures (fixed) by `custom_id`; submission deadline = downstream deadline − 24h; refine on a synchronous sample first.
**How it gets asked**
- [WHICH] Pre-merge check → sync; overnight tech-debt / weekly audit / nightly tests / 10,000 documents → batch.
- [CAUSE] Results don't line up with inputs → matched by position; use `custom_id`.
- [HOW] 95 of 100 succeed, 5 hit context limits → re-submit only the 5, chunked.
- [HOW] Results needed within 30h → submit within 6h; recurring pipeline → 4h windows.
- [HOW] Validate a new extraction prompt before a 10,000-doc batch → synchronous sample first.
- [WHICH ⚑] "Can a batch request define tools / carry a multi-turn history?" → yes. "Can it pause for a `tool_result` mid-request?" → no; continue in a follow-up request. Guide wording: "does not support multi-turn tool calling *within a single request*."
**Trap points**
- ✗ Rely on result order `[silent mis-join]`.
- ✗ Re-submit all 100 `[pays twice, duplicates]`; re-submit the 5 unchanged `[same failure]`.
- ✗ Plan around typical latency `[no SLA]`.
- ✗ "Batches can't use tools" ⚑ `[outdated]`; "batch will pause while I answer the tool call" `[one shot]`.
- ✗ Iterate on the full batch `[each try costs a batch + 24h]`.
- ✗ Batch a blocking check "for the discount"; poll faster to make it interactive `[latency isn't negotiable]`.

### 4.12 · Multi-pass review (same point as 1.7)
**Rule.** Single-pass over many items → attention dilution; per-file pass + integration pass.
**Trap points** — ✗ larger model / bigger window `[BIGGER-CONTEXT]`.

### 4.13 · Multi-instance independent review
**Rule.** Send only the artefact + criteria to a fresh instance; have the reviewer report confidence per finding so high-confidence findings auto-comment and low-confidence ones go to a human.
**How it gets asked** — [FIX] passes its own "review carefully" step, bugs reach production → second instance; [WHICH] "second pass in the same conversation?" → not independent; [HOW] route findings by reviewer confidence.
**Trap points** — ✗ self-review instruction; ✗ extended thinking; ✗ same-conversation second pass; ✗ consensus voting `[SILENT]`.

### 4.14 · Prompt chaining
**Rule.** Sequential focused prompts, each output feeding the next (identify issues → generate fixes); the fixed-pipeline pattern of 1.7.
**How it gets asked** — [WHICH] name the pattern; when chaining beats one big prompt (focus, consistency); chaining vs adaptive (predictable vs open-ended).
**Trap points** — ✗ chaining for an open-ended investigation `[REVERSE]`; ✗ one prompt for a multi-stage task `[dilution]`.

### 4.15 · Escalation & confidence routing
**Rule.** Explicit escalation criteria with few-shot "escalate when / resolve when" examples in the system prompt.
**How it gets asked** — [FIX] agent escalates simple photo-proven replacements, handles complex policy exceptions itself; 55% FCR vs 80% → explicit criteria + examples.
**Trap points** — ✗ self-confidence rating + threshold `[OVERBUILD, uncalibrated]`; ✗ separate classifier `[OVERBUILD]`; ✗ sentiment `[5.8]`.

### 4.16 · Specificity vs abstraction
**Rule.** Replace vague intent with testable criteria ("flag only when the claimed behaviour contradicts the code's actual behaviour"; explicit severity criteria with examples).
**How it gets asked** — [FIX] review flags correct comments as wrong; severity inconsistent → concrete criteria.
**Trap points** — ✗ "be more careful" / more adjectives `[still abstract]`; ✗ bigger model `[BIGGER-CONTEXT]`.

### 4.17 · Trust restoration by category
**Rule.** Temporarily disable the high-false-positive categories (style, naming, docs) and keep the high-precision ones (security, performance) while the prompts are fixed.
**How it gets asked** — [FIX] 52% style FP, 48% docs, 8% security, 18% performance; developers dismiss everything → surgical disable.
**Trap points** — ✗ show confidence scores `[still all shown]`; ✗ few-shot across all categories over weeks `[too slow]`; ✗ uniform strictness cut `[hurts precise categories]`; watch stem constraints like "stakeholders rejected filtering before developers see findings" — then disabling is off the table and the key shifts.

### 4.18 · Context-aware suggestions
**Rule.** Claude can only avoid duplicating what it can see — put the existing tests/artefacts in context.
**How it gets asked** — [FIX] 6 of 10 suggested tests already exist → include the test file.
**Trap points** — ✗ ask for 5 `[assumes ordering]`; ✗ keyword post-filter `[misses semantic dupes]`.

### 4.19 · Proceed with stated assumptions vs ask
**Rule.** For a vague end-user request, state reasonable assumptions and proceed, inviting corrections; not 4+ questions, not one compound question, not hidden defaults; applies to subagents too.
**How it gets asked** — [HOW] "Can you help with the report?" → proceed with stated assumptions; [WHICH] synthesis agent blocking on every gap → proceed and annotate.
**Trap points** — ✗ 4+ questions `[35–40% abandonment]`; ✗ one compound question `[same burden]`; ✗ hidden defaults `[SILENT]`; ✗ **LOOKALIKE with 3.7.1** — the interview pattern is right for a *developer's underspecified implementation brief*; proceed-with-assumptions is right for a *user's vague request in conversation* — the stem tells you which room you are in.

### 4.20 · Behavioural drift
**Rule.** Accumulated assistant responses dilute the system prompt's influence; fixes are reminders at breakpoints, few-shot instead of verbose rules, prefill for specific patterns; it is not context overflow and the system prompt does not "apply only once".
**How it gets asked**
- [CAUSE] Generic advice by turn 7 at 2,500 tokens → drift by accumulation.
- [FIX] Tutor with a 2,800-token rule-heavy prompt ignores proficiency after 12 turns → replace verbose rules with few-shot demonstrations.
- [WHICH] Reminders every 4–5 turns → symptom when the prompt itself is the problem.
**Trap points** — ✗ context overflow `[impossible at that size]`; ✗ "system prompt only applies to turn 1" `[false]`; ✗ periodic reminders as the primary fix `[SYMPTOM]`; ✗ bigger context `[BIGGER-CONTEXT]`.

---

## 9. Content draft — Domain 5 · Context Management & Reliability (15%)

### 5.1 · The stateless API
**Rule.** No server-side memory; the application resends the whole `messages` array every call; more turns → more tokens → more cost and latency.
**How it gets asked** — [CAUSE] "I love jazz" forgotten two turns later → history not being sent; [CAUSE] latency/cost climb past 50 turns → the whole history rides along each time.
**Trap points** — ✗ `session_id` `[FAKE]`; ✗ vector DB for ordinary memory `[OVERBUILD — scale decides, see 5.7]`; ✗ context exceeded at 3 turns `[impossible]`; ✗ longer responses / DB slowness `[wrong cause]`.

### 5.2 · Lost in the middle
**Rule.** Attention is strong at the start and end of long input and weak in the middle; put a key-findings summary first, use section headings, and have upstream agents return structured facts instead of verbose traces.
**How it gets asked** — [FIX] 75K input; first 15K and last 10K used, middle 50K missed → summary at the start + headings; [FIX] 155K combined output but synthesis works best under 50K → upstream agents return structured facts.
**Trap points** — ✗ summarise everything under 20K `[loses findings]`; ✗ rotate which agent goes first `[pattern unchanged]`; ✗ intermediate summarisation agent `[OVERBUILD]`; ✗ bigger window `[BIGGER-CONTEXT]`.

### 5.3 · Context window management — the hybrid
**Rule.** Extract critical facts into a verbatim structured block, summarise the general discussion, keep the recent turns verbatim.
**How it gets asked** — [FIX] 78K-token cooking session with allergies, scaled quantities, chatter → hybrid.
**Trap points** — ✗ summarise the whole history `[allergy precision lost]`; ✗ keep only the last 20K `[early facts dropped]`.

### 5.4 · Transactional facts persistence
**Rule.** A case-facts block (IDs, amounts, dates, status) lives outside the summarised history in every prompt and is updated whenever a fact appears.
**How it gets asked** — [FIX] "the 15% discount I mentioned" becomes "promotional pricing was discussed" → case-facts block.
**Trap points** — ✗ raise the summarisation threshold `[delays]`; ✗ better summariser prompt `[still hopes]`; ✗ external storage + retrieval `[OVERBUILD for session facts]`.

### 5.5 · Trimming verbose tool outputs
**Rule.** A `PostToolUse` hook keeps only the relevant fields before results enter context.
**How it gets asked** — [FIX] `lookup_order` returns 40+ fields, 5 matter, every turn → trim in a hook; [REVERSE ⚑] hook deployed, a downstream consumer lost a needed field → widen the field list, don't remove the hook; [WHICH] trim vs `/compact` vs summarise for *tool clutter* → trim at the source.
**Trap points** — ✗ "ignore irrelevant fields" prompt `[tokens still spent]`; ✗ more aggressive summarisation `[SYMPTOM]`; ✗ bigger model `[BIGGER-CONTEXT]`; ✗ remove the hook ⚑ `[DISCARD]`.

### 5.6 · Context isolation with subagents
**Rule.** Subagents see only what is passed; that isolation is the feature that lets an Explore subagent absorb verbose discovery and return a summary.
**How it gets asked** — [FIX] discovery over 120 files fills the window before implementation → Explore subagent; [CAUSE] subagent lacks X → X wasn't passed.
**Trap points** — ✗ `/compact` `[precision]`; ✗ several sessions with `--continue` `[coordination]`; ✗ assume shared context `[FAKE]`.

### 5.7 · Long-term conversation memory
**Rule.** Months of history (85K tokens, many sessions) → semantic retrieval over the full history; rolling windows lose early sessions; progressive summarisation loses specific conclusions.
**How it gets asked** — [FIX] "What did we conclude about isolation?" across a 3-month book club → embeddings + retrieval; [LOOKALIKE] ordinary multi-turn memory (5.1) needs no vector DB — the scale decides.
**Trap points** — ✗ rolling window; ✗ progressive summarisation; ✗ XML tags marking conclusions `[doesn't retrieve at scale]`; ✗ vector DB for a 5-turn chat `[OVERBUILD]`.

### 5.8 · Escalation triggers, unreliable proxies, disambiguation
**Rule.** Escalate on structural signals — explicit request (immediately), policy silence, no progress after reasonable attempts, financial threshold (via a hook), repeated failures — never on sentiment or self-rated confidence; frustration is not a request for a human until reiterated; several matching records → ask for another identifier.
**How it gets asked**
- [HOW] "I want to speak to a manager" → escalate now, not "let me first…".
- [HOW] "This is outrageous!" → acknowledge, offer a resolution, escalate if they reiterate.
- [HOW] Two accounts under one name → ask for email/order number.
- [FIX] Escalation design → explicit criteria + few-shot (4.15).
**Trap points** — ✗ escalate on anger `[mood ≠ complexity]`; ✗ escalate below confidence 7/10 `[uncalibrated]`; ✗ never before three attempts `[violates immediate escalation]`; ✗ pick the most recent / first account `[misidentification]`; ✗ escalate the ambiguity `[resolvable by asking]`; ✗ complexity classifier `[OVERBUILD]`.

### 5.9 · Human oversight & confidence calibration
**Rule.** Field-level confidence, calibrated on a labelled validation set; route low-confidence and ambiguous/contradictory sources to humans; audit the automated path with stratified random samples across document types and fields; an aggregate 97% can hide 40% failure on one rare type — validate per segment before reducing review.
**How it gets asked** — [HOW] 97% overall, proposal to auto-process everything high-confidence → per-type/per-field analysis first + stratified sampling; [HOW] design the review routing; [WHICH] "audit only the low-confidence stream?" → no.
**Trap points** — ✗ aggregate threshold `[masks segments]`; ✗ trust raw self-confidence `[uncalibrated]`; ✗ skip auditing high-confidence `[novel errors undetected]`; ✗ sample only the common type `[under-samples the worst]`; ✗ flat 10% random review `[wastes capacity]`; ✗ humans re-review everything `[no automation]`.

### 5.10 · Conflict detection & source attribution
**Rule.** Complete the analysis with both values, annotate the conflict with attribution, let the coordinator or a human reconcile; don't stop the pipeline to ask first.
**How it gets asked** — [HOW] government report 40% vs industry 12%, both credible → both + annotation.
**Trap points** — ✗ heuristic pick `[SILENT]`; ✗ stop and ask before completing `[blocks]`.

### 5.11 · Provenance — claim→source, dates, rendering
**Rule.** Every claim carries a structured source mapping (URL/document, excerpt/location, publication date) that survives synthesis; dates stop temporal change being read as contradiction; render by content type (tables for financials, prose for analysis, lists for technical findings, chronological for time series); separate well-established from contested.
**How it gets asked** — [FIX] final report can't attribute claims → structured mappings preserved through synthesis; [WHICH] "10% vs 15% — contradiction?" → 2023 vs 2024, growth; [FIX] financial tables flattened to prose → render by type.
**Trap points** — ✗ bibliography at the end `[SYMPTOM]`; ✗ flag every numeric disagreement `[no dates]`; ✗ uniform prose "for consistency" `[imprecise]`; ✗ re-derive attributions by searching again `[expensive, error-prone]`.

### 5.12 · Scratchpads & crash-recovery state
**Rule.** Long tasks write intermediate state to a scratchpad file and re-read it on continuation; multi-agent systems export per-agent state (status, findings, coverage, gaps) plus a manifest, and the coordinator resumes from the checkpoint.
**How it gets asked** — [CAUSE] model starts citing "typical patterns" instead of the classes it found → context degradation → scratchpad; [HOW] crash mid-investigation → manifest resume, inject persisted findings.
**Trap points** — ✗ rely on conversation history surviving `[stateless]`; ✗ re-run everything after each failure `[waste]`; ✗ keep findings only in agents' contexts `[nothing survives]`.

### 5.13 · Conversation-level state
**Rule.** Hybrid window (recent verbatim + running summary + never-dropped facts block); drift prevention via reminders at breakpoints, concrete minimal rules, few-shot over verbose rule lists. (Cross-ref 5.3, 5.4, 4.20.)
**Trap points** — ✗ pure sliding window `[drops early preferences]`; ✗ verbose abstract rule lists `[drift faster than examples]`.

### 5.14 · Root cause → pattern (the summary table as a question form)
**How it gets asked** — [CAUSE] a symptom sentence → name the root cause: never terminates → `stop_reason`; precision lost → facts compressed; context bloat → verbose tool results; subagent lacks results → isolation; missed mid-input → lost in the middle; window exhausted in discovery → discovery in main session; human queue flooded → sentiment proxy; wrong customer → heuristic match; errors slip through → aggregate masking; can't attribute → mapping lost; false contradictions → missing dates; work lost on crash → no persisted state; drift → accumulated responses; format inconsistency across tools → no normalisation hook.

---

## 10. Look-alikes index (page in the sheet — 29 one-liners, each linking to its entry)

1 project vs user CLAUDE.md → who can see it (VCS or not) · 2 `.mcp.json` vs `~/.claude.json` → shared server, personal token via `${VAR}` · 3 CLAUDE.md vs `rules/` vs skills → always / on path / on demand · 4 same-name vs different-name personal skill → see 3.5 posture · 5 `tool_use` vs `end_turn` → run tool vs stop · 6 hub vs direct → coordinator sees all · 7 narrow decomposition vs subagent quality → all succeed + wrong ground = coordinator · 8 structured error vs generic → recovery decision needs the payload · 9 transient vs permanent, 0 results vs timeout → retry / don't / accept · 10 fix descriptions vs add routing → signal before layer · 11 prompt vs precondition → guarantee needs code · 12 token binding vs `dry_run` → boolean can be skipped · 13 `context: fork` vs main → exploration isolated · 14 Batch vs sync → latency tolerance; no mid-request tool pause · 15 `-p` vs fake flags · 16 few-shot vs more instructions → format failing → examples · 17 per-file passes vs single pass → attention, not window · 18 targeted vs generic examples → 4–6 ambiguous · 19 stated assumptions vs many questions → proceed · 20 lost-in-middle → summary first + headings, not rotation/over-summarising · 21 case-facts block vs better summariser · 22 Explore subagent vs `/compact` · 23 drift by accumulation vs overflow · 24 semantic retrieval vs progressive summarisation (months) · 25 stateless: `messages[]`, no `session_id`, no vector DB for ordinary memory · 26 Grep (content) vs Glob (paths) · 27 Edit (unique anchor) vs Read+Write · 28 incremental Grep→Read vs bulk read · 29 MCP tool vs built-in → fix the description, don't remove Grep.

## 11. Exam ≠ docs page (answer per the guide)

| Point | Current docs say | Answer on the paper |
|---|---|---|
| `allowed-tools` (skills) | permission pre-grant; `disallowed-tools` restricts | **restricts** tool access during the skill |
| Subagent tool name | `Agent` (v2.1.63+; `Task` still in `system:init`) | **`Task`**; never let the name decide |
| `@import` depth | 4 hops | **5** if forced; syntax is the stable part |
| CLAUDE.md levels | concatenated; 4 levels incl. managed policy + `CLAUDE.local.md` | levels + sharing scope; **no override mechanism** is the tested judgment |
| MCP scopes | local / project / user (+ enterprise) | **project vs user** |
| `tool_choice` | `none` exists | **auto / any / forced** only |
| `stop_reason` | 7 values | tested pair is `tool_use` / `end_turn` |
| Batch + tools | tools + multi-turn allowed, one shot per request | "no multi-turn tool calling **within a single request**" |
| Item format | — | multiple-response items exist; each states how many; all-or-nothing |
| Skip questions | v1.0 silent | no penalty → still answer everything |

## 12. Document structure (paged, one file, no external assets)

Sticky top nav + prev/next. Pages: **Start** (what this is, how to read an entry, badge legend, exam-day facts) · **The setter's toolkit** (§4 above — stem anatomy, ten molds, twelve tie-breakers, out-of-scope list) · **D1** · **D2** · **D3** · **D4** · **D5** · **Look-alikes** (§10) · **Exam ≠ docs** (§11) · **Your ledger** (only if Q2 = yes: the ⚑ entries ranked by miss count, linking in). Print stylesheet so it can be a PDF; no localStorage; inline CSS/SVG only. Design decisions (skin, density, whether entries collapse) wait on Q3.

## 13. Open decisions

- **Q-open-1 · §3.5 posture** — same-name override (corpus/KD 4, practice-test key) vs different-name variant (official guide bullet). Recommendation stated in 3.5; Ram to confirm.
- **§ tags on entries** — kept as small muted jump-pointers to the corpus; drop on request (the Masterclass rule was "no citations"; this sheet is corpus-keyed by design).
- **Popup questions** (asked in chat): concept unit · personal-miss overlay depth · playbook · exam timing.
- **Scope challenge, stated once:** the project's own repeated finding (Sessions 19–21) is that specific re-reads beat new artifacts this close to the sitting. This sheet is built to *be* that re-read — 73 entries, each one screen — but if the sitting is in a few hours the leanest use is: toolkit page → ⚑ entries → look-alikes → exam≠docs, and skip the rest.
