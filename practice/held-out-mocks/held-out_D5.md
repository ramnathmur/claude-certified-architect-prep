# Held-Out Mock Bank — Domain 5: Context Management & Reliability (15%)

> HELD-OUT INTEGRITY: original questions only; no reuse of practice-bank/checkpoint/guide-sample/teaching stems. For Mock A / Mock B only. Scenario 8 excluded.

## Mock A — Domain 5 (9 questions)

### A-D5-01 · Scenario: 7 (Conversational AI Architecture) · Type: Scenario/anti-pattern · Difficulty: Medium
A travel-concierge assistant runs sessions of 40+ turns. Your team assembles each request as one giant block: the system instructions, then the entire turn-by-turn history, then the tool catalog, then every tool result, and finally — buried two-thirds of the way down — the traveler's hard constraints ("wheelchair-accessible rooms only; no red-eye flights"). QA reports that around turn 25 the assistant starts booking inaccessible rooms and red-eye flights, even though the constraints are still physically present in the window. What is the primary design flaw?

A. The window has overflowed its token capacity, so the constraints were silently truncated by the API.
B. The constraints were placed in the low-salience middle region of a long input, where models attend least reliably; they should be anchored at the start or end of the request.
C. The tool catalog must always be the last block in the request, and placing it before the constraints corrupted tool selection.
D. Hard constraints cannot be enforced through context at all and must be moved into a PreToolUse hook before anything else is tried.

### A-D5-02 · Scenario: — · Type: Concept/application · Difficulty: Medium
An agent's `search_flights` tool returns a JSON object with 52 fields per flight (fare-class fee breakdowns, aircraft tail numbers, gate history, codeshare metadata, etc.), but the agent only ever needs `flight_number`, `depart_time`, `arrive_time`, `price`, and `seats_left`. Across a long booking session this is a recurring tax on the window. Which mechanism most directly and deterministically removes the irrelevant fields *before the model consumes the result*?

A. A `PostToolUse` hook that trims each tool result down to the five relevant fields.
B. A `PreToolUse` hook that rewrites the outgoing `search_flights` call to request fewer fields.
C. A system-prompt instruction telling the model to ignore fields it does not need.
D. Raising the compaction trigger threshold so the verbose results are summarized sooner.

### A-D5-03 · Scenario: 1 (Customer Support Agent) · Type: Scenario/anti-pattern · Difficulty: Medium
A support agent handles a warranty dispute over many turns. Your context strategy folds older turns into a running prose summary as the window fills. To protect the facts that matter, a teammate proposes: "Let's just write a better summarization prompt that says 'always keep all numbers and dates exactly.'" Several sessions later the agent still reports the claim amount as "around three hundred dollars" instead of the stated $327.40. What is the more robust fix, and why does the teammate's approach keep failing?

A. Increase the summary's length budget so more of the original wording survives compression.
B. Maintain a persistent "case facts" block (claim amount, SKU, purchase date, ticket ID) carried in every prompt *outside* the summarized history; a summarization prompt is probabilistic and still degrades exact values, while the facts block keeps them verbatim by construction.
C. Disable summarization entirely and rely on the full window, since the model attends to everything equally up to the token limit.
D. Move the claim amount into the tool definitions so it is sent on every turn as part of the stable prefix.

### A-D5-04 · Scenario: — · Type: Scenario/anti-pattern · Difficulty: Hard
A document-extraction pipeline reports 96% aggregate field-level accuracy on a labeled validation set, so the team ships full auto-processing with no human review. Within a month, finance flags that *handwritten* invoices — about 6% of volume — are wrong roughly 38% of the time, while typed invoices are near-perfect. The aggregate number never surfaced this. Which practice would have caught the problem before it reached production?

A. Raising the field-level confidence threshold uniformly across all document types.
B. Stratified sampling that measures accuracy broken out by document type and field, rather than relying on a single pooled accuracy figure.
C. Switching to `tool_use` with a strict JSON schema to guarantee well-formed output.
D. Increasing the validation-set size so the aggregate accuracy estimate has tighter confidence intervals.

### A-D5-05 · Scenario: — · Type: Recall · Difficulty: Easy
In the CALM framework for context engineering (Compress, Anchor, Layer, Monitor), what does the **Anchor** step refer to?

A. Pinning the `cache_control` breakpoint to the first user message so the cache never expires.
B. Keeping critical, must-not-drift information (key facts, constraints, identifiers) reliably present and positioned so it survives summarization and stays salient.
C. Hard-capping the conversation to a fixed number of turns to anchor the token budget.
D. Locking the model version for a session so behavior does not change mid-conversation.

### A-D5-06 · Scenario: 7 (Conversational AI Architecture) · Type: Scenario/anti-pattern · Difficulty: Medium
A long-running coding assistant spends many turns mapping an unfamiliar repo (tracing imports, locating the auth middleware, noting an external API's rate limit). Twenty turns later the context has degraded and it re-runs the same discovery from scratch, wasting turns and re-reading the same 15 files. Which approach best prevents this *and* keeps the coordinator's own window lean?

A. Increase `max_tokens` so the assistant has more room to remember its earlier discovery.
B. Have the assistant write key findings to a scratchpad file during discovery and consult that file later (or in a new session) instead of re-running discovery; delegate bulk file-reading to a subagent that returns a short summary so the coordinator keeps one line, not 15 files.
C. Disable compaction so none of the earlier discovery is ever summarized away.
D. Lower the compaction trigger threshold so summaries are generated more frequently and stay fresh.

### A-D5-07 · Scenario: — · Type: Scenario/anti-pattern · Difficulty: Hard
A research-synthesis agent merges findings from several sources. One source (dated 2022) says the segment is "12% of the market"; another (dated 2025) says "19%." During summarization the agent collapses these into a single line: "Sources disagree on market share (12% vs 19%) — data is unreliable." A reviewer flags this as a reasoning failure. What is the correct handling?

A. Keep only the most recent figure (19%) since newer data supersedes older data, and drop the 2022 number.
B. Average the two values and report "~15.5%" with a note that sources varied.
C. Preserve both figures with their full attribution including publication dates, so a 2022→2025 increase reads as plausible growth rather than a contradiction.
D. Flag the entire claim as unverifiable and exclude it from the synthesis to avoid presenting conflicting numbers.

### A-D5-08 · Scenario: — · Type: Concept/application · Difficulty: Medium
You are building a multi-source competitive-intelligence report. Stakeholders later challenge specific numbers and ask "where did this come from?" Which data structure best preserves the ability to defend each claim through aggregation and summarization?

A. A flat markdown bullet list of all findings, ordered by importance.
B. A structured claim→source mapping where each claim carries its `source_url`, `publication_date`, and a `confidence` value.
C. A single confidence score for the whole report, computed as the average of all source reliabilities.
D. The full raw text of every source concatenated into an appendix, so any claim can be traced manually.

### A-D5-09 · Scenario: 1 (Customer Support Agent) · Type: Scenario/anti-pattern · Difficulty: Medium
A returning customer reopens a chat that was last active eight days ago. To restore continuity, an engineer wants to prepend the exact account-balance and open-ticket tool results captured at the end of the prior session, verbatim, then continue. Why is this the wrong move for a support agent, and what should happen instead?

A. It is correct — replaying the prior results guarantees continuity and avoids redundant tool calls.
B. The embedded results are now stale (balance and ticket status change over days); open with a structured summary of prior context and fetch fresh live state at resume time.
C. Tool results can never be re-sent across sessions for security reasons, so the conversation must start fully blank with no carried context.
D. The only issue is cost; replay the old results but wrap them in a cache breakpoint so they are not re-billed.

## Mock B — Domain 5 (9 questions)

### B-D5-01 · Scenario: — · Type: Recall · Difficulty: Easy
Why must the *entire* conversation history (plus system prompt, tool definitions, and prior tool results) be re-sent on every Messages API request in a multi-turn agent?

A. Because the API charges less when the same tokens are re-sent, due to automatic deduplication.
B. Because the model is stateless across calls — it retains no memory between requests, so anything it must "remember" has to be present in the current request.
C. Because re-sending history is required to keep the prompt cache warm; omitting it would reset the cache.
D. Because the `session_id` only stores metadata, not content, and must be rehydrated from the client each turn.

### B-D5-02 · Scenario: 7 (Conversational AI Architecture) · Type: Scenario/anti-pattern · Difficulty: Hard
A multi-agent research system writes each subagent's state to `agent-state/{agent-id}.json` and a `agent-state/manifest.json` recording per-agent `status`, `queries_executed`, `results_count`, and `gaps`. Midway through a long run the orchestrator process crashes. On restart, what does this design buy you that an in-memory-only approach does not?

A. Nothing meaningful — the crashed run must restart from zero either way, since LLM calls cannot be resumed.
B. Crash recovery: the coordinator reloads the manifest, sees which agents completed and which have open `gaps`, and resumes only the unfinished work instead of repeating completed research.
C. It guarantees the subagents inherit the coordinator's full conversation history automatically on resume.
D. It eliminates the need to pass context into subagents, because each subagent reads the others' state files directly.

### B-D5-03 · Scenario: — · Type: Scenario/anti-pattern · Difficulty: Medium
An engineer formats a long aggregated input for a synthesis step as: detailed raw findings first (the bulk), then the key takeaways, then a one-line restatement of the task at the very bottom. Outputs frequently miss the most important findings even though they are present. Applying position-aware input design, how should the input be reorganized?

A. Put the KEY FINDINGS at the top, the detailed/supporting results in the middle, and the ACTION ITEMS / task at the end — exploiting the reliably-attended start and end regions.
B. Sort all content strictly alphabetically so the model can navigate it predictably.
C. Move everything into a single dense paragraph to reduce token count and avoid the middle entirely.
D. Place the task statement in the exact middle so it sits equidistant from both ends.

### B-D5-04 · Scenario: 1 (Customer Support Agent) · Type: Concept/application · Difficulty: Medium
A support agent's `lookup_subscription` MCP tool returns 30+ fields, but only `plan_tier`, `renewal_date`, and `payment_status` are ever used downstream. The team wants to keep the window lean *and* normalize a Unix-timestamp field into ISO 8601 at the same time, for every call, with a 100% guarantee rather than relying on the model to do it. Which approach fits?

A. A `PostToolUse` hook that both trims `lookup_subscription` results to the three needed fields and converts the timestamp to ISO 8601 before the model sees the result.
B. Few-shot examples in the system prompt showing the model how to ignore extra fields and reformat dates.
C. A `tool_choice: "any"` setting to force the model to call the tool and return clean output.
D. Raising the model's `max_tokens` so the verbose result fits more comfortably.

### B-D5-05 · Scenario: — · Type: Concept/application · Difficulty: Medium
A field-level extraction system outputs a confidence score per extracted field. The team wants to decide, per field, whether to auto-process or route to a human. What is the correct way to set the routing thresholds?

A. Use a single fixed threshold of 0.9 for all fields, since 90% is the industry default.
B. Calibrate thresholds against a labeled validation set per field, routing high-confidence + stably-accurate fields to automation and low-confidence or ambiguous ones to human review.
C. Let the model choose its own thresholds at runtime based on how certain it feels about the document overall.
D. Route purely on the *length* of the source text, since longer sources are more reliable.

### B-D5-06 · Scenario: 7 (Conversational AI Architecture) · Type: Scenario/anti-pattern · Difficulty: Medium
A coordinator spawns subagents to research subtopics in parallel. To "give them everything they might need," it pastes the full running conversation (≈120K tokens of prior turns and raw tool dumps) into each subagent prompt. The subagents are slow, expensive, and frequently drift off their assigned subtopic. What is the corrected pattern for subagent context budgets?

A. Send each subagent a minimal, scoped prompt — only the context relevant to its subtopic plus a required structured-output format — and limit its `allowed_tools`; subagents do not inherit the coordinator's history and should not be flooded with it.
B. Keep sending the full history but compress it with a sliding window first, so each subagent gets the most recent 40K tokens.
C. Give every subagent the full window but raise `max_tokens` so they have room to process it.
D. Have each subagent write the full history to a shared file and read it back, to avoid passing it in the prompt.

### B-D5-07 · Scenario: — · Type: Scenario/anti-pattern · Difficulty: Medium
A long investigation session has filled the window with verbose tool output. An engineer runs `/compact` and is satisfied. Later the agent quotes a config value as "roughly 100 requests per minute" when the actual documented limit it had read earlier was exactly 120 req/min. What does this illustrate about progressive summarization, and what guards against it?

A. Compaction is broken and should never be used; keep the entire raw history instead.
B. Progressive summarization reliably preserves all numeric values, so the error must be a model hallucination unrelated to compaction.
C. Summarization predictably degrades exact numbers, dates, and thresholds into vague approximations; protect such values by keeping them in a persistent facts block or a fact/retrieval store outside the summarized history.
D. The fix is to compact more aggressively so fewer raw tokens remain to confuse the model.

### B-D5-08 · Scenario: 1 (Customer Support Agent) · Type: Scenario/anti-pattern · Difficulty: Hard
A billing-support agent caches a stable prefix — tool definitions plus a 25K-token policy KB that is identical every turn. Output rendering is also a concern: financial breakdowns are being returned as flowing prose, which customers misread. Two separate decisions are on the table. Which pairing is correct?

A. Place `cache_control` on the per-turn customer message so the newest content is cached; render all content as prose for a conversational feel.
B. Place `cache_control` after the stable prefix (tool defs + KB) and before the variable per-turn content; render financial/tabular data as tables and narrative analysis as prose, matching format to content type.
C. Place `cache_control` before the tool definitions so the whole request is cached; render everything as a single table for consistency.
D. Skip caching because the KB changes the prefix each turn anyway; render financial data as prose to keep responses short.

### B-D5-09 · Scenario: — · Type: Recall · Difficulty: Easy
Which of the following is a genuine context-window risk that architects must design around, as opposed to a non-issue?

A. Tool results accumulate over a session — every call appends its full output, so verbose results that return far more fields than needed steadily crowd the window.
B. The system prompt is automatically dropped once history exceeds half the window, so it must be re-sent as a user message.
C. Prior tool results are excluded from the token count, so they can be sent freely without budget impact.
D. The model attends to all positions in a long input equally, so ordering of content within the window does not matter.

## Answer Key — Domain 5

### Mock A
- **A-D5-01** — Correct: B. The constraints sit in the low-salience middle of a long input (lost-in-the-middle); they should be anchored at the start or end. Why others fail: A — the constraints are stated to still be physically present, so this is salience, not truncation/overflow; C — there is no rule that the tool catalog must be last, and that is not the cause; D — a PreToolUse hook is a valid hard-guarantee in general, but the question is about why context placement fails, and constraints absolutely *can* be carried in context if positioned well. Sub-domain: D5.1.
- **A-D5-02** — Correct: A. A `PostToolUse` hook intercepts the tool result before the model consumes it and trims to the needed fields, deterministically. Why others fail: B — a PreToolUse hook acts on the outgoing call, and the scenario is about a fixed third-party-shaped result; trimming the *result* is the PostToolUse job; C — a prompt instruction is probabilistic and the verbose fields still occupy the window; D — compaction summarizes history later and does not surgically drop per-result fields, and it acts after accumulation, not before consumption. Sub-domain: D5.2.
- **A-D5-03** — Correct: B. A persistent "case facts" block carried outside the summarized history keeps exact values verbatim by construction; a "keep all numbers" summarization prompt is still probabilistic and degrades exact values. Why others fail: A — a longer summary still summarizes and still drifts; C — capacity is not attention and disabling summarization eventually overflows besides not fixing salience; D — tool definitions are not a place to stuff per-case mutable facts, and that would also bust caching and misuse the schema. Sub-domain: D5.2.
- **A-D5-04** — Correct: B. Stratified sampling broken out by document type and field surfaces per-type rot (handwritten invoices) that a pooled aggregate hides. Why others fail: A — a uniform threshold change does not reveal which subgroup is failing; C — strict JSON schema fixes syntax, not the semantic accuracy gap on handwritten inputs; D — a larger validation set tightens the *aggregate* estimate but still pools across types, so it still masks the subgroup. Sub-domain: D5.4.
- **A-D5-05** — Correct: B. Anchor = keeping critical must-not-drift information reliably present and well-positioned so it survives summarization and stays salient. Why others fail: A — that conflates Anchor with cache_control placement; C — turn-capping is the classic "Limit" misreading and is not part of CALM; D — model-version locking is unrelated to the framework. Sub-domain: D5.1.
- **A-D5-06** — Correct: B. A scratchpad file persists key findings across context degradation/new sessions, and delegating bulk reading to a subagent that returns a summary keeps the coordinator's window to one line instead of 15 files. Why others fail: A — `max_tokens` controls output length, not memory of prior discovery; C — disabling compaction overflows the window and still does not survive a new session; D — more frequent compaction loses precision faster and still re-summarizes the same churned content rather than persisting findings. Sub-domain: D5.3.
- **A-D5-07** — Correct: C. Preserve both figures with full attribution including publication dates; a 2022→2025 difference reads as growth, not a contradiction, once dated. Why others fail: A — dropping the older value discards real provenance and the trend signal; B — averaging fabricates a number neither source supports and destroys attribution; D — excluding the claim throws away usable, defensible information. Sub-domain: D5.5.
- **A-D5-08** — Correct: B. A structured claim→source mapping with `source_url`, `publication_date`, and `confidence` keeps every claim defensible through aggregation and summarization. Why others fail: A — a flat bullet list loses the claim-to-source link during summarization; C — one report-level average destroys per-claim attribution; D — a raw appendix preserves text but forces fragile manual tracing and does not bind each claim to its source. Sub-domain: D5.5.
- **A-D5-09** — Correct: B. Embedded results captured days ago are stale; open with a structured summary and fetch fresh live state at resume. Why others fail: A — trusting stale balances/tickets produces wrong answers; C — there is no blanket prohibition, and carrying a structured summary is exactly what you should do; D — the problem is staleness (wrong content), not cost, so caching stale data caches a wrong answer. Sub-domain: D5.1 / returning-users.

### Mock B
- **B-D5-01** — Correct: B. The model is stateless between calls, so everything it must use this turn has to be in this request. Why others fail: A — there is no "re-send discount via deduplication"; caching reduces cost but the content must still be supplied; C — keeping the cache warm is a side benefit, not the reason history is required; D — `session_id` is not the mechanism here (the Messages API is stateless regardless), and content lives in the request, not in server-side session storage. Sub-domain: D5.1.
- **B-D5-02** — Correct: B. Persisting structured state to known locations plus a manifest enables crash recovery — reload the manifest, see completed vs. open gaps, resume only unfinished work. Why others fail: A — the point of persisted state is precisely to avoid restarting from zero; C — state files do not auto-inject the coordinator's history into subagents; D — subagents still need scoped context passed in their prompt, not ad-hoc reads of peers' state. Sub-domain: D5.3.
- **B-D5-03** — Correct: A. Position-aware design puts KEY FINDINGS at the top and ACTION ITEMS/task at the end (the reliably-attended regions), with detail in the middle. Why others fail: B — alphabetical order ignores salience entirely; C — collapsing into one dense paragraph worsens mid-input neglect and loses structure; D — the middle is the *least* reliable position, so placing the task there is the opposite of the fix. Sub-domain: D5.2.
- **B-D5-04** — Correct: A. A `PostToolUse` hook both trims to the three needed fields and normalizes the timestamp before the model consumes the result, deterministically. Why others fail: B — few-shot guidance is probabilistic and still leaves the verbose fields in the window; C — `tool_choice: "any"` forces a tool call but does nothing to trim or reformat results; D — raising `max_tokens` neither trims fields nor normalizes formats. Sub-domain: D5.2.
- **B-D5-05** — Correct: B. Calibrate per-field thresholds against a labeled validation set; automate high-confidence/stably-accurate fields and route low-confidence/ambiguous ones to humans. Why others fail: A — a single fixed 0.9 ignores that calibration differs by field; C — model self-assessed certainty is poorly calibrated and can be confidently wrong; D — source length is not a reliable proxy for extraction accuracy. Sub-domain: D5.4.
- **B-D5-06** — Correct: A. Send each subagent a minimal scoped prompt plus a required structured-output format and limit `allowed_tools`; subagents do not inherit coordinator history and should not be flooded. Why others fail: B — a sliding window still ships large, mostly-irrelevant context and invites drift; C — more room to process irrelevant context does not fix scope drift or cost; D — round-tripping the full history through a file is the same flood by another route. Sub-domain: D5.3.
- **B-D5-07** — Correct: C. Progressive summarization predictably degrades exact numbers/dates/thresholds into approximations; keep such values in a persistent facts block or fact/retrieval store outside the summarized history. Why others fail: A — never compacting overflows the window and is not the prescribed guard; B — summarization does *not* reliably preserve exact numbers, which is the whole risk; D — more aggressive compaction loses *more* precision, not less. Sub-domain: D5.1 / D5.2.
- **B-D5-08** — Correct: B. Put `cache_control` after the stable prefix (tool defs + KB) and before the variable per-turn content; match output format to content type (tables for financial/tabular, prose for narrative). Why others fail: A — caching the changing per-turn message busts the prefix every turn, and all-prose misformats financial data; C — placing the breakpoint before the tool defs does not cache the KB usefully (caching covers a contiguous prefix, and the goal is to cache the *stable* prefix), and one giant table misformats narrative; D — the KB is identical every turn, so it is exactly what *should* be cached, and prose still misformats financial breakdowns. Sub-domain: D5.2 / caching + rendering.
- **B-D5-09** — Correct: A. Tool-result accumulation is a real risk: every call appends its full output and over-broad results crowd the window. Why others fail: B — the system prompt is not auto-dropped at half-window and must not be relocated to a user message; C — tool results *do* count toward the window budget; D — the model does *not* attend equally to all positions, so ordering matters (lost-in-the-middle). Sub-domain: D5.1.
