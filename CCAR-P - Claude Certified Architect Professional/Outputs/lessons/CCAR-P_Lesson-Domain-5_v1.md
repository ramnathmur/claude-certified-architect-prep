# Lesson — Domain 5: Governance, Safety & Risk Management

**Exam:** Claude Certified Architect – Professional (CCAR-P)
**Weight:** 14% (source: official exam guide v1.0, effective July 2026)

**The five published objectives, verbatim:**
1. Implement guardrails and safety controls
2. Identify risks, limitations, and failure modes of LLM systems
3. Apply human-in-the-loop validation strategies
4. Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP)
5. Address ethical AI considerations (bias, fairness, transparency)

---

## How to read this lesson

This is a teaching document, not a cram sheet. The corpus file (`CCAR-P_Domain-5_v1.md`) carries the
terse decision rules that generate practice questions. This one carries the mechanism behind each
rule, because a rule you can only recite fails the moment the exam rephrases the scenario, and it
fails much harder in a real client engagement.

Two facts about the paper are worth holding while you read. The exam is 63 items in 120 minutes, and
Domain 5 carries a 14% weight. If weight maps directly to item count, that is roughly nine items —
the guide publishes the weight, not a per-domain item count, so treat the nine as arithmetic rather
than as a stated fact. Two things about the format remain genuinely unresolved in this project's
verified sources: whether items stand alone or are grouped into shared-scenario blocks, and whether
multiple-response items are scored all-or-nothing or with partial credit. Neither is asserted
anywhere in this lesson, and neither should change how you study.

---

## The through-line

Every one of the five objectives is a version of the same question: **where does a property of this
system actually come from?**

A large language model is a conditional probability distribution over text. Given the same input it
may produce different output, and given a well-phrased instruction it will usually — not always —
comply. That is enough to build extraordinary products on. It is not enough to found a guarantee on,
and governance is the discipline of guarantees.

So the domain divides cleanly. Anything that must *tend* to happen can live in the prompt. Anything
that must *always* happen has to live somewhere deterministic: in code that runs before the call, in
code that runs after it, in the credentials the model can and cannot reach, or in a person whose
approval is required before an action executes.

That single distinction — tendency versus guarantee — is the discriminator behind most Domain 5
items. The five objectives are five places it shows up:

- **Guardrails** are the mechanism for converting a tendency into a boundary.
- **Failure modes** are the catalogue of what goes wrong when you mistake one for the other.
- **Human-in-the-loop** is the mechanism for the class of decisions where no automated control is
  sufficient and accountability must attach to a person.
- **Compliance** is the case where an external authority has already decided that a particular
  property is a guarantee, and you no longer get a vote.
- **Ethics** is the case where the property is one nobody has written down for you yet, and the
  architect has to name it, measure it, and be able to account for it afterwards.

A Foundations-level answer identifies which control to add. A Professional-level answer states what
the control costs, what it does not cover, what breaks first, and how it is explained to the person
signing the contract. Keep that bar in mind throughout.

---

# Objective 1 — Implement guardrails and safety controls

## The concept from first principles

A guardrail is a constraint on system behaviour that holds independently of what the model
generates. The independence is the whole point. If the constraint is expressed as text inside the
prompt, it is subject to the same probabilistic process it is meant to constrain, and it can be
argued with, out-competed by a longer instruction elsewhere in context, or simply not followed on
the tail of the distribution.

That gives four layers, and they are layers rather than alternatives because each fails differently.

**Layer 1 — Input validation, before the call.** Schema and type checks on structured fields. Length
and rate limits. Classification of the request against a policy. Detection of regulated data classes
before they are assembled into a request. Screening of retrieved or user-supplied content for
injected instructions. Anything that can be decided without the model belongs here, because this is
the only layer that acts before data has moved.

**Layer 2 — Output filtering, after the call and before the output reaches anyone.** Schema
validation of structured output. Pattern matching for identifiers that must never appear — account
numbers, national IDs, internal hostnames. A classifier pass over free text. A grounding check that
every cited source exists. This layer catches what the model produced, and its limitation is that
the model has already produced it; if generating the content was itself the harm, filtering is late.

**Layer 3 — Scoped permissions.** The set of tools the model can call, the credentials those tools
carry, and the blast radius of each. This is the strongest layer available, because it does not
constrain behaviour at all — it removes the possibility. A model cannot misuse a capability it does
not have.

**Layer 4 — Human approval on consequential actions.** Covered in depth under Objective 3.

The official exam guide's own sample material makes one of these points explicitly: least privilege
means **removing** an unneeded capability, not logging its use or asking for confirmation before it
runs. That is worth internalising as a sentence, because it is one of the very few pieces of
verified answer logic this project holds from the guide itself, and it generalises well past tool
configuration. Detection is not prevention. A log tells you the boundary was crossed.

Why layering rather than one strong control: the failure modes are uncorrelated. Input validation
fails on novel phrasing it was not written for. Output filtering fails on content that is harmful
but well-formed. Permission scoping fails when a legitimate capability is used toward an
illegitimate end. Human review fails to inattention. An attack, or an ordinary accident, has to
clear all four independently, and the probability of that is the product rather than the sum.

## Worked example

An insurance carrier deploys a claims assistant. It reads a submitted claim file, drafts an adjuster
note, and needs three capabilities: look up the policy, fetch the claimant's prior claim history,
and — in the original design — issue a payment.

The guardrail design that survives review:

*Input.* The claim narrative and any attached correspondence are untrusted. They are wrapped in a
delimited block that the system prompt declares as data to be summarised, never as instructions to
be followed. Before assembly, an input pass flags bank account and national ID patterns and replaces
them with tokens.

*Permissions.* `issue_payment` is removed from the assistant's tool list. The assistant emits a
payment *recommendation* — a structured object with a claim ID, an amount, and a rationale. A
separate settlement service, which holds the payment credential and which the model cannot reach,
validates the recommendation against policy limits and the claimant's coverage, then executes.

*Output.* The drafted note is schema-validated. Any string matching an account-number pattern is
stripped, on the assumption that layer 1 will occasionally miss one. Every policy clause the note
cites is verified to exist in the policy document before the note is released.

*Human.* Recommendations above $5,000, and every recommendation to deny, route to a named adjuster.

Notice what the strongest control did. It did not constrain how the model uses `issue_payment`. It
deleted the capability and moved the decision into deterministic code that already existed to make
it. The model went from being an actor in the payment path to being an advisor to it, and the entire
class of "the model issued a payment it should not have" disappeared rather than being mitigated.

## How the exam probes it

Expect a scenario that describes a working system with one control in place and asks what to add, or
what the highest-priority gap is. The four options will typically include one that removes or scopes
a capability and three that observe, log, alert on, or instruct against its misuse. The one that
removes wins.

A second common shape: a system with a prompt-level rule has leaked something or taken an action it
should not, and you choose the fix. The correct answer relocates the constraint from the prompt into
code or into the permission model. The tempting answer strengthens the prompt.

A third shape gives you a system with exactly one very strong control — a well-tuned safety
classifier on output, say — and asks whether the design is sound. It is not, because a single layer
is a single point of failure, and the answer names the missing layers rather than improving the one
that exists.

## The wrong turns and why they tempt

**Strengthening the system prompt.** It is fast, it is cheap, it demos well, and it uses the same
vocabulary as the requirement, which makes it read as directly responsive. It also produces a
measurable improvement in testing, which is exactly what makes it dangerous: a tendency that
improves from 97% to 99.4% is still a tendency.

**Adding logging and alerting and calling it a control.** Observability is genuinely valuable and
belongs in the design. It is not a guardrail, because it acts after the fact. On a question that
asks how to *prevent* something, an option that detects it is wrong-axis.

**Requiring confirmation before a dangerous tool call.** This is a half-move. It is better than
nothing and worse than removal, and it fails when the confirming party is the same automated
pipeline or a human who confirms everything.

**Choosing one sophisticated layer over four modest ones.** A fine-tuned safety model sounds more
architected than four boring checks. Boring checks that fail independently beat one elegant check
that fails alone.

## Takeaways

- A guardrail is a constraint that does not depend on model output. If it lives in the prompt, it is
  a tendency.
- Four layers: input validation, output filtering, scoped permissions, human approval. Design all
  four; a single layer is a single point of failure.
- Least privilege means removing the capability, not logging it or confirming it.
- Prefer moving the model out of the action path over constraining how it acts in the path.
- Detection is not prevention. On a "how do you prevent this" item, monitoring options are
  distractors.

---

# Objective 2 — Identify risks, limitations, and failure modes of LLM systems

## The concept from first principles

Everything in the failure catalogue follows from two facts: the model samples from a distribution
over plausible continuations, and it receives instructions and data through the same channel.

**Confabulation.** The model produces the most plausible continuation given its context. Plausibility
is correlated with truth and is not identical to it. When the two diverge, the output is fluent,
specific, and wrong — and the fluency is a property of the generation process, so it carries no
information about correctness. This is why a model's stated confidence is not a calibrated signal:
"I am highly confident" is generated by the same process that generated the claim.

**Confidently wrong retrieval-grounded output.** Retrieval changes what the model conditions on. It
does not change whether the conditioning material is correct. Give a model a stale or mis-indexed
chunk and it will faithfully and confidently report the contents. The exam guide's own sample
material carries this: a RAG system that turns confidently wrong immediately after a document
refresh points at retrieval and indexing first, not at the model. The timing is the evidence.

**Prompt injection, direct and indirect.** Instructions and data arrive in one channel, so any text
the model reads can attempt to act as an instruction. Indirect injection is the serious case: the
hostile text is not typed by the user but sits inside a retrieved web page, a PDF, a support ticket
body, a code comment, or a calendar invite. This is a property of the architecture rather than a bug
with a patch, which is why the controls are structural — treat retrieved content as untrusted, keep
privilege out of the model's reach, and validate the *action* the model requests rather than the
text that requested it.

**Data leakage, in two directions.** Sensitive data crossing a boundary it should not cross on the
way in, and sensitive context appearing in output it should not appear in on the way out. The
canonical architectural version is a shared retrieval index across tenants with no tenant filter at
query time, which produces cross-customer answers that look entirely normal.

**Non-determinism and version drift.** The same input can produce different output. Model versions
change, and a prompt tuned against one version can degrade against the next without a line of your
code changing. Anything that must be stable needs a pinned model version plus a regression suite
that runs before a version moves.

**Uneven attention over long context.** Material placed in the middle of a long input is used less
reliably than material at the beginning or the end. The fix is positional and structural — key
findings first, explicit headings, structured facts over verbose prose — rather than simply making
the input shorter, since shortening risks discarding the very content that was being missed.

**Cascading error in agentic chains.** Per-step accuracy compounds multiplicatively. A ten-step
agent with 96% accuracy per step is at 0.96^10 ≈ 66% end-to-end, and no single step looks broken in
testing. This is the failure mode that most often surprises architects, because every component
passes its own unit test.

**Automation bias.** A human reviewer presented with fluent, confident output approves it. This is
the failure mode of the human layer, and it is the reason a review step that shows only the
conclusion is close to worthless.

**Cost and latency failure.** A system that is correct and unaffordable at volume has failed. On the
Professional exam this belongs in the risk register alongside the others, because a design that
cannot be operated is not a design.

## Worked example

A hospital network builds a clinical documentation pipeline: retrieve the encounter record, extract
structured findings, reconcile them against the problem list, draft a discharge summary, check it
against formulary rules, and produce a patient-facing version. Six model-touching steps.

Measured per-step accuracy after tuning is 96%. End-to-end correctness is 0.96^6 ≈ 78%, and in
testing every stage looked healthy. The architectural response is not a better model, which moves
each step by a point or two and moves the product by less than you would hope. It is to interrupt
the compounding: after the extraction step, validate every extracted lab value against the
structured source data deterministically, and reject the batch on mismatch; after the formulary
check, validate against the formulary database rather than trusting the model's recollection of it.
Two deterministic checkpoints turn a chain of six probabilistic steps into two short chains with a
hard boundary between them.

The general principle: in an agentic pipeline, the design question is where to put the deterministic
checkpoints, and the answer is immediately after the steps whose errors are cheapest to detect and
most expensive to propagate.

## How the exam probes it

The dominant shape is a symptom with four candidate causes. The discipline is to reason from the
symptom's *timing and shape* to the mechanism rather than pattern-matching on vocabulary.

- Confident wrongness that started right after a content refresh → retrieval and indexing.
- The model has no memory of something said two turns ago, in a short conversation → the application
  is not resending history, not a context-window limit.
- Quality degrades only on long documents, and specifically on material in the middle → positional
  attention, fixed structurally.
- Behaviour changed with no code deployment → model version.
- Every step passes its test and the product still fails a third of the time → compounding.
- The agent took an action nobody asked for, after processing an external document → indirect
  injection.

A second shape asks you to populate a risk register for a described system and pick the highest-risk
item. The Professional-tier answer weights by consequence and reversibility, not by likelihood
alone: a rare irreversible action outranks a frequent recoverable one.

## The wrong turns and why they tempt

**Attributing every failure to the model and reaching for a larger one.** It is a single action that
plausibly improves everything, requires no diagnosis, and is easy to justify to a sponsor. It also
converts a diagnosable engineering problem into a permanent cost increase, and on a retrieval fault
it does nothing at all.

**Treating confabulation as a prompt problem.** "Only answer from the provided context" reduces the
rate. It does not create the guarantee, and a system that requires the guarantee needs verification
outside the model.

**Treating injection as a content-filtering problem.** Filters catch known phrasings. The
architectural fix is that the model has no privilege worth hijacking.

**Under-weighting drift because the system is working now.** Drift is invisible until it is
expensive. Version pinning plus regression evaluation is cheap insurance and reads as unnecessary
bureaucracy right up until the week it is not.

## Takeaways

- Fluency and stated confidence carry no information about correctness; both are generated.
- Diagnose from the symptom's timing and shape. Post-refresh confident wrongness is a retrieval
  fault. A behaviour change without a deployment is a version fault.
- Per-step accuracy compounds. Interrupt long chains with deterministic checkpoints.
- Indirect prompt injection is architectural. The control is removing privilege, not filtering text.
- Rank risks by consequence and reversibility, not frequency alone.

---

# Objective 3 — Apply human-in-the-loop validation strategies

## The concept from first principles

Human review is scarce, expensive, and imperfect. Treat it as a budget to be allocated rather than a
switch to be turned on, and the design question becomes: which items are worth a human's attention?

Two variables answer it.

**Consequence** — what it costs if this output is wrong. Reversibility matters more than magnitude:
a draft that a person reads before sending is recoverable; a payment issued, a message sent, a
record deleted, or an adverse decision communicated to a customer is not.

**Confidence** — how likely this particular item is to be wrong. This has to come from somewhere
real. Legitimate sources include agreement between the model's output and an independent verifier,
retrieval scores, whether structured output passed schema validation, a separately trained and
calibrated classifier, and plain business rules — amount, tenure, jurisdiction, novelty of the case.
The model's own statement of how sure it is does not qualify, since it is text produced by the
process being assessed.

Cross the two and you get the routing table:

| | Low consequence | High consequence |
|---|---|---|
| **High confidence** | Auto-approve, with continuous sampling | Human approves, always |
| **Low confidence** | Auto-approve or queue, by cost | Human approves, always |

The right-hand column has one entry twice on purpose. Above a consequence threshold, confidence
stops being the routing variable, because the point of the human is accountability rather than
accuracy. Someone has to own the decision.

Four design properties separate a real human-in-the-loop layer from a decorative one.

**The reviewer sees the evidence, not just the conclusion.** Show the source passage beside the
claim it supports, the retrieved record beside the extracted field, the policy clause beside the
decision. A reviewer shown only a fluent conclusion will approve it; this is automation bias, and it
is a design defect rather than a training problem.

**The reviewer's decision is captured as labelled data.** Approve, reject, and edit are three
different signals, and the edits are the most valuable dataset the system will ever produce. A
review layer that does not persist its outcomes has thrown away the only feedback loop it had.

**The auto-approved stream is continuously sampled.** A small fixed percentage of everything that
bypassed review is audited on a schedule, and the observed error rate on that sample is what tells
you whether the threshold is still correct. This is a monitoring mechanism, and it is a different
thing from routing by random sample — one measures the automated path, the other pretends to guard
it.

**Review capacity is a number in the design.** If 25% of 12,000 daily items route to review at four
minutes each, that is 200 reviewer-hours a day, roughly 25 full-time reviewers. Either the
organisation staffs it or the design changes. An architect who presents a routing policy without the
headcount it implies has presented half a design.

## Worked example

A carrier triages 12,000 claims a day. The routing policy:

*Auto-settle.* Claims under $500, with complete documentation, where an independent extraction check
agrees with the model's reading of the claim form. About 70% of volume, 8,400 items, no human.

*Threshold band.* Claims from $500 to $5,000, or any claim where the independent check disagreed.
About 25%, 3,000 items, routed to an adjuster who sees the claim form, the extracted fields, the
disagreement if there was one, and the recommendation. At four minutes each this is 200 hours a day.

*Always human.* Anything above $5,000, and every recommendation to deny, regardless of confidence.
Denial is the externally consequential act — it is what the customer experiences, what a regulator
asks about, and what a complaint is filed against.

*Sampling.* 2% of the auto-settled stream, 168 claims a day, reviewed weekly by a senior adjuster.
The error rate on that sample is the control signal. If it rises, the $500 threshold comes down.

Now the Professional-tier part. Twenty-five reviewers is the cost of this policy, and the two levers
that reduce it are raising the auto-settle threshold, which increases the error rate on the
unsupervised path, and improving the independent verifier, which is engineering work with an
uncertain payoff. Naming that trade — and the number attached to it — is what separates an
architecture from a diagram.

## How the exam probes it

A scenario states a volume, an accuracy figure, and a consequence, and asks for the review strategy.
The four options usually sample the failure space evenly: review everything, review nothing, review
a random sample, and route by confidence and consequence. The last one wins, and the wording that
identifies it usually mentions two variables rather than one.

A second shape describes a review layer that exists and is not catching errors, and asks why. The
answer is generally that the reviewer is shown the conclusion without the evidence, or that the
routing is on the model's self-reported confidence, or that the reviewer is approving at a rate that
makes genuine review impossible given the time budget.

## The wrong turns and why they tempt

**"Review 100% initially, then relax as confidence grows."** This sounds like the prudent, staged,
professional answer, and it is the classic architected distractor. It has no exit criterion, no
capacity plan, and no defined measurement that would ever justify the relaxation. If a scenario
gives you a volume figure, an option that requires reviewing all of it is almost always the wrong
answer, and the volume figure is there precisely to let you rule it out.

**Random sampling as the review strategy.** It is statistically respectable and it is the wrong
tool. A uniform sample encounters risky cases exactly in proportion to how rare they are, which is
to say it misses them. Sampling belongs on the auto-approved stream as a monitoring mechanism, not
on the whole stream as a routing mechanism.

**Routing on the model's self-reported confidence.** Right vocabulary, wrong source. This is the
purest wrong-axis distractor in the domain, because the option will use the word "confidence" and
the correct answer will too.

**Reviewing only what the model flags as uncertain.** Half-move. It routes on one variable and
ignores consequence entirely, so it sends a confident, high-value, irreversible action straight
through.

## Takeaways

- Route by confidence and consequence together. Above a consequence threshold, route to a human
  regardless of confidence.
- Confidence must come from something independent of the model: a verifier, a retrieval score, a
  schema check, a business rule.
- Show the reviewer the evidence beside the conclusion, or you have built approval theatre.
- Capture every review outcome as labelled data.
- Sample the auto-approved stream continuously; that is your threshold-calibration signal.
- State the headcount your routing policy implies.

---

# Objective 4 — Ensure compliance with regulations (GDPR, HIPAA, FedRAMP)

## The concept from first principles

A regulation is a set of obligations about data and about decisions that must hold regardless of how
the system happens to behave on a given day. "Regardless" is the operative word, and architecture is
the only place a "regardless" can be enforced.

Which turns every compliance scenario into three questions. **Where is the boundary?** — the line
between systems you control and systems you do not, which for an API-based deployment runs between
your infrastructure and the inference endpoint. **What crosses it?** — the exact payload, field by
field. **What proves it?** — the record that would satisfy an auditor a year later.

The architectural pattern that answers most compliance scenarios has five steps, in order:

1. **Classify before you move.** Know which fields are regulated before assembling a request. This
   is metadata work and it is unglamorous and everything downstream depends on it.
2. **De-identify or tokenise at the boundary.** Replace the regulated element with a surrogate
   before the call. The narrative goes out; the identifier does not.
3. **Re-associate locally.** The mapping from surrogate to real value lives inside the trust
   boundary and never leaves it. When the response returns, join it back.
4. **Log the crossing.** An immutable record of what was sent, when, under what stated purpose, to
   which model version, and what came back. This is the artefact that makes the boundary auditable
   rather than merely intended.
5. **Constrain retention.** An explicit purpose and an explicit duration for anything stored, and a
   deletion path that actually reaches every store.

Contrast this with the instruction "do not store, repeat, or reason about any patient identifiers in
this record." That instruction is evaluated by the model after the identifiers are already in the
request, which means the transmission the regulation cares about has already happened. It also
depends on the model complying. A required control cannot rest on probabilistic behaviour, because
probabilistic behaviour does not produce guarantees — and the corollaries matter as much as the rule
itself. High measured accuracy is a strong tendency. A documented residual risk is an acknowledged
tendency. A larger model is a better tendency. None of the three converts a tendency into a
guarantee, and the exam builds distractors from all three.

## What each regime forces into the design

Describe these by their architectural consequences. The exam is testing an architect, not a lawyer,
and nothing in this project's verified sources supports quoting provisions or thresholds.

**GDPR** governs personal data relating to people in the EU.

It forces a stated lawful purpose established *before* collection, with processing confined to that
purpose — which means a prompt built for support triage cannot quietly become a dataset for
marketing analytics. It forces data minimisation, so the payload carries the fields the task needs
and no more; sending a whole customer record because it was convenient is the violation, even if
nothing bad happens to it. It forces erasure on request, and this is the requirement that most often
catches architects, because erasure has to reach *every* store holding that person's data —
production database, prompt and response logs, evaluation datasets built from real traffic, cached
context, and vector indexes. An embedding derived from someone's record is still derived from their
record. It forces attention to where processing physically happens, which constrains which regional
inference endpoint you may use. And it forces the ability to account for automated decisions that
significantly affect a person, which is the bridge into Objective 5.

**HIPAA** governs protected health information in the United States.

It forces the choice between de-identifying PHI before it leaves the covered boundary and bringing
the processor inside the boundary under an appropriate agreement with the environment in scope. It
forces "minimum necessary" — the excerpt of the record you send is the excerpt the task requires. It
forces audit trails over access to PHI. And it forces a distinction architects routinely blur:
de-identified data has had the identifying elements removed; pseudonymised data has had them
replaced with a key. Both are useful and they are not the same, and the re-identification key stays
inside the boundary in either case. The practical pattern is the one above — strip direct
identifiers, send the clinical narrative, reattach the patient context locally on return, and have a
clinician sign whatever reaches a chart.

**FedRAMP** governs cloud services used by US federal agencies.

It forces the service processing the data to be an authorised environment at the appropriate impact
level. That is a procurement and boundary fact rather than a configuration setting, which has a
sharp architectural consequence: the model or deployment topology you would otherwise choose may
simply be unavailable, and no amount of configuration makes an unauthorised environment compliant.
The design response is to route through an authorised environment or to keep the regulated data out
of the unauthorised one. FedRAMP also carries continuous monitoring and documented control
implementation, which means logging, change management, and evidence collection are part of the
build rather than something added when the assessment is scheduled.

**Retention, cutting across all three.** Storing model interactions is an active decision that
creates obligations. Every retained request and response is scope for an erasure request, surface
area in a breach, and material in a legal hold. The default posture is a stated purpose and a
bounded duration — "thirty days, for incident investigation, de-identified" is a policy; "we keep
everything, it might be useful for evaluation later" is an unpriced liability wearing the costume of
diligence.

## Worked example

A hospital network wants a discharge-summary drafter.

*Boundary.* The EHR and the hospital VPC are in scope. The inference endpoint is outside it.

*Flow.* A pipeline pulls the encounter note. A de-identification stage replaces name, medical record
number, address, and provider identifiers with tokens, and shifts dates by a per-patient offset. The
token map is written to an EHR-side store that has no network path to the outside. The de-identified
clinical narrative is sent. The draft returns; tokens are re-associated locally; dates are shifted
back; a clinician reviews and signs before anything enters the chart.

*Retention.* De-identified request and response pairs are retained thirty days for incident
investigation under a stated purpose code. The token map is retained under the EHR's existing record
policy and is never part of any dataset that leaves the network.

*Audit.* Every crossing writes an immutable record: encounter ID, token-set version,
de-identification rule version, timestamp, model version, purpose code, outcome.

*What was rejected.* Appending "do not store or repeat any patient identifiers" to the system prompt,
and a plan to redact the logs nightly. The first acts after transmission. The second fixes the
record and not the transmission.

## How the exam probes it

The scenario names a sector or a regime and describes a system, then offers four ways to satisfy the
constraint. One puts a deterministic control before the boundary. The others handle it in the
prompt, in a signed agreement, in a post-hoc log redaction, or by selecting a different model. Pick
the one that acts before the data moves.

A second shape asks what an erasure or deletion request has to reach, and the answer is broader than
the production database.

A third shape presents a system with an impressive accuracy figure against a requirement stated in
absolute terms, and asks whether the requirement is met. It is not, and the reasoning is that a
percentage is not a guarantee no matter how high.

## The wrong turns and why they tempt

**The prompt-level instruction.** It is the single most attractive wrong answer in Domain 5. It is
fast, it is testable in a demo, and it is usually phrased in the same words as the regulation, which
makes it read as precisely responsive. It acts after the boundary crossing it was supposed to
prevent.

**Treating a signed agreement as the control.** A processing agreement or a business associate
agreement is genuinely necessary and it allocates liability. It does not stop data crossing a
boundary, and a question that asks how to *prevent* the crossing is not asking about paperwork.

**Post-hoc redaction of logs.** This fixes the record. The transmission already happened.

**Treating an enterprise tier or a no-training-on-your-data commitment as sufficient.** Both are
relevant and neither is the boundary control. This is the subtlest distractor in the set because
everything it says is true.

**Requesting more residual-risk documentation.** Documenting a residual risk is a governance
practice and it converts nothing. On a question where the requirement is absolute, an option that
documents the gap is an option that concedes it.

## Takeaways

- Enforce compliance boundaries architecturally, before data crosses. De-identify or tokenise ahead
  of the call, re-associate locally, audit the crossing.
- A model instruction acts after the crossing and depends on compliance; it is not a control.
- A required control cannot depend on probabilistic behaviour. High accuracy, documented residual
  risk, and a larger model all fail to convert a tendency into a guarantee.
- GDPR forces purpose limitation, minimisation, erasure reaching every derived store, and processing
  location. HIPAA forces de-identification before the boundary, minimum necessary, and audit trails.
  FedRAMP forces an authorised environment, which constrains topology and model availability.
- Retention needs a purpose and a duration. Storing by default is a liability, not caution.

---

# Objective 5 — Address ethical AI considerations (bias, fairness, transparency)

## The concept from first principles

Models are trained on data that encodes the distribution of past decisions. Where past decisions
were skewed, the skew reappears, and it reappears in fluent, confident, plausible prose — which
makes it considerably harder to notice than a skewed coefficient in a regression.

Fairness in a deployed system is a property of the whole system rather than of the model: the model,
the evaluation data, the decision threshold, and the population it is applied to all contribute. A
model can be unchanged and a system's fairness properties can shift because the applicant pool
changed.

Five mechanics carry most of the weight here.

**Measure by subgroup or you have not measured.** An aggregate accuracy figure is a weighted average
and it hides exactly the thing you are looking for. A screener at 91% overall can be 94% on the
majority group and 78% on a minority group, and the aggregate will never show it. This means the
evaluation set has to be stratified deliberately, with adequate sample size *per group* rather than
population-proportional sampling — proportional sampling gives the smallest group the least
statistical power, which is backwards relative to where the risk sits.

**Proxy variables.** Removing a protected attribute does not remove the signal. Postal code, school
name, employment gaps, name morphology, and phrasing register all carry it, and a sufficiently
capable model recovers the association without being told. Blindness is not fairness, and in a
system where you cannot measure by group you also cannot detect the disparity you were trying to
avoid.

**Fairness definitions conflict, mathematically.** Equal selection rates across groups, equal
false-negative rates across groups, and equal calibration cannot in general all hold when base rates
differ. So the design has to declare which definition it is holding itself to, and why, in terms of
which harm it is controlling. If the harm you care about is a qualified person being wrongly
rejected, you are managing false-negative parity. That declaration is a stakeholder conversation
with a written outcome, not a setting.

**Transparency means two different things, and the exam uses both.** *Disclosure* is the affected
person knowing that AI was involved and knowing how to reach a human. *Explainability* is being able
to account for a specific decision after the fact. The second is served by a reconstructable trace —
the inputs used, the evidence retrieved, the model and prompt versions, the score, the threshold,
and the rule that produced the outcome. It is not served by asking the model to explain itself,
because a generated rationale is plausible text about the decision rather than a record of what
produced it, and it can be confidently wrong about its own causes in exactly the way everything else
generated can be.

**Contestability.** A person affected by a consequential decision needs a route to challenge it and
reach a human. Designing this in at the start costs a queue and a status field. Retrofitting it
after a complaint costs considerably more.

## Worked example

A recruiting screener that ranks applications against a rubric.

*Evaluation.* A held-out set stratified by the demographic categories the organisation is
accountable for, with equal N per stratum rather than proportional, so the smallest group has enough
items to detect a five-point gap. The set includes deliberately constructed near-pairs: applications
identical in substance, differing in a proxy signal such as school name or a career gap.

*Metric.* False-negative rate parity, chosen because the harm being controlled is a qualified
candidate never reaching a human. The choice is written down with its rationale, because in twelve
months someone will ask why this metric and not another.

*Threshold.* Set against the error rate of the worst-performing group rather than the mean, which
costs throughput and is the point.

*Trace.* For every decision, persist the résumé fields used, the rubric version, the prompt version,
the model version, the score, the threshold in force, and the human decision that followed. This is
the explainability artefact.

*Disclosure and contestability.* Candidates are told AI is used in initial screening and are given a
stated route to request human review.

*Ongoing.* Subgroup metrics are recomputed monthly against live traffic, because the applicant pool
moves and a fairness result is a measurement rather than a property.

## How the exam probes it

The common shape: a system reporting strong aggregate accuracy is generating complaints from one
group, and you choose the response. The correct answer disaggregates the measurement. Distractors
remove the protected field, raise the overall accuracy target, add a fairness instruction to the
system prompt, or ask the model to self-assess for bias.

A second shape asks how to make a system "explainable" for an audit. The correct answer is a logged,
reconstructable trace. The tempting answer is a model-generated rationale attached to each decision,
which is more impressive to demo and is not evidence.

A third shape mixes fairness with human-in-the-loop: the answer routes adverse decisions to a human
and preserves the trace, rather than tuning the model.

## The wrong turns and why they tempt

**Removing the protected attribute.** It is intuitive, it feels principled, and it is often legally
encouraged as a floor. It does not remove proxy signal, and it destroys your ability to measure
disparity, which makes the system less safe rather than more.

**Model-generated explanations as the audit record.** They read beautifully and they are generated
text. An auditor asking why this applicant was rejected needs the inputs and the threshold, not a
paragraph.

**A single aggregate fairness score as a release gate.** Better than nothing, and it obscures which
definition is being enforced and which group is bearing the error.

**Adding a fairness statement to the system prompt.** Same category as every other prompt-level
control in this domain: a tendency, in a place where the requirement was a measurement.

## Takeaways

- Aggregate accuracy hides subgroup failure. Stratify the evaluation set, with adequate N per group.
- Removing the protected attribute does not remove proxy signal and removes your ability to measure.
- Fairness definitions conflict when base rates differ. Declare which harm you are controlling.
- Transparency is disclosure plus explainability. Explainability is a logged trace, not a generated
  rationale.
- Build a contestation route for consequential decisions before you need one.

---

# Synthesis — the five objectives in one regulated design

Take a single system and run all five through it: a European bank deploys an assistant that drafts
hardship-plan offers to customers in arrears. It reads the account history and the customer's
correspondence, proposes a payment-restructuring offer, and drafts the letter.

Every objective has a claim on this system. Personal data of EU customers is in scope. The offers
are consequential decisions communicated to individuals. The assistant touches a system that can
amend an account. Volume is high enough that reviewing everything is not available. And the
correspondence it reads is text written by third parties, which makes it untrusted input.

**Data boundary and minimisation.** The payload is the arrears history, the account terms, and the
customer's stated circumstances — not the full customer record. Name, account number, and national
ID are tokenised before the call and re-associated locally. Processing runs against an EU-region
endpoint. Purpose is declared as hardship assessment, and the resulting logs are not available to
the marketing analytics pipeline, which is a per-purpose access control rather than a policy
statement.

**Guardrails.** The assistant has no tool that can amend an account. It emits a structured offer
object. A separate service validates the offer against the bank's hardship policy — term limits,
rate floors, eligibility — and only that service holds the credential. Customer correspondence is
wrapped as untrusted data, and the eligibility decision never depends on instructions found inside
it. Output is schema-validated, and any offer outside policy bounds is rejected before a human ever
sees it, so the reviewer's queue contains only well-formed candidates.

**Failure modes addressed explicitly.** Confabulated policy terms are caught by validating every
cited term against the policy database. Injection via correspondence is neutralised by the absence
of privilege. Version drift is handled by pinning the model version and running a regression set of
200 historical cases before any version change. Compounding error across the four model-touching
steps is interrupted by the deterministic policy validation in the middle.

**Human-in-the-loop.** Every offer that would be *declined*, and every offer above a defined
concession value, goes to a case handler regardless of confidence, because those are the outcomes
the customer experiences and a regulator asks about. Offers inside standard bands, where the policy
validator and the model agree, are auto-issued. Two percent of auto-issued offers are audited
weekly. The reviewer's screen shows the arrears history, the specific policy clause, and the
proposed terms side by side. Every reviewer edit is stored.

**Fairness and transparency.** Offer generosity and decline rates are measured monthly by the
subgroups the bank is accountable for, on a stratified set with equal N. The declared metric is
parity of decline rate among customers with comparable arrears profiles, chosen because wrongful
decline is the harm. Each decision carries a trace: fields used, policy version, prompt and model
version, validator result, human decision. Customers are told an automated system assists in
preparing offers and are given a route to human review.

**Now the trades, which is where the Professional tier actually lives.** Tightening the human-review
band improves accountability and costs case-handler headcount, and that number belongs in the
business case. Aggressive minimisation improves the compliance posture and can reduce offer quality,
because context that was stripped was sometimes context that mattered. A longer log retention window
helps fairness auditing and enlarges the erasure surface. Pinning the model version protects against
drift and defers capability improvements. None of these has a correct answer independent of the
organisation's risk appetite, and the architect's job is to surface the trade with a number attached
rather than to resolve it silently.

**The stakeholder answer.** A sponsor who is not an engineer needs each control in one sentence. The
assistant cannot change an account; it proposes, and the bank's existing rules engine decides.
Customer identifiers never leave the bank's systems. Every decline is seen by a person. We measure
whether outcomes differ across customer groups every month and we can show the reasoning behind any
individual offer. Those five sentences are the governance design, and being able to say them without
jargon is a tested competence in this exam's neighbouring domain.

---

# Misconceptions

| Misconception | Correction |
|---|---|
| "Telling the model not to store or repeat sensitive data satisfies the compliance requirement." | The instruction is evaluated after the data is already in the request; the boundary crossing has happened. Control it before the call. |
| "We're at 99.2% accuracy, so we meet the requirement." | A percentage is a tendency. A required control needs a mechanism that cannot fail probabilistically. |
| "Documenting the residual risk closes the gap." | Documentation records a gap; it does not convert one. |
| "A more capable model will satisfy the guarantee." | A better model is a better tendency. The class of failure is unchanged. |
| "Least privilege means logging or confirming when a risky tool is used." | It means removing the capability the system does not need. |
| "We have logging and alerting, so the risk is controlled." | Detection is not prevention. A log tells you the boundary was crossed. |
| "One strong safety layer is cleaner than four modest ones." | Layers fail independently; a single layer is a single point of failure. |
| "Ask the model to double-check its own output." | The check is not independent of the process that produced the error. Verification must sit outside the model. |
| "Two models agreeing means the answer is right." | Correlated training and correlated failure modes mean two models can agree and both be wrong. |
| "The model said it was highly confident, so route on that." | Stated confidence is generated text. Route on an independent signal — a verifier, a retrieval score, a schema check, a business rule. |
| "Review everything at launch, then relax it." | Without an exit criterion, a measurement, and a capacity plan, this is a policy that never relaxes and never staffs. |
| "A random sample of outputs is a sound review strategy." | Uniform sampling encounters risky cases in proportion to their rarity, which is to say it misses them. Sample the auto-approved stream to calibrate; route by confidence and consequence. |
| "Retaining all model interactions is the cautious choice." | Retention creates obligations. Purpose and duration have to justify storage. |
| "An erasure request means deleting the person's row." | It has to reach every derived store: prompt and response logs, evaluation datasets, caches, and vector indexes. |
| "A signed processing agreement means the data can go." | An agreement allocates liability. It does not stop the transmission. |
| "Remove the protected attribute and the system is fair." | Proxy variables carry the signal, and removing the attribute destroys your ability to measure the disparity. |
| "91% accuracy overall means it works for everyone." | An aggregate is a weighted average that hides subgroup failure. Measure by subgroup. |
| "Attach a model-generated rationale to each decision for the audit." | A generated rationale is plausible text about the decision. Explainability is a logged, reconstructable trace. |
| "Each pipeline step passes its tests, so the pipeline is fine." | Per-step accuracy compounds. Ten steps at 96% is roughly 66% end to end. |
| "Prompt injection is solved by filtering hostile phrasings." | It is architectural. The fix is that the model holds no privilege worth hijacking. |

---

# Quick reference

**The governing distinction.** Prompt text produces a tendency. Code, permissions, and people
produce guarantees. Match the mechanism to whether the requirement is "usually" or "always".

**Guardrails — four layers.** Input validation · output filtering · scoped permissions · human
approval on consequential actions. Least privilege removes the capability. Detection is not
prevention.

**Failure modes, by diagnostic signature.**
- Confidently wrong right after a content refresh → retrieval and indexing.
- No memory of two turns ago in a short conversation → history not resent by the application.
- Degrades only mid-document → positional attention; fix structurally, not by shortening.
- Behaviour changed with no deployment → model version drift.
- Every step passes, product fails → compounding; add deterministic checkpoints.
- Unrequested action after reading external content → indirect prompt injection.

**Human-in-the-loop.** Route by confidence × consequence. Above a consequence threshold, always
human. Confidence from an independent signal. Show evidence beside conclusion. Capture every review
outcome. Sample the auto-approved stream continuously. State the headcount.

**Compliance pattern.** Classify → de-identify or tokenise at the boundary → re-associate locally →
log the crossing immutably → bound retention by purpose and duration.

**Regime consequences.** GDPR: purpose limitation, minimisation, erasure reaching derived stores,
processing location. HIPAA: de-identify before the boundary, minimum necessary, audit trails,
re-identification key stays inside. FedRAMP: authorised environment at the right impact level,
which constrains topology and model availability, plus continuous monitoring.

**Verification.** Independent of the model. A self-check is not independent, and two models can
agree and both be wrong.

**Fairness and transparency.** Stratified subgroup measurement with adequate N per group. Proxies
survive attribute removal. Declare which fairness definition and which harm. Disclosure plus a
logged trace. A contestation route before it is needed.

**Professional-tier reflex.** For any control you propose, be ready with four things: what it costs
at volume, what breaks first under real traffic, what a regulated sector adds to the decision, and
the one sentence that explains it to someone who is not an engineer.
