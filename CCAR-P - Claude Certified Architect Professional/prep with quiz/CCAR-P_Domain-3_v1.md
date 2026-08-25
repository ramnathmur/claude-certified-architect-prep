# Domain 3 — Integration

**Weight:** 19% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Evaluate tool/agent configuration for capability bloat · Analyze authentication and authorization requirements to identify security gaps · Evaluate accuracy-latency trade-offs and justify configuration decisions · Analyze observability challenges and select monitoring strategies at scale · Design a RAG pipeline with appropriate chunking and indexing strategies · Apply retrieval strategies matched to data shape and query pattern · Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent) · Evaluate progressive discovery vs. monolithic context strategy

---

## 3.1 Tool Surface Sizing & Capability Bloat

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Evaluate tool/agent configuration for capability bloat |
| Discriminator | Is the failure caused by the size of the decision space, or by the quality of individual descriptions? |
| Three costs of a tool | Tokens on every request · discrimination difficulty on every turn · blast radius when misused |
| Cost dimension | Tool definitions are a fixed per-request tax paid whether the tool is called or not |
| Failure mode at volume | Misroutes concentrate in near-duplicate tool pairs; error rate rises faster than tool count |
| Sanctioned exception | A narrowly scoped cross-role tool for a genuine high-frequency need; complex cases still route via the coordinator |

### Decision Axis — Reduce the Decision Space vs Improve the Descriptions

Cut the number of candidate tools first; sharpen descriptions only for the confusable pairs that survive the cut.

| Situation | Answer | Why |
|---|---|---|
| One agent holds 20+ tools spanning several unrelated roles, misrouting between near-duplicates | Split into role-scoped agents of 4–6 tools each | Moves confusable pairs into different agents; the discrimination problem disappears rather than being mitigated |
| Two tools in the same scoped agent are still confused | Expand both descriptions with input formats, boundaries, and when-not-to-use | Descriptions are the primary selection lever once the decision space is already small |
| A generic tool (`fetch_url`) is being used outside its intended scope | Replace it with a constrained tool that validates its own inputs | Enforces the boundary at the interface, not probabilistically in a prompt |
| A scoped agent needs one simple cross-role lookup on nearly every turn | Give it a narrowly scoped cross-role tool | Coordinator round-trips on a high-frequency need cost more than the scoping buys |
| A stakeholder asks to keep all tools available "for flexibility" | Push back with the per-request token cost and the measured misroute rate | Flexibility on a tool surface is indistinguishable from ambiguity |

### Exam scenario: an agent with 22 tools misroutes 11% of requests touching three near-duplicate tool pairs

- ✅ Split the agent into role-scoped agents so each request sees only the 4–6 tools its role uses, then tighten descriptions on any pair still confusable inside one agent
- ❌ Write more detailed descriptions for all 22 tools — **HALF-MOVE**: improves discrimination without shrinking the decision space, the token tax, or the privilege surface
- ❌ Put a routing classifier in front of the agent — **ARCHITECTED**: sounds like proper separation of concerns, but adds a component, a hop, and a failure mode to compensate for a configuration problem that scoping solves outright

### ❌ Misconception
"More tools give the agent more flexibility, so extra tools can only help." — Every tool costs tokens on every request, adds a confusable neighbour to the selection problem, and enlarges the blast radius when the agent is pushed off-script.

---

## 3.2 Least Privilege — Removal vs Compensating Control

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Analyze authentication and authorization requirements to identify security gaps |
| Rule | Least privilege means the capability does not exist |
| Compensating controls | Logging · confirmation prompts · time-window restrictions · rate limits |
| When compensating controls are correct | The privilege is genuinely required and its risk must be managed |
| When they are wrong | The scenario states the capability is not needed |
| Source | Official exam guide v1.0, §8 sample question — VERIFIED |

### Decision Axis — Is the Capability Needed?

If the scenario says the agent does not need the capability, remove it; every other control is wrapped around a privilege you are choosing to keep.

| Situation | Answer | Why |
|---|---|---|
| Agent holds a write/delete capability no workflow uses | Remove it from the tool set | The privilege is the gap; nothing else closes it |
| Agent needs a consequential capability that a workflow genuinely requires | Keep it and add human confirmation and audit logging | Confirmation is the right control for needed-but-consequential actions |
| Agent needs a capability only for a specific narrow case | Replace the broad capability with a narrow one scoped to that case | Narrowing the privilege beats gating the broad one |
| Compliance requires proof of who did what | Audit logging, in addition to removal of unneeded privileges | Logging is an audit requirement, not a substitute for scoping |

### Exam scenario: an agent has a capability the scenario states it does not require

- ✅ Remove the capability from the agent's configuration
- ❌ Keep it and log every use for audit review — **HALF-MOVE**: logging records afterwards that the unwanted thing happened; it never prevents it
- ❌ Keep it but restrict it to business hours — **WRONG-AXIS**: narrows a time window rather than a privilege, producing a posture where the unwanted action is acceptable at 2pm

### ❌ Misconception
"Least privilege means monitoring closely what the agent does with its permissions." — Least privilege means the permission is not there; logging, confirmation, and time-boxing are controls for privileges you have decided to keep.

---

## 3.3 Authorization Enforcement Point & Identity Propagation

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Analyze authentication and authorization requirements to identify security gaps |
| Authentication | Establishes who is calling |
| Authorization | Establishes what that caller may reach |
| Default gap | The agent calls tools under its own service credential; the user's entitlements are stripped at the tool boundary |
| Discriminator | Is entitlement enforced in the query, or after the content has been retrieved? |
| Failure mode | Restricted content enters context and the trace store even when it is filtered out of the answer |
| Compliance constraint | Auditors require enforcement provable at the point of access, not asserted in application code |

### Decision Axis — Enforce in the Query vs Filter After Retrieval

Entitlement must constrain what is *retrievable*; anything filtered later has already entered context and observability storage.

| Situation | Answer | Why |
|---|---|---|
| Multi-tier document store, one service account, post-retrieval filtering | Propagate user identity and apply an entitlement filter as part of the retrieval query | Restricted chunks are never candidates, never ranked, never traced |
| The vector store cannot filter at query time | Separate indexes per entitlement tier, routed by caller tier | More infrastructure, but enforcement is structural rather than code-path dependent |
| A shared third-party integration where actions must be attributable to the operator | Per-user credential substitution rather than one shared service token | Attribution and revocation both require a per-user identity |
| Someone proposes a system-prompt rule stating what the agent may not access | Reject | Prompt-level rules are probabilistic; security enforcement must be deterministic |

### Exam scenario: a multi-user assistant reaches a tiered document store under a single service account and filters restricted results out of the answer

- ✅ Propagate the requesting user's identity to the retrieval layer and apply the entitlement filter inside the query
- ❌ Keep post-retrieval filtering and add a second review pass over the drafted answer — **REPAIR**: fixes downstream what the query could have prevented upstream, and the restricted content is already in context and in traces
- ❌ Add an explicit instruction to the system prompt telling the agent which tiers it may cite — **WRONG-AXIS**: treats an access-control problem as an instruction-following problem

### ❌ Misconception
"The agent runs under a trusted service account, so access control is already handled." — A service account collapses every user into one identity at the point where data is actually reached; each user's entitlement has to be re-established at the query.

---

## 3.4 Accuracy–Latency Budgeting

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Evaluate accuracy-latency trade-offs and justify configuration decisions |
| Discriminator | Does the option satisfy the *stated* requirement, or does it maximize an unstated one? |
| Method | Stage-level budget table at the percentile the SLA names |
| Accuracy levers that cost latency | Larger model · more retrieved chunks · reranking · reasoning cues · self-critique passes · multi-hop retrieval |
| The one lever that improves both | Static content ordered first with prompt caching enabled — cuts time-to-first-token and cost together |
| Stakeholder answer | Present the stage table and the measured accuracy delta, not a preference |

### Decision Axis — Requirement-Fit vs Maximum Accuracy

Check each option against the SLA the scenario states; the most accurate option is frequently the one that violates it.

| Situation | Answer | Why |
|---|---|---|
| Stated p95 budget with slack, accuracy short of target | Spend the slack on the highest accuracy-per-millisecond stage, usually reranking | Buys the requirement inside the budget |
| Proposed change exceeds the stated SLA | Reject it, or reopen the SLA explicitly with the stakeholder | An SLA breach is a decision to be made with the business, not absorbed silently |
| Latency and cost both named, large identical preamble on every request | Order static content first and enable prompt caching | A stable reused prefix cuts both, with no accuracy cost |
| Accuracy already above the stated target, an option offers more at triple the latency | Reject | Accuracy purchased outside a requirement is unpriced cost |
| Budget is tight and no slack exists | Look for wasted latency (ordering, caching, redundant hops) before cutting retrieved context | Cutting context costs more accuracy per millisecond saved than restructuring does |

### Exam scenario: a system at 2,800ms against a 3,000ms p95 SLA needs +4 accuracy points, and a proposed self-critique pass costs 1,400ms

- ✅ Reject the self-critique pass; reorder the static preamble to the front, enable prompt caching, and spend the recovered budget on a higher-capability generation model that fits inside the SLA
- ❌ Add the self-critique pass and raise the SLA to 4,500ms without consulting the business — **OVERSPEC**: buys a stronger guarantee than anyone asked for by breaking a contractual one that was stated
- ❌ Reduce the number of retrieved chunks to make room for the critique pass — **DISCARD**: removes a working mechanism rather than tuning the pipeline, and usually loses more accuracy than the critique pass returns

### ❌ Misconception
"If we can make the system more accurate, we should." — Accuracy is bought with latency and cost; an accuracy gain that breaches a stated SLA or budget is a failed design, not a better one.

---

## 3.5 Perceived Latency vs Total Latency

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Evaluate accuracy-latency trade-offs and justify configuration decisions |
| Streaming changes | Time-to-first-token |
| Streaming does not change | Total end-to-end latency |
| Discriminator | Does the consumer read incrementally, or wait for the complete response? |
| Percentile rule | Budget at the percentile the SLA names — usually p95 or p99, not the mean |

### Decision Axis — Interactive Consumer vs Batch Consumer

Streaming is worth a great deal to a human reading as tokens arrive and nothing at all to a service that parses the finished response.

| Situation | Answer | Why |
|---|---|---|
| Human-facing chat surface, users complain the system "feels slow" | Enable streaming | Time-to-first-token is what the complaint is actually about |
| Downstream service consumes the complete response before acting | Streaming buys nothing; reduce total latency instead | The consumer cannot start work early |
| Dashboard shows mean latency improved but users still complain | Measure and optimize p95/p99 | The SLA and the complaint both live in the tail |
| Both an interactive surface and a batch path share the pipeline | Stream the interactive path only; optimize total time for the batch path | Two consumers, two different latency definitions |

### Exam scenario: a service-to-service integration misses its latency SLA and someone proposes enabling streaming

- ✅ Reject streaming for this consumer and reduce total latency at the slowest measured stage
- ❌ Enable streaming and report the improved time-to-first-token against the SLA — **WRONG-AXIS**: right vocabulary, wrong metric; the consumer waits for the complete response either way
- ❌ Report the improved mean latency after a change that leaves p95 unchanged — **HALF-MOVE**: a real improvement measured at the wrong percentile, which is the one the SLA names

### ❌ Misconception
"Streaming makes the system faster." — It changes when the first token appears for a consumer that reads incrementally; total latency is unchanged and a batch consumer sees no benefit at all.

---

## 3.6 Observability — Trace Depth

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Analyze observability challenges and select monitoring strategies at scale |
| Unit of observability | The trace, not the log line |
| A useful trace captures | Tool calls with arguments and results · retrieved chunk IDs, document versions and scores · decision points and guardrail firings · one correlation ID end to end |
| Discriminator | Does the capture explain *why* the output was produced, or only *that* it was? |
| Failure mode without it | A confidently wrong answer is indistinguishable from a correct one at the response layer |
| Compliance constraint | Traces hold prompts and retrieved documents — a second copy of sensitive data with its own retention and access requirements |

### Decision Axis — Decision Path vs Final Output

Capture what the system decided and what it read, because the final output of a non-deterministic system does not explain itself.

| Situation | Answer | Why |
|---|---|---|
| Intermittent wrong answers, team can see only inputs and final outputs | Instrument tool calls, retrieved context with document versions, and decision points | Tells you which stage produced the error rather than that one did |
| Latency regression, only end-to-end timing captured | Add per-stage timing | Turns "the system got slow" into "the reranker got slow" |
| A request spans several agents and tools | Propagate one correlation ID through every hop | Without it, the trace fragments and cannot be reassembled |
| Traces will contain regulated content | Design redaction, retention and access control on the trace store at the same time as the pipeline | The observability system inherits the sensitivity of what it captures |

### Exam scenario: a RAG-backed agent intermittently returns wrong answers and the team has request/response logging only

- ✅ Add tracing that records retrieved chunk IDs with document versions and scores, every tool call and result, and the decision points, all tied to one correlation ID
- ❌ Increase log retention and add full request and response bodies at 100% — **HALF-MOVE**: more volume of the same low-information capture; still records outcomes rather than causes
- ❌ Add a user feedback widget and triage from reported issues — **REPAIR**: reacts after the fact, and confidently wrong answers are the failure users are least likely to report

### ❌ Misconception
"We log every request and response, so we have observability." — That records what happened and nothing about why; the diagnostic content is the tool calls, the retrieved context, and the decision points in between.

---

## 3.7 Trace Sampling Strategy at Scale

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Analyze observability challenges and select monitoring strategies at scale |
| Discriminator | Are the events you need to see common or rare? |
| Cost dimension | Full-fidelity traces run to gigabytes per day at six-figure request volumes |
| Stratified policy | 100% of errors, escalations, low-confidence paths, and audit-relevant requests; a small percentage of routine successes |
| Cardinality rule | Metrics carry low-cardinality dimensions (tool name, model, tenant tier, outcome class); user, session and document IDs belong in traces |
| Retention rule | Retention set per stratum — short for routine samples, regulation-length for audit metadata |

### Decision Axis — Stratified Sampling vs Uniform Sampling

Uniform sampling is calibrated to the common case; failures are rare, so capture all of them and only a slice of the routine traffic.

| Situation | Answer | Why |
|---|---|---|
| High volume, need to characterize failures | 100% of errors/escalations/low-confidence, 1–5% of successes | Captures every high-information event at a fraction of full-capture cost |
| High volume, need baseline distributions and regression detection | A small uniform sample of routine successes | Baselines only need enough samples to be stable |
| Regulated data accessed, audit requires proof of access | 100% of access metadata with redacted payload | Audit needs the fact of access, not the content |
| Someone proposes labelling metrics by user ID to enable per-user slicing | Reject; serve that need from traces | High-cardinality labels make the metrics backend slow and expensive |
| Someone proposes 100% full-fidelity capture "and we'll optimize later" | Reject on cost and on data-protection exposure | At these volumes it is unaffordable and creates a second sensitive store |

### Exam scenario: 200,000 requests/day, full tracing is unaffordable, and the team needs to diagnose a rising escalation rate

- ✅ Stratify: trace 100% of errors, escalations and low-confidence paths, 2% of routine successes, and keep redacted metadata for every regulated-data access
- ❌ Sample uniformly at 1% across all traffic — **WRONG-AXIS**: the textbook answer to a volume problem, applied to a rare-event problem; it captures almost none of the escalations
- ❌ Trace everything at full fidelity and revisit storage cost next quarter — **OVERSPEC**: buys total coverage nobody asked for, at a cost the scenario states is unavailable, and duplicates sensitive data into a new store

### ❌ Misconception
"We sample 1% of traffic, so our monitoring coverage is proportional." — Uniform sampling is proportional to the common case; the events worth tracing are rare, so they need their own 100% stratum.

---

## 3.8 RAG Chunk Boundaries

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design a RAG pipeline with appropriate chunking and indexing strategies |
| Definition of a chunk | The smallest span of a document that still makes sense read completely out of context |
| Discriminator | Does the boundary follow the document's own structure, or an arbitrary token count? |
| Overlap | 10–15% is insurance against a sentence straddling a boundary, not a chunking strategy |
| Content that should not be embedded | Tabular and relational data queried by filter or aggregation |
| Failure mode | Boundaries that cut mid-clause produce two chunks that are both individually useless |

### Decision Axis — Structure-Led Boundaries vs Fixed-Size Windows

Chunk on the seams the document's author already created — clause, endpoint, ticket, function — because those are where meaning is self-contained.

| Situation | Answer | Why |
|---|---|---|
| Policy manual with numbered clauses and heading hierarchy | Chunk on clause boundaries; carry clause number, heading path, effective date and jurisdiction as metadata | Version and jurisdiction metadata are a correctness requirement for time-sensitive lookups |
| API reference, one regular section per endpoint | Chunk per endpoint, whole | Splitting parameters from the description produces two unusable chunks |
| Support threads of 3–40 messages | Chunk per ticket, not per message | A single reply is unanswerable without the problem statement above it |
| Wide relational table of product specifications | Do not embed; expose as a structured query tool | Row embeddings are mostly noise, and aggregation has no vector-space answer |
| Unstructured prose with no headings at all | Fixed-size windows with overlap, as the fallback | The fallback is correct only where no structure exists to follow |

### Exam scenario: a knowledge base mixes clause-numbered policy manuals, threaded support tickets, and a 12,000-row specification table

- ✅ Chunk the manuals on clause boundaries and the tickets per thread, and expose the specification table as a structured query tool rather than embedding it
- ❌ Apply 512-token fixed windows with 50-token overlap uniformly across all three sources — **WRONG-AXIS**: treats chunk size as the decision when the decision is where the boundary falls, and it fails hardest on the structured content
- ❌ Embed the specification table row by row so everything lives in one index — **ARCHITECTED**: a single unified retrieval path sounds cleaner, but no retrieval tuning answers a counting or filtering question

### ❌ Misconception
"512-token chunks with overlap are a reasonable default for any corpus." — Boundaries should follow document structure; fixed windows are the fallback for prose that has no structure to follow.

---

## 3.9 Chunk Contextualization vs Chunk Enlargement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design a RAG pipeline with appropriate chunking and indexing strategies |
| Problem | A chunk pulled from mid-document loses the title and heading hierarchy that made it interpretable |
| Contextualization | Prepend document title and heading path to the chunk *text before embedding*, so the context enters the vector |
| Discriminator | Is the chunk missing context, or missing content? |
| Effect of enlarging chunks instead | The embedding is diluted across more topics, lowering retrieval precision |

### Decision Axis — Add Context vs Add Size

Prepend the surrounding context to the chunk; enlarging the chunk adds unrelated content to the same vector and costs precision.

| Situation | Answer | Why |
|---|---|---|
| Retrieved chunks are topically right but ambiguous out of context ("this limit does not apply to renewals") | Prepend title and heading path before embedding | Puts the missing context into the vector, not only into metadata |
| Retrieved chunks are genuinely truncated mid-idea | Fix the boundary to follow structure | The problem is the cut, not the size |
| Precision is dropping as chunk size grows | Reduce size and contextualize instead | A larger chunk spreads its embedding across more topics |
| Metadata already carries the heading path but is not embedded | Also prepend it to the embedded text | Metadata is filterable but does not influence semantic similarity |

### Exam scenario: retrieved policy chunks are on-topic but too ambiguous to answer from, and someone proposes doubling the chunk size

- ✅ Keep the chunk size and prepend the document title and full heading path to each chunk's text before embedding
- ❌ Double the chunk size so more surrounding text is included — **WRONG-AXIS**: treats a missing-context problem as a missing-length problem, and dilutes the embedding across additional topics
- ❌ Store the heading path in chunk metadata and surface it in the prompt after retrieval — **HALF-MOVE**: helps the model interpret what was retrieved, but does nothing to improve which chunks get retrieved

### ❌ Misconception
"Bigger chunks give the model more context, so retrieval gets better." — Larger chunks spread the embedding across more topics and lower precision; contextualization adds the missing context without the dilution.

---

## 3.10 Index Coupling & Post-Refresh Degradation

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design a RAG pipeline with appropriate chunking and indexing strategies |
| Coupled unit | Chunking scheme + embedding model version + vector index — change one and the space is inconsistent |
| Failure signature | No error; confident, fluent, wrong answers |
| Discriminator | Did the degradation correlate with an ingestion, refresh, or pipeline deployment? |
| Diagnostic order | Re-index completeness → chunk-schema change → embedding model version → stale vectors for deleted documents → only then prompt and model |
| Prevention | Golden queries with known-correct chunk IDs run after every re-index, blocking promotion on a hit-rate drop |
| Source | Official exam guide v1.0, §8 sample question — VERIFIED |

### Decision Axis — Retrieval/Indexing Layer vs Model/Prompt Layer

Degradation that begins immediately after a document refresh is a retrieval and indexing fault; the model and prompt did not change.

| Situation | Answer | Why |
|---|---|---|
| Quality falls right after a nightly document reload | Investigate the index: completeness, chunk schema, embedding version, stale vectors | The refresh is the only variable that moved |
| Answers cite clause numbers that do not match the quoted text | Suspect a chunk-schema change or a partial re-index | Content and metadata have come apart |
| Retrieval scores dropped across the board with no content change | Suspect an embedding model version drift | Vectors from a different model live in a different geometry |
| Quality degraded gradually with no deployment or refresh | Now the model, prompt, or drifting query distribution is in scope | No indexing event to correlate against |

### Exam scenario: a stable RAG system begins returning confident, fluent, incorrect answers the morning after a document refresh

- ✅ Investigate the retrieval and indexing layer — verify re-index completeness, the chunking configuration, the embedding model version pinned to the index, and removal of superseded vectors
- ❌ Lower the sampling temperature to reduce confident wrong answers — **WRONG-AXIS**: temperature governs token selection and says nothing about which documents were retrieved
- ❌ Move to a higher-capability model to improve answer quality — **DISCARD**: replaces a working component instead of repairing the one that changed; a better model reading the wrong document is more articulately wrong

### ❌ Misconception
"Confident wrong answers mean the model is hallucinating, so tighten the model settings." — When the degradation starts at a document refresh, the retrieval layer is feeding the model the wrong source; the model is reporting what it was given.

---

## 3.11 Retrieval Mechanism vs Data Shape & Query Pattern

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Apply retrieval strategies matched to data shape and query pattern |
| Dense/vector | Strong on paraphrase and conceptual similarity; weak on exact identifiers, codes, part numbers, rare proper nouns |
| Lexical/BM25 | Strong on exact terms and identifiers; weak on paraphrase |
| Hybrid | Earns its place when the corpus *and* the query mix contain both prose and exact identifiers |
| Structured query (SQL) | The answer for counting, summing, filtering and joining — not a retrieval problem |
| Graph traversal | Multi-hop relationship questions only; expensive to build and maintain |
| Metadata filter | Applied as part of the query so ranking happens within the eligible set |

### Decision Axis — Two Axes, Not One

Choose on what the data *is* and what the query *does*; a single mechanism across a mixed corpus is wrong for most of its query types.

| Situation | Answer | Why |
|---|---|---|
| Prose corpus, conceptual questions in natural language | Dense retrieval | Paraphrase tolerance is exactly what embeddings provide |
| Query contains an exact error code or part number | Lexical, or hybrid | Rare identifiers carry almost no distributional meaning and their vectors are near-noise |
| Corpus contains prose explanation with identifiers inline, users query both ways | Hybrid with fused ranking | This is the condition hybrid exists for |
| "How many X in region Y this quarter" | Structured query against the relational source | Aggregation has no vector-space answer |
| "What superseded part 88-2210J" | Foreign-key or graph traversal | A relationship lookup, not a similarity problem |
| Pure narrative corpus with no identifiers, queried in natural language | Dense only | Adding a lexical index and a fusion step buys nothing |

### Exam scenario: field technicians query a prose troubleshooting corpus using both plain descriptions and exact error codes, and code-based queries have a 34% hit rate

- ✅ Add lexical retrieval alongside dense and fuse the rankings, because the corpus and the query mix both contain exact identifiers and prose
- ❌ Tune the embedding model and increase top-k until the code-based queries succeed — **HALF-MOVE**: raises recall by flooding context while leaving the identifier weakness in place
- ❌ Build a knowledge graph over the equipment hierarchy to improve retrieval — **ARCHITECTED**: an impressive and expensive answer to a lexical-matching problem, with ongoing maintenance attached

### ❌ Misconception
"RAG means a vector database, so retrieval quality is an embedding-tuning problem." — Vector search is one mechanism among several; identifiers want lexical, aggregations want SQL, and relationships want traversal.

---

## 3.12 Retrieval Depth vs Reranking

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Apply retrieval strategies matched to data shape and query pattern |
| Pattern | Retrieve wide (top 20–50) with a fast approximate search, rerank narrow (top 3–5) with an accurate model |
| Discriminator | Is the right document absent from the candidate set, or present but ranked low? |
| Cost of raising top-k | More tokens, more cost, more latency, and a worse attention gradient over a longer context |
| Cost of reranking | An added latency stage that must fit the budget from §3.4 |

### Decision Axis — Rank Better vs Retrieve More

If the right document is already in the candidate set but ranked low, rerank; raising top-k only helps when the document is missing from the set entirely.

| Situation | Answer | Why |
|---|---|---|
| Correct document consistently retrieved at rank 8–15 | Add a reranking stage over the existing candidate set | It is a ranking problem, and the candidates are already there |
| Correct document not in the top 50 at all | Change the retrieval mechanism or the chunking, not the depth | Depth cannot surface something the mechanism never matches |
| Top-k already raised to 40 and context is crowded | Reduce k and rerank to 3–5 | Fewer, better chunks beat more, noisier ones |
| Reranking would breach the stated latency SLA | Reduce candidate width, or fund the stage by recovering latency elsewhere | The budget is the constraint, not the technique |

### Exam scenario: the correct document is retrieved but consistently ranks eighth, and answers use the wrong source

- ✅ Add a reranking stage that reorders the existing top-20 candidates down to the top 3–5 passed into context
- ❌ Raise top-k from 5 to 25 so the correct document is always included — **HALF-MOVE**: gets the document into context at the cost of 20 lower-relevance chunks, more spend, and a worse attention gradient
- ❌ Replace the retrieval mechanism with a different embedding model — **DISCARD**: swaps out a mechanism that is already surfacing the right document, to fix a ranking problem

### ❌ Misconception
"If the right document isn't being used, retrieve more documents." — When it is already in the candidate set, the problem is ranking; raising top-k floods context and worsens the very attention problem it is meant to solve.

---

## 3.13 Connection Protocol Selection

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent) |
| Discriminator | Who decides what happens next — your code, the model, or another agent? |
| Direct API/CLI | Known, mandatory, deterministic step; one round-trip; testable |
| MCP tools | Actions the model chooses to call |
| MCP resources | Read-only content the model can consult, e.g. a catalog of what exists |
| Agent-to-agent | The other side brings its own judgment, context, and accountability |
| Cost gradient | API < MCP tool call < agent-to-agent handoff; each step up buys flexibility and spends determinism |
| Build vs adopt | Community servers for standard integrations; custom servers for genuinely unique workflows |

### Decision Axis — Who Decides

Deterministic sequence known at design time is a direct call; model-chosen action is a tool; delegated judgment is another agent.

| Situation | Answer | Why |
|---|---|---|
| A record must be fetched on every request and the ID is already known | Direct API call in pre-processing | No model decision exists to make; one hop, deterministic, testable |
| A control that must run on every qualifying request | Direct API from the orchestration layer, not a tool | Exposing it as a tool lets the model choose not to call it |
| The agent should decide whether and when to search a document store | MCP tool | The decision depends on the conversation |
| The agent needs to know what content exists before querying | MCP resource exposing a catalog | Provides the map as readable context instead of exploratory model turns |
| A standard third-party system (issue tracker, source control, chat) | Existing community MCP server | Custom effort belongs on workflows nothing else covers |
| Work needing separate domain judgment and separate audit attribution | Agent-to-agent | The determination must be owned by the other function |

### Exam scenario: a compliance scoring service must run on every claim above a threshold, and the team proposes exposing it as an agent tool

- ✅ Call it directly from the orchestration layer whenever the threshold is met, keeping it outside the model's discretion
- ❌ Expose it as an MCP tool with a system-prompt rule requiring the agent to call it on every qualifying claim — **HALF-MOVE**: makes a mandatory control probabilistic, and adds a model decision's latency and cost to a deterministic step
- ❌ Delegate the scoring to a dedicated compliance agent that decides when to run — **ARCHITECTED**: a full inference loop and a second failure surface bought to perform what is a function call with fixed inputs

### ❌ Misconception
"Anything the agent might need should be exposed as a tool so it can decide." — A mandatory deterministic step should be a direct call; making it a tool introduces non-determinism into a step that had none.

---

## 3.14 Progressive Discovery vs Monolithic Context

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Evaluate progressive discovery vs. monolithic context strategy |
| Monolithic | Whole surface loaded every request; full token cost paid whether used or not |
| Progressive | Compact index loaded, detail fetched on demand |
| Discriminator | Is the surface large enough that the token saving exceeds the discovery round-trip? |
| Cost of progressive | One extra model turn on requests needing expansion, plus a discovery failure mode |
| Mitigations | Index entries written as a usable map, and high-frequency capabilities promoted into the base surface |
| Where monolithic wins | Small stable surface · latency budget that cannot absorb a round-trip · content needed on every single request |
| Content needed every request | Order it first and cache it — that is a caching answer, not a discovery answer |

### Decision Axis — Surface Size vs Round-Trip Cost

Below roughly ten tools the discovery round-trip costs more than the tokens it saves; well above that, the token tax and the discrimination load both justify the extra turn.

| Situation | Answer | Why |
|---|---|---|
| 60 tools across 8 systems, median request touches one system | Namespace-level index plus on-demand expansion | Most of the surface is irrelevant to any given request |
| Trace data shows six tools account for 61% of calls | Promote those six into the base surface | The common path stops paying the round-trip |
| Five stable tools and a tight latency budget | Load them all; skip discovery | The round-trip costs more than the surface does |
| A large document catalog the agent should be aware of | Expose it as a readable resource | The map stays current and is consulted on demand |
| A large identical block needed on every request | Order it first with prompt caching | Nothing is being discovered; it is always required |

### Exam scenario: an agent carries 60 tool definitions totalling ~12,000 tokens per request, misroutes frequently, and the median request touches one of eight systems

- ✅ Expose eight namespace-level entries with expansion on demand, and promote the highest-frequency tools into the base surface based on measured call distribution
- ❌ Paste the full tool catalog into the system prompt so the agent always has visibility — **WRONG-AXIS**: relocates monolithic context into the prompt and adds a staleness problem; nothing about the token cost or discrimination load changes
- ❌ Remove the least-used tools until the surface fits — **DISCARD**: eliminates required capabilities to solve a presentation problem, when restructuring how the surface is presented keeps them all

### ❌ Misconception
"Progressive discovery is the modern pattern, so load capabilities on demand wherever possible." — It costs a round-trip and introduces a discovery failure mode; on a small, stable surface, or under a tight latency budget, loading everything up front is the correct answer.

---

**Section count:** 14 major sections (§3.1–§3.14)
