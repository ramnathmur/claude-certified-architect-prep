# Domain 6 — Stakeholder Communication & Lifecycle Management

**Weight:** 14% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Conduct structured discovery and requirement gathering · Communicate architectural decisions and trade-offs · Manage stakeholder feedback loops and expectation alignment (including SLAs) · Document architectures and provide implementation guidance · Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

---

## 6.1 Discovery — Eliciting the Decision Behind the Request

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Conduct structured discovery and requirement gathering |
| Discriminator | Has the business decision the system serves been stated, or only a solution the stakeholder has pre-selected |
| Architect's first output | The problem and the decision it feeds — never a component list |
| Wrong default | Build what the stakeholder named, or reject it |

### Stated Solution vs Underlying Decision

A stakeholder arriving with a chosen solution has still not stated a problem; discovery ends when the business decision the system feeds is written down.

| Situation | Answer | Why |
|---|---|---|
| Sponsor asks for "a multi-agent system to handle our intake" | Elicit the intake problem and the decision it feeds, then assess whether the named pattern fits | The pattern may be right; it cannot be assessed against a problem nobody has stated |
| Sponsor names a pattern and the elicited problem does not need it | Say so, with the simpler design and what it gives up | Sequence matters: the problem licenses the pattern, not the reverse |
| Sponsor states a business outcome with no solution attached | Proceed to bounding the requirement (see 6.2) | The precondition is already met |
| Team proposes benchmarking candidate models before the problem is stated | Defer | A benchmark number is uninterpretable without a target and an error cost |

### Exam scenario: a sponsor opens the engagement by naming the architecture they want

- ✅ Establish the business problem and the decision the system serves, then evaluate the proposed pattern against it
- ❌ Begin design of the named pattern, since the stakeholder is the requirement owner — **HALF-MOVE**: honours the stakeholder but skips the step that makes their request buildable and verifiable
- ❌ Run a model benchmark on sample data to ground the conversation in evidence — **WRONG-AXIS**: produces a number before there is a target or an error cost to interpret it against

### ❌ Misconception
"The stakeholder owns the requirement, so the architect's job is to build what they specify." — The stakeholder owns the business outcome; converting it into a specification that can be designed against and verified is the architect's job.

---

## 6.2 Bounding an Unbounded Requirement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Conduct structured discovery and requirement gathering |
| Discriminator | Can the stated requirement be verified — is there a number, a method, and a set |
| Unbounded phrasings | "as accurate as possible" · "reliable enough for production" · "at least as good as our team" |
| The four parts | Target number · measurement method · evaluation set · cost of an error |
| Stakeholder answer | A signed acceptance criterion the sponsor can hold delivery to |

### Verifiable vs Aspirational Requirement

An unbounded requirement cannot be designed against or verified; establishing the accuracy the use case needs, and what an error costs, precedes design.

| Situation | Answer | Why |
|---|---|---|
| Sponsor says "as accurate as possible" | Establish the accuracy the use case requires and what a wrong answer costs, before design | No design can be shown to have met or missed an unbounded target |
| Requirement is bounded but the evaluation set is unspecified | Specify a held-out set stratified to the real input mix | An unstratified set reports a number for a population that does not exist |
| Sponsor cannot state the cost of an error | Keep eliciting; it determines threshold, review placement, and error direction | Error cost is a design input for a probabilistic system, not a footnote |
| Requirement is bounded, measured, and the mix is known | Move to design | The precondition is met |

### Exam scenario: a sponsor requests a document-processing system that is "as accurate as possible"

- ✅ Establish the accuracy level the use case actually requires, how it will be measured, and what an error costs, before proceeding to design
- ❌ Select the highest-capability model and the most thorough pipeline to maximise accuracy — **OVERSPEC**: buys an unpriced guarantee against a target nobody has stated, and still leaves no basis for declaring delivery complete
- ❌ Escalate to the sponsor's leadership that the requirement is not actionable — **DISCARD**: treats requirement definition as an obstacle to the architect's work rather than as the architect's work

### ❌ Misconception
"'As accurate as possible' means aim as high as the budget allows." — It means the requirement has not been stated yet; without a target, a measurement method, and an error cost, neither the design nor the acceptance can be settled.

---

## 6.3 Error Cost Asymmetry as a Design Driver

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Conduct structured discovery and requirement gathering |
| Discriminator | Do a false positive and a false negative cost the same |
| What asymmetry decides | Confidence threshold · which direction the model is biased · where human review sits |
| Compliance constraint | In regulated flows the expensive direction is usually the undetected miss, and the regulator defines it |

### Symmetric vs Asymmetric Error Cost

Where the two error directions cost differently, the threshold and the review placement follow from the asymmetry, not from a generic accuracy target.

| Situation | Answer | Why |
|---|---|---|
| Missed fraud costs 200× a false alert | Bias toward recall; route flagged cases to human review | The cheap error is the one a human can dismiss in seconds |
| False rejection blocks a legitimate customer payment; a missed one is recoverable next-day | Bias toward precision; set a higher action threshold | The expensive error is the irreversible one |
| Sponsor asks only for "95% accuracy" with both directions unpriced | Return to discovery and price both directions | A single accuracy target cannot express an asymmetric cost |
| Both directions cost roughly the same and are correctable | A single accuracy target is adequate | Nothing to trade off |

### Exam scenario: a triage system where a missed high-severity case is far costlier than a false alert

- ✅ Bias the system toward flagging, set the confidence threshold from the cost ratio, and route flagged cases to human review
- ❌ Tune for the highest overall accuracy on the evaluation set — **WRONG-AXIS**: optimises an aggregate that weights both error directions equally when the business does not
- ❌ Add a post-hoc audit that samples missed cases weekly — **REPAIR**: detects the expensive error after it has already been paid for, instead of biasing against it upstream

### ❌ Misconception
"Higher overall accuracy is always the better system." — Where error costs are asymmetric, the system with the lower aggregate accuracy and fewer expensive-direction errors is the better system.

---

## 6.4 Reporting Performance to a Sponsor

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Communicate architectural decisions and trade-offs |
| Discriminator | Does performance vary sharply by input type — if so, an aggregate misleads |
| The three components | Break out by case type · state the measurement method and set · give the end-to-end outcome including human review |
| Both failure directions | The flattering aggregate misleads; refusing to quantify fails the sponsor |
| Cost dimension | The sponsor is deciding budget; the end-to-end outcome is the number that decision needs |

### Aggregate vs Segmented Reporting

Report in the shape the system's performance actually has: segment where it varies, and always with the measurement basis attached.

| Situation | Answer | Why |
|---|---|---|
| 94% on standard cases, 61% on complex, sponsor wants "one number" | Give per-segment figures, the measurement basis, and the end-to-end outcome including human review | The aggregate is a weighted average over a mix that will change |
| Performance is genuinely uniform across input types | A single figure is honest — still state the method and set | Segmentation without variance is noise |
| Architect declines to give any number because "it depends on the case" | Not acceptable | The sponsor has a budget decision and cannot make it on a qualitative answer |
| Sponsor has been given the model metric and is planning against it | Supply the end-to-end outcome with human steps included | The sponsor is accountable for the process, not the component |

### Exam scenario: an executive demands a single accuracy figure for a system whose performance varies sharply by document type

- ✅ Report accuracy broken out by document type, state how it was measured and on what set, and give the end-to-end business outcome including the human review step
- ❌ Report the weighted average across all document types as the headline figure — **HALF-MOVE**: answers the question asked with a number that is unstable and conceals the weak segment
- ❌ Explain that accuracy varies too much by case for a single figure to be meaningful — **DISCARD**: technically defensible, but abandons the quantification the sponsor's decision requires

### ❌ Misconception
"They asked for one number, so giving them one number is responsive." — Where performance varies by case type, an aggregate misleads and will move next quarter for reasons nobody can explain; segment it, state the method, and give the end-to-end outcome.

---

## 6.5 Metric Selection for a Stakeholder

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Manage stakeholder feedback loops and expectation alignment |
| Discriminator | Which decision is this particular stakeholder about to make |
| Rule | A useful metric is tied to the decision the stakeholder faces, and is stated together with what it does not cover |
| Failure mode | Metrics that are real, measurable, and irrelevant to the decision in front of that person |

### Decision-Linked vs Dashboard-Available Metric

Pick the metric from the stakeholder's pending decision, not from what the monitoring stack already emits.

| Stakeholder decision | Metric | Not |
|---|---|---|
| Operations lead staffing the review queue | Volume reaching human review, and its variance | Per-token cost; p95 latency |
| CFO deciding renewal | Cost per processed item and its trajectory at projected volume | Model accuracy in isolation |
| Compliance owner signing off | Override rate and audit-trail completeness on the regulated segment | Aggregate accuracy across all segments |
| Engineering lead tuning the system | Per-segment accuracy, latency percentiles, failure taxonomy | End-to-end business outcome alone |

### Exam scenario: choosing what to report to an operations director planning next quarter's staffing

- ✅ Report the proportion of volume routed to human review, its variance, and what that metric does not cover
- ❌ Report overall system accuracy, as the headline quality measure — **WRONG-AXIS**: a real metric, but it does not answer the staffing decision in front of them
- ❌ Report the full monitoring dashboard so they can select what matters to them — **ARCHITECTED**: looks thorough and transparent, and transfers the architect's interpretation job to someone without the context to do it

### ❌ Misconception
"More metrics gives the stakeholder a fuller picture." — A metric that does not inform the decision in front of the stakeholder is noise; select for the decision and state the metric's blind spot alongside it.

---

## 6.6 Explaining the Limits of Automation

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Communicate architectural decisions and trade-offs |
| Discriminator | Can the specific decisions that resist automation be named, along with what automating them would risk |
| Two classes that resist automation | Decisions carrying accountability someone must attest to · decisions the system cannot verify it got right |
| Register that fails | Generic appeals to model imperfection or to "human in the loop for safety" |
| Compliance constraint | Where a regulator requires an accountable person, the constraint is the attestation, not the accuracy |

### Specific Named Limits vs Generic Caution

Name which decisions cannot be automated and what automating them would risk; a general statement about AI fallibility gives the stakeholder nothing to decide with.

| Situation | Answer | Why |
|---|---|---|
| Stakeholder asks why the last 20% still needs people | Name the decisions in that 20% that carry accountability or are unverifiable, and the risk of automating each | Gives the stakeholder a costed choice rather than a caution |
| The residual work is unverifiable rather than regulated | Say so: the system cannot check its own output on these cases against ground truth | Different limit, different remedy — it may be closable with better evaluation data |
| The residual work is small, low-risk, and merely unbuilt | Say so, and price it | Not every human step is a principled limit |
| Stakeholder proposes removing review from a regulated segment to hit a savings target | Refuse on the named attestation requirement, and quantify what the segment is worth | The constraint is external and not tradeable against savings |

### Exam scenario: a stakeholder asks why the system cannot be fully automated

- ✅ Identify the specific decisions that require human accountability or cannot be verified by the system, and state what automating each would risk
- ❌ Explain that AI systems are probabilistic and a human in the loop is a safety best practice — **HALF-MOVE**: true and unspecific; the stakeholder still cannot tell which work could be automated and which cannot
- ❌ Commit to full automation once accuracy improves past a threshold — **OVERSPEC**: promises a future guarantee on decisions whose obstacle is accountability, which accuracy does not remove

### ❌ Misconception
"Explaining why full automation isn't possible means explaining that AI isn't perfect." — The useful answer names the specific decisions that carry accountability or are unverifiable, and what automating them would put at risk.

---

## 6.7 Architecture Decision Records

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Document architectures and provide implementation guidance |
| Discriminator | Can a reader who was not present tell a load-bearing constraint from a preference |
| The four parts | The decision · the alternatives considered · the trade-offs · the constraints that drove the choice |
| For AI systems, also record | The evaluation numbers the decision rested on, and the condition that reopens it |
| Failure mode | Constraints expire; an unrecorded constraint makes the decision unreopenable |

### Chosen Design vs Decision Record

A record of the chosen design answers "what"; only the alternatives, trade-offs, and driving constraints answer "why, and may I change it".

| Situation | Answer | Why |
|---|---|---|
| Documenting a model-tier choice made under a latency ceiling | Record the decision, the rejected options with their numbers, the trade-off, and the ceiling | When the ceiling moves, the decision can be reopened on evidence |
| A year-old decision is questioned after a constraint changed | Check the recorded constraint and re-evaluate against it | The record exists for exactly this moment |
| Team proposes a detailed component diagram and inventory as the documentation | Insufficient alone | Diagrams answer "what"; they carry no reasoning |
| Team proposes a recorded architecture walkthrough | Insufficient alone | Transfers knowledge once and goes stale on the first change |

### Exam scenario: deciding what the architecture documentation must contain for a design that will be maintained by another team

- ✅ Record the decision, the alternatives considered, the trade-offs accepted, and the constraints that drove the choice
- ❌ Produce a comprehensive description of the chosen architecture with detailed component diagrams — **ARCHITECTED**: more effort and more pages, missing the content that makes the design safe to change
- ❌ Record a walkthrough session with the original architects for the maintaining team — **HALF-MOVE**: one-time transfer to whoever watches it, stale the first time the system changes

### ❌ Misconception
"Good architecture documentation describes the system thoroughly." — Thorough description of the chosen design cannot support revisiting it; the alternatives, trade-offs, and driving constraints are what make the decision reopenable.

---

## 6.8 Implementation Guidance for a Receiving Team

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Document architectures and provide implementation guidance |
| Discriminator | Can the receiving team build and change the system without reconstructing the architect's reasoning |
| Contents | Interface contracts · configuration rationale · failure modes with the response to each · tests that must pass before a change ships |
| Distinct from | The ADR, which explains why the design is as it is |

### Guidance Artifact vs Narrative Overview

Implementation guidance is a set of contracts, rationales, failure responses, and gating tests; narrative prose about the system is not implementation guidance.

| Situation | Answer | Why |
|---|---|---|
| Another team will extend the pipeline | Interface contracts, configuration rationale, failure modes, gating tests | They can change it safely without the original team |
| A prompt or model change is proposed post-handover | Regression tests that must pass first, named in the guidance | Prevents a silent behavioural regression from shipping |
| Team asks for an onboarding overview document instead | Supplement, not substitute | Orients a reader; does not gate a change |
| Configuration values documented without their rationale | Insufficient | A value without its reason is changed by the next person who finds it inconvenient |

### Exam scenario: an internal team will take over extending a delivered Claude system

- ✅ Provide interface contracts, the rationale behind each configuration value, the known failure modes with the response to each, and the tests that must pass before any change ships
- ❌ Provide a thorough narrative overview of how the system works end to end — **ARCHITECTED**: reads as complete documentation and gates nothing
- ❌ Provide the repository with well-commented code and offer to answer questions in a shared channel — **REPAIR**: reactive support in place of a durable artifact, and it evaporates when the original team is reassigned

### ❌ Misconception
"If the code is clean and commented, the receiving team has what they need." — Code states what the system does; it does not state which configuration values are load-bearing, which failures are known, or which tests gate a change.

---

## 6.9 Service Commitments on a Probabilistic System

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Manage stakeholder feedback loops and expectation alignment (including SLAs) |
| Discriminator | Does the commitment depend on inputs the provider does not control |
| Infrastructure commitments | Availability and latency — provider-controlled, commit normally |
| Accuracy commitments | Four parts: what is committed · on what population · how and how often measured · what is excluded |
| Failure mode | A stated metric with no stated exclusions is read as covering everything |

### Qualified Commitment vs Flat Number

Availability and latency can be committed flat; an accuracy commitment must name its population, its measurement method and cadence, and its exclusions.

| Situation | Answer | Why |
|---|---|---|
| Client wants "95% accuracy" in the contract | Commit per segment, with the scoring method, the cadence, and the excluded segments named | Accuracy depends on the client's future input mix, which the provider does not control |
| Provider offers only availability and latency, no accuracy commitment | Insufficient | Pushes all performance risk to the client and leaves them unable to plan |
| Client's input mix is contractually fixed and monitored | A tighter accuracy commitment is defensible | The uncontrolled variable has been controlled |
| Latency commitment on a provider-hosted endpoint | Commit a percentile, not a maximum | Tail latency on a shared service is not fully controllable |

### Exam scenario: a client asks for a contractual accuracy guarantee on a document-classification service

- ✅ Commit an accuracy figure scoped to a named document population, with the evaluation set, the scoring method, the review cadence, and the excluded document types stated
- ❌ Commit to the aggregate accuracy measured during the pilot — **OVERSPEC**: converts a measurement taken on one input mix into a guarantee about every future input mix
- ❌ Commit to availability and latency only, and state that accuracy cannot be contractually guaranteed — **DISCARD**: drops the commitment the client actually needs instead of qualifying it into something keepable

### ❌ Misconception
"An SLA is an SLA — commit the number we measured." — Availability and latency are provider-controlled; an accuracy figure depends on the client's input distribution and is only keepable when its population, method, cadence, and exclusions are stated.

---

## 6.10 Feedback Loops and Expectation Drift

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Manage stakeholder feedback loops and expectation alignment |
| Discriminator | Does the mechanism recur, and does each item become an evaluation case |
| Structured loop captures | The input · the system output · the expected output · the reviewer |
| Drift direction | Expectations decay toward believing the system is more capable and more finished than it is |
| Failure mode | Anecdotes carry no frequency, so nothing can be prioritised |

### Recurring Structured Loop vs One-Off Correction

Expectations re-inflate at every demonstration, so alignment is a routine; feedback that never reaches the evaluation set changes nothing.

| Situation | Answer | Why |
|---|---|---|
| Sponsor's expectations inflated after a successful demo | Establish a recurring review showing real performance on real inputs against the agreed criteria | A single correction does not hold against continuous drift |
| Users report failures in a shared chat channel | Restructure: capture input, output, expected output, reviewer, and feed the evaluation set | Anecdotes have no frequency and cannot be prioritised |
| Feedback is collected but the evaluation set never grows | Broken loop | The system is measured against a set that diverges from what it processes |
| A single well-argued memo resets the sponsor's understanding | Necessary, not sufficient | Fixes today's gap and none of next quarter's |

### Exam scenario: a sponsor's expectations have inflated after an early period on clean data

- ✅ Establish a recurring review that reports real performance on real production inputs against the agreed acceptance criteria
- ❌ Send a detailed written correction setting out the system's actual limitations — **HALF-MOVE**: accurate and one-time, against a drift that is continuous
- ❌ Open a feedback channel where users raise issues as they encounter them — **WRONG-AXIS**: collects reactions rather than measurements, and produces anecdotes with no frequency

### ❌ Misconception
"We have a feedback channel, so we have a feedback loop." — A loop captures the input, the output, the expected output, and the reviewer, and feeds the evaluation set; a channel that produces anecdotes cannot prioritise anything.

---

## 6.11 Pilot to Scale — the Assumption Audit

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Support lifecycle phases (discovery, design, handoff, monitoring, iteration) |
| Discriminator | Which small-scale assumptions stop holding at large scale |
| The three classes | Input distribution widens · support and human-review load grows · rare failures become routine |
| Sequence | Surface the assumptions first; cost model and model choice follow from them |
| Failure mode | Extrapolating pilot cost and pilot accuracy linearly onto a wider population |

### Assumption Audit vs Capacity Plan

Scaling changes the inputs, not just the volume; the architect's contribution is the list of assumptions at risk, and the cost model is rebuilt on that list rather than extrapolated.

| Situation | Answer | Why |
|---|---|---|
| Successful 40-user pilot going to 800 users | List which input, support-load, and edge-case assumptions may not hold, then rebuild the cost model | The wider population brings input types the pilot never sampled |
| A 1-in-500 failure seen twice in a 200-case pilot | Plan for it as a routine event | Rare is relative to volume; at scale it is several events a day |
| Human review absorbed 12% of pilot volume | Convert to a staffing line at projected volume before rollout | Pilot review was done by the build team and is invisible in the pilot cost |
| Rate limits and infrastructure capacity for the new volume | Necessary, and not the binding constraint | The visible constraint; the input distribution is the one that bites |

### Exam scenario: a successful pilot is to be rolled out to twenty times the user base

- ✅ Identify which assumptions held at pilot scale and may not hold at full scale — input variety, support and review load, edge-case frequency — and rebuild the cost and model-tier decisions on those findings
- ❌ Project infrastructure capacity and rate limits for the new request volume — **HALF-MOVE**: a real and necessary step that skips the assumptions which determine what to project
- ❌ Move to a higher-capability model ahead of rollout to absorb the wider variety of inputs — **ARCHITECTED**: sounds prudent, spends money before anyone has characterised the inputs it is meant to handle

### ❌ Misconception
"The pilot worked, so scaling it is a capacity exercise." — Scaling widens the input distribution, multiplies the support and review load, and turns rare failures into routine ones; the assumption audit comes before the capacity plan.

---

## 6.12 Handoff, Monitoring, and Iteration

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Support lifecycle phases (discovery, design, handoff, monitoring, iteration) |
| Discriminator | Can the receiving team answer "is it still working?" without the original team |
| The four handover items | The evaluation suite · the acceptance criteria · a named owner (a person, with a deputy) · the re-check routine |
| Monitoring layers | Operational telemetry (latency, errors, cost, volume) plus quality telemetry (evaluation scores, human-override rate, confidence distribution) |
| Failure mode | Degradation is silent — nothing crashes, outputs stay plausible while the input distribution moves |

### Operable vs Detectable Handover

Source code and a demonstration make the system runnable; only the suite, criteria, owner, and routine make its degradation detectable.

| Situation | Answer | Why |
|---|---|---|
| System transferring to an internal operations team | Evaluation suite, thresholds, named owner and deputy, re-check cadence, plus the implementation guidance | The receiving team can detect and act without the original team |
| Handover consists of repository access, documentation, and training sessions | Insufficient | Nothing in it detects a change in behaviour |
| Ownership assigned to a team rather than a person | Insufficient | A distributed owner is no owner |
| Complaints rise post-launch while error rates are flat | Check input-distribution shift and re-run the evaluation suite | Silent quality degradation does not show in operational telemetry |
| Evaluation set unchanged twelve months after launch | Broken iteration | The set has drifted away from what the system actually processes |

### Exam scenario: a delivered system is being handed to the client's internal team

- ✅ Transfer the evaluation suite, the acceptance thresholds and the trigger for action, a named owner with a deputy, and the routine for re-running the suite on a stated cadence and after any model or input-format change
- ❌ Transfer the repository, complete architecture documentation, and run training sessions for the receiving team — **ARCHITECTED**: comprehensive and effortful, and silent on how the team detects that the system has stopped working
- ❌ Retain a support arrangement with the delivery team for the first year — **REPAIR**: keeps the capability with the wrong party and defers the handover rather than completing it

### ❌ Misconception
"Handover is complete when the team has the code, the documentation, and a walkthrough." — Degradation in these systems is silent, so a handover is only complete when the receiving team holds the evaluation suite, the criteria, a named owner, and the routine for re-checking.
