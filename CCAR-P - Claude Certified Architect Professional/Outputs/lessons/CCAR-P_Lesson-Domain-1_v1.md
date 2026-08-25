# Domain 1 — Solution Design & Architecture

**Weight:** 17% (source: official exam guide v1.0, effective July 2026)
**Exam:** CCAR-P · 63 items · 120 minutes · scaled 100–1000 · pass at 720 · closed book
**Objectives covered (6):** translate business problems into Claude-based AI solutions · design end-to-end architectures (input → processing → output → feedback loops) · select appropriate architectural patterns (workflow, agentic, augmented LLM) · design multi-agent systems and orchestration strategies · apply decomposition techniques for complex problem solving · align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

---

## What this domain is actually about

Seventeen percent is the second-largest single weight on this exam. If item allocation tracks the published weight proportionally, that is roughly eleven of the 63 items — enough that Domain 1 alone can move you across or under 720. Whether those items arrive standalone or grouped under shared scenarios is not stated in the exam guide, so plan for either.

The six objectives look like six separate topics. They are one argument, read left to right:

> A business states an outcome. You find the decision inside their workflow that a model can own. You wire that decision into a system with an input boundary, a processing core, an output contract, and a feedback path. You pick the simplest pattern that satisfies the stated requirements. You decompose whatever is still too big to evaluate as one unit. And you express the whole thing in the unit the business will measure it in.

Every one of those steps constrains the next. That is the through-line, and it is also the reason distractors on this domain are so effective: a wrong answer is usually a design that is defensible in isolation and unjustified by the requirement the scenario actually stated.

Foundations tested whether a design was correct. Professional tests whether it survives production and whether you can defend it to someone holding a budget. Four dimensions run through everything below and are worth carrying into every scenario you read: **what does it cost at volume**, **what breaks first under real traffic**, **how do you explain it to a non-engineer**, and **what does a regulated sector add to the decision**.

One idea sits at the centre of the domain and deserves naming before anything else.

### The pattern ladder

```
plain model call
   → augmented LLM        (the model plus retrieval, tools, or memory)
      → workflow          (fixed steps orchestrated in your code)
         → agent          (the model decides the path; a loop terminates it)
            → multi-agent (a coordinator plus specialists)
```

**Move right only when the rung to the left demonstrably cannot meet a stated requirement.** Each step right buys adaptivity and pays for it in nondeterminism, token volume, latency variance, evaluation difficulty, and debugging surface. The exam is built on this ladder. Most Domain 1 questions are, underneath the scenario prose, asking you to identify which rung the requirements land on.

The ladder is not a maturity model. Nobody gets a better grade for being on rung five.

---

## Objective 1 — Translate business problems into Claude-based AI solutions

### The concept from first principles

A business problem arrives as an outcome, not a specification. "We take too long to issue quotes." "Our support backlog grows faster than we can hire." "Underwriters spend their week reading PDFs." None of these name a system, and none of them can be built.

Translation is the work of converting an outcome statement into a **decision** — a specific, recurring point in a workflow where someone looks at inputs and produces a judgment. Systems are built around decisions. They are not built around outcomes, because an outcome has no interface.

The reason this step exists as its own objective is that the previous generation of automation skipped it. Rules engines and RPA were pointed at *tasks* — click here, copy that field, paste it there — which worked as long as the input never varied. Language models moved the automatable unit from the task to the judgment, and that made the sourcing question harder: not "which clicks repeat" but "which judgments repeat, and can we see whether they were right."

Four properties make a decision a good candidate:

1. **Scale exceeds practical human capacity.** Volume, frequency, or concurrency is past what the team can sustain. Without this, you are building an expensive assistant.
2. **The decision is a repeatable pattern with observable feedback.** The same shape of judgment recurs, and someone eventually finds out whether it was right. No feedback surface means no evaluation, and no evaluation means no improvement path.
3. **The context is machine-readable, or can be made so.** If the inputs live in a filing cabinet or in an employee's head, the first project is data access, not AI.
4. **Throughput justifies the fixed build cost.** Amortisation is a design input, not an afterthought.

And five properties push the other way — signals that the stance itself is wrong:

1. **Decisions are irreversible and rare.** No learning surface, high blast radius. The worst combination.
2. **Regulation explicitly requires a human decision-maker.** Statutory human-in-the-loop is a design constraint, not a preference to be optimised around.
3. **The output is novel-creative judgment with low repeatability.** Each output is bespoke; there is no pattern to match.
4. **The human relationship is the product.** Coaching, therapy, relationship-managed sales. Automating the relationship removes the thing being bought.
5. **A human must gate every single iteration.** If the user has to refine, select, or approve inside every loop pass, you are designing an assistive tool. That is a legitimate product; it is just not the architecture the scenario is usually asking for, and it changes the value case completely.

Note that these signals rarely apply to a *whole workflow*. They apply to the individual steps inside it, which is why translation almost always produces a split: some steps automated, some drafted-then-approved, some left alone.

### Worked example

A commercial insurance broker issues quotes. Current state, measured:

- 400 quote requests per week
- 22 minutes average handling time per quote
- 3 analysts, each ~35 productive hours/week (105 hours available; ~147 hours of work — hence a permanent backlog)
- Turnaround averages 3.2 business days; the broker loses business above 2 days

Decompose the 22 minutes:

| Step | Minutes | Repeatable? | Feedback visible? | Regulated? |
|---|---|---|---|---|
| Read submission email + attachments, extract fields | 9 | Yes | Immediately (field is right or wrong) | No |
| Look up prior claims history in two systems | 3 | Yes | Immediately | No |
| Classify risk tier from the extracted profile | 4 | Yes | At 12 months, via loss ratio | No |
| Price and sign the quote | 4 | Yes | At 12 months | **Yes** — licensed sign-off |
| Format and send | 2 | Yes | Immediately | No |

The translation writes itself. Extraction and lookup are pure fit: high volume, machine-readable, instant feedback. Risk classification is a fit with a caveat — the feedback loop is twelve months long, so it needs a proxy signal (analyst override rate) to be evaluable on a useful timescale. Pricing sign-off is statutorily human and stays human, but it can receive a fully-prepared draft.

Result: automate extraction, lookup, and a risk-tier recommendation; present a complete draft quote to the analyst for sign-off. Handling time goes from 22 minutes to a projected 6. At 400 quotes per week that is 400 × 16 = 6,400 minutes, or about 107 hours returned per week against 105 hours of capacity. The backlog disappears and turnaround, not headcount, is the value story.

The important part of that example is the last column. Nothing about the architecture was chosen before the regulated step was identified, because identifying it is what determined that the system produces a *draft* rather than a *decision*.

### How the exam probes it

The scenario gives you an organisation, a stated business goal, a workload figure, and one or two constraints buried in the prose. The four options each automate something. They differ in **which step they target**.

The correct option targets the step that either consumes the stated cost or carries the stated requirement. The distractors target a step that is visible but cheap, or a step the scenario has already told you is constrained.

Watch for the constraint sentence. In the example above, "quotes must be signed by a licensed underwriter" is one clause in a paragraph of context, and it invalidates any option that has the model issuing the quote. Professional-tier items hide the disqualifying constraint in the setup rather than in the options.

### The wrong turns

- **Building what was asked for instead of what was wanted.** "Can Claude write our quotes?" is a request. "We lose business above two days' turnaround" is the requirement. An option that produces beautifully written quotes but does not touch turnaround has solved the request.
- **Skipping the baseline.** If you cannot state the current cost in a unit — minutes per quote, tickets per analyst per day, dollars per claim — you have nothing to compare against, and Objective 6 becomes unanswerable later. On the exam this shows up as an option that proposes to "measure improvement after launch," which is measurement with no before.
- **Treating a wrong-stance signal as a challenge to engineer around.** When a scenario states a regulatory human-decision requirement, the correct answer accommodates it. Options that add an audit log, a confidence threshold, or a post-hoc review as a substitute for the required human decision are the trap.
- **Automating the relationship.** In scenarios where the human contact is the product being sold, the right answer usually automates the *preparation* for the interaction, not the interaction.

### Takeaways

- Convert the outcome into a specific recurring decision before designing anything.
- Score each step for scale, repeatability, feedback visibility, and machine-readable input.
- A statutory or contractual human-decision requirement is a hard boundary; design the draft, not the decision.
- Capture the baseline in a business unit at translation time. You will need it twice more.
- Long feedback latency does not disqualify a decision, but it forces a proxy signal.

---

## Objective 2 — Design end-to-end architectures (input → processing → output → feedback loops)

### The concept from first principles

Four stages, and the fourth is the one people ship without.

**Input** is the boundary. Three jobs happen here: acquisition (webhook, queue, batch, upload), validation and normalisation (does this document parse, is this field present, is this file the type it claims), and the trust decision. Everything crossing the input boundary from outside your control is untrusted content. That is a prompt-injection surface, and where it enters determines where it must be constrained. Input design also fixes what the rest of the system can never recover: information not captured at the boundary does not exist downstream.

**Processing** is the model call plus the deterministic code wrapped around it. The most common design error in this stage is putting work in the model that code does better. Arithmetic, lookups, deduplication, sorting, threshold comparison, and schema validation are cheaper, faster, and exactly correct in code. The model's job is judgment on unstructured input. Deterministic requirements belong in deterministic components — that is the same principle that makes a programmatic precondition the right answer when a sequence *must* hold, rather than a prompt instruction asking politely for the sequence.

**Output** is a contract, not a text blob. It has a schema, a destination, a consumer, and an error tolerance. The consumer determines the shape: a downstream service needs parseable structure and a confidence field it can route on; a human reviewer needs the reasoning and the citations; an auditor needs the inputs, the version of the prompt, and the timestamp. Design the output for the consumer named in the scenario.

**Feedback** is what makes it a system rather than a script. This is the stage the exam cares most about because it is the one most often missing.

### Feedback, properly

Feedback has three sources with very different latencies and costs:

| Signal type | Example | Latency | Cost to capture |
|---|---|---|---|
| **Implicit** | Reviewer edits the draft; overrides the category; deletes the suggestion | Immediate | Near zero — you already have both versions |
| **Explicit** | Thumbs up/down; a labelling queue; a correction form | Immediate to days | Requires human effort, so volume is low |
| **Outcome** | Did the quote convert; did the ticket reopen within 7 days; what was the 12-month loss ratio | Days to a year | Free, but it arrives late and is confounded |

Implicit signals are the workhorse. If a human is already in your loop reviewing output, the difference between what the model produced and what the human shipped is a labelled training pair you get for nothing. Systems that put a human reviewer in the path and then discard their corrections are throwing away the most valuable data the system generates.

A feedback loop is only closed when the signal **reaches something that changes behaviour**. Name the destination:

- into the **evaluation set** (the disagreement cases are the highest-value eval items you will ever get)
- into the **prompt** (a recurring correction becomes a rule or a few-shot example)
- into the **retrieval layer** (wrong citations mean an indexing or chunking problem, not a model problem)
- into the **routing thresholds** (a confidence band that overrides too often should route differently)
- into **model selection** (a class of failure that a larger model clears)

Logging is not feedback. A log records what happened; it does not record whether it was right. Monitoring dashboards belong to Domain 4 and answer a different question. The Domain 1 question is whether a labelled signal has a path back into the design.

### Worked example

Support ticket triage at 12,000 tickets per month.

**Input.** Webhook from the ticketing system on ticket creation. Attachments extracted to text; anything that fails extraction routes to a human queue rather than proceeding with empty content. PII redaction runs before the model call, because the redaction requirement is deterministic and pre-model. Customer tier and account history are attached from internal systems — this is the architect's decision, not the model's, and it costs nothing at the boundary while being unrecoverable later.

**Processing.** Retrieval over the knowledge base scoped to the product line named in the ticket; classification into one of 14 categories; a drafted first response with citations to the retrieved articles.

**Output.** A JSON contract: `category`, `confidence`, `draft_response`, `citations[]`, `suggested_priority`, `prompt_version`. Routing is code: confidence at or above the threshold auto-assigns to the queue, below it goes to a human triager with the draft attached.

**Feedback.** Three signals, wired to three destinations:

- Category overrides. Observed at roughly 4% — about 480 per month. Each override is a labelled example. The overrides cluster; a monthly review of the confusion pairs drives prompt and category-definition changes.
- Edit distance between `draft_response` and what the agent actually sent. High-edit drafts are pulled into the eval set. Low-edit drafts confirm the pattern is working.
- Reopen rate at 7 days, joined back to the original category and confidence. This is the outcome signal, and it catches the failure mode the other two cannot: confidently-correct-looking triage that resolves the ticket wrongly.

Notice the arithmetic. 480 labelled examples per month is a substantial eval corpus generated for free, and it is generated only because the architecture routed the override event somewhere instead of overwriting the field in place.

### How the exam probes it

Three recognisable shapes:

1. **"The system works but does not improve."** The scenario describes a deployed system, decent accuracy, humans reviewing output, and nothing getting better over six months. The answer captures the human corrections and routes them into the eval set or the prompt. Distractors add a bigger model, more few-shot examples chosen by the team, or a monitoring dashboard.
2. **"Which component is missing from this architecture?"** The scenario lists input handling, processing, and output. The answer is the feedback path.
3. **"Where should X happen?"** X is validation, redaction, enrichment, or a deterministic rule, and the answer is almost always earlier than the tempting option places it. A constraint that can be enforced at the input boundary should not be repaired at the output.

### The wrong turns

- **Calling logging a feedback loop.** Logs answer "what did the system do." Feedback answers "was it right, and what changed as a result."
- **A human review step whose output is discarded.** The reviewer fixes the record and the correction never leaves the record. This is the single most common real-world gap and it appears repeatedly as a distractor's blind spot.
- **Repairing downstream what the input boundary could have prevented.** Adding an output filter to catch a document type the input validator should have rejected. The distractor family is REPAIR and it is persistently attractive because the downstream fix is usually easier to describe.
- **Designing the output for yourself instead of the consumer.** Rich prose output to a service that needs a parseable field; a bare enum to a human who needs to know why.

### Takeaways

- Four stages, and feedback is a stage, not a phase-two enhancement.
- Untrusted content enters at the input boundary; that is where its constraints belong.
- Deterministic requirements go in deterministic code, not in prompt instructions.
- The output contract is set by whoever consumes it.
- Every feedback signal needs a named destination that changes behaviour.
- Implicit signals from humans already in the loop are the cheapest labelled data you will ever have.

---

## Objective 3 — Select appropriate architectural patterns (workflow, agentic, augmented LLM)

### The concept from first principles

Here is the ladder again, with what each rung buys and what it costs.

| Rung | What it is | Buys you | Costs you |
|---|---|---|---|
| **Plain call** | One prompt, one response | Determinism of structure, lowest latency, lowest cost, trivially evaluable | Nothing beyond the model's parametric knowledge |
| **Augmented LLM** | Model + retrieval, tools, or memory | Current and private data; the ability to act | A retrieval layer to build and evaluate; tool-call latency |
| **Workflow** | Fixed steps you orchestrate in code | Each step separately promptable, testable, and model-assignable; predictable cost and latency; gates between steps | Cannot handle a path you did not enumerate |
| **Agent** | Model chooses the sequence; a loop terminates on a stop condition | Handles tasks whose path is not knowable in advance | Nondeterministic cost and latency; harder evaluation; wider blast radius per action |
| **Multi-agent** | Coordinator plus specialists | Context isolation; parallelism; per-role tool privileges | Token multiplication; coordination overhead; information loss at every handoff |

**The discriminator is enumerability.** Can you write down, in advance, the set of paths a request might take? If yes, code them — that is a workflow, and it will be cheaper, faster, more testable, and easier to debug than an agent doing the same thing. If the path depends on what the model discovers partway through, and the discoveries cannot be enumerated, you need an agent.

Two clarifications people get wrong in both directions:

A **workflow can branch**. Routing a request to one of five sub-prompts based on a classification step is still a workflow, because the five branches are enumerated. Branching is not the same as agency. The model choosing *among enumerated options* is a routing workflow; the model choosing *what to do next without a fixed menu* is an agent.

An **agent is not a smarter workflow**. It is a workflow whose control flow has been handed to a nondeterministic component. That is the right trade in some cases and a bad trade in most.

The named workflow patterns worth having at your fingertips: **prompt chaining** (fixed sequence, each step's output feeding the next, with the option of a programmatic gate between steps); **routing** (classify, then dispatch to a specialised handler); **parallelisation** (independent subtasks fanned out, results aggregated — either sectioning by aspect or voting for reliability); **orchestrator-worker** (a controlling step that dispatches to workers, with the dispatch logic in code); **evaluator-optimiser** (a generator and an independent critic, looping until the critic passes).

That last one earns a note. An evaluator-optimiser only works if the evaluator is genuinely independent — a separate call that does not see the generator's reasoning. A generator asked to self-review inside the same context has already rationalised its own choices, and it will confirm them.

### The hybrid answer

Real systems are rarely on one rung. The most professionally correct answer, and one the exam rewards, is a workflow that handles the enumerated majority with an escape hatch to an agent for the remainder.

Take invoice processing. 50,000 invoices per month. 96% come from 40 known vendors in stable formats; 4% are one-off, malformed, or novel.

- Pure workflow: fails on the 4%, which fall to a human queue at 2,000 items/month.
- Pure agent: pays agent-grade cost and latency on the 96% that never needed it.
- Hybrid: a five-step fixed pipeline for the known formats; a validation gate at step three; anything that fails the gate routes to an agent with document-inspection tools, and anything the agent cannot resolve escalates to a human with structured context.

The hybrid is not a compromise. It is the design that matches each population to the cheapest rung that handles it.

### Worked example with numbers

Same invoice pipeline, costed. Take rates of $3 per million input tokens and $15 per million output tokens — the exact figures change over time, the arithmetic does not.

**Workflow path:** 5 calls per invoice, roughly 4,000 input and 500 output tokens each. Per invoice: 20,000 in, 2,500 out. That is $0.060 + $0.0375 = **$0.0975**, call it ten cents. At 50,000/month: **$4,875**.

**Agent path:** averages 9 calls per invoice, and because the agent carries its history forward, average input per call is nearer 12,000 tokens with 400 out. Per invoice: 108,000 in, 3,600 out = $0.324 + $0.054 = **$0.378**. At 50,000/month: **$18,900**.

Roughly 3.9× — and the average understates the risk, because the agent's cost distribution has a tail. The 95th-percentile invoice might take 20 calls. A workflow's cost is a point; an agent's cost is a distribution, and you budget against the tail, not the mean.

Now the hybrid: 48,000 invoices at $0.0975 plus 2,000 at $0.378 = $4,680 + $756 = **$5,436**. You have bought agentic handling of the hard cases for about 11% more than the pure workflow, instead of 288% more.

Latency follows the same shape. If a single call is ~1.5s at p95, a five-step serial chain is ~7.5s and predictable; a nine-call agent averages ~13s with a much longer tail. Against a stated 10-second SLA the workflow passes and the agent fails, and no amount of prompt tuning changes that.

### How the exam probes it

Two mirror-image shapes, and you will see both.

**Shape A — the scenario sounds sophisticated but the requirements are enumerable.** A description full of words like "intelligent," "adaptive," and "end-to-end," with a workload that is in fact five known steps. The options span the ladder and the correct answer is a workflow. The agentic option is the ARCHITECTED distractor: it sounds more capable, and nothing in the stated requirements calls for it.

**Shape B — the scenario states a requirement the workflow cannot meet.** The number of steps is not knowable in advance; the relevant tools are discovered at runtime; the next action depends on what the previous one found. Here the agent is correct and the workflow option is the HALF-MOVE — it handles the enumerated part and silently drops the requirement that made the task non-enumerable.

Both directions get tested. Drilling only "don't over-engineer" will lose you Shape B items, which is exactly how a one-directional habit becomes a repeat miss.

A third shape asks you to justify a choice rather than make it. The stem gives a design and asks which statement supports it. The correct statement cites a requirement from the scenario; the distractors cite a general virtue ("agents are more flexible," "workflows are more reliable") that is true in the abstract and unconnected to this scenario.

### The wrong turns

- **Agentic by default.** The most expensive habit in the field. Agency is a cost centre justified by non-enumerability, and by nothing else.
- **Workflow by reflex when the scenario has disqualified it.** Over-correction is a real failure mode. Read for the sentence that says the path cannot be known in advance.
- **Confusing branching with agency.** Enumerated branches are still a workflow.
- **Reaching for multi-agent when one agent with the right tools suffices.** Rung five is not the top of a mountain; it is the rung with the worst cost multiplier and the most information loss.
- **Self-review inside the generator's context.** An evaluator that sees the generator's reasoning is not an evaluator.

### Takeaways

- Enumerability is the discriminator. Enumerable paths belong in code.
- Every step right on the ladder must be paid for by a requirement stated in the scenario.
- Cost of a workflow is a point; cost of an agent is a distribution with a tail.
- Hybrid — workflow with an agentic exception route — is frequently the professionally correct answer.
- Know the five workflow patterns by name: chaining, routing, parallelisation, orchestrator-worker, evaluator-optimiser.
- An evaluator must be independent of the generator to be worth anything.

---

## Objective 4 — Design multi-agent systems and orchestration strategies

### The concept from first principles

Multi-agent systems are hub-and-spoke: one coordinator, several specialist subagents, and **no direct communication between subagents**. Everything flows through the coordinator.

That constraint is the whole design. It buys four things:

- **Visibility.** The coordinator observes every interaction, so there is one place where the system's state is knowable.
- **Uniform error handling.** One component decides retry versus skip versus escalate, so failure policy is consistent instead of per-agent.
- **Information control.** The coordinator decides what each subagent sees. Subagent context is isolated by default — a subagent knows only what it was passed.
- **Separation of responsibilities.** Each subagent has a narrow scope and, critically, a narrow tool set. Per-role least privilege is enforced by configuration, not by asking a subagent not to use a tool it has.

Context isolation is simultaneously the main benefit and the main hazard. It is why parallel subagents do not pollute each other's reasoning. It is also why a synthesis subagent produces a report with missing citations — it never received the source metadata, because the coordinator passed merged free text instead of a structure that separates content from its provenance. The instinct to fix that by telling the synthesis agent to "remember to cite sources" fails for a mechanical reason: it cannot cite metadata that never reached it.

The **coordinator owns four things**, and nearly every multi-agent exam item is about one of them:

1. **Decomposition.** How the problem is partitioned before delegation. Partition explicitly — assign distinct subtopics or source types — or subagents will overlap and leave gaps.
2. **Context passing.** What each subagent receives, in what structure. Content and metadata stay separate so attribution survives aggregation.
3. **Error handling.** Subagents return *structured* failure context: failure type, what was attempted, partial results, and viable alternatives. A bare error string gives the coordinator nothing to decide with.
4. **Termination.** When the loop stops. This requires stated quality criteria; without them, a refinement loop either stops too early or does not stop.

### Orchestration strategies

| Strategy | Shape | Use when |
|---|---|---|
| **Parallel fan-out** | Coordinator dispatches N independent subagents at once, aggregates results | Subtasks are genuinely independent; wall-clock latency matters |
| **Sequential chaining** | Subagent B's input depends on A's output | A real dependency exists — do not serialise independent work |
| **Iterative refinement** | Delegate → synthesise → coordinator evaluates for gaps → re-delegate targeted queries → re-synthesise | Coverage cannot be guaranteed in one pass |
| **Evaluator-optimiser** | Generator plus an independent critic, looping until criteria pass | Quality is checkable and the first attempt is often insufficient |

Two mechanical points that decide items. Parallelism requires the dispatch to happen **in a single coordinator turn** — issuing the same delegations across separate turns runs them sequentially, and the design intent is lost with no error raised. And **coordinator prompts should state goals and quality criteria, not step-by-step procedure**. A procedural coordinator prompt produces checklist-shaped, shallow results, because it has converted an adaptive system into a brittle script. The fix for a shallow research coordinator is a goal-oriented rewrite, not more detailed steps and not more subagents.

### When multi-agent is actually justified

Three conditions. You want at least two of them present:

1. **Independent parallelisable subtasks**, where wall-clock time is a stated constraint.
2. **Context that would not fit, or would interfere, in one window.** Four research threads at 30k tokens each accumulate to 120k in a single agent, with every thread's noise contaminating every other's reasoning.
3. **Genuinely different tool privileges per role.** A drafting agent that must not have write access; a verification agent that must not have search access.

If none of these hold, one agent with the right tool set does the job at a fraction of the cost.

### Worked example

A research report over four independent domains.

**Single agent:** sequential. Four searches, context accumulating to roughly 160k tokens by the final synthesis, with everything the model read about domain one still occupying the window while it reasons about domain four. Wall clock is the sum of all four branches. Cost is one long, expensive context.

**Multi-agent:** one coordinator plus four search subagents, each with ~30k tokens of isolated context, plus a synthesis subagent that receives four structured summaries rather than four raw transcripts.

- **Wall clock:** the longest single branch, not the sum. If branches take 40/55/35/50 seconds, you pay ~55s instead of ~180s.
- **Token cost:** higher, not lower. The coordinator's own reasoning, four subagent contexts, and a synthesis pass typically land at 4–5× the single-agent token spend, because context that was shared is now duplicated across isolated agents.
- **Quality:** better on cross-domain coverage, because each branch reasons on clean context and the coordinator can partition the space explicitly.

The honest summary: multi-agent trades tokens for latency, isolation, and privilege separation. If the scenario names none of those three as requirements, the trade is unfunded.

### How the exam probes it

Root-cause questions dominate. The symptom appears in the *output* and the answer names something the *coordinator* did.

- Report misses whole subtopics, and every subagent returned correct results → the coordinator's decomposition was too narrow. Not subagent query quality.
- Two subagents investigated the same ground → the coordinator did not partition before delegating. The fix is partitioning up front, not deduplication after.
- Citations are wrong or missing → content and metadata were passed as merged text. Fix the passing structure.
- Synthesis has coverage gaps → the coordinator evaluates and re-delegates targeted queries, then re-synthesises. It does not hand the synthesis agent a search tool, because that dissolves the least-privilege boundary that justified the architecture.
- A subagent failure killed the whole run → structured error propagation plus a coordinator recovery policy. One subagent failing should not terminate a workflow.
- Human reviewers receiving escalations keep re-asking for information the system already gathered → the handoff payload was a flag or free text, not a structured, self-contained summary. The escalation summary must stand alone, because the receiving human does not have the transcript.

A specific trap worth memorising: **an empty result is not a failure.** "Zero results found" is a valid, informative finding. A timeout is an access failure requiring a retry decision. Conflating the two produces pointless retries in one direction and lost findings in the other.

### The wrong turns

- **Fixing the subagent when the coordinator caused the problem.** The most common Domain 1 root-cause miss.
- **Instructing rather than configuring.** Telling a subagent not to use a tool it possesses is probabilistic. Removing the tool is deterministic. Least privilege means *removing* the capability, not logging or confirming its use.
- **Adding subagents to fix a decomposition problem.** More agents executing a bad partition produces more of the same gap.
- **More detailed coordinator steps to fix shallow output.** That deepens the rigidity that caused it.
- **Unbounded refinement.** A loop without stated sufficiency criteria does not terminate on judgment; it terminates on a limit, which is a different and worse thing.
- **Multi-agent as a signal of seriousness.** It is the most expensive rung, and cost is a Professional-tier dimension the exam actively tests.

### Takeaways

- Hub-and-spoke; subagents never talk to each other.
- The coordinator owns decomposition, context passing, error handling, and termination — and that is where root causes live.
- Context isolation is the benefit and the hazard; pass structure, not merged prose.
- Parallel dispatch must occur in one coordinator turn.
- Coordinator prompts state goals and quality criteria, never procedure.
- Justify multi-agent with latency, context isolation, or privilege separation. Otherwise it is 4–5× tokens for nothing.
- Structured error context and structured handoff summaries are architecture, not politeness.

---

## Objective 5 — Apply decomposition techniques for complex problem solving

### The concept from first principles

Decomposition is the technique the other five objectives keep calling. Translation decomposes a workflow into steps. Architecture decomposes a system into stages. Pattern selection decomposes a population into the enumerable majority and the awkward remainder. Orchestration decomposes a problem space before delegating.

Four things go wrong when a task stays too large for one unit of work:

1. **Attention dilution.** A single pass over fourteen files goes deep on some and shallow on others, and you cannot predict which.
2. **Mixed evaluation criteria.** If one unit is judged on extraction accuracy and tone and completeness simultaneously, a failing score does not tell you what failed.
3. **Unrecoverable partial failure.** One monolithic call either succeeds or you redo everything.
4. **Nowhere to put a gate.** Validation, human approval, and cost controls need a seam. A monolith has none.

Item 2 gives the granularity rule that is worth carrying into the exam:

> **Split until each unit has one evaluation criterion and one failure mode. Stop when the coordination overhead exceeds the benefit.**

Both halves matter. Over-decomposition is a real failure: every split adds a handoff, and every handoff loses information that was implicit in the shared context. A ten-step chain where three steps could have been one is three extra opportunities for something to fall out.

### The techniques

| Technique | Split by | Fits |
|---|---|---|
| **Functional** | Stage of the process | A predictable pipeline: extract → validate → enrich → format |
| **Aspectual** | Dimension of analysis | Same input, different lenses: a security pass, a performance pass, a style pass |
| **Data-partition** | Chunks of the corpus | Map-reduce over 200 documents; per-file then cross-file |
| **Confidence-tier** | How hard the case is | Cheap path for the routine 90%, expensive path for the rest |
| **Risk-tier** | Blast radius | Reversible actions autonomous; irreversible actions gated |

The last two are the Professional-tier ones. Confidence-tier decomposition is where cost control actually lives — routing by difficulty rather than running every item through the most capable path. Risk-tier decomposition is where governance meets architecture, and it is the honest answer when a scenario mixes routine actions with one action nobody can undo.

Cutting across all five is the choice of **fixed pipeline versus dynamic adaptive decomposition**:

- **Fixed sequential pipeline (prompt chaining).** Steps known in advance. Use when structure is predictable and reproducibility matters — a review that always follows the same template, an extraction that always yields the same fields.
- **Dynamic adaptive decomposition.** Subtasks generated from intermediate findings. Use when scope is unknown up front and each step depends on what the last one discovered — map the structure first, identify high-impact areas, build a prioritised plan, adapt as dependencies surface.

That is the same enumerability discriminator from Objective 3, applied to the shape of the plan rather than to the shape of the runtime.

### Worked example

A pull request touching 14 files, roughly 800 changed lines.

**Single pass.** One prompt, the whole diff. Three predictable outcomes: attention dilutes so files seven through fourteen get a lighter read than files one through three; verdicts become inconsistent, with a pattern flagged in one file and approved in another; and cross-file issues get missed because the model is spending its capacity on local detail.

**Two-pass decomposition.**

- *Pass 1, per file.* Fourteen independent calls, each seeing one file's diff plus enough surrounding context to judge it. Evaluation criterion: local correctness. Failure mode: a missed local bug. These calls parallelise, so wall clock is one file's latency rather than fourteen. Each produces a structured summary: issues found, exported symbols changed, dependencies touched.
- *Pass 2, integration.* One call over the fourteen structured summaries plus the dependency graph — not the raw diffs. Evaluation criterion: cross-file consistency. Failure mode: type mismatches, circular dependencies, an interface changed on one side only.

Two units, two criteria, two failure modes. When quality drops you know which pass to fix, which the single-pass design could never tell you.

Note what pass 2 receives. Handing it all fourteen raw diffs reintroduces the dilution the decomposition existed to remove. The summaries are the point.

### How the exam probes it

- **"Which decomposition strategy?"** The stem describes the task's scope; you match fixed versus adaptive. Open-ended investigation with unknown scope takes adaptive. A templated, repeating review takes the fixed pipeline, and the adaptive option is unnecessary complexity.
- **"Output is shallow / inconsistent / misses cross-cutting issues."** Diagnose the decomposition. The answer usually adds a separate pass with a different evaluation criterion. A larger model is the DISCARD distractor; more detailed instructions is the REPAIR one.
- **"Where should the split be?"** The right seam is where two different evaluation criteria meet, or where a gate must be inserted. The tempting seam is wherever the process happens to have a natural-sounding name.
- **Over-decomposition items.** Less frequent but they exist: a design split so finely that context is lost between handoffs, with the correct answer merging steps. If you have only ever drilled "split it up," this reads as counterintuitive and you will miss it.

### The wrong turns

- **Splitting by convenience rather than by failure mode.** Process-shaped names are not the same as evaluable units.
- **Passing raw content forward through a decomposition designed to reduce load.** The summaries exist for a reason.
- **A fixed pipeline for genuinely open-ended scope.** A script cannot react to a discovery.
- **Dynamic decomposition where a predictable template exists.** Unnecessary nondeterminism, harder to reproduce, more expensive.
- **Serialising work that is independent.** Sequential chaining is for real dependencies.

### Takeaways

- Split until each unit has one evaluation criterion and one failure mode.
- Stop when handoff overhead exceeds the benefit. Over-decomposition loses context.
- Five techniques: functional, aspectual, data-partition, confidence-tier, risk-tier.
- Fixed pipeline for known scope; dynamic adaptive for discovered scope.
- Pass summaries between units, not raw payloads.
- Confidence-tier decomposition is the main architectural lever for cost; risk-tier is the main one for governance.

---

## Objective 6 — Align solutions to business value pillars

### The concept from first principles

The exam guide names five pillars: **efficiency, transformation, productivity, cost, performance SLAs**. They are not interchangeable framings of "value." They are five different units, and the one the scenario names determines which architecture is correct.

| Pillar | The unit | The question it answers |
|---|---|---|
| **Efficiency** | Input per unit of output — minutes per quote, FTE-hours per thousand tickets | Are we doing the same work with less? |
| **Transformation** | Existence — something not previously done at all | Are we doing something we could not do before? |
| **Productivity** | Output per person, or share of time on higher-value work | Are the same people producing more, or better? |
| **Cost** | Unit economics of the system — cost per transaction, total run rate | What does the solution itself cost to operate? |
| **Performance SLA** | Latency, availability, accuracy, expressed as a commitment | Does it meet the promise we made? |

Efficiency and productivity are close enough to be worth separating carefully. Efficiency reduces the input to a fixed output. Productivity changes what the freed capacity does. The same project reads differently: "we cut handling time 40%" is efficiency; "underwriters now spend Friday on broker relationships instead of PDFs" is productivity. Which one you lead with depends on who is listening, and the exam does sometimes ask exactly that.

**Cost is not just inference cost.** Total cost of a solution includes inference, retrieval infrastructure, human review time, the cost of errors, and maintenance. A design that halves inference cost while doubling human review time has made things worse, and the arithmetic to show it is short.

### Pillars as architectural constraints

This is the part that makes Objective 6 an architecture objective rather than a communications one.

**A latency SLA constrains the pattern.** Suppose the commitment is a p95 response under 3 seconds and a single model call runs ~1.5s at p95.

- A five-step serial chain is ~7.5s. Fails.
- The same five steps with three of them parallel is ~1.5s + 1.5s + 1.5s ≈ 4.5s. Still fails.
- Move the two enrichment steps off the request path — precompute at ingest — and the request path is two calls, ~3s. Passes, barely.
- An agent averaging nine calls is not in the conversation, and its tail is worse than its mean.

The SLA did not just rank the designs. It eliminated a rung of the ladder.

**A cost pillar at volume constrains model selection and decomposition.** This is where confidence-tier decomposition earns its place, and where prompt caching (Domain 2) and the ordering of static content become architectural rather than cosmetic decisions.

**A transformation pillar loosens constraints the others impose.** If the business case is that a capability did not previously exist, per-unit efficiency comparison has no denominator. A design that would fail an efficiency test can be correct under a transformation pillar, and the reverse. Read for which pillar the scenario named.

### Worked example

The invoice pipeline again, argued three ways for three audiences. Same system, same numbers.

- **To the CFO (cost):** processing cost falls from $4.10 per invoice in fully-manual handling to $0.11 in compute plus $0.38 in residual human review, on 50,000 invoices a month. Annual run rate on the platform is roughly $65,000 against about $2.4M in current handling cost.
- **To the operations director (efficiency and productivity):** average handling time drops from 11 minutes to under 2. The team of eighteen stops keying invoices and moves to exception handling and vendor disputes — the work that was permanently deferred.
- **To the CIO (SLA):** p95 processing time is 7.5 seconds against a 10-second commitment, with a documented escape route for the 4% of invoices that take the agentic path and a human queue behind that.

Three sentences, three units, one architecture. Producing them is the skill Objective 6 tests, and it is the skill the "communicate architectural decisions" objective in Domain 6 builds on.

### How the exam probes it

- **Two workable designs, one named pillar.** Both options function. The scenario names a constraint — cost at volume, a latency commitment, a headcount reduction target — and only one design satisfies it. The trap is choosing the technically superior design that fails the named pillar.
- **"How would you justify this to the stakeholder?"** The correct option states the value in a business unit. The distractors state model-level metrics — accuracy, F1, token counts — to an audience that did not ask for them.
- **A stated SLA in the setup paragraph.** Treat any latency, availability, or turnaround number as a filter to apply to the options before evaluating anything else.
- **Cost questions that are really scope questions.** An option reduces inference cost and increases human review. The arithmetic decides, and the arithmetic includes the humans.

### The wrong turns

- **Optimising an unnamed pillar.** A cost-optimised answer to a latency question is wrong, however elegant.
- **Speaking in model metrics to a business audience.** Accuracy is an input to the business case, not the business case.
- **Counting only inference cost.** Human review, error remediation, and retrieval infrastructure are part of the number.
- **Treating an SLA as an aspiration.** It is a commitment, and it eliminates designs before the comparison starts.
- **Leading with efficiency when the value is transformational.** A capability that did not exist has no baseline to be efficient against, and forcing one understates the case.

### Takeaways

- Five pillars, five units. The scenario names one; that one decides.
- Efficiency is input per output; productivity is what the freed capacity does.
- Cost means total cost, including human time.
- An SLA is a filter applied before design comparison, not a tiebreaker after.
- Be able to state any architecture in the unit the listener uses.

---

## Synthesis: the six objectives in one design

A regional insurer wants to cut claims cycle time. Current state: 8,000 first-notice-of-loss claims a month, average 6.4 days to first decision, 40 handlers. Regulatory position: claim *denials* require a licensed adjuster's decision; approvals under $2,500 do not. A stated service commitment of 24-hour acknowledgement, currently missed 30% of the time.

**Objective 1 — translate.** The outcome is cycle time. Decomposing the handler's work locates the decisions: intake extraction from a mixed bundle of forms, photos, and emails (repeatable, machine-readable, instant feedback); coverage verification against the policy (repeatable, deterministic once the policy is retrieved); severity and complexity triage (repeatable, feedback observable via reopen rate); approve/deny (partly regulated — denials are statutorily human, small approvals are not). Extraction and triage are automated; coverage verification is retrieval plus deterministic checks; denial stays human, and the wrong-stance signal that produced that is regulation, not difficulty.

**Objective 2 — end-to-end.** Input: claim bundle arrives by email or portal; attachments extracted; anything unparseable routes to a human queue rather than proceeding empty; policy number validated against the policy system before any model call. Processing: retrieval of the policy document, structured extraction of loss details, coverage check in code, triage classification. Output: a JSON contract carrying `claim_summary`, `coverage_status`, `severity_tier`, `confidence`, `recommended_action`, `citations`, `prompt_version` — designed for two consumers, the routing service and the adjuster. Feedback: adjuster overrides of severity tier (implicit, immediate, feeds the eval set), edit distance on the claim summary, and reopen-within-30-days as the outcome signal.

**Objective 3 — pattern.** The path for a standard auto claim is enumerable: five steps, every time. That is a workflow. Complex liability claims with multiple parties are not enumerable — the number of parties, documents, and lookups is discovered during the work. Those route to an agent with document-retrieval and policy-lookup tools. Hybrid, with a validation gate deciding which population a claim belongs to.

**Objective 4 — orchestration.** The complex path uses a coordinator with three specialists: document analysis, policy interpretation, and precedent lookup. They run in parallel from one coordinator turn, because the three are independent and the 24-hour commitment makes wall clock a stated requirement. The coordinator partitions explicitly, passes findings as structured content-plus-metadata so the final summary can cite the policy clause it relied on, and evaluates the summary for gaps before accepting it. When a claim escalates to an adjuster, the payload is a structured handoff — claim ID, extracted facts, coverage determination with clause citations, actions taken, recommended action, escalation reason — because the adjuster does not see the transcript.

**Objective 5 — decomposition.** Functional split along the pipeline. Confidence-tier split routing simple auto claims down the cheap path and complex liability down the expensive one. Risk-tier split putting every denial and every approval above $2,500 behind a human gate regardless of confidence. Three different criteria, three different seams, and the risk-tier seam is set by regulation rather than by engineering judgment.

**Objective 6 — value.** To the COO: 6.4 days to a projected 1.8, with 24-hour acknowledgement moving from 70% to a designed 98%. To the CFO: compute at roughly $0.31 per standard claim and $1.20 per complex one, against $47 in current handling cost. To the Chief Risk Officer: no denial is issued without a licensed adjuster's decision, every coverage determination cites the clause it relied on, and the audit trail carries the prompt version used.

Read the six sections back in order and notice the dependency chain: the regulatory constraint found in Objective 1 set the risk-tier seam in Objective 5, which set the human gate in Objective 2's output routing, which is the sentence that satisfies the Chief Risk Officer in Objective 6. That chain is what "end-to-end architecture" means, and it is what the exam is testing when it hides a constraint in the setup paragraph.

---

## Misconceptions

| Misconception | Correction |
|---|---|
| "Agentic is the modern architecture; workflows are legacy." | The ladder is a cost ladder, not a maturity ladder. Move right only when a stated requirement makes the left rung impossible. |
| "If the model can decide the path, let it." | Nondeterministic control flow costs tokens, latency variance, evaluability, and debuggability. It is purchased with a requirement, not with a preference. |
| "A workflow can't branch — branching means you need an agent." | Enumerated branches are routing, which is a workflow pattern. Agency is choosing without a fixed menu. |
| "More agents means better coverage." | Coverage is set by the coordinator's decomposition. More agents executing a bad partition produce more of the same gap. |
| "The subagent produced the bad output, so fix the subagent." | In hub-and-spoke, most output defects trace to coordinator decomposition, context passing, or termination criteria. |
| "Tell the agent not to use that tool." | Instructions are probabilistic; configuration is deterministic. Least privilege means removing the capability, not logging or confirming its use. |
| "Logging the system's behaviour is the feedback loop." | A log records what happened. Feedback carries a correctness signal to a destination that changes the system. |
| "Human review in the loop means the system will improve." | Only if the correction is captured and routed somewhere. Reviewers whose edits are discarded generate no learning. |
| "Zero results from a subagent is a failure to retry." | An empty result is a valid finding. A timeout is an access failure. Conflating them causes pointless retries or lost findings. |
| "Split the work as finely as possible." | Every split adds a handoff and loses context. Split until each unit has one evaluation criterion and one failure mode, then stop. |
| "Cost means inference cost." | Total cost includes human review, error remediation, retrieval infrastructure, and maintenance. Halving inference while doubling review is a regression. |
| "The SLA is a target we'll tune toward after launch." | An SLA eliminates designs before comparison begins. A nine-call agent does not meet a three-second p95 by being tuned. |
| "Accuracy figures are how you justify the architecture." | Justify in the pillar's unit — minutes, dollars, throughput, or the commitment met. Accuracy is an input to that case. |
| "A regulatory human-decision requirement can be satisfied with an audit log and a confidence threshold." | It requires the human decision. Design the draft that reaches them, not a substitute for them. |
| "Prompt the model to always call step A before step B." | Mandatory sequencing goes in a programmatic precondition. Prompt-level sequencing is probabilistic. |

---

## Quick reference

**The ladder** — plain call → augmented LLM → workflow → agent → multi-agent. Move right only on a stated requirement. Discriminator: **can you enumerate the paths?**

**Workflow patterns** — prompt chaining · routing · parallelisation (sectioning or voting) · orchestrator-worker · evaluator-optimiser (the evaluator must be independent).

**Four architecture stages** — input (acquire, validate, normalise, trust boundary) → processing (model plus deterministic code) → output (schema, destination, consumer, error tolerance) → feedback (signal plus a destination that changes behaviour).

**Feedback signals** — implicit (edits, overrides — cheapest and best) · explicit (labels, ratings) · outcome (conversion, reopen, loss ratio — late but decisive). Destinations: eval set · prompt · retrieval layer · routing thresholds · model selection.

**Coordinator owns** — decomposition · context passing · error handling · termination criteria. Root causes live here.

**Multi-agent is justified by** — parallelism under a latency requirement · context isolation · per-role tool privilege. Expect 4–5× tokens.

**Decomposition techniques** — functional · aspectual · data-partition · confidence-tier (cost lever) · risk-tier (governance lever). Fixed pipeline for known scope; dynamic adaptive for discovered scope.

**Granularity rule** — one evaluation criterion and one failure mode per unit; stop when handoff overhead exceeds benefit.

**Five value pillars** — efficiency (input per output) · transformation (capability that did not exist) · productivity (output per person) · cost (total, including human time) · performance SLA (a commitment that filters designs).

**Distractor families to recognise in the options**

| Family | Shape |
|---|---|
| OVERSPEC | A stronger guarantee than the requirement asks for |
| DISCARD | Replaces a working mechanism instead of adjusting it narrowly |
| REPAIR | Fixes downstream what a constraint could have prevented upstream |
| ARCHITECTED | Sounds more professional or more thorough; unjustified by the stated requirement |
| HALF-MOVE | A partial version of the right answer that drops the binding requirement |
| WRONG-AXIS | Right vocabulary, wrong discriminator |

**Reading habits for Domain 1 items**

1. Find the stated requirement — the number, the commitment, the regulation. It is usually in the setup, not the question.
2. Ask which rung of the ladder that requirement forces. Eliminate rungs before comparing options.
3. For root-cause items in a multi-agent scenario, look at the coordinator before the subagents.
4. For "which is missing" items, check the feedback stage first.
5. Before selecting, name the pillar the scenario measures in, and confirm your answer moves that pillar.
6. Multiple-response items state how many to select. Whether they are scored all-or-nothing or with partial credit is not published; treat every selection as if the whole item depends on it.
