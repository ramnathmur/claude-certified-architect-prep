# Held-Out Mock Bank — Domain 1: Agentic Architecture & Orchestration (27%)

> HELD-OUT INTEGRITY: every question is original and does not reuse/paraphrase any practice-bank, checkpoint, study-guide-sample, or teaching stem. For Mock A / Mock B only — keep separate from study material. Scenario 8 intentionally excluded (uncovered).

## Mock A — Domain 1 (16 questions)

### A-D1-01 · Scenario: Customer Support Agent · Type: anti-pattern · Difficulty: hard
A travel-booking support agent at *Voyantra* runs an agentic loop. The engineer wrote the loop so that after each model response it scans the assistant's text for the phrase "I've finished" or "all done"; if it finds either, the loop exits and the reply is shown to the customer. In production, the loop sometimes stops while a `cancel_booking` tool call is still pending, leaving cancellations half-applied, and other times runs an extra cycle because the model said "I've finished gathering the details" mid-task. What is the core defect?

A. The completion signal is being inferred from assistant text instead of from `stop_reason == "end_turn"`, which is the only reliable terminator.
B. The loop should exit when the model produces any text content alongside a tool call, since text signals the agent is ready to respond.
C. The loop needs a higher `max_tokens` so the model can finish its closing sentence before the scan runs.
D. The phrases should be matched case-insensitively and combined with a regular expression to catch more completion variants.

### A-D1-02 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: medium
At *Lumen Analytics*, a lead research agent must produce a competitive-landscape brief on four named EV-charging startups. The four startups are unrelated, the data for each lives in a different external source, and there are no dependencies between them; a final writer agent then merges the four findings into one brief. The lead is currently delegating to the four research workers one at a time, waiting for each to return before launching the next. Each worker takes about 40 seconds. How should the lead be restructured, and what will the parallel research phase's elapsed time be?

A. Keep them sequential but cache each worker's output; elapsed stays ~160s but cost drops.
B. Spawn all four plus the writer concurrently; elapsed becomes ~40s because every agent now runs at once.
C. Merge the four workers into one worker that handles all startups serially; elapsed stays ~160s but coordination overhead disappears.
D. Spawn all four research workers in a single response so they run concurrently; the research phase's elapsed time becomes ~40s (the slowest worker), and the writer runs after.

### A-D1-03 · Scenario: — · Type: concept · Difficulty: medium
An architect is deciding between a fixed prompt-chaining pipeline and dynamic decomposition for two jobs. Job 1: every incoming insurance claim runs through the same five stages (intake parse → coverage check → fraud screen → payout calc → letter generation), identical structure every time. Job 2: diagnosing why a nightly data-pipeline silently drops ~3% of records, where each finding reveals where to look next and the investigation path can't be known in advance. Which assignment is correct?

A. Job 1 → dynamic decomposition (claims vary); Job 2 → fixed pipeline (debugging always follows the same steps).
B. Both → fixed pipeline, because both are repeatable production workloads.
C. Job 1 → fixed prompt chaining (predictable, known stages); Job 2 → dynamic decomposition (next step emerges from the prior finding).
D. Both → dynamic decomposition, since the model should always decide its own steps for flexibility.

### A-D1-04 · Scenario: Conversational AI Architecture · Type: anti-pattern · Difficulty: hard
*Northwind Bank* runs a conversational money-movement assistant. To enforce "no outbound transfer over £2,000 without two-factor step-up," the team appended to the system prompt, in bold: "**You must NEVER initiate a transfer above £2,000 without step-up verification.**" An audit found the assistant occasionally initiated a £2,400 transfer when a user phrased the request persuasively across several turns. What is the most effective remediation?

A. Enforce the threshold in code — a `PreToolUse` hook (or in-tool check) that reads a server-controlled limit and blocks/redirects the call — using the prompt only as a soft bias layer.
B. Repeat the rule in capitals at both the top and bottom of the system prompt so attention to it survives long conversations.
C. Move the £2,000 figure into a parameter the model passes to `initiate_transfer` so the limit is explicit in every call.
D. Lower the prompt threshold to £1,500 to create a safety margin against the model's drift.

### A-D1-05 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: medium
At *Cartograph Research*, the lead agent has spent many turns and ~60K tokens assembling a dossier on a pharma merger across web searches and internal filings. It now delegates to a "risk-summary" subagent by calling the Task tool with the prompt: "Summarize the regulatory risks." The subagent returns a vague, generic paragraph that omits every merger-specific detail the lead had gathered. What is the root cause?

A. The subagent's context window was too small to hold the dossier, so it truncated the details.
B. A subagent receives only the constructed Task prompt — none of the lead's prior turns, tool results, or memory — so the dossier specifics were never passed to it.
C. The subagent should have been configured to inherit the lead's model so it could reason at the same depth.
D. The lead exceeded its own context limit, corrupting the dossier before delegation.

### A-D1-06 · Scenario: Customer Support Agent · Type: scenario · Difficulty: medium
A subscription-box support agent at *Crateful* has one escalation rule: "Escalate to a human only after four unsuccessful self-service attempts." In production it (a) keeps trying for several minutes when a user types "I am not talking to a bot, transfer me to a person now," and (b) silently processes a request to close a deceased customer's account — an action requiring legal review — because no tool failed. Which escalation principle is being violated?

A. The attempt counter should be lowered from four to two so escalation fires sooner.
B. Escalation should never be automatic; the agent should retry indefinitely until it succeeds.
C. Escalation should be driven by category and impact — explicit human requests, actions needing authority the agent lacks, policy/legal exceptions, uncertain states — not a count of failed attempts.
D. The escalation decision should be moved entirely into the system prompt so it can weigh nuance per case.

### A-D1-07 · Scenario: — · Type: recall · Difficulty: easy
In the Claude Agent SDK, which statement about an `AgentDefinition`'s `allowed_tools` reflects the principle of least privilege for a worker subagent that only needs to read and summarize files?

A. Grant it the full default toolset so it never blocks on a missing capability.
B. Grant it `Task` so it can spawn helper subagents if a file is large.
C. Leave `allowed_tools` unset, which is equivalent to least privilege.
D. Grant it only the read/summarize tools it actually needs, and omit write, delete, and Task tools it has no role for.

### A-D1-08 · Scenario: Conversational AI Architecture · Type: scenario · Difficulty: hard
A developer-assistant at *Forgeline* is helping a user choose between two refactor strategies for a 50-file module: extract a shared base class, or compose via small utilities. The user wants to explore both from the exact same investigated starting point (the same files read, the same dependency map built) and then compare the two resulting plans side by side. Which session capability fits, and what is true of the two branches?

A. `--resume` the prior session twice in two terminals; each terminal continues the same live transcript.
B. `fork_session` from the investigated state; both branches inherit context up to the fork point and then diverge independently.
C. Start two fresh sessions and re-run the investigation in each; this guarantees identical starting context.
D. Use `/compact` to shrink the investigation, then run both strategies in one session so they share results.

### A-D1-09 · Scenario: Multi-Agent Research System · Type: anti-pattern · Difficulty: hard
At *Beacon Intelligence*, a reviewer flags a coordinator design as broken "because in one turn it fires six Task calls at once." On inspection, the six workers each research a distinct, independent country's energy policy with no shared state and no ordering requirement; the coordinator then synthesizes. Under what condition would the six-at-once pattern actually be a legitimate problem rather than a false alarm?

A. It would be a problem only if the six tasks were interdependent or needed sequencing, or the coordinator were doing worker-level grunt work itself, or the fan-out were runaway — independent parallel work is correct.
B. Six parallel Task calls is always an anti-pattern; the raw count is the smell.
C. It is a problem only if there are fewer than six subagent definitions available.
D. It is never a problem, because more parallel workers always shortens elapsed time.

### A-D1-10 · Scenario: Customer Support Agent · Type: scenario · Difficulty: medium
A food-delivery support agent at *Morsel* finishes resolving a refund dispute, then attempts to send the customer a confirmation email as the final step. The email API returns a timeout — the agent cannot tell whether the email was actually delivered. The refund itself has already posted successfully. What is the correct behavior?

A. Re-send the email immediately to be safe; a duplicate confirmation is harmless.
B. Report the whole interaction as fully successful, since the refund — the part that matters — went through.
C. Mark the entire resolution as failed and reopen the dispute so nothing is reported as partially done.
D. Degrade gracefully: confirm the refund posted, state that the email-delivery status is uncertain, and offer a next step — without claiming the email was sent.

### A-D1-11 · Scenario: — · Type: concept · Difficulty: medium
A `PostToolUse` hook and a `PreToolUse` hook are both available. A team needs (1) to convert every `lookup_shipment` result's Unix timestamps to ISO 8601 before the model reads them, and (2) to block any `apply_credit` call above a server-defined ceiling before it executes. Which hook handles which need?

A. (1) PreToolUse, because timestamps must be fixed before the call; (2) PostToolUse, because blocking happens after execution.
B. (1) PostToolUse, because it intercepts the tool result before the model consumes it; (2) PreToolUse, because it intercepts the outgoing call before it executes.
C. Both belong in PostToolUse, since both transform data the model sees.
D. Both belong in PreToolUse, since hooks always run before the model acts.

### A-D1-12 · Scenario: Multi-Agent Research System · Type: anti-pattern · Difficulty: medium
*Atlas Briefs* runs a coordinator with three research workers on the prompt "research the offshore-wind supply chain." Outputs frequently overlap — two workers independently cover 2024 turbine pricing — while the 2019–2021 permitting history is never touched. The coordinator's delegation prompts are each just the single line "research offshore wind." What is the most direct fix?

A. Add a fourth and fifth worker so statistical coverage closes the gaps.
B. Let the three workers message each other at runtime to divide the territory themselves.
C. Give each worker a detailed, bounded assignment — explicit subtopic, time range, source guidance, and a clear division of labor — so coverage is partitioned before work begins.
D. Replace the multi-agent system with one agent to remove all coordination overhead.

### A-D1-13 · Scenario: Conversational AI Architecture · Type: scenario · Difficulty: hard
A multi-turn legal-intake assistant at *Statute* escalates a matter to a human paralegal mid-conversation. The engineer's handoff implementation forwards the entire 22-turn verbatim transcript to the paralegal's queue. Paralegals complain they must read the whole thing to find the few facts that matter. What should the handoff carry instead?

A. A structured handoff payload — matter type, parties, key facts/records, actions already taken, and the recommended next action — instead of the raw transcript.
B. Only the client's matter ID, so the paralegal can pull the full transcript on demand.
C. The full transcript, but with the assistant's own turns removed to halve the length.
D. A free-form paragraph in which the assistant narrates how cooperative the client seemed.

### A-D1-14 · Scenario: — · Type: concept · Difficulty: medium
An architect must justify spending roughly 15× the tokens of a single agent by going multi-agent (orchestrator-workers). Which task profile is the *strongest* fit for that spend?

A. A latency-critical task where every agent must continuously share one evolving context and steps are tightly interdependent.
B. A small, well-scoped task the coordinator could already complete with the context it holds.
C. Any task at all, because multi-agent setups generally beat single agents.
D. A high-value task with heavy parallelizable, largely independent subtasks whose combined information exceeds a single context window.

### A-D1-15 · Scenario: Customer Support Agent · Type: anti-pattern · Difficulty: medium
An insurance support agent at *Harborline* applies its full agentic apparatus to every inbound message: it spawns an intent-classifier subagent, then a policy-lookup subagent, then a resolution-planner subagent, then an executor — even for "What are your office hours?" Average latency and token cost have tripled, and the vast majority of messages are one-step FAQ lookups. What is the primary architectural flaw?

A. The classifier subagent should run last, after resolution, to confirm intent.
B. The subagents should be nested under one another to cut coordination cost.
C. The full multi-stage pipeline is applied uniformly instead of matching orchestration complexity to the task; simple lookups need at most a single direct step.
D. Parallel subagents should replace the sequential chain to restore speed.

### A-D1-16 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: medium
At *Quorum Labs*, an engineer designs a research worker that, for every source it discovers, spawns its own child subagent to drill into that source — producing a nested tree several levels deep. The implementation keeps failing to launch the grandchild agents. What constraint was overlooked, and what is the right alternative?

A. Subagents cannot spawn their own subagents (the tree is one level deep); keep delegation at the coordinator, or restructure deeper needs as chained workers / Skills.
B. Subagents are hard-capped at eight concurrent children; reduce the fan-out and it will work.
C. Child subagents inherit the parent's full context, so nesting blows the token budget; pass summaries instead and it will launch.
D. Nesting is allowed only if each deeper level uses a progressively smaller model.

## Mock B — Domain 1 (16 questions)

### B-D1-01 · Scenario: Customer Support Agent · Type: anti-pattern · Difficulty: hard
A retail support agent at *Threadbare* drives its agentic loop with a hard rule: "Run at most three iterations, then return whatever the assistant last said." A multi-step return-plus-store-credit case needs five tool calls to complete. The loop halts after three iterations and tells the customer the return is processed when it is not. What is the fundamental flaw in the loop's design?

A. Three iterations is too few; raising the cap to ten would make the loop correct.
B. Using a fixed iteration count as the primary stop condition instead of looping until `stop_reason == "end_turn"`; an iteration cap is at best a runaway safeguard, not the completion signal.
C. The loop should terminate as soon as the assistant emits any natural-language text.
D. The loop should re-send the full history only on the final iteration to save tokens.

### B-D1-02 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: hard
At *Vista Research*, the lead agent partitions a market-sizing job into four parallel workers by giving each an equal slice: 25% of the source list. Worker 1 finishes in 20s, Worker 2 in 22s, Worker 3 in 75s (its slice happened to contain dense regulatory filings), Worker 4 in 18s. An engineer budgets the parallel phase at ~135s. Why is the estimate wrong, and what should the team reconsider about the partition?

A. The estimate is right; parallel elapsed time is the sum of all worker durations.
B. Parallel elapsed time is the mean ≈ 34s; the fix is to double the worker count to eight.
C. Parallel elapsed time is max(durations) ≈ 75s, not the sum; and slices should be balanced by expected effort, not by equal source count, so one heavy slice doesn't dominate.
D. Parallel elapsed time is min(durations) ≈ 18s; the heavy slice should simply be dropped.

### B-D1-03 · Scenario: — · Type: concept · Difficulty: medium
A platform team must pick between *routing* and *orchestrator-workers* for two systems. System P receives support tickets that always fall into three known, distinct lanes (billing, outage, how-to), each needing a different specialized prompt. System Q receives open-ended audit requests whose required sub-investigations cannot be enumerated in advance and must be decided per request. Which mapping is correct?

A. P → routing (classify into known lanes, dispatch to a specialized prompt); Q → orchestrator-workers (sub-tasks decided dynamically by the orchestrator at runtime).
B. Both should use orchestrator-workers, since both involve delegating to specialists.
C. P → orchestrator-workers; Q → routing.
D. Both should use a fixed prompt chain for determinism.

### B-D1-04 · Scenario: Conversational AI Architecture · Type: scenario · Difficulty: medium
A multi-turn HR assistant at *Pillar* needs a deterministic guarantee that no message it sends ever contains an employee's national ID number, and separately wants to relabel the verbose status codes returned by `lookup_hr_record` into plain-English statuses before the model reasons over them. Which mechanism should enforce the ID-redaction guarantee, and why?

A. A strongly worded system-prompt instruction, because the model follows explicit safety rules reliably enough.
B. A few-shot example showing redacted output, because examples teach the format unambiguously.
C. A nullable schema field for the ID, because the model can then return null instead of the number.
D. A hook, because hooks give a deterministic (100%) guarantee whereas prompt instructions are probabilistic; redaction is a compliance bright-line and the status relabel is a PostToolUse transform.

### B-D1-05 · Scenario: Multi-Agent Research System · Type: anti-pattern · Difficulty: hard
At *Meridian Insights*, a worker finishes a deep web investigation and returns its raw 90K-token tool transcript — every page it fetched — directly into the next worker's Task prompt so "no context is lost." Downstream workers slow down and the lead's context balloons. Which principle does this violate, and what is the correct pattern?

A. Nothing is wrong; passing the full transcript guarantees the next worker has everything it needs.
B. It defeats the purpose of context isolation: pass a structured summary plus source indexes between agents, not raw mega-outputs — workers exist to compress, not to forward bulk.
C. The fix is to give the downstream worker a larger context window so the 90K transcript fits comfortably.
D. The fix is to let the two workers share one context window so the transcript never has to be copied.

### B-D1-06 · Scenario: Customer Support Agent · Type: scenario · Difficulty: medium
A telecom support agent at *Cableton* receives: "I want to dispute a charge, but first — just put me through to a human supervisor, I've already tried the bot twice." How should the agent handle the explicit human request, per the escalation patterns?

A. Escalate to a human immediately, because the customer explicitly and unambiguously asked for one — do not attempt autonomous resolution first.
B. Attempt to resolve the disputed charge first; escalate only if its own resolution attempt fails.
C. Ask three clarifying questions to confirm the customer truly wants a human before escalating.
D. Run a sentiment analysis on the message and escalate only if the detected frustration crosses a threshold.

### B-D1-07 · Scenario: — · Type: recall · Difficulty: easy
For a coordinator agent in the Claude Agent SDK to be able to spawn subagents, what must its `allowed_tools` include?

A. `Spawn`
B. `Delegate`
C. `Task`
D. `Subagent`

### B-D1-08 · Scenario: Customer Support Agent · Type: scenario · Difficulty: medium
A banking support agent at *Tidewater* searches for the customer by the name they gave and gets two distinct account matches with the same name. Company policy does not address what to do when multiple records match. What should the agent do?

A. Pick the account with the more recent activity, since it is statistically the likelier match.
B. Proceed against both accounts simultaneously to be safe.
C. Invent a reasonable tie-breaking policy on the spot and apply it.
D. Ask the customer for an additional identifier (e.g., account number or date of birth) to disambiguate, rather than guessing — and since policy is silent, treat the ambiguity as an escalation candidate rather than inventing a rule.

### B-D1-09 · Scenario: Conversational AI Architecture · Type: anti-pattern · Difficulty: hard
A conversational ops assistant at *Switchboard* decides when to escalate to an on-call human by asking the model to rate its own confidence 1–10 each turn and escalating whenever the score drops below 4. In incident reviews, the agent repeatedly self-rated 8–9 while confidently giving wrong remediation steps, so it never escalated. What is the design lesson?

A. The threshold should be raised to 6 so more cases escalate.
B. Model self-rated confidence is an unreliable escalation trigger — a model can be confidently wrong — so escalation should key on category and impact (authority limits, uncertain/unsafe state, explicit request), not a self-score.
C. The model should rate confidence on a 1–100 scale for finer resolution.
D. Confidence scoring is fine; the real fix is a separately trained classifier on incident history.

### B-D1-10 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: hard
At *Keystone Research*, a synthesis worker frequently needs to confirm small facts (a date, a CEO name, a single statistic) while merging findings. Today it bounces every such check back to the coordinator, which invokes a web-search worker and then re-runs synthesis — adding round trips and latency. Analysis shows ~80% of these checks are trivial fact confirmations and ~20% need genuine investigation. Which design reduces overhead while respecting least privilege?

A. Give the synthesis worker a narrow `confirm_fact` tool for the trivial 80%, and keep routing the 20% complex checks through the coordinator to the web-search worker.
B. Give the synthesis worker full access to every web-search tool so it can resolve any check itself.
C. Have the synthesis worker batch all checks and send them to the coordinator only at the very end.
D. Pre-cache extra context around every source during initial research in case synthesis needs it later.

### B-D1-11 · Scenario: — · Type: concept · Difficulty: medium
When is `--resume` of a prior named session the right choice, versus starting fresh with a short summary?

A. Always resume; resuming is strictly cheaper than re-establishing context.
B. Always start fresh; resuming risks loading corrupted state.
C. Resume when the prior context is still current (files unchanged, results still valid); start fresh when results are stale or much time has passed — a short summary beats resuming with outdated tool data.
D. Resume only when the session is under a fixed token size, regardless of staleness.

### B-D1-12 · Scenario: Customer Support Agent · Type: anti-pattern · Difficulty: medium
A SaaS support agent at *Ledgerly* is configured so that whenever any tool returns an error, the whole interaction aborts with a generic "Something went wrong, please try later." A transient timeout on a non-critical `fetch_usage_stats` call now kills sessions even when the customer's actual billing question could have been answered from data already retrieved. What is the most effective fix?

A. Retry every failed tool call up to ten times inside the agent before aborting.
B. Suppress the error silently and treat the empty stats result as success.
C. Escalate to a human on every tool error, regardless of category.
D. Attempt local recovery for transient failures and otherwise degrade gracefully — proceed with what was successfully retrieved, state what couldn't be completed — instead of aborting the whole interaction on any single failure.

### B-D1-13 · Scenario: Multi-Agent Research System · Type: scenario · Difficulty: medium
A multi-agent research system at *Polaris* is being designed so that a document-analysis worker, when it finishes, sends its results straight to the synthesis worker, skipping the coordinator entirely, "to save a hop." What is the main reason to route all inter-agent communication through the coordinator instead?

A. Direct worker-to-worker calls are technically impossible in the SDK, so the coordinator is mandatory.
B. The hub-and-spoke coordinator gives centralized observability, uniform error handling, and control over exactly what context each worker receives — the core benefits of the star topology.
C. The coordinator batches the workers' calls together to cut total API calls and latency.
D. Only the coordinator can serialize a worker's output, which direct calls cannot do.

### B-D1-14 · Scenario: Conversational AI Architecture · Type: scenario · Difficulty: hard
A long-running troubleshooting assistant at *Gridwise* resumes a two-day-old investigation session. Since then, the user has edited several of the config files the agent had read and whose contents are embedded as tool results in the resumed transcript. The agent confidently reasons from the stale embedded file contents and recommends a change that no longer applies. What should the architect have done?

A. Recognized that resumed tool results can be stale when files change, and either started fresh with a short current-state summary or re-fetched the affected files before reasoning.
B. Resumed the session anyway; embedded tool results are authoritative regardless of file changes.
C. Forked the session so both the old and new file states could be compared automatically.
D. Increased the context window so the full two-day history would fit without summarization.

### B-D1-15 · Scenario: — · Type: concept · Difficulty: medium
A 14-file pull request gets a single combined review pass and the results are uneven — deep comments on some files, shallow on others, and a missed cross-module data-flow bug. Which decomposition fixes this, and why?

A. One large pass with a higher-context model, because more context window restores consistent attention.
B. Three full-PR review passes, reporting only issues that appear in at least two passes.
C. Splitting the PR so developers submit no more than four files at a time.
D. A per-file local-analysis pass (parallelizable across workers) followed by a separate cross-file integration pass, because single-pass review over many files dilutes attention and misses both local depth and cross-file interactions.

### B-D1-16 · Scenario: Customer Support Agent · Type: scenario · Difficulty: hard
A healthcare-billing support agent at *Veraclaim* has a coordinator that already holds the patient's full claim record in context after a single lookup. It now needs to determine whether the claim qualifies for a hardship waiver — a one-line comparison of the balance against a threshold it already has in front of it. The design spawns a dedicated "waiver-eligibility" subagent to make this determination. What is the issue?

A. Nothing — isolating the check in a subagent keeps the coordinator's context clean and is best practice.
B. The subagent should be granted the Task tool so it can spawn its own validation helper.
C. Delegation is unjustified: the work is trivial and the coordinator already has the data, so spawning a subagent only adds a tool call, a fresh empty context, and a separate invocation for no benefit.
D. The coordinator should escalate the eligibility decision to a more capable model before deciding.

## Answer Key — Domain 1

### Mock A
- **A-D1-01** — Correct: A. The agentic loop's only reliable completion signal is `stop_reason == "end_turn"`; inferring completion from assistant text both stops prematurely (tool calls still pending) and over-runs (the model says "finished" mid-task). Why others fail: B treats text-alongside-tool-use as done, which is exactly the misread causing half-applied cancellations; C is a `max_tokens` (truncation) concern unrelated to the completion signal; D refines a fundamentally wrong signal (text scanning). Sub-domain: D1.1.
- **A-D1-02** — Correct: D. The four research tasks are independent, so the lead should issue all four Task calls in one response; for parallel subagents elapsed time = max(durations) ≈ 40s, and the writer runs sequentially afterward because it depends on their outputs. Why others fail: A keeps the needless 160s serial cost; B wrongly parallelizes the dependent writer with the workers it consumes; C collapses parallelism back to a 160s serial worker. Sub-domain: D1.4.
- **A-D1-03** — Correct: C. Fixed prompt chaining fits predictable, fully-known stage sequences (the claims pipeline); dynamic decomposition fits open-ended investigation where each finding determines the next step (the silent-drop debug). Why others fail: A inverts both; B forces a fixed chain onto an unknowable debug path; D applies dynamic decomposition to a stable pipeline that gains nothing from runtime planning. Sub-domain: D1.8.
- **A-D1-04** — Correct: A. Hard financial/compliance limits must be enforced in code (a PreToolUse hook or in-tool check reading a server-controlled value), giving a deterministic guarantee; the prompt is only a probabilistic bias layer. Why others fail: B relies on prompt emphasis, which is >90% not 100%; C makes the limit a model-controllable parameter, so it isn't an enforcement boundary; D still trusts the prompt, just at a lower number. Sub-domain: D1.5.
- **A-D1-05** — Correct: B. A subagent's only input channel is the constructed Task prompt — it inherits none of the lead's prior turns, tool results, or memory — so the dossier details must be packed into the prompt or they never arrive. Why others fail: A and D invoke context-size/truncation issues that aren't indicated and wouldn't transfer context anyway; C misstates SDK behavior (subagents don't inherit the parent's model state to gain its gathered context). Sub-domain: D1.3.
- **A-D1-06** — Correct: C. Escalation must key on category and impact — explicit human requests, actions requiring authority the agent lacks, policy/legal exceptions, uncertain states — not a failed-attempt counter, which both ignored the explicit request and waved through a legally sensitive account closure. Why others fail: A still relies on a counter; B removes escalation entirely; D pushes a hard, high-stakes decision into the probabilistic prompt layer. Sub-domain: D1.6.
- **A-D1-07** — Correct: D. Least privilege grants a worker only the tools its role requires (here, read/summarize) and withholds write, delete, and Task tools it has no use for. Why others fail: A grants everything (the opposite of least privilege); B grants Task to a worker that has no delegation role (and subagents can't nest anyway); C leaving it unset is not least privilege — it does not scope tools to the role. Sub-domain: D1.2.
- **A-D1-08** — Correct: B. `fork_session` branches from a shared investigated state; both branches inherit context up to the fork point and then diverge independently — ideal for comparing two approaches from one starting point. Why others fail: A describes resuming one transcript in two terminals, which is unsafe and not two comparable branches; C re-runs investigation and risks divergent (not identical) starting context plus wasted work; D collapses both strategies into one shared session, defeating side-by-side comparison. Sub-domain: D1.7.
- **A-D1-09** — Correct: A. Parallel Task calls to genuinely independent tasks are good and reduce elapsed time; the count is a smell only when tasks are interdependent/need sequencing, the coordinator is doing worker grunt work, or the fan-out is runaway. Why others fail: B and D are the two opposite over-simplifications (always-bad vs always-good); C invents an irrelevant rule about the number of subagent definitions. Sub-domain: D1.4.
- **A-D1-10** — Correct: D. Graceful degradation: state what is verified (refund posted), state what is uncertain (email delivery), offer a next step, and never claim a side effect that wasn't confirmed. Why others fail: A retries an uncertain write and risks a duplicate send; B fakes full success; C discards a genuine partial success by failing everything. Sub-domain: D1.6.
- **A-D1-11** — Correct: B. PostToolUse intercepts a tool *result* before the model consumes it (timestamp normalization); PreToolUse intercepts an *outgoing call* before it executes (blocking an over-ceiling credit). Why others fail: A swaps the two; C and D collapse both needs into one hook type, but transforming inputs vs results requires different lifecycle points. Sub-domain: D1.5.
- **A-D1-12** — Correct: C. Vague one-line delegation causes duplicated work and coverage gaps; the direct fix is detailed, bounded assignments (subtopic, time range, source guidance) that partition the space before work starts. Why others fail: A throws more workers at a coordination problem; B is impossible (subagents don't share context to self-deconflict at runtime); D abandons the architecture instead of fixing the delegation. Sub-domain: D1.3.
- **A-D1-13** — Correct: A. The handoff should be a structured, self-contained payload (matter type, parties, key facts/records, actions taken, recommended next action), not a transcript dump the human must mine. Why others fail: B forces the human to reconstruct everything from a bare ID; C still dumps a transcript, just shorter; D is unstructured narrative with no actionable fields. Sub-domain: D1.6.
- **A-D1-14** — Correct: D. Multi-agent's ~15× token cost is justified by high-value tasks with heavy, largely independent parallelizable work whose information exceeds one context window. Why others fail: A and B describe shared-context, tightly-coupled or small work that is a poor fit; C over-generalizes into "always multi-agent." Sub-domain: D1.3.
- **A-D1-15** — Correct: C. The flaw is applying the full multi-stage pipeline uniformly regardless of task difficulty; simple FAQ lookups warrant at most one direct step, so complexity should scale with the task. Why others fail: A reorders stages without fixing uniform over-processing; B nesting is both disallowed and beside the point; D swaps sequential for parallel but still over-orchestrates trivial lookups. Sub-domain: D1.8.
- **A-D1-16** — Correct: A. Subagents cannot spawn their own subagents — the orchestration tree is one level deep — so deeper needs must be handled by the coordinator, chained workers, or Skills. Why others fail: B invents a concurrency cap that isn't the real constraint; C misstates SDK behavior (subagents start fresh, they don't inherit the parent's full context) and isn't why nesting fails; D the model-size rule is fabricated. Sub-domain: D1.4.

### Mock B
- **B-D1-01** — Correct: B. The defect is using a fixed iteration count as the *primary* stop condition instead of looping until `stop_reason == "end_turn"`; an iteration cap is at most a runaway safeguard, never the completion signal — which is why a 5-call task got cut off and falsely reported done. Why others fail: A just moves the same broken cap; C terminates on any text, which fires mid-task; D's token optimization is unrelated to the completion bug. Sub-domain: D1.1.
- **B-D1-02** — Correct: C. Parallel elapsed time = max(durations) ≈ 75s, not the sum; and the deeper lesson is to balance slices by expected effort rather than equal source count, so one dense slice doesn't dominate wall-clock time. Why others fail: A is the classic sum mistake; B invents an average and an unrelated worker-count fix; D drops real work and misreads elapsed as the minimum. Sub-domain: D1.4.
- **B-D1-03** — Correct: A. Routing classifies an input into known, distinct lanes and dispatches to a specialized prompt (System P); orchestrator-workers fits when sub-tasks aren't pre-defined and are decided dynamically by the orchestrator per request (System Q). Why others fail: B and C blur or invert the distinction; D forces determinism onto an investigation whose steps can't be pre-listed. Sub-domain: D1.8.
- **B-D1-04** — Correct: D. A deterministic compliance guarantee (never emit a national ID) requires a hook (100% enforcement) rather than a probabilistic prompt instruction; the status relabel is a PostToolUse transform on the tool result. Why others fail: A and B rely on probabilistic prompt/few-shot compliance for a bright-line rule; C's nullable field governs schema output shape, not redaction of model-sent messages. Sub-domain: D1.5.
- **B-D1-05** — Correct: B. Forwarding a raw 90K-token transcript defeats context isolation; agents should pass structured summaries plus source indexes, because workers exist to compress before handing off, not to forward bulk. Why others fail: A endorses the anti-pattern; C and D treat the symptom (bigger window / shared context) instead of compressing at the seam, re-bloating downstream context. Sub-domain: D1.3.
- **B-D1-06** — Correct: A. An explicit, unambiguous request for a human is the immediate-escalation pattern: escalate now, do not attempt autonomous resolution first. Why others fail: B is the attempt-then-escalate pattern, wrong when the human request is explicit; C over-interrogates a clear request; D substitutes an unreliable sentiment trigger for the stated request. Sub-domain: D1.6.
- **B-D1-07** — Correct: C. A coordinator must have `Task` in its `allowed_tools` to spawn subagents. Why others fail: A, B, and D are invented tool names that don't exist for subagent spawning in the SDK. Sub-domain: D1.2.
- **B-D1-08** — Correct: D. With multiple record matches the agent should request an additional identifier to disambiguate rather than guess; and because policy is silent on the situation, the ambiguity is an escalation candidate, not a place to invent a rule. Why others fail: A guesses heuristically (recency ≠ correct customer); B acts on both accounts, risking wrong-account actions; C fabricates policy where none exists. Sub-domain: D1.6.
- **B-D1-09** — Correct: B. Model self-rated confidence is an unreliable escalation trigger because a model can be confidently wrong (the agent self-rated 8–9 while giving wrong steps); escalation should key on category and impact instead. Why others fail: A and C tweak a fundamentally unreliable self-score; D's trained classifier is overengineering that still ignores the category/impact principle. Sub-domain: D1.6.
- **B-D1-10** — Correct: A. A narrow `confirm_fact` tool lets the synthesis worker resolve the trivial 80% directly (cutting round trips) while complex 20% checks still route through the coordinator — applying least privilege. Why others fail: B grants full search access, breaking least privilege and role separation; C's end-of-run batching blocks checks whose results later steps depend on; D speculatively caches context it can't reliably predict. Sub-domain: D1.4.
- **B-D1-11** — Correct: C. Resume when prior context is still current (files unchanged, results valid); start fresh with a short summary when results are stale or significant time has passed, since a summary is more reliable than resuming with outdated tool data. Why others fail: A and B are absolute rules that ignore staleness; D gates on token size rather than the real criterion (currency of the context). Sub-domain: D1.7.
- **B-D1-12** — Correct: D. The fix is local recovery for transient failures plus graceful degradation — proceed with what was retrieved, state what couldn't complete — rather than aborting the whole interaction on any single tool error. Why others fail: A's blind ten retries add latency/duplicate risk and still don't degrade gracefully; B silently masks failure as success; C escalates indiscriminately regardless of error category. Sub-domain: D1.6.
- **B-D1-13** — Correct: B. Routing all communication through the coordinator (hub-and-spoke) provides centralized observability, uniform error handling, and control over what context each worker receives. Why others fail: A overstates impossibility as the reason; C and D cite secondary/incorrect mechanics (batching, serialization) rather than the core star-topology benefits. Sub-domain: D1.3.
- **B-D1-14** — Correct: A. Resumed sessions can carry stale tool results when underlying files change; the architect should have started fresh with a current-state summary or re-fetched the changed files before reasoning. Why others fail: B treats stale embedded results as authoritative (the exact failure); C's fork doesn't refresh stale file contents; D enlarging the window keeps the stale data, just more of it. Sub-domain: D1.7.
- **B-D1-15** — Correct: D. A per-file local pass (parallelizable) plus a separate cross-file integration pass fixes attention dilution from single-pass multi-file review, restoring per-file depth and catching cross-module interactions. Why others fail: A is the misconception that more context window fixes attention quality; B suppresses real bugs by requiring cross-pass consensus; C shifts burden to developers without improving the review system. Sub-domain: D1.8.
- **B-D1-16** — Correct: C. Delegation is unwarranted when the work is trivial and the coordinator already holds the data; spawning a subagent only adds a tool call, a fresh empty context, and a separate invocation for no benefit. Why others fail: A treats isolation as always worthwhile when here it is pure overhead; B grants Task to a subagent that has no delegation role (and nesting is disallowed); D escalates a one-line threshold check to a bigger model needlessly. Sub-domain: D1.4.
