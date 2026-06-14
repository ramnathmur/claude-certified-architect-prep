# CCA-F Practice — Domain 1: Agentic Architecture & Orchestration (27%)
_14 questions · original, exam-style · grounded in EXAM-DIGEST + D1 citations_

## Questions

**Q1.** A team builds an internal "knowledge bot." For each incoming question it runs a fixed five-stage pipeline: spawn a planner subagent, fan out three parallel research subagents, run an evaluator subagent, then a synthesis subagent — every single time, including for "What's the office Wi-Fi password?" Latency and token cost have ballooned. Most queries are simple lookups answerable in one call. What is the primary architectural flaw?
- A) They used parallel subagents where prompt chaining would have been faster.
- B) They applied the full multi-agent pipeline uniformly instead of escalating complexity only when the task warrants it.
- C) The evaluator subagent should run before the research subagents, not after.
- D) They should have nested the research subagents under the planner to reduce coordination overhead.

**Q2.** An architect is designing a system to investigate intermittent production failures. The next diagnostic step genuinely depends on what the previous step uncovers — a slow query might point to an index, which points to a migration, which points to a schema change — and the path can't be known up front. Which orchestration pattern fits, and what safeguard is essential?
- A) Parallel subagents; cap the number of concurrent workers.
- B) Prompt chaining; add a gate check after each fixed step.
- C) Dynamic decomposition; set a step cap to prevent unbounded investigation.
- D) Routing; ensure the classifier is accurate.

**Q3.** A data team partitions a 12,000-row dataset into four equal chunks and spawns four subagents to process them in parallel, then synthesizes. Chunk A takes 30s, B takes 35s, C takes 90s (it hit a dense, complex section), D takes 25s. An engineer estimates total elapsed processing time as roughly 180 seconds. Why is this estimate wrong, and what should the team also reconsider?
- A) It's right; parallel time is the sum of all durations.
- B) Elapsed time is max(durations) ≈ 90s, not the sum; and chunks should be balanced by expected effort, not row count alone.
- C) Elapsed time is the average ≈ 45s; the partition count should be increased to eight.
- D) Elapsed time is min(durations) ≈ 25s; complex sections should be dropped.

**Q4.** An orchestrator agent already has a customer's full account record loaded in context after a lookup. It now needs to compute the customer's loyalty tier — a trivial arithmetic check against the record it's already holding. The architect's design spawns a dedicated "tier-calculator" subagent for this step. What's the issue?
- A) Nothing — isolating the calculation in a subagent keeps the orchestrator's context clean.
- B) The subagent should be given the Agent tool so it can spawn its own helper.
- C) Delegation is unwarranted here: the work is small and the orchestrator already has the context, so a delegation pays a tool call, fresh context, and a separate invocation for no benefit.
- D) The orchestrator should route the request to a more capable model first.

**Q5.** A parent agent has spent 80,000 tokens gathering case history across many turns and tool calls. It now delegates a drafting task to a subagent by calling the Agent tool with a short prompt: "Draft the apology email." The subagent produces a generic email missing all the case specifics. What is the root cause?
- A) The subagent's model was too small; it should inherit the parent's model.
- B) The subagent should have been given Read access to the parent's transcript file.
- C) A subagent sees only what the parent explicitly puts in its constructed prompt — not the parent's prior turns, tool results, or memory — so the case specifics never reached it.
- D) The parent's context exceeded 200K tokens and was truncated before delegation.

**Q6.** A customer-service agent is configured with this escalation rule: "If three consecutive tool calls fail, escalate to a human." In production it (a) keeps retrying for several minutes when a customer explicitly types "I want to speak to a person," and (b) auto-approves a $40,000 refund because the refund tool succeeded on the first try. What is the correct escalation design principle being violated?
- A) The counter should trigger after one failure, not three.
- B) Escalation should key on category and impact — explicit human request, authority limits, policy exceptions, high-value transactions, uncertain/unsafe states — not a simple failed-call counter.
- C) The agent should never escalate; it should retry indefinitely with backoff.
- D) Escalation logic belongs in the prompt, not in code.

**Q7.** When a support agent escalates a billing dispute to a human specialist, what should the handoff payload contain?
- A) The complete verbatim conversation transcript so the human has full context.
- B) Only the customer's ID, so the human can pull everything themselves.
- C) A structured summary — customer_id, issue_type, root_cause, relevant_records, amount, actions_taken, recommended_next_action — rather than the raw transcript.
- D) A natural-language paragraph the agent writes describing how it felt the conversation went.

**Q8.** A fintech architect enforces a "no single transaction over $10,000 without secondary approval" rule by adding a strongly-worded instruction to the agent's system prompt: "NEVER approve a transaction above $10,000 without approval — this is CRITICAL." Compliance is mandatory. Why is this design unsafe, and what's the correct approach?
- A) It's fine as long as the rule is in capital letters and marked CRITICAL.
- B) The threshold should be a parameter the model passes to the tool so it's explicit in the call.
- C) Hard compliance rules must be enforced in code — the threshold check lives inside the tool, reading a server-controlled source — with the prompt only biasing behavior as one layer of defense-in-depth.
- D) The rule should be moved to a Resource so the model reads it as passive context.

**Q9.** A reviewer flags an agent design as broken because, in a single turn, the agent issues 8 tool calls at once. Under what condition is this actually a legitimate concern rather than a false alarm?
- A) Eight tool calls in one turn is always an anti-pattern; the count itself is the smell.
- B) It's only a concern if the 8 calls are interdependent and need sequencing, or the orchestrator is doing worker grunt-work, or it's runaway — parallel calls to genuinely independent tools are good.
- C) It's a concern only if fewer than 8 tools exist in the toolset.
- D) It's never a concern; more parallel tool calls always means better performance.

**Q10.** A weather agent attempts to send a confirmation SMS as the last step of booking an appointment. The SMS gateway returns a timeout — the agent cannot tell whether the message was actually sent. The booking itself succeeded. What is the correct behavior?
- A) Immediately retry the SMS send to be safe; duplicates are harmless.
- B) Report success on the whole flow, since the booking — the important part — went through.
- C) Report graceful degradation: state the booking is confirmed, that the SMS status is uncertain, and offer a next step — without claiming the SMS was sent.
- D) Throw a generic error and abandon the entire booking.

**Q11.** An architect is choosing between routing and orchestrator-workers for two different systems. System X handles incoming tickets that fall into three well-known, distinct categories (refunds, tech support, general) each needing a different downstream prompt. System Y handles open-ended research requests where the needed subtasks can't be predicted and must be decided per request. Which mapping is correct?
- A) Both should use orchestrator-workers, since both involve delegation.
- B) X → routing (classify into known categories); Y → orchestrator-workers (subtasks determined dynamically by the orchestrator at runtime).
- C) X → orchestrator-workers; Y → routing.
- D) Both should use parallel subagents for maximum speed.

**Q12.** An engineer designs a research orchestration where one subagent must spawn its own set of sub-subagents to drill into each source it finds, creating a nested tree several levels deep. The implementation keeps failing. What constraint did the design ignore, and what's the right alternative?
- A) Subagents are limited to 16 concurrent workers; reduce the fan-out.
- B) Subagents cannot spawn their own subagents (one level deep); chain workers from the main conversation, use the Workflow tool for large fan-outs, or restructure as Skills.
- C) Subagents inherit the parent's full context, so nesting duplicates tokens; pass summaries instead.
- D) Nesting is allowed but only if each subagent uses a smaller model.

**Q13.** A team's multi-agent research system frequently produces overlapping and contradictory findings — e.g., two subagents independently research the same 2025 supply-chain data while a gap in 2021 history goes uncovered. The orchestrator's delegation prompts are short and vague ("research the chip shortage"). What is the most direct fix?
- A) Increase the number of subagents so coverage gaps close statistically.
- B) Let the subagents talk to each other at runtime to deconflict.
- C) Give each subagent a detailed task description — objective, output format, tool/source guidance, and clear task boundaries with an explicit division of labor.
- D) Switch from orchestrator-workers to a single agent to avoid coordination entirely.

**Q14.** An architect must decide whether to build a multi-agent (orchestrator-worker) system or a single agent for a new feature. Which task profile is the *strongest* fit for going multi-agent despite the ~15× token cost?
- A) A low-value, latency-sensitive task where every agent needs to share the same evolving context and steps are tightly dependent.
- B) A high-value task involving heavy parallelization and information that exceeds a single context window, where subtasks are largely independent.
- C) A coding task that requires all agents to stay in lockstep on the same files with frequent cross-dependencies.
- D) Any task at all, since multi-agent systems outperformed single-agent on Anthropic's internal eval.

---

## Answer Key

**Q1 — B.** The anti-pattern is using the full pipeline for a simple fact lookup; Anthropic's guidance is to find the simplest solution and add complexity only when needed. A is wrong because no single pattern swap fixes a design that mis-escalates *every* query regardless of difficulty. _Sub-topic: simplicity-first / pattern selection · Difficulty: easy_

**Q2 — C.** Dynamic decomposition applies when the next step only becomes clear after the current finding (debugging/root-cause), and a step cap is the essential guardrail against unbounded investigation. B (prompt chaining) assumes a *fixed* sequence of known steps, which contradicts "path can't be known up front." _Sub-topic: dynamic decomposition · Difficulty: med_

**Q3 — B.** For parallel subagents, elapsed time = max(durations) ≈ 90s, not the sum — they run concurrently. The deeper lesson: balance chunks by *expected effort*, not raw row count, or one heavy chunk (C) dominates wall-clock time. A repeats the classic sum mistake. _Sub-topic: parallel subagents / elapsed=max · Difficulty: med_

**Q4 — C.** The coordinator should NOT delegate when the work is small and it already holds the context — delegation costs a tool call, a fresh (empty) context, and a separate invocation. A is the tempting misconception that isolation is always worth it; here it's pure overhead. _Sub-topic: when not to delegate · Difficulty: med_

**Q5 — C.** A subagent's context starts fresh: the only channel from parent to subagent is the Agent tool's constructed prompt string — never the parent's prior turns, tool results, system prompt, or memory. The fix is to pass the case specifics (structured summary) in the delegation prompt. D is wrong: nothing here indicates 200K truncation, and even a full context wouldn't transfer to the child. _Sub-topic: multi-agent context passing · Difficulty: med_

**Q6 — B.** Escalation should be driven by category and impact — explicit human request, authority the agent lacks, policy/regulated/high-value transactions, lack of progress, or uncertain/unsafe states — not a simple "escalate after N failures" counter. The counter both ignores the explicit human request and waves through a $40K refund that succeeded on the first call. A still relies on a count; D inverts the compliance-in-code rule. _Sub-topic: escalation logic · Difficulty: med_

**Q7 — C.** The handoff should be a structured payload (customer_id, issue_type, root_cause, relevant_records, amount, actions_taken, recommended_next_action), not a raw transcript dump (A) and not a bare ID (B) that forces the human to reconstruct everything. Dumping the transcript is explicitly an anti-pattern. _Sub-topic: structured handoff · Difficulty: easy_

**Q8 — C.** Hard compliance rules must be enforced in code: the threshold check lives inside the tool and reads a server-controlled source, with the prompt as only one (bias) layer of defense-in-depth (prompt biases → tools enforce → audit logs detect). B is the trap — a model-passed parameter is model-controllable and therefore not an enforcement boundary; prompt emphasis (A) aids salience, not guarantees. _Sub-topic: compliance-in-code · Difficulty: hard_

**Q9 — B.** Judging "8 tools in one turn" as a smell *by count* is the misconception. Parallel calls to genuinely independent tools are good (and speed things up); it's only a problem when the calls are interdependent/need sequencing, the orchestrator is doing worker grunt-work, or it's runaway. A and D are the two opposite over-simplifications. _Sub-topic: parallel tool calls / count-not-smell · Difficulty: hard_

**Q10 — C.** Graceful degradation: state what was verified (booking confirmed), what couldn't be confirmed (SMS status uncertain), and offer a next step — never claim a side effect happened if it didn't. A is wrong because retrying an uncertain write risks duplicate sends; B fakes success; D discards a real partial success. Partial completion beats fake success or a generic error. _Sub-topic: graceful degradation · Difficulty: med_

**Q11 — B.** Routing classifies an input into known distinct categories and dispatches to specialized downstream prompts (System X). Orchestrator-workers fits when subtasks aren't pre-defined but are determined dynamically by the orchestrator per input (System Y) — that runtime, LLM-driven decomposition is its defining feature. A and C blur or invert the distinction. _Sub-topic: routing vs orchestrator-workers · Difficulty: med_

**Q12 — B.** Subagents cannot spawn their own subagents — the orchestration tree is one level deep by default (don't put Agent in a subagent's tools). For nested needs, chain workers from the main conversation, restructure as Skills, or graduate to the Workflow tool for dozens-to-hundreds of agents. A misstates the 16-agent figure (a Workflow-runtime cap, not the nesting rule); C is false (subagents start fresh, not inheriting parent context). _Sub-topic: no-nesting constraint · Difficulty: hard_

**Q13 — C.** Vague delegation causes duplicated/conflicting work and coverage gaps; the direct fix is detailed task descriptions with objective, output format, tool/source guidance, and clear boundaries (explicit division of labor). B is impossible — subagents don't share context and can't self-deconflict at runtime; A throws tokens at a coordination problem without fixing it. _Sub-topic: orchestrator delegation / failure modes · Difficulty: med_

**Q14 — B.** Multi-agent excels at high-value tasks with heavy parallelization and information exceeding a single context window, where subtasks are largely independent — that's what justifies the ~15× token spend. A and C describe shared-context, tightly-dependent, latency-sensitive work that is a *poor* fit; D over-generalizes a point-in-time eval result into "always use multi-agent." _Sub-topic: multi-agent economics gate · Difficulty: hard_
