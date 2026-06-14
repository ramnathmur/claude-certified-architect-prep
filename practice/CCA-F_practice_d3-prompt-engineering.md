# CCA-F Practice — Domain 3: Prompt Engineering & Structured Output (20%)
_10 questions · original, exam-style · grounded in EXAM-DIGEST + D3 citations_

## Questions

**Q1.** A team ships a customer-support assistant on the Messages API. Each user message is sent as a single API call that includes only the new user turn plus a `session_id` they generate per conversation. Users complain that the assistant "forgets" what they said two messages ago, even though the same `session_id` is reused. What is the root cause?
- A) The `session_id` must be passed in the top-level `system` parameter, not alongside the messages, for memory to activate.
- B) The Messages API is stateless; `session_id` is not a memory mechanism, so the full prior history must be re-sent on every call.
- C) Prompt caching has expired, dropping the conversation state that the API was holding server-side.
- D) The model's context window is too small to retain the earlier turns across separate requests.

**Q2.** An extraction pipeline must call a `record_invoice` tool on every request — a bare text reply is never acceptable. The engineer sets `tool_choice` to `auto` and writes "You MUST always call the record_invoice tool" in the system prompt. Occasionally Claude still replies with plain text. What is the correct fix?
- A) Add "CRITICAL" and "NEVER reply without the tool" in uppercase to the system prompt to raise reliability.
- B) Switch `tool_choice` to `auto` but lower the temperature so the model is more deterministic about calling tools.
- C) Set `tool_choice` to `any` or to a named tool `{"type":"tool","name":"record_invoice"}`, since only those guarantee a tool call.
- D) Wrap the instruction in XML tags so the salience of the requirement increases enough to force the call.

**Q3.** A service parses Claude's JSON output and intermittently crashes on `JSON.parse()` because the model returns trailing prose or a missing brace. The current design relies on a strong system-prompt instruction to "respond only with valid JSON," and on a retry-and-dead-letter queue when parsing fails. Which change best addresses the problem at the source?
- A) Increase the retry count and add exponential backoff so malformed responses eventually succeed.
- B) Move the "valid JSON only" instruction earlier in the prompt and repeat it at the end for salience.
- C) Use Structured Outputs (constrained decoding via `output_config.format` or strict tool use) so invalid output is impossible; keep retry only as a fallback.
- D) Prefill the assistant turn with an opening brace `{` to force the model into JSON mode.

**Q4.** You are designing a JSON schema for extracting a `phone_number` field from scanned documents where the phone number is frequently absent. The first draft marks `phone_number` as `required`. Reviewers note the model is inventing plausible-looking phone numbers when none exist. Which schema change most directly reduces this fabrication?
- A) Add `minLength` and `maxLength` constraints to the field so only realistic phone numbers validate.
- B) Make the field optional and/or nullable so "absent" is a representable, non-fabricated outcome.
- C) Set `additionalProperties: true` so the model can place uncertain data elsewhere.
- D) Add a recursive sub-schema that lets the model nest a confidence object inside the field.

**Q5.** An invoice-extraction system uses Structured Outputs, and every response now validates cleanly against the JSON schema. In production, a finance auditor finds that line-item amounts sometimes don't sum to the stated invoice total, and some dates fall outside the billing period. What does this reveal?
- A) The schema is misconfigured; `additionalProperties` should be set to `false` to stop the bad values.
- B) Constrained decoding has a bug; the team should disable Structured Outputs and fall back to prompt-only JSON.
- C) Valid JSON guarantees syntax, not correctness; semantic validation (sum checks, date-range checks, ID formats) is still required.
- D) The schema needs numeric `minimum`/`maximum` constraints so out-of-range totals are rejected by the decoder.

**Q6.** After semantic validation flags that an extracted total is internally inconsistent, an engineer wants to recover the correct value without human review. Which approach is most reliable?
- A) Blindly resend the identical request several times and take the first response that passes validation.
- B) Run a correction loop: resend the source document along with the prior extraction and the exact validation errors, asking Claude to fix them.
- C) Raise the model's `effort` to `max` on a plain retry so it reasons harder the second time.
- D) Lower the temperature to 0 and resend the same prompt so the output becomes deterministic.

**Q7.** An architect is writing the system prompt for a long-running coding agent. Two requirements differ in nature: (1) "calibrate explanation depth to the user's apparent expertise" and (2) "if the user reports a security incident, immediately direct them to the on-call escalation path." How should these be expressed?
- A) Both as rigid conditionals, so the model never has to use judgment for either case.
- B) Both as open principles, trusting the model to generalize the right behavior in all situations.
- C) (1) as a principle for judgment; (2) as a conditional bright-line, because safety-critical behavior should not be left to interpretation.
- D) (1) as a conditional and (2) as a principle, since expertise is binary and safety is contextual.

**Q8.** In a multi-phase agent conversation, the team notices that rules stated once at the start of a long session (e.g., "always cite the source file before editing") are followed early but ignored after many turns. Which explanation and remedy are correct?
- A) The rules were silently dropped from the context window; the only fix is to shrink the conversation with a sliding window.
- B) Attention to the system prompt weakens as the conversation grows (it is competed for, not dropped); reinforce key rules at phase breakpoints.
- C) The model has a hard recency bias that can only be overcome by raising `effort`.
- D) The system prompt was placed in a user message; moving it to the top-level `system` param fixes the decay permanently.

**Q9.** A nightly job extracts structured data from 50,000 documents with no real-time requirement. The engineer submits them through the Batch API and then iterates over the results array positionally, assuming `results[0]` corresponds to `requests[0]`. Some records end up attached to the wrong document. What is the flaw?
- A) The Batch API does not support structured output, so the records were silently corrupted.
- B) Batch results may return out of order; each result must be joined back to its request by its `custom_id`.
- C) The batch size exceeded the limit, truncating the array and shifting indices.
- D) Batch requests must be submitted one at a time to preserve ordering.

**Q10.** An extraction system reports a single aggregate accuracy of 94% across all document types and fields, and the team treats it as production-ready. A downstream consumer complains that handwritten-form dates are almost always wrong. Which critique is correct?
- A) 94% aggregate accuracy is below the 99% bar required for any extraction system, so the system simply needs more training data.
- B) Confidence and accuracy should be calibrated per segment (doc type, field, source) against a labeled set; aggregate accuracy hides per-field rot.
- C) The fix is to make every field `required` in the schema so the model is forced to try harder on dates.
- D) Handwriting recognition is out of scope for prompt engineering; only model selection can address it.

---

## Answer Key

**Q1 — B.** The Messages API is stateless: there is no server-side memory between calls, and `session_id` is not a memory mechanism — full prior history must be re-sent each request. C is wrong because the API holds no conversation state to expire (caching speeds re-sending the same prefix; it does not store turns for you); A misstates where `session_id` lives; D is a red herring since no history was sent at all. _Sub-topic: Stateless Messages API · Difficulty: easy_

**Q2 — C.** Only `tool_choice: any` (a tool from the set) or a named tool guarantees a tool call; `auto` leaves the call optional regardless of how forcefully the prompt is worded. A and D try to use salience/emphasis as a guarantee mechanism — they bias behavior but do not enforce it. B keeps the non-guaranteeing `auto` setting. _Sub-topic: tool_choice semantics · Difficulty: med_

**Q3 — C.** Structured Outputs (constrained decoding) makes malformed JSON impossible at generation time — the source-level fix — with retry/dead-letter as the fallback, not the primary mechanism. A treats retry as the fix; B relies on prompt salience, which cannot guarantee validity; D uses prefill, which is unsupported on Claude 4.6+ models and still wouldn't guarantee well-formed JSON. _Sub-topic: Structured Outputs vs retry · Difficulty: med_

**Q4 — B.** Making the field optional and/or nullable gives the model a faithful way to represent absence, removing the hallucination pressure that a `required` field creates. A and D describe schema features Structured Outputs does not support (string-length constraints; recursive schemas). C loosens `additionalProperties`, which neither stops fabrication nor is permitted (Structured Outputs requires `additionalProperties: false`). _Sub-topic: Schema rules / killing fabrication · Difficulty: med_

**Q5 — C.** Schema validation catches syntax, not logic; valid JSON ≠ correct data, so semantic validation (line-item sums, date ranges, ID formats) is still required. A and D propose constraints that don't address cross-field logic — and numeric/length constraints are not supported by Structured Outputs anyway. B over-reacts by abandoning a feature that is working as designed. _Sub-topic: Semantic validation · Difficulty: med_

**Q6 — B.** A correction loop — resending the document plus the prior extraction plus the exact errors — gives the model what it needs to fix the specific mistake, and beats blind retries. A is exactly the blind-retry anti-pattern. C and D change a knob but resend essentially the same uninformed request, so they don't target the identified error. _Sub-topic: Correction loop vs blind retry · Difficulty: med_

**Q7 — C.** Principles ("adapt depth to expertise") are for judgment calls; conditionals ("if X, do Y") are for safety bright-lines that must not be left to interpretation. B leaves safety to discretion; A removes judgment where it's valuable and bloats the prompt with conditionals; D inverts the correct mapping. _Sub-topic: Principles vs conditionals · Difficulty: hard_

**Q8 — B.** System-prompt attention is competed for and weakens as context grows — the rules are not dropped — so the remedy is to reinforce key rules at phase breakpoints. A misdiagnoses it as eviction and forces an unnecessary trade-off; C invents a fix unrelated to the mechanism; D is wrong because the prompt was already a proper system prompt and placement doesn't cure salience decay. _Sub-topic: System-prompt salience decay · Difficulty: hard_

**Q9 — B.** Batch API results may arrive out of order, so each result must be joined to its request by `custom_id` rather than by array position. A is false (Batch supports structured output); C and D invent constraints that don't exist — batch is designed for many concurrent requests, and the join key, not submission order, preserves correctness. _Sub-topic: Batch API / custom_id · Difficulty: med_

**Q10 — B.** Confidence and accuracy must be calibrated per segment (doc type, field, source) against a labeled set; a single aggregate number masks per-field rot like the failing handwritten dates. A invents an arbitrary universal bar and the wrong remedy; C adds hallucination pressure without improving accuracy; D wrongly forecloses prompt-level levers (few-shot edge-case examples, source grounding) before model selection. _Sub-topic: Confidence calibration per segment · Difficulty: med_
