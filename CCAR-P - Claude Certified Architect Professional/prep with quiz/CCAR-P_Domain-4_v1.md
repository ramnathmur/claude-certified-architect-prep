# Domain 4 — Evaluation, Testing & Optimization

**Weight:** 16% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Define evaluation metrics (accuracy, latency, cost, safety, security) · Design evaluation datasets and test frameworks using mixed methodologies · Conduct A/B testing and iterative improvements · Diagnose system issues (prompt failure, hallucinations, model mismatch) · Optimize token usage, latency, and cost-performance trade-offs · Monitor system performance using logging and observability tools

---

## 4.1 Metric Definition — Threshold Declared in Advance

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Define evaluation metrics (accuracy, latency, cost, safety, security) |
| A finished metric | Named failure + denominator + segment + threshold set before results are seen |
| Latency form | p95/p99, not the mean; TTFT for interactive, total for batch |
| Cost form | Per unit of business work (per resolved ticket, per claim), not per token |
| Hard zero permitted when | A deterministic check can enforce it (PII field present, citation span missing) |
| Hard zero forbidden when | The property is open-ended and model-judged — set a small achievable non-zero rate |

### Threshold Timing — Declared in Advance vs Set After Results

The discriminator is *when* the number was chosen: a bar fixed before any score is seen gates a decision; a bar chosen afterwards only describes the result.

| Situation | Answer | Why |
|---|---|---|
| New capability, no baseline yet | Set the bar from the success criterion, frontier reality, or the current process's error rate | An anchored bar is still a bar; "we'll decide later" is not |
| Stakeholder asks to "calibrate the threshold once we see baseline numbers" | Reject — set it now, revise it as a recorded decision later | A post-hoc bar is only ever revised downward |
| Existing manual process with a measured 8% error rate is being replaced | Bar tied to and beating 8% | The replacement's bar has a real-world anchor |
| Open-ended safety property, proposed bar of 0% | Re-anchor to a small non-zero rate (e.g. < 0.1% of 10,000) | An unachievable bar becomes non-binding on first miss |
| Requirement is "outputs must never contain another customer's account id" | 0 per N — deterministic check | Code can enforce it exactly |

### Exam scenario: a business sponsor states the assistant "must be fast, accurate, and safe"

- ✅ Convert each adjective into a metric with a named failure, a denominator, a reporting segment, and a threshold agreed before measurement begins
- ❌ Track average response time, average response length, and daily request volume — **WRONG-AXIS**: these are collectable telemetry, not decision-gating metrics; none of them corresponds to any of the three stated requirements
- ❌ Define one composite quality score and set its pass bar after establishing a baseline — **ARCHITECTED**: a single tidy number sounds like executive-grade reporting, but it cannot be diagnosed when it moves, and the bar is being chosen after the result

### ❌ Misconception
"We'll set the pass threshold once we see what the baseline looks like." — A bar chosen after the scores is a description of the result, not a gate on it; anchor it in advance to the success criterion, frontier reality, or the process being replaced.

---

## 4.2 Metric Family — Safety vs Security

### Core Facts

| Attribute | Value |
|---|---|
| Safety measures | What the model says — policy-violating, toxic, or non-compliant output |
| Security measures | What the system permits — injection reaching a tool, over-scoped credentials, data egress via tool results |
| Safety instrument | Rate over a stated denominator, model-graded or classifier-graded |
| Security instrument | Adversarial suite — attempted-injection block rate, unauthorized-tool-invocation count, least-privilege audit |
| Independence | A system can pass every safety metric and fail every security control |

### Requirement Classification — Output Content vs System Permission

The discriminator is whether the risk is realised by what the model *emits* or by what the system *allows it to do*.

| Situation | Family | Why |
|---|---|---|
| "The assistant must not produce discriminatory language" | Safety | The harm is in the emitted text |
| "A malicious instruction inside a retrieved document must not trigger a refund tool call" | Security | The harm is a permitted action, not a sentence |
| "The agent must not be able to read records outside the requesting customer's account" | Security | Authorization scope, measured by audit and adversarial probe |
| "Outputs must not include another policyholder's identifier" | Both — deterministic PII check is the enforcing control | Content check enforces a security property; log it under both |
| Proposal to cover a prompt-injection risk with a tone rubric | Reject | A quality rubric cannot measure whether a tool fired |

### Exam scenario: a RAG agent with tool access ingests third-party documents; the risk raised is instruction injection

- ✅ Build an adversarial suite of injected documents and measure block rate on unauthorized tool invocations, alongside a least-privilege audit of the agent's tool set
- ❌ Add prompt-injection wording to the safety rubric the model grader scores — **WRONG-AXIS**: right vocabulary, wrong instrument; a content rubric cannot observe whether a tool call fired
- ❌ Log every tool invocation and review the logs weekly — **HALF-MOVE**: detection after the fact, with no measured block rate and no reduction of the permitted capability

### ❌ Misconception
"Safety and security metrics are two names for the same thing." — Safety scores emitted content; security scores what the system permits the model to do, and it is measured against an adversarial suite, not a quality rubric.

---

## 4.3 Evaluation Dataset Composition — Coverage over Count

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design evaluation datasets and test frameworks using mixed methodologies |
| Source priority | Real production traces → synthetic → hand-written for expected-but-unobserved failures |
| Working size | 20–50 hand-verified cases beat hundreds of unverified synthetics |
| The bias | A set built from cases the system already handles overstates performance |
| The non-fix | Enlarging that set multiplies the bias and narrows the interval around a wrong number |
| Balance rule | Roughly equal should-fire and shouldn't-fire cases |

### Set Repair — Recompose vs Enlarge

The discriminator is whether the set's *composition* or its *size* is the defect. A set missing failure modes is never fixed by adding more of what it already contains.

| Situation | Answer | Why |
|---|---|---|
| 500-case set reports 96%, customers still report failures | Rebuild from real production failures and report by segment | The set omits the failure classes that are occurring |
| Same situation, proposal to expand to 2,000 cases drawn the same way | Reject | Same sampling process, four times the bias, tighter interval on a wrong number |
| Set has 600 unverified synthetic cases with an unknown label error rate | Cut to 40 hand-verified cases | An unverified case adds a score without adding information |
| Set contains only failure cases | Add matched shouldn't-fire cases | An all-negative set hides false alarms |
| Set contains only clean cases | Add should-fire cases per known failure mode | An all-positive set hides misses |
| Genuinely new capability, no production traces exist yet | Hand-write cases and label the whole set provisional until real traces confirm the failure modes | Spec-derived failure modes are hypotheses, not findings |

### Exam scenario: an eval set scores 96% while production complaints continue

- ✅ Rebuild the evaluation set from real production failures, stratified by segment, and report accuracy per segment
- ❌ Expand the set from 500 to 2,000 cases using the same collection process — **HALF-MOVE**: more data is the right reflex almost everywhere else; here it scales the sampling bias rather than removing it
- ❌ Generate the additional cases with the same model that serves production — **DISCARD**: replaces human-verified grounding with the model's own competence and phrasing distribution, guaranteeing the set contains nothing the model cannot already do

### ❌ Misconception
"A bigger evaluation set is a better evaluation set." — Coverage of the failure modes that actually occur beats count; a biased set enlarged is a biased set with a tighter confidence interval.

---

## 4.4 Stratified Reporting — the Aggregate-Accuracy Mask

### Core Facts

| Attribute | Value |
|---|---|
| The trap | An aggregate 97% accuracy can conceal a 40% failure rate on a rare segment |
| Sampling rule | Build the eval set to answer per-segment questions, not to mirror production frequency |
| Rare-segment rule | Over-sample rare, high-cost segments relative to their traffic share |
| Practical floor | A segment needs enough cases to support a rate (~30 as a working floor), not one |
| Gate on reducing oversight | Every segment clears the bar independently, not the weighted average |
| Live extension | Stratified sampling of the automated high-confidence stream, not only the flagged queue |

### Sampling Basis — Reporting Segments vs Natural Frequency

The discriminator is what the number has to answer. Sampling at natural frequency optimizes for a representative aggregate; per-segment reporting requires deliberate over-sampling of the rare segments.

| Situation | Answer | Why |
|---|---|---|
| 50-case set, document mix 78/15/5/2 across four types | Rebuild with enough cases per type to support a rate | At natural frequency the 2% segment gets one case; one case cannot measure a rate |
| Team proposes auto-processing everything above an aggregate confidence threshold | Analyse accuracy by document type and field first | The aggregate averages away the segment that fails 40% of the time |
| Ongoing audit of an automated extraction path | Stratified random sample across document types and field categories | Novel error patterns surface first in the high-confidence stream |
| Proposal to review only the lowest-confidence extractions | Reject as the sole audit | The automated path goes unmeasured exactly where volume is highest |
| Proposal to sample only the most common document type | Reject | Under-samples the worst-performing segments by construction |

### Exam scenario: an extraction system shows 97% overall accuracy and the team proposes auto-processing all high-confidence output

- ✅ Analyse accuracy by document type and field segment first, then auto-process only segments with independently validated accuracy, with stratified random sampling of the automated stream for ongoing error measurement
- ❌ Auto-process everything above the aggregate confidence threshold — **WRONG-AXIS**: uses an aggregate number to make a per-segment decision; a rare document type may fail 40% of the time inside that 97%
- ❌ Trust the model's self-reported confidence scores directly as the routing signal — **HALF-MOVE**: confidence routing is the right mechanism, but raw self-reported confidence is unreliable until calibrated against a labeled validation set

### ❌ Misconception
"97% accuracy means we can safely reduce human review." — Aggregates average away segment-level failure; every segment must clear the bar independently before oversight is reduced anywhere.

---

## 4.5 Grader Selection — Deterministic First

### Core Facts

| Attribute | Value |
|---|---|
| Layering order | Deterministic code checks filter → model grader scales subjective quality → humans calibrate periodically |
| Deterministic reach | Schema validity, field match, numeric compare, regex, forbidden-pattern/PII scan, execution against tests, tool-call ordering, refusal-when-required, verbatim citation-span existence |
| Citation validation | Verbatim string check, not a model grader — judges score citation validity at roughly 38% in cited studies |
| Human grader's job | Ground-truth labeling and periodic calibration of the model grader, not grading at scale |
| Solvability bar | If two domain experts would not independently reach the same verdict, no automated grader is trustworthy at any threshold |

### Instrument Choice — Code-Checkable vs Genuinely Subjective

The discriminator is whether the property has an exact, machine-decidable answer. If it does, a model grader is a strictly worse instrument regardless of how good the rubric is.

| Situation | Answer | Why |
|---|---|---|
| "Every output must be valid JSON matching this schema" | Deterministic schema validation | Exact, free, reproducible |
| "Every cited passage must exist verbatim in the cited document" | Deterministic verbatim string check | Judges are near-chance on citation validity |
| "No output may contain another customer's account identifier" | Deterministic pattern/field scan | Enforceable as a hard zero |
| "The answer must be in the right register for a regulated communication" | Model grader with a binary rubric | No code check reaches tone |
| "The summary must be faithful to the source" | Model grader for faithfulness, with an overlap metric as a cheap floor | Faithfulness is semantic; the overlap metric alone is not sufficient |
| Ambiguous cases where two adjusters disagree on the verdict | Human adjudication, and re-scope the eval row | Unstable ground truth defeats every automated grader |

### Exam scenario: the team proposes an LLM-graded rubric for "output conforms to the required JSON schema and cites only real document sections"

- ✅ Route both properties to deterministic checks — schema validation and a verbatim citation-span check — and reserve the model grader for the subjective criteria
- ❌ Build a detailed grading rubric and have a model score both properties — **ARCHITECTED**: an elaborate rubric reads as rigorous, but it introduces grader error into two properties code settles exactly and for free
- ❌ Have humans review a sample of outputs for schema and citation errors — **WRONG-AXIS**: humans are the calibration instrument, not the scaling one; this spends the scarcest resource on the cheapest check

### ❌ Misconception
"An LLM judge with a good rubric can grade anything." — Never route a code-checkable property to a model grader; deterministic checks are exact, free, and immune to grader error, and citation validation in particular is a verbatim string check.

---

## 4.6 Model-Graded Evaluation — Out-of-Family and Human-Calibrated

### Core Facts

| Attribute | Value |
|---|---|
| Rubric form | Binary sub-criteria; whole-output pass = all hard criteria pass |
| Why not 1–5 | Hides mid-scale uncertainty, drifts between runs, needs larger samples, aggregates poorly |
| Family rule | Grader must be a different model family than the generator |
| Same-family effect | Self-preference bias plus correlated blind spots — the failures it cannot see are the generator's failures |
| Trust gate | Measure grader-vs-human agreement on a hand-labeled sample before believing any score (~75% as a starting bar, not a settled constant) |
| Known biases | Position (favours first/last), verbosity (rewards length), self-preference |
| Bias guards | Randomize and swap option order and aggregate both; binary length-controlled criteria; out-of-family grader |

### Grader Trust — Validated Against Human Labels vs Assumed

The discriminator is whether the grader itself has been measured. An unvalidated grader's scores describe the grader, not the system.

| Situation | Answer | Why |
|---|---|---|
| New model grader proposed for tone and helpfulness | Hand-label 20–50 cases, run the grader, compute agreement, then decide | The grader is the measuring instrument and has not been calibrated |
| Agreement measured at 0.62 | Rebuild the criterion as binary sub-criteria and re-validate before use | A fuzzy scalar is the most common cause of low agreement |
| Agreement still below bar after rework, no deterministic fallback exists | Drop the row and record why | An untrustworthy grader shipped as validated is worse than no row |
| Only a same-family grader is available | Use it but mark the row degraded; never report it as ground truth | Self-preference bias and shared blind spots |
| Grader has been in production six months, never re-audited | Resume periodic human calibration | Agreement drifts; a grader that was trusted is not permanently trusted |

### Exam scenario: a team reports 4.2/5 average quality from a model grader of the same family as the production model

- ✅ Rebuild the rubric as binary sub-criteria, switch to an out-of-family grader, and validate it against a hand-labeled sample before reporting any score
- ❌ Report the 4.2/5 and set the pass bar at 4.0 — **HALF-MOVE**: it produces a number and a threshold, on an uncalibrated same-family grader whose scale nobody can define
- ❌ Increase the sample from 100 to 1,000 outputs to make the average more reliable — **WRONG-AXIS**: more samples tighten the estimate of a biased grader's own score; the defect is the grader, not the sample size

### ❌ Misconception
"If the rubric is detailed enough, the judge's score is the system's quality." — An unvalidated grader describes itself; measure grader-vs-human agreement first, use binary criteria, and never grade a model with its own family.

---

## 4.7 Two-Layer Evaluation — RAG and Agentic

### Core Facts

| Attribute | Value |
|---|---|
| RAG layers | Retrieval (Recall@k / context precision vs gold passage ids) + generation (faithfulness / answer relevancy) |
| RAG rule | Both layers must clear their own bar; a single blended score is a defect |
| Why | Faithfulness computed over the wrong passages is meaningless, and retrieval is the more common failure |
| Agentic layers | Trajectory (tool selection, step order) + outcome (final state, task completion) |
| Agentic rule | A correct result reached via a wrong or irreversible path is a failure |
| Multi-turn rule | Attribute the first failing turn, not just the final state |

### Grading Granularity — Per-Layer vs Blended

The discriminator is whether the system has an internal step whose failure the final output can disguise.

| Situation | Answer | Why |
|---|---|---|
| RAG assistant with one overall quality score, regression cannot be located | Split into retrieval and generation rows | The blended score cannot say which layer moved |
| Retrieval Recall@5 = 0.55, generation faithfulness = 0.97 | Both bars are read; the system fails on retrieval | High faithfulness to the wrong passages is not quality |
| Agent completes the task but deleted a record on the way | Fail | Trajectory row exists precisely for this |
| Agent selects correct tools in correct order but final state is wrong | Fail | Outcome row exists precisely for this |
| Multi-turn assistant recovers by turn 6 from a turn-2 error | Report the turn-2 failure | A late correction masks a defect that will not always self-correct |

### Exam scenario: a RAG system's single quality metric drops and the team cannot identify the cause

- ✅ Split evaluation into a retrieval row (Recall@k against gold passage ids) and a generation row (faithfulness), each with its own pass bar
- ❌ Improve the grading rubric for the overall quality score — **HALF-MOVE**: a better rubric on a blended score still cannot attribute the drop to a layer
- ❌ Move to a higher-capability model to raise the overall score — **DISCARD**: replaces a component that has not been shown to be at fault, and produces more articulate answers over the same passages

### ❌ Misconception
"One quality score is enough if the rubric is good." — RAG grades retrieval and generation separately, agentic systems grade trajectory and outcome separately, and multi-turn attributes the earliest failing turn; a blended score cannot locate a regression.

---

## 4.8 Reliability Aggregation — pass@k vs pass^k

### Core Facts

| Attribute | Value |
|---|---|
| `pass@k` | Passes when at least one of k attempts succeeds — measures reachable success |
| `pass^k` | Passes when all k attempts succeed — measures reliability |
| `pass@k` fits | A downstream validator or test catches failures and triggers a retry |
| `pass^k` fits | Every attempt is user-visible or acts in the world |
| Hard gate | Any irreversible-action step is a gate regardless of the aggregate score |

### Aggregation Choice — Is Every Attempt Consequential?

The discriminator is whether a failed attempt is absorbed by a downstream check or reaches the world.

| Situation | Answer | Why |
|---|---|---|
| Code generation with a test harness that reruns on failure | `pass@k` | The harness absorbs failures; reachable success is what matters |
| Tool call behind a schema validator that retries on rejection | `pass@k` | Same structure |
| Agent must confirm with a human before any irreversible action | `pass^k` = 1.0 | One silent irreversible action in k attempts is a failed control |
| Every generated answer is shown directly to a customer | `pass^k` | There is no retry; each attempt is the product |
| Confirmation gate reported as `pass@5 = 1.0` | Reject the framing | A gate that fires once in five attempts would score as passing |

### Exam scenario: an agent that can issue refunds must confirm with a human before acting

- ✅ Grade the confirmation gate as `pass^k` — every attempt must halt for confirmation, one silent action is a hard fail
- ❌ Grade it as `pass@k` alongside the task-completion row — **WRONG-AXIS**: right metric vocabulary, wrong aggregation; `pass@k` would score a gate that fires once in five attempts as passing
- ❌ Apply `pass^k = 1.0` to every row in the plan, including task completion — **OVERSPEC**: a stronger guarantee than the requirement asks for; the completion step sits behind a validator that retries, so demanding perfect first-pass reliability there sets an unreachable bar and makes the whole plan non-binding

### ❌ Misconception
"pass@5 and pass^5 both mean we tested it five times." — `pass@k` measures reachable success behind a retry; `pass^k` measures reliability, and any user-visible or world-acting step needs `pass^k`.

---

## 4.9 Prompt Change Release Path — Regression, Then Controlled A/B

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Conduct A/B testing and iterative improvements |
| The order | Regression evaluation on the fixed set → controlled A/B against the current prompt on metrics defined in advance → staged rollout |
| Why regression first | The A/B costs live traffic, and only the fixed set over-samples rare segments |
| Why A/B second | The fixed set cannot report on the live distribution, real load, or production latency |
| Attribution rule | One variable per variant |
| Randomization unit | User or session — never per request |
| Metrics rule | Primary metric plus guardrails declared before launch; guardrails can only block |
| Stopping rule | Fixed duration and sample size; no stopping early on favourable numbers |
| Reading rule | Report by segment as well as in aggregate |

### Change Gating — Attributable and Pre-Gated vs Neither

The discriminator is whether the change was checked before it touched traffic and whether a result could be attributed to it.

| Situation | Answer | Why |
|---|---|---|
| Prompt edit looked better on ten hand-picked examples | Run the regression set first, then a controlled A/B | Ten non-randomly chosen examples is persuasive and is not evidence |
| Variant changes prompt, model, and retrieval depth together | Split into separate variants | A win is unattributable and the next regression has three suspects |
| A/B randomized per request | Re-randomize by user or session | Conversations flip prompts mid-thread, corrupting behaviour and metric together |
| Test looks favourable at day 4 of a planned 14 | Run to the declared duration | Stopping on good news inflates the false-positive rate |
| Variant improves the primary metric, breaches the declared latency guardrail | Do not ship | Guardrails were declared to block precisely this |
| Aggregate improves 1.5 points, one segment regresses 12 | Do not ship on the aggregate | Segment masking applies to A/B results as it does to accuracy |
| Change already shipped to 100% with no control arm | State that no clean comparison exists | Before/after is confounded by everything else in the window |

### Exam scenario: a prompt change improves output on a set of examples the team reviewed manually

- ✅ Run the change against the fixed regression set first, then a controlled A/B against the current prompt with the primary metric and guardrails declared in advance, then roll out in stages
- ❌ Deploy to 100% and monitor the quality dashboard for regressions — **REPAIR**: catches damage after users absorb it, and with no control arm the comparison is confounded
- ❌ Skip the regression set and go straight to a live A/B because live traffic is more representative — **HALF-MOVE**: live traffic delivers rare segments at natural frequency, so a regression confined to one of them will not surface

### ❌ Misconception
"The new prompt clearly performs better on our examples, so we can ship it." — A prompt change is a production change: regression set first, then a controlled A/B on pre-declared metrics with one variable changed, then staged rollout.

---

## 4.10 Diagnosis Order — Data and Retrieval Before Model

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Diagnose system issues (prompt failure, hallucinations, model mismatch) |
| Order | Data and retrieval → prompt and context → model mismatch |
| Why this order | Each earlier layer poisons everything downstream, and checking it is far cheaper |
| Timeline rule | A sharp drop with a change immediately before it — the change is the hypothesis |
| Hallucination type A | Unsupported claim while context contained the answer → grounding/prompt; fix with cited spans + verbatim check |
| Hallucination type B | Unsupported claim while retrieval returned nothing relevant → retrieval fix + explicit refusal/escalation path |
| Hallucination type C | Fabrication under truncation or compaction → context management; extract critical facts verbatim |
| Model mismatch signature | Fails broadly on genuinely multi-step reasoning with retrieval verified and prompt clean |

### Fault Layer — What Changed vs What Is Easiest to Change

The discriminator is which layer the symptom's timing and shape point at, not which layer is quickest to swap.

| Symptom | Layer | Not the cause |
|---|---|---|
| Confidently wrong right after a document refresh or re-index | Retrieval / indexing | The model, which did not change |
| Wrong on one document or query type, correct elsewhere | Data coverage / chunking | A general capability deficit |
| Facts correct, required format or steps missing | Prompt / instructions | Retrieval |
| Format inconsistent across runs despite explicit instructions | Few-shot examples needed | More prose instruction, which has already failed |
| Fails only on long inputs; misses mid-document facts | Context structure and position | Context window exceeded |
| Forgets a fact from two turns ago in a short conversation | Application not resending history | Context limit — the API is stateless |
| Fails broadly on multi-step reasoning, retrieval verified, prompt clean | Model mismatch | Anything upstream, already cleared |

### Exam scenario: a RAG assistant becomes confidently wrong in the week following a corpus refresh

- ✅ Check retrieval first — measure Recall@k against gold passage ids and inspect how the refreshed documents were chunked and indexed
- ❌ Move to a higher-capability model — **DISCARD**: replaces a component that was never implicated, and produces more fluent answers built on the same missing passages
- ❌ Add an explicit instruction to the system prompt not to state facts it cannot support — **REPAIR**: patches the symptom downstream of a data fault, and cannot conjure material that was never retrieved

### ❌ Misconception
"The model started hallucinating, so we need a better model." — Diagnose data and retrieval first, then prompt and context, then model mismatch; hallucination has three distinct causes with three distinct fixes, and model mismatch is a conclusion, not an opening move.

---

## 4.11 Cost and Latency Optimization — Caching First

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Optimize token usage, latency, and cost-performance trade-offs |
| Coupling | A token is simultaneously a cost line and a latency line |
| Sequencing | Profile which stage dominates the budget before optimizing anything |
| Highest-value lever | Prompt caching — static content first, dynamic last; cuts TTFT and cost together with no quality loss |
| Cache-breaking | Any variation in the prefix — timestamp, session id, user name — destroys reuse |
| Cascade rule | Route the routine majority to a smaller model; the escalation trigger must be measured per segment, not assumed |
| Retrieval lever | Fewer, better passages is often cheaper *and* more accurate |
| Streaming | Reduces perceived latency only; total time and cost unchanged; worthless for batch |
| Hard limit | An optimization that breaches a stated quality, policy, or compliance constraint is not an optimization |

### Optimization Choice — Reuse the Content vs Remove the Content

The discriminator is whether the saving preserves everything the requirement demands. Reordering for cache reuse loses nothing; truncation loses content.

| Situation | Answer | Why |
|---|---|---|
| Identical large policy preamble on every request; latency and cost both named | Order static content first and enable prompt caching | The stable prefix is reused; both metrics improve, nothing is lost |
| Same situation, proposal to cut the preamble by 60% | Reject if the removed sections are required | A compliance regression, not a saving |
| Same situation, proposal to summarize the preamble with an extra model call at request time | Reject | Adds a full model invocation with its own cost and latency, and degrades policy precision |
| Quality floor plus a budget ceiling, mixed task difficulty | Cascade: small model for the routine class, escalate the rest, trigger validated per segment | Matches capability to what each class actually requires |
| Nightly batch job, latency complaint | Batch/async and output shaping | Nobody is watching a cursor; streaming changes nothing here |
| Retrieval fetches top 20 passages | Reduce to the passages that clear the relevance floor | Noise in the middle of the window costs tokens and accuracy |
| Latency complaint, no stage-level timing collected | Profile first | Halving a stage worth 8% of the budget buys 4% |

### Exam scenario: an identical large system preamble is sent on every request and both p95 latency and monthly cost are over target

- ✅ Reorder so the static preamble comes first and the varying input last, and enable prompt caching
- ❌ Truncate the preamble to the sections used most often — **DISCARD**: removes required content to solve a problem reuse solves without any loss
- ❌ Enable response streaming to bring the latency number down — **WRONG-AXIS**: streaming changes perceived latency, not total completion time, and does nothing for cost

### ❌ Misconception
"Cutting the system prompt is a free cost saving." — Removing required policy or safety content is a compliance regression; caching reuses the same content at a fraction of the cost and latency without removing anything.

---

## 4.12 Observability — Logging for Attribution

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Monitor system performance using logging and observability tools |
| Division of labour | Evals measure a frozen set; monitoring measures the distribution nobody anticipated. Both required |
| Load-bearing field | Prompt version and model identifier per request — without it no metric change is attributable to a release |
| Minimum log | Trace id · prompt/model version · retrieved document ids and scores · tool calls with arguments and results · token counts split input/output/cache-read · latency by stage · guardrail verdicts · outcome signal |
| Online proxies | Escalation rate, retry rate, thumbs-down rate, conversation length, abandonment — they move before offline metrics |
| Live sampling | Stratified across segments *and* verdict classes, including the high-confidence automated stream |
| Alerting | On rates and segments, and on leading indicators — not on individual events |
| Signature | Cost and latency move together while quality holds → token or caching layer, not model behaviour |
| Regulated overlay | Redact at write time, set retention, restrict access — the eval sample inherits the same obligations |

### Instrumentation Purpose — Attribution vs Recording

The discriminator is whether the logged fields let you say *which layer and which release* moved the metric.

| Situation | Answer | Why |
|---|---|---|
| Quality metric moved, cause unknown, only final outputs are logged | Add prompt/model version, retrieved ids, tool calls, staged latency | Output alone cannot name the layer that produced it |
| Cost tripled overnight, latency up, quality flat | Check cache-read token counts and the prompt-version field | That combination points at the caching or token layer |
| Dashboard shows aggregate averages only | Add per-segment breakdowns | The masking trap reproduced in real time |
| Alerting configured to fire on every individual error | Alert on rates and segment rates instead | Per-event alerting is ignored within a week |
| Only complaints and flagged outputs are sampled for quality | Add stratified sampling of the high-confidence stream | Novel error patterns appear first where nobody is looking |
| Post-incident, the proposed remedy is "add monitoring" | Accept as prevention, not as the root-cause fix | Instrumentation diagnoses the next incident, not this one |
| Regulated sector, real-traffic logs | Redact at write, define retention, restrict access | A control with an auditor attached |

### Exam scenario: a system that performed well in pre-production degrades in production and the team cannot say why

- ✅ Instrument for attribution — prompt/model version, retrieved document ids, tool calls, staged latency, split token counts, outcome signals — and add stratified sampling of live traffic through the grading stack
- ❌ Expand the pre-production evaluation set — **WRONG-AXIS**: the eval set is a frozen distribution and cannot observe production drift, which is the actual gap
- ❌ Log every request and response in full and review them when problems arise — **HALF-MOVE**: volume without the attribution fields, and in a regulated sector it creates a retention and PII exposure of its own

### ❌ Misconception
"We log everything, so we have observability." — Observability means attribution: without prompt version, retrieved ids, staged latency, and split token counts, a metric that moved cannot be tied to a layer or a release.
