# CCAR-P Lesson — Domain 6: Stakeholder Communication & Lifecycle Management

**Weight:** 14% (official exam guide v1.0, effective July 2026)

**The five published objectives, verbatim from §6 of the guide:**
1. Conduct structured discovery and requirement gathering
2. Communicate architectural decisions and trade-offs
3. Manage stakeholder feedback loops and expectation alignment (including SLAs)
4. Document architectures and provide implementation guidance
5. Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

---

## Why this domain is worth more attention than it looks

Domain 6 is 14% of the blueprint. Domain 5, Governance, Safety & Risk Management, is another 14%.
Together they are 28% — more than Integration (19%), more than Solution Design (17%). The exam
guide states weights, not per-domain item counts, so the exact number of items is not published; on
a 63-item paper, 14% is the weight of a meaningful block either way. There is no per-domain floor
score, so a weak Domain 6 does not fail you by itself. It just quietly takes 14% of your ceiling
with it.

Technically strong candidates lose marks here, and the reason is structural rather than careless.
The vocabulary of this domain — discovery, alignment, expectations, handoff — is the vocabulary of
soft skills, and soft skills feel like the part of an exam where several answers could be defended.
That intuition is wrong for this paper. The answers in Domain 6 are as determinate as the answers in
Integration. A discovery question either establishes a testable requirement or it does not. A metric
either informs the decision the stakeholder is about to make or it does not. A handover package
either lets the receiving team detect degradation next year or it does not. These are binary
properties of an artifact, and the exam tests them as such.

For a management consultant this is unusually friendly ground. You have run discovery workshops. You
have written a steering-committee pack that had to survive a hostile CFO. You know that a
recommendation without its alternatives is an assertion, not a recommendation. Most of Domain 6 is
that instinct, already correct, needing only to be converted into the vocabulary the exam uses and
sharpened at the two or three points where AI systems genuinely change the advice.

### The through-line

All five objectives are one discipline seen at five moments: **an AI system's behaviour is
probabilistic and drifting, so every commitment made about it must be bounded, measured, and
re-checkable.**

Read the objectives again with that in mind.

- Discovery bounds the requirement, because "as accurate as possible" cannot be designed against.
- Communicating trade-offs bounds the claim, because a single aggregate accuracy number conceals the
  variance that will define the stakeholder's actual experience.
- Feedback loops and SLAs bound the promise, because a commitment made about a probabilistic system
  needs a stated measurement method and a stated exclusion list or it will be read as a guarantee.
- Documentation bounds the decision, because a design recorded without its alternatives and its
  constraints cannot be revisited when those constraints change.
- Lifecycle support bounds the *time* over which all of the above holds, because model versions
  change, input distributions shift, and a system that was correct at handover is not therefore
  correct a year later.

Where a Domain 6 question feels ambiguous, ask which option makes something bounded and checkable
that was previously open-ended. That option is nearly always the key.

---

## Objective 1 — Conduct structured discovery and requirement gathering

### The concept, from first principles

Discovery exists to convert a stakeholder's stated want into a specification an engineer can build
against and a tester can verify. It is a translation problem, and it has a failure mode: a
requirement that cannot be falsified. "Fast," "accurate," "reliable," "as good as a human" — none of
these can be designed against, because no design can be shown to have met them and no design can be
shown to have missed them.

Consulting discovery already carries most of this. You elicit the business problem before the
solution, you separate the sponsor's want from the user's need, you write acceptance criteria into a
statement of work. Three things change when the system being specified is an LLM system.

**First: acceptance criteria become statistical.** A deterministic system either produces the right
output for a given input or it has a bug. An LLM system has an accuracy distribution. The
requirement is therefore not "the system classifies claims correctly" but "the system reaches ≥92%
top-label accuracy on a held-out set of 400 claims, stratified to match last quarter's claim mix."
Every word of that is doing work: the number, the sample, the stratification, and the fact that the
set is held out.

**Second: the cost of an error becomes a design input, not a footnote.** Errors in a probabilistic
system are certain — only their rate and their direction are negotiable. Establishing what a false
positive costs and what a false negative costs is what determines whether the design biases toward
recall or precision, where human review sits, and what the confidence threshold should be. A sponsor
who cannot tell you what a wrong answer costs has not yet given you enough to design a system.

**Third: the input distribution has to be interrogated, not assumed.** Ask what fraction of inputs
are the clean, standard case the sponsor has in mind, and what the long tail actually contains.
Almost every unpleasant surprise in an AI deployment is a tail that nobody characterised during
discovery.

### Worked example

An insurer's claims director asks for "an AI that reads incoming claims and routes them to the right
handler, as accurately as possible."

Three of the questions that turn this into a specification, with the reason each one is asked:

> **"When a claim is routed to the wrong handler today, what happens next and what does it cost?"**
> Establishes the error cost, and reveals whether errors are self-correcting. If a misrouted claim
> is spotted by the receiving handler in ten minutes and forwarded, the tolerable error rate is much
> higher than if it sits in a queue for four days.
>
> **"What accuracy do your handlers achieve on this routing today, and how do you know?"**
> Establishes the baseline and — more usefully — reveals whether anyone measures it. Often no one
> does, which means the real requirement is not "beat the humans" but "be measurable at all," and
> that is a materially different engagement.
>
> **"Of last quarter's claims, what proportion were the standard motor and household types, and what
> was in the remainder?"**
> Characterises the input distribution. If 78% are two clean categories and the remaining 22% span
> forty edge types, the design and the pilot both have to be built around that split rather than
> around the 78%.

The output of discovery is a written requirement the sponsor signs, in roughly this form:

> The system assigns one of nine handler queues to each incoming claim. Target: ≥92% correct
> assignment measured on a held-out set of 400 claims stratified to the prior quarter's mix.
> Claims below a 0.75 model confidence score route to a human triage queue rather than to a handler;
> that queue is expected to absorb 10–15% of volume at launch. A misrouted claim currently costs a
> mean 1.4 days of cycle time; the programme accepts up to 8% misrouting on the automated portion
> against a measured baseline of 11% today.

Every clause is testable. That is the only property that matters.

### How the exam probes it

The scenario shape: a stakeholder states a requirement in unbounded or purely qualitative terms —
"as accurate as possible," "reliable enough for production," "at least as good as our current team"
— and the question asks what the architect should do first, or what the most important next step is.

The key is the option that converts the requirement into something measurable *before* design
proceeds: establish the target accuracy the use case requires, the measurement method, and the cost
of an error. The word "first" in the stem is usually load-bearing. Several options will describe
things a competent architect genuinely does; the discriminator is sequence, and quantifying the
requirement precedes all of them.

A second, subtler shape gives you a stakeholder who has arrived with a solution already chosen ("we
want a multi-agent system that…") and asks how to proceed. The key surfaces the underlying business
problem and the decision the system is meant to serve, without either rejecting the stakeholder's
idea outright or simply building it.

### Wrong turns, and why they are tempting

**Designing against the unbounded requirement anyway, aiming high.** Choosing the strongest model and
the most thorough pipeline "to maximise accuracy" feels responsible, and on a technical domain it
would sometimes be right. Here it fails on its own terms: without a target, there is no basis for
declaring the system finished, no basis for a cost trade-off, and no basis for the sponsor to accept
delivery. Maximising an unbounded objective is not rigour; it is an open-ended bill.

**Benchmarking first.** Running a quick evaluation on sample data before defining the target is
attractive because it produces a number fast. The number is uninterpretable — 89% is either
excellent or unusable, and only the error cost tells you which.

**Escalating to the sponsor's superior, or refusing to start.** Both appear as options, both look
like the answer to an impasse. Neither is the architect's move. Establishing the requirement is your
job, not an obstacle to your job.

### Takeaways

- An unbounded requirement is not a requirement. Bound it before designing.
- Bound it in four parts: the target number, the measurement method, the evaluation set, and the cost
  of an error.
- Establish the input distribution during discovery, including the tail.
- Acceptance criteria for a probabilistic system are statistical and stratified, never binary.
- A stakeholder who arrives with a solution has still not stated a problem. Get the problem.

---

## Objective 2 — Communicate architectural decisions and trade-offs

### The concept, from first principles

An architectural decision made by one person and understood by one person is a liability. It cannot
be challenged before it is expensive, it cannot be revisited when the constraint that drove it
changes, and it cannot be defended when a stakeholder asks why the system costs what it costs.
Communicating the decision is what makes it an organisational asset rather than a personal one.

The professional standard has three parts.

**State the trade-off, not just the choice.** Every architectural decision spends something to buy
something. A stakeholder who is told only what was chosen has been given a conclusion without the
reasoning, and will treat the next constraint change as a reason to distrust the architect rather
than as a reason to revisit the decision.

**Report performance in the shape the system actually has.** This is where AI systems break the usual
consulting advice most sharply. A single headline number is normally good communication practice —
it is the pyramid principle working correctly. For a system whose performance varies sharply by case
type, a single aggregate number is actively misleading, because the aggregate is a weighted average
over a mix that will change. A system at 94% on standard cases and 61% on complex ones reports as
"87% accurate" only until the case mix shifts, at which point the number moves for reasons nobody
can explain.

The professional answer has three components: **break performance out by case type**, **state how it
was measured**, and **give the end-to-end business outcome including human review**. The third
matters because the sponsor is not buying a model; they are buying an outcome from a process that
contains a model and some people. A model at 61% on complex cases inside a workflow that routes
low-confidence complex cases to a specialist may deliver a better end-to-end result than the
headline suggests, and the sponsor deserves that number too.

Note the two failure directions. A flattering aggregate misleads. Refusing to quantify — "accuracy
varies, it depends on the case" — fails the sponsor, who has a budget decision to make and cannot
make it on a shrug. The exam tests both directions, so drill both.

**Translate without diluting.** Explaining a trade-off to a non-technical audience means changing the
vocabulary, not softening the content. "We chose the smaller model because latency at 40,000 daily
requests is the binding constraint" becomes "at your volume, the more capable model would add about
two seconds to every request and roughly £18,000 a month, and it improves accuracy on about 4% of
cases." Same decision, same trade-off, priced in the units the audience owns.

### Worked example

The sponsor of the claims-routing system asks, in a steering meeting: "So how accurate is it? Give me
one number I can take to the board."

The answer that fails: "87%." The mix that produced 87% is not stable, and the number will move next
quarter for reasons unrelated to the system.

The answer that also fails: "It's hard to reduce to one number." True, and useless.

The answer that works:

> "Three numbers, because one would mislead you. On the two standard claim types, which are 78% of
> your volume, it assigns the correct queue 94% of the time. On the remaining 22% — the mixed and
> unusual claims — it is at 61%. Both figures are measured on 400 claims from last quarter that the
> system has never seen, scored against your senior handlers' own assignments.
>
> The number for the board is the third one. With low-confidence claims routed to human triage, 91%
> of all claims reach the right handler without any manual step, against 89% today, and mean routing
> time falls from 4.2 hours to 11 minutes. The 22% complex tail is where the remaining error sits,
> and that is the segment we would target next."

That is one paragraph, it is honest about the weak segment, it is quantified, and it gives the board
the outcome rather than the component.

### How the exam probes it

The dominant scenario: an executive or sponsor demands a single accuracy figure, or has been given
one and is now planning against it, and the system's performance varies by input type. Choose the
option that segments by type, states the measurement basis, and reports the end-to-end outcome
including human review.

A second shape gives you a stakeholder asking why a system cannot simply be fully automated. The key
names *which specific decisions* carry accountability or cannot be verified by the system, and what
automating them would risk. Generic appeals to "AI isn't perfect" or "we need a human in the loop for
safety" are the wrong register — they are true, unspecific, and give the stakeholder nothing to
decide with. The useful answer sounds like: "Three of the nine queues cover claims with a
regulatory-reporting obligation. The system can identify the claim type, but it cannot attest that
the reporting decision was made by an accountable person, and that attestation is what your
regulator asks for. Automating those three would save about 4% of volume and would remove the audit
trail on the part you are most examined on."

A third shape: a technical trade-off must be explained to a non-technical audience. The key states
the trade-off in business units. Distractors either dump the technical detail unchanged or remove the
trade-off entirely and present the choice as obviously correct.

### Wrong turns, and why they are tempting

**The flattering aggregate.** Reporting 87% is not dishonest in intent, and it is what the stakeholder
asked for. It is wrong because the number is unstable and conceals the segment where the risk lives.

**Declining to quantify.** Attractive because it is technically defensible and feels appropriately
humble. It leaves the sponsor unable to decide, which is a failure of the architect's role.

**Reporting only the model metric.** Offering the model's accuracy without the end-to-end outcome
answers a question the sponsor did not ask. They are accountable for the process, not the component.

**Explaining the mechanism instead of the trade-off.** Describing how retrieval-augmented generation
works to a CFO who asked why the system costs £30,000 a month is a category error, and a common one
among strong engineers.

### Takeaways

- Segment performance by case type whenever performance varies by case type.
- Always state the measurement method and the evaluation set alongside the number.
- Report the end-to-end business outcome, human steps included, not just the model metric.
- Refusing to quantify is a failure mode, equal in weight to the misleading aggregate.
- When asked why full automation is not possible, name the specific decisions and the specific risk.
- Translate into the audience's units; do not soften the content.

---

## Objective 3 — Manage stakeholder feedback loops and expectation alignment (including SLAs)

### The concept, from first principles

Expectations about an AI system decay in one direction: toward believing it is more capable, more
consistent, and more finished than it is. Demonstrations show the good case. Early usage is on the
clean subset. Every conversation that does not actively correct the picture lets it drift optimistic.
A feedback loop is the mechanism that keeps the stakeholder's mental model attached to the system's
actual behaviour.

The two components are the loop and the commitment.

**The loop** has to be structured to be useful. Ad hoc feedback — a channel where users post
complaints, a monthly call where someone recounts a bad experience — produces anecdotes, and
anecdotes cannot be prioritised because they carry no frequency. A structured loop captures the
input, the output, the expected output, and the reviewer, so that a reported failure becomes a case
that can be added to the evaluation set. That is the point of the loop: **feedback that does not
become an evaluation case is entertainment.** The consulting analogue is a RAID log, and the same
discipline applies — a risk that is not written with an owner and a date is a conversation.

**The commitment** is where AI systems change the standard advice. A conventional SLA commits to
availability and latency, both of which are properties of infrastructure and both of which the
provider controls. A commitment about *accuracy* is different in kind, because accuracy depends on
the input distribution, which the provider does not control. Committing to "95% accuracy" without
qualification is a promise about the customer's future data, and you cannot keep it.

The professional form of an AI-system service commitment has four parts:

1. **What is committed** — availability, latency percentile, and where relevant an accuracy figure.
2. **On what population** — the input segment the figure applies to, defined precisely.
3. **How it is measured** — the evaluation set, the scoring method, the cadence.
4. **What is excluded** — the segments and conditions the commitment does not cover.

The fourth is the one people omit, and it is the one that prevents the dispute. A metric stated
without what it does not cover will be read as covering everything.

The same logic gives the general rule for metric choice: **a useful metric is the one tied to the
decision the stakeholder actually faces, stated together with what it does not cover.** An operations
director deciding staffing needs the volume that reaches human review and its variance, not a
per-token cost. A CFO deciding renewal needs cost per processed claim and its trajectory at projected
volume, not latency percentiles. Choosing the metric is an act of understanding the decision.

### Worked example

A service commitment for the claims-routing system, written to be signed:

| Commitment | Value | Population | Measurement | Excluded |
|---|---|---|---|---|
| Availability | 99.5% monthly | All requests | Provider status log, monthly | Scheduled maintenance windows, notified 5 days ahead |
| Response time | 95th percentile under 6 seconds | All requests | Application-side timing, monthly | Requests over 40,000/day |
| Routing accuracy | ≥90% correct queue | Standard motor and household claims only | 400-claim stratified sample, scored quarterly by two senior handlers | Complex and mixed claims (~22% of volume), which route to human triage |
| Triage volume | 10–15% of claims to human queue | All requests | Queue counts, monthly | Periods following a claim-form change, for 30 days |

The accuracy row does the real work. It commits to a number, names the population, names the scoring
method and cadence, and states plainly that the complex tail is not covered. A sponsor reading this
cannot later be surprised by the complex tail, which is the entire purpose.

The feedback loop that sits behind it, in one sentence a client will accept:

> "Every claim a handler re-routes is logged with the original claim text, the system's assignment,
> and the handler's correction; the operations lead reviews the log fortnightly and any recurring
> pattern is added to the evaluation set before the next quarterly scoring run."

### How the exam probes it

Scenario shape one: a stakeholder wants a service commitment on an AI system, or has proposed a flat
accuracy SLA. The key qualifies the commitment by population, measurement method, and exclusions.
Distractors either commit to the flat number, or refuse to commit to accuracy at all and offer only
availability and latency.

Scenario shape two: a stakeholder has an inflated expectation after a successful demonstration or an
early clean-data period. The key establishes a structured, recurring channel that shows real
performance on real inputs against the agreed criteria. Distractors offer a one-off correction — a
meeting, a memo, a caveat slide — which is a HALF-MOVE, since expectations drift continuously and a
single correction does not.

Scenario shape three: which metric to report to a named role. The key matches the metric to that
role's decision. Distractors offer metrics that are real, measurable, and irrelevant to the decision
in front of that person.

### Wrong turns, and why they are tempting

**Committing to a flat accuracy number.** It is what the client asks for and it closes the
negotiation. It is a promise about data you do not control.

**Refusing to commit to accuracy at all.** Technically safe, and it looks like discipline. It pushes
the entire performance risk onto the client and leaves them unable to plan.

**Treating an unstructured feedback channel as a feedback loop.** A shared inbox or chat channel is
genuinely responsive and feels collaborative. It produces anecdotes with no frequency data, so
nothing can be prioritised and nothing reaches the evaluation set.

**Correcting an expectation once.** A well-argued email that resets the sponsor's understanding is
better than nothing and worse than a routine. Expectations re-inflate at the next demo.

### Takeaways

- Structure feedback so that each item becomes an evaluation case, with the input, the output, and
  the expected output captured.
- An accuracy commitment must name its population, its measurement method, its cadence, and its
  exclusions.
- State what a metric does not cover, in the same breath as the metric.
- Pick the metric from the stakeholder's decision, not from the dashboard.
- Expectation alignment is a recurring routine, not an event.

---

## Objective 4 — Document architectures and provide implementation guidance

### The concept, from first principles

Documentation of an architecture serves a reader you have not met, at a moment you cannot predict,
usually when something has changed. That reader's question is almost never "what does this system
do" — they can read the code for that. It is "why is it like this, and can I change it?"

A document that records only the chosen design cannot answer that question. The reader sees a
component and has no way to distinguish a load-bearing constraint from an arbitrary preference, so
they either change nothing out of fear or change something that mattered. Both outcomes cost more
than writing the document properly would have.

Hence the architecture decision record, whose four parts are the whole discipline:

1. **The decision** — what was chosen, stated plainly.
2. **The alternatives considered** — what else was on the table, and what each would have given up.
3. **The trade-offs** — what this choice spends and what it buys.
4. **The constraints that drove it** — the facts about the world that made this the right choice.

The fourth part is the one that gives the document its life. Constraints expire. A model choice made
under a latency ceiling is revisitable the moment the ceiling moves — but only if the ceiling was
written down. An ADR without its constraints is a decision that can never be safely reopened.

For an AI system there is a fifth thing worth recording, though it lives under constraints: **the
performance the decision was based on, and the evaluation that produced it.** "We chose model X" is
weak; "we chose model X after it reached 86.7% on the 400-claim stratified set against model Y's
88.0%, because the 1.3-point gap did not justify 2.1 seconds of added latency at 40,000 daily
requests" is a decision a successor can re-run when either number changes.

Implementation guidance is the adjacent artifact and answers a different question: not "why" but
"how do I build this without rediscovering your reasoning." It carries the interface contracts, the
configuration that matters and why, the failure modes and what to do about each, and the tests that
must pass. Prose describing the system is not implementation guidance.

ADRs are also, incidentally, the cheapest revision material this exam offers. The roadmap for this
project already notes that keeping an architecture decision record during real production work
doubles as Solution Design and Stakeholder revision, and that is not a motivational flourish — the
four parts of an ADR are the four things Domain 6 questions ask you to identify.

### Worked example

An ADR for the model choice on the claims-routing system, in the compact form that actually gets
written:

> **ADR-014: Model selection for claim classification**
> **Status:** Accepted, 2026-09-03. Supersedes nothing. Revisit if daily volume falls below 15,000 or
> the latency ceiling is relaxed.
>
> **Decision.** Use the mid-tier model for claim classification, with low-confidence cases routed to
> human triage.
>
> **Alternatives considered.**
> *(a)* The frontier model for all claims — 88.0% on the evaluation set, but adds 2.1s median latency
> and roughly £18,000/month at projected volume.
> *(b)* A fine-tuned smaller model — potentially cheaper still, but requires a labelled corpus the
> client does not have and adds a retraining obligation to the operating model.
> *(c)* Two-stage routing, small model first with escalation — rejected for now; adds a failure
> surface for a 1.3-point gain. Recorded as the first thing to reconsider if the complex tail grows.
>
> **Trade-offs.** Spends 1.3 points of accuracy on the evaluation set. Buys a 2.1s latency margin
> against the 6s 95th-percentile commitment and £18,000/month. The accuracy given up falls almost
> entirely in the complex tail, which routes to human triage regardless, so the end-to-end impact is
> smaller than the model-level gap suggests.
>
> **Constraints that drove it.** 95th-percentile response under 6s, contractually committed.
> Projected volume 40,000/day. No labelled training corpus available. Complex claims (22% of volume)
> already have a human triage path for regulatory reasons.

Two hundred words, and a successor in eighteen months can tell instantly whether the decision still
holds.

### How the exam probes it

Scenario shape one: a team is documenting an architecture, or a stakeholder asks what the
documentation should contain. The key includes alternatives, trade-offs, and driving constraints
alongside the decision. Distractors offer a thorough description of the chosen design — often with
appealing extras like detailed diagrams and a full component inventory — which is the ARCHITECTED
distractor: more effort, missing the load-bearing content.

Scenario shape two: a decision made a year ago is being questioned because a constraint has changed.
The key traces back to the recorded constraint and re-evaluates. Distractors re-derive the decision
from scratch, or defend it on authority.

Scenario shape three: a receiving team must implement or extend the system. The key supplies
interface contracts, configuration rationale, failure modes, and the tests that must pass.
Distractors offer a walkthrough session or a narrative overview document — both HALF-MOVEs, since
neither survives the first personnel change.

### Wrong turns, and why they are tempting

**Documenting the design without the alternatives.** This is the default output of a competent
engineer writing up their work, and it looks complete. It cannot support revisiting.

**Recording the trade-off but not the constraint.** Half the discipline, and the half that ages
badly. Trade-offs are stable; constraints expire, and only a recorded constraint can be checked for
expiry.

**Substituting a diagram.** A good architecture diagram is valuable and answers "what," never "why."

**Substituting a recorded walkthrough.** It transfers knowledge once, to whoever watches it, and goes
stale the first time the system changes.

### Takeaways

- An ADR carries four things: decision, alternatives, trade-offs, driving constraints.
- Record the evaluation numbers the decision rested on, so it can be re-run.
- Write a revisit trigger into the record — the condition under which this should be reopened.
- Implementation guidance is contracts, configuration rationale, failure modes, and tests.
- A diagram or a walkthrough recording is a supplement, never the artifact.

---

## Objective 5 — Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

### The concept, from first principles

The five phases are named in the objective, which means the exam expects you to know which phase a
scenario is in and what the architect owes at that point. The two phases that carry most of the
marks are the ones where things are handed across a boundary: pilot to scale, and delivery to
operations.

**Pilot to scale.** A pilot succeeds under conditions the pilot itself created: a narrow user group,
a curated or naturally clean input set, close support from the people who built it, and a volume low
enough that edge cases have not been sampled. Scaling changes all four at once. The architect's
contribution at this moment is not a capacity plan — it is an **explicit list of which assumptions
held at small scale and may not hold at large scale.** Cost and model choice follow from that list;
they are not the starting point.

The three assumption classes worth naming every time:

- **Inputs.** Wider user population means wider input distribution. Formats, languages, quality, and
  edge types the pilot never sampled arrive at scale. This is the assumption that breaks most often
  and the one nobody writes down.
- **Support load.** Pilot users had direct access to the team. At ten times the users, the same
  question rate becomes a support function that does not exist yet, and the human-review queue that
  absorbed 12% of pilot volume becomes a staffing line item.
- **Edge cases.** A 1-in-500 failure is invisible in a 200-case pilot and is eighty events a day at
  scale. Rare events are only rare relative to volume.

**Delivery to operations.** A handover that survives its first year is defined by what the receiving
team can do without you. They must be able to answer "is it still working?" without your judgement.
That requires four things: **the evaluation suite**, **the criteria** (what score means acceptable
and what triggers action), **a named owner**, and **the routine** — the cadence at which the suite is
re-run and the results reviewed.

Source code and a demonstration give the receiving team the ability to run the system and no ability
to tell whether it is still right. That gap is the single most consequential handover failure in AI
delivery, because degradation in these systems is silent. Nothing crashes. The outputs keep looking
plausible while the input distribution moves underneath them.

**Monitoring and iteration** follow from the handover package. Monitoring here means two layers:
operational telemetry (latency, error rates, cost, volume) and quality telemetry (evaluation scores,
human-override rates, confidence distribution). The second layer is what catches drift, and it is the
layer teams skip because the first is what their existing tooling already provides. A rising
human-override rate on a stable input volume is the earliest honest signal that a system is
degrading, and it costs nothing to collect because the overrides are already happening.

### Worked example

The handover package for the claims-routing system, as a signed checklist:

> **Transferred to Claims Operations, 2026-11-14. Accountable owner: the Claims Operations
> Systems Lead.**
>
> 1. **Evaluation suite.** 400 stratified claims with senior-handler labels, plus 60 cases added from
>    the pilot's override log. Runnable by one command; produces per-segment accuracy.
> 2. **Criteria.** Standard segment ≥90% and complex segment ≥55% are acceptable. Below either, or a
>    human-override rate above 18% for two consecutive weeks, raises a defect and pauses any pending
>    configuration change.
> 3. **Routine.** Suite re-run quarterly, and additionally within 10 working days of any model
>    version change or claim-form change. Results tabled at the monthly operations review.
> 4. **Owner.** Named above, with a named deputy. The override log review is fortnightly and belongs
>    to the same owner.
> 5. **Guidance.** Interface contracts, the confidence-threshold rationale (ADR-017), the four known
>    failure modes with the response to each, and the regression tests that must pass before any
>    prompt or model change ships.

The demonstration and the repository access are assumed. They are not what makes this a handover.

### How the exam probes it

Scenario shape one: a pilot has succeeded and the organisation wants to roll it out to ten or twenty
times the users. The key surfaces which pilot assumptions may not survive the scale change,
specifically around input variety, support and review load, and edge-case frequency. Distractors go
straight to infrastructure capacity, straight to model upgrade, or straight to a cost projection —
each is a real activity that has skipped the step that would tell you what to project.

Scenario shape two: a system is being handed to an internal team. The key includes the evaluation
suite, the acceptance criteria, a named owner, and the re-check cadence. Distractors offer
comprehensive documentation plus training sessions — thorough, well-intentioned, and silent on how
the receiving team detects degradation.

Scenario shape three: a system in production is producing more complaints than at launch, with no
error-rate change. The key looks at input distribution shift and re-runs the evaluation suite.
Distractors reach for a model upgrade or a prompt rewrite before establishing what changed.

### Wrong turns, and why they are tempting

**Scaling as a capacity question.** Rate limits and infrastructure are the visible constraint and the
easiest to plan, so they absorb the attention. The input distribution is the constraint that actually
bites, and it is invisible until it arrives.

**Handing over code and a demonstration.** This is what "handover" means in most software contexts
and it feels complete. For a probabilistic system it omits the only mechanism by which the receiving
team can detect that anything has gone wrong.

**Naming a team rather than a person as owner.** A distributed owner is no owner, and this is the
distractor that most often looks acceptable.

**Treating go-live as the end of the engagement.** Iteration is a named phase in the objective. A
system whose evaluation set never grows after launch is one whose evaluation set is steadily
diverging from what it actually processes.

### Takeaways

- At pilot-to-scale, list the assumptions before the costs. Inputs, support load, edge cases.
- A handover is the evaluation suite, the criteria, a named owner, and the routine.
- Degradation in AI systems is silent. Detection must be built, not assumed.
- Monitor quality telemetry, not just operational telemetry. Human-override rate is the cheapest
  early signal available.
- The evaluation set is a living artifact; feedback and production failures are added to it.

---

## Synthesis — one engagement, five phases

Follow the claims-routing engagement end to end and watch the same discipline recur.

**Discovery.** The claims director asks for routing "as accurately as possible." You do not design.
You establish that a misrouted claim costs a mean 1.4 days of cycle time, that the current human
baseline is roughly 11% misrouting and has never been measured formally, and that 78% of volume is
two clean claim types while 22% spans a long tail. You write the requirement with a number, a
measurement method, a held-out stratified evaluation set, and a stated error cost. The sponsor signs
it. **Bounded.**

**Design.** You evaluate two models against the 400-claim set. The frontier model wins by 1.3 points
and loses on latency and cost at 40,000 requests a day. You write ADR-014 with the decision, the
three alternatives, the trade-off, the driving constraints, and the condition under which the
decision should be reopened. **Recorded with its expiry conditions.**

**Communication.** In the steering meeting the sponsor asks for one number. You give three: 94% on
the standard segment, 61% on the complex tail, 91% end-to-end with human triage against 89% today,
all measured on unseen claims scored by senior handlers. You state the complex tail as the remaining
risk. When the sponsor asks why the tail cannot be automated too, you name the three queues carrying
a regulatory-reporting obligation and explain that the system can identify the claim type but cannot
attest that an accountable person made the reporting decision. **Segmented, measured, specific.**

**Commitment.** The SLA commits 99.5% availability, a 6-second 95th-percentile response, and ≥90%
routing accuracy *on the standard segment only*, scored quarterly on the stratified sample by two
senior handlers, with the complex tail explicitly excluded and routed to human triage. The
handler-override log feeds the evaluation set fortnightly. **Qualified and re-checkable.**

**Pilot to scale.** The pilot ran with 40 handlers on one region's claims. Before the national
rollout you table the assumptions at risk: the input distribution widens across regions with
different claim-form versions; the human triage queue at 12% of pilot volume becomes 4,800 claims
a day at national volume, a staffing line item rather than a rounding error; the 1-in-500
malformed-attachment failure that appeared once in the pilot becomes dozens of events per day. The cost model and the model-tier decision are then rebuilt on those
numbers rather than extrapolated from the pilot. **Assumptions before arithmetic.**

**Handoff.** Claims Operations receives the evaluation suite, the per-segment thresholds, the
override-rate trigger, a named systems lead with a named deputy, the quarterly-plus-on-change re-run
routine, and the implementation guidance with the four known failure modes. **Detectable.**

**Iteration.** Six months later, complaints rise while the error rate is flat. The override log shows
the increase concentrated in one region that changed its claim form. The suite is re-run, the new
form's cases are added to the evaluation set, and ADR-014's revisit trigger is checked — volume is
still above 15,000/day, so the model decision stands. The prompt is adjusted for the new form and the
regression tests pass. **The loop closed because it was built to close.**

Every phase did the same thing to a different object: made a claim about a probabilistic system
bounded, measured, and checkable again later.

---

## Misconceptions

| Misconception | Correction |
|---|---|
| "The stakeholder domain is judgement; several answers could be defended." | Each option either produces a bounded, verifiable artifact or does not. That is a binary property, and it is what the item is testing. |
| "The sponsor asked for one number, so give them one number." | Where performance varies sharply by case type, an aggregate misleads. Segment it, state the measurement method, and give the end-to-end outcome. |
| "Accuracy varies too much to quantify responsibly." | Refusing to quantify fails the sponsor, who has a budget decision to make. Quantify per segment with the method stated. |
| "'As accurate as possible' means aim as high as we can." | An unbounded requirement cannot be designed against or verified. Establish the accuracy the use case needs and the cost of an error before designing. |
| "Design documentation should describe the chosen architecture thoroughly." | The chosen design answers "what." A decision record must also carry the alternatives, the trade-offs, and the constraints that drove the choice, or it can never be safely revisited. |
| "The SLA should commit to the accuracy we measured." | An accuracy commitment must name its population, its measurement method, its cadence, and its exclusions. A bare number is a promise about data you do not control. |
| "If the pilot worked, scaling it is a capacity exercise." | Scaling changes the input distribution, the support and review load, and the frequency of rare failures. Name which assumptions may not survive, then rebuild the cost model on those. |
| "Handover is complete when the team has the code and a walkthrough." | The receiving team must be able to answer "is it still working?" without you: evaluation suite, criteria, named owner, re-check routine. |
| "A shared channel for user feedback is a feedback loop." | Unstructured feedback produces anecdotes with no frequency. A loop captures input, output, expected output, and reviewer, and feeds the evaluation set. |
| "We corrected the sponsor's expectations in the last meeting." | Expectations re-inflate at every demo and every clean-data period. Alignment is a recurring routine. |
| "Naming the operations team as owner is sufficient." | A distributed owner is no owner. Name a person and a deputy. |
| "Once it's live, the engagement is delivery-complete." | Iteration is a named lifecycle phase. An evaluation set that never grows after launch diverges from what the system actually processes. |
| "Explaining why full automation isn't possible means explaining that AI is imperfect." | Name the specific decisions that carry accountability or cannot be verified, and state what automating them would risk. |

---

## Quick reference

**The through-line.** Every commitment about a probabilistic system must be bounded, measured, and
re-checkable. When an option makes something open-ended into something checkable, it is usually the
key.

**Discovery — bound it in four parts**
Target number · measurement method · evaluation set · cost of an error.
Plus: characterise the input distribution, including the tail.

**Communicating performance — three components**
Break out by case type · state how it was measured · give the end-to-end outcome including human
review.
Both failure directions are tested: the flattering aggregate, and the refusal to quantify.

**Metric choice**
The metric tied to the decision the stakeholder actually faces, stated with what it does not cover.

**Why not full automation**
Name which specific decisions carry accountability or are unverifiable, and what automating them
would risk. Not "AI is imperfect."

**ADR — four parts**
Decision · alternatives considered · trade-offs · constraints that drove it.
Add the evaluation numbers behind it and the condition that reopens it.

**Implementation guidance**
Interface contracts · configuration rationale · failure modes and responses · tests that must pass.

**SLA on an AI system — four parts**
What is committed · on what population · how measured and how often · what is excluded.

**Feedback loop**
Captures input, output, expected output, reviewer. Feeds the evaluation set. Recurring, not ad hoc.

**Pilot → scale — three assumption classes**
Input distribution widens · support and review load grows · rare failures become routine.
Assumptions first; cost and model choice follow.

**Handover — four items**
Evaluation suite · acceptance criteria · named owner (a person) · re-check routine.
Code and a demonstration are assumed, not sufficient.

**Monitoring**
Operational telemetry plus quality telemetry. Human-override rate is the cheapest early drift signal.

**Distractor families to expect in this domain**
ARCHITECTED (a thorough document or programme that omits the load-bearing content) ·
HALF-MOVE (a one-off correction where a routine is required) ·
REPAIR (fixing downstream what discovery should have bounded) ·
WRONG-AXIS (right vocabulary, wrong stakeholder decision) ·
DISCARD (replace the mechanism rather than qualify it) ·
OVERSPEC (a stronger commitment than the requirement asks for — a flat accuracy SLA is the classic).
