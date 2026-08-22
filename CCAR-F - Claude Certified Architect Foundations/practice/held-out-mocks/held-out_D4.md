# Held-Out Mock Bank — Domain 4: Prompt Engineering & Structured Output (20%)

> HELD-OUT INTEGRITY: original questions only; no reuse of practice-bank/checkpoint/guide-sample/teaching stems. For Mock A / Mock B only. Scenario 8 excluded.

## Mock A — Domain 4 (12 questions)

### A-D4-01 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Medium
A logistics firm extracts shipment fields from carrier emails. The schema marks `delivery_window` as a single enum: `["morning", "afternoon", "evening"]`. In practice, carriers write things like "anytime after 9pm" or "driver will call ahead." The team finds the model is silently coercing these to the nearest enum value, corrupting the dataset. Which schema change best preserves the unusual inputs without abandoning the enum?

A. Switch `delivery_window` to a free-text string so any phrasing is captured verbatim.
B. Add `minLength` and `maxLength` constraints to the enum so out-of-range phrasings are rejected at decode time.
C. Add an `"other"` member to the enum plus a nullable `delivery_window_detail` string to carry the original phrasing.
D. Make `delivery_window` required so the model is forced to reason harder about which bucket fits.

### A-D4-02 · Scenario: Conversational AI Architecture · Type: Scenario/Anti-pattern · Difficulty: Medium
A travel-booking assistant runs on the Messages API. To reduce token spend, the team sends only the latest user turn plus a one-line server-side note ("user is booking a flight") on each call, relying on a stable `conversation_id` they pass in the request body. Users report the assistant repeatedly re-asks for the departure city it was told moments ago. What is the actual cause and fix?

A. The `conversation_id` must be placed in the `system` parameter; once moved, the API will rehydrate prior turns.
B. The Messages API is stateless and `conversation_id` is not memory; the full prior turn history must be re-sent each request (compress it if needed, but do not drop it).
C. Prompt caching lapsed, dropping the server-held turns; lengthening the cache TTL will retain them.
D. The model's context window is overflowing, so earlier turns are being evicted server-side; a larger-context model fixes it.

### A-D4-03 · Scenario: — · Type: Recall · Difficulty: Easy
Which single `tool_choice` setting guarantees that the model emits a call to one *specific* tool on a given turn, rather than choosing among several or possibly replying in prose?

A. `{"type": "auto"}`
B. `{"type": "any"}`
C. `{"type": "tool", "name": "<that tool>"}`
D. `{"type": "none"}`

### A-D4-04 · Scenario: Structured Data Extraction · Type: Concept/Application · Difficulty: Medium
An expense system uses strict tool-use with a JSON schema, so every response is well-formed and every required field is present. A quarterly audit nonetheless finds receipts where the `tax_amount` exceeds the `subtotal`, and a few where the `merchant_country` does not match the currency. The lead concludes the JSON-schema approach is unreliable. What is the correct diagnosis?

A. The schema must add numeric `maximum` bounds so the decoder rejects a tax larger than the subtotal.
B. Constrained decoding is producing bad values; disable strict tool use and validate the prose output instead.
C. Schema enforcement guarantees syntax and structure, not semantics; cross-field business rules (tax ≤ subtotal, currency↔country) require a separate validation layer.
D. The fields should be merged into one composite string so the model reasons about them jointly.

### A-D4-05 · Scenario: Claude Code in CI/CD · Type: Scenario/Anti-pattern · Difficulty: Medium
A nightly headless job summarizes the day's merged commits into a changelog and must emit machine-readable JSON for a downstream publisher. The engineer's prompt ends with "Return ONLY valid JSON, no markdown fences, no commentary," and a dead-letter queue catches the runs that still come back wrapped in prose. The team wants to stop the malformed runs at the source. What is the right primary fix?

A. Move the "ONLY valid JSON" instruction to the top of the prompt and repeat it at the end to raise its salience.
B. Constrain generation with the structured-outputs feature (a JSON schema via `--json-schema` / `output_config.format`); keep the dead-letter queue only as a fallback.
C. Increase the retry ceiling and add jitter so a malformed run eventually yields parseable text.
D. Prefill the assistant message with `{` so the model is locked into JSON mode.

### A-D4-06 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Hard
A team extracts a patient's `primary_diagnosis_code` from referral letters. The field is `required`. Many letters simply do not state a code. Reviewers notice the model is emitting plausible but fabricated ICD-10 codes for those letters. Beyond making the field nullable/optional, which *additional* prompt-level technique most directly reduces this specific fabrication?

A. Raise the model's reasoning effort to max so it works harder to locate a code.
B. Add few-shot edge-case examples that show a letter with no code mapping to `null` (or an explicit "not stated"), demonstrating that absence is an acceptable answer.
C. Add an `additionalProperties: true` clause so the model can place the code wherever it fits.
D. Lower the temperature to 0 so outputs become deterministic.

### A-D4-07 · Scenario: — · Type: Concept/Application · Difficulty: Hard
You are writing the system prompt for a long-running data-migration agent. Requirement 1: "tune the level of detail in status updates to how technical the operator seems." Requirement 2: "never run a destructive DROP on a table whose name is not on the approved allowlist." How should each be expressed, and why?

A. Both as open principles, so the model adapts fluidly to each situation.
B. Both as rigid conditionals, so neither is left to interpretation.
C. Requirement 1 as a principle (a judgment call); Requirement 2 as a hard conditional bright-line — and note that the destructive guard ultimately belongs in code, not prose, because a prompt only biases behavior.
D. Requirement 1 as a conditional and Requirement 2 as a principle, since detail level is binary and safety is contextual.

### A-D4-08 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Medium
A pipeline extracts purchase-order tables. A validator flags that, on one document, `line_item_count` reported by the model is 7 but the `line_items` array it returned has 9 entries. An engineer wants automated recovery without a human. Which approach is most likely to fix this *specific* error?

A. Resend the identical request up to five times and accept the first response that passes the validator.
B. Resend the source document together with the model's prior extraction and the exact mismatch ("line_item_count=7 but array length=9; recount"), asking it to correct the inconsistency.
C. Switch the call to the Batch API, since batching re-checks arithmetic before returning.
D. Add a `maxItems: 7` constraint so the array can never exceed the stated count.

### A-D4-09 · Scenario: Structured Data Extraction · Type: Concept/Application · Difficulty: Medium
A back-office team must process 80,000 archived contracts into structured summaries. There is no interactive user; the results feed a report due in three days. A junior engineer wants to fire all 80,000 through synchronous calls in a tight loop for speed. What is the strongest argument for the Message Batches API here, and what is its key limitation to plan around?

A. Batch guarantees sub-minute latency per request; the only limitation is that it costs more than synchronous.
B. Batch offers roughly 50% lower cost for this non-interactive bulk workload; plan around its up-to-24-hour processing window (no latency SLA) and the fact that multi-turn tool calling is not supported.
C. Batch is required whenever request volume exceeds 1,000; its limitation is that it cannot return JSON.
D. Batch automatically retries every failed request forever; its limitation is that results arrive in submission order so you must not reorder them.

### A-D4-10 · Scenario: — · Type: Recall · Difficulty: Easy
In the Message Batches API, what is the purpose of the `custom_id` you attach to each request?

A. It sets the priority order in which the batch is processed.
B. It is the join key that links each result back to its originating request, since results need not return in submission order and only the failures can then be resubmitted.
C. It encrypts the request payload for transport.
D. It enables multi-turn tool calling within a single batched request.

### A-D4-11 · Scenario: Conversational AI Architecture · Type: Scenario/Anti-pattern · Difficulty: Hard
A multi-turn cooking assistant is told once at the start of a session: "the user is allergic to peanuts — never suggest a recipe containing them." Forty turns later it recommends a satay sauce. The team blames the model "forgetting." What is the most accurate account, and the most reliable remedy?

A. The allergy line was silently evicted from the window; the only fix is a sliding window that keeps the last N turns.
B. System-prompt instructions lose *salience* (they compete for attention) as the conversation grows; reinforce the critical safety constraint at phase breakpoints and, for a hard guarantee, enforce it as a code-level filter on candidate recipes rather than relying on prose.
C. The model has incurable recency bias; raising reasoning effort is the only mitigation.
D. The instruction was malformed; rewriting it in ALL CAPS with "CRITICAL" makes it a guarantee.

### A-D4-12 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Medium
An extraction prompt must distinguish a *quoted* price ("we may charge up to $400") from a *confirmed* price ("the agreed fee is $400"). A long prose paragraph of instructions describing the distinction keeps producing inconsistent labels. Which intervention most reliably teaches the distinction?

A. Add more adjectives and emphasis ("VERY carefully distinguish quoted from confirmed") to the prose paragraph.
B. Provide a few labeled few-shot examples that contrast a quoted sentence (→ `quoted`) with a confirmed sentence (→ `confirmed`), since examples convey decision logic that prose struggles to pin down.
C. Make both `quoted_price` and `confirmed_price` required so the model always fills them.
D. Move to the Batch API so the model has more time to deliberate on each label.

## Mock B — Domain 4 (12 questions)

### B-D4-01 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Medium
An insurance-claims extractor must capture a `date_of_incident`. Source documents express it as "last Tuesday," "3 days ago," "March," or a full date — and sometimes omit it. The current schema requires a strict `YYYY-MM-DD` string and marks the field required. The team sees both fabricated dates (when absent) and inconsistent formats. Which combination addresses both problems?

A. Keep the field required but add an example showing the model to guess the most probable date.
B. Make the field nullable so absence is representable, and add prompt normalization rules (relative phrases → compute an absolute `YYYY-MM-DD`; bare "March" → flag as imprecise) plus an edge-case example for "no date stated."
C. Relax the format to free text and stop validating dates entirely.
D. Add a numeric `minimum`/`maximum` on the date so out-of-range guesses are rejected by the decoder.

### B-D4-02 · Scenario: — · Type: Concept/Application · Difficulty: Medium
You have three extraction tools — `extract_invoice`, `extract_receipt`, `extract_statement` — and a document that could match any one of them. You require the model to call exactly one of these (never reply in prose) but you do *not* want to dictate which. Which `tool_choice` setting fits?

A. `{"type": "tool", "name": "extract_invoice"}` — name the most common one.
B. `{"type": "auto"}` — let the model decide whether to call a tool at all.
C. `{"type": "any"}` — force a call to *some* tool from the set while letting the model pick the best fit.
D. `{"type": "none"}` — disable tools and parse the prose.

### B-D4-03 · Scenario: Claude Code in CI/CD · Type: Scenario/Anti-pattern · Difficulty: Hard
A CI step uses one Claude session to generate a database-migration script and then, in the *same* session, asks Claude to review that script for data-loss risks. The review almost always returns "looks safe," yet migrations still occasionally drop columns. What design flaw does this expose, and what is the fix?

A. The session ran out of context; compacting the history before the review will surface the risks.
B. A model reviewing its own output in the same context retains its generation reasoning and is less likely to challenge it; run the review in an independent instance (fresh session / separate subagent / separate CI job) without the generation context.
C. The review prompt lacked the word "critical"; emphasizing severity will catch the drops.
D. Reviews are inherently unreliable; only a human can catch data-loss risk, so automated review should be removed.

### B-D4-04 · Scenario: Structured Data Extraction · Type: Concept/Application · Difficulty: Hard
A document-extraction service runs a validate-and-retry loop: extract → validate → on failure, re-prompt with the error. After three retries, a particular field (`policyholder_ssn`) still fails because it is genuinely not present anywhere in the submitted document. The team keeps increasing the retry limit. What is the correct understanding?

A. More retries will eventually succeed because the model just needs more attempts.
B. Retry-with-feedback fixes format, structural, and arithmetic errors, but cannot conjure information that is absent from the source; the field should be returned null and routed to human review or a request for the missing document.
C. The retry prompt should drop the error detail so the model is not biased toward failure.
D. Switching to the Batch API will resolve it because batch processing has access to more context.

### B-D4-05 · Scenario: Conversational AI Architecture · Type: Scenario/Anti-pattern · Difficulty: Medium
A banking chatbot receives: "Move my savings to the account ending 4417 — actually no, send it to my checking instead." The two instructions conflict and the action is irreversible. The current design picks the most recent instruction and executes. What is the better design principle here?

A. Always obey the last instruction, since later statements supersede earlier ones.
B. Average the two — split the transfer across both accounts to satisfy both intents.
C. Because the action is irreversible and the intent is genuinely ambiguous, ask one targeted disambiguating question ("Confirm: send to checking, not the account ending 4417?") before executing.
D. Escalate every transfer to a human regardless of clarity, to be safe.

### B-D4-06 · Scenario: — · Type: Recall · Difficulty: Easy
Using `tool_use` with a JSON schema is described as the most reliable way to get structured output from the model. Precisely which guarantee does it provide?

A. It guarantees the *values* are factually correct.
B. It guarantees syntactically valid JSON and that required structural fields are present — but not semantic correctness of the values.
C. It guarantees the model will never call any other tool for the rest of the conversation.
D. It guarantees the response fits within the context window.

### B-D4-07 · Scenario: Structured Data Extraction · Type: Scenario/Anti-pattern · Difficulty: Medium
A team extracting financial figures wants the model to flag its own arithmetic conflicts so a downstream rule can catch them, without a second API call. Which schema/prompt design enables this self-flagging directly in one extraction response?

A. Extract only the document's stated total and trust it.
B. Have the model extract both the stated total and an independently computed total, plus a boolean that is set true when they disagree, so the conflict is visible in the single response.
C. Force the totals field to be required so the model cannot leave it blank.
D. Run the same extraction twice and diff the two responses outside the model.

### B-D4-08 · Scenario: Claude Code in CI/CD · Type: Scenario/Anti-pattern · Difficulty: Medium
A comment-on-PR bot re-runs on every push. After the third push to a PR, developers complain it re-posts the same five findings it already raised on push one, drowning the new issue. The JSON output and permissions are all correct. What is the prompt-level fix?

A. Lower the model's temperature so it produces the same findings deterministically.
B. Include the prior review's findings in the context and instruct the model to report only new or still-unresolved issues.
C. Switch the output format to text so duplicates are easier to dedupe by hand.
D. Force a tool call with `tool_choice: any` so the bot always emits something.

### B-D4-09 · Scenario: — · Type: Concept/Application · Difficulty: Medium
A pipeline reviews a 22-file feature branch. A single prompt that dumps all 22 files yields uneven results: thorough notes on the first few files, thin notes on the rest, and a contradiction (a pattern flagged in one file, approved in identical code in another). Setting aside simply using a bigger-context model, which restructuring directly targets the root cause?

A. Concatenate the files in a different order so the important ones are not in the middle.
B. Chain the review into per-file local-analysis passes (consistent depth each), then a separate cross-file integration pass for boundary interactions — countering the attention dilution of one mega-prompt.
C. Ask the model to review the whole branch three times and report only findings that appear in all three runs.
D. Raise `max_tokens` so the model has room to be thorough on every file.

### B-D4-10 · Scenario: Structured Data Extraction · Type: Concept/Application · Difficulty: Hard
An extraction service reports 96% field-level accuracy overall and is approved for fully automated processing. Two months in, a partner reports that scanned handwritten intake forms are wrong far more often than that average suggests. What was the measurement mistake, and the right fix?

A. 96% is below the universal 99.5% bar; the only remedy is a larger model.
B. Aggregate accuracy hid per-segment rot; accuracy and confidence should be calibrated per document type and field against a labeled set, with low-confidence segments (e.g., handwritten forms) routed to human review.
C. The schema needs every field marked required so the model tries harder on hard inputs.
D. Handwriting is outside prompt engineering's scope; nothing in the extraction design can help.

### B-D4-11 · Scenario: Conversational AI Architecture · Type: Scenario/Anti-pattern · Difficulty: Medium
A developer-onboarding assistant is asked to "set up caching for the orders service." There are several valid caching strategies with materially different trade-offs (TTL vs event-based invalidation; per-tenant vs global), and the wrong pick would be costly to undo. The assistant immediately starts writing code with default choices. What pattern should it have used, and when is that pattern warranted?

A. Proceed with sensible defaults; asking questions wastes the user's time.
B. Use the interview/clarifying-question pattern — surface the non-obvious design forks before implementing — warranted when approaches diverge materially and the choice is costly to reverse.
C. Escalate to a human architect, since any ambiguity means the agent should stop.
D. Generate all possible implementations in parallel and let the user pick.

### B-D4-12 · Scenario: — · Type: Concept/Application · Difficulty: Medium
A reviewer prompt says only: "Review the config for problems. Be conservative and don't nitpick." It produces a noisy mix — flagging cosmetic key ordering while missing a real misconfigured secret. Which rewrite most improves precision and the team's trust in the output?

A. Append "be MORE conservative" and "only high-confidence issues" to the existing instruction.
B. Replace the vague guidance with explicit inclusion/exclusion criteria — e.g., flag ONLY (1) a secret committed in plaintext, (2) a value that contradicts a required setting, (3) a deprecated key still in use; do NOT flag key ordering or stylistic naming — and define severity levels with examples.
C. Switch to `tool_choice: any` so the reviewer is forced to return findings.
D. Run the review on the Batch API so the model deliberates longer per issue.

## Answer Key — Domain 4

### Mock A
- **A-D4-01** — Correct: C. An `"other"` enum member plus a nullable detail string preserves out-of-vocabulary phrasings without losing the closed-set benefit. Why others fail: A discards the enum's structure entirely (loses the clean categories you still want for the common cases); B applies length constraints that constrained decoding does not support and that would not stop coercion anyway; D making it required raises fabrication/coercion pressure, the opposite of the fix. Sub-domain: D4.5.
- **A-D4-02** — Correct: B. The Messages API is stateless; an id in the body is not server-side memory, so prior turns must be re-sent (compressed, not dropped). Why others fail: A misplaces the id and invents rehydration the API does not do; C invokes caching, which speeds re-sending the same prefix but never stores turns for you; D blames eviction though no history was sent at all. Sub-domain: D4.5 (stateless API; conversational context).
- **A-D4-03** — Correct: C. A named tool choice forces a call to that specific tool. Why others fail: A leaves calling optional; B forces *a* call but lets the model pick which tool; D disables tools entirely. Sub-domain: D4.6.
- **A-D4-04** — Correct: C. Schema enforcement covers syntax and structure, not cross-field logic; semantic/business validation must be added. Why others fail: A and D rely on numeric bounds/composite fields that don't capture relational rules (and bounds aren't supported by constrained decoding); B wrongly abandons a feature working as designed. Sub-domain: D4.7.
- **A-D4-05** — Correct: B. Constrained decoding via a JSON schema makes malformed output impossible at the source; the dead-letter queue is the fallback. Why others fail: A and C treat salience/retry as guarantees (they are not); D prefill is unsupported on current models and still wouldn't guarantee a complete, valid object. Sub-domain: D4.8 (Structured Outputs vs retry).
- **A-D4-06** — Correct: B. Edge-case few-shot examples that map "no code" to null teach the model that absence is acceptable, removing fabrication pressure. Why others fail: A raises effort without changing the incentive to fill the field; C `additionalProperties: true` is unsupported by constrained decoding and irrelevant to fabrication; D temperature 0 makes fabrication consistent, not absent. Sub-domain: D4.1 (few-shot edge cases) / D4.5.
- **A-D4-07** — Correct: C. Judgment calls → principles; safety bright-lines → conditionals, and a truly destructive guard belongs in code because a prompt only biases. Why others fail: A leaves safety to discretion; B removes valuable judgment and bloats the prompt; D inverts the mapping. Sub-domain: D4.2 (principles vs conditionals).
- **A-D4-08** — Correct: B. A correction loop that returns the document, the prior extraction, and the exact mismatch targets the identified error. Why others fail: A is the blind-retry anti-pattern; C invents a batch behavior that doesn't exist; D `maxItems` would silently truncate real data rather than reconcile the count. Sub-domain: D4.8.
- **A-D4-09** — Correct: B. Bulk, non-interactive workload is the canonical Batch case (~50% cheaper); plan around the up-to-24h window and no multi-turn tool calling. Why others fail: A inverts the latency/cost facts; C invents a volume threshold and falsely claims no JSON; D invents infinite retry and an ordering guarantee (results may be out of order — join by custom_id). Sub-domain: D4.9.
- **A-D4-10** — Correct: B. `custom_id` is the join key tying results to requests (which may return out of order), enabling targeted resubmission of only the failures. Why others fail: A, C, D describe priority, encryption, and multi-turn tool calling — none are what custom_id does (and multi-turn tools aren't supported in batch). Sub-domain: D4.9.
- **A-D4-11** — Correct: B. System-prompt salience decays as context grows (competition, not eviction); reinforce at breakpoints and enforce the hard safety constraint in code. Why others fail: A misdiagnoses as eviction and forces an unnecessary trade-off; C invents an incurable bias; D treats emphasis as a guarantee. Sub-domain: D4.2 / D4.3 (instruction persistence).
- **A-D4-12** — Correct: B. Contrastive few-shot examples convey the decision boundary that prose can't pin down. Why others fail: A adds emphasis, not decision logic; C forces both fields and invites fabrication; D batching doesn't add "deliberation time" per label. Sub-domain: D4.1.

### Mock B
- **B-D4-01** — Correct: B. Nullable field removes fabrication pressure; prompt normalization rules plus a "no date" edge-case example handle the format variance and absence together. Why others fail: A keeps the required field and tells it to guess; C abandons validation entirely; D numeric bounds don't apply to date strings and aren't supported by constrained decoding. Sub-domain: D4.1 (normalization rules) / D4.5.
- **B-D4-02** — Correct: C. `any` forces a tool call while letting the model select the best-fitting one. Why others fail: A dictates a specific tool you didn't want to fix; B leaves calling optional; D disables tools. Sub-domain: D4.6.
- **B-D4-03** — Correct: B. Self-review in the same context preserves the generation reasoning and resists self-challenge; use an independent instance for review. Why others fail: A compaction doesn't restore adversarial distance; C emphasis isn't a mechanism; D overcorrects — independent automated review is exactly the fix. Sub-domain: D4.10.
- **B-D4-04** — Correct: B. Retry-with-feedback cannot supply information absent from the source; return null and route to human/missing-document handling. Why others fail: A misunderstands why retries fail here; C dropping the error detail removes the only useful signal for the cases retry *can* fix; D batch doesn't add missing context. Sub-domain: D4.8.
- **B-D4-05** — Correct: C. Irreversible action + genuine ambiguity warrants one targeted disambiguating question before executing. Why others fail: A blindly trusts recency on an irreversible action; B averaging conflicting intents is nonsensical and harmful; D escalating *every* transfer ignores that most are unambiguous. Sub-domain: D4.4 (interview / clarifying questions).
- **B-D4-06** — Correct: B. The guarantee is valid JSON + required structure present, not value correctness. Why others fail: A claims semantic correctness it does not provide; C and D invent guarantees about future tool calls and context fit. Sub-domain: D4.5 / D4.7.
- **B-D4-07** — Correct: B. Extracting both a stated and an independently computed total plus a conflict boolean surfaces the discrepancy in one response. Why others fail: A trusts the stated value blindly; C forcing required doesn't detect conflict; D works but needs a second call and out-of-model diffing — not "directly in one response." Sub-domain: D4.8 (self-correction).
- **B-D4-08** — Correct: B. Feed prior findings into context and instruct the model to report only new/unresolved issues. Why others fail: A determinism still re-emits the resolved findings; C text format doesn't stop duplication; D forcing a call doesn't address dedup. Sub-domain: D4.10 / D4.3 (re-review with prior context).
- **B-D4-09** — Correct: B. Prompt-chaining into per-file passes plus a cross-file integration pass directly counters attention dilution. Why others fail: A reordering doesn't fix per-file depth across 22 files; C consensus-of-three suppresses real bugs found in only one run; D more tokens doesn't improve attention quality. Sub-domain: D4.3.
- **B-D4-10** — Correct: B. Aggregate accuracy masked per-segment rot; calibrate per doc type/field against a labeled set and route low-confidence segments to humans. Why others fail: A invents a universal bar and the wrong remedy; C adds fabrication pressure; D wrongly forecloses prompt-level levers. Sub-domain: D4.10 / (calibration, links to D5.4).
- **B-D4-11** — Correct: B. The interview pattern is warranted when approaches diverge materially and the choice is costly to reverse. Why others fail: A defaults silently on a consequential fork; C over-escalates on any ambiguity; D brute-forces all options wastefully. Sub-domain: D4.4.
- **B-D4-12** — Correct: B. Explicit inclusion/exclusion criteria plus severity levels with examples cut false positives and rebuild trust. Why others fail: A piles on vague emphasis; C forcing findings worsens noise; D batching changes nothing about the criteria. Sub-domain: D4.2.
