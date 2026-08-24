# Authoring brief — D5 Context Management & Reliability (15%) · building: The hospital ward

Corpus depth file: `prep with quiz/CCA-Prep_Domain-5_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements 5.1–5.x and the sample questions).

30 cards, in this order (ids fixed):

## D5-01 — Summaries blur numbers — keep a case-facts block outside the history
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Amounts, dates, order numbers and statuses go into a persistent structured block included in every prompt; summarised history loses them.
Official-guide bullets this card must cover:
- [5.1-K1] Progressive summarization risks: condensing numerical values, percentages, dates, and customer-stated expectations into vague summaries
- [5.1-S1] Extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent "case facts" block included in each prompt, outside summarized history
- [5.1-S2] Extracting and persisting structured issue data (order IDs, amounts, statuses) into a separate context layer for multi-issue sessions
Appendix items it also serves: [APP-I16] Context window optimization: Trimming verbose tool outputs, structured fact extraction, po…; [APP-T12] Context window management — Token budgets, progressive summarization, lost-in-the-middle e…

Key Distinction to weave into `tested` / `remember`:
```
KD #21 — Persistent case-facts block vs Summarization improvements
For preserving precise numbers/amounts across long conversations:
- ✅ Extract transactional facts into a case-facts block outside summarized history (survives compression)
- ❌ Revise summarization prompt to preserve numbers (still relies on perfect execution)
- ❌ Increase summarization threshold (buys time but doesn't fix the fundamental precision loss)

---
```

## D5-02 — Lost in the middle — summary first, explicit section headers
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Models read the start and end of long input reliably; put key findings at the top and label the sections.
Official-guide bullets this card must cover:
- [5.1-K2] The "lost in the middle" effect: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections
- [5.1-S4] Placing key findings summaries at the beginning of aggregated inputs and organizing detailed results with explicit section headers to mitigate position effects
Appendix items it also serves: [APP-I16] Context window optimization: Trimming verbose tool outputs, structured fact extraction, po…; [APP-T12] Context window management — Token budgets, progressive summarization, lost-in-the-middle e…

Key Distinction to weave into `tested` / `remember`:
```
KD #20 — "Lost in the middle" mitigation
- ✅ Key-findings summary at the start + explicit section headings
- ❌ Rotation of which agent's output appears first (doesn't fix the attention pattern)
- ❌ Summarize everything to under 20K (may lose critical information)

---
```

## D5-03 — Trim tool output before it lands in context
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Forty fields per order lookup when five matter; keep only the relevant fields.
Official-guide bullets this card must cover:
- [5.1-K3] How tool results accumulate in context and consume tokens disproportionately to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant)
- [5.1-S3] Trimming verbose tool outputs to only relevant fields before they accumulate in context (e.g., keeping only return-relevant fields from order lookups)
Appendix items it also serves: [APP-I16] Context window optimization: Trimming verbose tool outputs, structured fact extraction, po…; [APP-T12] Context window management — Token budgets, progressive summarization, lost-in-the-middle e…

## D5-04 — The API is stateless — send the full history every turn
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Claude remembers nothing between requests; coherence comes from the messages array you send.
Official-guide bullets this card must cover:
- [5.1-K4] The importance of passing complete conversation history in subsequent API requests to maintain conversational coherence

Key Distinction to weave into `tested` / `remember`:
```
KD #25 — Stateless API memory pattern
Claude has **no server-side memory**. The only way Claude "remembers" prior conversation is because the application includes prior messages in the `messages[]` array.

**Exam trap:** "Claude needs a `session_id` parameter" → False. The API is stateless; the application manages conversation state.

**Exam trap:** "Claude needs a vector database to maintain conversation memory" → False. Simple conversation memory is the `messages[]` array. Vector databases are for retrieval over long histories (months), not standard multi-turn conversations.

---
```

## D5-05 — Subagents return structured, metadata-rich output — not prose
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Key facts, citations, dates, relevance scores instead of verbose reasoning, so downstream agents with small budgets can synthesise accurately.
Official-guide bullets this card must cover:
- [5.1-S5] Requiring subagents to include metadata (dates, source locations, methodological context) in structured outputs to support accurate downstream synthesis
- [5.1-S6] Modifying upstream agents to return structured data (key facts, citations, relevance scores) instead of verbose content and reasoning chains when downstream agents have limited context budgets

## D5-06 — Behavioural drift is diluted instructions, not overflow
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): At 2,500 tokens the window is not full; the system prompt's influence is being diluted by accumulated responses.
Note: Practice-test distinction adjacent to TS 5.1.

Key Distinction to weave into `tested` / `remember`:
```
KD #23 — Behavioral drift: accumulated responses vs Context window overflow
When system prompt behavior degrades across turns at short token counts (2,500 tokens, 7 turns):
- Root cause: ✅ Accumulated assistant responses dilute system prompt influence
- Not: context window overflow (impossible at 2,500 tokens)
- Not: system prompt "only applies to the first turn" (false — it's included in every request)

---
```

## D5-07 — Months of history need retrieval, not summarisation
Home task statement: TS 5.1 — Manage conversation context to preserve critical information across long interactions
Gist (the concept, to be written as one flat sentence): Specific recall over 85K tokens of past conversation calls for semantic retrieval; progressive summarisation compresses conclusions into abstractions.
Note: Practice-test distinction adjacent to TS 5.1.

Key Distinction to weave into `tested` / `remember`:
```
KD #24 — Semantic retrieval vs Progressive summarization for long-term recall
For specific recall from months of conversation history (85K tokens):
- ✅ Semantic embeddings with retrieval of relevant exchanges
- ❌ Progressive summarization (compresses specific conclusions into abstractions that can't be recalled precisely)

---
```

## D5-08 — Escalation triggers: human requested, policy gap, no progress
Home task statement: TS 5.2 — Design effective escalation and ambiguity resolution patterns
Gist (the concept, to be written as one flat sentence): Escalate when the customer asks for a human, when policy is silent or ambiguous, or when the agent cannot progress — not merely when the case is complex.
Official-guide bullets this card must cover:
- [5.2-K1] Appropriate escalation triggers: customer requests for a human, policy exceptions/gaps (not just complex cases), and inability to make meaningful progress
- [5.2-S4] Escalating when policy is ambiguous or silent on the customer's specific request (e.g., competitor price matching when policy only addresses own-site adjustments)
Appendix items it also serves: [APP-I8] Escalation decision-making: Explicit criteria, honoring customer preferences, policy gap i…

## D5-09 — Explicit criteria plus few-shot; never sentiment or self-confidence
Home task statement: TS 5.2 — Design effective escalation and ambiguity resolution patterns
Gist (the concept, to be written as one flat sentence): Escalation calibration comes from written criteria with examples; sentiment scores and self-reported confidence do not track case complexity.
Official-guide bullets this card must cover:
- [5.2-K3] Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity
- [5.2-S1] Adding explicit escalation criteria with few-shot examples to the system prompt demonstrating when to escalate versus resolve autonomously
Appendix items it also serves: [APP-I8] Escalation decision-making: Explicit criteria, honoring customer preferences, policy gap i…

## D5-10 — Asked for a human: escalate now. Frustrated: acknowledge and offer
Home task statement: TS 5.2 — Design effective escalation and ambiguity resolution patterns
Gist (the concept, to be written as one flat sentence): An explicit request is honoured immediately without investigation; frustration on a solvable issue gets acknowledgement plus an offer, escalating only if the customer insists.
Official-guide bullets this card must cover:
- [5.2-K2] The distinction between escalating immediately when a customer explicitly demands it versus offering to resolve when the issue is straightforward
- [5.2-S2] Honoring explicit customer requests for human agents immediately without first attempting investigation
- [5.2-S3] Acknowledging frustration while offering resolution when the issue is within the agent's capability, escalating only if the customer reiterates their preference
Appendix items it also serves: [APP-I8] Escalation decision-making: Explicit criteria, honoring customer preferences, policy gap i…

## D5-11 — Two customer matches — ask for one more identifier
Home task statement: TS 5.2 — Design effective escalation and ambiguity resolution patterns
Gist (the concept, to be written as one flat sentence): Never pick a match by heuristic; request an additional identifier.
Official-guide bullets this card must cover:
- [5.2-K4] How multiple customer matches require clarification (requesting additional identifiers) rather than heuristic selection
- [5.2-S5] Instructing the agent to ask for additional identifiers when tool results return multiple matches, rather than selecting based on heuristics

## D5-12 — State reasonable assumptions and proceed; do not fire off four questions
Home task statement: TS 5.2 — Design effective escalation and ambiguity resolution patterns
Gist (the concept, to be written as one flat sentence): For a vague request, proceed with stated assumptions and invite correction; a wall of clarifying questions drives abandonment, and silent defaults confuse.
Note: Practice-test distinction adjacent to TS 5.2 (ambiguity resolution).

Key Distinction to weave into `tested` / `remember`:
```
KD #19 — State explicit assumptions vs Ask multiple clarifying questions
For vague user requests:
- ✅ Proceed with stated reasonable assumptions, invite corrections (eliminates abandonment)
- ❌ Ask 4+ clarifying questions (causes 35–40% abandonment rate)
- ❌ Use hidden defaults without stating them (user confused when response doesn't match intent)

---
```

## D5-13 — Structured error context lets the coordinator recover
Home task statement: TS 5.3 — Implement error propagation strategies across multi-agent systems
Gist (the concept, to be written as one flat sentence): Failure type, attempted query, partial results and alternatives; a generic "search unavailable", a silent empty success, or killing the whole workflow are all anti-patterns.
Official-guide bullets this card must cover:
- [5.3-K1] Structured error context (failure type, attempted query, partial results, alternative approaches) as enabling intelligent coordinator recovery decisions
- [5.3-K3] Why generic error statuses ("search unavailable") hide valuable context from the coordinator
- [5.3-K4] Why silently suppressing errors (returning empty results as success) or terminating entire workflows on single failures are both anti-patterns
- [5.3-S1] Returning structured error context including failure type, what was attempted, partial results, and potential alternatives to enable coordinator recovery
Appendix items it also serves: [APP-I7] Error handling and propagation: Structured error responses, transient vs business vs permi…

Key Distinction to weave into `tested` / `remember`:
```
KD #8 — Structured error context vs Generic failure status
| | Structured error context | Generic "search unavailable" |
|---|---|---|
| Includes | Failure type + attempted query + partial results + alternatives | Only: "failed" |
| Enables | Intelligent coordinator recovery (retry with modified query? continue partial?) | Only: retry or abort |
| Correct choice | ✅ Always | ❌ Never return generic status |

---
```

## D5-14 — Access failure is not an empty result
Home task statement: TS 5.3 — Implement error propagation strategies across multi-agent systems
Gist (the concept, to be written as one flat sentence): A timeout needs a retry decision; zero matches is a successful query — report them differently.
Also serves TS 2.2.
Official-guide bullets this card must cover:
- [5.3-K2] The distinction between access failures (timeouts needing retry decisions) and valid empty results (successful queries with no matches)
- [5.3-S2] Distinguishing access failures from valid empty results in error reporting so the coordinator can make appropriate decisions
- [2.2-S4] Distinguishing between access failures (needing retry decisions) and valid empty results (representing successful queries with no matches)

Key Distinction to weave into `tested` / `remember`:
```
KD #9 — Transient vs Permanent errors (MCP tool design)
| | Transient (timeout, network) | Permanent (syntax error, not found) |
|---|---|---|
| Retry? | ✅ Yes, with backoff | ❌ No — will always fail |
| Handle where? | Inside the tool before surfacing | Immediately return error with details |
| "0 results" | Valid result (NOT an error) | — |
| Timeout | Access failure (needs coordinator decision) | — |

**Exam trap:** "0 results" and "timeout" look similar but require completely different responses. Distinguish them explicitly.

---
```

## D5-15 — Recover locally first; propagate only what you could not fix, with what you tried
Home task statement: TS 5.3 — Implement error propagation strategies across multi-agent systems
Gist (the concept, to be written as one flat sentence): Subagents retry transient failures themselves and escalate the rest with partial results and the attempts made.
Also serves TS 2.2.
Official-guide bullets this card must cover:
- [5.3-S3] Having subagents implement local recovery for transient failures and only propagate errors they cannot resolve, including what was attempted and partial results
- [2.2-S3] Implementing local error recovery within subagents for transient failures, propagating to the coordinator only errors that cannot be resolved locally along with partial results and what was attempted
Appendix items it also serves: [APP-I7] Error handling and propagation: Structured error responses, transient vs business vs permi…

## D5-16 — Coverage annotations in the synthesis
Home task statement: TS 5.3 — Implement error propagation strategies across multi-agent systems
Gist (the concept, to be written as one flat sentence): Mark which findings are well supported and which topic areas have gaps because a source was unavailable.
Official-guide bullets this card must cover:
- [5.3-S4] Structuring synthesis output with coverage annotations indicating which findings are well-supported versus which topic areas have gaps due to unavailable sources
Appendix items it also serves: [APP-I18] Information provenance: Claim-source mappings, temporal data handling, conflict annotation…

## D5-17 — Context degradation in long sessions
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): The model starts giving inconsistent answers and citing "typical patterns" instead of the classes it found earlier.
Official-guide bullets this card must cover:
- [5.4-K1] Context degradation in extended sessions: models start giving inconsistent answers and referencing "typical patterns" rather than specific classes discovered earlier

## D5-18 — Scratchpad files persist findings across context boundaries
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): Agents write key findings to a file and read it back for later questions.
Official-guide bullets this card must cover:
- [5.4-K2] The role of scratchpad files for persisting key findings across context boundaries
- [5.4-S2] Having agents maintain scratchpad files recording key findings, referencing them for subsequent questions to counteract context degradation
Appendix items it also serves: [APP-T12] Context window management — Token budgets, progressive summarization, lost-in-the-middle e…

## D5-19 — Delegate verbose exploration; the main agent keeps the high-level picture
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): Spawn subagents for "find all test files" or "trace the refund flow" while the main agent coordinates.
Official-guide bullets this card must cover:
- [5.4-K3] Subagent delegation for isolating verbose exploration output while the main agent coordinates high-level understanding
- [5.4-S1] Spawning subagents to investigate specific questions (e.g., "find all test files," "trace refund flow dependencies") while the main agent preserves high-level coordination

Key Distinction to weave into `tested` / `remember`:
```
KD #22 — Subagent isolation for discovery vs Main-session discovery
For verbose discovery that would exhaust main context:
- ✅ Explore subagent: isolates verbose output, returns concise summary to main session
- ❌ Use `/compact` mid-task (loses precision needed for implementation phase)

---
```

## D5-20 — Summarise a phase before spawning the next
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): Inject the previous phase's key findings into the next phase's initial context.
Official-guide bullets this card must cover:
- [5.4-S3] Summarizing key findings from one exploration phase before spawning sub-agents for the next phase, injecting summaries into initial context

## D5-21 — Crash recovery: state exports plus a manifest
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): Each agent writes state to a known location; on resume the coordinator loads the manifest and injects it into prompts.
Official-guide bullets this card must cover:
- [5.4-K4] Structured state persistence for crash recovery: each agent exports state to a known location, and the coordinator loads a manifest on resume
- [5.4-S4] Designing crash recovery using structured agent state exports (manifests) that the coordinator loads on resume and injects into agent prompts
Appendix items it also serves: [APP-I3] Subagent context management: Explicit context passing, structured state persistence, crash…

## D5-22 — /compact when discovery output fills the window
Home task statement: TS 5.4 — Manage context effectively in large codebase exploration
Gist (the concept, to be written as one flat sentence): Reduce context usage mid-session; note that compaction loses precision, so isolate discovery first where you can.
Official-guide bullets this card must cover:
- [5.4-S5] Using /compact to reduce context usage during extended exploration sessions when context fills with verbose discovery output
Appendix items it also serves: [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

Key Distinction to weave into `tested` / `remember`:
```
KD #22 — Subagent isolation for discovery vs Main-session discovery
For verbose discovery that would exhaust main context:
- ✅ Explore subagent: isolates verbose output, returns concise summary to main session
- ❌ Use `/compact` mid-task (loses precision needed for implementation phase)

---
```

## D5-23 — 97% overall can hide a bad segment — measure by document type and field
Home task statement: TS 5.5 — Design human review workflows and confidence calibration
Gist (the concept, to be written as one flat sentence): Aggregate accuracy masks weak document types or fields; verify every segment before automating high-confidence extractions.
Official-guide bullets this card must cover:
- [5.5-K1] The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields
- [5.5-K4] The importance of validating accuracy by document type and field segment before automating high-confidence extractions
- [5.5-S2] Analyzing accuracy by document type and field to verify consistent performance across all segments before reducing human review
Appendix items it also serves: [APP-I17] Human review workflows: Confidence calibration, stratified sampling, accuracy segmentation…

## D5-24 — Stratified random sampling of high-confidence output
Home task statement: TS 5.5 — Design human review workflows and confidence calibration
Gist (the concept, to be written as one flat sentence): Keep sampling the confident extractions to measure error rate and catch novel patterns.
Official-guide bullets this card must cover:
- [5.5-K2] Stratified random sampling for measuring error rates in high-confidence extractions and detecting novel error patterns
- [5.5-S1] Implementing stratified random sampling of high-confidence extractions for ongoing error rate measurement and novel pattern detection
Appendix items it also serves: [APP-I17] Human review workflows: Confidence calibration, stratified sampling, accuracy segmentation…; [APP-T14] Confidence scoring — Field-level confidence, calibration with labeled validation sets, str…

## D5-25 — Field-level confidence, calibrated on labeled data, routes to human review
Home task statement: TS 5.5 — Design human review workflows and confidence calibration
Gist (the concept, to be written as one flat sentence): Have the model output confidence per field, calibrate thresholds on a labeled set, and send low-confidence or contradictory cases to reviewers.
Official-guide bullets this card must cover:
- [5.5-K3] Field-level confidence scores calibrated using labeled validation sets for routing review attention
- [5.5-S3] Having models output field-level confidence scores, then calibrating review thresholds using labeled validation sets
- [5.5-S4] Routing extractions with low model confidence or ambiguous/contradictory source documents to human review, prioritizing limited reviewer capacity
Appendix items it also serves: [APP-I17] Human review workflows: Confidence calibration, stratified sampling, accuracy segmentation…; [APP-T14] Confidence scoring — Field-level confidence, calibration with labeled validation sets, str…

## D5-26 — Claim-source mappings survive synthesis
Home task statement: TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis
Gist (the concept, to be written as one flat sentence): Subagents output claim, excerpt, source URL/document; the synthesis agent preserves and merges the mapping instead of compressing it away.
Official-guide bullets this card must cover:
- [5.6-K1] How source attribution is lost during summarization steps when findings are compressed without preserving claim-source mappings
- [5.6-K2] The importance of structured claim-source mappings that the synthesis agent must preserve and merge when combining findings
- [5.6-S1] Requiring subagents to output structured claim-source mappings (source URLs, document names, relevant excerpts) that downstream agents preserve through synthesis
Appendix items it also serves: [APP-I18] Information provenance: Claim-source mappings, temporal data handling, conflict annotation…

## D5-27 — Conflicting figures: keep both, attribute both, let the coordinator reconcile
Home task statement: TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis
Gist (the concept, to be written as one flat sentence): Do not pick a value; annotate the conflict with sources.
Official-guide bullets this card must cover:
- [5.6-K3] How to handle conflicting statistics from credible sources: annotating conflicts with source attribution rather than arbitrarily selecting one value
- [5.6-S3] Completing document analysis with conflicting values included and explicitly annotated, letting the coordinator decide how to reconcile before passing to synthesis
Appendix items it also serves: [APP-I18] Information provenance: Claim-source mappings, temporal data handling, conflict annotation…

## D5-28 — Well-established vs contested findings in separate sections
Home task statement: TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis
Gist (the concept, to be written as one flat sentence): Keep the sources' own characterisations and methodological context.
Official-guide bullets this card must cover:
- [5.6-S2] Structuring reports with explicit sections distinguishing well-established findings from contested ones, preserving original source characterizations and methodological context

## D5-29 — Dates in every structured output
Home task statement: TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis
Gist (the concept, to be written as one flat sentence): Publication or collection dates stop temporal differences being read as contradictions.
Official-guide bullets this card must cover:
- [5.6-K4] Temporal data: requiring publication/collection dates in structured outputs to prevent temporal differences from being misinterpreted as contradictions
- [5.6-S4] Requiring subagents to include publication or data collection dates in structured outputs to enable correct temporal interpretation
Appendix items it also serves: [APP-I18] Information provenance: Claim-source mappings, temporal data handling, conflict annotation…

## D5-30 — Render each content type in its natural form
Home task statement: TS 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis
Gist (the concept, to be written as one flat sentence): Financial data as tables, news as prose, technical findings as lists.
Official-guide bullets this card must cover:
- [5.6-S5] Rendering different content types appropriately in synthesis outputs—financial data as tables, news as prose, technical findings as structured lists—rather than converting everything to a uniform format
