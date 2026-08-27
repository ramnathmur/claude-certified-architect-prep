# Lesson — Domain 4: Evaluation, Testing & Optimization

**Exam:** Claude Certified Architect – Professional (CCAR-P)
**Domain weight:** 16% (official exam guide v1.0, effective July 2026)
**Paper size:** 63 items, 120 minutes, closed book. At 16% of the blueprint, this domain is worth
roughly ten items — arithmetic on the published weight, not a published item count.
**Scoring:** scaled 100–1000, pass at 720, decided on total score. There is no per-domain floor.
**Objectives covered (verbatim from the guide, §6):**
1. Define evaluation metrics (accuracy, latency, cost, safety, security)
2. Design evaluation datasets and test frameworks using mixed methodologies
3. Conduct A/B testing and iterative improvements
4. Diagnose system issues (prompt failure, hallucinations, model mismatch)
5. Optimize token usage, latency, and cost-performance trade-offs
6. Monitor system performance using logging and observability tools

**Two things this lesson will not tell you**, because the official guide does not say and nobody
should invent them: whether the 63 items are standalone or grouped into shared-scenario blocks, and
whether multiple-response items are scored all-or-nothing or with partial credit. Prepare as though
multiple-response items are all-or-nothing — that was the Foundations reality and it cost eight
marks — but do not treat that as a stated rule.

---

## 0. What this domain is actually about

Every other domain on this exam asks whether you can build the thing. This one asks whether you can
tell, afterwards, that the thing is working — and prove it to someone who will not take your word.

The six objectives look like six separate skills. They are one loop, and the loop has a direction.
You define what "working" means as a number with a threshold. You build a fixed set of cases that
number is measured on. You use that set to gate every change before it touches traffic. When
production tells you something has broken, you diagnose in a fixed order rather than by hunch. You
make the system cheaper and faster only inside the quality bar you already declared. And you
instrument production so it reports back — both to catch the next break and to restock the eval set
with failures you never imagined.

The loop closes at that last step, and the closure is the whole point. An evaluation set built at
design time contains the failures its authors could think of. Production contains the ones they
could not. A programme that never feeds production failures back into the set is measuring its own
imagination, at increasing precision, indefinitely.

The Professional tier adds a fifth question to every one of these: *can you defend the decision?* Not
just which eval design is correct, but which one is affordable at 200,000 requests a month, which one
survives a regulator asking how you know, and how you explain the trade-off to a stakeholder who
thinks "97% accurate" is a finished sentence.

A structural note before we start. Because pass/fail runs on the total scaled score with no domain
floor, a weak Domain 4 is survivable in arithmetic. It is not survivable in practice, because this
domain's reflexes leak into the others: Domain 3's observability-at-scale objective, Domain 5's
human-in-the-loop validation, Domain 6's SLA conversations. The habits below get tested more than ten
times.

---

## 1. Defining evaluation metrics

### The concept

A metric is a commitment to a decision. If a number crossing its threshold would change nothing you
do, the number is decoration. That single test — *what decision does this number gate?* — eliminates
most of the metrics teams actually collect.

Which means a metric is only finished when it has four parts:

- **A specific failure being counted.** "Quality" is not countable. "Answers the gold label marks
  incorrect" is.
- **A denominator.** A count without a base rate cannot be compared to anything, including itself
  last month.
- **A segment.** The population the number describes. Omit this and you get the masking trap in §2.
- **A threshold, declared before you see any results.** A bar set after the scores arrive is not a
  bar; it is a description of what you got.

The exam guide names five metric families, and they are named separately because they fail
separately and are owned by different people.

**Accuracy** is task fidelity against a ground truth. It needs a labeled set and a defined notion of
correct. It is the only one of the five that requires you to have already decided what the right
answer is.

**Latency** is a distribution, not a number. The mean is close to useless for an SLA, because the
users who churn are in the tail. Report p50 and p95 or p99. Distinguish time-to-first-token from
total completion time: for a streaming chat interface, TTFT is what the user experiences as
responsiveness; for a batch pipeline where nobody is watching a cursor blink, only total time
matters. Getting this backwards is a favourite distractor.

**Cost** is per unit of business work, not per token. Tokens are the unit you are billed in, and the
unit nobody outside the engineering team can reason about. "Mean cost per resolved ticket ≤ $0.08" is
a metric a finance stakeholder can hold you to. "1.4M tokens per day" is telemetry.

**Safety** is a rate of policy-violating output over a stated denominator. The critical property is
achievability. On an open-ended generative task, a bar of 0% is not a stretch goal, it is an
unachievable number that guarantees the metric gets quietly ignored the first time it is missed. Set
a small non-zero rate — "< 0.1% of 10,000 outputs flagged for toxicity" — and reserve the hard zero
for properties a deterministic check can actually guarantee, like "0 outputs containing a field
marked PII."

**Security** is a different axis from safety, and the exam will test whether you know that. Safety is
about what the model says. Security is about what the system permits: whether an injected
instruction in a retrieved document can reach a tool, whether the agent's credentials are scoped to
what it needs, whether data can leave through a tool result. Security is measured against an
adversarial suite — attempted-injection block rate, unauthorized-tool-invocation count, least-
privilege audit findings — not against a quality rubric. A system can be perfectly safe and
completely insecure.

### Forcing a fuzzy goal into a metric

Requirements arrive as adjectives. The conversion is mechanical:

| Lever | The question it forces | Applied to "safe outputs" |
|---|---|---|
| Specific | What exact failure are we counting? | outputs flagged for toxicity |
| Measurable | Over what denominator? | out of 10,000 outputs |
| Achievable | Is the bar reachable in reality, not in principle? | a small non-zero rate, not 0% |
| Relevant | Does crossing it change a real decision? | it gates ship / block on this capability |
| Threshold | What number separates pass from fail? | < 0.1% |

"Safe outputs" becomes "< 0.1% of 10,000 outputs flagged for toxicity." One is a hope; the other is a
release gate.

### Worked example

An insurance claims assistant. Reads a submitted claim plus retrieved policy documents, drafts a
coverage determination, escalates when the policy is ambiguous. Production volume: 12,000 claims per
month. Here is the finished metric set.

| # | Metric | Definition | Threshold | Gate it controls |
|---|---|---|---|---|
| 1 | Determination accuracy | Fraction of claims where the drafted determination matches the adjuster's gold label, reported **per claim type** | ≥ 0.95 on every claim type independently | Auto-draft vs mandatory review |
| 2 | Grounding | Fraction of policy citations whose quoted span exists verbatim in the cited document | 1.00 — any fabricated citation is a hard fail | Release block |
| 3 | Escalation recall | Fraction of genuinely ambiguous claims that were escalated | ≥ 0.98 | Release block |
| 4 | Latency (p95) | End-to-end, submission to drafted determination | ≤ 6.0 s | SLA commitment |
| 5 | Cost | Mean cost per claim processed | ≤ $0.19 | Budget review |
| 6 | PII containment | Outputs containing a policyholder identifier not belonging to this claim | 0 per 12,000 | Regulatory control |

Note what happened. Metric 1 carries a segment clause; without it, a claim type that is 3% of volume
could fail 40% of the time and never appear. Metrics 2 and 6 are hard zeros because a deterministic
check can enforce them. Metric 3 is expressed as recall rather than accuracy, because the expensive
error here is failing to escalate, and a plain accuracy number would let a high true-negative rate
paper over it. Metric 5 is stated in dollars per claim, because that is the sentence the business
sponsor will repeat.

### How the exam probes this

The scenario hands you a requirement in adjectives — "the system must be fast, accurate, and safe" —
plus a business context, and asks which measurement plan to adopt. The correct option names a
denominator, a segment, and a threshold set in advance. The distractors are usually:

- Metrics that are easy to collect rather than decision-relevant (average response length, tokens per
  day, number of requests served).
- A single composite quality score, which sounds tidy and cannot be acted on, because nothing tells
  you which component moved.
- A threshold to be "calibrated once we see baseline performance" — which is the after-the-fact bar,
  dressed as prudence.
- A safety metric applied to a security requirement, or vice versa.

Another common shape gives you a stated business constraint and four metrics, and asks which one the
constraint actually implies. A per-request SLA implies p95 or p99, not the mean. A budget stated in
dollars per resolved case implies cost per unit of work, not cost per token.

### Wrong turns and why they are tempting

**Measuring what is easy.** Token counts and response lengths are free to collect and require no
labeling. They are tempting because they produce a chart immediately. They correlate with nothing you
care about on an open-ended task.

**The composite score.** One number for "quality" is attractive to a dashboard and useless to a
diagnosis. When it drops three points you cannot tell whether tone regressed, grounding broke, or one
segment collapsed.

**Setting the bar after the run.** This never feels like cheating in the moment; it feels like
calibration. The tell is that nobody ever calibrates the bar upward.

**Demanding perfection on open-ended properties.** A 100% safety bar reads as rigour in a design
review and functions as an off switch in production, because the first miss makes the metric
non-binding and everyone quietly stops reporting it.

### Takeaways

- A metric that gates no decision is decoration. Name the decision first.
- Every metric needs a failure definition, a denominator, a segment, and a threshold declared in
  advance.
- Latency is a distribution: p95/p99, and TTFT versus total, chosen by what the user experiences.
- Cost is per unit of business work. Tokens are the billing unit, not the metric.
- Safety is what the model says. Security is what the system permits. Different suites, different
  owners, different failure signatures.
- Hard zeros belong only to properties a deterministic check can enforce.

---

## 2. Designing evaluation datasets and test frameworks

This is the longest section, because it is where the domain's real difficulty lives and where the
exam's most instructive traps are set.

### Why a fixed dataset exists at all

An evaluation set is a measuring stick. Its value comes entirely from being held constant: if the
cases change between runs, a score change tells you nothing about the system. That is the first
principle, and it has an uncomfortable corollary — the set will go stale, and refreshing it destroys
comparability with everything measured before. You manage this by versioning the set and re-baselining
deliberately, not by editing cases in place because one looked wrong.

### Composition: where cases come from

Real production traces first, synthetic cases second, and hand-written cases only for failure shapes
you have reason to expect but have not yet observed.

The reason is blunt: the failures you imagine from a specification are not the failures that occur. A
set derived entirely from a design document encodes the authors' model of the system, and the whole
purpose of an evaluation is to test that model. Treat every spec-derived case as a hypothesis until a
real trace confirms the failure exists.

Twenty to fifty hand-verified cases beat several hundred unverified synthetic ones. This is
counterintuitive until you consider what an unverified case does: it contributes a score without
contributing information, because you do not know whether its label is right. A set of 500 cases with
a 6% label error rate has a hard floor on measurable accuracy at 94%, and you will spend weeks
chasing the last six points of a ghost.

### The bias that makes an eval set lie

An evaluation set assembled from cases the system already handles will report excellent performance
and conceal every failure that matters. It happens naturally: the team collects examples while
building, keeps the ones where behaviour was interesting, and quietly drops the ones that were too
messy to label.

Enlarging that set does not correct it. Adding 500 more cases drawn the same way multiplies the same
bias by ten and produces a tighter confidence interval around a wrong number. The fix is
compositional, not volumetric — the set must be rebuilt around the segments and failure modes you
need to report on.

### Stratification, and why natural frequency is the wrong sampling rule

The instinct is to sample the eval set to match production frequency, so the number "represents
reality." It defeats the purpose.

Consider a document extraction system: 78% invoices, 15% purchase orders, 5% credit notes, 2%
handwritten remittance advices. Sample 50 cases at natural frequency and the handwritten segment gets
one case. You cannot measure a failure rate on one case. You cannot even detect a 40% failure rate on
one case — you will see one pass or one fail, and both are noise.

So build the set to answer the questions you must answer. If you have to report accuracy by document
type, every document type needs enough cases to support a rate — thirty or so as a working floor —
and rare high-cost segments get *over*-sampled relative to their traffic share, not under-sampled.
The aggregate number is then reconstructed by weighting, if you need it at all.

**The masking trap, stated plainly:** an aggregate 97% accuracy can conceal a 40% failure rate on a
rare document type. Overall metrics average away segment failures, and the segments they hide are
disproportionately the rare, weird, expensive ones. Before anyone reduces human review, accuracy must
be validated per segment, and every segment must clear the bar independently.

### Balance: should-fire and shouldn't-fire

For every failure the eval is meant to catch, include a near-miss case where the system behaves
correctly and a brittle grader would wrongly flag it. A set of only failure cases hides false alarms;
a set of only clean cases hides misses. Roughly equal counts is the working rule, and it hardens from
preference to requirement as stakes rise.

### The three instruments

This is the "mixed methodologies" phrase in the objective, and it is asking whether you know that
these are three different tools with three different jobs.

**Instrument 1 — deterministic checks.** Exact match, regex, schema validation, numeric comparison,
field-by-field match against gold, execution against unit tests, PII pattern scan, and
verbatim-source grounding checks.

Properties: exact, reproducible, effectively free at any volume, and immune to grader error. They
reach only surface-checkable properties. That limitation is narrower than people assume — schema
validity, citation-span existence, forbidden-field presence, numeric tolerance, tool-call ordering,
and refusal-when-required are all deterministic.

Use them first, always, and never route a code-checkable property to a model grader. Citation
validation deserves its own sentence: asking a model "is this citation accurate?" is a judgement call
it can get wrong in both directions, and you would then need a second measurement to know how often,
while checking whether the quoted string appears in the cited document is exact and costs nothing. When a property is checkable in code, a
model grader is a strictly worse instrument.

**Instrument 2 — rubric-driven, model-graded evaluation.** For subjective quality that no code check
can reach: tone, coherence, helpfulness, faithfulness of a summary, whether an answer actually
resolves the question asked.

Four rules govern it.

*Decompose into binary sub-criteria.* A 1–5 scalar hides its own uncertainty — nobody can say what
separates a 3 from a 4, the boundary drifts between runs, and you need far more samples to move the
number reliably. Replace "rate the answer 1–5 for relevance" with three binary questions: on-topic?
answers the specific question asked? free of filler? Whole-output pass means every hard criterion
passes. Binary verdicts also aggregate cleanly and make grader-versus-human agreement trivial to
compute.

*Use a different model family than the one being graded.* A grader from the same family as the
generator exhibits self-preference bias — it rewards its own family's style — and worse, it shares
the generator's blind spots, so the failures it cannot see are exactly the failures the system
produces. If only a same-family grader is available, the result may be reported as degraded but never
as ground truth.

*Validate the grader against human labels before believing it.* Hand-label a sample, run the grader
on the same sample, and measure agreement. A commonly cited starting bar is around 75% agreement;
treat it as a starting recommendation to be set on first real use, not a settled constant. Below the
bar, the grader is the thing that is broken, and its scores describe the grader rather than the
system.

*Know its biases.* Position bias (favouring whichever option was shown first), verbosity bias
(rewarding length regardless of correctness), and self-preference. Direction is reliable, magnitude
is corpus-specific. Guards: randomize and swap option order and aggregate across both, use binary
sub-criteria and length-controlled rubrics, and enforce the out-of-family rule.

**Instrument 3 — human review.** Its job is calibration and ground-truth labeling, not grading at
scale. Humans establish the labels the deterministic checks compare against, they produce the labeled
sample the model grader is validated against, and they periodically re-audit the grader to catch
drift. Humans also adjudicate the genuinely ambiguous cases, and there is a bar worth remembering: if
two domain experts would not independently reach the same verdict on a case, no automated grader can
be trusted on it at any threshold, and the case needs re-scoping rather than a better grader.

### How they combine — the layering order

Deterministic checks filter, the model grader scales, humans calibrate periodically. In that order,
every time.

Worked example, a support assistant producing 2,000 answers per day:

1. **Deterministic layer, all 2,000, zero marginal cost.** Schema validity. Verbatim-existence of
   every cited span in the cited document. PII scan against the account fields of other customers.
   Refusal present when retrieval returned nothing above the relevance floor. Say 110 answers fail
   here; they are logged with a failure code and never reach the next layer.
2. **Model-graded layer, the surviving 1,890.** An out-of-family grader scores four binary rubric
   criteria: grounded in the retrieved passages, resolves the specific question asked, correct
   register, no unsupported policy claim. Costs a fraction of a cent each.
3. **Human layer, 50 per week, stratified.** Not the 50 worst, and not 50 at random from the whole
   stream — stratified across segments and across grader verdicts, so both the pass and fail
   populations are audited. Agreement between the human labels and the grader's verdicts is computed
   and tracked over time. When it slides below the bar, the grader is repaired before its output is
   believed again.

The economics are the argument. Layer 1 costs nothing and settles the properties that carry the
hardest guarantees. Layer 2 costs about a dollar a day and covers everything code cannot see. Layer 3
costs a few hours a week and is the only thing that can tell you layer 2 has stopped working.

### Two-layer structures

Some system shapes cannot be graded with a single verdict, and the exam knows it.

**RAG needs two rows.** One grades retrieval — Recall@k against gold passage IDs, or context
precision. One grades generation — faithfulness of the answer to the retrieved passages. Both must
pass independently. A faithfulness score computed over the wrong passages is a meaningless number: the
answer is perfectly faithful to material that does not answer the question. And when a RAG system
degrades, retrieval is the more common culprit, so a single blended score obscures exactly the layer
you need to see.

**Agentic systems need two rows.** One grades the trajectory — was the right tool selected, in a
valid order. One grades the outcome — did the final state satisfy the goal. Both matter, because a
correct answer reached through a wrong or irreversible path is still a failure. If the agent deleted
the record and then reported the correct value, outcome grading alone calls that a pass.

**Multi-turn systems need first-failure attribution.** Score the earliest breaking turn, not just the
final state, or a late self-correction masks an early defect that will not always self-correct.

### Reliability aggregation: pass@k versus pass^k

The same k attempts read as two entirely different claims depending on how you aggregate.

`pass@k` passes when *at least one* of k attempts succeeds. It measures reachable success, and it is
the right aggregation when a downstream check catches failures and triggers a retry — code with a
test harness, a tool call behind a validator.

`pass^k` passes when *all* k attempts succeed. It measures reliability, and it is the right
aggregation when every attempt is user-visible or acts in the world.

Worked instance: an agent that books changes to a customer's account. The task-completion row uses
`pass@3 ≥ 0.90`, because a validator catches a bad plan and the agent retries. The
confirm-before-any-irreversible-action row uses `pass^5 = 1.0`, because one silent irreversible action
out of five attempts is one too many. Reporting the second as `pass@5` would let a gate that fires
once in five attempts look like a passing control.

### How the exam probes dataset design

The characteristic scenario gives you a healthy-looking number and an unhappy reality: accuracy is
96% on a 500-case set, and customers keep complaining. The correct answer rebuilds the set from real
production failures and reports by segment. The seductive answer expands the set, because "more data"
is a reflex that is right in most of engineering and wrong here.

A second shape gives you a specific property to grade and four grading instruments, testing the
deterministic-first rule. If the property is checkable in code — schema, citation existence, forbidden
field, exact numeric — the model-graded option is wrong however elaborate its rubric.

A third shape describes a RAG or agentic system with one blended quality score and asks why the team
cannot locate the regression. The answer is the missing layer.

A fourth shape is the reduce-human-review proposal on the back of an aggregate accuracy figure. The
answer analyses by segment first and adds stratified sampling of the automated stream.

### Wrong turns and why they are tempting

**Enlarging a biased set.** More data is the correct instinct almost everywhere else in engineering.
Here it multiplies the bias and tightens the confidence interval around a number that was already
wrong.

**Exact match on open-ended generation.** It is deterministic, cheap, and reproducible — all the
properties you were told to prefer. It measures string identity with one reference phrasing, which
for open-ended text is close to a random variable.

**Response length as a quality proxy.** Free, and it correlates with nothing.

**A same-family grader trusted as truth.** It is the most convenient grader available and produces
plausible scores immediately. It also inflates them and cannot see what the generator cannot see.

**Generating the eval set with the same model that serves production.** Efficient, and it guarantees
the set contains only cases inside that model's own competence and phrasing distribution.

**Sampling only the complaints.** Reviewing exclusively the flagged or low-confidence stream is
efficient use of reviewer time and blind by construction: novel error patterns first appear in the
high-confidence stream, which is precisely where nobody is looking.

### Takeaways

- The set's value comes from being held constant. Version it; re-baseline deliberately.
- Real traces first. Spec-derived cases are hypotheses until a real failure confirms them.
- 20–50 hand-verified cases beat hundreds of unverified ones.
- A set of already-handled cases overstates performance; enlarging it does not fix it.
- Stratify by the segments you must report on, and over-sample rare high-cost segments.
- An aggregate figure can hide a catastrophic segment. Validate per segment before reducing oversight.
- Balance should-fire against shouldn't-fire cases.
- Deterministic checks filter, model graders scale, humans calibrate — in that order.
- Model graders: binary sub-criteria, out-of-family, validated against human labels, biases guarded.
- RAG and agentic systems grade in two layers. Multi-turn attributes the first failing turn.
- `pass@k` for reachable success behind a retry; `pass^k` for reliability of a user-visible or
  world-acting step.

---

## 3. A/B testing and iterative improvement

### The concept

A prompt is production code with no type system, no compiler, and no unit of change smaller than
"the whole behaviour." Editing one sentence can move accuracy on a segment you were not thinking
about. The only safety net is measurement, and the measurement has to happen in a fixed order.

**The order: regression evaluation, then a controlled A/B against the current prompt on metrics
defined in advance, then staged rollout.**

Each step exists because the next one cannot do its job.

*Regression first*, because the A/B costs real user traffic. A change that regresses on the held set
has already disqualified itself and should never reach a live cohort. The regression run is also the
only step that covers rare segments, because you built the set to over-sample them; live traffic
delivers those segments at natural frequency, which is to say barely.

*Then the A/B*, because the regression set cannot tell you how the change performs on the live
distribution, on inputs nobody thought to include, at production latency, under production load.

*Then staged rollout*, because a two-week A/B on a 50/50 split still has not exposed the change to
every seasonal pattern, every enterprise customer's peculiar phrasing, or the Monday-morning volume
spike.

### Designing the A/B so the result means something

**One variable.** If the variant changes the prompt, swaps the model, and adjusts retrieval depth,
a win tells you the bundle is better and nothing about which part earned it — and when a later change
regresses, you have three suspects and no way to isolate them.

**Randomize at a stable unit.** User or session, not request. Randomizing per request means a single
conversation flips between prompts mid-thread, which corrupts multi-turn behaviour and the metric
simultaneously.

**Declare the primary metric and the guardrails before the test starts.** One primary metric decides
ship or no-ship. Guardrail metrics can only block: latency p95, cost per unit, safety rate, escalation
rate. A variant that improves the primary metric while blowing a guardrail does not ship.

**Fix the duration and sample size in advance, and do not stop early on good news.** Watching a
running test and stopping the moment it looks favourable inflates the false-positive rate. If you are
going to peek, decide the peeking schedule up front.

**Report by segment, not only in aggregate.** The same masking that ruins an accuracy report ruins an
A/B result: an aggregate win of 1.5 points can contain a 12-point regression on a small segment.

### Worked example

A support assistant handling 40,000 requests a week. The proposed change adds three targeted few-shot
examples to disambiguate two tools the agent has been confusing.

*Step 1 — regression.* Run the 400-case eval set. Tool-selection accuracy on the ambiguous subset
rises from 0.71 to 0.93. Overall accuracy holds at 0.94. Grounding, refusal recall, and PII checks
unchanged. Token count per request rises 340 tokens; p95 latency in the harness rises 0.2 s. Nothing
regressed, so it earns a live test.

*Step 2 — A/B.* Declared before launch: primary metric is first-contact resolution rate. Guardrails
are p95 latency ≤ 4.0 s and cost per resolved ticket ≤ $0.11. Split 50/50 by user id. Duration two
weeks, roughly 40,000 requests per arm. Ship rule: resolution rate improves and neither guardrail is
breached.

*Step 3 — result.* Resolution rate 0.82 → 0.86. p95 latency 3.4 s → 3.6 s, inside the guardrail. Cost
per resolved ticket $0.094 → $0.099, inside the guardrail. Segment view: the gain is concentrated in
the ambiguous-intent segment, as predicted, with no segment regressing more than half a point. Ship.

*Step 4 — rollout.* 10%, then 50%, then 100%, with the same guardrails alerting at each stage.

Note that the extra 340 tokens were not free — they cost half a cent per resolved ticket and 0.2
seconds at p95. The change shipped because those costs were declared as guardrails and cleared, not
because they were invisible.

### How the exam probes it

The most common shape presents a prompt change that looked better on a handful of hand-picked
examples and asks what to do before shipping. The correct answer runs the regression set first, then
a controlled comparison on pre-declared metrics.

A second shape hands you an A/B result with a mixed outcome — quality up, latency or cost
significantly up — and asks for the call. The answer is governed by whether a guardrail was declared
and breached, not by whether the quality gain feels worth it.

A third shape describes a variant that changed several things at once and asks why the team cannot
explain the result.

A fourth shape offers a change already live in production and asks how to evaluate it. The
uncomfortable answer is that you cannot cleanly, because there is no concurrent control — you have a
before-and-after comparison confounded by everything else that changed in the same window.

### Wrong turns and why they are tempting

**Shipping on spot-checks.** Ten examples that look better is genuinely persuasive evidence to a
human reader, and it is a sample of ten drawn non-randomly by someone who wants the change to work.

**Bundling changes.** It is faster, and it is how most teams actually work. It makes attribution
impossible and turns the next regression into an archaeology project.

**Stopping when the numbers look good.** It feels like being responsive to data.

**Replacing the regression set with the A/B.** Live traffic feels more real than a fixed set. It also
delivers rare segments at natural frequency and cannot detect a regression confined to one of them.

**Treating a flat result as a win.** A variant that performed identically is a variant with no
demonstrated benefit and a real switching cost.

### Takeaways

- Regression evaluation, then controlled A/B, then staged rollout. The order is not negotiable.
- One variable per variant, or the result is unattributable.
- Randomize at user or session level, never per request.
- Primary metric and guardrails declared before launch; guardrails can only block.
- Fixed duration and sample size; no stopping early on good news.
- Report the A/B by segment as well as in aggregate.
- A prompt change is a production change and gets a production change's process.

---

## 4. Diagnosing system issues

### The concept

When an LLM system degrades, the fault is far more often in what feeds the model than in the model.
That is the empirical fact behind the diagnosis order, and the order matters because each earlier
layer poisons everything downstream — swapping the model while retrieval is broken changes the
phrasing of a wrong answer.

**The order: data and retrieval, then prompt and context, then model mismatch.**

The order is also economically correct. Checking retrieval is a query against gold passage IDs and
takes an afternoon. Swapping the model is a re-benchmark, a re-tune, a cost renegotiation, and a
re-run of every eval. Testing the cheap hypothesis first is not timidity, it is sequencing.

### Failure signatures

| Symptom | Layer | The tell |
|---|---|---|
| Confidently wrong immediately after a corpus refresh or re-index | Retrieval / indexing | The timing. Nothing about the model changed |
| Wrong on one document or query type, correct elsewhere | Data coverage / chunking | The failure is segment-shaped, not general |
| Facts correct, format or required steps missing | Prompt / instructions | The knowledge arrived; the instruction did not |
| Format inconsistent across runs despite explicit instructions | Few-shot examples needed | Prose instruction has already failed; more prose will fail again |
| Fails only on long inputs; misses facts from the middle | Context structure / position | Length-correlated, position-correlated |
| Forgets a fact from two turns ago in a short conversation | Application layer | The API is stateless; history was not resent. Not a context limit |
| Fails broadly on genuinely multi-step reasoning, with retrieval verified and prompt clean | Model mismatch | Everything upstream has been cleared |

That last row is the point of the table. Model mismatch is a real diagnosis, and it is the one you
reach after eliminating the others, not the one you reach because it is the easiest thing to change.

### Hallucination is three different failures

Treating "hallucination" as one phenomenon produces one reflexive fix — usually an instruction not to
make things up — which addresses none of them.

**Type A: unsupported claim when the context did contain the answer.** The material was retrieved and
the model departed from it. This is a grounding and prompt problem. Fix by requiring citation of a
source span for every claim and adding a deterministic verbatim check that fails the output when the
span does not exist.

**Type B: unsupported claim when retrieval returned nothing relevant.** The model filled a vacuum.
This is a retrieval problem plus a missing refusal path. Fix the retrieval, and add an explicit
"insufficient context, escalate" branch with its own eval row measuring escalation recall.

**Type C: fabrication under context pressure or truncation.** Content was dropped by compaction or
truncation and the model reconstructed it. This is a context-management problem. Fix by extracting
precision-critical facts verbatim into a structured block instead of summarizing uniformly.

Three causes, three fixes, one symptom. Diagnosis means finding out which one you have, and the
evidence is in the logs: what was retrieved, what was in the context window, and whether the claim
had a resolvable source.

### Worked example

A policy assistant's grounded-answer rate falls from 0.94 to 0.71 over one week. The team's first
proposal is a larger model.

Walking the order:

*Data and retrieval.* Recall@5 against gold passage IDs has fallen from 0.92 to 0.55. Root cause: the
documentation team restructured headings in the refreshed corpus, the chunker now splits mid-table,
and the entitlement tables that answer the most common question class are split across two chunks
that individually rank below the relevance floor.

The investigation stops there. The prompt was never examined, the model was never in question, and a
larger model would have produced more articulate answers built on the same missing passages. Fix: a
chunking strategy that respects table boundaries, re-index, and a regression run to confirm Recall@5
recovers before anything else is touched.

The general lesson: when quality drops sharply and something changed just before, the thing that
changed is the hypothesis. Sharp drops have causes; gradual drift has drivers.

### How the exam probes it

The scenario gives a symptom plus a timeline detail — a corpus refresh, a re-index, a new document
type, a prompt release, a traffic-mix change. The timeline detail is the answer key. The official
guide's own sample item follows this shape: a RAG system turning confidently wrong right after a
document refresh points at retrieval and indexing, not at the model.

The distractors are consistent across variations:

- Upgrade the model (DISCARD — replaces a working component instead of fixing the broken one).
- Add "do not hallucinate" or similar to the system prompt (REPAIR — patches the symptom downstream
  of a data fault).
- Add logging and monitoring (HALF-MOVE — necessary for next time, does not diagnose this time).
- Add few-shot examples (WRONG-AXIS — correct instrument, wrong failure class).

### Wrong turns and why they are tempting

**Upgrading the model first.** It is a one-line change, it feels decisive, and it is the single most
expensive way to not fix a retrieval bug.

**The anti-hallucination instruction.** It is free and it reads as responsible. It cannot conjure
material that was never retrieved.

**Adding observability instead of diagnosing.** Instrumentation is genuinely valuable and it is not a
diagnosis. Proposing it in response to "why did this break" answers a different question.

**Rewriting the prompt for a data problem.** Prompt work is the layer most teams are most comfortable
in, which is exactly why it gets applied to faults that live elsewhere.

### Takeaways

- Diagnose in order: data and retrieval, then prompt and context, then model mismatch.
- The order is both empirically and economically correct.
- A sharp drop with a change just before it has a cause; name the change.
- Hallucination is three distinct failures with three distinct fixes; identify which from the logs.
- Model mismatch is the conclusion of a diagnosis, not its opening move.

---

## 5. Optimizing token usage, latency, and cost-performance

### The concept

Three quantities, tightly coupled through one shared unit. A token is simultaneously a line of cost
and a line of latency, so reducing tokens usually improves both. Adding context to improve accuracy
worsens both. Optimization in this domain is the discipline of moving along that curve deliberately,
inside a quality bar you declared first.

The sequencing rule that governs everything below: **measure which stage dominates before optimizing
anything.** Halving the time of a stage that consumes 8% of the latency budget buys 4%.

### The levers, ordered by gain-to-risk

**1. Prompt caching.** When a large block of content is byte-identical on every request — a system
prompt, a policy document, a tool schema, a set of few-shot examples — order it first, put the varying
content last, and enable caching. The stable prefix is reused instead of reprocessed, which cuts
time-to-first-token and cost together, and loses nothing. This is the highest-value lever available
and it has essentially no quality downside.

It is also, per the official guide's own sample rationale, the answer whenever a scenario names
latency and cost together. Two conditions matter: the prefix must be genuinely identical (a
timestamp, a session id, or a user name inserted into the prefix destroys it), and the static content
must come first.

**2. Model right-sizing and cascades.** Route the routine majority of traffic to a smaller, faster
model and escalate the hard minority. The escalation trigger must be measured, not assumed — validate
on a labeled set that the small model actually clears the accuracy bar on the class you are routing
to it, per segment.

**3. Retrieval discipline.** Fetching the top 20 passages instead of the top 5 costs tokens on every
request and often reduces accuracy, because the additional passages are noise sitting in the middle
of the context window where attention is weakest. Fewer, better passages is usually both cheaper and
more accurate.

**4. Output shaping.** Output tokens are typically the more expensive side of the ledger, and output
length drives total latency directly, token by generated token. Ask for structured, bounded output;
set a sensible max; drop the preamble the model would otherwise write before the answer.

**5. Context compaction.** For long conversations, extract precision-critical facts verbatim into a
structured block, summarize the general discussion, keep recent turns intact. Uniform summarization
degrades exact values into approximate paraphrase, which is how an amount or an identifier turns into
"approximately."

**6. Streaming.** Streaming reduces *perceived* latency by delivering the first tokens sooner. It does
not reduce total completion time and does not reduce cost. For an interactive interface this is a
large win; for a batch pipeline where no human is waiting, it is nothing. An exam distractor will
offer streaming as a latency fix for a nightly batch job.

**7. Batching and asynchronous processing.** For work with no interactive deadline, moving to
asynchronous or batch processing changes the cost structure without touching quality.

### Worked example

The claims assistant from §1. Per request: an 8,000-token static policy preamble, a 400-token claim
summary, roughly 300 output tokens. Volume 200,000 requests per month.

Without caching, the preamble is billed and processed 200,000 times: 1.6 billion input tokens a month
that are byte-for-byte identical every time. It also sits in front of every request's
time-to-first-token, because it must be processed before generation begins.

Reorder so the preamble sits first and the claim summary last, and enable caching on the prefix. Cache
reads bill at a small fraction of the base input rate — check current pricing for the exact multiplier
— and the prefix does not need reprocessing, so TTFT drops materially. Nothing was removed, no policy
content was lost, and quality is unchanged by construction.

Now the tempting alternative. Someone proposes cutting the preamble from 8,000 tokens to 3,000 by
removing "the parts we rarely need." That saves tokens, and it removes required policy content from a
regulated determination process. It is a compliance regression wearing an optimization's clothes, and
it is exactly the kind of trade a Professional-tier item is built to test.

The stakeholder sentence for this decision: "We reordered the prompt so the unchanging policy text is
cached rather than re-sent, which cut per-claim cost and response time without removing any policy
content." Nobody in that conversation needs to hear the word token.

### How the exam probes it

The dominant shape names two constraints at once — latency *and* cost — with a large repeated static
block in the description. Caching with static-first ordering is the answer.

A second shape names a quality floor plus a budget ceiling. The answer is a cascade with a measured
escalation trigger, not a blanket model downgrade and not a blanket upgrade.

A third shape offers an optimization that quietly removes something required: truncating a policy
preamble, dropping citations, disabling a safety check to save a call. The Professional-tier judgement
is that a saving which breaches a stated constraint is not a saving.

A fourth shape tests the streaming distinction, usually by putting streaming on offer for a
non-interactive workload.

### Wrong turns and why they are tempting

**Truncating required content.** It produces the largest token reduction on the slide and creates a
compliance exposure.

**Summarizing the static preamble with an extra model call.** It sounds clever and adds a whole model
invocation, with its own latency and cost, to solve a problem caching solves for free — while risking
the precision of the policy text.

**Reaching for the largest model "to be safe."** Headroom purchased without a stated requirement is
unpriced cost, and at 200,000 requests a month it is a large one.

**Optimizing before profiling.** Teams reliably optimize the stage they understand best rather than
the stage that dominates the budget.

**Treating streaming as a latency reduction.** The perceived-versus-total distinction is the entire
test.

### Takeaways

- Tokens are simultaneously cost and latency. Measure which stage dominates before optimizing.
- Prompt caching with static content first is the highest-value lever and the exam's default answer
  when latency and cost are both named.
- Any variation in the prefix — a timestamp, a session id — destroys the cache.
- Cascades need a measured escalation trigger, validated per segment.
- Fewer, better retrieved passages is often cheaper *and* more accurate.
- Streaming changes perceived latency only.
- An optimization that breaches a stated constraint is not an optimization.

---

## 6. Monitoring with logging and observability

### The concept

An evaluation tells you what happened on a fixed set of cases. Monitoring tells you what is happening
on traffic nobody anticipated. The evaluation set cannot detect drift, because its input distribution
is frozen by design — that is its virtue as a measuring stick and its blind spot as an alarm.

So production needs its own instrumentation, and the instrumentation has one organizing requirement:
**attribution**. A metric that moved is only useful if you can say what moved it.

### What to log, per request

- Request id, and a trace id spanning the entire chain across services.
- **Model identifier and prompt version.** This is the load-bearing field. Without it, a quality
  change cannot be tied to a release, and every investigation starts with archaeology in the deploy
  log.
- Retrieved document ids and relevance scores. Without these, every RAG diagnosis is guesswork.
- Tool calls: name, arguments, result status.
- Token counts, split input / output / cache-read. Cache-read is what tells you the prefix is still
  intact.
- Latency by stage: retrieval, model call, tool calls, total. An aggregate latency number cannot be
  optimized.
- Guardrail and deterministic-check verdicts.
- The outcome signal: escalation, retry, thumbs-down, resolution, abandonment.

### Online proxies for quality

Offline evaluation is precise and slow. Production gives you cheap proxies that move first:

| Signal | What it usually indicates |
|---|---|
| Escalation rate rising | The system is finding more cases it cannot handle — often a data or coverage change |
| Retry rate rising | Outputs are failing a downstream check |
| Thumbs-down rate rising | Quality regression the deterministic checks do not cover |
| Conversation length rising | Users are working harder to get the same result |
| Abandonment rising | Latency, or a quality failure severe enough that people give up |

None is a quality measurement. All of them move before anyone opens the eval harness, which is what
makes them worth alerting on.

### Continuous quality sampling

Run the model grader on a stratified sample of live traffic — not the whole stream, which is
unnecessary, and not only the flagged cases, which is blind. Stratify across segments and across
verdict classes so the high-confidence automated path is audited too. This is the same stratification
argument from §2, applied online, and it exists for the same reason: novel error patterns surface
first where nobody is looking.

### Alerting

Alert on rates and on segments, not on individual events. One failure is noise; a segment's failure
rate doubling is a signal. Alert on leading indicators — cache-hit rate, retrieval recall proxy, p95
latency, escalation rate — as well as on outcomes, because leading indicators move earlier and are
usually more diagnostic.

### Privacy

Production logs of a real system contain real user data. Redact at write time rather than at read
time, set an explicit retention period, and restrict access. In a regulated sector this is a control
with an auditor attached, not a hygiene preference, and the eval sample drawn from those logs inherits
the same obligations.

### Worked example

Overnight, cost per request triples. Latency p95 rises 1.8 s. Quality metrics are flat.

The cache-hit-rate panel shows 0.93 → 0.11 at 02:14. The prompt-version field shows a release at
02:10. The release inserted a rendered timestamp into the system preamble for debugging, which made
the prefix different on every request and destroyed cache reuse.

Time to diagnosis: about four minutes, because two fields existed — cache-read tokens and prompt
version. Without them, this is a week of bisecting deploys while the finance team asks questions.

The general shape is worth internalizing: cost and latency moved together, quality did not move at
all. That combination points at the token or caching layer rather than at model behaviour, because a
model-behaviour change would have disturbed quality too.

### How the exam probes it

The characteristic scenario is a system that performed well in testing and degrades in production,
and asks what is missing. The answer involves layer-level logging and stratified live sampling rather
than a larger evaluation set — the eval set was not the problem; the absence of a production signal
was.

A second shape gives a metric that moved and asks what would let you attribute it. The answer is
prompt and model version in the request log.

A third shape asks what to alert on, testing rates-and-segments versus individual events, and leading
indicators versus lagging outcomes.

A fourth shape, at Professional tier, adds the compliance angle: logging real traffic in a regulated
sector, with redaction, retention, and access control as part of the correct answer rather than an
afterthought.

### Wrong turns and why they are tempting

**Logging only the final output.** It is the thing you care about, and it is the one field that
cannot tell you which layer produced it.

**A dashboard of aggregate averages.** It looks like observability and reproduces the masking trap in
real time.

**Alerting on every error.** It feels thorough for about a week, after which nobody reads the alerts.

**Adding observability after an incident and calling that the fix.** It is the right investment and
it is not a root-cause remedy; the two get conflated in post-mortems constantly.

**Sampling only complaints.** Efficient, and structurally blind to new failure modes in the automated
stream.

### Takeaways

- Evals measure a frozen set; monitoring measures the distribution you did not anticipate. Both are
  required.
- Log for attribution: trace id, prompt and model version, retrieved ids, tool calls, staged latency,
  split token counts, guardrail verdicts, outcome signal.
- Prompt version in the log is the field that makes attribution possible at all.
- Online proxies — escalation, retry, thumbs-down, abandonment — move before offline metrics.
- Sample live traffic stratified across segments and verdict classes, including the high-confidence
  stream.
- Alert on rates and segments and on leading indicators.
- Cost and latency moving while quality holds points at the token or caching layer.
- Real-traffic logs carry PII: redact at write, set retention, restrict access.

---

## 7. Synthesis — the six objectives as one programme

Take the claims assistant through a full cycle and watch each objective hand its output to the next.

**Week 1 — metrics (obj. 1).** Six metrics, thresholds declared before anything is measured, each
tied to a decision it gates. Accuracy carries a per-claim-type clause. Grounding and PII containment
are hard zeros, because deterministic checks can enforce them. Latency is p95. Cost is dollars per
claim. Every threshold is agreed with the business sponsor while nobody yet knows what the system
scores, which is the only time such a conversation is honest.

**Weeks 2–3 — the dataset (obj. 2).** 400 cases pulled from real submitted claims, stratified across
claim type — including 40 handwritten remittance advices that represent 2% of traffic and 30% of the
risk. Every case hand-verified by an adjuster. Balanced should-fire and shouldn't-fire pairs on each
known failure mode. Grading stack: deterministic checks for schema, citation spans, PII, and
refusal-when-required; an out-of-family model grader on four binary rubric criteria for the
determination text; 50 human-adjudicated cases per week to calibrate the grader. Grader-versus-human
agreement measured at 0.83 before any of its scores are believed. RAG is graded in two layers, and the
escalation gate uses `pass^5 = 1.0` because a missed escalation on an ambiguous claim is
world-acting.

**Ongoing — change control (obj. 3).** Every prompt edit runs the 400-case regression first. Passing
changes go to a two-week A/B split by claim id, primary metric declared, guardrails on latency and
cost declared, results read by segment. Passing variants roll out in stages.

**Month 4 — a degradation (obj. 4).** Grounded-answer rate drops from 0.94 to 0.71. The diagnosis
order runs: retrieval Recall@5 first, which has collapsed from 0.92 to 0.55 following a corpus
refresh that broke table chunking. The model is never touched. The fix is a chunking change, verified
by the regression set before it is released, and the newly discovered failure mode — tables split
across chunks — becomes twelve new cases in the eval set. **This is the loop closing: production just
told the evaluation set something its authors did not know.**

**Month 5 — optimization (obj. 5).** Profiling shows the 8,000-token policy preamble dominates both
cost and TTFT. Reorder static-first, enable caching. Cost per claim and p95 latency both fall. The
proposal to also trim the preamble by 5,000 tokens is rejected, because the removed sections are
regulatorily required and the quality bar declared in week 1 is not negotiable for a cost saving.

**Continuous — monitoring (obj. 6).** Dashboards carry accuracy by claim type, escalation rate, p95
latency by stage, cost per claim, cache-hit rate, and grader-versus-human agreement over time. Alerts
fire on segment rates and leading indicators. A stratified 2% live sample runs through the model
grader daily. Every failure it surfaces becomes a candidate case for the next version of the eval set,
which is re-baselined quarterly.

The programme has one property worth naming: nothing in it depends on anyone's judgement about
whether the system feels better. Every decision is gated by a number that was defined before the
result was known, and every number is attributable to a layer.

---

## 8. Misconceptions

| Misconception | Correction |
|---|---|
| "A bigger evaluation set is a better evaluation set." | Coverage of real failure modes beats count. Enlarging a biased set multiplies the bias and tightens the interval around a wrong number. |
| "97% accuracy means the system is ready to reduce human review." | An aggregate can hide a 40% failure rate on a rare segment. Validate per segment; each must clear the bar independently. |
| "Exact-match against a reference is the most objective way to grade any output." | For open-ended generation it measures string identity with one phrasing. Exact checks belong to schema, fields, citation spans, and forbidden patterns. |
| "Longer, more detailed answers are better answers." | Length correlates with nothing except cost and latency, and model graders reward it through verbosity bias, which is a reason to control for it. |
| "A model can grade its own family's output fine if the rubric is good." | Same-family graders show self-preference bias and share the generator's blind spots. Use a different family, or report the result as degraded. |
| "The grader's score is the system's quality." | An unvalidated grader describes itself. Measure grader-versus-human agreement before believing any of its scores. |
| "A 1–5 quality scale gives more information than pass/fail." | It hides mid-scale uncertainty, drifts between runs, and needs larger samples. Decompose into binary sub-criteria. |
| "One quality score for a RAG system is enough." | Retrieval and generation need separate rows with separate bars. Faithfulness computed over the wrong passages is meaningless. |
| "The agent got the right answer, so the run passed." | Agentic systems grade trajectory and outcome. A correct result reached through a wrong or irreversible path is a failure. |
| "pass@5 and pass^5 both mean 'we tested it five times'." | `pass@k` is reachable success behind a retry; `pass^k` is reliability. World-acting steps need `pass^k`. |
| "The prompt improved on our test examples, so ship it." | A prompt change is a production change: regression set, then controlled A/B on pre-declared metrics, then staged rollout. |
| "We can set the pass threshold once we see baseline numbers." | A bar chosen after the scores is a description of the result. Declare thresholds in advance. |
| "The model started hallucinating, so we need a better model." | Diagnose data and retrieval first, then prompt and context, then model. Hallucination has three distinct causes with three distinct fixes. |
| "Adding logging fixes the problem." | Instrumentation prevents the next incident and diagnoses nothing about this one. |
| "Streaming makes the system faster." | It reduces perceived latency. Total completion time and cost are unchanged, and a batch job gains nothing. |
| "Cutting the system prompt is a free cost saving." | Removing required policy or safety content is a compliance regression, not an optimization. |
| "Safety and security metrics measure the same thing." | Safety is what the model says. Security is what the system permits — injection reaching a tool, over-scoped credentials, data egress. |
| "We audit the low-confidence outputs, so we have coverage." | Novel error patterns appear first in the high-confidence automated stream. Sample it stratified. |

---

## 9. Quick reference

**Metric definition.** Failure + denominator + segment + threshold declared in advance. Latency as
p95/p99, TTFT versus total. Cost per unit of business work. Safety as an achievable non-zero rate;
hard zeros only where a deterministic check enforces them. Security is a separate axis from safety.

**Dataset.** Real traces first. 20–50 hand-verified beats hundreds unverified. Stratify by reporting
segment; over-sample rare high-cost segments. Balance should-fire and shouldn't-fire. A set of
already-handled cases overstates performance and enlarging it does not help.

**Grading stack.** Deterministic checks filter → out-of-family model grader scales → humans calibrate
periodically. Never route a code-checkable property to a model grader. Citation validation is a
verbatim string check.

**Model graders.** Binary sub-criteria over Likert. Different family from the generator. Validated
against human labels (~75% agreement as a starting bar). Guard position, verbosity, self-preference
bias.

**Two-layer shapes.** RAG = retrieval + generation, both must pass. Agentic = trajectory + outcome.
Multi-turn = attribute the first failing turn.

**Aggregation.** `pass@k` = reachable success behind a downstream check. `pass^k` = reliability for
user-visible or world-acting steps.

**Change control.** Regression eval → controlled A/B on pre-declared primary + guardrail metrics →
staged rollout. One variable per variant. Randomize by user or session. Fixed duration. Read results
by segment.

**Diagnosis order.** Data and retrieval → prompt and context → model mismatch. A sharp drop after a
change points at the change. Hallucination types: unsupported-with-context (grounding),
unsupported-without-context (retrieval + refusal), fabricated-under-truncation (context management).

**Optimization.** Profile first. Caching with static-first ordering is the default answer when latency
and cost are both named, and any prefix variation destroys it. Cascades need a measured escalation
trigger. Fewer, better passages. Streaming = perceived latency only. An optimization that breaches a
stated constraint is not one.

**Monitoring.** Log for attribution: trace id, prompt/model version, retrieved ids, tool calls, staged
latency, split token counts, guardrail verdicts, outcome signal. Online proxies move first. Sample
live traffic stratified, including the high-confidence stream. Alert on rates, segments, and leading
indicators. Redact at write, set retention, restrict access.

**Professional-tier overlay on every answer.** What does it cost at real volume · what breaks first
under real traffic · how is it explained to a non-engineer · what does a regulated sector add.
