# CCAR-P Lesson — Domain 3: Integration

**Weight:** 19% — the heaviest of the seven domains
**Objectives:** 8 — more than any other domain
**Source for weight and objectives:** official exam guide v1.0, effective July 2026, §6

---

## What this domain is actually about

Domains 1 and 2 are about the system you design. Domain 3 is about everything your system has to touch that you did not design: the identity provider someone configured in 2019, the document store whose refresh job runs at 02:00, the downstream service with a 400ms p99, the ticketing system whose API predates REST conventions. Integration is the discipline of connecting a probabilistic component to a deterministic estate without either one corrupting the other.

The eight objectives look scattered on first read — tool bloat, auth, latency, observability, chunking, retrieval, protocols, discovery. They share one spine. **Every one of them is an admission-control decision: what gets into the model's context, what the model is allowed to reach, what that admission costs, and what record you keep of it.**

Read the objectives through that lens and they line up:

| Objective | The admission question it answers |
|---|---|
| Capability bloat | How many capabilities enter the agent's decision space? |
| Auth/authz gaps | Whose privileges does the agent exercise when it reaches out? |
| Accuracy–latency trade-offs | What does each admitted thing cost in time? |
| Observability at scale | What record do you keep of what was admitted and why? |
| RAG chunking and indexing | What shape does admitted knowledge arrive in? |
| Retrieval strategy | How do you decide which knowledge gets admitted for this query? |
| Connection protocols | Through which door does anything get admitted at all? |
| Progressive vs monolithic | Does everything get admitted up front, or on demand? |

Hold that spine. Professional-tier questions in this domain rarely ask "what is X." They give you a production system that is misbehaving, or a design proposal with a cost or SLA attached, and ask which change addresses the cause. The candidates who lose marks here are usually adding something — a classifier, a logging rule, a confirmation prompt — where the correct answer removes or narrows something.

A note on exam mechanics before we start, because it matters for how you budget attention. The exam has 63 items and 120 minutes, scored on a 100–1000 scale with a 720 pass mark, and there is no per-domain floor: pass/fail runs on total scaled score alone. At 19%, Domain 3 carries more of that total than any other single domain. Two things about the exam's structure are genuinely unknown and should not be assumed either way — whether items stand alone or are grouped into shared-scenario blocks, and whether multiple-response items are scored all-or-nothing or with partial credit. Prepare as though multiple-response items are all-or-nothing, because that is the more expensive assumption to get wrong.

---

## Objective 1 — Evaluate tool/agent configuration for capability bloat

### The concept from first principles

A tool is not free, and it is not free in two separate currencies.

The first is **tokens**. Every tool definition — name, description, input schema — is serialized into the request. It is present whether the tool is used or not. A tool surface is a fixed tax on every single call.

The second currency is **discrimination**, and it is the one that actually breaks systems. The model selects a tool by reading the descriptions and matching them against the request. With five tools that is a five-way decision over reasonably distinct options. With twenty-two, it is a twenty-two-way decision, and the marginal tools are far more likely to be near-neighbours of ones already there: `search_documents` beside `find_files` beside `query_knowledge_base`. Selection error does not scale linearly with tool count, because the density of confusable pairs grows faster than the count does.

There is a third cost that only shows up in incident review. Every tool is a **privilege**. A tool the agent never legitimately needs is still a tool it can call when a prompt goes sideways or a user is adversarial. Blast radius is a function of the tool surface, not of the intended workflow.

The Foundations-tier framing of this is "least privilege." The Professional-tier framing adds the arithmetic: what does the bloat cost per day, and what breaks first at volume.

### Worked example

An internal operations agent has accumulated 22 tools over three quarters, because each new integration was added to the same agent rather than to a scoped one.

Token cost: tool definitions average roughly 200 tokens each once the input schema is included. 22 tools is about 4,400 tokens present on every request before a single word of user content. At 40,000 requests per day, that is 176 million tokens per day spent describing tools, the large majority of which are irrelevant to any given request.

Selection cost: audit of a week of traces shows misroutes concentrated in three pairs — `get_customer` / `get_account`, `search_tickets` / `search_knowledge`, `send_notification` / `create_alert`. Misroute rate on requests touching those domains is 11%. On requests touching the other sixteen tools it is under 2%.

The fix is not one change but a decomposition. Split the agent by role: a customer-lookup agent with 4 tools, a knowledge agent with 3, a notification agent with 3. Each request routes to one role. Tool surface per request drops from 22 to 3–4, token cost per request drops by roughly 3,700, and the confusable pairs are now in *different agents*, so the discrimination problem disappears rather than being mitigated.

Then, and only then, tighten the descriptions on the pairs that remain confusable within a single agent.

### How the exam probes it

The scenario shape is: an agent with a stated, uncomfortably large number of tools, exhibiting a stated failure — wrong tool called, or an agent doing work outside its specialization (a synthesis agent running open-ended web searches). Sometimes a token cost or a latency figure is attached to force the trade-off.

The correct answer restricts the tool set to the role's actual scope, or replaces a broad tool with a narrow one that makes the unwanted behaviour impossible at the interface. The exam consistently prefers a constraint enforced by the tool's own definition over a constraint asserted in a prompt.

There is one sanctioned exception worth knowing, because it appears as a distractor in the other direction. If a scoped agent has a genuine **high-frequency** need that would otherwise round-trip through a coordinator on every turn, giving it a narrowly scoped cross-role tool is correct — with complex cases still routed through the coordinator. Strict scoping taken to an extreme produces its own failure mode.

### Wrong turns and why they tempt

**Improve every tool description instead of cutting the count.** Tempting because descriptions genuinely are the primary lever for tool selection, so this answer is *partially* right. It is a HALF-MOVE: it improves discrimination without reducing the decision space, and it does nothing about the token tax or the privilege surface.

**Add a routing classifier in front of the agent.** Tempting because it sounds like proper architecture — a dedicated component with a single responsibility. It adds a component, a failure mode, and a latency hop to compensate for a configuration problem that a smaller tool set solves outright.

**Keep all tools "for flexibility."** Tempting to anyone who has been burned by an agent that could not do what a user asked. Flexibility on a tool surface is indistinguishable from ambiguity, and the cost lands on every request.

**Merge confusable tools into one general tool.** `get_customer` plus `get_account` becomes `lookup_entity`. Tool count drops, which looks like the right direction. Semantic precision drops with it, and the discrimination problem moves from tool selection into parameter selection where it is harder to observe.

### Takeaways

- Tool count is a cost in tokens, in selection accuracy, and in blast radius. Price all three.
- Reduce the decision space before improving the descriptions; do both, in that order.
- Prefer a narrow tool that makes misuse impossible over a broad tool plus an instruction not to misuse it.
- Role-scoped agents beat one agent with a large catalog. The exception is a narrowly scoped cross-role tool for a genuinely high-frequency need.
- Merging tools to reduce count is not the same as scoping them; merging trades one failure mode for a less visible one.

---

## Objective 2 — Analyze authentication and authorization requirements to identify security gaps

### The concept from first principles

Authentication answers *who is calling*. Authorization answers *what that caller may do*. In conventional application architecture these two travel together through the whole request path: the user's identity is established at the edge and carried down, and each layer enforces what that identity may reach.

LLM integrations break the assumption quietly. The agent runs as a service. When it calls a tool, the tool is usually invoked with the *agent's* credentials, not the user's. Every user collapses into a single identity at the point where the actual data access happens. This is the confused-deputy problem: a privileged component acting on behalf of a less-privileged caller, with the caller's constraints stripped off in transit.

The consequence is that authorization must be re-established explicitly, at the layer where the data is actually reached. For a RAG system that means the retrieval query itself must be filtered by the requesting user's entitlements — not the answer, afterwards. Filtering after retrieval means the restricted content entered the model's context, and content in context is content that can leak through a summary, a paraphrase, or a follow-up question.

Then there is the reflex the exam guide's own sample question encodes, and it is worth stating flatly because it is the single most reliably rewarded instinct in this domain. **Least privilege means removing the capability. Logging it, confirming it, or restricting it to business hours are compensating controls wrapped around a privilege that should not exist.**

Compensating controls are not worthless. They are what you deploy when the privilege is genuinely required and you need to manage its risk. They are the wrong answer when the scenario states the capability is not needed. The exam distinguishes these two cases cleanly, and the tell is in the scenario prose: if it says the agent does not need the capability, remove it.

### Worked example

An HR assistant serves 4,000 employees. It retrieves from a document store containing three tiers of content: general policy (all staff), manager guidance (people managers, roughly 400 users), and compensation planning documents (HR business partners, 12 users).

The initial build uses one service account with read access across all three tiers, because that was the fastest path to a working demo. Retrieval is a vector search across the whole index, and a post-retrieval step drops chunks whose metadata says the user is not entitled to them.

Three gaps, in increasing severity.

**One.** The post-retrieval filter runs after the chunks are selected. If a compensation document is the top match, the filter drops it and the answer degrades to whatever ranked fourth and fifth — the user gets a worse answer with no indication why. That is a quality bug caused by a security control in the wrong place.

**Two.** The filter is application code. Any path that reaches the index without going through that code — a debugging endpoint, a batch summarization job, a new feature written by someone who did not know the filter existed — has no authorization at all. Enforcement that lives in one code path is enforcement that will eventually be bypassed.

**Three.** Traces and logs capture retrieved context. The retrieved context includes chunks that were subsequently filtered. The observability system now holds compensation data that its own access controls were never designed for.

The correct design pushes authorization down to the query. The user's identity propagates from the edge to the retrieval layer. The vector search executes with an entitlement filter as part of the query, so restricted chunks are never candidates. Nothing the user may not see is ever ranked, retrieved, placed in context, or written to a trace.

If the store cannot filter at query time, the correct answer is separate indexes per entitlement tier — three indexes, routed by the caller's tier. That is more infrastructure, and it is the right trade when the alternative is enforcement in application code.

### How the exam probes it

Two shapes recur.

The first is the **unneeded capability**. An agent has a tool or permission the scenario states it does not require. The options offer removal, logging, a confirmation step, and a time-window restriction. Remove it.

The second is the **identity gap**. A multi-user system where the agent reaches a data source under a shared credential. The question asks what the security gap is, or how to close it. The answer involves propagating the requesting user's identity and enforcing entitlement at the data layer, not at the response layer.

Expect the compliance dimension to be named: a regulated sector, an audit requirement, a data-residency constraint. When it is, the answer that satisfies the auditor is the one where enforcement is provable at the point of access, not asserted in application logic.

### Wrong turns and why they tempt

**Log the privileged action instead of removing the privilege.** Tempting because logging is unambiguously good practice and appears in every security checklist. Logging tells you afterwards that something you did not want happened. It does not prevent it. This is the official sample question's own designated wrong answer.

**Add a human confirmation step.** Tempting because human-in-the-loop is a legitimate and heavily-tested pattern elsewhere (Domain 5). Confirmation is the right control for an action that is *needed but consequential*. It is the wrong control for an action that is not needed at all, and it taxes every legitimate interaction to defend against one illegitimate one.

**Restrict the capability to business hours.** Tempting because it sounds like a real, enforced, technical control rather than a soft one. It narrows a window without narrowing a privilege, and it produces the odd security posture where the thing you did not want is fine at 2pm.

**Filter results after retrieval.** Tempting because it works in the demo and is a small code change. It admits restricted content into context and into traces, and the enforcement lives in exactly one code path.

**Put the authorization rule in the system prompt.** Tempting because it is fast and reads clearly. A prompt instruction is probabilistic. Security controls need to be deterministic, and a control that fails 1% of the time on 40,000 daily requests fails 400 times a day.

### Takeaways

- Authentication is identity; authorization is entitlement. LLM integrations lose the second one at the tool boundary by default.
- If the scenario says a capability is not needed, remove it. Logging, confirming, and time-boxing are controls for privileges you are keeping.
- Enforce entitlement in the query, not in the post-processing. Content that entered context has already leaked into traces.
- Prompt-level rules are probabilistic. Security enforcement must be deterministic.
- Observability systems inherit the sensitivity of whatever they capture. Design their access controls at the same time as the pipeline's.

---

## Objective 3 — Evaluate accuracy–latency trade-offs and justify configuration decisions

### The concept from first principles

Accuracy and latency are both budgets, and almost every mechanism that buys accuracy spends latency. A larger model, more retrieved chunks, a reranking pass, an extended reasoning cue, a self-critique step, a second retrieval hop — each of these has a defensible accuracy story and a measurable time cost.

The Professional-tier skill is not knowing that the trade-off exists. It is converting the argument into arithmetic. An architect who says "we should use the faster model" is having an opinion. An architect who says "our p95 budget is 3,000ms, generation currently consumes 1,900ms of it, and the reranking pass we are proposing costs 300ms for a 4-point recall gain, leaving 260ms of slack" is making a decision that can be defended to a stakeholder and revisited when the SLA changes.

Two disciplines make that arithmetic honest.

**Budget the tail, not the mean.** SLAs are written at p95 or p99 because that is where users actually experience the system. Mean latency improvements that do not move the tail are invisible to the people complaining.

**Distinguish total latency from perceived latency.** Streaming changes time-to-first-token dramatically and total time not at all. For an interactive chat surface that is a genuine and large win. For a downstream service that consumes the complete response before doing anything, it is worth nothing. The exam will tell you which consumer you have, in the scenario prose, and it is easy to miss.

There is one configuration that improves accuracy-adjacent cost and latency simultaneously rather than trading them, and it is verified from the exam guide's own sample questions: **when a large identical block of content is sent on every request, order the static content first and enable prompt caching.** A stable prefix is reused, which cuts both time-to-first-token and cost. Whenever a scenario names latency *and* cost together with an unchanging preamble, this is the move.

### Worked example

A document-triage assistant has a contractual p95 of 3,000ms end to end. Current measured breakdown at p95:

| Stage | p95 (ms) |
|---|---|
| Edge, auth, identity propagation | 120 |
| Query embedding | 180 |
| Vector search (top-20) | 240 |
| Cross-encoder rerank (20 → 5) | 300 |
| Generation | 1,900 |
| Response assembly | 60 |
| **Total** | **2,800** |

Slack: 200ms. Quality is at 91% on the eval set; the business wants 95%.

Three proposals arrive.

*Add a self-critique pass.* Measured cost, ~1,400ms. Accuracy gain on the eval set, +3 points. Total becomes 4,200ms. It blows the SLA by 40%. Not viable without renegotiating the SLA — which is a legitimate outcome, and a Domain 6 conversation.

*Move to a higher-capability model for generation.* Generation p95 rises from 1,900ms to 2,600ms; total 3,500ms. Also over. Unless something else is cut.

*Retrieve more and rerank harder.* Top-50 instead of top-20 costs 90ms more in search and 210ms more in rerank. Total 3,100ms. Marginally over, +1.5 accuracy points.

The productive move is to find the latency to spend. The static system preamble is 3,100 tokens and identical on every request; it currently sits after the retrieved chunks. Reordering it to the front and enabling prompt caching cuts time-to-first-token measurably and reduces per-request cost. That freed budget is what pays for the higher-capability model, and the resulting configuration lands inside the SLA with a real accuracy gain.

The general shape: before buying accuracy, look for the latency you are currently wasting.

### How the exam probes it

The scenario names an SLA, or a latency complaint, or a cost figure — often two of the three. It then presents configuration options with different accuracy and latency profiles. The correct answer is the one that satisfies the *stated* requirement, which is frequently not the most accurate option available.

This is where the ARCHITECTED distractor family does its worst damage. The most thorough-sounding option — add validation, add a critique pass, add a second retrieval hop — is often correct-looking and requirement-violating. Read the requirement, then check each option against it.

When latency and cost are both named alongside a large repeated block of content, order static content first and enable caching.

### Wrong turns and why they tempt

**Optimize the mean when the SLA names the tail.** Tempting because mean latency is the number most dashboards show by default. A change that cuts the mean by 200ms and leaves p95 untouched has not addressed the complaint.

**Treat streaming as a latency fix for a non-interactive consumer.** Tempting because streaming genuinely is the highest-leverage perceived-latency fix in interactive products. For a batch or service-to-service consumer, total time is unchanged.

**Buy accuracy nobody asked for.** OVERSPEC in its purest form. The scenario says 95%; the option delivers 98% at triple the latency. Extra accuracy purchased outside a requirement is unpriced cost.

**Cut the retrieved context to hit the budget.** Tempting because it is the fastest lever and reduces both cost and time. It usually costs more accuracy than the equivalent time saved elsewhere, and it is a DISCARD move — removing a working mechanism rather than tuning it.

**Cache the model's outputs to reduce latency.** Prompt caching reuses a stable input prefix, not the output. Response caching is a different mechanism with different correctness conditions, and conflating them produces answers that are wrong about how the saving is achieved.

### Takeaways

- Convert the trade-off into a budget table with measured stage timings. Argue from arithmetic.
- Budget at p95 or p99, matching the SLA's own wording.
- Streaming moves perceived latency for interactive consumers only.
- Latency and cost named together with a large fixed preamble: static content first, prompt caching on.
- Find wasted latency before buying accuracy. Reordering and caching often fund the upgrade.

---

## Objective 4 — Analyze observability challenges and select monitoring strategies at scale

### The concept from first principles

In a deterministic service, a failure and its cause are usually close together: a stack trace, a status code, a query plan. In an agentic system the final output is the *last* thing in a chain of decisions, and it rarely explains itself. A confidently wrong answer looks identical to a confidently right one at the response layer.

So the unit of observability is the **trace**, not the log line, and a useful trace captures the decision path:

- Which tools were called, with what arguments, in what order, and what each returned.
- What context was retrieved — the chunk identifiers, the document versions, the retrieval scores.
- The decision points: where the model chose between branches, where a guardrail fired, where a confidence threshold was or was not met.
- The correlation identifier that stitches the user request to every downstream call.

Capture only the final output and you can tell that something went wrong. You cannot tell whether the retrieval returned the wrong document, the right document was retrieved and misread, a tool returned stale data, or a guardrail suppressed the correct path.

"At scale" is in the objective's own wording, and it changes the design in three concrete ways.

**Volume.** Full-fidelity traces are large. At 200,000 requests per day and roughly 30KB per trace — prompt, retrieved chunks, tool arguments, tool results — that is about 6GB per day, 2.2TB per year, in a store you will be querying.

**Cardinality.** Metrics labelled with user identifiers, session identifiers, or document identifiers explode the label space and make the metrics backend expensive and slow. High-cardinality data belongs in traces and logs, which are queried on demand; metrics carry low-cardinality dimensions like tool name, model, tenant tier, and outcome class.

**Sensitivity.** Traces contain prompts, retrieved documents, and tool payloads. That is a second copy of your most sensitive data, in a system whose access controls were probably designed for engineers debugging outages. Retention, redaction, and access control on the trace store are part of the integration design, not an afterthought for the platform team.

The strategy that reconciles all three is **stratified sampling**, not uniform sampling.

### Worked example

A claims assistant at 200,000 requests/day. Uniform 100% capture is 6GB/day and puts regulated claimant data into the observability store indefinitely. Uniform 1% sampling is 60MB/day and captures roughly 20 of the day's 2,000 escalations — nowhere near enough to characterize failure.

Stratified policy:

| Stratum | Sample rate | Rationale |
|---|---|---|
| Requests ending in error or exception | 100% | Rare and maximally informative |
| Requests escalated to a human | 100% | The system's own admission of difficulty |
| Requests where model confidence fell below threshold | 100% | Leading indicator of quality drift |
| Requests touching regulated claim data | 100% metadata, redacted payload | Audit requires the fact of access; the audit does not require the content |
| Successful routine requests | 2% | Enough for baseline distributions and regression detection |

Result: roughly 5–7% of requests fully traced, about 350MB/day, with every high-information event captured. Retention split by stratum — 90 days for routine samples, longer for audit-stratum metadata under whatever the regulation requires.

Alongside this, low-cardinality metrics computed on 100% of traffic: request count, latency percentiles, tool-call counts by tool name, retrieval hit rate, escalation rate, guardrail-trigger rate, cost per request. Metrics tell you *that* something moved. Traces tell you *why*, for the sampled subset.

The alerting layer sits on the metrics. A useful early-warning set for a RAG-backed agent: retrieval hit rate below baseline, mean retrieval score dropping, escalation rate rising, tool error rate by tool, and p95 latency by stage rather than end-to-end only. Stage-level latency is what turns "the system got slow" into "the reranker got slow."

### How the exam probes it

The scenario describes a production system exhibiting intermittent or unexplained quality problems, with a team that can only see inputs and final outputs. Or it describes an observability proposal with a stated volume or cost problem. The question asks what to monitor, or what the monitoring gap is.

The correct answers cluster around: capture the decision path, not just the outcome; sample by stratum rather than uniformly; instrument stages, not just totals; and treat the trace store as a system holding sensitive data.

Expect the cost dimension to be explicit at Professional tier — a figure for storage, or a statement that full capture is not affordable.

### Wrong turns and why they tempt

**Log inputs and final outputs, at 100%.** Tempting because it feels complete, and because it is what most API gateways give you for free. It is the highest-volume, lowest-information capture available: it tells you what happened and nothing about why.

**Turn on full-fidelity tracing everywhere and deal with cost later.** Tempting because it is the option that definitely does not miss anything. At the volumes these scenarios name, it is not affordable, and it creates a data-protection liability the scenario often hints at.

**Sample uniformly at a low rate.** Tempting because it is the textbook answer to a volume problem, and it is genuinely correct for high-volume homogeneous traffic. It is wrong here because failures are rare and are exactly what you need. Uniform sampling is calibrated to the common case; you are hunting the rare one.

**Rely on user reports to identify quality problems.** Tempting because it is zero-cost and users do complain. Confidently wrong answers are the failure mode users are least likely to report, because they do not know the answer was wrong.

**Add user IDs as a metric label so you can slice by user.** Tempting because per-user slicing is a real operational need. It is a cardinality bomb; the need is served by traces, which are queried on demand.

### Takeaways

- Trace the decision path — tool calls, retrieved context with document versions, decision points — not the final output alone.
- Correlate everything to one request identifier, end to end.
- Sample by stratum: 100% of errors, escalations, and low-confidence paths; a small percentage of routine successes.
- Metrics carry low-cardinality dimensions; high-cardinality data belongs in traces.
- Instrument per stage so latency and quality regressions are attributable.
- The trace store holds a second copy of your sensitive data. Design its retention and access controls with the pipeline.

---

## Objective 5 — Design a RAG pipeline with appropriate chunking and indexing strategies

### The concept from first principles

Retrieval-augmented generation exists because model weights hold general knowledge and your organization's specifics live somewhere else, change on their own schedule, and carry access rules. RAG is the pipeline that pulls the right specifics into context at request time.

The pipeline has five stages, and failures are almost always attributable to one of them: ingestion, chunking, embedding, indexing, retrieval. Diagnosing RAG means asking which stage.

**Chunking** is the stage architects most often under-think. A chunk is the retrieval unit. The working definition worth memorizing: *a chunk is the smallest span of the document that still makes sense when read completely out of context.* That definition does most of the work.

It immediately rules out fixed-size splitting as a universal default, because a fixed 512-token window cuts wherever 512 tokens happens to land — mid-clause, mid-table, mid-function. It also explains why chunk boundaries should follow **document structure**: clause boundaries in a policy manual, endpoint boundaries in an API reference, ticket boundaries in a support archive. The structure a human author imposed is a map of where the semantic seams are.

Two refinements make structural chunking work in practice.

*Overlap.* A small overlap, typically 10–15%, protects against a key sentence straddling a boundary. Overlap is insurance against imperfect boundaries, not a substitute for choosing good ones.

*Contextualization.* A chunk taken from the middle of a long document loses everything the document title and heading hierarchy conveyed. "This limit does not apply to renewals" is meaningless standalone. Prepending the document title and heading path to the chunk text before embedding puts that context into the vector, not merely into the metadata. This is one of the highest-return, least-glamorous changes available in a RAG pipeline.

**Indexing** is the stage that produces the failure mode the exam guide's own sample question tests. An index is a coupled unit of three things: the chunking scheme that produced the chunks, the embedding model that vectorized them, and the vector store holding the result. Change any one of the three without the others and the space becomes inconsistent. Vectors from a different embedding model land in a different geometry; similarity scores between them are arithmetic without meaning. The system does not error. It returns confident nonsense.

Which is why: **a RAG system that starts returning confident-but-wrong answers immediately after a document refresh is a retrieval and indexing problem.** Not the model, not the prompt, not the sampling temperature. The correlation with the refresh is the whole clue. Look for a re-index that partially failed, a chunking change shipped alongside the refresh, an embedding model version that moved, or stale vectors left behind for deleted documents.

### Worked example

An insurance operations knowledge base with four content types. One chunking strategy would be wrong for at least three of them.

**Policy manuals** — 40 to 200 pages, numbered clauses, deep heading hierarchy. Chunk on clause boundaries, typically 200–600 tokens. Prepend the full heading path and clause number to the chunk text before embedding. Metadata: policy ID, effective date, jurisdiction, clause number. That metadata is what lets a query filter to the version in force on the claim's date — a correctness requirement, not a nicety.

**API reference for the claims system** — highly regular, one section per endpoint. Chunk per endpoint, whole. Splitting an endpoint's parameters away from its description produces two chunks that are both useless.

**Support ticket archive** — threads of 3 to 40 messages. Chunk per *ticket*, not per message. A single message ("try clearing the cache") is unanswerable without the problem statement above it and the outcome below it. Long tickets get summarized-plus-full-thread treatment rather than mechanical splitting.

**Product specification tables** — 12,000 rows, 40 columns, in a relational store. Do not embed this at all. Queries against it are filters and aggregations. Expose it as a structured query tool. Embedding a table row produces a vector that is mostly noise, and no amount of retrieval tuning fixes "how many products in category X exceed threshold Y."

Then the refresh incident. Six weeks after launch, a nightly reload of the policy manuals runs. The next morning the assistant answers coverage questions confidently and cites clause numbers that do not match the text quoted. Investigation order:

1. Did the re-index complete? Chunk count in the index versus expected count from the source. A 30% shortfall means a partial run.
2. Did the chunking configuration change with the refresh? Diff the chunk-schema version.
3. Did the embedding model version change? Compare the index's recorded model version against the query-time embedding model. A mismatch is the classic silent killer.
4. Were deleted or superseded documents removed from the index, or are stale vectors still ranking?
5. Only after those four: examine the prompt and the model.

In this example the cause is (3) — the ingestion job pulled a floating model version that moved. The fix pins the embedding model version to the index and re-embeds the whole corpus. The prevention is a post-index validation gate: a fixed set of golden queries with known-correct chunk IDs, run automatically after every re-index, blocking promotion if hit rate drops.

### How the exam probes it

Two shapes.

**Design shape:** a corpus is described with its structure named — clause-numbered, tabular, threaded, code — and the question asks for the chunking or indexing strategy. Match the boundary to the structure. Watch for the content type that should not be embedded at all.

**Diagnosis shape:** a working RAG system degrades, with a stated trigger. When the trigger is a document refresh, an ingestion change, or a pipeline deployment, the answer is in retrieval and indexing. The distractors will offer model, prompt, and temperature changes.

### Wrong turns and why they tempt

**Fixed-size chunks for every content type.** Tempting because it is simple, uniform, and what every tutorial demonstrates. It ignores the structure that tells you where the seams are, and it fails hardest on the structured content where retrieval matters most.

**Lower the temperature to stop the confident-wrong answers.** Tempting because "confidently wrong" sounds like a sampling problem and temperature is the parameter everyone reaches for. Temperature changes how the model selects tokens. It has nothing to say about which documents were retrieved.

**Swap in a more capable model.** Tempting because it is a single change with a plausible story and no engineering required. A better model reading the wrong document produces a more articulate wrong answer.

**Add "say you don't know if unsure" to the system prompt.** Tempting because it is a genuinely good guardrail. It suppresses a symptom of a broken index without repairing the index, and it degrades every correct answer's confidence along the way.

**Increase chunk size so more context fits.** Tempting because it looks like it addresses the "chunk lacks context" problem directly. Larger chunks dilute the embedding across more topics, which lowers retrieval precision. Contextualization — prepending the heading path — solves the context problem without the dilution.

### Takeaways

- A chunk is the smallest span that stands alone when read out of context. Let structure set the boundaries.
- Prepend document title and heading path to chunk text before embedding.
- Overlap of 10–15% is insurance against imperfect boundaries, not a chunking strategy.
- Chunking scheme, embedding model version, and index are one coupled unit. Version them together.
- Tabular and relational data is queried, not embedded.
- Degradation correlated with a document refresh points at retrieval and indexing first.
- Gate every re-index with golden queries that assert known-correct chunk IDs.

---

## Objective 6 — Apply retrieval strategies matched to data shape and query pattern

### The concept from first principles

"RAG" and "vector database" have become near-synonyms in casual usage, and that conflation is the source of most retrieval mistakes. Retrieval strategy is chosen on two axes.

**Data shape** — what the corpus actually is. Free prose. Structured records. Code. Tables. Entities with relationships. Time series.

**Query pattern** — what the user is actually asking the system to do. Look up a known identifier. Find semantically similar text. Filter by attribute. Aggregate across records. Traverse a relationship. Compare across a time range.

The mechanisms, and where each earns its place:

| Mechanism | Strong at | Weak at |
|---|---|---|
| Dense / vector | Paraphrase, conceptual similarity, "documents about X" | Exact tokens — part numbers, error codes, proper nouns, rare terms |
| Lexical / BM25 | Exact terms, identifiers, codes, rare vocabulary | Paraphrase; a query sharing no vocabulary with the answer |
| Hybrid (fused) | Corpora and query mixes that contain both of the above | Cost and complexity when only one form is present |
| Metadata filter + semantic | Scoping to a jurisdiction, tenant, date range, entitlement, then ranking within it | Nothing much — it is usually additive and underused |
| Structured query (SQL) | Aggregation, counting, filtering, joins, exact numerics | Anything requiring semantic understanding of prose |
| Graph traversal | Multi-hop relationship questions | Everything else; it is expensive to build and maintain |

The embedding weakness deserves emphasis because it is counter-intuitive and heavily tested. Embedding models compress meaning. A part number like `ERR_5521` carries almost no distributional meaning — it appears rarely, in few contexts, and its vector is close to other rare token sequences rather than to the document that explains it. Meanwhile every article about upgrade errors sits in a tight semantic cluster. Vector search on "why does ERR_5521 happen after upgrade" returns five thematically perfect articles, none of which mention `ERR_5521`. Lexical search returns the one document that does.

**Hybrid retrieval earns its place exactly when the corpus contains both natural-language explanation and exact identifiers, and users mix both query forms.** That condition is common in support, legal, medical, and engineering corpora, and it is not universal. Hybrid retrieval on a corpus of pure narrative prose queried in pure natural language adds a second index, a fusion step, and two sets of tuning parameters for no gain. It is OVERSPEC.

Two more strategies belong in the working set.

**Filter before you rank.** If a query is scoped — one tenant, one jurisdiction, one date range, one entitlement tier — apply the metadata filter as part of the query so semantic ranking happens within the eligible set. This is correctness for entitlement (see Objective 2) and precision for everything else.

**Retrieve wide, rerank narrow.** Vector search is fast and approximate; a cross-encoder reranker is slow and accurate. Retrieving the top 20–50 and reranking down to the top 3–5 buys most of the precision of an expensive search at most of the speed of a cheap one. The cost is a latency stage that must fit the budget from Objective 3.

### Worked example

A field-service assistant over three sources.

*Source A:* 8,000 troubleshooting articles, natural-language prose, containing error codes and part numbers inline.
*Source B:* a parts catalog, 45,000 rows, relational, with part number, compatibility, stock, and price.
*Source C:* an equipment hierarchy — models, sub-assemblies, compatible parts, superseded-by relationships.

Query types, from a week of real logs:

| Query | Shape | Strategy |
|---|---|---|
| "Compressor is short-cycling on a model 400" | Prose, conceptual | Dense over A, filtered on model=400 |
| "What does ERR_5521 mean" | Exact identifier | Lexical over A; dense alone misses it |
| "Is part 88-2210J still in stock" | Structured lookup | SQL against B; no retrieval involved |
| "How many model 400 units use a superseded compressor" | Aggregation over relationships | SQL against B joined to C |
| "What replaced the 88-2210J" | Relationship traversal | Graph or foreign-key traversal over C |
| "Why does the compressor fail after the ERR_5521 sequence" | Mixed prose + identifier | Hybrid over A — this is the case that justifies it |

One retrieval strategy across all six would be wrong four times. The design is a router that classifies query shape and dispatches to the appropriate mechanism, with hybrid reserved for source A where the mixed condition genuinely holds.

Measured: the last query type, on dense-only retrieval, had a hit rate of 34%. With hybrid fusion it was 89%. Those are the numbers that justify the added index to a stakeholder — not the phrase "hybrid retrieval is best practice."

### How the exam probes it

The scenario names the data shape and the query pattern in its prose, usually both, and the correct answer matches them. When the query contains exact identifiers, lexical or hybrid is in play. When the question is a count, a sum, or a filter, the answer is a structured query and not retrieval at all. When the question is multi-hop across relationships, traversal.

The scenario may also name a precision problem — "the right document exists but ranks eighth" — which points at reranking or at filtering before ranking, not at a different retrieval mechanism.

### Wrong turns and why they tempt

**Assume RAG means vector search.** Tempting because it is the default mental model and the default in most tooling. It fails on identifiers, aggregations, and relationship queries — three of the six query types above.

**Add hybrid retrieval everywhere.** Tempting because hybrid genuinely outperforms dense-only on mixed corpora, and "hybrid" reads as the more sophisticated answer. On a corpus without exact identifiers it is cost and complexity for no measurable gain. OVERSPEC.

**Build a knowledge graph for a lookup problem.** Tempting because graphs are the impressive answer and the scenario mentions relationships. Building and maintaining a graph is a large ongoing commitment; if the actual query is a single-hop foreign-key lookup, a join answers it.

**Increase top-k until the right document appears.** Tempting because it demonstrably improves recall and is a one-line change. It floods the context with lower-relevance chunks, raises cost and latency, and worsens the lost-in-the-middle problem. Reranking is the targeted version of the same intent.

**Embed the relational table so everything is in one index.** Tempting because a single retrieval path is architecturally cleaner. Row embeddings are mostly noise, and aggregation queries have no vector-space answer.

### Takeaways

- Choose retrieval on two axes: what the data is, and what the query does.
- Dense fails on exact identifiers. Lexical fails on paraphrase. That asymmetry is what hybrid exists to cover.
- Hybrid earns its place when the corpus and the query mix both forms — not by default.
- Aggregation, counting, and filtering are structured queries, not retrieval.
- Filter by metadata as part of the query, then rank within the eligible set.
- Retrieve wide, rerank narrow, and check the reranker against the latency budget.

---

## Objective 7 — Evaluate connection protocols and select the appropriate integration mechanism

### The concept from first principles

Three mechanisms, and the discriminator between them is a single question: **who decides what happens next?**

**Direct API or CLI call.** Your code decides. The sequence is known at design time, the call happens whether or not a model is involved, and the result is deterministic. Fetching a claim record before the conversation starts is this. It is the cheapest, fastest, and most testable option, and it is under-used because "the agent should decide" is a seductive default.

**MCP.** The model decides, within a surface you expose. The Model Context Protocol standardizes how a server offers three kinds of thing to a client: **tools** (actions the model can call), **resources** (read-only data it can access), and **prompts** (reusable templates). Tools from all configured servers are discovered at connection time. The architectural value is standardization — one server implementation is consumable by any MCP-capable client, rather than one bespoke integration per agent.

The reuse logic that follows from that: for **standard integrations** — issue trackers, source control, chat platforms — prefer an existing community server. Build custom servers for workflows genuinely unique to your organization. Building a bespoke server for a widely-integrated system spends engineering effort re-implementing a maintained standard.

**Agent-to-agent.** Another agent decides. You hand over a task rather than requesting data, and the other side brings its own context, its own tools, and its own judgment, returning a result rather than a payload. This is the right mechanism when the work requires reasoning your agent should not be doing — a specialist domain, a different data boundary, a separately-owned system with its own accountability.

The cost gradient runs in one direction. A direct API call is one network round-trip. An MCP tool call is a model decision plus a round-trip plus a result the model must then interpret. An agent-to-agent handoff is all of that plus a whole second inference loop with its own latency, cost, and failure modes. Each step up the gradient buys flexibility and spends determinism.

One more distinction that catches people: MCP **resources** versus MCP **tools**. A resource is read-only content the agent can look at — a catalog of what exists, a schema, a document hierarchy. A tool is an action it calls. Exposing a content catalog as a resource gives the agent a map without requiring it to spend model calls on exploratory queries. This is directly relevant to the next objective.

### Worked example

A claims-processing assistant integrating with five systems.

**Claims database — read the claim under discussion.** The claim ID is known from the request. There is no decision for the model to make. Direct API call in the request pre-processing, result placed in context. One round-trip, deterministic, testable, and it removes an entire class of "the agent forgot to look up the claim" failures.

**Policy document store — search when the agent needs a clause.** The agent decides whether and what to search, because that depends on the conversation. MCP tool. Alongside it, an MCP resource exposing the policy catalog — document titles, effective dates, jurisdictions — so the agent can see what exists without guessing at search queries.

**Fraud scoring service — obtain a risk score.** Deterministic input, deterministic output, called on every claim above a threshold. Direct API, invoked by the orchestration layer, not by the model. Exposing it as a tool would let the model choose not to call it, which is precisely wrong for a control that must always run.

**Issue tracker — file an escalation.** Standard system, widely integrated. Existing community MCP server, configured with per-user credential substitution so the escalation is filed as the operator, not as a shared service account. That last detail is Objective 2 showing up inside a protocol decision.

**Medical necessity review — interpret whether a treatment is covered under the plan's clinical criteria.** This requires clinical reasoning over a body of guidance the claims agent has no business holding, and the result must be attributable to the clinical review function for audit. Agent-to-agent: hand the case over, receive a determination with a rationale.

Five integrations, three mechanisms, and each choice traceable to who decides.

### How the exam probes it

The scenario describes an integration need and asks which mechanism fits. The tells:

- A fixed step that must always run, in a known sequence → direct API/CLI.
- The agent should choose whether and when, based on the conversation → MCP tool.
- The agent needs to know what exists before it can query → MCP resource.
- A standard third-party system → existing community server before a custom build.
- Work requiring judgment, separate context, or separate accountability → agent-to-agent.

Cost and latency are frequently the deciding constraint at Professional tier. If the scenario names a tight budget, the mechanism further down the gradient usually wins.

### Wrong turns and why they tempt

**Expose deterministic pipeline steps as tools so the agent can decide.** Tempting because it sounds more agentic and more flexible. It introduces non-determinism into a step that had none, adds a model decision's worth of latency and cost, and creates the possibility that a mandatory step is skipped.

**Build a custom MCP server for a standard integration.** Tempting because "for control" and "for our specific needs" are always sayable. It reimplements a maintained integration and inherits its maintenance forever.

**Reach for agent-to-agent when a tool call would do.** Tempting because multi-agent architecture is the impressive answer and the exam does test it elsewhere. If the other side is not exercising judgment, you have paid for an inference loop to perform a function call.

**Paste the catalog into the system prompt instead of exposing a resource.** Tempting because it removes a round-trip. It bloats every request with content that is stale the moment the catalog changes.

**Add a `list_everything` tool rather than a resource.** A HALF-MOVE. It gives the agent a way to see the map but requires the agent to remember to call it, and it spends a model turn on something a resource provides as readable context.

### Takeaways

- The discriminator is who decides: your code, the model, or another agent.
- Direct API/CLI for known, mandatory, deterministic steps. It is faster, cheaper, and more testable.
- MCP when the model should choose. Tools are actions; resources are read-only content the model can consult.
- Community servers for standard integrations; custom servers for genuinely unique workflows.
- Agent-to-agent only when the other side brings judgment, context, or accountability you do not have.
- The cost gradient runs API → MCP → agent-to-agent. Justify each step up.

---

## Objective 8 — Evaluate progressive discovery vs. monolithic context strategy

### The concept from first principles

Monolithic context means loading the whole surface up front: every tool definition, every schema, the full document catalog, all of it in the request. Progressive discovery means loading a compact map and fetching detail on demand.

Three forces push toward progressive discovery as the surface grows.

**Token cost is paid on every request.** A monolithic surface of 12,000 tokens is 12,000 tokens whether the request uses one tool or none. Progressive discovery pays a small base plus the cost of what was actually needed.

**Discrimination degrades with surface size.** This is Objective 1's argument, applied to context rather than to tool count specifically. A model choosing among 8 namespaces then 6 tools within one namespace is solving two small problems instead of one large one.

**Long context has an attention gradient.** Content at the beginning and end of a long input is attended to more reliably than content in the middle. A monolithic surface guarantees that most of it sits in the penalized middle.

Progressive discovery is not free, and the Professional-tier skill is naming its cost honestly. It adds a **round-trip** — one extra model turn to expand a namespace — which is real latency on the requests that need it. And it adds a **discovery failure mode**: the agent may fail to find a capability that exists, because the index entry did not make clear that it was there. A monolithic surface at least guarantees visibility.

Which yields the conditions under which monolithic is correct:

- The surface is **small and stable** — five tools, not sixty. A progressive layer over five tools is overhead with no offsetting saving.
- The latency budget **cannot absorb a discovery round-trip**, and the surface fits.
- The content is needed on **literally every request**. Then it belongs in the request — and, being identical every time, it should be ordered first and served from a cached prefix, which is where this objective meets Objective 3.

The mitigations for progressive discovery's failure mode are worth knowing because they show up as correct answers. Write namespace-level index entries as a genuine map — what lives here, when you would come here — rather than a bare list of names. And **promote high-frequency capabilities into the base surface**, so the common path never pays the round-trip and only the long tail does.

### Worked example

An enterprise agent with access to 60 tools across 8 systems. Tool definitions average roughly 200 tokens.

*Monolithic.* 60 × 200 = 12,000 tokens of tool definitions on every request. At 50,000 requests/day that is 600 million tokens per day of tool surface. Trace analysis shows the median request calls 1.4 tools and touches exactly one system.

*Progressive.* Expose 8 namespace entries, each a 150-token description of what that system covers and when to reach for it: 1,200 tokens base. The agent selects a namespace; a discovery step returns that namespace's tool definitions, averaging 7.5 tools, about 1,500 tokens. Typical request total: ~2,700 tokens of surface, plus one extra round-trip costing roughly 250ms on the requests that require expansion.

Saving: about 9,300 tokens per request, roughly 465 million tokens per day. Cost: 250ms of added latency on the subset of requests needing expansion, and a new risk that the agent picks the wrong namespace.

*Refinement.* Trace analysis shows six tools account for 61% of all calls. Promote those six into the base surface: base becomes 1,200 + 1,200 = 2,400 tokens, 61% of requests need no expansion at all, and the median request now costs less in both tokens and latency than either pure strategy.

That refinement is the shape of a good Professional-tier answer: not one strategy or the other, but a hybrid justified by measured call distribution.

The same reasoning applies to knowledge, not only tools. A document catalog exposed as a readable resource is the progressive-discovery pattern for content: the agent gets the map — what documents exist, what they cover, when they were updated — and fetches the territory only when it decides it needs to. Dumping the catalog into the system prompt is the monolithic version, and it goes stale between deployments.

### How the exam probes it

The scenario names a large surface and at least one of: a token cost, a latency figure, a misrouting rate. It asks how to restructure. The correct answer usually introduces a discovery layer or promotes a subset, and the justification is the measured usage distribution.

The inverse also appears, and it is the direction people drill less. A small, stable surface with a tight latency budget, where someone proposes a discovery mechanism. The correct answer rejects it: the round-trip costs more than the surface does.

Look for content that is identical on every request. That is a caching answer, not a discovery answer.

### Wrong turns and why they tempt

**Load everything, because the agent might need it.** Tempting because it is the option that cannot fail to expose a capability. It pays maximum cost on every request and degrades selection accuracy across the board.

**Apply progressive discovery to a small surface.** Tempting because progressive discovery is the more sophisticated pattern and reads as the better answer. Below roughly ten tools the round-trip costs more than the tokens saved.

**Paste the full catalog into the system prompt.** Tempting because it is the fastest implementation of "give the agent visibility." It is monolithic context with a staleness problem attached.

**Add a discovery tool the agent must remember to call first.** HALF-MOVE. It provides the map but makes access to the map probabilistic, and spends a model turn on it. Readable content the agent can consult is the stronger form.

**Cut tools to shrink the surface when they are all genuinely needed.** DISCARD. When the capabilities are required, the answer is to restructure how they are presented, not to remove them.

### Takeaways

- Monolithic pays full token cost on every request; progressive pays a base plus what was used.
- Progressive discovery costs a round-trip and introduces a discovery failure mode. Name both.
- Monolithic is correct for small, stable surfaces, tight latency budgets, and content needed on every request.
- Content needed on every request should be ordered first and cached, not discovered.
- Promote high-frequency capabilities into the base surface. Measured call distribution is the justification.
- Index entries must be a usable map, not a list of names.

---

## Synthesis — the eight objectives in one design

A regional insurer builds a claims assistant for 900 adjusters. Volume: 180,000 requests/day. Contractual p95: 3,000ms. Regulated: claim content is protected data with a seven-year audit requirement. Watch all eight objectives land on one system.

**Protocol selection (7).** The claim record is fetched by direct API in pre-processing, since the claim ID is known and the lookup is mandatory. The policy document store is exposed as an MCP tool with a companion resource carrying the policy catalog. The fraud scorer is a direct API call from the orchestration layer, never a tool, because it must run on every claim above threshold and the model must not be able to skip it. Escalations are filed through an existing community MCP server for the issue tracker. Medical necessity review is agent-to-agent, because the determination must be attributable to the clinical function.

**Capability bloat (1).** The first design gave the adjuster agent all 19 available tools. Trace analysis found an 8% misroute rate concentrated between three near-duplicate pairs. The agent is split into three role-scoped agents of 4–6 tools each. One narrowly scoped cross-role tool survives the split: the claims agent keeps a read-only `check_policy_status` because it needs it on nearly every turn and the coordinator round-trip was the dominant latency cost.

**Progressive discovery (8).** Across the three agents plus their sub-systems the total surface is 34 tools. Namespace-level discovery over 5 namespaces plus promotion of the 7 tools accounting for 64% of calls. Base surface: ~2,150 tokens against 6,800 monolithic.

**Auth and authz (2).** The adjuster's identity propagates from the edge to every data access. The policy store's retrieval query carries an entitlement filter, so documents outside the adjuster's line of business are never candidates. The issue-tracker server uses per-user credential substitution. During review, the agent was found to hold a `update_claim_status` tool that no workflow used; it was removed rather than logged, confirmed, or restricted by hour.

**RAG chunking and indexing (5).** Policy manuals chunked on clause boundaries with heading path prepended; effective date and jurisdiction in metadata so the retrieval filters to the version in force on the claim date. The claims-history table is not embedded; it is queried. Embedding model version is pinned to the index. Every re-index runs 40 golden queries with known chunk IDs and blocks promotion if hit rate falls below baseline.

**Retrieval strategy (6).** Hybrid over the policy corpus, because adjusters query in prose and in clause numbers within the same conversation. Metadata filter applied before ranking. Top-30 retrieved, reranked to top-4. Claims-history questions dispatch to SQL. Superseded-policy chains traverse foreign keys.

**Accuracy–latency (3).** Budget table: 120ms edge and identity, 180ms embedding, 240ms hybrid search, 300ms rerank, 1,850ms generation, 60ms assembly — 2,750ms, 250ms slack. The 3,400-token static preamble was moved to the front of the request and prompt caching enabled, which funded the reranking stage that would otherwise not have fit. Streaming is enabled for the adjuster-facing surface and irrelevant to the batch triage path that consumes complete responses.

**Observability (4).** Correlation ID from edge to every tool call and retrieval. Stratified capture: 100% of errors, escalations, low-confidence paths, and clinical-review handoffs; 2% of routine successes; 100% metadata with redacted payload for every request touching protected claim content, retained to satisfy the seven-year audit. Metrics at 100% with low-cardinality dimensions: latency by stage, retrieval hit rate, mean retrieval score, tool error rate by tool, escalation rate, cost per request. Alerting on retrieval hit rate and mean retrieval score is what would have caught the embedding-version drift in Objective 5's worked example within an hour instead of a morning.

The interlock is the point. The caching decision from Objective 3 funded the reranker from Objective 6. The entitlement filter from Objective 2 is implemented in the retrieval query from Objective 6 and constrains what Objective 4 is permitted to store. The tool split from Objective 1 changed the surface that Objective 8's discovery layer had to cover. Integration decisions are not independent, and the exam's harder items are built on exactly that dependency.

---

## Misconceptions

| Misconception | Correction |
|---|---|
| "Least privilege means monitoring what the agent does with its permissions." | Least privilege means the permission does not exist. Logging, confirmation, and time-windows are controls for privileges you are keeping. |
| "More tools give the agent more flexibility, which can only help." | Every tool costs tokens on every request, adds a confusable neighbour to the selection problem, and enlarges the blast radius. |
| "Better tool descriptions fix misrouting." | They help, and they do not reduce the decision space, the token tax, or the privilege surface. Scope first, then describe. |
| "The agent's service account is fine because the app checks permissions." | A check in one code path is bypassed by the next code path. Enforce entitlement in the data query itself. |
| "Filtering restricted content out of the answer protects it." | Content that reached the context has already reached the trace store and can surface through a paraphrase. Filter before retrieval, not after. |
| "Confident-but-wrong answers mean the temperature is too high." | Temperature governs token selection. When degradation follows a document refresh, the cause is in retrieval and indexing. |
| "A more capable model will fix the RAG quality problem." | A better model reading the wrong document produces a more articulate wrong answer. |
| "512-token chunks are a reasonable default for any corpus." | Chunk boundaries should follow document structure. A chunk is the smallest span that stands alone out of context. |
| "Bigger chunks give the model more context, so retrieval improves." | Larger chunks dilute the embedding across more topics and lower precision. Prepend the heading path instead. |
| "RAG means a vector database." | Vector search is one mechanism. Identifiers want lexical, aggregations want SQL, relationships want traversal. |
| "Hybrid retrieval is best practice, so use it everywhere." | Hybrid earns its place when the corpus and the queries mix prose and exact identifiers. Otherwise it is two indexes for no gain. |
| "Raising top-k until the right document appears is a fix." | It floods context, raises cost and latency, and worsens the attention gradient. Rerank instead. |
| "Logging inputs and outputs gives us observability." | That records what happened, not why. The unit of observability is a trace of tool calls, retrieved context, and decision points. |
| "We sample 1% of traffic, so we have monitoring coverage." | Uniform sampling is calibrated to the common case. Failures are rare, so capture 100% of errors, escalations, and low-confidence paths. |
| "Prompt caching stores the response so repeat questions are instant." | It reuses a stable input prefix. The static content must be identical and ordered first, every time. |
| "Streaming makes the system faster." | It changes time-to-first-token for interactive consumers. Total latency is unchanged, and a batch consumer sees no benefit. |
| "Anything the agent might call should be an MCP tool." | A mandatory deterministic step should be a direct API call. Making it a tool lets the model skip it. |
| "Agent-to-agent is the modern way to connect systems." | It costs a full second inference loop. Use it when the other side brings judgment, context, or accountability you do not have. |
| "Progressive discovery is always better than loading everything." | Below roughly ten tools the discovery round-trip costs more than the tokens saved. |
| "Give the agent a tool that lists everything available." | That makes access to the map probabilistic and spends a model turn. Readable content the agent can consult is stronger. |

---

## Quick reference

**Capability bloat.** Cut the surface before improving descriptions. Narrow tool beats broad tool plus instruction. Role-scoped agents; one exception for a scoped cross-role tool serving a high-frequency need.

**Auth and authz.** Authentication is who; authorization is what. Propagate identity to the data layer. If the capability is not needed, remove it — do not log, confirm, or time-box it. Enforce in the query, deterministically.

**Accuracy–latency.** Build a stage-level budget table at p95. Streaming is perceived latency for interactive consumers only. Latency plus cost plus a fixed preamble: static content first, prompt caching on. Find wasted latency before buying accuracy.

**Observability.** Trace the decision path, not the output. One correlation ID end to end. Stratified sampling: 100% of errors, escalations, and low-confidence; a few percent of routine. Low-cardinality metrics, high-cardinality traces. The trace store holds sensitive data.

**RAG chunking and indexing.** A chunk stands alone out of context. Structure sets the boundary. Prepend heading path before embedding. 10–15% overlap is insurance, not strategy. Chunking scheme, embedding version, and index are one unit. Degradation after a refresh means retrieval and indexing. Gate re-indexes with golden queries.

**Retrieval strategy.** Two axes: data shape, query pattern. Dense fails identifiers; lexical fails paraphrase; hybrid covers both when both are present. Aggregation is SQL. Filter before ranking. Retrieve wide, rerank narrow.

**Connection protocols.** Who decides — your code, the model, or another agent. Direct API for mandatory deterministic steps. MCP tools for model-chosen actions, MCP resources for read-only maps. Community servers for standard integrations. Agent-to-agent for delegated judgment. Cost rises API → MCP → agent-to-agent.

**Progressive vs monolithic.** Monolithic pays full cost every request; progressive pays a base plus a round-trip. Monolithic wins on small stable surfaces and tight latency budgets. Promote high-frequency capabilities into the base. Content needed every request gets cached, not discovered.

**The spine.** Every objective in this domain is an admission-control decision. What enters the context, what the agent can reach, what that costs in time, and what record survives the transaction.
