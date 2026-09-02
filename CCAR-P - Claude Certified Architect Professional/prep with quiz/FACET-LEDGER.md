# CCAR-P Facet Ledger — v1

**Built:** 2026-08-29 · **Source:** the seven `CCAR-P_Domain-N_v1.md` corpus files, read-only.
**Rebuild rule:** this ledger is regenerated from the corpus and from shipped papers, never from a
session's own account of what it wrote. Foundations lost two seed records to prose self-report.

## What a facet is

One row of one decision table inside a corpus section: a `Situation | Answer | Why` triple. It is the
smallest independently testable decision the corpus contains, and it is the unit the generator
addresses.

Section-level addressing does not work here. 78 sections against a 63-item paper means one paper
consumes 80% of the corpus and Paper 2 has nothing fresh. Foundations hit that wall at Exam 8 with 71
sections and spent its remaining twelve papers managing it.

## Supply, measured

**Corrected 2026-09-01 — D2 corpus expansion implemented, Ram's decision, `EXAM-LOG.md` Paper 5
entry.** The numbers below through "Papers 1 through 5 are reachable without item 3" describe the
state through Paper 4 and are kept for the record, exactly as this project keeps every superseded
decision legible rather than erasing it. D2 gained 21 new decision-table rows (F-2.1-04/05,
F-2.2-05, F-2.3-04/05, F-2.4-03/04, F-2.5-03/04, F-2.6-02/03/04, F-2.7-02/03/04, F-2.8-02/03/04,
F-2.9-02/03/04) before Paper 5's D2 items were planned. D2 now holds **39 facets across 9 sections**,
up from 18, closing most of the gap to its siblings. The **372-facet / 39-D2-facet totals directly
below already include this expansion.**

**372 facets across 74 sections.** Four sections carry no decision table at all.

| Domain | Sections | Facets | Items/paper | Facets per item | Papers before reuse |
|---|---|---|---|---|---|
| D1 | 12 | 62 | 11 | 5.6 | **5.6** |
| D2 | 9 | 39 | 8 | 4.9 | **4.9** |
| D3 | 14 | 65 | 12 | 5.4 | **5.4** |
| D4 | 12 | 70 | 10 | 7.0 | **7.0** |
| D5 | 11 | 52 | 9 | 5.8 | **5.8** |
| D6 | 12 | 45 | 9 | 5.0 | **5.0** |
| D7 | 8 | 39 | 4 | 9.8 | **9.8** |
| **All** | **78** | **372** | **63** | **5.9** | **5.9** |

**D2's supply picture before this expansion (kept for the record):** 18 facets against 8 items per
paper was 2.2 papers of supply. Sections 2.6, 2.7, 2.8, and 2.9 held exactly one facet each. Paper 1
alone consumed 44% of every distinct decision D2 contained. Three ways out were identified, in
preference order:

1. **Direction doubling (in force since Paper 4).** A facet tests a decision axis, and the two sides
   of that axis are different items. The corpus already works this way — section 1.4 exists only to
   test the reverse direction of 1.3. Each facet therefore yields two addressable slots, `+` and `-`.
2. **Misconception units (fully spent as of Paper 4).** Every section carries one misconception
   block, which is a testable trap in its own right — 9 in D2, all 9 used across Papers 1-4.
3. **Corpus expansion — implemented 2026-09-01.** D2 needed roughly 20 more decision-table rows to
   match its siblings' density; 21 were added. This is the only fix that also raised D2's *coverage*,
   not just its *supply*, and is now done rather than deferred.

Papers 1 through 5 were reachable without item 3, using direction doubling plus misconception units.
Papers 6-10 would not have been without it — this is why the expansion was implemented at Paper 5
rather than deferred again. Facet freshness for Paper 5's own planning should still be computed from
the shipped HTML per standing practice (F-21), not from this ledger's "used" column.

## Ledger

Columns: `facet-id` · `section` · `objective` · the decision's situation and answer, abbreviated ·
`used` records `paper:direction:outcome` per sitting and is empty until a paper ships.

### D1

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-1.1-01` | 1.1 | O1.1 | Step is high-volume, machine-readable, correctness visible imme… | Automate the step | P1:normal:? |
| `F-1.1-02` | 1.1 | O1.1 | Step's outcome feedback arrives in 12 months (e.g. loss ratio) | Automate, with a proxy signal (override rate, r… | P3:normal:? |
| `F-1.1-03` | 1.1 | O1.1 | Step requires a licensed or statutorily human decision | Human decides; model prepares the draft | P2:normal:? |
| `F-1.1-04` | 1.1 | O1.1 | Whole workflow judged "not a fit" because one step is regulated | Reject that judgment — decompose first | P4:inverted:? |
| `F-1.1-05` | 1.1 | O1.1 | The human relationship is the product being sold | Automate the preparation, not the interaction | P5:inverted:? |
| `F-1.2-01` | 1.2 | O1.1 | Request: "can Claude write our quotes"; stated pain: 3.2-day tu… | Target turnaround; quality of prose is not the … | P1:normal:? |
| `F-1.2-02` | 1.2 | O1.1 | No baseline available for the current process | Measure it before committing to a design | P3:normal:? |
| `F-1.2-03` | 1.2 | O1.1 | Proposal to "measure the improvement after launch" | Reject | P2:normal:? |
| `F-1.2-04` | 1.2 | O1.1 | Capability that did not previously exist at all | No efficiency baseline exists; argue transforma… | P4:inverted:? |
| `F-1.3-01` | 1.3 | O1.3 | Five known steps, same order, every request | Workflow | P1:normal:? |
| `F-1.3-02` | 1.3 | O1.3 | Classify then dispatch to one of five specialised handlers | Workflow (routing pattern) | P3:normal:? |
| `F-1.3-03` | 1.3 | O1.3 | Number of steps unknown; each action depends on what the last o… | Agent | P4:normal:? |
| `F-1.3-04` | 1.3 | O1.3 | Task needs current or private data but the path is fixed | Augmented LLM | P2:normal:? |
| `F-1.3-05` | 1.3 | O1.3 | 96% of traffic is one known format, 4% is novel | Workflow with an agentic exception route | P5:normal:? |
| `F-1.4-01` | 1.4 | O1.3 | "Add comprehensive tests to a legacy codebase of unknown struct… | Agent with dynamic adaptive planning | P1:normal:? |
| `F-1.4-02` | 1.4 | O1.3 | "Produce the same six-section review for every submission" | Fixed pipeline (prompt chaining) | P3:normal:? |
| `F-1.4-03` | 1.4 | O1.3 | Agent chosen, and a p95 latency SLA is stated | Re-check — the agent's tail may fail the SLA ev… | P4:normal:? |
| `F-1.4-04` | 1.4 | O1.3 | Team proposes an agent "because the workflow feels rigid" | Reject absent a stated non-enumerable requireme… | P2:normal:? |
| `F-1.5-01` | 1.5 | O1.4 | Four independent research threads, turnaround is a stated commi… | Multi-agent, parallel fan-out | P1:normal:? |
| `F-1.5-02` | 1.5 | O1.4 | One agent's context would exceed the window, or threads would c… | Multi-agent | P2:normal:? |
| `F-1.5-03` | 1.5 | O1.4 | A drafting role must not have write access; a verifier must not… | Multi-agent | P4:normal:? |
| `F-1.5-04` | 1.5 | O1.4 | Sequential task, no latency constraint, one tool set would serve | Single agent | |
| `F-1.5-05` | 1.5 | O1.4 | Cost is the stated pillar and the subtasks are sequential | Single agent | |
| `F-1.6-01` | 1.6 | O1.4 | Report misses whole subtopics; every subagent returned correct … | Coordinator's decomposition was too narrow | P1:normal:? |
| `F-1.6-02` | 1.6 | O1.4 | Two subagents investigated the same ground | Coordinator did not partition the space before … | P3:normal:? |
| `F-1.6-03` | 1.6 | O1.4 | Final report's citations are wrong or missing | Content and metadata were passed as merged free… | P4:normal:? |
| `F-1.6-04` | 1.6 | O1.4 | One subagent's failure terminated the whole run | No structured error propagation and no coordina… | |
| `F-1.6-05` | 1.6 | O1.4 | Coordinator attempts everything itself and never delegates | The `Task`-equivalent spawning capability is ab… | |
| `F-1.6-06` | 1.6 | O1.4 | Research output is shallow and checklist-like | Coordinator prompt is procedural instead of goa… | |
| `F-1.7-01` | 1.7 | O1.4 | Synthesis subagent must cite sources | Pass findings as `{content, metadata}` with sou… | P1:normal:? |
| `F-1.7-02` | 1.7 | O1.4 | Synthesis output has coverage gaps | Coordinator evaluates, re-delegates targeted qu… | P5:inverted:? |
| `F-1.7-03` | 1.7 | O1.4 | Human reviewers keep re-asking for information the system alrea… | Structured handoff summary, self-contained | |
| `F-1.7-04` | 1.7 | O1.4 | Upstream inputs were partially unavailable (3 of 5 sources retu… | Synthesise with coverage annotations marking wh… | P2:normal:? |
| `F-1.7-05` | 1.7 | O1.4 | A subagent returns "0 results" | Accept as a valid finding | |
| `F-1.8-01` | 1.8 | O1.4 | Three independent aspects of one customer issue | Parallel fan-out in a single turn, then synthes… | P3:normal:? |
| `F-1.8-02` | 1.8 | O1.4 | Step B needs Step A's extracted entity | Sequential chaining | P5:normal:? |
| `F-1.8-03` | 1.8 | O1.4 | Coverage of the synthesis cannot be guaranteed in one pass | Iterative refinement loop with stated sufficien… | |
| `F-1.8-04` | 1.8 | O1.4 | Refinement loop runs indefinitely | Add explicit quality criteria the coordinator e… | P2:normal:? |
| `F-1.8-05` | 1.8 | O1.4 | Coordinator emits its delegations across successive turns | Fix to one turn | |
| `F-1.9-01` | 1.9 | O1.2 | Deployed system, humans reviewing output, no improvement over 6… | Capture the overrides and route them into the e… | P1:normal:? |
| `F-1.9-02` | 1.9 | O1.2 | Architecture lists input, processing, and output components | The feedback path is what is missing | P3:normal:? |
| `F-1.9-03` | 1.9 | O1.2 | Outcome signal arrives 12 months later | Add a fast proxy (override rate, reopen rate) a… | P4:normal:? |
| `F-1.9-04` | 1.9 | O1.2 | Team proposes a monitoring dashboard as the improvement mechani… | Insufficient on its own | P2:normal:? |
| `F-1.9-05` | 1.9 | O1.2 | Wrong citations after a document refresh | Route the signal to the retrieval/indexing layer | P5:normal:? |
| `F-1.10-01` | 1.10 | O1.2 | Unsupported file types reach the model and produce garbage | Reject at input validation | P1:normal:? |
| `F-1.10-02` | 1.10 | O1.2 | PII must not reach the model | Redact before the model call | P2:normal:? |
| `F-1.10-03` | 1.10 | O1.2 | Step A must always precede Step B for correctness | Programmatic precondition blocking B until A re… | P3:normal:? |
| `F-1.10-04` | 1.10 | O1.2 | Downstream service needs to route on model output | JSON contract with an explicit confidence field | P4:inverted:? |
| `F-1.10-05` | 1.10 | O1.2 | A human reviewer consumes the output | Include reasoning and citations alongside the v… | P5:normal:? |
| `F-1.10-06` | 1.10 | O1.2 | Customer tier and history would help the model | Attach at the input boundary | |
| `F-1.11-01` | 1.11 | O1.5 | 14-file PR reviewed in one pass; output shallow and inconsistent | Per-file local pass (parallel) + one integratio… | P1:normal:? |
| `F-1.11-02` | 1.11 | O1.5 | Integration pass receives all 14 raw diffs | Pass the structured per-file summaries instead | P3:normal:? |
| `F-1.11-03` | 1.11 | O1.5 | 90% routine cases, 10% hard, cost is the named pillar | Confidence-tier split: cheap path for routine, … | P2:normal:? |
| `F-1.11-04` | 1.11 | O1.5 | Mix of reversible actions and one irreversible action | Risk-tier split: reversible autonomous, irrever… | P3:normal:? |
| `F-1.11-05` | 1.11 | O1.5 | A design split so finely that later steps lack context earlier … | Merge steps | P4:inverted:? |
| `F-1.11-06` | 1.11 | O1.5 | Repeating review that always follows the same template | Fixed pipeline | P4:normal:? |
| `F-1.12-01` | 1.12 | O1.6 | p95 latency commitment of 3s; a 5-step serial chain is proposed | Parallelise independent steps and move enrichme… | P1:normal:? |
| `F-1.12-02` | 1.12 | O1.6 | Cost is the named pillar at high volume | Confidence-tier routing plus the smallest model… | P2:normal:? |
| `F-1.12-03` | 1.12 | O1.6 | A design halves inference cost and doubles human review time | Reject | P3:normal:? |
| `F-1.12-04` | 1.12 | O1.6 | Capability did not previously exist | Argue transformation; efficiency has no denomin… | P4:normal:? |
| `F-1.12-05` | 1.12 | O1.6 | Non-engineer stakeholder asks whether it is working | Answer in minutes, dollars, throughput, or comm… | P5:normal:? |
| `F-1.12-06` | 1.12 | O1.6 | Two designs both work; only one meets the stated commitment | Pick the one meeting the commitment | P5:normal:? |

### D2

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-2.1-01` | 2.1 | O2.1 | Narrow, bounded, high-volume, latency-gated classification | Smallest/fastest model that clears the accuracy… | P1:normal:?, P4:inverted:? |
| `F-2.1-02` | 2.1 | O2.1 | Multi-step synthesis across ambiguous sources, low volume | Higher-capability model | P2:normal:? |
| `F-2.1-03` | 2.1 | O2.1 | A stakeholder asks for "the biggest model, to be safe," with no… | Push back — ask what specifically requires it | P2:normal:? |
| `F-2.1-04` | 2.1 | O2.1 | Workload already meets its accuracy bar; a newer, more capable … | Only upgrade if a specific unmet requirement dr… | P5:inverted:? |
| `F-2.1-05` | 2.1 | O2.1 | Deep multi-step reasoning across ambiguous, high-stakes trade-o… | Enable extended thinking for that step, not a m… | P5:normal:? |
| `F-2.2-01` | 2.2 | O2.2 | Tone, persona, or response-format rule for the whole conversati… | System prompt | P1:normal:?, P4:inverted:? |
| `F-2.2-02` | 2.2 | O2.2 | A rule stated in the first user message | Not durable | P2:normal:? |
| `F-2.2-03` | 2.2 | O2.2 | A rule "set" via an environment variable | No effect at all | P3:normal:? |
| `F-2.2-04` | 2.2 | O2.2 | A refusal boundary or escalation trigger (a guardrail) | System prompt | P2:normal:? |
| `F-2.2-05` | 2.2 | O2.2 | A guardrail needs to react differently depending on which tool/… | Scope the guardrail to the relevant layer, not … | P5:inverted:? |
| `F-2.3-01` | 2.3 | O2.3 | Model inconsistently formats output despite clear instructions | Add 3–4 examples of the exact required format | P1:normal:? |
| `F-2.3-02` | 2.3 | O2.3 | Model misroutes an ambiguous request between two tools | Add 4–6 examples targeted at exactly that ambig… | P3:normal:? |
| `F-2.3-03` | 2.3 | O2.3 | Proposal to add 10–15 examples of clear-cut, unambiguous cases | Reject | P2:normal:? |
| `F-2.3-04` | 2.3 | O2.3 | Few-shot examples already in place but drawn from easy cases, n… | Replace with examples drawn from the observed f… | P5:normal:? |
| `F-2.3-05` | 2.3 | O2.3 | A single well-chosen example already resolves an ambiguous case… | Ship with that one targeted example, no padding | |
| `F-2.4-01` | 2.4 | O2.3 | Multi-step reasoning or comparison task | Add a "think step by step" cue | P1:normal:?, P4:inverted:? |
| `F-2.4-02` | 2.4 | O2.3 | Single-step task (e.g., translate one sentence) | Don't add a reasoning cue | P2:normal:? |
| `F-2.4-03` | 2.4 | O2.3 | Multi-step task already reasons correctly without a cue, verifi… | Don't add the cue | P5:inverted:? |
| `F-2.4-04` | 2.4 | O2.3 | Multi-step task also carries a latency budget the reasoning tok… | Use a bounded/structured reasoning cue, not ope… | |
| `F-2.5-01` | 2.5 | O2.4 | Claude "forgot" something from 2 turns ago, in a short conversa… | Application isn't including prior messages in t… | P1:normal:? |
| `F-2.5-02` | 2.5 | O2.4 | Latency/cost rising as a conversation passes 50 turns | Full history resent every call — more turns mea… | P2:normal:? |
| `F-2.5-03` | 2.5 | O2.4 | Team wants to reduce tokens resent per call without losing cont… | Summarize/truncate older turns, still resend fu… | |
| `F-2.5-04` | 2.5 | O2.4 | Two separate client sessions for the same user need to share co… | Application must merge and pass combined histor… | |
| `F-2.6-01` | 2.6 | O2.4 | Long synthesis input misses critical mid-document findings | Restructure: findings-first + headings + struct… | P1:normal:? |
| `F-2.6-02` | 2.6 | O2.4 | A single precision-critical fact sits mid-document and gets fab… | Pull that fact into a short structured highligh… | P5:normal:? |
| `F-2.6-03` | 2.6 | O2.4 | Whether ordering matters when total input is short, well under … | No — the phenomenon needs length to trigger it | |
| `F-2.6-04` | 2.6 | O2.4 | Scattered facts of equal importance, no single dominant finding | Convert to explicit headed sections grouped by … | |
| `F-2.7-01` | 2.7 | O2.4 | Long conversation with precision-critical facts (amounts, IDs, … | Extract critical facts into a structured block,… | P1:normal:?, P4:inverted:? |
| `F-2.7-02` | 2.7 | O2.4 | An early decision must never change for the rest of a hundreds-… | Pin it into a persistent block, separate from t… | P5:normal:? |
| `F-2.7-03` | 2.7 | O2.4 | Unsure how often to re-run automatic summarization of older tur… | Re-summarize incrementally as turns roll off | |
| `F-2.7-04` | 2.7 | O2.4 | Retrieved documents and conversation history both need space in… | Budget each source independently against the wi… | |
| `F-2.8-01` | 2.8 | O2.5 | Identical large system prompt/policy sent on every request, var… | Order static content first, enable prompt cachi… | P1:normal:?, P4:inverted:? |
| `F-2.8-02` | 2.8 | O2.5 | A byte-identical static block has a dynamic timestamp inserted … | Move the dynamic content to after the cached pr… | P5:inverted:? |
| `F-2.8-03` | 2.8 | O2.5 | A caching candidate is only requested once every 20 minutes, lo… | Accept caching won't help; use another lever | |
| `F-2.8-04` | 2.8 | O2.5 | Two downstream tools each need a different static block appende… | Shared prefix, then per-tool block, then dynami… | |
| `F-2.9-01` | 2.9 | O2.5 | Multiple teams each maintain their own copy of similar system p… | Consolidate into versioned, shared modular prom… | P2:normal:? |
| `F-2.9-02` | 2.9 | O2.5 | A shared component updates, but some teams stay pinned to an ol… | Version the component explicitly for independen… | |
| `F-2.9-03` | 2.9 | O2.5 | A team's use case needs 90% of a shared Skill plus one differin… | Parameterize/extend the Skill, don't fork it | |
| `F-2.9-04` | 2.9 | O2.5 | No discovery mechanism; teams re-author snippets that already e… | Maintain a discoverable, indexed catalog | |

### D3

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-3.1-01` | 3.1 | O3.1 | One agent holds 20+ tools spanning several unrelated roles, mis… | Split into role-scoped agents of 4–6 tools each | P1:normal:?, P5:inverted:? |
| `F-3.1-02` | 3.1 | O3.1 | Two tools in the same scoped agent are still confused | Expand both descriptions with input formats, bo… | P3:normal:? |
| `F-3.1-03` | 3.1 | O3.1 | A generic tool (`fetch_url`) is being used outside its intended… | Replace it with a constrained tool that validat… | P2:normal:? |
| `F-3.1-04` | 3.1 | O3.1 | A scoped agent needs one simple cross-role lookup on nearly eve… | Give it a narrowly scoped cross-role tool | P3:normal:? |
| `F-3.1-05` | 3.1 | O3.1 | A stakeholder asks to keep all tools available "for flexibility" | Push back with the per-request token cost and t… | P4:inverted:? |
| `F-3.2-01` | 3.2 | O3.2 | Agent holds a write/delete capability no workflow uses | Remove it from the tool set | P1:normal:? |
| `F-3.2-02` | 3.2 | O3.2 | Agent needs a consequential capability that a workflow genuinel… | Keep it and add human confirmation and audit lo… | P2:normal:? |
| `F-3.2-03` | 3.2 | O3.2 | Agent needs a capability only for a specific narrow case | Replace the broad capability with a narrow one … | P3:normal:? |
| `F-3.2-04` | 3.2 | O3.2 | Compliance requires proof of who did what | Audit logging, in addition to removal of unneed… | P4:normal:? |
| `F-3.3-01` | 3.3 | O3.2 | Multi-tier document store, one service account, post-retrieval … | Propagate user identity and apply an entitlemen… | P1:normal:? |
| `F-3.3-02` | 3.3 | O3.2 | The vector store cannot filter at query time | Separate indexes per entitlement tier, routed b… | P2:normal:? |
| `F-3.3-03` | 3.3 | O3.2 | A shared third-party integration where actions must be attribut… | Per-user credential substitution rather than on… | P3:normal:? |
| `F-3.3-04` | 3.3 | O3.2 | Someone proposes a system-prompt rule stating what the agent ma… | Reject | P4:normal:? |
| `F-3.4-01` | 3.4 | O3.3 | Stated p95 budget with slack, accuracy short of target | Spend the slack on the highest accuracy-per-mil… | P1:normal:? |
| `F-3.4-02` | 3.4 | O3.3 | Proposed change exceeds the stated SLA | Reject it, or reopen the SLA explicitly with th… | P3:normal:? |
| `F-3.4-03` | 3.4 | O3.3 | Latency and cost both named, large identical preamble on every … | Order static content first and enable prompt ca… | P4:inverted:? |
| `F-3.4-04` | 3.4 | O3.3 | Accuracy already above the stated target, an option offers more… | Reject | P2:normal:? |
| `F-3.4-05` | 3.4 | O3.3 | Budget is tight and no slack exists | Look for wasted latency (ordering, caching, red… | P5:normal:? |
| `F-3.5-01` | 3.5 | O3.3 | Human-facing chat surface, users complain the system "feels slo… | Enable streaming | P1:normal:? |
| `F-3.5-02` | 3.5 | O3.3 | Downstream service consumes the complete response before acting | Streaming buys nothing; reduce total latency in… | P2:normal:? |
| `F-3.5-03` | 3.5 | O3.3 | Dashboard shows mean latency improved but users still complain | Measure and optimize p95/p99 | P3:normal:? |
| `F-3.5-04` | 3.5 | O3.3 | Both an interactive surface and a batch path share the pipeline | Stream the interactive path only; optimize tota… | P4:normal:? |
| `F-3.6-01` | 3.6 | O3.4 | Intermittent wrong answers, team can see only inputs and final … | Instrument tool calls, retrieved context with d… | P1:normal:? |
| `F-3.6-02` | 3.6 | O3.4 | Latency regression, only end-to-end timing captured | Add per-stage timing | P3:normal:? |
| `F-3.6-03` | 3.6 | O3.4 | A request spans several agents and tools | Propagate one correlation ID through every hop | P4:normal:? |
| `F-3.6-04` | 3.6 | O3.4 | Traces will contain regulated content | Design redaction, retention and access control … | P5:normal:? |
| `F-3.7-01` | 3.7 | O3.4 | High volume, need to characterize failures | 100% of errors/escalations/low-confidence, 1–5%… | P1:normal:? |
| `F-3.7-02` | 3.7 | O3.4 | High volume, need baseline distributions and regression detecti… | A small uniform sample of routine successes | P3:normal:? |
| `F-3.7-03` | 3.7 | O3.4 | Regulated data accessed, audit requires proof of access | 100% of access metadata with redacted payload | P2:normal:? |
| `F-3.7-04` | 3.7 | O3.4 | Someone proposes labelling metrics by user ID to enable per-use… | Reject; serve that need from traces | P4:normal:? |
| `F-3.7-05` | 3.7 | O3.4 | Someone proposes 100% full-fidelity capture "and we'll optimize… | Reject on cost and on data-protection exposure | P5:normal:? |
| `F-3.8-01` | 3.8 | O3.5 | Policy manual with numbered clauses and heading hierarchy | Chunk on clause boundaries; carry clause number… | P1:normal:? |
| `F-3.8-02` | 3.8 | O3.5 | API reference, one regular section per endpoint | Chunk per endpoint, whole | P3:normal:? |
| `F-3.8-03` | 3.8 | O3.5 | Support threads of 3–40 messages | Chunk per ticket, not per message | P5:normal:? |
| `F-3.8-04` | 3.8 | O3.5 | Wide relational table of product specifications | Do not embed; expose as a structured query tool | |
| `F-3.8-05` | 3.8 | O3.5 | Unstructured prose with no headings at all | Fixed-size windows with overlap, as the fallback | |
| `F-3.9-01` | 3.9 | O3.5 | Retrieved chunks are topically right but ambiguous out of conte… | Prepend title and heading path before embedding | P1:normal:? |
| `F-3.9-02` | 3.9 | O3.5 | Retrieved chunks are genuinely truncated mid-idea | Fix the boundary to follow structure | P5:inverted:? |
| `F-3.9-03` | 3.9 | O3.5 | Precision is dropping as chunk size grows | Reduce size and contextualize instead | P2:normal:? |
| `F-3.9-04` | 3.9 | O3.5 | Metadata already carries the heading path but is not embedded | Also prepend it to the embedded text | |
| `F-3.10-01` | 3.10 | O3.5 | Quality falls right after a nightly document reload | Investigate the index: completeness, chunk sche… | P2:normal:? |
| `F-3.10-02` | 3.10 | O3.5 | Answers cite clause numbers that do not match the quoted text | Suspect a chunk-schema change or a partial re-i… | P4:inverted:? |
| `F-3.10-03` | 3.10 | O3.5 | Retrieval scores dropped across the board with no content change | Suspect an embedding model version drift | |
| `F-3.10-04` | 3.10 | O3.5 | Quality degraded gradually with no deployment or refresh | Now the model, prompt, or drifting query distri… | |
| `F-3.11-01` | 3.11 | O3.6 | Prose corpus, conceptual questions in natural language | Dense retrieval | P1:normal:? |
| `F-3.11-02` | 3.11 | O3.6 | Query contains an exact error code or part number | Lexical, or hybrid | P3:normal:? |
| `F-3.11-03` | 3.11 | O3.6 | Corpus contains prose explanation with identifiers inline, user… | Hybrid with fused ranking | P5:normal:? |
| `F-3.11-04` | 3.11 | O3.6 | "How many X in region Y this quarter" | Structured query against the relational source | P2:normal:? |
| `F-3.11-05` | 3.11 | O3.6 | "What superseded part 88-2210J" | Foreign-key or graph traversal | |
| `F-3.11-06` | 3.11 | O3.6 | Pure narrative corpus with no identifiers, queried in natural l… | Dense only | |
| `F-3.12-01` | 3.12 | O3.6 | Correct document consistently retrieved at rank 8–15 | Add a reranking stage over the existing candida… | P4:normal:? |
| `F-3.12-02` | 3.12 | O3.6 | Correct document not in the top 50 at all | Change the retrieval mechanism or the chunking,… | |
| `F-3.12-03` | 3.12 | O3.6 | Top-k already raised to 40 and context is crowded | Reduce k and rerank to 3–5 | |
| `F-3.12-04` | 3.12 | O3.6 | Reranking would breach the stated latency SLA | Reduce candidate width, or fund the stage by re… | P2:normal:? |
| `F-3.13-01` | 3.13 | O3.7 | A record must be fetched on every request and the ID is already… | Direct API call in pre-processing | P1:normal:? |
| `F-3.13-02` | 3.13 | O3.7 | A control that must run on every qualifying request | Direct API from the orchestration layer, not a … | P2:normal:? |
| `F-3.13-03` | 3.13 | O3.7 | The agent should decide whether and when to search a document s… | MCP tool | P3:normal:? |
| `F-3.13-04` | 3.13 | O3.7 | The agent needs to know what content exists before querying | MCP resource exposing a catalog | P4:normal:? |
| `F-3.13-05` | 3.13 | O3.7 | A standard third-party system (issue tracker, source control, c… | Existing community MCP server | P5:normal:? |
| `F-3.13-06` | 3.13 | O3.7 | Work needing separate domain judgment and separate audit attrib… | Agent-to-agent | |
| `F-3.14-01` | 3.14 | O3.8 | 60 tools across 8 systems, median request touches one system | Namespace-level index plus on-demand expansion | P1:normal:? |
| `F-3.14-02` | 3.14 | O3.8 | Trace data shows six tools account for 61% of calls | Promote those six into the base surface | P3:normal:? |
| `F-3.14-03` | 3.14 | O3.8 | Five stable tools and a tight latency budget | Load them all; skip discovery | P2:normal:? |
| `F-3.14-04` | 3.14 | O3.8 | A large document catalog the agent should be aware of | Expose it as a readable resource | P4:normal:? |
| `F-3.14-05` | 3.14 | O3.8 | A large identical block needed on every request | Order it first with prompt caching | P5:normal:? |

### D4

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-4.1-01` | 4.1 | O4.1 | New capability, no baseline yet | Set the bar from the success criterion, frontie… | P1:normal:? |
| `F-4.1-02` | 4.1 | O4.1 | Stakeholder asks to "calibrate the threshold once we see baseli… | Reject — set it now, revise it as a recorded de… | P3:normal:? |
| `F-4.1-03` | 4.1 | O4.1 | Existing manual process with a measured 8% error rate is being … | Bar tied to and beating 8% | P3:normal:? |
| `F-4.1-04` | 4.1 | O4.1 | Open-ended safety property, proposed bar of 0% | Re-anchor to a small non-zero rate (e.g. < 0.1%… | P5:normal:? |
| `F-4.1-05` | 4.1 | O4.1 | Requirement is "outputs must never contain another customer's a… | 0 per N — deterministic check | P5:normal:? |
| `F-4.2-01` | 4.2 | O4.1 | "The assistant must not produce discriminatory language" | Safety | P1:normal:? |
| `F-4.2-02` | 4.2 | O4.1 | "A malicious instruction inside a retrieved document must not t… | Security | P4:normal:? |
| `F-4.2-03` | 4.2 | O4.1 | "The agent must not be able to read records outside the request… | Security | P2:normal:? |
| `F-4.2-04` | 4.2 | O4.1 | "Outputs must not include another policyholder's identifier" | Both — deterministic PII check is the enforcing… | P4:normal:? |
| `F-4.2-05` | 4.2 | O4.1 | Proposal to cover a prompt-injection risk with a tone rubric | Reject | |
| `F-4.3-01` | 4.3 | O4.2 | 500-case set reports 96%, customers still report failures | Rebuild from real production failures and repor… | P1:normal:? |
| `F-4.3-02` | 4.3 | O4.2 | Same situation, proposal to expand to 2,000 cases drawn the sam… | Reject | P3:normal:? |
| `F-4.3-03` | 4.3 | O4.2 | Set has 600 unverified synthetic cases with an unknown label er… | Cut to 40 hand-verified cases | |
| `F-4.3-04` | 4.3 | O4.2 | Set contains only failure cases | Add matched shouldn't-fire cases | |
| `F-4.3-05` | 4.3 | O4.2 | Set contains only clean cases | Add should-fire cases per known failure mode | |
| `F-4.3-06` | 4.3 | O4.2 | Genuinely new capability, no production traces exist yet | Hand-write cases and label the whole set provis… | |
| `F-4.4-01` | 4.4 | O4.2 | 50-case set, document mix 78/15/5/2 across four types | Rebuild with enough cases per type to support a… | P1:normal:? |
| `F-4.4-02` | 4.4 | O4.2 | Team proposes auto-processing everything above an aggregate con… | Analyse accuracy by document type and field fir… | P4:normal:? |
| `F-4.4-03` | 4.4 | O4.2 | Ongoing audit of an automated extraction path | Stratified random sample across document types … | |
| `F-4.4-04` | 4.4 | O4.2 | Proposal to review only the lowest-confidence extractions | Reject as the sole audit | |
| `F-4.4-05` | 4.4 | O4.2 | Proposal to sample only the most common document type | Reject | |
| `F-4.5-01` | 4.5 | O4.2 | "Every output must be valid JSON matching this schema" | Deterministic schema validation | P1:normal:? |
| `F-4.5-02` | 4.5 | O4.2 | "Every cited passage must exist verbatim in the cited document" | Deterministic verbatim string check | P3:normal:? |
| `F-4.5-03` | 4.5 | O4.2 | "No output may contain another customer's account identifier" | Deterministic pattern/field scan | |
| `F-4.5-04` | 4.5 | O4.2 | "The answer must be in the right register for a regulated commu… | Model grader with a binary rubric | |
| `F-4.5-05` | 4.5 | O4.2 | "The summary must be faithful to the source" | Model grader for faithfulness, with an overlap … | |
| `F-4.5-06` | 4.5 | O4.2 | Ambiguous cases where two adjusters disagree on the verdict | Human adjudication, and re-scope the eval row | |
| `F-4.6-01` | 4.6 | O4.2 | New model grader proposed for tone and helpfulness | Hand-label 20–50 cases, run the grader, compute… | P4:normal:? |
| `F-4.6-02` | 4.6 | O4.2 | Agreement measured at 0.62 | Rebuild the criterion as binary sub-criteria an… | |
| `F-4.6-03` | 4.6 | O4.2 | Agreement still below bar after rework, no deterministic fallba… | Drop the row and record why | |
| `F-4.6-04` | 4.6 | O4.2 | Only a same-family grader is available | Use it but mark the row degraded; never report … | |
| `F-4.6-05` | 4.6 | O4.2 | Grader has been in production six months, never re-audited | Resume periodic human calibration | P2:normal:? |
| `F-4.7-01` | 4.7 | O4.2 | RAG assistant with one overall quality score, regression cannot… | Split into retrieval and generation rows | P5:normal:? |
| `F-4.7-02` | 4.7 | O4.2 | Retrieval Recall@5 = 0.55, generation faithfulness = 0.97 | Both bars are read; the system fails on retriev… | |
| `F-4.7-03` | 4.7 | O4.2 | Agent completes the task but deleted a record on the way | Fail | P2:normal:? |
| `F-4.7-04` | 4.7 | O4.2 | Agent selects correct tools in correct order but final state is… | Fail | |
| `F-4.7-05` | 4.7 | O4.2 | Multi-turn assistant recovers by turn 6 from a turn-2 error | Report the turn-2 failure | |
| `F-4.8-01` | 4.8 | O4.2 | Code generation with a test harness that reruns on failure | `pass@k` | P5:normal:? |
| `F-4.8-02` | 4.8 | O4.2 | Tool call behind a schema validator that retries on rejection | `pass@k` | |
| `F-4.8-03` | 4.8 | O4.2 | Agent must confirm with a human before any irreversible action | `pass^k` = 1.0 | |
| `F-4.8-04` | 4.8 | O4.2 | Every generated answer is shown directly to a customer | `pass^k` | P2:normal:? |
| `F-4.8-05` | 4.8 | O4.2 | Confirmation gate reported as `pass@5 = 1.0` | Reject the framing | |
| `F-4.9-01` | 4.9 | O4.3 | Prompt edit looked better on ten hand-picked examples | Run the regression set first, then a controlled… | P1:normal:? |
| `F-4.9-02` | 4.9 | O4.3 | Variant changes prompt, model, and retrieval depth together | Split into separate variants | P1:normal:? |
| `F-4.9-03` | 4.9 | O4.3 | A/B randomized per request | Re-randomize by user or session | P2:normal:? |
| `F-4.9-04` | 4.9 | O4.3 | Test looks favourable at day 4 of a planned 14 | Run to the declared duration | P3:normal:? |
| `F-4.9-05` | 4.9 | O4.3 | Variant improves the primary metric, breaches the declared late… | Do not ship | P4:normal:? |
| `F-4.9-06` | 4.9 | O4.3 | Aggregate improves 1.5 points, one segment regresses 12 | Do not ship on the aggregate | P3:normal:? |
| `F-4.9-07` | 4.9 | O4.3 | Change already shipped to 100% with no control arm | State that no clean comparison exists | P4:normal:? |
| `F-4.10-01` | 4.10 | O4.4 | Confidently wrong right after a document refresh or re-index | Retrieval / indexing | P1:normal:? |
| `F-4.10-02` | 4.10 | O4.4 | Wrong on one document or query type, correct elsewhere | Data coverage / chunking | P3:normal:? |
| `F-4.10-03` | 4.10 | O4.4 | Facts correct, required format or steps missing | Prompt / instructions | P3:normal:? |
| `F-4.10-04` | 4.10 | O4.4 | Format inconsistent across runs despite explicit instructions | Few-shot examples needed | P4:inverted:? |
| `F-4.10-05` | 4.10 | O4.4 | Fails only on long inputs; misses mid-document facts | Context structure and position | P4:normal:? |
| `F-4.10-06` | 4.10 | O4.4 | Forgets a fact from two turns ago in a short conversation | Application not resending history | P2:normal:? |
| `F-4.10-07` | 4.10 | O4.4 | Fails broadly on multi-step reasoning, retrieval verified, prom… | Model mismatch | P5:normal:? |
| `F-4.11-01` | 4.11 | O4.5 | Identical large policy preamble on every request; latency and c… | Order static content first and enable prompt ca… | P3:normal:? |
| `F-4.11-02` | 4.11 | O4.5 | Same situation, proposal to cut the preamble by 60% | Reject if the removed sections are required | P4:inverted:? |
| `F-4.11-03` | 4.11 | O4.5 | Same situation, proposal to summarize the preamble with an extr… | Reject | P5:normal:? |
| `F-4.11-04` | 4.11 | O4.5 | Quality floor plus a budget ceiling, mixed task difficulty | Cascade: small model for the routine class, esc… | P1:normal:? |
| `F-4.11-05` | 4.11 | O4.5 | Nightly batch job, latency complaint | Batch/async and output shaping | P2:normal:? |
| `F-4.11-06` | 4.11 | O4.5 | Retrieval fetches top 20 passages | Reduce to the passages that clear the relevance… | P2:normal:? |
| `F-4.11-07` | 4.11 | O4.5 | Latency complaint, no stage-level timing collected | Profile first | P5:normal:? |
| `F-4.12-01` | 4.12 | O4.6 | Quality metric moved, cause unknown, only final outputs are log… | Add prompt/model version, retrieved ids, tool c… | P1:normal:? |
| `F-4.12-02` | 4.12 | O4.6 | Cost tripled overnight, latency up, quality flat | Check cache-read token counts and the prompt-ve… | P2:normal:? |
| `F-4.12-03` | 4.12 | O4.6 | Dashboard shows aggregate averages only | Add per-segment breakdowns | P3:normal:? |
| `F-4.12-04` | 4.12 | O4.6 | Alerting configured to fire on every individual error | Alert on rates and segment rates instead | P4:normal:? |
| `F-4.12-05` | 4.12 | O4.6 | Only complaints and flagged outputs are sampled for quality | Add stratified sampling of the high-confidence … | P5:normal:? |
| `F-4.12-06` | 4.12 | O4.6 | Post-incident, the proposed remedy is "add monitoring" | Accept as prevention, not as the root-cause fix | |
| `F-4.12-07` | 4.12 | O4.6 | Regulated sector, real-traffic logs | Redact at write, define retention, restrict acc… | P2:normal:? |

### D5

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-5.1-01` | 5.1 | O5.1 | Output classifier is the only safety control on a customer-faci… | Add pre-call input validation, tool scoping, an… | P1:normal:? |
| `F-5.1-02` | 5.1 | O5.1 | Team proposes replacing four simple checks with one fine-tuned … | Reject | P4:normal:? |
| `F-5.1-03` | 5.1 | O5.1 | Assistant already has input validation, output filtering, and s… | Add the human-approval layer on the consequenti… | P2:normal:? |
| `F-5.1-04` | 5.1 | O5.1 | A low-consequence internal drafting tool with no external outpu… | Input validation and output schema checks are s… | P4:normal:? |
| `F-5.2-01` | 5.2 | O5.1 | Agent has a write/delete tool it has never legitimately needed | Remove the tool | P1:normal:? |
| `F-5.2-02` | 5.2 | O5.1 | Agent needs the capability sometimes, and misuse is consequenti… | Model emits a structured request; a separate se… | P3:normal:? |
| `F-5.2-03` | 5.2 | O5.1 | Agent needs the capability routinely, misuse is low-consequence… | Keep the tool, add logging | P3:normal:? |
| `F-5.2-04` | 5.2 | O5.1 | Proposal: keep the dangerous tool and log every invocation | Reject as the primary control | P5:normal:? |
| `F-5.3-01` | 5.3 | O5.4 | Regulated identifiers must never reach the inference endpoint | De-identify or tokenise in the pipeline before … | P1:normal:? |
| `F-5.3-02` | 5.3 | O5.4 | Same requirement, proposal is a system-prompt instruction to ig… | Reject | P4:inverted:? |
| `F-5.3-03` | 5.3 | O5.4 | Same requirement, proposal is nightly redaction of stored logs | Reject as the control | P2:normal:? |
| `F-5.3-04` | 5.3 | O5.4 | Requirement is a strong preference rather than an absolute (e.g… | A prompt instruction is appropriate | P5:inverted:? |
| `F-5.4-01` | 5.4 | O5.4 | EU customer records feeding a support assistant | Minimise fields to what the task needs, declare… | P1:normal:? |
| `F-5.4-02` | 5.4 | O5.4 | Clinical narratives drafted by an assistant | Strip direct identifiers before the call, send … | P3:normal:? |
| `F-5.4-03` | 5.4 | O5.4 | Federal agency deployment where the preferred model is not in a… | The model is unavailable for that data; route t… | P3:normal:? |
| `F-5.4-04` | 5.4 | O5.4 | A GDPR erasure request arrives for a customer whose support tic… | Deletion must reach the logs, the evaluation da… | P5:normal:? |
| `F-5.5-01` | 5.5 | O5.4 | Team proposes retaining all requests and responses indefinitely… | Reject; define purpose and duration, and de-ide… | P1:normal:? |
| `F-5.5-02` | 5.5 | O5.4 | Incident investigation needs recent traffic | Bounded window (e.g., 30 days), de-identified, … | P4:normal:? |
| `F-5.5-03` | 5.5 | O5.4 | Regulator may ask why a specific decision was made | Retain the decision trace — inputs used, versio… | P2:normal:? |
| `F-5.5-04` | 5.5 | O5.4 | Auditability requirement met by application logs the operations… | Reject | |
| `F-5.6-01` | 5.6 | O5.2 | Confidently wrong immediately after a content refresh | Retrieval / indexing | P3:normal:? |
| `F-5.6-02` | 5.6 | O5.2 | No memory of something said two turns earlier, short conversati… | Application not resending history | P3:normal:? |
| `F-5.6-03` | 5.6 | O5.2 | Quality degrades only on long inputs, on mid-document content | Uneven attention across position | P2:normal:? |
| `F-5.6-04` | 5.6 | O5.2 | Behaviour changed with no code deployment | Model version drift | P1:normal:? |
| `F-5.6-05` | 5.6 | O5.2 | Every step passes its own test, end-to-end accuracy is far lower | Compounding across steps (0.96^10 ≈ 66%) | P4:normal:? |
| `F-5.6-06` | 5.6 | O5.2 | Agent took an unrequested action after processing an external d… | Indirect prompt injection | P4:normal:? |
| `F-5.6-07` | 5.6 | O5.2 | RAG answers turned confident and wrong the day the corpus was r… | Investigate chunking, embedding version, and in… | P5:normal:? |
| `F-5.6-08` | 5.6 | O5.2 | Ten-step agent at 96% per step delivering ~66% end-to-end | Insert deterministic validation checkpoints mid… | |
| `F-5.6-09` | 5.6 | O5.2 | Same prompt, same code, different behaviour this week | Check the pinned model version and run the regr… | |
| `F-5.6-10` | 5.6 | O5.2 | Risk register ranking: a rare irreversible action vs a frequent… | Rank the irreversible one higher | |
| `F-5.7-01` | 5.7 | O5.2 | Agent summarises third-party documents and holds a tool that ca… | Remove the send capability, or require human ap… | P1:normal:? |
| `F-5.7-02` | 5.7 | O5.2 | Same agent, proposal is a filter for known injection phrasings | Keep as a layer, reject as the control | |
| `F-5.7-03` | 5.7 | O5.2 | Retrieved content must be included in context | Wrap it in a delimited block the system prompt … | P2:normal:? |
| `F-5.7-04` | 5.7 | O5.2 | Agent processes only internally authored, access-controlled con… | Delimiting plus input validation is proportiona… | |
| `F-5.8-01` | 5.8 | O5.3 | High volume, high accuracy, mixed consequence | Auto-approve high-confidence low-consequence; r… | P1:normal:?, P5:inverted:? |
| `F-5.8-02` | 5.8 | O5.3 | Any irreversible or externally visible action (denial, payment,… | Human, regardless of confidence | P2:normal:? |
| `F-5.8-03` | 5.8 | O5.3 | Monitoring whether the auto-approved threshold is still correct | Continuous small sample of the auto-approved st… | P3:normal:? |
| `F-5.8-04` | 5.8 | O5.3 | Volume figure is stated in the scenario and 100% review is prop… | Reject | P3:normal:? |
| `F-5.8-05` | 5.8 | O5.3 | Genuinely low-volume, uniformly high-consequence work (e.g., a … | Human review of every item is correct | P4:normal:? |
| `F-5.9-01` | 5.9 | O5.2 | Extracted figures must match the source document | Deterministic comparison against the structured… | P5:normal:? |
| `F-5.9-02` | 5.9 | O5.2 | Cited policy clauses must exist | Look each citation up in the policy database be… | P2:normal:? |
| `F-5.9-03` | 5.9 | O5.2 | Free-text summary quality with no ground truth available | A second-model or rubric-based check, with its … | |
| `F-5.9-04` | 5.9 | O5.2 | Team proposes a self-critique pass to catch hallucination | Accept as a quality improvement, reject as the … | |
| `F-5.10-01` | 5.10 | O5.5 | 91% aggregate accuracy, complaints concentrated in one group | Disaggregate the metric by subgroup on a strati… | P1:normal:? |
| `F-5.10-02` | 5.10 | O5.5 | Proposal to drop the protected attribute from the input | Reject as the fairness control | P4:normal:? |
| `F-5.10-03` | 5.10 | O5.5 | Small subgroup, population-proportional evaluation sample | Rebalance to equal N per group | P2:normal:? |
| `F-5.10-04` | 5.10 | O5.5 | Two fairness metrics cannot both be satisfied | Choose by which harm is being controlled and re… | P5:normal:? |
| `F-5.10-05` | 5.10 | O5.5 | Fairness measured once at launch and signed off | Recompute on live traffic on a schedule | |
| `F-5.11-01` | 5.11 | O5.5 | Regulator asks why a specific applicant was declined | Produce the stored trace — fields used, version… | P3:normal:? |
| `F-5.11-02` | 5.11 | O5.5 | Team proposes attaching a model-written explanation to each dec… | Useful for the end user, not the audit record | P5:normal:? |
| `F-5.11-03` | 5.11 | O5.5 | Requirement is that people know they are interacting with an AI… | Disclosure at the point of interaction, plus a … | |
| `F-5.11-04` | 5.11 | O5.5 | Consequential automated decision with no challenge path | Add a contestation route with a queue and a sta… | P2:normal:? |

### D6

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-6.1-01` | 6.1 | O6.1 | Sponsor asks for "a multi-agent system to handle our intake" | Elicit the intake problem and the decision it f… | P1:normal:? |
| `F-6.1-02` | 6.1 | O6.1 | Sponsor names a pattern and the elicited problem does not need … | Say so, with the simpler design and what it giv… | P2:normal:? |
| `F-6.1-03` | 6.1 | O6.1 | Sponsor states a business outcome with no solution attached | Proceed to bounding the requirement (see 6.2) | P4:normal:? |
| `F-6.1-04` | 6.1 | O6.1 | Team proposes benchmarking candidate models before the problem … | Defer | |
| `F-6.2-01` | 6.2 | O6.1 | Sponsor says "as accurate as possible" | Establish the accuracy the use case requires an… | P1:normal:? |
| `F-6.2-02` | 6.2 | O6.1 | Requirement is bounded but the evaluation set is unspecified | Specify a held-out set stratified to the real i… | P2:normal:? |
| `F-6.2-03` | 6.2 | O6.1 | Sponsor cannot state the cost of an error | Keep eliciting; it determines threshold, review… | |
| `F-6.2-04` | 6.2 | O6.1 | Requirement is bounded, measured, and the mix is known | Move to design | P5:normal:? |
| `F-6.3-01` | 6.3 | O6.1 | Missed fraud costs 200× a false alert | Bias toward recall; route flagged cases to huma… | P1:normal:? |
| `F-6.3-02` | 6.3 | O6.1 | False rejection blocks a legitimate customer payment; a missed … | Bias toward precision; set a higher action thre… | P3:normal:? |
| `F-6.3-03` | 6.3 | O6.1 | Sponsor asks only for "95% accuracy" with both directions unpri… | Return to discovery and price both directions | P3:normal:? |
| `F-6.3-04` | 6.3 | O6.1 | Both directions cost roughly the same and are correctable | A single accuracy target is adequate | |
| `F-6.4-01` | 6.4 | O6.2 | 94% on standard cases, 61% on complex, sponsor wants "one numbe… | Give per-segment figures, the measurement basis… | P1:normal:? |
| `F-6.4-02` | 6.4 | O6.2 | Performance is genuinely uniform across input types | A single figure is honest — still state the met… | P2:normal:? |
| `F-6.4-03` | 6.4 | O6.2 | Architect declines to give any number because "it depends on th… | Not acceptable | P3:normal:? |
| `F-6.4-04` | 6.4 | O6.2 | Sponsor has been given the model metric and is planning against… | Supply the end-to-end outcome with human steps … | P4:normal:? |
| — | 6.5 | O6.3 | *no decision table — scenario and misconception only* | | |
| `F-6.6-01` | 6.6 | O6.2 | Stakeholder asks why the last 20% still needs people | Name the decisions in that 20% that carry accou… | P1:normal:?, P5:inverted:? |
| `F-6.6-02` | 6.6 | O6.2 | The residual work is unverifiable rather than regulated | Say so: the system cannot check its own output … | P3:normal:? |
| `F-6.6-03` | 6.6 | O6.2 | The residual work is small, low-risk, and merely unbuilt | Say so, and price it | P4:normal:? |
| `F-6.6-04` | 6.6 | O6.2 | Stakeholder proposes removing review from a regulated segment t… | Refuse on the named attestation requirement, an… | P2:normal:?, P4:inverted:? |
| `F-6.7-01` | 6.7 | O6.4 | Documenting a model-tier choice made under a latency ceiling | Record the decision, the rejected options with … | P1:normal:? |
| `F-6.7-02` | 6.7 | O6.4 | A year-old decision is questioned after a constraint changed | Check the recorded constraint and re-evaluate a… | P3:normal:? |
| `F-6.7-03` | 6.7 | O6.4 | Team proposes a detailed component diagram and inventory as the… | Insufficient alone | P3:normal:? |
| `F-6.7-04` | 6.7 | O6.4 | Team proposes a recorded architecture walkthrough | Insufficient alone | P5:normal:? |
| `F-6.8-01` | 6.8 | O6.4 | Another team will extend the pipeline | Interface contracts, configuration rationale, f… | P1:normal:? |
| `F-6.8-02` | 6.8 | O6.4 | A prompt or model change is proposed post-handover | Regression tests that must pass first, named in… | P2:normal:? |
| `F-6.8-03` | 6.8 | O6.4 | Team asks for an onboarding overview document instead | Supplement, not substitute | P4:normal:? |
| `F-6.8-04` | 6.8 | O6.4 | Configuration values documented without their rationale | Insufficient | P4:normal:? |
| `F-6.9-01` | 6.9 | O6.3 | Client wants "95% accuracy" in the contract | Commit per segment, with the scoring method, th… | P1:normal:? |
| `F-6.9-02` | 6.9 | O6.3 | Provider offers only availability and latency, no accuracy comm… | Insufficient | P4:inverted:? |
| `F-6.9-03` | 6.9 | O6.3 | Client's input mix is contractually fixed and monitored | A tighter accuracy commitment is defensible | P2:normal:? |
| `F-6.9-04` | 6.9 | O6.3 | Latency commitment on a provider-hosted endpoint | Commit a percentile, not a maximum | P4:normal:? |
| `F-6.10-01` | 6.10 | O6.3 | Sponsor's expectations inflated after a successful demo | Establish a recurring review showing real perfo… | P3:normal:? |
| `F-6.10-02` | 6.10 | O6.3 | Users report failures in a shared chat channel | Restructure: capture input, output, expected ou… | P2:normal:? |
| `F-6.10-03` | 6.10 | O6.3 | Feedback is collected but the evaluation set never grows | Broken loop | P3:normal:? |
| `F-6.10-04` | 6.10 | O6.3 | A single well-argued memo resets the sponsor's understanding | Necessary, not sufficient | P5:inverted:? |
| `F-6.11-01` | 6.11 | O6.5 | Successful 40-user pilot going to 800 users | List which input, support-load, and edge-case a… | P2:normal:? |
| `F-6.11-02` | 6.11 | O6.5 | A 1-in-500 failure seen twice in a 200-case pilot | Plan for it as a routine event | P3:normal:? |
| `F-6.11-03` | 6.11 | O6.5 | Human review absorbed 12% of pilot volume | Convert to a staffing line at projected volume … | P5:normal:? |
| `F-6.11-04` | 6.11 | O6.5 | Rate limits and infrastructure capacity for the new volume | Necessary, and not the binding constraint | |
| `F-6.12-01` | 6.12 | O6.5 | System transferring to an internal operations team | Evaluation suite, thresholds, named owner and d… | P1:normal:? |
| `F-6.12-02` | 6.12 | O6.5 | Handover consists of repository access, documentation, and trai… | Insufficient | P4:normal:? |
| `F-6.12-03` | 6.12 | O6.5 | Ownership assigned to a team rather than a person | Insufficient | |
| `F-6.12-04` | 6.12 | O6.5 | Complaints rise post-launch while error rates are flat | Check input-distribution shift and re-run the e… | P2:normal:? |
| `F-6.12-05` | 6.12 | O6.5 | Evaluation set unchanged twelve months after launch | Broken iteration | |

### D7

| facet-id | sec | obj | situation | answer | used |
|---|---|---|---|---|---|
| `F-7.1-01` | 7.1 | O7.1 | Three engineers apply a convention, a fourth (new) does not, sa… | The convention lives in the originals' `~/.clau… | P1:normal:?, P5:inverted:? |
| `F-7.1-02` | 7.1 | O7.1 | A partner team wants to adopt your Claude Code setup | Version-controlled shared configuration, skills… | P2:normal:? |
| `F-7.1-03` | 7.1 | O7.1 | Same situation, offered as a recorded walkthrough | Reject | P4:normal:? |
| `F-7.1-04` | 7.1 | O7.1 | Same situation, offered as a shared chat channel for questions | Reject | |
| `F-7.1-05` | 7.1 | O7.1 | Results on a large legacy codebase are poor; team blames repo s… | Write the conventions and structure into commit… | |
| `F-7.1-06` | 7.1 | O7.1 | One engineer wants their own `/commit` behaviour without affect… | `~/.claude/skills/commit/SKILL.md` — same name,… | |
| `F-7.1-07` | 7.1 | O7.1 | A subdirectory file is added to "override" the project file for… | Reject | |
| `F-7.2-01` | 7.2 | O7.1 | A skill uses a tool it should not touch | Scope `allowed-tools` in that skill's frontmatt… | P1:normal:? |
| `F-7.2-02` | 7.2 | O7.1 | Same situation, fixed by adding "do not use that tool" to the s… | Reject | P4:normal:? |
| `F-7.2-03` | 7.2 | O7.1 | A skill's exploratory output crowds the main task out of context | Set `context: fork` | P3:normal:? |
| `F-7.2-04` | 7.2 | O7.1 | Same situation, fixed by adding "be concise" to the skill | Reject | P5:normal:? |
| `F-7.2-05` | 7.2 | O7.1 | A convention applies only to test files but bleeds elsewhere | `.claude/rules/` entry with a glob for test pat… | P3:normal:? |
| `F-7.2-06` | 7.2 | O7.1 | Universal coding standards | Project CLAUDE.md | |
| `F-7.2-07` | 7.2 | O7.1 | A 500-line CLAUDE.md mixing standards, PR checklists and deploy… | Keep universal standards; move workflow procedu… | |
| `F-7.2-08` | 7.2 | O7.1 | Same situation, fixed by moving everything into skills | Reject | |
| `F-7.2-09` | 7.2 | O7.1 | A rule that must hold every time regardless of what any prompt … | Deterministic enforcement — a hook, or a `deny`… | P3:normal:? |
| `F-7.2-10` | 7.2 | O7.1 | A style preference, proposed for deterministic enforcement | Reject | |
| `F-7.3-01` | 7.3 | O7.2 | Restructure a monolith into services across dozens of files | Plan mode | P1:normal:? |
| `F-7.3-02` | 7.3 | O7.2 | Add a new integration with multiple valid approaches | Plan mode | P3:normal:? |
| `F-7.3-03` | 7.3 | O7.2 | Library migration touching 45+ files | Plan mode | P4:normal:? |
| `F-7.3-04` | 7.3 | O7.2 | Implement a function against a well-defined input/output spec | Direct execution | |
| `F-7.3-05` | 7.3 | O7.2 | Single-file bug fix with a clear stack trace | Direct execution | |
| `F-7.3-06` | 7.3 | O7.2 | Large task, but the approach was settled in an approved design | Direct execution | |
| `F-7.3-07` | 7.3 | O7.2 | Multi-approach refactor in a change-controlled environment | Plan mode | |
| — | 7.4 | O7.2 | *no decision table — scenario and misconception only* | | |
| `F-7.5-01` | 7.5 | O7.2 | Each finding must be posted as an inline PR comment (path, line… | `--output-format json` with `--json-schema` | P5:normal:? |
| `F-7.5-02` | 7.5 | O7.2 | Same situation, addressed by an "Output Format" section in CLAU… | Reject | |
| `F-7.5-03` | 7.5 | O7.2 | CI job hangs indefinitely instead of completing | Add `-p` / `--print` | |
| `F-7.5-04` | 7.5 | O7.2 | Review posts near-duplicate comments on every push | Include the prior run's findings in the re-run … | |
| `F-7.5-05` | 7.5 | O7.2 | Overnight tech-debt report, nobody blocked | Batch API | |
| `F-7.5-06` | 7.5 | O7.2 | Blocking pre-merge check | Synchronous | P2:normal:? |
| `F-7.5-07` | 7.5 | O7.2 | Non-urgent analysis that fetches related files mid-analysis | Synchronous | P2:normal:? |
| — | 7.6 | O7.2 | *no decision table — scenario and misconception only* | | |
| — | 7.7 | O7.3 | *no decision table — scenario and misconception only* | | |
| `F-7.8-01` | 7.8 | O7.1 | A capability must never be exercised, regardless of any prompt | A `deny` rule in `settings.json` permissions | P1:normal:? |
| `F-7.8-02` | 7.8 | O7.1 | Same situation, addressed by a strongly-worded CLAUDE.md instru… | Reject | P4:normal:? |
| `F-7.8-03` | 7.8 | O7.1 | An action must happen every time a tool runs (format, test, aud… | A hook on the relevant event, scoped by matcher | P5:normal:? |
| `F-7.8-04` | 7.8 | O7.1 | Same situation, addressed by "remember to run the formatter" in… | Reject | |
| `F-7.8-05` | 7.8 | O7.1 | A tool call must be stopped before it executes | `PreToolUse` hook, or a `deny` permission rule | P2:normal:? |
| `F-7.8-06` | 7.8 | O7.1 | A narrow `allow` exists and a broad `deny` also matches | Denied | P3:normal:? |
| `F-7.8-07` | 7.8 | O7.1 | An organisation must guarantee a rule survives every local over… | Managed policy settings | P3:normal:? |
| `F-7.8-08` | 7.8 | O7.1 | A team style preference, proposed for a hook or a deny rule | Reject | |

## Misconception units

One per section, addressable as `M-<section>`. Used when a facet would repeat, and preferred over any
facet reuse on Papers 1 through 5.

| unit | sec | obj | the misconception |
|---|---|---|---|
| `M-1.1` | 1.1 | O1.1 | "If any step in the process is regulated, the process isn't a candidate for AI." — Fit is score… |
| `M-1.2` | 1.2 | O1.1 | "We'll know it worked because everyone will notice the difference." — Value on this exam is sta…  **[used: P5:normal:?]** |
| `M-1.3` | 1.3 | O1.3 | "Agentic architectures are the modern approach; workflows are what you build when you can't do … |
| `M-1.4` | 1.4 | O1.3 | "The safe answer is always the simpler architecture." — Simplicity is the default, not the rule…  **[used: P5:inverted:?]** |
| `M-1.5` | 1.5 | O1.4 | "Multi-agent is the more scalable architecture, so it's the safer default for a complex problem… |
| `M-1.6` | 1.6 | O1.4 | "The subagent produced the bad output, so the subagent is where the fix goes." — Decomposition,… |
| `M-1.7` | 1.7 | O1.4 | "Telling the synthesis agent to always include its sources will fix the citation problem." — It… |
| `M-1.8` | 1.8 | O1.4 | "An iteration limit is what stops the refinement loop." — A cap stops runaway spend; terminatio… |
| `M-1.9` | 1.9 | O1.2 | "We log every request and response, so we have a feedback loop." — Logs record what happened; f… |
| `M-1.10` | 1.10 | O1.2 | "If the system prompt states the rule clearly enough, the model will follow it every time." — M… |
| `M-1.11` | 1.11 | O1.5 | "Break the work into as many small steps as possible — smaller is always more reliable." — Ever…  **[used: P5:normal:?]** |
| `M-1.12` | 1.12 | O1.6 | "The SLA is a target we'll tune toward once we see real traffic." — A latency or availability c… |
| `M-2.1` | 2.1 | O2.1 | "The safest choice is always the largest model." — Model choice is a cost-latency-quality trade…  **[used: P3:normal:?]** |
| `M-2.2` | 2.2 | O2.2 | "If it's documented anywhere in the pipeline, the model will follow it." — Only content that ac…  **[used: P3:normal:?]** |
| `M-2.3` | 2.3 | O2.3 | "More examples always help." — Only examples targeted at the specific ambiguous cases fix the f…  **[used: P4:normal:?]** |
| `M-2.4` | 2.4 | O2.3 | "Chain-of-thought never hurts, so add it everywhere." — It's a targeted tool for multi-step tas…  **[used: P3:normal:?]** |
| `M-2.5` | 2.5 | O2.4 | "Claude has some memory across calls by default." — The API has none; all continuity is the app…  **[used: P4:normal:?]** |
| `M-2.6` | 2.6 | O2.4 | "The fix for 'lost in the middle' is a shorter prompt." — The fix is structural position and fo…  **[used: P3:normal:?]** |
| `M-2.7` | 2.7 | O2.4 | "Summarization is always safe as long as it's shorter." — Uniform summarization loses precision…  **[used: P3:normal:?]** |
| `M-2.8` | 2.8 | O2.5 | "Caching means storing the response for reuse." — Prompt caching reuses a stable *input prefix*…  **[used: P3:normal:?]** |
| `M-2.9` | 2.9 | O2.5 | "Documentation of the prompt is enough; everyone can copy it once." — A copied prompt drifts th…  **[used: P4:normal:?]** |
| `M-3.1` | 3.1 | O3.1 | "More tools give the agent more flexibility, so extra tools can only help." — Every tool costs …  **[used: P4:normal:?]** |
| `M-3.2` | 3.2 | O3.2 | "Least privilege means monitoring closely what the agent does with its permissions." — Least pr…  **[used: P5:normal:?]** |
| `M-3.3` | 3.3 | O3.2 | "The agent runs under a trusted service account, so access control is already handled." — A ser…  **[used: P5:normal:?]** |
| `M-3.4` | 3.4 | O3.3 | "If we can make the system more accurate, we should." — Accuracy is bought with latency and cos… |
| `M-3.5` | 3.5 | O3.3 | "Streaming makes the system faster." — It changes when the first token appears for a consumer t…  **[used: P5:normal:?]** |
| `M-3.6` | 3.6 | O3.4 | "We log every request and response, so we have observability." — That records what happened and… |
| `M-3.7` | 3.7 | O3.4 | "We sample 1% of traffic, so our monitoring coverage is proportional." — Uniform sampling is pr… |
| `M-3.8` | 3.8 | O3.5 | "512-token chunks with overlap are a reasonable default for any corpus." — Boundaries should fo… |
| `M-3.9` | 3.9 | O3.5 | "Bigger chunks give the model more context, so retrieval gets better." — Larger chunks spread t… |
| `M-3.10` | 3.10 | O3.5 | "Confident wrong answers mean the model is hallucinating, so tighten the model settings." — Whe… |
| `M-3.11` | 3.11 | O3.6 | "RAG means a vector database, so retrieval quality is an embedding-tuning problem." — Vector se… |
| `M-3.12` | 3.12 | O3.6 | "If the right document isn't being used, retrieve more documents." — When it is already in the … |
| `M-3.13` | 3.13 | O3.7 | "Anything the agent might need should be exposed as a tool so it can decide." — A mandatory det… |
| `M-3.14` | 3.14 | O3.8 | "Progressive discovery is the modern pattern, so load capabilities on demand wherever possible.… |
| `M-4.1` | 4.1 | O4.1 | "We'll set the pass threshold once we see what the baseline looks like." — A bar chosen after t… |
| `M-4.2` | 4.2 | O4.1 | "Safety and security metrics are two names for the same thing." — Safety scores emitted content… |
| `M-4.3` | 4.3 | O4.2 | "A bigger evaluation set is a better evaluation set." — Coverage of the failure modes that actu… |
| `M-4.4` | 4.4 | O4.2 | "97% accuracy means we can safely reduce human review." — Aggregates average away segment-level… |
| `M-4.5` | 4.5 | O4.2 | "An LLM judge with a good rubric can grade anything." — Never route a code-checkable property t… |
| `M-4.6` | 4.6 | O4.2 | "If the rubric is detailed enough, the judge's score is the system's quality." — An unvalidated… |
| `M-4.7` | 4.7 | O4.2 | "One quality score is enough if the rubric is good." — RAG grades retrieval and generation sepa… |
| `M-4.8` | 4.8 | O4.2 | "pass@5 and pass^5 both mean we tested it five times." — `pass@k` measures reachable success be… |
| `M-4.9` | 4.9 | O4.3 | "The new prompt clearly performs better on our examples, so we can ship it." — A prompt change …  **[used: P5:inverted:?]** |
| `M-4.10` | 4.10 | O4.4 | "The model started hallucinating, so we need a better model." — Diagnose data and retrieval fir…  **[used: P5:normal:?]** |
| `M-4.11` | 4.11 | O4.5 | "Cutting the system prompt is a free cost saving." — Removing required policy or safety content… |
| `M-4.12` | 4.12 | O4.6 | "We log everything, so we have observability." — Observability means attribution: without promp… |
| `M-5.1` | 5.1 | O5.1 | "We have a strong safety classifier, so the system is guarded." — One layer is a single point o… |
| `M-5.2` | 5.2 | O5.1 | "Least privilege is satisfied by auditing privileged actions." — It is satisfied by not grantin…  **[used: P5:normal:?]** |
| `M-5.3` | 5.3 | O5.4 | "If we instruct the model clearly enough and measure high compliance, the requirement is met." … |
| `M-5.4` | 5.4 | O5.4 | "FedRAMP is a configuration setting we can enable." — It is an authorisation status of the envi… |
| `M-5.5` | 5.5 | O5.4 | "Keeping everything is the cautious choice — you can always delete later." — Retention creates … |
| `M-5.6` | 5.6 | O5.2 | "Confidently wrong output means the model is hallucinating." — When the fault is in retrieval, … |
| `M-5.7` | 5.7 | O5.2 | "Prompt injection is a content problem we can filter." — It follows from instructions and data … |
| `M-5.8` | 5.8 | O5.3 | "Start by reviewing everything and dial it back once we trust it." — Without an exit criterion,…  **[used: P4:normal:?]** |
| `M-5.9` | 5.9 | O5.2 | "Have the model check its own work before returning it." — A self-check shares the failure mode… |
| `M-5.10` | 5.10 | O5.5 | "Remove the protected attribute and the system can't be biased." — Proxy variables carry the sa… |
| `M-5.11` | 5.11 | O5.5 | "The model can explain its own decisions, so the system is explainable." — A generated rational… |
| `M-6.1` | 6.1 | O6.1 | "The stakeholder owns the requirement, so the architect's job is to build what they specify." —… |
| `M-6.2` | 6.2 | O6.1 | "'As accurate as possible' means aim as high as the budget allows." — It means the requirement … |
| `M-6.3` | 6.3 | O6.1 | "Higher overall accuracy is always the better system." — Where error costs are asymmetric, the … |
| `M-6.4` | 6.4 | O6.2 | "They asked for one number, so giving them one number is responsive." — Where performance varie…  **[used: P5:inverted:?]** |
| `M-6.5` | 6.5 | O6.3 | "More metrics gives the stakeholder a fuller picture." — A metric that does not inform the deci…  **[used: P5:normal:?]** |
| `M-6.6` | 6.6 | O6.2 | "Explaining why full automation isn't possible means explaining that AI isn't perfect." — The u…  **[used: P5:normal:?]** |
| `M-6.7` | 6.7 | O6.4 | "Good architecture documentation describes the system thoroughly." — Thorough description of th…  **[used: P5:normal:?]** |
| `M-6.8` | 6.8 | O6.4 | "If the code is clean and commented, the receiving team has what they need." — Code states what… |
| `M-6.9` | 6.9 | O6.3 | "An SLA is an SLA — commit the number we measured." — Availability and latency are provider-con… |
| `M-6.10` | 6.10 | O6.3 | "We have a feedback channel, so we have a feedback loop." — A loop captures the input, the outp… |
| `M-6.11` | 6.11 | O6.5 | "The pilot worked, so scaling it is a capacity exercise." — Scaling widens the input distributi… |
| `M-6.12` | 6.12 | O6.5 | "Handover is complete when the team has the code, the documentation, and a walkthrough." — Degr… |
| `M-7.1` | 7.1 | O7.1 | "Personal configuration is fine as long as everyone sets it up the same way." — Personal config… |
| `M-7.2` | 7.2 | O7.1 | "If the model does the wrong thing, tell it more firmly in the prompt." — A behaviour governed … |
| `M-7.3` | 7.3 | O7.2 | "Plan mode is for big tasks." — Plan mode is for undetermined approaches; a large task whose ap… |
| `M-7.4` | 7.4 | O7.2 | "Report one issue per message so it can focus." — True for independent issues; for interacting … |
| `M-7.5` | 7.5 | O7.2 | "The batch API is the cheap option for any job that isn't urgent." — Batch cannot execute a too… |
| `M-7.6` | 7.6 | O7.2 | "Adoption is high and usage keeps climbing, so the investment is paying off." — Activity metric… |
| `M-7.7` | 7.7 | O7.3 | "Behaviour that works sometimes is non-deterministic and hard to pin down." — It is usually con… |
| `M-7.8` | 7.8 | O7.1 | "Hooks and permission rules are two names for the same enforcement layer." — A permission rule … |

## Canonical worked examples — reserved, never an item

Each section's `Exam scenario` block is that section's canonical worked example. A generated item must
produce a **different failure mode** from it. On Foundations this single instruction caught 9 of 15
draft questions in one block before they reached the coordinator.

A hybrid plan once made Paper 1 an exception (TRANSCRIBE mode, these scenarios as the direct item
source) — rejected 2026-08-29/30 after measurement showed the corpus's own correct answers run
longest 84% of the time. Every paper, including Paper 1, is authored fresh; canonical scenarios stay
reference-only from Paper 1 onward.
