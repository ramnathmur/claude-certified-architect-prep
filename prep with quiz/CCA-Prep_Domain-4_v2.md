# Domain 4: Prompt Engineering & Structured Output (20%)

**Source:** guide_en.MD — Chapters 2.4–2.5, 6.5–6.6, 7, 9–11, Scenarios: All; CCA-F Official Exam Guide Task Statements 4.1–4.6  
**Version:** 2.0 | 2026-07-06  
**Changelog v2:** Retains all v1 content (renumbered). Added: §4.6 Guaranteeing Structured Output via tool_use + tool_choice; §4.7 Syntax vs Semantic Errors; §4.8 Programmatic Validation (Pydantic/Typed Schemas); §4.9 expanded Retry-with-Feedback with retry limits + detected_pattern tracking; §4.10 Self-Correction Patterns (stated_total vs calculated_total); §4.11 Batch Processing Strategy (custom_id join key, selective re-submission, SLA planning, sample-first iteration, tool-use accuracy correction); §4.13 Multi-Instance Independent Review.

---

## 4.1 Few-Shot Prompting

### When to Use
Few-shot examples are the most effective technique when:
- **Prose instructions produce inconsistent output** — examples show exact expected format
- **Ambiguous tool selection** — examples for the specific ambiguous cases (not generic cases)
- **Multi-issue request handling** — examples demonstrate correct decomposition and sequencing
- **Escalation calibration** — examples show "escalate this / don't escalate this"

### Critical Principle: Target the Ambiguous Cases
Do not add 10–15 examples of clear, unambiguous cases. Target the 4–6 examples at exactly the cases where the model gets it wrong.

**Exam scenario:** Agent misroutes "I need help with my recent purchase" — ambiguous between `get_customer` and `lookup_order`.
- ✅ Add 4–6 examples targeted at ambiguous scenarios, each with rationale for why one tool was chosen over alternatives
- ❌ Add 10–15 examples of clear, unambiguous requests (doesn't help with the edge cases)

**Exam scenario:** Automated review generates inconsistent feedback format despite instructions.
- ✅ Add 3–4 few-shot examples showing exact required format: identified issue, location in code, concrete fix
- ❌ Further refine instructions with more explicit requirements (instructions are already failing)

---

## 4.2 Chain-of-Thought / Reasoning Cues

### Step-by-Step Instruction
Including "Think step by step before answering" improves accuracy on multi-step reasoning tasks.

### When Required (R5 in Compliance Checklist)
Add a reasoning cue when the task requires:
- Multi-step mathematical reasoning
- Multi-stage analysis
- Comparison across N items
- Step-wise transformation

Do NOT add for single-step tasks (e.g., "translate this sentence to French").

---

## 4.3 System Prompt Design

### Persistent Behavioral Constraints Belong in the System Prompt
The system prompt is the correct location for:
- Tone and persona constraints
- Behavioral rules that apply for the entire conversation
- Response format requirements

**Exam scenario:** "Where should enthusiasm, reasoning transparency, and clarifying-question requirements live?"
- ✅ System prompt
- ❌ First user message (loses authority mid-conversation)
- ❌ Environment variables (no effect on model behavior)
- ❌ First assistant message (model can deviate from its own prior statements)

---

## 4.4 Prefilling (Response Seeding)

### What It Is
Including the beginning of an assistant message in the API call so Claude continues from it, rather than generating a new response from scratch.

### Use Cases
1. **Suppress filler phrases** ("Certainly!", "I'd be happy to help!") — append a direct opening partial response; Claude continues from it
2. **Inject real-time context** into next response — prefix the next user message with the event data ("Your package has shipped. Now: [user message]")

**Exam scenario:** Users report repetitive "Certainly!" openings.
- ✅ Append a partial assistant message with a direct response opening (prefilling)
- ❌ Lower temperature (controls randomness, not specific phrases)
- ❌ Post-process to remove greetings (fragile workaround)
- ❌ System prompt instruction to avoid those phrases (less reliable)

**Exam scenario:** Webhook fires during active chat session — package has shipped.
- ✅ Append the status update as a prefix to the next user message
- ❌ Modify the system prompt (requires rebuilding session)
- ❌ Send a synthetic user message (breaks natural dialogue flow)

---

## 4.5 JSON Schema Design for Tool Use / Structured Output

### Key Schema Design Decisions

| Situation | Schema Design |
|---|---|
| Field always present and never null | `required: [field]`, type is not nullable |
| Field sometimes absent | Omit from `required`; make nullable or use `anyOf: [type, null]` |
| Field has known values but might have new ones | `enum: ["A", "B", "other"]` with a companion `detail` field |
| Model cannot confidently pick a category | Add `"unclear"` to the enum — honest `"unclear"` beats a confident wrong category |
| Confidence score per field | Add `field_confidence: float [0,1]` alongside each field |
| Unclear from source | `nullable: true` — preserve ambiguity in output |

### Why Nullable Matters: Fabrication Prevention
Mark fields as `required` only if the information is **always** available in the source. A required, non-nullable field pushes the model to **fabricate values** to satisfy the schema when the data is missing. Nullable fields (`"type": ["string", "null"]`) let the model return `null` instead of hallucinating.

- ✅ Optional/nullable fields for information that may be absent → model returns `null`
- ❌ "Make every field required so the output is always complete" — completeness by fabrication, not extraction

### Format Normalization
Include format normalization rules **in the prompt** alongside the strict output schema when source documents have inconsistent formatting (dates, currencies, informal measurements). The schema constrains the shape; the prompt governs how messy inputs map into it.

---

## 4.6 Guaranteeing Structured Output: tool_use + tool_choice

### The Mechanism That Guarantees Structure
Defining a tool whose **input schema** is your desired output structure, then reading the structured data from the `tool_use` block, is the **most reliable** way to get schema-compliant structured output. The tool doesn't need to "do" anything — it exists to force schema-conformant JSON.

This **eliminates JSON syntax errors** (missing braces, trailing commas, wrong field types). Contrast with asking nicely in the prompt ("respond only with valid JSON matching this schema"), which the model may or may not honor — prompt-based JSON requests can still return prose preambles, markdown fences, or malformed JSON.

### tool_choice Modes

| Value | Behavior | When to use |
|---|---|---|
| `{"type": "auto"}` | Model decides whether to call a tool or answer in text | Default conversational use — **no structure guarantee** |
| `{"type": "any"}` | Model **must** call some tool | Guaranteed structured output when multiple extraction schemas exist and document type is unknown — model picks the best-fitting tool, but you always get structured output |
| `{"type": "tool", "name": "extract_metadata"}` | Model **must** call that specific tool | Forcing a particular extraction to run (e.g., metadata extraction before enrichment steps) |

**Exam scenario:** Pipeline must always receive schema-valid JSON; documents may be invoices, receipts, or contracts (three extraction tools defined).
- ✅ `tool_choice: {"type": "any"}` — model must call one of the tools; output is always structured
- ❌ `tool_choice: {"type": "auto"}` — model may answer in free text instead of calling a tool
- ❌ Prompt instruction "always respond with JSON" — no guarantee; syntax errors and prose wrappers still occur
- ❌ Post-process free-text responses with a JSON repair library (treats the symptom; tool_use removes the problem at the source)

**Exam scenario:** Enrichment step keeps running before metadata extraction has produced its output.
- ✅ Force the specific tool: `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first call
- ❌ `tool_choice: "any"` (guarantees *a* tool call, not *that* tool)

### ❌ Misconception
"tool_use with a strict JSON schema guarantees the output is **correct**." — It guarantees the output is **syntactically valid and schema-shaped**. Values can still be semantically wrong (see §4.7). Schema compliance ≠ content correctness.

---

## 4.7 Syntax vs Semantic Errors

The exam's core distinction for extraction quality:

| Error type | Examples | Detected by | Fixed by |
|---|---|---|---|
| **Syntax** | Malformed JSON (missing brace, trailing comma), wrong field type, missing required field — schema violations | Programmatic validators (JSON Schema, Pydantic) — deterministic, catches 100% | `tool_use` with a JSON schema **eliminates** these; otherwise retry-with-feedback fixes them |
| **Semantic** | Valid JSON but wrong content: line items don't sum to `total`, value placed in the wrong field, hallucinated value, wrong category | Business-rule validation, cross-field checks, self-correction fields | Validation checks + retry with the specific error; self-correction patterns (§4.10); sometimes human review |

**Key insight:** strict schemas via tool use eliminate the entire syntax class but do **nothing** for the semantic class. A response can pass schema validation perfectly and still claim an invoice total of $150 when the line items sum to $145.

**Exam scenario:** Extraction pipeline moved to tool_use with strict schemas; JSON parse failures dropped to zero, but downstream reconciliation still finds totals that don't match line items.
- ✅ Expected behavior — schemas eliminated syntax errors; the remaining failures are semantic and need validation + feedback loops
- ❌ "The schema must be wrong — tighten it further" (no schema constraint can verify that numbers sum correctly)
- ❌ "Tool use is unreliable, revert to prompt-based JSON" (would reintroduce the syntax error class on top of the semantic one)

### ❌ Misconception
"A validator that passes means the extraction is correct." — A schema validator proves only structural validity. Semantic errors sail through schema validation by definition: the JSON is valid, the content is wrong.

---

## 4.8 Programmatic Validation: Pydantic / Typed Schemas

The validation layer sits **in your code, after** receiving JSON from Claude — never trust model output unvalidated.

### What Pydantic (or equivalent typed-schema validation) Gives You
1. **Structural validation** — types, requiredness, enum membership checked deterministically in code
2. **Semantic validation** — custom validators encode business logic: `sum(line_items) == total`, `start_date < end_date`
3. **Validate–retry loops** — on validation failure, Pydantic's error message becomes the feedback for the retry prompt (§4.9)
4. **Single source of truth** — Pydantic models can **generate the JSON Schema** used in the tool definition, so the tool's input schema and your code's validator can never drift apart

**Exam scenario:** Team maintains the tool's JSON schema by hand and a separate validation class; they keep drifting out of sync.
- ✅ Generate the tool's JSON Schema from the Pydantic model — one definition drives both the tool_use contract and post-hoc validation
- ❌ Add a code-review checklist item to update both files (process patch for an architecture problem)

### ❌ Misconception
"tool_use already enforces the schema, so validating again in code is redundant." — Tool use enforces structure at generation time, but your code should still validate: (a) semantic/business rules that no JSON schema can express, and (b) defense-in-depth for anything downstream consumes. The schema constrains shape; Pydantic validators check meaning.

---

## 4.9 Retry-with-Feedback Loop — and Its Limits

### The Loop
When extraction fails validation:
```
1. Send: document + extraction prompt
2. Receive: extracted JSON
3. Validate against schema + business rules (Pydantic)
4. If invalid: retry with original document + incorrect extraction + specific validation error
5. Repeat until valid or max retries reached
```

**Critical:** Include the **specific validation error** in the retry prompt, not just "try again."
> "Field 'total' = 150, but sum(line_items) = 145. Re-check values."

The retry request contains three things: the original document, the previous (failed) extraction, and the specific error.

### When Retry WILL Help
- **Format errors** — date in the wrong format, wrong number representation
- **Structural errors** — a value placed in the wrong field
- **Arithmetic inconsistencies** — the model can re-check and re-derive

### When Retry Will NOT Help
- **The information is genuinely absent from the source document** — no number of retries can extract what isn't there
- **The required context is external** — the data lives in another document that wasn't provided

Retrying in these cases **burns tokens for nothing** — and worse, pressure to fill a required field can push the model into fabrication. The correct design: nullable/optional fields (§4.5) so the model returns `null`/absent, and your pipeline treats "not found" as a legitimate answer, not a failure to retry.

**Exam scenario:** Extraction of `purchase_order_number` fails validation on 40 documents; investigation shows those documents never contained a PO number.
- ✅ Make the field nullable; accept `null`; stop retrying — the information is absent, retries waste tokens and invite fabrication
- ❌ Increase max retries from 3 to 10 (absent information stays absent)
- ❌ Strengthen the retry feedback message (no feedback can conjure missing data)
- ❌ Keep the field required "for data quality" (guarantees fabricated values)

### detected_pattern Tracking Across Retries and Findings
Add a `detected_pattern` field to structured findings/extractions identifying **which construct triggered the finding**. This enables systematic analysis:
- When developers dismiss findings, group dismissals by `detected_pattern` to find which patterns drive false positives
- Across retries, track which patterns repeatedly fail validation to identify systematic prompt/schema weaknesses rather than treating each failure as an isolated event

**Exam scenario:** Review tool's findings are frequently dismissed but the team can't tell which finding types are noise.
- ✅ Add a `detected_pattern` field to each finding; analyze dismissal rates per pattern
- ❌ Ask developers to write a free-text reason on every dismissal (unstructured; doesn't aggregate)

### ❌ Misconception
"If validation fails, retrying with feedback always converges on a correct answer." — Retry-with-feedback only fixes errors the model *can* correct from the provided context (format, structure, arithmetic). For absent information, retry is pure waste; the fix is schema design (nullable) not loop tuning.

---

## 4.10 Self-Correction Patterns

Have the model **re-derive and compare** within a single structured output, so internal contradictions surface as data instead of hiding.

### stated_total vs calculated_total
```json
{
  "stated_total": "$150.00",
  "calculated_total": "$145.00",
  "conflict_detected": true,
  "line_items": [
    {"name": "Widget A", "price": 75.00},
    {"name": "Widget B", "price": 70.00}
  ]
}
```
- `stated_total` — the value as written in the document
- `calculated_total` — the model re-derives the total from the extracted line items
- `conflict_detected` — boolean flag when they disagree

This catches **arithmetic drift** (extraction picked up the wrong number, or the source document itself is inconsistent) and lets your pipeline route conflicts to review instead of silently trusting either number. The same pattern generalizes: extract both the claimed value and an independently derived value; flag disagreement with a boolean.

**Exam scenario:** Invoice pipeline occasionally reports totals that don't match line items, discovered weeks later in reconciliation.
- ✅ Extract `calculated_total` alongside `stated_total` with a `conflict_detected` flag; route conflicts for handling at extraction time
- ❌ Post-hoc monthly reconciliation report (detection weeks late; the pattern moves it to extraction time)
- ❌ Prompt "be careful with totals" (vague instruction; no detection mechanism)

### ❌ Misconception
"Self-correction means asking the model 'are you sure?' after it answers." — The exam pattern is **structural**: build the re-derivation into the output schema (stated vs calculated + conflict boolean) so checking happens on every extraction and produces machine-readable signals — not an optional conversational follow-up.

---

## 4.11 Batch Processing Strategy (Message Batches API)

### Core Facts

| Attribute | Value |
|---|---|
| Cost | **50% discount** vs synchronous calls |
| Processing window | Up to **24 hours**; most batches complete much faster — but there is **no latency SLA** |
| Correlation | `custom_id` per request — the join key between requests and results |
| Tool use / multi-turn | **Supported** — batch requests can include tools and full multi-turn message histories (see accuracy note below) |

### Batch vs Synchronous — Match API to Latency Tolerance

| Task | API | Why |
|---|---|---|
| Pre-merge PR check | **Synchronous** | The developer is waiting; up to 24h is unacceptable |
| Overnight tech-debt report | **Batch** | Result needed by morning; 50% savings |
| Weekly security audit | **Batch** | Not urgent; 50% savings |
| Interactive code review | **Synchronous** | Immediate response required |
| Processing 10,000 documents | **Batch** | Bulk; savings are significant |

Batch is for **non-blocking, latency-tolerant** workloads (overnight reports, weekly audits, nightly test generation); synchronous for anything a human or pipeline is blocking on.

### custom_id: The Join Key (Required Discipline)
Batch results **can arrive in any order** — there is no guaranteed correspondence between submission order and result order. `custom_id` is how you match each result back to its originating request:
- Link the result to the original document (`"custom_id": "doc-invoice-2024-001"`)
- Identify exactly which items failed
- Avoid re-processing successful items

- ✅ Assign a meaningful, unique `custom_id` to every request in every batch
- ❌ Rely on result ordering to match results to inputs (ordering is not guaranteed — this silently mis-joins data)

### Selective Re-submission After Partial Failure
```
1. Submit a batch of 100 documents
2. 95 succeed; 5 fail (e.g., context limit exceeded)
3. Identify the 5 failures by custom_id
4. Modify strategy for those items (e.g., chunk the long documents)
5. Re-submit ONLY the 5 failed documents
```
- ✅ Re-submit only failures, identified by `custom_id`, with an appropriate modification
- ❌ Re-submit the entire batch of 100 (pays again for 95 successes; may produce duplicate results downstream)
- ❌ Re-submit the 5 failures unchanged (they failed for a reason — fix the cause, e.g., chunking, before retrying)

### SLA Planning: Budget the 24-Hour Worst Case
Plan submission windows against the **worst case** (24h), not the typical case:
- Need results within 30 hours? Submission window = 30 − 24 = **6 hours**. Batches must be submitted no later than 24 hours before the downstream deadline.
- For a recurring pipeline with a 30-hour SLA, split submissions into 4-hour windows so every batch has the full 24h buffer before its deadline.

- ✅ Submission deadline = downstream deadline − 24h
- ❌ Plan around "batches usually finish in an hour" (no SLA — the one batch that takes 23 hours blows your deadline)

### Sample-First Iteration
Before committing a large batch, validate the prompt on a **small synchronous sample**:
1. Run the extraction prompt synchronously on a representative sample (fast feedback)
2. Refine prompt/schema until the sample passes validation
3. Only then submit the full batch

This maximizes first-pass success and avoids paying (and waiting up to 24h) to discover a prompt defect replicated across 10,000 requests.

- ✅ Refine on a synchronous sample set first, then batch the volume
- ❌ Submit the full 10,000-document batch and iterate on the whole batch (each iteration costs a full batch and up to 24h)

### ⚠️ Accuracy Note: Tool Use in Batches (verified against platform.claude.com docs, 2026-07-06)
The Batch API **does support tool use and multi-turn conversations** — a batch request's `params` are the same as a regular Messages API call, including `tools` and multi-message histories. Older study materials claiming "batches cannot use tools" are **wrong**.

What batches cannot do is **interactive back-and-forth within one request's processing**: each batch request is self-contained — if the model responds with `tool_use`, that batch request completes with that response. Your client cannot execute the tool and return a `tool_result` *mid-request*; continuing the loop requires submitting a follow-up request (in a new batch or synchronously) with the tool result appended.

- ✅ Batch request with `tools` defined and a multi-turn history → valid; response may end in `tool_use`
- ❌ "The Batch API doesn't support tools" (outdated/false)
- ❌ Expecting the batch to pause while your client answers a mid-request tool call (each request is one shot: submit → single model response)

### ❌ Misconception
"Batch = 50% cheaper synchronous API with a delay, so use it everywhere and just poll faster." — Batch has **no latency SLA**; anything blocking (pre-merge checks, interactive flows) must stay synchronous, and every batch deadline calculation must absorb the full 24-hour worst case.

---

## 4.12 Multi-Pass Review Architecture

When a single pass over many items produces inconsistent results (attention dilution):

**Problem:** Single-pass review of 14-file PR produces:
- Detailed comments on some files, shallow on others
- Missed obvious bugs
- Contradictory feedback (same pattern flagged in one file, approved in another)

**Root cause:** Attention dilution when processing many items at once.

**Solution:** Focused passes
1. Per-file pass: review each file individually for local issues
2. Integration pass: separate pass examining cross-file data flows

**Exam trap:** "Switch to a larger model with bigger context window" — wrong. Larger context does not fix attention quality. The attention quality issue exists regardless of window size.

---

## 4.13 Multi-Instance Independent Review

### Why Self-Review Falls Short
A model that generated code **retains the reasoning context from generation**. Within the same session, it is anchored to its own decisions and less likely to question them — the same blind spots that produced a bug tend to survive a same-session re-check.

### The Pattern: True Independence
Send the generated output to a **second Claude instance with no access to the first instance's reasoning** — a fresh request containing only the artifact to review (plus review criteria), not the generation conversation. Without the generator's justifications in context, the reviewer evaluates the code on its own merits and catches subtle issues the generator rationalized away.

**Exam scenario:** Generated code passes its own "review your work carefully" step but bugs keep reaching production.
- ✅ Route the output to a second, independent Claude instance that never sees the generator's reasoning
- ❌ Add "review your own code thoroughly before finishing" to the generator's prompt (self-review inside the same context inherits the same anchoring)
- ❌ Enable extended thinking on the generator (more reasoning by the same anchored instance ≠ independent scrutiny)
- ❌ Ask for a "second pass" in the same conversation (see misconception below)

### Confidence-Calibrated Routing
In verification passes, have the reviewing model **self-report confidence alongside each finding** so downstream routing can be calibrated — e.g., high-confidence findings auto-comment, low-confidence findings route to human review.

### ❌ Misconception
"Asking the same conversation for a second review pass gives you an independent review." — It does not. A second pass **in the same conversation** still carries the full generation reasoning in context; the model re-reads its own justifications and confirms them. Independence requires a **separate instance/request without the first's reasoning context**. Same-conversation second pass ≠ independent review.

---

## 4.14 Prompt Chaining

Break complex tasks into sequential focused prompts where each step's output feeds the next.

**Examples from practice scenarios:**
- Step 1: Identify issues in code
- Step 2: Generate fixes for identified issues
- Result: More focused, consistent output at each stage

---

## 4.15 Escalation and Confidence Routing

### When to Escalate (Explicit Criteria Approach)
Add explicit escalation criteria with few-shot examples to the system prompt showing:
- "Escalate when: [scenario]"
- "Resolve autonomously when: [scenario]"

**Exam scenario:** Agent escalates simple standard replacements (photo-proven damage) but tries to handle complex policy exceptions autonomously. First-contact resolution 55%, target 80%.
- ✅ Add explicit escalation criteria with few-shot examples distinguishing simple vs complex
- ❌ Self-confidence rating + automatic routing threshold (adds infrastructure without addressing root cause)
- ❌ Separate classifier model (overkill; root cause is unclear decision boundaries in prompt)

---

## 4.16 Instruction Specificity vs Abstraction

When vague instructions produce inconsistent output, move from abstract to concrete.

| Problem | Abstract instruction | Concrete fix |
|---|---|---|
| Review flags wrong comments | "Check that comments are accurate" | "Flag comments only when the behavior they claim contradicts the code's actual behavior" |
| Review has inconsistent severity | "Rate severity appropriately" | Define explicit criteria for critical/high/medium/low with examples |

**Exam pattern:** Replace vague intent ("check accuracy") with explicit, testable criteria ("flag only when claimed behavior contradicts actual behavior").

---

## 4.17 Trust Restoration via Category Management

**Exam scenario:** Automated review has 52% false positives on style, 48% on documentation, 8% on security, 18% on performance. Developers dismiss all findings.

- ✅ **Temporarily disable high-false-positive categories** (style, naming, documentation); keep only high-precision categories while improving prompts
- ❌ Display confidence scores (still shows all findings; trust still eroded)
- ❌ Add few-shot examples across all categories over several weeks (slow; trust continues to erode)
- ❌ Uniform strictness reduction (damages high-precision categories unnecessarily)

**Why:** High-false-positive categories cause developers to dismiss everything, including real findings in accurate categories. Surgical disabling stops the trust bleed while you fix the noisy categories.

---

## 4.18 Context-Aware Suggestions (Deduplication)

**Exam scenario:** Automated tool suggests 10 test cases for a PR, but 6 duplicate existing tests.
- ✅ Include the existing test file in context — Claude can only avoid duplicates if it knows what exists
- ❌ Reduce requested count to 5 (assumes priority ordering)
- ❌ Post-process with keyword matching (fragile, misses semantic duplicates)

---

## 4.19 Clarification Strategy — Proceed vs Ask

**When users send vague requests:**
- Do NOT ask 4+ clarifying questions (causes 35–40% abandonment)
- ✅ State assumptions explicitly and proceed, inviting corrections
- ❌ Ask all questions in one compound message (still demands effort from user)
- ❌ Use hidden defaults (user unaware of what was assumed)

**Exam pattern:** "Can you help with the report?" / "Book a venue for the party"
- ✅ Proceed with stated reasonable assumptions
- This applies both to user-facing assistants AND multi-agent systems (synthesis agent should not block awaiting coordinator clarification on all gaps)

---

## 4.20 Behavioral Drift Mitigation

### What It Is
As assistant responses accumulate in conversation history, system prompt influence dilutes relative to the growing body of assistant-generated content. The model increasingly pattern-matches its own prior outputs.

### Fixes

| Fix | When |
|---|---|
| Inject user-role reminder messages at conversation breakpoints | Persistent behavioral constraint drift |
| Replace verbose rules with few-shot examples | Long system prompt with abstract rules that fail after 10–15 turns |
| Prefill partial assistant response | Suppressing specific response patterns |

**Exam scenario:** Contractor persona assistant gives generic advice by turn 7, conversation only 2,500 tokens.
- Root cause: ✅ Accumulated assistant responses dilute system prompt influence (not context window overflow, not "system prompt only applies once")

**Exam scenario:** AI tutor 2,800-token system prompt; ignores proficiency levels after 12 turns.
- ✅ Replace verbose rules with few-shot examples demonstrating proficiency-level adaptation
- ❌ Periodic reminder injection every 4–5 turns (addresses symptoms, not root cause)
