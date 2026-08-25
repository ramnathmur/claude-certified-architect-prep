# Domain 1 — Solution Design & Architecture

**Weight:** 17% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Translate business problems into Claude-based AI solutions · Design end-to-end architectures (input → processing → output → feedback loops) · Select appropriate architectural patterns (workflow, agentic, augmented LLM) · Design multi-agent systems and orchestration strategies · Apply decomposition techniques for complex problem solving · Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

---

## 1.1 Translating a Business Outcome into an Automatable Decision

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Translate business problems into Claude-based AI solutions |
| Unit of automation | A recurring **decision** inside a workflow, not an outcome and not a task |
| Fit signals | Scale exceeds human capacity · repeatable pattern with observable feedback · machine-readable context · volume amortizes build cost |
| Wrong-stance signals | Irreversible **and** rare · regulation requires a human decision-maker · novel-creative low-repeatability output · the human relationship is the product · a human must gate every iteration |
| Granularity | Signals apply per workflow **step**, not to the whole workflow |

### Fit Assessment — Whole Workflow vs Per-Step

Score each step separately; a workflow almost never scores uniformly, and the split it produces is the design.

| Situation | Answer | Why |
|---|---|---|
| Step is high-volume, machine-readable, correctness visible immediately | Automate the step | All four fit signals present |
| Step's outcome feedback arrives in 12 months (e.g. loss ratio) | Automate, with a proxy signal (override rate, reopen rate) | Long feedback latency needs a fast surrogate, not disqualification |
| Step requires a licensed or statutorily human decision | Human decides; model prepares the draft | Regulation is a boundary, not a constraint to engineer around |
| Whole workflow judged "not a fit" because one step is regulated | Reject that judgment — decompose first | Per-step scoring is the technique; whole-workflow scoring loses the automatable majority |
| The human relationship is the product being sold | Automate the preparation, not the interaction | Removing the relationship removes the value |

### Exam scenario: a broker wants faster quotes; one step requires a licensed underwriter's signature

- ✅ Automate extraction, lookup, and a risk-tier recommendation; present a complete draft for the licensed sign-off, and state the value in turnaround time
- ❌ Automate the full quote including sign-off, with an audit log and a confidence threshold for oversight — **OVERSPEC**: substitutes a monitoring guarantee for the human decision the scenario states is required; no threshold satisfies a statutory decision-maker requirement
- ❌ Declare the workflow unsuitable for automation because of the regulated step — **WRONG-AXIS**: applies the wrong-stance test at workflow granularity when the objective's technique is per-step decomposition

### ❌ Misconception
"If any step in the process is regulated, the process isn't a candidate for AI." — Fit is scored per step; the regulated step stays human and receives a fully prepared draft, which is usually where most of the cycle-time value was.

---

## 1.2 Baseline and Value Unit Before Design

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Translate business problems into Claude-based AI solutions (feeds Objective 6) |
| Required before designing | Current cost stated in a business unit — minutes/item, FTE-hours/1000, $/transaction, days to turnaround |
| Reason | Without a before, no design can be compared and no value can be reported |
| Failure mode | The system ships, works, and cannot be shown to have helped |
| Stakeholder answer | The baseline is the sentence the business case is written in |

### What the Business Asked vs What the Business Needs

The stated request names a mechanism; the stated outcome names the requirement. Design against the outcome.

| Situation | Answer | Why |
|---|---|---|
| Request: "can Claude write our quotes"; stated pain: 3.2-day turnaround loses business above 2 days | Target turnaround; quality of prose is not the binding constraint | The requirement is the metric named in the pain, not the mechanism named in the request |
| No baseline available for the current process | Measure it before committing to a design | A design chosen without a baseline cannot be defended or compared |
| Proposal to "measure the improvement after launch" | Reject | Measurement with no before produces a number with nothing to compare it to |
| Capability that did not previously exist at all | No efficiency baseline exists; argue transformation | Per-unit comparison has no denominator |

### Exam scenario: a stakeholder requests an AI drafting tool; the stated pain is turnaround time

- ✅ Baseline handling time per item and turnaround days, then design against the turnaround requirement
- ❌ Build the drafting tool as requested and measure satisfaction after launch — **HALF-MOVE**: delivers the requested mechanism while leaving the stated requirement untouched and unmeasurable
- ❌ Instrument the deployed system with dashboards and derive the baseline retrospectively from its own logs — **REPAIR**: reconstructs downstream a measurement the pre-project step could have captured cleanly

### ❌ Misconception
"We'll know it worked because everyone will notice the difference." — Value on this exam is stated in a unit with a before and an after; an unmeasured improvement is not defensible to the stakeholder who funded it.

---

## 1.3 The Pattern Ladder — Selecting the Rung

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Select appropriate architectural patterns (workflow, agentic, augmented LLM) |
| Ladder | plain call → augmented LLM (retrieval, tools, memory) → workflow (fixed steps in code) → agent (model decides the path) → multi-agent (coordinator + specialists) |
| Rule | Move right only when the rung to the left demonstrably cannot meet a **stated** requirement |
| Discriminator | **Enumerability** — can the set of paths a request may take be written down in advance? |
| Cost of moving right | Nondeterminism · latency variance · token multiplication · harder evaluation · wider blast radius |
| Not a maturity model | No credit for being further right |

### Enumerability — Enumerable Paths vs Discovered Paths

If the paths can be listed in advance, they belong in code. If the next action depends on an unlistable discovery, the model must choose it.

| Situation | Answer | Why |
|---|---|---|
| Five known steps, same order, every request | Workflow | Paths are enumerable; code is cheaper, faster, and testable |
| Classify then dispatch to one of five specialised handlers | Workflow (routing pattern) | Enumerated branches are routing, not agency |
| Number of steps unknown; each action depends on what the last one found | Agent | Non-enumerable path is the requirement that funds the move right |
| Task needs current or private data but the path is fixed | Augmented LLM | Retrieval solves it without control-flow nondeterminism |
| 96% of traffic is one known format, 4% is novel | Workflow with an agentic exception route | Match each population to the cheapest rung that handles it |

### Exam scenario: a document pipeline described as "intelligent and adaptive" whose requirements are five fixed steps

- ✅ Implement as a fixed workflow with a validation gate, routing gate failures to an agentic exception path
- ❌ Implement as an agent so the system can adapt to future document types — **ARCHITECTED**: sounds more capable and future-proof; nothing in the stated requirements is non-enumerable, and the agent multiplies cost and latency variance on 100% of traffic to serve a hypothetical
- ❌ Implement as a workflow with no exception route, sending anything unhandled to a human queue — **HALF-MOVE**: correct rung for the majority, but drops the stated requirement to handle novel formats

### ❌ Misconception
"Agentic architectures are the modern approach; workflows are what you build when you can't do agents." — The ladder is a cost ladder. Agency is purchased with a non-enumerability requirement and with nothing else.

---

## 1.4 Workflow vs Agent — The Reverse Direction

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Select appropriate architectural patterns |
| Direction tested | Both. Over-engineering **and** under-engineering appear as separate items |
| Disqualifying phrases for a workflow | "scope is not known up front" · "each step depends on what the previous step discovered" · "the relevant tools are identified at runtime" |
| Failure mode of the wrong choice | A workflow on a non-enumerable task silently handles only the enumerated part |
| Cost shape | Workflow cost is a point; agent cost is a distribution — budget against the tail, not the mean |

### Requirement Disqualification — Which Rung Is Ruled Out

Read the setup for a sentence that makes the path unlistable; that sentence eliminates the workflow before options are compared.

| Situation | Answer | Why |
|---|---|---|
| "Add comprehensive tests to a legacy codebase of unknown structure" | Agent with dynamic adaptive planning | Scope is discovered by mapping first; no fixed script can react to it |
| "Produce the same six-section review for every submission" | Fixed pipeline (prompt chaining) | Predictable and reproducible; agency adds nondeterminism for nothing |
| Agent chosen, and a p95 latency SLA is stated | Re-check — the agent's tail may fail the SLA even if its mean passes | An SLA filters designs before comparison |
| Team proposes an agent "because the workflow feels rigid" | Reject absent a stated non-enumerable requirement | Rigidity is a feeling; enumerability is the test |

### Exam scenario: an open-ended investigation whose scope is only discoverable by exploring first

- ✅ Agent with adaptive planning — map structure, prioritise high-impact areas, adapt as dependencies surface
- ❌ Fixed pipeline with predetermined steps, extended to cover the most likely cases — **HALF-MOVE**: covers the enumerable subset and silently drops the requirement that made the task non-enumerable
- ❌ One large single-pass prompt covering the entire codebase at once — **DISCARD**: replaces staged, adaptive work with a monolith that dilutes attention across everything

### ❌ Misconception
"The safe answer is always the simpler architecture." — Simplicity is the default, not the rule; when the scenario states that the path cannot be known in advance, the simpler rung is the wrong answer and loses the item.

---

## 1.5 Single Agent vs Multi-Agent

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design multi-agent systems and orchestration strategies |
| Justifications (need at least one, stated in the scenario) | Parallelism under a latency requirement · context isolation · per-role tool privilege separation |
| Cost | Typically 4–5× the token spend of a single agent, because shared context is duplicated across isolated agents |
| Latency benefit | Wall clock becomes the longest branch instead of the sum |
| Failure mode | Information loss at every coordinator↔subagent handoff |
| Stakeholder answer | "We pay more tokens to buy wall-clock time and clean separation of privilege" |

### Justification Test — Is the Token Multiplier Funded

Name which of the three justifications the scenario states. If none is stated, one agent with the right tools is the answer.

| Situation | Answer | Why |
|---|---|---|
| Four independent research threads, turnaround is a stated commitment | Multi-agent, parallel fan-out | Latency requirement funds the token multiplier |
| One agent's context would exceed the window, or threads would contaminate each other | Multi-agent | Context isolation is the justification |
| A drafting role must not have write access; a verifier must not have search access | Multi-agent | Privilege separation is the justification |
| Sequential task, no latency constraint, one tool set would serve | Single agent | Nothing funds the multiplier |
| Cost is the stated pillar and the subtasks are sequential | Single agent | Multi-agent moves the named pillar the wrong way |

### Exam scenario: a sequential analysis task with no stated latency, context, or privilege constraint

- ✅ Single agent with the required tool set
- ❌ Coordinator plus three specialist subagents, for separation of concerns — **ARCHITECTED**: reads as the more rigorous design; adds 4–5× tokens and a handoff at every boundary to satisfy no stated requirement
- ❌ Two agents that pass results directly to each other without a coordinator — **WRONG-AXIS**: violates hub-and-spoke, which is the topology that makes multi-agent governable at all

### ❌ Misconception
"Multi-agent is the more scalable architecture, so it's the safer default for a complex problem." — It is the most expensive rung and the one that loses the most information at handoffs; it is chosen for latency, isolation, or privilege, never for sophistication.

---

## 1.6 Coordinator Responsibilities and Root-Cause Location

### Core Facts

| Attribute | Value |
|---|---|
| Topology | Hub-and-spoke — subagents never communicate directly with each other |
| Coordinator owns | Decomposition · context passing · error handling · termination criteria |
| Context default | Subagent context is isolated; it knows only what the coordinator passed |
| Root-cause rule | An output-level symptom in a multi-agent system usually traces to the coordinator, not to a subagent |

### Symptom → Owner — Coordinator Fault vs Subagent Fault

Ask what the coordinator did before asking what the subagent did.

| Symptom | Root cause | Not the cause |
|---|---|---|
| Report misses whole subtopics; every subagent returned correct results | Coordinator's decomposition was too narrow | Subagent query quality |
| Two subagents investigated the same ground | Coordinator did not partition the space before delegating | Missing deduplication after the fact |
| Final report's citations are wrong or missing | Content and metadata were passed as merged free text | The synthesis agent failing to "remember to cite" |
| One subagent's failure terminated the whole run | No structured error propagation and no coordinator recovery policy | The subagent being unreliable |
| Coordinator attempts everything itself and never delegates | The `Task`-equivalent spawning capability is absent from its configuration | Its system prompt not mentioning delegation |
| Research output is shallow and checklist-like | Coordinator prompt is procedural instead of goal-oriented | Too few subagents |

### Exam scenario: a research report omits entire subtopics although each subagent returned correct results

- ✅ Widen the coordinator's decomposition and have it explicitly partition the space before delegating
- ❌ Improve the search subagents' query construction — **WRONG-AXIS**: right vocabulary, wrong owner; the subagents executed correctly on the ground they were assigned
- ❌ Increase the number of subagents to broaden coverage — **HALF-MOVE**: more agents executing the same narrow partition produce more of the same gap

### ❌ Misconception
"The subagent produced the bad output, so the subagent is where the fix goes." — Decomposition, context passing, error policy, and termination all live in the coordinator; most multi-agent defects are visible at a subagent and caused at the hub.

---

## 1.7 Context Passing and Structured Handoff

### Core Facts

| Attribute | Value |
|---|---|
| Rule | Pass structured data that separates content from metadata (source, document name, page, date) |
| Why | Attribution is destroyed during aggregation when content and provenance are merged into free text |
| Escalation rule | A human receiving an escalation does **not** have the transcript; the handoff summary must be self-contained |
| Handoff payload | Entity ID · issue summary · root cause · actions already taken · amount or quantity at stake · recommended action · escalation reason |
| Conflicting values across sources | Preserve both with attribution and annotate the conflict; the coordinator decides |
| Compliance constraint | A regulated audit trail needs the citation, the input, and the prompt version — all of which are lost if provenance is flattened |

### Passing Format — Structured Content+Metadata vs Merged Prose

A downstream agent can only cite what it received as a distinguishable field.

| Situation | Answer | Why |
|---|---|---|
| Synthesis subagent must cite sources | Pass findings as `{content, metadata}` with source URL, document name, page | Citation requires the metadata to survive as metadata |
| Synthesis output has coverage gaps | Coordinator evaluates, re-delegates targeted queries, re-invokes synthesis | Refinement is the coordinator's job |
| Human reviewers keep re-asking for information the system already gathered | Structured handoff summary, self-contained | The human has no transcript access |
| Upstream inputs were partially unavailable (3 of 5 sources returned) | Synthesise with coverage annotations marking what is well-supported vs missing | Graceful degradation; do not fail the whole run |
| A subagent returns "0 results" | Accept as a valid finding | An empty result is information; a timeout is an access failure |

### Exam scenario: human agents receiving escalations keep asking customers for details the system already collected

- ✅ Compile a structured handoff summary containing entity ID, root cause, actions taken, amount, and recommended action, and pass it on escalation
- ❌ Give the human agents access to the raw conversation transcript — **DISCARD**: replaces a compact designed artifact with the entire raw history, which the receiving human must now read end to end
- ❌ Escalate earlier so that less context accumulates before the handoff — **WRONG-AXIS**: treats context volume as the problem when the problem is that context was never transferred; also lowers autonomous resolution rate

### ❌ Misconception
"Telling the synthesis agent to always include its sources will fix the citation problem." — It cannot cite metadata it never received; the fix is the passing format upstream, not an instruction downstream.

---

## 1.8 Orchestration Topology — Parallel, Sequential, Iterative Refinement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design multi-agent systems and orchestration strategies |
| Parallel fan-out | Independent subtasks dispatched together; wall clock = longest branch |
| Mechanical requirement | Parallel delegations must be issued in a **single coordinator turn**; spread across turns they run sequentially with no error raised |
| Sequential chaining | Only where a real data dependency exists |
| Iterative refinement | delegate → synthesise → coordinator evaluates for gaps → re-delegate targeted queries → re-synthesise |
| Termination | Requires stated quality/sufficiency criteria; an iteration cap is a safety net, not a criterion |
| Coordinator prompt style | Goals and quality criteria, never step-by-step procedure |

### Topology Choice — Dependency vs Independence

Serialise only what genuinely depends on an earlier result; everything else fans out in one turn.

| Situation | Answer | Why |
|---|---|---|
| Three independent aspects of one customer issue | Parallel fan-out in a single turn, then synthesise | Independent work serialised wastes wall clock and repeats context fetches |
| Step B needs Step A's extracted entity | Sequential chaining | Real dependency |
| Coverage of the synthesis cannot be guaranteed in one pass | Iterative refinement loop with stated sufficiency criteria | Gap evaluation and re-delegation belong to the coordinator |
| Refinement loop runs indefinitely | Add explicit quality criteria the coordinator evaluates against | Termination is a criteria problem, not a counter problem |
| Coordinator emits its delegations across successive turns | Fix to one turn | Otherwise the parallel design is sequential in practice |

### Exam scenario: a billing dispute containing three independent issues is investigated one issue at a time

- ✅ Decompose into three issues and dispatch them in parallel from a single coordinator turn with shared customer context, then synthesise one resolution
- ❌ Keep the sequential investigation but give the agent a faster model — **WRONG-AXIS**: treats per-call latency as the constraint when the constraint is the serialised topology
- ❌ Dispatch the three investigations across three successive coordinator turns — **HALF-MOVE**: names the right decomposition and still executes it sequentially, because parallelism requires a single turn

### ❌ Misconception
"An iteration limit is what stops the refinement loop." — A cap stops runaway spend; termination on quality requires stated sufficiency criteria the coordinator evaluates the synthesis against.

---

## 1.9 The Feedback Stage

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design end-to-end architectures (input → processing → output → feedback loops) |
| Definition of closed | A correctness signal reaches a destination that **changes** system behaviour |
| Signal types | Implicit (edits, overrides, rejections — immediate, near-zero cost) · explicit (labels, ratings) · outcome (conversion, reopen, loss ratio — late, decisive) |
| Destinations | Evaluation set · prompt or few-shot examples · retrieval/indexing layer · routing thresholds · model selection |
| Not feedback | Logs · dashboards · monitoring alerts — these record behaviour without a correctness label |
| Cheapest labelled data | The delta between what the model produced and what the human in the loop actually shipped |

### Closing the Loop — Signal Captured vs Signal Discarded

A human reviewer in the path generates labelled data only if their correction is captured as an event rather than overwriting the record in place.

| Situation | Answer | Why |
|---|---|---|
| Deployed system, humans reviewing output, no improvement over 6 months | Capture the overrides and route them into the eval set and the prompt | The signal exists and is being discarded |
| Architecture lists input, processing, and output components | The feedback path is what is missing | Four stages, and this is the one omitted at ship time |
| Outcome signal arrives 12 months later | Add a fast proxy (override rate, reopen rate) alongside it | A loop that closes annually cannot steer a monthly release cycle |
| Team proposes a monitoring dashboard as the improvement mechanism | Insufficient on its own | It shows what happened; it carries no correctness label and changes nothing |
| Wrong citations after a document refresh | Route the signal to the retrieval/indexing layer | The failure is retrieval, not the model |

### Exam scenario: an accurate system with human reviewers shows no measurable improvement after six months

- ✅ Capture reviewer corrections as labelled events and route the disagreement cases into the evaluation set and prompt revisions
- ❌ Add a monitoring dashboard tracking accuracy, latency, and volume over time — **ARCHITECTED**: reads as the professional operational answer; it measures the plateau rather than supplying the signal that would end it
- ❌ Move to a more capable model to raise the accuracy ceiling — **DISCARD**: replaces a working component instead of adding the missing one, and leaves the system unable to improve at any ceiling

### ❌ Misconception
"We log every request and response, so we have a feedback loop." — Logs record what happened; feedback carries whether it was right to somewhere that changes the design.

---

## 1.10 Input Boundary and Output Contract

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design end-to-end architectures |
| Input boundary jobs | Acquisition · validation and normalisation · trust decision for untrusted external content |
| Irreversibility | Context not captured at the boundary does not exist downstream |
| Deterministic work | Arithmetic, lookups, schema validation, threshold comparison, redaction, and mandatory sequencing belong in code, not in prompt instructions |
| Output contract | Schema · destination · consumer · error tolerance — set by whoever consumes it |
| Compliance constraint | Pre-model redaction is a boundary control; post-model filtering does not undo the exposure |

### Constraint Placement — Upstream Prevention vs Downstream Repair

Enforce at the earliest point that can enforce it; a downstream filter is a repair for something the boundary could have prevented.

| Situation | Answer | Why |
|---|---|---|
| Unsupported file types reach the model and produce garbage | Reject at input validation | The boundary is the only place that prevents rather than detects |
| PII must not reach the model | Redact before the model call | Post-hoc filtering does not undo the exposure |
| Step A must always precede Step B for correctness | Programmatic precondition blocking B until A returns | Prompt instructions are probabilistic; a precondition is deterministic |
| Downstream service needs to route on model output | JSON contract with an explicit confidence field | Routing is code; it needs a field, not prose |
| A human reviewer consumes the output | Include reasoning and citations alongside the verdict | The consumer determines the shape |
| Customer tier and history would help the model | Attach at the input boundary | Free there, unrecoverable later |

### Exam scenario: a support agent occasionally acts on the wrong account because identity verification is skipped

- ✅ Programmatic precondition — block the account-action tool until the verification call has returned a verified identifier
- ❌ Strengthen the system prompt to always verify identity first — **REPAIR**: addresses at the prompt layer a sequencing requirement that must hold every time; probabilistic enforcement of a security-critical order
- ❌ Add few-shot examples demonstrating the correct call order — **HALF-MOVE**: raises compliance with the order without guaranteeing it, on a requirement that needs a guarantee

### ❌ Misconception
"If the system prompt states the rule clearly enough, the model will follow it every time." — Mandatory sequencing and hard constraints are enforced in code; prompt-level enforcement is probabilistic and fails on the cases that matter.

---

## 1.11 Decomposition Granularity and Technique Choice

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Apply decomposition techniques for complex problem solving |
| Granularity rule | Split until each unit has **one evaluation criterion and one failure mode**; stop when handoff overhead exceeds the benefit |
| Techniques | Functional (process stage) · aspectual (analysis dimension) · data-partition (corpus chunks) · confidence-tier (case difficulty — the cost lever) · risk-tier (blast radius — the governance lever) |
| Plan shape | Fixed pipeline for known scope; dynamic adaptive for discovered scope |
| Failure of a monolith | Attention dilution · mixed evaluation criteria · unrecoverable partial failure · nowhere to insert a gate |
| Failure of over-splitting | Every handoff loses context that was implicit in the shared window |
| What passes between units | Structured summaries, not raw payloads |

### Seam Selection — Evaluation Criterion vs Process Name

Cut where two different evaluation criteria meet, or where a gate must be inserted — not wherever the process has a natural-sounding name.

| Situation | Answer | Why |
|---|---|---|
| 14-file PR reviewed in one pass; output shallow and inconsistent | Per-file local pass (parallel) + one integration pass over the summaries | Two criteria — local correctness, cross-file consistency — need two units |
| Integration pass receives all 14 raw diffs | Pass the structured per-file summaries instead | Raw payloads reintroduce the dilution the split existed to remove |
| 90% routine cases, 10% hard, cost is the named pillar | Confidence-tier split: cheap path for routine, expensive path for hard | Routing by difficulty is the primary architectural cost lever |
| Mix of reversible actions and one irreversible action | Risk-tier split: reversible autonomous, irreversible gated | Blast radius, not confidence, sets this seam |
| A design split so finely that later steps lack context earlier steps had | Merge steps | Over-decomposition is a real defect |
| Repeating review that always follows the same template | Fixed pipeline | Predictable and reproducible; adaptivity adds nondeterminism for nothing |

### Exam scenario: a large multi-file review produces inconsistent verdicts and misses cross-file issues

- ✅ Two-pass decomposition — parallel per-file passes, then one integration pass over the per-file structured summaries and the dependency graph
- ❌ Move to a higher-capability model with a larger context window — **DISCARD**: replaces the model instead of fixing the structure; attention dilution over a large mixed input persists at any capacity
- ❌ Add more detailed instructions to the single review prompt about being consistent and checking cross-file effects — **REPAIR**: patches with prose a defect caused by asking one unit to serve two evaluation criteria

### ❌ Misconception
"Break the work into as many small steps as possible — smaller is always more reliable." — Every split adds a handoff and loses context; the stopping rule is one evaluation criterion and one failure mode per unit.

---

## 1.12 Business Value Pillars and SLA-Driven Design

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Align solutions to business value pillars |
| Five pillars | Efficiency (input per output) · transformation (a capability that did not exist) · productivity (output per person) · cost (total unit economics) · performance SLAs (a stated commitment) |
| Efficiency vs productivity | Efficiency reduces input for fixed output; productivity changes what the freed capacity does |
| Cost includes | Inference · retrieval infrastructure · human review time · error remediation · maintenance |
| SLA behaviour | A filter applied before designs are compared, not a tiebreaker after |
| Cost shape by rung | Workflow cost is a point; agent cost is a distribution — budget the tail |
| Stakeholder answer | State the architecture in the unit the listener measures in |

### Pillar Alignment — Named Pillar vs General Virtue

The scenario names one pillar; the correct design moves that pillar, and a justification that cites a general virtue instead of the stated requirement is the distractor.

| Situation | Answer | Why |
|---|---|---|
| p95 latency commitment of 3s; a 5-step serial chain is proposed | Parallelise independent steps and move enrichment off the request path (precompute at ingest) | The SLA eliminates serial depth before quality is compared |
| Cost is the named pillar at high volume | Confidence-tier routing plus the smallest model that clears the bar per tier | Difficulty-based routing is the lever that moves cost |
| A design halves inference cost and doubles human review time | Reject | Total cost includes human time; this is a regression |
| Capability did not previously exist | Argue transformation; efficiency has no denominator | Forcing a per-unit comparison understates the case |
| Non-engineer stakeholder asks whether it is working | Answer in minutes, dollars, throughput, or commitment met | Model metrics are an input to the business case, not the case |
| Two designs both work; only one meets the stated commitment | Pick the one meeting the commitment | The technically superior design that misses the SLA is the trap |

### Exam scenario: a stated p95 latency commitment, and an agentic design whose mean latency fits but whose tail does not

- ✅ Restructure to a workflow with independent steps parallelised and enrichment precomputed at ingest, keeping the agent only for the exception population
- ❌ Keep the agentic design and tune prompts to reduce the average number of tool calls — **HALF-MOVE**: improves the mean while the commitment is written against the tail
- ❌ Add caching, retries, and a monitoring alert on SLA breaches — **REPAIR**: instruments and mitigates a breach the architecture will keep producing, rather than removing its cause

### ❌ Misconception
"The SLA is a target we'll tune toward once we see real traffic." — A latency or availability commitment eliminates whole rungs of the ladder at design time; a nine-call agent does not reach a three-second p95 by being tuned.
