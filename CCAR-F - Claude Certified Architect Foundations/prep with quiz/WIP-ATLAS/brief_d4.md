# Authoring brief — D4 Prompt Engineering & Structured Output (20%) · building: The courthouse

Corpus depth file: `prep with quiz/CCA-Prep_Domain-4_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements 4.1–4.x and the sample questions).

24 cards, in this order (ids fixed):

## D4-01 — Explicit categorical criteria beat vague instructions
Home task statement: TS 4.1 — Design prompts with explicit criteria to improve precision and reduce false positives
Gist (the concept, to be written as one flat sentence): "Flag a comment only when the claimed behaviour contradicts the code" works; "be conservative" and "only high-confidence findings" do not.
Official-guide bullets this card must cover:
- [4.1-K1] The importance of explicit criteria over vague instructions (e.g., "flag comments only when claimed behavior contradicts actual code behavior" vs "check that comments are accurate")
- [4.1-K2] How general instructions like "be conservative" or "only report high-confidence findings" fail to improve precision compared to specific categorical criteria
- [4.1-S1] Writing specific review criteria that define which issues to report (bugs, security) versus skip (minor style, local patterns) rather than relying on confidence-based filtering

## D4-02 — False positives erode trust — switch off the noisy category while you fix it
Home task statement: TS 4.1 — Design prompts with explicit criteria to improve precision and reduce false positives
Gist (the concept, to be written as one flat sentence): A high-false-positive category undermines confidence in the accurate ones; disable it temporarily.
Official-guide bullets this card must cover:
- [4.1-K3] The impact of false positive rates on developer trust: high false positive categories undermine confidence in accurate categories
- [4.1-S2] Temporarily disabling high false-positive categories to restore developer trust while improving prompts for those categories
Appendix items it also serves: [APP-I14] Few-shot prompting: Ambiguous scenario targeting, format consistency, false positive reduc…

## D4-03 — Severity levels defined by concrete code examples
Home task statement: TS 4.1 — Design prompts with explicit criteria to improve precision and reduce false positives
Gist (the concept, to be written as one flat sentence): Each level gets example code, so classification is consistent.
Official-guide bullets this card must cover:
- [4.1-S3] Defining explicit severity criteria with concrete code examples for each severity level to achieve consistent classification

## D4-04 — Few-shot examples for consistent format when instructions fail
Home task statement: TS 4.2 — Apply few-shot prompting to improve output consistency and quality
Gist (the concept, to be written as one flat sentence): Show the exact output shape (location, issue, severity, fix) instead of writing longer instructions.
Official-guide bullets this card must cover:
- [4.2-K1] Few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results
- [4.2-S2] Including few-shot examples that demonstrate specific desired output format (location, issue, severity, suggested fix) to achieve consistency
Appendix items it also serves: [APP-I14] Few-shot prompting: Ambiguous scenario targeting, format consistency, false positive reduc…; [APP-T10] Few-shot prompting — Targeted examples for ambiguous scenarios, format demonstration, gene…

Key Distinction to weave into `tested` / `remember`:
```
KD #16 — Few-shot examples vs Instruction refinement for format consistency
When instructions produce inconsistent output format:
- ✅ Few-shot examples showing exact required format (gives model a concrete pattern)
- ❌ More detailed / explicit instructions (already failing; adding more text doesn't help)

---
```

## D4-05 — Aim examples at the ambiguous cases, with the reasoning
Home task statement: TS 4.2 — Apply few-shot prompting to improve output consistency and quality
Gist (the concept, to be written as one flat sentence): Two to four targeted examples that show why one action beat the plausible alternative let the model generalise to new patterns.
Official-guide bullets this card must cover:
- [4.2-K2] The role of few-shot examples in demonstrating ambiguous-case handling (e.g., tool selection for ambiguous requests, branch-level test coverage gaps)
- [4.2-K3] How few-shot examples enable the model to generalize judgment to novel patterns rather than matching only pre-specified cases
- [4.2-S1] Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen over plausible alternatives
- [4.2-S3] Providing few-shot examples distinguishing acceptable code patterns from genuine issues to reduce false positives while enabling generalization
Appendix items it also serves: [APP-I14] Few-shot prompting: Ambiguous scenario targeting, format consistency, false positive reduc…; [APP-T10] Few-shot prompting — Targeted examples for ambiguous scenarios, format demonstration, gene…

Key Distinction to weave into `tested` / `remember`:
```
KD #18 — Target ambiguous examples vs Generic examples for misrouting
- ✅ 4–6 examples targeted at the specific ambiguous cases where misrouting occurs, with rationale
- ❌ 10–15 examples of clear, unambiguous requests for each tool (doesn't address the ambiguous edge cases)

---
```

## D4-06 — Few-shot for extraction across varied documents
Home task statement: TS 4.2 — Apply few-shot prompting to improve output consistency and quality
Gist (the concept, to be written as one flat sentence): Examples of inline citations vs bibliographies, methodology sections vs embedded details, reduce hallucination and fix null required fields.
Official-guide bullets this card must cover:
- [4.2-K4] The effectiveness of few-shot examples for reducing hallucination in extraction tasks (e.g., handling informal measurements, varied document structures)
- [4.2-S4] Using few-shot examples to demonstrate correct handling of varied document structures (inline citations vs bibliographies, methodology sections vs embedded details)
- [4.2-S5] Adding few-shot examples showing correct extraction from documents with varied formats to address empty/null extraction of required fields
Appendix items it also serves: [APP-T10] Few-shot prompting — Targeted examples for ambiguous scenarios, format demonstration, gene…

## D4-07 — tool_use with a JSON schema is the structured-output guarantee
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): Define an extraction tool whose input schema is the output you want and read it from the tool_use block; syntax errors disappear.
Official-guide bullets this card must cover:
- [4.3-K1] Tool use (tool_use) with JSON schemas as the most reliable approach for guaranteed schema-compliant structured output, eliminating JSON syntax errors
- [4.3-S1] Defining extraction tools with JSON schemas as input parameters and extracting structured data from the tool_use response
Appendix items it also serves: [APP-I13] Structured output via tool_use: Schema design, tool_choice configuration, nullable fields …; [APP-T5] Claude API — tool_use with JSON schemas, tool_choice options ("auto", "any", forced tool s…; [APP-T7] JSON Schema — Required vs optional fields, enum types, nullable fields, "other" + detail s…

## D4-08 — tool_choice: auto may answer in text, any must call some tool, forced must call this tool
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): any guarantees a tool call when the document type is unknown; {"type": "tool", "name": ...} guarantees a specific extraction runs first.
Also serves TS 2.3.
Official-guide bullets this card must cover:
- [4.3-K2] The distinction between tool_choice: "auto" (model may return text instead of calling a tool), "any" (model must call a tool but can choose which), and forced tool selection (model must call a specific named tool)
- [4.3-S2] Setting tool_choice: "any" to guarantee structured output when multiple extraction schemas exist and the document type is unknown
- [4.3-S3] Forcing a specific tool with tool_choice: {"type": "tool", "name": "extract_metadata"} to ensure a particular extraction runs before enrichment steps
- [2.3-K4] tool_choice configuration options: "auto", "any", and forced tool selection ({"type": "tool", "name": "..."})
- [2.3-S4] Using tool_choice forced selection to ensure a specific tool is called first (e.g., forcing extract_metadata before enrichment tools), then processing subsequent steps in follow-up turns
- [2.3-S5] Setting tool_choice: "any" to guarantee the model calls a tool rather than returning conversational text
Appendix items it also serves: [APP-I13] Structured output via tool_use: Schema design, tool_choice configuration, nullable fields …; [APP-T5] Claude API — tool_use with JSON schemas, tool_choice options ("auto", "any", forced tool s…

## D4-09 — Schema-valid is not the same as correct
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): Strict schemas remove syntax errors; line items that do not sum and values in the wrong field are semantic errors that survive.
Official-guide bullets this card must cover:
- [4.3-K3] That strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors (e.g., line items that don't sum to total, values in wrong fields)
- [4.4-K4] The difference between semantic validation errors (values don't sum, wrong field placement) and schema syntax errors (eliminated by tool use)
Appendix items it also serves: [APP-T7] JSON Schema — Required vs optional fields, enum types, nullable fields, "other" + detail s…; [APP-T8] Pydantic — Schema validation, semantic validation errors, validation-retry loops…

## D4-10 — Nullable fields stop fabrication
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): Mark fields optional when the source may lack them; a required field forces an invented value.
Official-guide bullets this card must cover:
- [4.3-K4] Schema design considerations: required vs optional fields, enum fields with "other" + detail string patterns for extensible categories
- [4.3-S4] Designing schema fields as optional (nullable) when source documents may not contain the information, preventing the model from fabricating values to satisfy required fields
Appendix items it also serves: [APP-I13] Structured output via tool_use: Schema design, tool_choice configuration, nullable fields …; [APP-T7] JSON Schema — Required vs optional fields, enum types, nullable fields, "other" + detail s…

## D4-11 — Enums with "unclear" and "other" + detail
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): Ambiguous cases get an unclear value; extensible categories get other plus a free-text detail field.
Official-guide bullets this card must cover:
- [4.3-K4] Schema design considerations: required vs optional fields, enum fields with "other" + detail string patterns for extensible categories
- [4.3-S5] Adding enum values like "unclear" for ambiguous cases and "other" + detail fields for extensible categorization
Appendix items it also serves: [APP-T7] JSON Schema — Required vs optional fields, enum types, nullable fields, "other" + detail s…

## D4-12 — Normalisation rules travel with the schema
Home task statement: TS 4.3 — Enforce structured output using tool use and JSON schemas
Gist (the concept, to be written as one flat sentence): Tell the prompt how to normalise inconsistent source formats alongside the strict output schema.
Official-guide bullets this card must cover:
- [4.3-S6] Including format normalization rules in prompts alongside strict output schemas to handle inconsistent source formatting

## D4-13 — Retry with the specific validation error
Home task statement: TS 4.4 — Implement validation, retry, and feedback loops for extraction quality
Gist (the concept, to be written as one flat sentence): Send the original document, the failed extraction and the exact error; the model corrects format and structure faults.
Official-guide bullets this card must cover:
- [4.4-K1] Retry-with-error-feedback: appending specific validation errors to the prompt on retry to guide the model toward correction
- [4.4-S1] Implementing follow-up requests that include the original document, the failed extraction, and specific validation errors for model self-correction
Appendix items it also serves: [APP-T8] Pydantic — Schema validation, semantic validation errors, validation-retry loops…

## D4-14 — Retry cannot create information that is not in the source
Home task statement: TS 4.4 — Implement validation, retry, and feedback loops for extraction quality
Gist (the concept, to be written as one flat sentence): Format mismatches retry well; a value that exists only in a document you did not provide will fail every time.
Official-guide bullets this card must cover:
- [4.4-K2] The limits of retry: retries are ineffective when the required information is simply absent from the source document (vs format or structural errors)
- [4.4-S2] Identifying when retries will be ineffective (e.g., information exists only in an external document not provided) versus when they will succeed (format mismatches, structural output errors)

## D4-15 — detected_pattern turns dismissals into a feedback loop
Home task statement: TS 4.4 — Implement validation, retry, and feedback loops for extraction quality
Gist (the concept, to be written as one flat sentence): Record which code construct triggered each finding so dismissed findings can be analysed for false-positive patterns.
Official-guide bullets this card must cover:
- [4.4-K3] Feedback loop design: tracking which code constructs trigger findings (detected_pattern field) to enable systematic analysis of dismissal patterns
- [4.4-S3] Adding detected_pattern fields to structured findings to enable analysis of false positive patterns when developers dismiss findings

## D4-16 — Self-checking schema: calculated_total beside stated_total, conflict_detected
Home task statement: TS 4.4 — Implement validation, retry, and feedback loops for extraction quality
Gist (the concept, to be written as one flat sentence): Extract both numbers so discrepancies flag themselves; add a boolean for inconsistent source data.
Official-guide bullets this card must cover:
- [4.4-S4] Designing self-correction validation flows: extracting "calculated_total" alongside "stated_total" to flag discrepancies, adding "conflict_detected" booleans for inconsistent source data

## D4-17 — Message Batches API: 50% cheaper, up to 24 hours, no latency SLA
Home task statement: TS 4.5 — Design efficient batch processing strategies
Gist (the concept, to be written as one flat sentence): Batch fits overnight reports and weekly audits; blocking pre-merge checks stay synchronous.
Official-guide bullets this card must cover:
- [4.5-K1] The Message Batches API: 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA
- [4.5-K2] Batch processing is appropriate for non-blocking, latency-tolerant workloads (overnight reports, weekly audits, nightly test generation) and inappropriate for blocking workflows (pre-merge checks)
- [4.5-S1] Matching API approach to workflow latency requirements: synchronous API for blocking pre-merge checks, batch API for overnight/weekly analysis
Appendix items it also serves: [APP-I15] Batch processing: Message Batches API appropriateness, latency tolerance assessment, failu…; [APP-T6] Message Batches API — 50% cost savings, up to 24-hour processing window, custom_id for req…

Key Distinction to weave into `tested` / `remember`:
```
KD #14 — Message Batches API vs Synchronous API
| | Synchronous | Batches API |
|---|---|---|
| Cost | Standard | 50% savings |
| Latency | Immediate | Up to 24 hours (no SLA) |
| Multi-turn tool calls | ✅ Supported | ❌ Not supported — fire-and-forget |
| Use for | Blocking checks, interactive use | Scheduled, non-blocking tasks |

**Exam trap:** Iterative code review (fetches related files mid-review via tool calls) → **cannot use batch API**. Batch is fire-and-forget; it cannot execute tools during a request and return results to Claude.

---
```

## D4-18 — A batch request cannot run a tool loop mid-request
Home task statement: TS 4.5 — Design efficient batch processing strategies
Gist (the concept, to be written as one flat sentence): Batches are fire-and-forget; anything that needs tool results returned mid-request stays synchronous.
Official-guide bullets this card must cover:
- [4.5-K3] The batch API does not support multi-turn tool calling within a single request (cannot execute tools mid-request and return results)
Appendix items it also serves: [APP-T6] Message Batches API — 50% cost savings, up to 24-hour processing window, custom_id for req…

Key Distinction to weave into `tested` / `remember`:
```
KD #14 — Message Batches API vs Synchronous API
| | Synchronous | Batches API |
|---|---|---|
| Cost | Standard | 50% savings |
| Latency | Immediate | Up to 24 hours (no SLA) |
| Multi-turn tool calls | ✅ Supported | ❌ Not supported — fire-and-forget |
| Use for | Blocking checks, interactive use | Scheduled, non-blocking tasks |

**Exam trap:** Iterative code review (fetches related files mid-review via tool calls) → **cannot use batch API**. Batch is fire-and-forget; it cannot execute tools during a request and return results to Claude.

---
```

## D4-19 — custom_id correlates results and lets you resubmit only the failures
Home task statement: TS 4.5 — Design efficient batch processing strategies
Gist (the concept, to be written as one flat sentence): Identify failed documents by custom_id and resubmit them, chunking the ones that exceeded context.
Official-guide bullets this card must cover:
- [4.5-K4] custom_id fields for correlating batch request/response pairs
- [4.5-S3] Handling batch failures: resubmitting only failed documents (identified by custom_id) with appropriate modifications (e.g., chunking documents that exceeded context limits)
Appendix items it also serves: [APP-I15] Batch processing: Message Batches API appropriateness, latency tolerance assessment, failu…; [APP-T6] Message Batches API — 50% cost savings, up to 24-hour processing window, custom_id for req…

## D4-20 — Submission cadence from the SLA arithmetic
Home task statement: TS 4.5 — Design efficient batch processing strategies
Gist (the concept, to be written as one flat sentence): A 30-hour SLA with a 24-hour batch window means submitting every 4 hours or so.
Official-guide bullets this card must cover:
- [4.5-S2] Calculating batch submission frequency based on SLA constraints (e.g., 4-hour windows to guarantee 30-hour SLA with 24-hour batch processing)
Appendix items it also serves: [APP-I15] Batch processing: Message Batches API appropriateness, latency tolerance assessment, failu…

## D4-21 — Refine the prompt on a sample before the big batch
Home task statement: TS 4.5 — Design efficient batch processing strategies
Gist (the concept, to be written as one flat sentence): Tune on a small set first so first-pass success is high and resubmission cost low.
Official-guide bullets this card must cover:
- [4.5-S4] Using prompt refinement on a sample set before batch-processing large volumes to maximize first-pass success rates and reduce iterative resubmission costs

## D4-22 — An independent instance reviews; the author does not
Home task statement: TS 4.6 — Design multi-instance and multi-pass review architectures
Gist (the concept, to be written as one flat sentence): The session that wrote the code keeps its reasoning and will not question it; a second instance without that context catches more than self-review or extended thinking.
Also serves TS 3.6.
Official-guide bullets this card must cover:
- [4.6-K1] Self-review limitations: a model retains reasoning context from generation, making it less likely to question its own decisions in the same session
- [4.6-K2] Independent review instances (without prior reasoning context) are more effective at catching subtle issues than self-review instructions or extended thinking
- [4.6-S1] Using a second independent Claude instance to review generated code without the generator's reasoning context
- [3.6-K4] Session context isolation: why the same Claude session that generated code is less effective at reviewing its own changes compared to an independent review instance

## D4-23 — Per-file passes plus a cross-file integration pass
Home task statement: TS 4.6 — Design multi-instance and multi-pass review architectures
Gist (the concept, to be written as one flat sentence): A 14-file single pass dilutes attention and contradicts itself; split into local passes and one integration pass — a bigger context window does not fix it.
Also serves TS 1.6.
Official-guide bullets this card must cover:
- [4.6-K3] Multi-pass review: splitting large reviews into per-file local analysis passes plus cross-file integration passes to avoid attention dilution and contradictory findings
- [4.6-S2] Splitting large multi-file reviews into focused per-file passes for local issues plus separate integration passes for cross-file data flow analysis
- [1.6-K2] Prompt chaining patterns that break reviews into sequential steps (e.g., analyze each file individually, then run a cross-file integration pass)
- [1.6-S2] Splitting large code reviews into per-file local analysis passes plus a separate cross-file integration pass to avoid attention dilution
Appendix items it also serves: [APP-T11] Prompt chaining — Sequential task decomposition into focused passes…

Key Distinction to weave into `tested` / `remember`:
```
KD #17 — Per-file review passes vs Single-pass full-PR review
| | Per-file + integration pass | Single-pass all files |
|---|---|---|
| Attention quality | High per file | Diluted across all files |
| Local issue detection | Consistent depth | Variable — some files shallow, some deep |
| Cross-file issues | Separate integration pass | Included but may be missed |
| Correct for large PRs | ✅ Yes | ❌ No |

**Exam trap:** "Use a larger model with bigger context window" → Wrong. Larger context does not fix attention quality. More tokens available ≠ consistent attention per token.

---
```

## D4-24 — Confidence beside each finding routes the review
Home task statement: TS 4.6 — Design multi-instance and multi-pass review architectures
Gist (the concept, to be written as one flat sentence): Have the model self-report confidence per finding so low-confidence items get human attention.
Official-guide bullets this card must cover:
- [4.6-S3] Running verification passes where the model self-reports confidence alongside each finding to enable calibrated review routing
