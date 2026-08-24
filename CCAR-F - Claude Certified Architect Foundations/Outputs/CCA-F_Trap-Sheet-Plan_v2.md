# CCA-F Trap Sheet — Plan & Full Content Draft (v2 · one card per testable point)

**Supersedes:** `CCA-F_Trap-Sheet-Plan_v1.md` (same words, section-level entries). v2 splits every multi-concept section into its testable points — **136 cards** — per Ram's choice on 2026-08-18. Decisions locked in the same popup: ⚑ personal-miss badges from `SESSION-STATE.md` + `CCA-Prep_Mistake-Patterns_v1.html` (no EXAM-LOG mining) · lean purpose-built layout, no playbook · sitting is today, ship lean.
**Deliverable:** `Outputs/CCA-F_Trap-Sheet_v1.html`, generated from this file by `prep with quiz/WIP-TRAPSHEET/build_trap_sheet.py` (this markdown is the single source of truth; the script parses the card grammar below).
**Card grammar (for the renderer):** `### Dn-NN · Title` · meta line `§x.y · KD n · ⚑ …` (any subset) · `**Rule.**` one sentence · `**Asked**` bullets `- [FORM] …` · `**Traps**` bullets `- ✗ … \`[MOLD]\``. Cross-references are bare card ids (`D2-08`) and become links.

---

## Start page

**What this is.** Every earlier CCA-F artifact answers *what is true*. This sheet answers, for each concept, *how a setter turns it into an item and which wrong option is built to catch a candidate who half-knows it*. Two lenses per card, nothing else: **Asked** (the signal in the stem → the form of the ask → the answer direction, including the mirror-image REVERSE angle) and **Traps** (the distractor, why it fails, its mold).

**Exam facts.** 60 items · 120 min · 4 of 6 scenarios · scaled 100–1000, pass 720 · per-domain % on the report is informational · **multiple-response items exist and each item states how many to select; scoring is all-or-nothing** — every tick must be independently defensible · no penalty for guessing, so answer everything · D1 27% · D2 18% · D3 20% · D4 20% · D5 15%.

**Legend.** `[FIX]` best fix/approach (~67% of real items) · `[HOW]` how should you… (~12%) · `[CAUSE]` root cause (~9%) · `[WHICH]` which mode/situation/pattern (~9%) · `[WHERE]` placement (~3%) · `[REVERSE]` the mirror-image ask · `⚑` you have missed this in a scored paper (exam numbers on the card) · `§` jump-pointer to the corpus section · `KD` Key Distinction number.

## The setter's toolkit

**How a stem is built.** 2–5 sentences of situation with operational evidence — a percentage ("45% of the time", "55% first-contact resolution vs 80% target"), a count ("14 files", "400+ lines", "12+ tool calls", "~75K tokens"), a quoted user line ("I love jazz", "I want a manager") or an inline token (`get_customer`, `context: fork`, `${GITHUB_TOKEN}`). It often ends by naming a constraint ("without affecting teammates", "without adding human oversight", "stakeholders rejected filtering findings") — read that constraint before the options; it usually eliminates one. Then one ask. No negative stems, no "why", no true/false in the samples.

**The ten distractor molds** (7 from the practice-test explanations, 3 from your own miss record):

| # | Mold | What it looks like | Tell |
|---|---|---|---|
| 1 | SYMPTOM | Fix downstream (post-process, dedupe after, regenerate, filter, remind) instead of at the source | The key is justified as "directly addresses the root cause" |
| 2 | FAKE | A flag/param/behaviour that does not exist: `--batch`, `CLAUDE_HEADLESS=true`, `override: true`, `session_id`, "Claude caches CLAUDE.md" | Plausible name, never in the docs |
| 3 | PROMPT-NOT-CODE | Instruction or few-shot offered where the requirement is a guarantee | "must always", "never without", "15% wrong account" → hook / gate / token / schema / `tool_choice` |
| 4 | OVERBUILD | Classifier, routing layer, extra model, vector DB, intermediate agent, shared-state layer | A lighter fix (description, example, partition, scope) exists |
| 5 | BIGGER-CONTEXT | Larger model / wider window / raise the threshold | Delays the same problem; attention quality unchanged |
| 6 | SILENT | Swallow errors, success with an error inside, hidden defaults, consensus voting to drop findings | Destroys the signal the system needs |
| 7 | BURDEN | Push the work to humans or upstream ("developers must split PRs", "customer must fill an intake form") | The system, not the person, should change |
| 8 | DISCARD ⚑ | Throw away a working mechanism (hook, session, tool) when a narrow adjustment fixes the side-effect | Exam 14 Q19/Q54 |
| 9 | OVERSPEC ⚑ | Force a *specific* mechanism when the requirement only needs *a* mechanism — `tool_choice: tool` where `any`/`auto` is right; forced on every turn | Exam 19 Q23, Exam 20 Q48 |
| 10 | EXAM≠DOCS | Current-docs truth offered against the guide's framing | Answer per the guide — see the Exam≠docs page |

Two more families that recur everywhere: **LOOKALIKE** (a Key-Distinction pair — 0 results vs timeout, Grep vs Glob, `any` vs forced) and **REVERSE** (the right pattern applied in the wrong direction — plan mode for a one-line fix, dynamic decomposition for a fixed template, composite where bundling suffices, or vice versa).

**The twelve tie-breakers.** Fix the root cause · proportionate first response · programmatic enforcement for critical sequences · least privilege · deterministic over probabilistic · structured error > generic failure · parallel + shared context > sequential · coordinator is the hub · independence for review · match API to latency · coverage gaps trace upstream · attention dilution → split passes.

**When two options both work:** take the one that fixes the signal at its source with the least new machinery — unless the stem asks for a guarantee, in which case take code (hook, gate, token, schema, `tool_choice`) over prompt.

**Out-of-scope = automatic distractor:** fine-tuning · auth/billing · MCP hosting/transport · model internals · RLHF · embeddings implementation · computer use · vision · streaming/SSE · rate limits · OAuth · cloud configs · benchmarks · prompt-caching internals · tokenizer details. An option that leans on any of these is not the key.

---

## Domain 1 · Agentic Architecture & Orchestration (27%)

### D1-01 · The loop terminates on `stop_reason`, nothing else
§1.1 · KD 5
**Rule.** The orchestrator reads `stop_reason` after every call — `end_turn` ends the loop, `tool_use` continues it; text content and iteration counts are not the signal.
**Asked**
- [CAUSE] Loop never terminates, or stops mid-task; the code looks for "I'm done" or a hard cap → termination keyed on text or count.
- [WHICH] "What determines when to stop?" → `stop_reason == "end_turn"`.
- [REVERSE] `stop_reason: max_tokens` → not done; handle/continue, don't return a truncated answer as final.
**Traps**
- ✗ Parse assistant text for a completion phrase `[FAKE mechanism]`.
- ✗ Stop after N iterations — a cap is a safety net, not the exit `[SYMPTOM]`.
- ✗ Treat `max_tokens` as `end_turn` `[LOOKALIKE]`.
- ✗ "There are exactly four `stop_reason` values" — current docs add `pause_turn`, `refusal`, `model_context_window_exceeded`; only `tool_use` vs `end_turn` is scored `[EXAM≠DOCS]`.

### D1-02 · `tool_use` → execute → append `tool_result` → call again
§1.1 · §2.1
**Rule.** On `tool_use`, the application executes the tool, appends a `tool_result` block matched to the call's `id`, and sends the full history back; Claude never runs the tool itself.
**Asked**
- [HOW] Order the steps of one tool round-trip.
- [WHICH] Which field links a result to its call → the `tool_use` block's `id` (`tool_use_id` on the result).
- [CAUSE] Model keeps re-requesting the same tool → the result was never appended.
**Traps**
- ✗ Match results by tool name `[wrong key]`.
- ✗ Expect Claude to execute the tool `[FAKE]`.
- ✗ Drop the result and re-prompt `[SILENT]`.

### D1-03 · Hub-and-spoke — subagents never talk to each other
§1.2 · KD 6
**Rule.** All inter-agent communication routes through the coordinator, which gives visibility, uniform error handling, and control over what each subagent sees.
**Asked**
- [WHICH] Proposal to let subagents message each other to save hops → reject.
- [CAUSE] Coordinator "can't see" why a downstream agent produced X → direct inter-agent traffic bypassed it.
**Traps**
- ✗ Direct inter-agent messaging "for efficiency" `[REVERSE — breaks the hub]`.
- ✗ Shared blackboard/state layer between subagents `[OVERBUILD]`.

### D1-04 · Subagents start empty — pass context explicitly
§1.2 · §5.6
**Rule.** A subagent sees only what its prompt contains; it inherits nothing from the coordinator's history or from sibling agents.
**Asked**
- [CAUSE] Synthesis agent doesn't know what web-search found → the coordinator never put those results in its prompt.
- [FIX] → include the complete upstream findings in the subagent prompt (see D1-11).
**Traps**
- ✗ Assume shared memory or inherited history `[FAKE]`.
- ✗ Tell the subagent to "refer to earlier findings" `[it has none — PROMPT-NOT-CODE]`.

### D1-05 · The `Task` tool spawns subagents; several in one response run in parallel
§1.2 · §1.15
**Rule.** Subagents are spawned via `Task`; multiple `Task` calls emitted in a single coordinator response execute in parallel, one per turn runs them sequentially.
**Asked**
- [HOW] Make three investigations run concurrently → emit all three `Task` calls in one response.
- [CAUSE] "My parallel subagents ran one after another" → issued across separate turns.
**Traps**
- ✗ Sequential calls labelled "parallel" `[mechanic misread]`.
- ✗ Name game: current SDK calls it `Agent` (renamed in Claude Code v2.1.63); the guide says `Task` — never let the name decide `[EXAM≠DOCS]`.

### D1-06 · `AgentDefinition` — description, system prompt, tool restrictions
§1.3
**Rule.** A subagent type is its `description` (what it is for, read by orchestration), `system_prompt` (how it behaves) and `allowed_tools` (what it may touch).
**Asked**
- [WHICH] Which lever enforces least privilege per type → `allowed_tools`; which tells orchestration the type's purpose → `description`.
- [REVERSE] "Give every type the full tool set for flexibility" → wrong; restriction is the separation mechanism.
**Traps**
- ✗ Full catalogue everywhere `[REVERSE of least privilege]`.
- ✗ Conflate `allowed_tools` (SDK AgentDefinition) with `allowed-tools` (SKILL.md frontmatter, D3-10) `[LOOKALIKE]`.

### D1-07 · The coordinator's `allowedTools` must include `Task`
§1.3
**Rule.** Without `"Task"` in its `allowedTools` a coordinator physically cannot spawn subagents — a binary gate, not a preference.
**Asked**
- [CAUSE/FIX] Coordinator attempts everything itself, never delegates → check `Task` in `allowedTools`.
**Traps**
- ✗ Rewrite the coordinator prompt to "delegate more" `[PROMPT-NOT-CODE — a prompt can't grant a tool]`.
- ✗ Add subagent descriptions to the coordinator's system prompt `[FAKE mechanism]`.
- ✗ An option that turns on `Task` vs `Agent` spelling `[EXAM≠DOCS — expect `Task`]`.

### D1-08 · Coordinator prompts state goals and quality criteria, not procedures
§1.4
**Rule.** A goal-oriented coordinator prompt (goal + what good looks like) lets subagents adapt as findings emerge; a step-by-step script is brittle.
**Asked**
- [FIX] Research output is shallow and checklist-like → rewrite to goals + quality criteria (≥3 sources per claim; cover production, distribution, composition).
- [WHICH] Which style lets subagents adapt → goal-oriented.
- [REVERSE] A review that must follow the same template every run → that is D1-15's fixed pipeline, not a reason to script the *research* coordinator.
**Traps**
- ✗ Add more detailed steps `[SYMPTOM — deepens rigidity]`.
- ✗ Add more subagents `[OVERBUILD]`.
- ✗ Confuse goal-oriented prompting with dynamic decomposition (D1-15) `[same principle, different level]`.

### D1-09 · Content and metadata travel in separate structured fields
§1.5 · §5.11
**Rule.** Findings pass between agents as structured data with content and metadata (source URL, document, page, date) in separate fields so attribution survives aggregation.
**Asked**
- [CAUSE] Final report has wrong or missing citations → content and metadata were merged as free text.
- [FIX] → structured content/metadata format required from every subagent and preserved downstream.
**Traps**
- ✗ "Remember to cite sources" instruction `[PROMPT-NOT-CODE — it never received the metadata]`.
- ✗ Re-search the web at the end for sources `[SYMPTOM, mis-attributes]`.
- ✗ Bibliography at the end `[claims no longer traceable]`.

### D1-10 · Pass complete upstream findings into the next agent's prompt
§1.5
**Rule.** The synthesis subagent's prompt must carry the full web-search and document-analysis outputs — not a pointer, not a summary of a summary.
**Asked**
- [FIX] Synthesis is generic and misses specifics the searchers found → the coordinator passed a précis, not the findings.
**Traps**
- ✗ Give the synthesis agent search tools to "look things up itself" `[least privilege broken, D1-25]`.
- ✗ Rely on a shared context that does not exist `[FAKE]`.

### D1-11 · Conflicting statistics — keep both, attribute, annotate
§1.5 · §5.10
**Rule.** When two credible sources disagree, the agent completes its analysis with both values, marks the conflict with attribution, and lets the coordinator or a human reconcile.
**Asked**
- [HOW] Government report says 40%, industry analysis 12% → both + annotation; don't pick, don't stop.
**Traps**
- ✗ Heuristic pick of the "more likely" value `[SILENT]`.
- ✗ Stop and ask the coordinator before completing `[blocks the pipeline]`.
- ✗ Report a contradiction when the dates differ (see D5-19) `[missing dates]`.

### D1-12 · Narrow decomposition — the coordinator, not the subagents
§1.6 · KD 7
**Rule.** If every subagent succeeds and the answer still covers the wrong ground, the coordinator decomposed too narrowly; fix the coordinator prompt.
**Asked**
- [CAUSE] "AI's impact on creative industries" returns only visual art; all subagents ran correctly → decomposition too narrow.
- [WHERE] Where does the fix live → coordinator prompt.
**Traps**
- ✗ Blame web-search query quality / synthesis gap detection / document filters `[wrong layer]`.
- ✗ Add more subagents `[OVERBUILD]`.

### D1-13 · Partition the research space before delegating
§1.6
**Rule.** The coordinator assigns distinct subtopics or source types up front so subagents neither duplicate nor miss coverage.
**Asked**
- [FIX] Two agents research the same subtopics → partition before delegating.
**Traps**
- ✗ Deduplicate after the fact `[SYMPTOM]`.
- ✗ Let each subagent "choose its own angle" `[no partition]`.

### D1-14 · Fixed pipeline vs dynamic adaptive decomposition
§1.7 · §4.14
**Rule.** Predictable structure → fixed sequential pipeline (prompt chaining); open-ended investigation whose scope is unknown → adaptive decomposition where subtasks come from what each step finds.
**Asked**
- [WHICH] "Add comprehensive tests to a legacy codebase" → adaptive.
- [WHICH] "A review that always follows the same template" → fixed pipeline.
- [REVERSE] Predictable extraction pipeline offered "adaptive planning" → unnecessary complexity.
**Traps**
- ✗ Fixed script for the open-ended task `[can't react to discoveries]`.
- ✗ Dynamic decomposition for a fixed template `[OVERBUILD]`.
- ✗ One giant single-pass prompt `[dilution]`.

### D1-15 · Adaptive investigation: map → prioritise → adapt
§1.7
**Rule.** For open-ended codebase work, first map the structure (Glob, Grep), identify high-impact areas, make a prioritised plan, and adapt it as dependencies (mocks, external APIs) surface.
**Asked**
- [WHICH] First step for "add tests to a legacy codebase" → map the structure, not start writing tests.
- [HOW] A dependency on an external API is discovered mid-way → add a mock before continuing; the plan adapts.
**Traps**
- ✗ Write tests module by module in alphabetical order `[no prioritisation]`.
- ✗ Read every file first (D2-25) `[bulk-read anti-pattern]`.

### D1-16 · Large PR review — per-file passes plus an integration pass
§1.7 · §4.12 · KD 17
**Rule.** A single pass over 10+ files dilutes attention (deep on some, shallow on others, contradictory comments); split into per-file passes for local issues plus a separate cross-file integration pass.
**Asked**
- [FIX] 14-file PR: detailed on some files, shallow on others, same pattern flagged in one file and approved in another → per-file + integration.
- [CAUSE] "Why inconsistent?" → attention dilution, not model capability.
**Traps**
- ✗ Larger model / bigger context window `[BIGGER-CONTEXT — attention quality unchanged]`.
- ✗ "Require developers to split large PRs" `[BURDEN]`.
- ✗ Ask for "more thorough" review `[abstract instruction]`.

### D1-17 · The coordinator's iterative refinement loop
§1.8
**Rule.** The coordinator evaluates the synthesis for gaps, re-delegates targeted queries to search/analysis, re-invokes synthesis, and stops when its quality criteria are met — it owns gap evaluation and termination.
**Asked**
- [HOW] Synthesis has coverage gaps and the sources are still reachable → refinement loop.
- [WHICH] Who decides "sufficient" → the coordinator, against the criteria from D1-08.
- [LOOKALIKE] Gap is unrecoverable (source down) → coverage annotation (D1-21), not another loop.
**Traps**
- ✗ Synthesis agent searches the web itself `[least privilege]`.
- ✗ Ship with "further research needed" while re-delegation is available `[SILENT-ish]`.
- ✗ Loop with no sufficiency criterion `[never terminates]`.

### D1-18 · Structured error context, not a generic failure
§1.9 · KD 8
**Rule.** A failing subagent returns failure type, what was attempted, partial results, and alternatives, so the coordinator can retry, reroute, continue with partials, or escalate.
**Asked**
- [CAUSE] Coordinator can't decide retry vs skip vs continue → it received "search unavailable".
- [WHICH] What the payload must contain → the four fields.
**Traps**
- ✗ Generic failure status `[SILENT]`.
- ✗ Silence / catch-and-return-success `[SILENT]`.
- ✗ Terminate the whole workflow on one failure `[over-reaction]`.

### D1-19 · Transient vs permanent vs valid-empty
§1.9 · §2.3 · KD 9
**Rule.** Transient (timeout, network) → retry with backoff; permanent (syntax, auth) → don't retry, log, continue; "0 results" is a valid finding, not an error.
**Asked**
- [WHICH] Patent DB timeout vs "0 results" from industry reports → retry-decision vs accept as finding.
- [CAUSE] Agent keeps retrying a malformed query → permanent error treated as transient.
**Traps**
- ✗ Treat empty results as failure and retry `[LOOKALIKE]`.
- ✗ Retry a syntax/permission error `[wrong category]`.
- ✗ Report "no data found" when the source was unreachable `[SILENT, D2-12]`.

### D1-20 · Handle errors at the right level
§1.9 · §2.3
**Rule.** Transient failures the subagent (or tool) can resolve are handled there with retry + backoff; only what it cannot resolve is escalated to the coordinator, with context and partial progress.
**Asked**
- [WHERE] Where to retry a timeout → inside the subagent/tool, before surfacing.
- [WHICH] What reaches the coordinator → decisions only it can make.
**Traps**
- ✗ Escalate every transient `[wrong level]`.
- ✗ Swallow permanent errors locally `[SILENT]`.

### D1-21 · Coverage annotations when inputs are incomplete
§1.10
**Rule.** With partial upstream data, synthesise from what arrived, mark which conclusions are well-supported and where the gaps are, and propagate the uncertainty upward.
**Asked**
- [HOW] Web search returned 3 of 5 source categories → annotated output.
- [LOOKALIKE] Missing categories still fetchable → D1-17 loop first.
**Traps**
- ✗ Return an error because input is incomplete `[blocks]`.
- ✗ Proceed without noting gaps `[SILENT]`.
- ✗ Block on the coordinator for every gap (D4-30) `[over-asking]`.

### D1-22 · Scoped cross-role tool for a high-frequency simple need
§1.11 · §2.5
**Rule.** When an agent needs another role's capability constantly for simple cases, give it a narrowly scoped tool (`verify_fact`) and route the complex cases through the coordinator.
**Asked**
- [FIX] Synthesis agent needs 85% simple fact checks, 15% complex → scoped `verify_fact`; complex via coordinator.
- [REVERSE] "Route every check through the coordinator" → correct scoping, wrong cost.
**Traps**
- ✗ Full `web_search` to the synthesis agent `[scope creep]`.
- ✗ Batch all verification to the end `[blocking]`.

### D1-23 · Replace a misused generic tool with a constrained one
§1.11 · §2.5
**Rule.** A generic tool that gets misused (`fetch_url` used for web search) is replaced by a constrained alternative (`load_document` that validates document URLs) — the boundary is enforced at the interface.
**Asked**
- [FIX] Document-analysis agent starts downloading search-result pages → `load_document`.
**Traps**
- ✗ Prompt "don't use `fetch_url` for search" `[PROMPT-NOT-CODE]`.
- ✗ Block known search-engine domains `[fragile]`.

### D1-24 · When to escalate — policy gap, explicit request, no progress, high stakes
§1.12 · §5.8
**Rule.** Escalate when the policy is silent or ambiguous, the user asks for a human, retries have failed, or a wrong call would do real harm — and not otherwise.
**Asked**
- [WHICH] Competitor price-match request; policy covers own-site drops only → escalate.
- [WHICH] "Which situation most justifies escalation?" → the policy-silent one, not the angry one.
- [REVERSE] Policy covers it, ambiguity resolvable by asking (D5-15) → resolve.
**Traps**
- ✗ Apply own-site rules to competitors / refuse citing an unwritten rule `[invented policy]`.
- ✗ Escalate on sentiment `[unreliable proxy]`.
- ✗ Escalate a resolvable multiple-match ambiguity `[REVERSE]`.

### D1-25 · Least privilege per subagent (the principle)
§1.11 · §2.5
**Rule.** Each agent gets only the tools its scope needs; broader tool sets cause scope creep and misuse (a synthesis agent doing open-ended research).
**Asked**
- [WHICH] Which agent should hold `web_search` → the research agents, not synthesis.
**Traps**
- ✗ "Full toolset for flexibility" `[REVERSE]`.
- ✗ Confuse least privilege (what it can *call*) with context isolation (what it can *see*) `[LOOKALIKE]`.

### D1-26 · Structured handoff — the human has no transcript
§1.13
**Rule.** An escalation carries a self-contained summary — customer ID, root cause, amount, actions taken, recommended action, escalation reason — because the human agent cannot see the conversation.
**Asked**
- [CAUSE/FIX] Human agents keep re-asking customers for what the AI collected → the escalation passed a flag or a note; send the structured handoff.
- [WHICH] Fields the exam names → customer ID, root cause, amount, recommended action.
**Traps**
- ✗ Give humans the raw transcript `[no access by design; re-reading everything]`.
- ✗ Have the human re-run the tools `[duplicate work]`.
- ✗ Escalate earlier so less context accumulates `[fixes nothing]`.

### D1-27 · Critical sequencing → programmatic preconditions
§1.14 · KD 11
**Rule.** When an order must hold (identity before action), enforce it in code — a gate or `PreToolUse` hook — because prompt compliance is probabilistic.
**Asked**
- [FIX] Agent skips `get_customer`, calls `lookup_order` with the customer-supplied number; wrong account 15% → block `lookup_order` until `get_customer` returns a verified identifier.
- [REVERSE] Ordinary non-critical guidance → the prompt is fine.
**Traps**
- ✗ "Always call `get_customer` first" in the prompt `[PROMPT-NOT-CODE]`.
- ✗ Few-shot of the right order `[PROMPT-NOT-CODE]`.
- ✗ Orchestration-layer confirmation prompt `[OVERBUILD]`.

### D1-28 · Multi-issue request → decompose, parallelise with shared context, synthesise once
§1.15
**Rule.** A message with several issues is split into items, investigated in parallel with the shared customer context, and answered in one synthesis.
**Asked**
- [HOW] Charged twice + discount missing + cancel order → three parallel investigations, one answer.
**Traps**
- ✗ Sequential investigation `[tool-call bloat]`.
- ✗ Parallel without shared context `[redundant fetching]`.
- ✗ Shared-state mechanism `[OVERBUILD]`.

### D1-29 · `--resume <name>` — and tell it which files changed
§1.16 · §3.12
**Rule.** Resume a named session when its context is still mostly valid; after code changes, name the changed files so it re-analyses only those.
**Asked**
- [HOW] Yesterday's analysis; three files refactored today → resume and name the three files.
- [WHICH] Flag recall: `--resume` / `-r`; `--continue` / `-c` is "most recent".
**Traps**
- ✗ Resume as-is `[stale evidence]`.
- ✗ Always start over `[waste]`.
- ✗ Discard a resumable session when a targeted note would do ⚑ `[DISCARD — Exam 14 Q19/Q54]`.

### D1-30 · `fork_session` — compare approaches from a shared baseline
§1.16 · §3.12
**Rule.** Fork one analysed session into independent branches that inherit context up to the branch point, so two approaches are evaluated without re-analysis and without contaminating each other.
**Asked**
- [WHICH] Evaluate two refactoring strategies from one completed analysis → `fork_session` (CLI `--fork-session`).
**Traps**
- ✗ Run both strategies in one session `[second biased by the first]`.
- ✗ Two brand-new sessions `[baseline redone twice]`.

### D1-31 · Fresh session + injected summary when tool results are stale
§1.16 · §3.12
**Rule.** When files changed heavily, much time passed, or context degraded, start a new session with a structured summary of prior conclusions — carrying the conclusions without the stale evidence.
**Asked**
- [WHICH] Resume vs fresh → mostly-valid context resumes; stale results start fresh with a summary.
**Traps**
- ✗ Resume with stale results "to save time" `[reasons over old evidence]`.
- ✗ Fresh session with no summary `[redoes everything]`.

### D1-32 · Independent review needs a separate instance
§1.17 · §4.13 · §3.8
**Rule.** A second instance that never sees the generator's reasoning catches what the generator rationalised away; a second pass in the same conversation is not independent.
**Asked**
- [FIX] Generated code passes its own edge-case check; bugs found only in PR review → independent reviewer instance.
- [WHICH] Extended thinking on the generator? → same anchored instance.
- [WHICH] The CI session that wrote the code reviews it → weak reviewer; use an independent instance.
**Traps**
- ✗ "Review your own work carefully" `[same context]`.
- ✗ Extended thinking `[more of the same reasoning]`.
- ✗ Second pass in the same conversation `[not independent]`.
- ✗ Report only findings seen in ≥2 runs `[SILENT — suppresses signal]`.

### D1-33 · Name the pattern
§1.18
**Rule.** The named patterns: hub-and-spoke · agentic loop · parallel execution · context isolation · evaluator-optimizer · structured error propagation · coverage annotation · least-privilege tooling · goal-oriented delegation · content/metadata separation · prompt chaining · dynamic adaptive decomposition · iterative refinement loop · structured handoff · session forking · fresh-plus-summary.
**Asked**
- [WHICH] A one-paragraph description → its name, or the reverse.
**Traps**
- ✗ Evaluator-optimizer confused with prompt chaining `[critic stage vs sequential stages]`.
- ✗ Context isolation confused with least privilege `[sees vs calls]`.

---

## Domain 2 · Tool Design & MCP Integration (18%)

### D2-01 · The three `tool_choice` values and what each guarantees
§2.1 · §2.5 · §4.6
**Rule.** `auto` (default) guarantees nothing — the model may answer in text; `any` guarantees some tool will be called; `{"type":"tool","name":…}` guarantees that specific tool.
**Asked**
- [WHICH] What does `auto` guarantee → nothing.
- [WHICH] `any` with three extraction tools → the model still picks the best-fitting one; output is always structured.
**Traps**
- ✗ `{"type":"none"}` as the key — exists in current docs; the guide's task 2.3 names only auto/any/forced `[EXAM≠DOCS]`.
- ✗ `auto` + "you must use a tool" in the prompt `[PROMPT-NOT-CODE]`.

### D2-02 · Tool description quality — purpose, inputs, when, when-not
§2.2 · KD 10
**Rule.** Descriptions are the primary input for tool selection; a good one states purpose, accepted input formats with examples, when to use it versus similar tools, and boundary cases; misrouting → check descriptions first.
**Asked**
- [FIX] `get_customer` and `lookup_order` have 1-line descriptions and similar ID formats; `get_customer` called for order queries → expand both with formats, examples, edge cases, boundaries.
- [WHICH] "What should you check first when routing goes wrong?" → the descriptions.
**Traps**
- ✗ Merge into one `lookup_entity` `[loses precision]`.
- ✗ Pre-routing classifier `[OVERBUILD]`.
- ✗ Few-shot before descriptions are fixed ⚑ `[wrong lever first — Exam 19 Q53]`.

### D2-03 · Near-identical tool names → rename and differentiate
§2.2 · KD 10
**Rule.** `analyze_content` (web) vs `analyze_document` (docs) misroute because names and descriptions overlap; rename (`extract_web_results`) and rewrite each for a distinct purpose.
**Asked**
- [FIX] "Analyze the uploaded quarterly report" routed to the web-search agent 45% of the time → rename + rewrite.
**Traps**
- ✗ Add a routing layer `[OVERBUILD]`.
- ✗ Add more tools `[more overlap]`.

### D2-04 · Keyword-bound system-prompt wording overrides good descriptions
§2.2
**Rule.** A phrase in the system prompt can bind a tool to a keyword; when selection is wrong despite good descriptions, review the prompt.
**Asked**
- [CAUSE] Descriptions are fine, routing still wrong for one phrasing → keyword binding in the system prompt.
**Traps**
- ✗ Rewrite descriptions again `[wrong layer]`.
- ✗ "Always prefer X" rules `[blunt, keyword-sensitive]`.

### D2-05 · `isError` plus structured error metadata
§2.3 · KD 8
**Rule.** A tool error returns `isError: true` with `errorCategory`, `isRetryable`, a readable description, partial results and alternatives — never a bare "failed".
**Asked**
- [FIX] Agent can't tell a policy denial from an outage → structured error payload.
- [WHICH] Rank: handle transient internally > return a `retryable` flag > make the agent guess from text.
**Traps**
- ✗ Generic "Operation failed" `[SILENT]`.
- ✗ Success payload with embedded error `[SILENT]`.

### D2-06 · The four error categories and the four responses
§2.3 · KD 9
**Rule.** Transient → retry (inside the tool first); validation → fix the input and re-call; business → explain the policy outcome, never retry; permission → escalate or switch credentials.
**Asked**
- [WHICH] Timeout / malformed ID / refund over policy limit / access denied → four different moves.
**Traps**
- ✗ Business error tagged transient `[wasted retries]`.
- ✗ Retry a permission error `[wasted]`.

### D2-07 · Business-rule errors — `retriable: false` and a customer-friendly explanation
§2.3
**Rule.** A policy violation is a valid answer that the action is disallowed, not a tool failure; return `retriable: false` with an explanation the agent can relay.
**Asked**
- [FIX] `process_refund` rejects (outside the 30-day window) and the agent keeps retrying → `retriable: false` + "Refunds are available within 30 days…".
**Traps**
- ✗ Generic failure `[agent retries or escalates wrongly]`.
- ✗ `isRetryable: true` `[can never succeed]`.

### D2-08 · Empty result ≠ access failure
§2.3 · KD 9
**Rule.** A query that ran and found nothing is a success with an empty result (`isError` absent/false); a query that could not run is `isError: true` with a category; conflating them corrupts decisions in both directions.
**Asked**
- [WHICH] Customer genuinely has no orders → `{"results": [], "isError": false}`; DB down → `isError: true`.
- [CAUSE] Agent tells customers "you have no orders" during an outage → access failure masked as an empty list.
**Traps**
- ✗ `isError: true` for zero matches `[agent retries a good query]`.
- ✗ Empty list on connection failure `[false statement to the customer]`.

### D2-09 · Two-tool token binding
§2.4 · KD 12
**Rule.** `preview_*` returns the impact and a single-use token; `execute_*` requires that token; skipping the preview becomes architecturally impossible.
**Asked**
- [FIX] `dry_run: false` called directly on first attempt → preview + execute bound by a token.
- [WHICH] What property makes the guarantee hold → the token exists only after a preview, is single-use, server-issued, unguessable.
- [LOOKALIKE] Token binding vs `PreToolUse` hook → token when a preview must have happened; hook when a threshold must block; both are code-level.
**Traps**
- ✗ Server-side timing heuristic `[fragile]`.
- ✗ Orchestration-layer confirmation prompt `[OVERBUILD]`.
- ✗ Prompt + examples `[PROMPT-NOT-CODE]`.
- ✗ Reusable or guessable token `[guarantee leaks]`.

### D2-10 · Too many tools degrades selection — 4–5 per role, not 18
§2.5
**Rule.** Every extra tool is another candidate to discriminate on every turn; the guide's own numbers are 4–5 role-scoped tools versus 18.
**Asked**
- [FIX] Subagent with 18 tools misfires; peer with 5 selects correctly → restrict to the role's 4–5.
**Traps**
- ✗ Keep 18 and write better descriptions for all `[count is the root cause]`.
- ✗ Full catalogue "for flexibility" `[misuse outside specialisation]`.

### D2-11 · `tool_choice: any` when the output must be structured
§2.5 · §4.6
**Rule.** `any` forces a tool call, so an extraction agent can never answer in prose; with several extraction tools the model still chooses the fitting one.
**Asked**
- [FIX] Extraction agent sometimes replies in prose → `{"type":"any"}`.
- [FIX] Documents may be invoices, receipts or contracts (three tools); output must always be schema-valid → `any`.
**Traps**
- ✗ `auto` + prompt instruction `[PROMPT-NOT-CODE]`.
- ✗ Forcing one named tool ⚑ `[OVERSPEC — Exam 19 Q23, Exam 20 Q48]`.

### D2-12 · Forced first step, then relax to `auto`
§2.5 · §4.6
**Rule.** To guarantee a specific first tool (`extract_metadata` before enrichment), force it on the first request only, then continue with `auto`/`any`.
**Asked**
- [FIX] Metadata must precede enrichment; prompt obeyed ~90% → force `extract_metadata` on call one, then `auto`.
**Traps**
- ✗ Forced on every turn — enrichment tools can never run `[OVERSPEC]`.
- ✗ `any` when a specific tool must run first `[LOOKALIKE — any ≠ that tool]`.
- ✗ "ALWAYS call extract_metadata first" in the prompt `[PROMPT-NOT-CODE]`.

### D2-13 · MCP primitives — tools act, resources are read, prompts are templates; all servers' tools available together
§2.6
**Rule.** Tools are callable actions, resources are read-only data, prompts are reusable templates; tools from every configured server are discovered at connection and available simultaneously.
**Asked**
- [WHICH] "Do multiple servers take turns?" → no.
- [WHICH] Which primitive for a schema the agent should be able to read → resource.
**Traps**
- ✗ Servers "activated one at a time" `[FAKE]`.
- ✗ A tool for something that should be a resource (see D2-16) `[LLM call + hope]`.

### D2-14 · `.mcp.json` (project, version-controlled) vs `~/.claude.json` (user)
§2.6 · KD 2
**Rule.** Team servers live in the repo's `.mcp.json`; personal or experimental servers in `~/.claude.json`.
**Asked**
- [WHERE] Server every teammate needs → `.mcp.json`; personal experiment → `~/.claude.json`.
**Traps**
- ✗ Each developer adds the shared server in user scope `[inconsistent tooling]`.
- ✗ Three-scope answer (local/project/user) — real in current docs; the exam frames two `[EXAM≠DOCS]`.

### D2-15 · `${ENV_VAR}` expansion keeps secrets out of the repo
§2.6 · KD 2
**Rule.** `.mcp.json` references `${GITHUB_TOKEN}`; each developer supplies their own value; the file stays version-controlled without credentials.
**Asked**
- [FIX] Team shares a server, each dev has a GitHub token → `.mcp.json` + `${GITHUB_TOKEN}`, documented in README.
**Traps**
- ✗ Commit a placeholder token `[secret in repo]`.
- ✗ Move the whole config to user scope "for the token" `[inconsistent]`.

### D2-16 · MCP resources as content catalogs
§2.6
**Rule.** A resource exposes an issue list, doc hierarchy or schema as readable context, giving the agent a map of what exists without exploratory tool calls.
**Asked**
- [FIX] Agent burns turns guessing `search_issues` queries to learn what exists → expose an issue catalog as a resource.
- [WHICH] Resource vs a `list_everything` tool on staleness, context cost, invocation reliability; "what can a resource not do" → act.
**Traps**
- ✗ `list_everything` tool the agent must remember to call `[LLM call + hope]`.
- ✗ Paste the catalog into the system prompt `[bloat, stale]`.

### D2-17 · Community servers for standard integrations, custom for team-specific workflows
§2.6
**Rule.** Jira, GitHub, Slack → existing community MCP servers; build custom only for workflows no server covers.
**Asked**
- [WHICH] Colleague proposes a custom Jira server "for control" → use the community server.
- [REVERSE] A genuinely team-specific workflow → custom is correct.
**Traps**
- ✗ Reinvent a maintained integration `[waste]`.
- ✗ Force a team-specific workflow onto an ill-fitting community server `[REVERSE]`.

### D2-18 · MCP tool losing to a built-in — fix its description
§2.6 · KD 29
**Rule.** Selection runs on descriptions, so an MCP tool whose description does not spell out what Grep cannot do loses to Grep; enrich the description with its unique capability and outputs.
**Asked**
- [FIX] Semantic, index-backed code search exists; agent keeps using Grep → richer MCP description.
**Traps**
- ✗ Remove or disable Grep `[DISCARD — breaks legitimate cases]`.
- ✗ "Always prefer MCP tools" rule `[blunt, misroutes]`.

### D2-19 · `PostToolUse` — normalise heterogeneous tool outputs centrally
§2.7
**Rule.** A `PostToolUse` hook rewrites Unix timestamps, ISO dates and numeric codes into one format before the model sees them — deterministic, one place.
**Asked**
- [FIX] Third-party tools return different formats you cannot change → `PostToolUse` normalisation.
**Traps**
- ✗ `normalize_data` tool the agent calls after each retrieval `[LLM overhead + hope]`.
- ✗ Document the formats in the system prompt `[PROMPT-NOT-CODE]`.
- ✗ Per-tool wrappers `[fragmented maintenance]`.

### D2-20 · `PreToolUse` — block above a threshold, redirect to escalation
§2.7 · §5.8
**Rule.** A `PreToolUse` hook fires before the call regardless of what the model wants; use it to block bulk deletion over 50 records or a refund over $500 and route to escalation.
**Asked**
- [FIX] Deletions above a threshold must never run → `PreToolUse` block + escalate.
- [WHICH] Which hook for the identity-before-refund gate → `PreToolUse` (D1-27); for trimming output → `PostToolUse` (D5-06).
**Traps**
- ✗ Threshold rule in the prompt `[PROMPT-NOT-CODE]`.
- ✗ Remove a hook because one consumer lost a field ⚑ `[DISCARD — Exam 14 Q19/Q54; widen the field list]`.

### D2-21 · Bundling vs composite tools ⚑ five-paper miss
§2.8 · ⚑ missed on Exams 5, 8, 10, 11, 14 — the oldest open trap
**Rule.** When two tools are habitually called in sequence, first prompt the agent to bundle the calls into one turn (several `tool_use` blocks in one response); a composite tool is the fallback because it hides the composition.
**Asked**
- [FIX] `get_customer` then `lookup_order` in separate turns on nearly every case → instruct bundling.
- [REVERSE] The team already built `get_customer_with_orders` and now sees a second-order cost → hidden composition, coupling, loss of independent reuse, one more description competing for selection.
- [WHICH] When is a composite justified → invariant sequence, atomicity/one transaction, or the composition must be enforced rather than hoped — the corpus's own preference can be the distractor when the stem demands a guarantee.
- [LOOKALIKE] Bundling (several tool calls, one turn) vs parallel subagents (several `Task` calls, one turn).
**Traps**
- ✗ Composite by default `[hides composition]`.
- ✗ Bundling when the stem asks for atomicity/enforcement `[REVERSE]`.
- ✗ A hook to force ordering when the only problem is latency `[OVERBUILD]`.

### D2-22 · Grep searches content, Glob matches paths
§2.9 · KD 26
**Rule.** Grep finds text inside files (function names, error strings, imports, call sites); Glob finds files by name or extension pattern (`**/*.test.tsx`).
**Asked**
- [WHICH] Every file referencing deprecated `formatDate` → Grep; all TypeScript test files → Glob.
- [WHICH] Run tests / git → Bash; load a file → Read; new file → Write.
**Traps**
- ✗ Glob `**/formatDate*` `[matches names, not contents]`.
- ✗ Grep for the word "test" `[matches prose, misses files]`.

### D2-23 · Edit needs a unique anchor — fall back to Read + Write
§2.9 · KD 27
**Rule.** Edit replaces via a unique text match and fails when the anchor appears more than once; the sanctioned fallback is Read the file, modify, Write it back.
**Asked**
- [FIX] Edit failed, anchor appears twice → Read + Write.
**Traps**
- ✗ Retry Edit with a shorter anchor `[more collisions, not fewer]`.
- ✗ `sed` via Bash `[bypasses the sanctioned fallback]`.

### D2-24 · Incremental investigation — Grep entry points, then Read
§2.9 · KD 28
**Rule.** Build understanding incrementally: Grep for entry points → Read them → Grep usages → Read consumers; never read the whole repository first.
**Asked**
- [HOW] Understand an unfamiliar codebase → Grep → Read → Grep → Read.
**Traps**
- ✗ Read every file first "for full context" `[burns context]`.
- ✗ Glob the whole tree and Read each match `[same anti-pattern]`.

### D2-25 · Wrapped and re-exported functions — collect every name first
§2.9
**Rule.** When a function is wrapped or re-exported under other names, first collect all exported names from the wrapper modules, then Grep for each.
**Asked**
- [HOW] Rename `calculateTax`, wrapped as `getTax` and re-exported from `index.ts` → collect names, Grep each.
**Traps**
- ✗ Grep only `calculateTax` and stop `[misses wrapper callers]`.

### D2-26 · Which hook / which mechanism — the deterministic-vs-probabilistic decision
§2.7 · §1.14 · KD 11
**Rule.** Hooks, gates, tokens, schemas and `tool_choice` are deterministic; prompts and examples are probabilistic; safety-critical enforcement uses the deterministic one.
**Asked**
- [WHICH] Given a requirement stated as a guarantee, pick the code-level mechanism; given general guidance, the prompt is proportionate.
**Traps**
- ✗ Prompt for a guarantee `[PROMPT-NOT-CODE]`.
- ✗ Hook for mere guidance `[OVERBUILD]`.

### D2-27 · Tool-use request anatomy — `name`, `description`, `input_schema`
§2.1
**Rule.** A tool definition is `name` + `description` + `input_schema` (JSON Schema); the response's `tool_use` block carries `id`, `name`, `input`.
**Asked**
- [WHICH] Where the output structure of an extraction "tool" is declared → its `input_schema` (D4-08).
**Traps**
- ✗ Put the schema in the description text `[not enforced]`.

### D2-28 · Descriptions vs few-shot — which lever first
§2.2 · §4.1 · ⚑ Exam 19 Q53
**Rule.** For tool selection, the description is the first lever; few-shot examples are for the residual ambiguous requests after descriptions are right.
**Asked**
- [WHICH] Misrouting with thin descriptions → fix descriptions; misrouting on genuinely ambiguous phrasings with good descriptions → 4–6 targeted examples (D4-02).
**Traps**
- ✗ Examples first, descriptions untouched ⚑ `[wrong lever]`.

---

## Domain 3 · Claude Code Configuration & Workflows (20%)

### D3-01 · CLAUDE.md levels — and they concatenate, they don't override
§3.1
**Rule.** User (`~/.claude/CLAUDE.md`), project (`CLAUDE.md` or `.claude/CLAUDE.md`), directory-level, and `.claude/rules/` all load; discovered files are concatenated into context; there is no override precedence between levels.
**Asked**
- [WHICH] "Does a subdirectory CLAUDE.md override the root?" → no; both are in context; resolve conflicts by editing.
- [WHICH] Which level applies to all of one user's projects → user level.
**Traps**
- ✗ "Lower level overrides higher" `[EXAM≠DOCS — not the key]`.
- ✗ `CLAUDE.local.md` / managed policy as the answer — real, outside the guide's levels `[EXAM≠DOCS]`.
- ✗ "Claude caches CLAUDE.md" / "learns per-user preferences" `[FAKE]`.

### D3-02 · Project config is shared; user config is personal
§3.1 · KD 1
**Rule.** Project-level files are version-controlled and reach every teammate; `~/.claude/CLAUDE.md` reaches only that developer.
**Asked**
- [CAUSE] Three developers follow "comprehensive error handling", the new fourth doesn't, same repo → the rule lives in their user files; move it to the project file.
**Traps**
- ✗ Repeat the instruction louder each session `[SYMPTOM]`.
- ✗ Put team conventions in the user file `[REVERSE]`.

### D3-03 · `@import` — modular CLAUDE.md
§3.1
**Rule.** `@path` (no space) pulls another file into the concatenated context; relative paths resolve against the importing file; each package's CLAUDE.md can import only the standards that apply to it.
**Asked**
- [HOW] Standards per package without one giant global file → per-package `@import`s.
- [EXAM≠DOCS] Nesting depth is contested (corpus 5, current docs 4, guide silent) — if forced, answer 5; syntax is the stable part.
**Traps**
- ✗ `include:` / `#import` syntax `[FAKE]`.
- ✗ One giant global file imported everywhere `[defeats the point]`.

### D3-04 · `/memory` — see what is actually loaded
§3.1 · §3.12
**Rule.** `/memory` lists the memory files loaded in the session; it is the first diagnostic when a rule works sometimes and not others.
**Asked**
- [HOW] Convention applies in some sessions, not others → `/memory` to see which files loaded.
**Traps**
- ✗ Rewrite the instruction `[SYMPTOM]`.
- ✗ Reinstall / clear cache `[FAKE cause]`.

### D3-05 · `.claude/rules/` — path-scoped conditional rules
§3.2 · KD 3
**Rule.** Markdown files with `paths:` YAML globs load only when Claude works on matching files — the trigger is the file path and nothing else.
**Asked**
- [FIX] React components / API handlers / DB models each have conventions; tests co-located → `rules/` with globs.
- [REVERSE] Convention that applies always → root CLAUDE.md; workflow guidance → a skill; missing context in CI → CLAUDE.md.
**Traps**
- ✗ Root CLAUDE.md under headings `[model inference, not path match]`.
- ✗ A CLAUDE.md in every subdirectory `[breaks when files are spread]`.
- ✗ ⚑ The `rules/` reflex — `rules/` as the answer to "where should this workflow live" or "what supplies the missing context" (six instances: Exams 12, 13, 17, 14×2).

### D3-06 · Organising a bloated CLAUDE.md
§3.11 · §3.2 · §3.1
**Rule.** Universal standards stay in CLAUDE.md (loads every session); workflow guidance (PR review, deploy, migrations) becomes skills (on demand); topic modularisation uses `.claude/rules/` per topic, or `@import` when the content should stay in the concatenated context.
**Asked**
- [FIX] 400+ lines mixing standards, PR checklist, deploy, migrations → keep standards, move workflows to skills.
- [FIX] 500+ lines hard to navigate → topic files under `rules/`, or `@import`.
- [WHICH] Every session / on invocation / on path match → CLAUDE.md / skill / rule.
**Traps**
- ✗ Move everything to skills `[standards would need invoking]`.
- ✗ Split workflow content into `rules/` ⚑ `[path-scoped, not workflow-scoped]`.

### D3-07 · Skills — `SKILL.md` frontmatter keys
§3.3
**Rule.** `.claude/skills/<name>/SKILL.md` frontmatter: `description` (menu text), `argument-hint` (prompts for required args), `context: fork`, `allowed-tools`.
**Asked**
- [WHICH] Which key prompts the user for arguments → `argument-hint`.
- [WHERE] Where a skill's tool scoping is configured → SKILL.md frontmatter, not `.mcp.json`, CLAUDE.md, or a `config.json` commands array.
**Traps**
- ✗ `config.json` commands array `[FAKE]`.
- ✗ Scoping in CLAUDE.md `[wrong file]`.

### D3-08 · `context: fork` — keep exploration out of the main window
§3.3 · KD 13
**Rule.** `context: fork` runs the skill in an isolated subagent context and returns a summary, so large output or rejected alternatives never pollute the main conversation; use it for discovery, analysis, exploration, brainstorming — implementation stays in main.
**Asked**
- [FIX] `/analyze-codebase` makes Claude lose the original task → `context: fork`.
- [FIX] `/explore-alternatives` — rejected approaches bleed into the implementation → `context: fork`.
**Traps**
- ✗ Switch to a faster model `[irrelevant]`; compress results `[loses analysis]`; split into two skills `[leak persists]`.
- ✗ `context: fork` for the implementation step `[REVERSE]`.

### D3-09 · `allowed-tools` in SKILL.md — the exam's scoping key
§3.3
**Rule.** To limit what a skill may do, set `allowed-tools` in its frontmatter (e.g. `[Write, Read]`); the exam frames it as restricting tool access during the skill.
**Asked**
- [WHERE] Limit a skill to safe file operations → `allowed-tools`.
- [EXAM≠DOCS] Current docs: `allowed-tools` is a permission pre-grant and `disallowed-tools` restricts; answer per the guide.
**Traps**
- ✗ `disallowed-tools` as the key `[EXAM≠DOCS]`.
- ✗ Scoping via `.mcp.json` `[wrong file]`.

### D3-10 · Custom slash commands — location and `$ARGUMENTS`
§3.4
**Rule.** `.claude/commands/` (project, version-controlled) vs `~/.claude/commands/` (personal); the text after the command name arrives as `$ARGUMENTS`; commands and skills are unified — both create `/name`.
**Asked**
- [WHERE] `/review` for everyone who clones → `.claude/commands/`.
- [WHICH] How the command receives its argument text → `$ARGUMENTS`.
**Traps**
- ✗ `~/.claude/commands/` for a team command `[personal scope]`.
- ✗ A registry/config array of commands `[FAKE]`.

### D3-11 · Personal skill customisation — two framings, your call
§3.5 · KD 4
**Rule.** Corpus / practice-test framing: a personal skill at `~/.claude/skills/commit/SKILL.md` with the same name overrides the project `/commit` for you. Official guide bullet (task 3.2, verbatim): "creating personal variants in `~/.claude/skills/` with different names to avoid affecting teammates."
**Asked**
- [HOW] Customise `/commit` without affecting teammates → a personal skill under `~/.claude/skills/` (both framings agree on the location).
- Posture if forced to choose between two personal-scope options that differ only by name: the guide's wording is "different names"; the practice-test key (source of the official samples) is same-name override. Decide before the sitting which you trust.
**Traps**
- ✗ Edit the project skill `[affects teammates]`.
- ✗ `override: true` frontmatter `[FAKE]`.

### D3-12 · Plan mode vs direct execution
§3.6
**Rule.** Plan mode (read-only exploration → plan → approval → execute) for large scope, architectural choices, multiple valid approaches, many files; direct execution for clear, routine, well-specified changes; decide up front.
**Asked**
- [WHICH] Monolith → microservices; Slack support with several integration options; 45-file migration → plan. Function with a clear I/O spec; one-file fix with a stack trace → direct.
- [WHICH] "Start direct and switch to plan when it gets hard" → wrong.
**Traps**
- ✗ Reactive switching `[rework]`.
- ✗ Plan mode for a routine one-liner `[OVERBUILD]`.
- ✗ "Plan mode executes with confirmation prompts" `[it is read-only]`.

### D3-13 · The interview pattern — have Claude ask you first
§3.7.1
**Rule.** For an underspecified brief in an unfamiliar domain, ask Claude to interview you before implementing; one interview turn replaces several correction cycles.
**Asked**
- [FIX] Caching layer in an unfamiliar domain; three versions each miss a different requirement → restart with "ask me what you need to know first".
- [LOOKALIKE] Interview (developer brief, non-obvious implications) vs proceed-with-assumptions (D4-30, end-user vague request) — opposite advice, different room.
**Traps**
- ✗ Keep iterating one missed requirement at a time `[slow, fixes disturb each other]`.
- ✗ "Interviewing wastes a turn" `[misconception]`.

### D3-14 · Test-driven iteration — tests first, feed the failures
§3.7.2
**Rule.** Write the tests first (behaviour, edge cases, performance) and iterate on concrete failures; a specific failing case with input and expected output is the fastest edge-case fix.
**Asked**
- [FIX] Null-handling bug described in prose, partial fixes → hand it a failing test with sample input + expected output.
**Traps**
- ✗ Re-describe the bug more emphatically `[prose stays ambiguous]`.
- ✗ Tests written after generation `[verification, not TDI]`.

### D3-15 · Two or three concrete input/output examples
§3.7.3
**Rule.** When a transformation described in prose is interpreted inconsistently, 2–3 concrete input→output pairs anchor format and decision logic; the model generalises the pattern.
**Asked**
- [FIX] Transformation output shape differs each run → 2–3 pairs.
**Traps**
- ✗ Lengthen the prose with more adjectives `[still ambiguous]`.
- ✗ "Examples make it copy instead of generalise" `[misconception]`.

### D3-16 · Batching feedback — interacting fixes together, independent fixes one at a time
§3.7.4 · ⚑ Exam 17; Exam 20 Q58
**Rule.** Fixes that affect each other go in one detailed message so Claude designs one coherent change; independent fixes go sequentially so each iteration is easy to verify — the axis is interaction, not count.
**Asked**
- [WHICH] Locking bug + retry bug that depends on it + unrelated typo → locking + retry together; typo separately or riding along.
**Traps**
- ✗ "Always one issue per message" ⚑ `[wrong axis]`.
- ✗ "Always everything in one message" ⚑ `[wrong axis]`.

### D3-17 · `-p` / `--print` for CI
§3.8 · KD 15
**Rule.** `claude -p "…"` processes the prompt, prints to stdout and exits; without it the pipeline waits for interactive input.
**Asked**
- [FIX] Pipeline hangs → `-p`.
**Traps**
- ✗ `--batch`, `CLAUDE_HEADLESS=true` `[FAKE]`.
- ✗ `stdin < /dev/null` `[workaround, not the documented approach]`.

### D3-18 · Re-runs — feed the prior findings, ask for new/unresolved only
§3.8
**Rule.** When a review re-runs after new commits, include the previous run's findings and instruct Claude to report only new or still-unaddressed issues.
**Asked**
- [FIX] Near-duplicate comments on every follow-up push → prior findings in context.
**Traps**
- ✗ Blank-slate re-run "for objectivity" `[re-litigates, floods]`.
- ✗ Report only findings seen in ≥2 runs `[SILENT]`.

### D3-19 · CLAUDE.md is how CI-invoked Claude gets project context
§3.8
**Rule.** Testing standards, fixture conventions and review criteria reach a CI run through CLAUDE.md; existing test files in context stop duplicate test suggestions.
**Asked**
- [WHICH] How does CI Claude know the fixture conventions → CLAUDE.md.
- [FIX] Suggested tests duplicate existing ones → include the test file (D4-29).
**Traps**
- ✗ Put conventions in the `-p` prompt string every run `[fragile, duplicated]`.
- ✗ Ask for fewer tests `[SYMPTOM]`.

### D3-20 · `--output-format json --json-schema` for machine-parseable results
§3.9
**Rule.** In print mode, `--output-format json` with `--json-schema schema.json` yields validated JSON downstream tools can parse.
**Asked**
- [FIX] Post each finding as an inline PR comment (path, line, severity, fix) → json + schema.
**Traps**
- ✗ "Output Format" section in CLAUDE.md `[not guaranteed]`; format instruction in the prompt `[variable]`; regex post-processing `[SYMPTOM]`.
- ✗ `--json` `[FAKE flag]`.

### D3-21 · `/compact` — what it risks, and when the Explore subagent is the answer instead
§3.12 · §5.6 · KD 22
**Rule.** `/compact` compresses context and can lose exact numbers, dates and specifics; when discovery output threatens the window before implementation, run discovery in an Explore subagent that returns a summary.
**Asked**
- [FIX] Discovery phase fills the window before implementation → Explore subagent.
- [WHICH] What `/compact` risks → exact values.
**Traps**
- ✗ `/compact` mid-task `[precision loss]`; several sessions with `--continue` `[coordination]`; bigger window `[BIGGER-CONTEXT]`.
- ✗ Abandon a working session for a fresh one when a targeted note would do ⚑ `[DISCARD]`.

---

## Domain 4 · Prompt Engineering & Structured Output (20%)

### D4-01 · Few-shot for format consistency — not more instructions
§4.1 · KD 16
**Rule.** When instructions already fail to produce a consistent format, 3–4 examples of the exact required format (issue, location, fix) work where more instruction text does not.
**Asked**
- [FIX] Automated review's feedback format inconsistent despite instructions → few-shot of the exact format.
**Traps**
- ✗ More detailed instructions `[already failing]`.
- ✗ Post-process the format `[SYMPTOM]`.

### D4-02 · Target the ambiguous cases — 4–6, not 10–15 clear ones
§4.1 · KD 18
**Rule.** Examples go where the model gets it wrong: 4–6 targeted at the ambiguous cases, each with a rationale for the choice.
**Asked**
- [FIX] "I need help with my recent purchase" misroutes between `get_customer` / `lookup_order` → 4–6 targeted examples with rationale.
**Traps**
- ✗ 10–15 clear examples `[don't touch the edge]`.
- ✗ Classifier `[OVERBUILD]`.
- ✗ Examples when thin descriptions are the root cause ⚑ `[D2-28]`.

### D4-03 · Reasoning cues for multi-step tasks only
§4.2
**Rule.** "Think step by step" helps multi-step reasoning, comparisons and staged transformations; it adds nothing to single-step tasks.
**Asked**
- [WHICH] Which task warrants a reasoning cue → the multi-stage one.
**Traps**
- ✗ Reasoning cue as the fix for a format problem `[wrong tool]`.
- ✗ Extended thinking as a substitute for independent review (D1-32) `[same instance]`.

### D4-04 · Persistent behaviour lives in the system prompt
§4.3
**Rule.** Tone, persona, conversation-wide rules and response-format requirements belong in the system prompt.
**Asked**
- [WHERE] Enthusiasm, reasoning transparency, clarifying-question rules → system prompt.
**Traps**
- ✗ First user message `[loses authority]`; environment variables `[no effect]`; first assistant message `[model deviates]`.
- ✗ Prefill (D4-05) for persistent rules `[per-response only]`.

### D4-05 · Prefill — suppress filler openings
§4.4
**Rule.** Seed the assistant turn with a direct opening so Claude continues from it instead of "Certainly!".
**Asked**
- [FIX] Users report repetitive "Certainly!" openings → prefill.
**Traps**
- ✗ Lower temperature `[randomness, not phrases]`; post-process greetings `[SYMPTOM]`; system-prompt instruction `[less reliable]`.

### D4-06 · Inject a real-time event by prefixing the next user message
§4.4
**Rule.** A webhook event during a live chat is prepended to the next user message ("Your package has shipped. Now: [message]").
**Asked**
- [FIX] Shipping webhook fires mid-session → prefix the next user message.
**Traps**
- ✗ Modify the system prompt `[rebuild session]`; synthetic user message `[breaks the dialogue]`.

### D4-07 · Required only when always present; nullable prevents fabrication
§4.5
**Rule.** A required, non-nullable field pushes the model to invent a value when the source lacks it; sometimes-absent fields are optional or nullable (`["string","null"]`) so the model can return `null`.
**Asked**
- [CAUSE/FIX] Model invents values for missing fields → required non-nullable; make nullable.
- [REVERSE ⚑] Prevention at the source (schema) beats repair after (validate + retry) — Exam 17/19 prevention-vs-repair.
**Traps**
- ✗ Make every field required "for completeness" `[fabrication]`.
- ✗ Retry to fill an absent field (D4-13) `[waste + fabrication]`.

### D4-08 · Enum + "other" + detail; "unclear"; per-field confidence
§4.5
**Rule.** Known values with possible new ones → `enum: [..., "other"]` with a `detail` field; when the model can't pick confidently → an `"unclear"` member beats a confident wrong category; a `field_confidence` float alongside each field supports routing.
**Asked**
- [WHICH ⚑] Which decision belongs where — schema (shape, requiredness, enums, nullability) · prompt (mapping messy input) · code (business rules) — Exam 19 Q35 select-2 schema-scope.
**Traps**
- ✗ Read `"unclear"` as low quality `[it is the honest signal]`.
- ✗ Closed enum with no escape `[forces a wrong pick]`.

### D4-09 · Format normalisation belongs in the prompt, shape in the schema
§4.5
**Rule.** When sources have inconsistent dates, currencies or informal measurements, the prompt states the normalisation rules; the schema constrains only the shape.
**Asked**
- [FIX] Mixed formats in source documents → normalisation rules in the prompt alongside a strict schema.
**Traps**
- ✗ Normalisation "in the schema" `[can't express it]`.
- ✗ Post-hoc normalisation code as the first fix `[SYMPTOM]`.

### D4-10 · `tool_use` with a schema is the structured-output guarantee
§4.6
**Rule.** A tool whose `input_schema` is the desired output shape makes the response schema-valid JSON with no syntax errors — no prose preambles, no fences, no missing braces.
**Asked**
- [FIX] Pipeline must always receive schema-valid JSON → define an extraction tool and read the `tool_use` input.
- [WHICH] "Schema compliance means the values are right?" → no (D4-11).
**Traps**
- ✗ "Respond only with valid JSON" in the prompt `[no guarantee]`.
- ✗ JSON-repair library `[SYMPTOM]`.
- ✗ "The schema guarantees correctness" `[shape ≠ meaning]`.

### D4-11 · Syntax errors vs semantic errors
§4.7
**Rule.** Schemas via `tool_use` eliminate the syntax class (malformed JSON, wrong types, missing required); semantic errors (wrong values, sums that don't add, wrong field, wrong category) need business-rule validation, cross-field checks, self-correction fields, sometimes humans.
**Asked**
- [WHICH] Parse failures dropped to zero; reconciliation still finds bad totals → expected; the remainder is semantic → validation + feedback loop.
**Traps**
- ✗ Tighten the schema `[can't check arithmetic]`.
- ✗ Revert to prompt JSON `[reintroduces syntax errors]`.
- ✗ "Validator passed = correct" `[structure only]`.

### D4-12 · Pydantic — validate in code, generate the schema from the model
§4.8
**Rule.** Validation lives in your code after receipt (types, requiredness, enums, plus business rules like `sum(line_items) == total`); validation errors become retry feedback; the Pydantic model generates the tool's JSON Schema so contract and validator never drift.
**Asked**
- [FIX] Hand-maintained schema and validator class drift → generate the schema from the model.
- [WHICH] "tool_use enforces the schema, so skip validation?" → no; semantics + defence in depth.
**Traps**
- ✗ Code-review checklist to keep both files in sync `[process patch]`.
- ✗ Business rules in the schema `[can't express them]`.

### D4-13 · Retry-with-feedback — what to send, and when it can't help
§4.9
**Rule.** Retry with the original document + the failed extraction + the specific error; this fixes format, structure and arithmetic; it cannot conjure information absent from the document or held elsewhere — there the fix is a nullable field and accepting `null`.
**Asked**
- [FIX] `purchase_order_number` fails on 40 documents that never had one → nullable, accept null, stop retrying.
- [WHICH] What goes in the retry request → the three things.
**Traps**
- ✗ Raise max retries 3 → 10 `[absent stays absent]`.
- ✗ Strengthen the feedback text `[can't conjure data]`.
- ✗ Keep the field required "for data quality" `[fabrication]`.
- ✗ "Retry always converges" `[misconception]`.

### D4-14 · `detected_pattern` — make failures and dismissals aggregable
§4.9
**Rule.** A `detected_pattern` field on each finding/extraction names the construct that triggered it, so dismissal rates and repeated validation failures can be grouped by pattern.
**Asked**
- [FIX] Findings frequently dismissed; team can't tell which types are noise → `detected_pattern`, dismissal rate per pattern.
**Traps**
- ✗ Free-text dismissal reason `[doesn't aggregate]`.

### D4-15 · Self-correction built into the schema — stated vs calculated + conflict flag
§4.10
**Rule.** Extract `stated_total`, have the model re-derive `calculated_total`, and set `conflict_detected` when they differ, so contradictions surface as data at extraction time.
**Asked**
- [FIX] Totals mismatch found weeks later in reconciliation → stated vs calculated + flag, route at extraction time.
- [WHICH] "Self-correction = ask 'are you sure?'" → no, structural.
**Traps**
- ✗ Monthly reconciliation `[weeks late]`; "be careful with totals" `[no mechanism]`; conversational are-you-sure `[optional, unmeasurable]`.

### D4-16 · Batch vs synchronous — match the API to latency tolerance
§4.11 · §3.10 · KD 14
**Rule.** Batch is 50% cheaper with up to 24h and no SLA; anything a human or pipeline is blocking on stays synchronous; overnight, weekly, nightly and bulk work goes to Batch.
**Asked**
- [WHICH] Pre-merge check → sync; overnight tech-debt / weekly audit / nightly tests / 10,000 documents → Batch.
**Traps**
- ✗ Batch a blocking check "for the discount" `[latency]`.
- ✗ Poll faster to make Batch interactive `[no SLA]`.

### D4-17 · `custom_id` is the join key — results arrive in any order
§4.11
**Rule.** Every batch request carries a meaningful unique `custom_id`; results are matched by it, never by position.
**Asked**
- [CAUSE] Results don't line up with inputs → matched by position.
**Traps**
- ✗ Rely on result order `[silent mis-join]`.

### D4-18 · Selective re-submission after partial failure
§4.11
**Rule.** Identify the failed items by `custom_id`, fix the cause (chunk the long documents), and re-submit only those.
**Asked**
- [HOW] 95 of 100 succeed, 5 hit context limits → re-submit the 5, chunked.
**Traps**
- ✗ Re-submit all 100 `[pays twice, duplicates]`.
- ✗ Re-submit the 5 unchanged `[same failure]`.

### D4-19 · SLA planning — budget the 24-hour worst case
§4.11
**Rule.** Submission deadline = downstream deadline − 24h; a recurring 30h-SLA pipeline submits in 4-hour windows.
**Asked**
- [HOW] Results needed within 30h → submit within 6h.
**Traps**
- ✗ Plan around "batches usually finish in an hour" `[no SLA]`.

### D4-20 · Sample-first — refine synchronously, then batch the volume
§4.11
**Rule.** Validate the prompt and schema on a small synchronous sample until it passes, then submit the full batch.
**Asked**
- [HOW] New extraction prompt before a 10,000-document batch → synchronous sample first.
**Traps**
- ✗ Iterate on the full batch `[each try costs a batch + 24h]`.

### D4-21 · Batch requests can define tools; they cannot pause mid-request ⚑
§4.11 · ⚑ Exam 20 Q42 + Q55
**Rule.** A batch request's params are a normal Messages call — tools and multi-turn history allowed — but each request is one shot: if the model returns `tool_use`, that request is complete; the client continues in a follow-up request. Guide wording: "does not support multi-turn tool calling within a single request."
**Asked**
- [WHICH] "Can a batch request define tools?" → yes. "Can it pause for a `tool_result`?" → no.
- [WHICH] Iterative code review that fetches related files via tools mid-analysis → not Batch (needs the interactive loop).
**Traps**
- ✗ "Batches can't use tools" ⚑ `[outdated]`.
- ✗ "The batch will wait while I answer the tool call" `[one shot]`.

### D4-22 · Confidence-calibrated routing of review findings
§4.13
**Rule.** The reviewing instance reports a confidence per finding; high-confidence findings auto-comment, low-confidence ones go to a human.
**Asked**
- [HOW] Route automated review findings → by reviewer confidence.
**Traps**
- ✗ Post everything `[trust erosion, D4-27]`; suppress everything below a bar silently `[SILENT]`.

### D4-23 · Escalation criteria with few-shot "escalate / resolve" examples
§4.15 · §5.8
**Rule.** Explicit escalation criteria in the system prompt with examples of "escalate when" and "resolve autonomously when" fix mis-calibrated escalation.
**Asked**
- [FIX] Agent escalates simple photo-proven replacements, handles complex policy exceptions itself; 55% FCR vs 80% → explicit criteria + examples.
**Traps**
- ✗ Self-confidence rating + threshold `[OVERBUILD, uncalibrated]`; separate classifier `[OVERBUILD]`; sentiment `[D5-14]`.

### D4-24 · Replace vague intent with testable criteria
§4.16
**Rule.** "Check that comments are accurate" becomes "flag a comment only when the behaviour it claims contradicts the code's actual behaviour"; severity gets explicit criteria with examples.
**Asked**
- [FIX] Review flags correct comments as wrong; severity inconsistent → concrete criteria.
**Traps**
- ✗ "Be more careful" / more adjectives `[still abstract]`; bigger model `[BIGGER-CONTEXT]`.

### D4-25 · Restore trust by disabling high-false-positive categories
§4.17
**Rule.** Temporarily disable the noisy categories (style, naming, docs) and keep the precise ones (security, performance) while prompts are fixed; noise in one category makes developers dismiss everything.
**Asked**
- [FIX] 52% style FP, 48% docs, 8% security, 18% performance; developers dismiss all → surgical disable.
**Traps**
- ✗ Show confidence scores `[still all shown]`; few-shot across all categories over weeks `[too slow]`; uniform strictness cut `[hurts precise categories]`.
- Watch stem constraints like "stakeholders rejected filtering before developers see findings" — then disabling is off the table and the key shifts.

### D4-26 · Include existing artefacts to avoid duplicates
§4.18 · §3.8
**Rule.** Claude can only avoid duplicating what it can see; put the existing test file (or prior findings) in context.
**Asked**
- [FIX] 6 of 10 suggested tests already exist → include the test file.
**Traps**
- ✗ Ask for 5 `[assumes ordering]`; keyword post-filter `[misses semantic dupes]`.

### D4-27 · Proceed with stated assumptions — don't ask 4+ questions
§4.19 · KD 19
**Rule.** For a vague end-user request, state reasonable assumptions and proceed, inviting corrections; 4+ questions cause 35–40% abandonment; hidden defaults confuse; this applies to subagents too.
**Asked**
- [HOW] "Can you help with the report?" → proceed with stated assumptions.
- [WHICH] Synthesis agent blocking on every gap → proceed and annotate.
- [LOOKALIKE] Interview pattern (D3-13) is for a developer's underspecified implementation brief — the stem tells you which room you are in.
**Traps**
- ✗ 4+ questions; one compound question `[same burden]`; hidden defaults `[SILENT]`.

### D4-28 · Behavioural drift — accumulated responses dilute the system prompt
§4.20 · KD 23
**Rule.** As assistant turns accumulate, the system prompt's influence dilutes and the model pattern-matches its own prior output; this happens at 2,500 tokens and is not overflow, and the system prompt does not apply "only once".
**Asked**
- [CAUSE] Generic advice by turn 7 at 2,500 tokens → drift by accumulation.
**Traps**
- ✗ Context overflow `[impossible at that size]`; "system prompt only applies to turn 1" `[false]`; bigger context `[BIGGER-CONTEXT]`.

### D4-29 · Drift fixes — few-shot over verbose rules; reminders at breakpoints; prefill
§4.20 · §5.13
**Rule.** Replace long abstract rule lists with few-shot demonstrations (they hold longer), inject user-role reminders at breakpoints for persistent constraints, prefill to suppress a specific pattern.
**Asked**
- [FIX] Tutor with a 2,800-token rule-heavy prompt ignores proficiency after 12 turns → few-shot demonstrations of proficiency adaptation.
- [WHICH] Reminders every 4–5 turns → symptom when the prompt itself is the problem.
**Traps**
- ✗ Periodic reminders as the primary fix `[SYMPTOM]`; more rules `[drift faster]`.

### D4-30 · Prompt chaining — sequential focused prompts
§4.14 · §1.7
**Rule.** Break a task into sequential prompts where each output feeds the next (identify issues → generate fixes) for focus and consistency; it is the fixed-pipeline pattern.
**Asked**
- [WHICH] Name the pattern; chaining vs adaptive (predictable vs open-ended, D1-14).
**Traps**
- ✗ Chaining for open-ended investigation `[REVERSE]`; one prompt for a multi-stage task `[dilution]`.

### D4-31 · Multi-pass review (same point as D1-16)
§4.12
**Rule.** Single-pass over many items → attention dilution; per-file pass + integration pass.
**Asked**
- [FIX] Inconsistent 14-file review → split passes.
**Traps**
- ✗ Larger model / bigger window `[BIGGER-CONTEXT]`.

---

## Domain 5 · Context Management & Reliability (15%)

### D5-01 · Stateless API — memory is the `messages` array
§5.1 · KD 25
**Rule.** Claude has no server-side memory; the application resends the whole conversation every call; without that, prior turns don't exist.
**Asked**
- [CAUSE] "I love jazz" forgotten two turns later → history not being sent.
**Traps**
- ✗ `session_id` `[FAKE]`; vector DB for ordinary memory `[OVERBUILD]`; context exceeded at 3 turns `[impossible]`.

### D5-02 · Cost and latency grow with conversation length
§5.1
**Rule.** Every request carries the full history, so more turns → more tokens → more cost and latency.
**Asked**
- [CAUSE] Latency and cost climb past 50 turns → the whole history rides along each call.
**Traps**
- ✗ Progressively longer responses / database slowness `[wrong cause]`.

### D5-03 · Lost in the middle — summary first, headings throughout
§5.2 · KD 20
**Rule.** Attention is strong at the start and end of long input and weak in the middle; put a key-findings summary first and use explicit section headings.
**Asked**
- [FIX] 75K input; first 15K and last 10K used, middle 50K missed → summary at the start + headings.
**Traps**
- ✗ Summarise everything under 20K `[loses findings]`; rotate which agent goes first `[pattern unchanged]`; bigger window `[BIGGER-CONTEXT]`.

### D5-04 · Upstream agents return structured facts, not verbose traces
§5.2
**Rule.** When combined subagent output is far larger than synthesis handles well, fix it at the source: key facts, quotes, citations, relevance scores instead of full pages and reasoning.
**Asked**
- [FIX] 155K combined output but synthesis works best under 50K → upstream structured output.
**Traps**
- ✗ Intermediate summarisation agent `[OVERBUILD, latency]`.

### D5-05 · Hybrid context management — extract, summarise, keep recent verbatim
§5.3 · §5.13
**Rule.** Extract critical facts into a verbatim structured block, summarise the general discussion, keep the recent turns verbatim.
**Asked**
- [FIX] 78K-token cooking session with allergies, scaled quantities, chatter → hybrid.
**Traps**
- ✗ Summarise the whole history `[allergy precision lost]`; keep only the last 20K `[early facts dropped]`.

### D5-06 · Case-facts block outside the summarised history
§5.4 · KD 21
**Rule.** IDs, amounts, dates and status live in a persistent case-facts block included in every prompt and updated whenever a fact appears; it survives compression.
**Asked**
- [FIX] "The 15% discount I mentioned" becomes "promotional pricing was discussed" → case-facts block.
**Traps**
- ✗ Raise the summarisation threshold `[delays]`; better summariser prompt `[still hopes]`; external storage + retrieval `[OVERBUILD]`.

### D5-07 · Trim verbose tool outputs with a `PostToolUse` hook
§5.5
**Rule.** A hook keeps only the relevant fields before results enter context; the tokens are never spent.
**Asked**
- [FIX] `lookup_order` returns 40+ fields, 5 matter, every turn → trim in a hook.
- [REVERSE ⚑] Hook deployed, a downstream consumer lost a needed field → widen the field list, don't remove the hook.
- [WHICH] Trim vs `/compact` vs summarise for tool clutter → trim at the source.
**Traps**
- ✗ "Ignore irrelevant fields" prompt `[tokens still spent]`; more aggressive summarisation `[SYMPTOM]`; bigger model `[BIGGER-CONTEXT]`; remove the hook ⚑ `[DISCARD]`.

### D5-08 · Explore subagent isolates verbose discovery
§5.6 · KD 22
**Rule.** Context isolation is a feature: an Explore subagent absorbs hundreds of call sites and returns a summary, keeping the main session for design and implementation.
**Asked**
- [FIX] Discovery over 120 files fills the window before implementation → Explore subagent.
**Traps**
- ✗ `/compact` `[precision]`; several sessions with `--continue` `[coordination]`.

### D5-09 · Months of history → semantic retrieval
§5.7 · KD 24
**Rule.** For specific recall across months (85K tokens, many sessions), retrieve relevant past exchanges with embeddings; rolling windows lose early sessions and progressive summarisation loses specific conclusions.
**Asked**
- [FIX] "What did we conclude about isolation?" across a 3-month book club → embeddings + retrieval.
- [LOOKALIKE] Ordinary multi-turn memory (D5-01) needs no vector DB — scale decides.
**Traps**
- ✗ Rolling window; progressive summarisation; XML tags marking conclusions `[doesn't retrieve at scale]`.

### D5-10 · Escalate on structural signals, not sentiment or self-confidence
§5.8
**Rule.** Reliable triggers: explicit request, policy silence, no progress after reasonable attempts, financial threshold (via a hook), repeated failures; mood and self-rated confidence do not track complexity.
**Asked**
- [FIX] Escalation design → explicit criteria + examples (D4-23).
**Traps**
- ✗ Escalate on anger `[mood ≠ complexity]`; escalate below confidence 7/10 `[uncalibrated]`; complexity classifier `[OVERBUILD]`.

### D5-11 · "I want a manager" → escalate immediately
§5.8
**Rule.** An explicit request for a human is honoured at once — no "let me first try…".
**Asked**
- [HOW] Customer asks for a manager → call `escalate_to_human` now.
**Traps**
- ✗ Attempt a resolution first `[violates the rule]`; "never before three attempts" `[same]`.

### D5-12 · Frustration is not a request for a human — until reiterated
§5.8
**Rule.** "This is outrageous!" → acknowledge, offer a concrete resolution, escalate only if the customer reiterates the wish for a human.
**Asked**
- [HOW] Angry message without a request → acknowledge + resolve; "No, I want to talk to someone!" → escalate.
**Traps**
- ✗ Escalate on the first expression of dissatisfaction `[floods the queue]`; ignore a reiterated request `[violates immediate escalation]`.

### D5-13 · Several matching records → ask for another identifier
§5.8
**Rule.** When a lookup returns multiple matches, request email, order number or phone — never choose by heuristic.
**Asked**
- [HOW] Two accounts under one name → "could you confirm the email or order number?"
**Traps**
- ✗ Pick the most recent / the first `[misidentification]`; escalate the ambiguity `[resolvable by asking]`.

### D5-14 · Field-level confidence, calibrated, drives review routing
§5.9
**Rule.** The model emits a confidence per field (not per document); thresholds are tuned on a labelled validation set; low-confidence and ambiguous/contradictory sources go to humans, validated-stable segments auto-process.
**Asked**
- [HOW] Design the review routing → per-field calibrated confidence.
**Traps**
- ✗ Trust raw self-confidence `[uncalibrated]`; one score per document `[too coarse]`; humans re-review everything `[no automation]`.

### D5-15 · Stratified random audit of the automated path
§5.9
**Rule.** Even high-confidence extractions get a regular random audit stratified across document types and fields, to measure the true error rate and catch novel error patterns.
**Asked**
- [WHICH] "Audit only the low-confidence stream?" → no.
**Traps**
- ✗ Skip auditing high-confidence `[novel errors undetected]`; sample only the common type `[under-samples the worst]`; flat 10% random review `[wastes capacity]`.

### D5-16 · Aggregate accuracy masks per-segment failure
§5.9
**Rule.** 97% overall can hide 40% failure on one rare document type; validate accuracy by document type and by field before reducing human review.
**Asked**
- [HOW] 97% overall, proposal to auto-process everything high-confidence → per-type/per-field analysis first + stratified sampling.
**Traps**
- ✗ Auto-process above an aggregate threshold `[masks segments]`.

### D5-17 · Conflict annotation — both values, attributed, coordinator decides
§5.10 · §1.5
**Rule.** Complete the analysis with both conflicting values, annotate the conflict with source attribution, let the coordinator or a human reconcile; don't stop to ask first.
**Asked**
- [HOW] Government 40% vs industry 12%, both credible → both + annotation.
**Traps**
- ✗ Heuristic pick `[SILENT]`; stop and ask before completing `[blocks]`.

### D5-18 · Claim→source mappings that survive synthesis
§5.11
**Rule.** Every claim carries a structured mapping (URL/document, excerpt/location, publication date, confidence) that subagents emit and synthesis preserves and merges.
**Asked**
- [FIX] Final report can't attribute claims → structured mappings preserved through synthesis.
**Traps**
- ✗ Bibliography at the end `[SYMPTOM]`; re-derive attributions by searching again `[expensive, error-prone]`.

### D5-19 · Publication dates prevent false contradictions
§5.11
**Rule.** Without dates, temporal change reads as contradiction; require publication or data-collection dates in every structured output.
**Asked**
- [WHICH] "10% vs 15% — contradiction?" → 2023 vs 2024, likely growth.
**Traps**
- ✗ Flag every numeric disagreement `[no dates]`.

### D5-20 · Render by content type
§5.11
**Rule.** Financial/tabular data → tables; news and analysis → prose; technical findings → lists; time series → chronological; separate well-established findings from contested ones.
**Asked**
- [FIX] Financial tables flattened to prose → render by type.
**Traps**
- ✗ Uniform prose "for consistency" `[imprecise]`.

### D5-21 · Scratchpad files for long tasks
§5.12
**Rule.** Write intermediate state and findings to a scratchpad file and re-read it on continuation; it survives context limits and counteracts degradation.
**Asked**
- [CAUSE] Model starts citing "typical patterns" instead of the classes it found → context degradation → scratchpad.
**Traps**
- ✗ Hold everything in context `[degrades]`.

### D5-22 · Crash recovery — per-agent state exports plus a manifest
§5.12
**Rule.** Each agent exports status, findings, coverage and gaps to a known location; the coordinator loads the manifest on resume and injects persisted findings into agent prompts.
**Asked**
- [HOW] Crash mid-investigation → manifest resume.
**Traps**
- ✗ Rely on conversation history surviving `[stateless]`; re-run everything after each failure `[waste]`; keep findings only in agents' contexts `[nothing survives]`.

### D5-23 · Root cause → pattern (the reliability table as a question form)
§5.14
**Rule.** A symptom sentence maps to one root cause: never terminates → `stop_reason` · precision lost → facts compressed · context bloat → verbose tool results · subagent lacks results → isolation · missed mid-input → lost in the middle · window exhausted in discovery → discovery in main · human queue flooded → sentiment proxy · wrong customer → heuristic match · errors slip through → aggregate masking · can't attribute → mapping lost · false contradictions → missing dates · work lost on crash → no persisted state · drift → accumulated responses · format inconsistency across tools → no normalisation hook.
**Asked**
- [CAUSE] Symptom → name the cause and its pattern.
**Traps**
- ✗ Adjacent cause with the same symptom (bloat vs lost-in-the-middle; drift vs overflow) `[LOOKALIKE]`.

---

## Look-alikes (page)

1 project vs user CLAUDE.md → who can see it (VCS or not) · D3-02
2 `.mcp.json` vs `~/.claude.json` → shared server, personal token via `${VAR}` · D2-14 D2-15
3 CLAUDE.md vs `rules/` vs skills → always / on path / on demand · D3-05 D3-06
4 same-name vs different-name personal skill → posture · D3-11
5 `tool_use` vs `end_turn` → run tool vs stop · D1-01
6 hub vs direct → coordinator sees all · D1-03
7 narrow decomposition vs subagent quality → all succeed + wrong ground = coordinator · D1-12
8 structured error vs generic → the recovery decision needs the payload · D1-18 D2-05
9 transient vs permanent; 0 results vs timeout → retry / don't / accept · D1-19 D2-08
10 fix descriptions vs add routing → signal before layer · D2-02 D2-03
11 prompt vs precondition → a guarantee needs code · D1-27 D2-26
12 token binding vs `dry_run` → a boolean can be skipped · D2-09
13 `context: fork` vs main → exploration isolated · D3-08
14 Batch vs sync → latency tolerance; no mid-request tool pause · D4-16 D4-21
15 `-p` vs fake flags · D3-17
16 few-shot vs more instructions → format failing → examples · D4-01
17 per-file passes vs single pass → attention, not window · D1-16
18 targeted vs generic examples → 4–6 ambiguous · D4-02
19 stated assumptions vs many questions → proceed · D4-27
20 lost-in-the-middle → summary first + headings, not rotation or over-summarising · D5-03
21 case-facts block vs better summariser · D5-06
22 Explore subagent vs `/compact` · D5-08 D3-21
23 drift by accumulation vs overflow · D4-28
24 semantic retrieval vs progressive summarisation (months) · D5-09
25 stateless: `messages[]`, no `session_id`, no vector DB for ordinary memory · D5-01
26 Grep (content) vs Glob (paths) · D2-22
27 Edit (unique anchor) vs Read+Write · D2-23
28 incremental Grep→Read vs bulk read · D2-24
29 MCP tool vs built-in → fix the description, don't remove Grep · D2-18

## Exam ≠ docs (page) — answer per the guide

| Point | Current docs say | Answer on the paper | Card |
|---|---|---|---|
| `allowed-tools` (skills) | permission pre-grant; `disallowed-tools` restricts | restricts tool access during the skill | D3-09 |
| Subagent tool name | `Agent` (v2.1.63+; `Task` still in `system:init`) | `Task`; never let the name decide | D1-05 D1-07 |
| `@import` depth | 4 hops | 5 if forced; syntax is the stable part | D3-03 |
| CLAUDE.md levels | concatenated; 4 levels incl. managed policy + `CLAUDE.local.md` | levels + sharing scope; no override mechanism | D3-01 |
| MCP scopes | local / project / user (+ enterprise) | project vs user | D2-14 |
| `tool_choice` | `none` exists | auto / any / forced only | D2-01 |
| `stop_reason` | 7 values | tested pair is `tool_use` / `end_turn` | D1-01 |
| Batch + tools | tools + multi-turn allowed, one shot per request | "no multi-turn tool calling within a single request" | D4-21 |
| Item format | — | multiple-response items exist; each states how many; all-or-nothing | Start |
| Skip questions | v1.0 silent | no penalty → answer everything | Start |

## Your ledger (page) — ⚑ cards ranked by miss count

D2-21 bundling vs composite (5 papers) · D3-05 / D3-06 the `rules/` reflex (6 instances, 4 papers) · D2-11 / D2-12 `tool_choice` over-specification (Exams 19, 20) · D4-21 batch tool support (Exam 20 ×2) · D4-07 prevention vs repair (Exams 17, 19) · D3-16 feedback batching (Exams 17, 20) · D2-28 / D2-02 descriptions vs examples (Exam 19) · D4-08 schema-scope select-2 (Exam 19) · D1-29 / D2-20 / D5-07 / D3-21 discard vs adjust (Exam 14) · Start-page note on multiple-response all-or-nothing (Exam 14, 4/4 majority-right).

## Document structure

Paged, one self-contained HTML file, no external assets, inline CSS, print stylesheet, no localStorage. Sticky top nav (Start · Toolkit · D1 · D2 · D3 · D4 · D5 · Look-alikes · Exam≠docs · Ledger) + prev/next at the foot of every page. Each domain page lists its cards in order; each card = title row (id, § tag, KD tag, ⚑ badge) · rule · Asked list · Traps list; cross-reference ids are links; a domain page opens with a one-line card index for jumping. Built by `prep with quiz/WIP-TRAPSHEET/build_trap_sheet.py` from this file; verified in the browser (every nav link resolves, prev/next chain covers all pages, print view renders) before delivery.

## Open decisions

- D3-11 posture (same-name override vs different-name variant) — Ram decides before the sitting; the card states both.
- § / KD tags stay as small muted jump-pointers; drop on request.
- Card count is 136 (D1 33 · D2 28 · D3 21 · D4 31 · D5 23); a few corpus points appear under two cards on purpose (least privilege in D1-25 and D2-10; multi-pass in D1-16 and D4-31; batch in D4-16 and the D3 CI angle folded into it) because the exam tests them from both domains.
