# Domain 4: Prompt Engineering & Structured Output (20%)

**Source:** guide_en.MD — Chapters 9–11, Scenarios: All  
**Version:** 1.0 | 2026-06-27

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
| Confidence score per field | Add `field_confidence: float [0,1]` alongside each field |
| Unclear from source | `nullable: true` — preserve ambiguity in output |

### Retry-with-Feedback Loop
When extraction fails validation:
```
1. Send: document + extraction prompt
2. Receive: extracted JSON
3. Validate against schema
4. If invalid: retry with original document + incorrect extraction + specific validation error
5. Repeat until valid or max retries reached
```

**Critical:** Include the specific validation error in the retry prompt, not just "try again."

---

## 4.6 Multi-Pass Review Architecture

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

## 4.7 Prompt Chaining

Break complex tasks into sequential focused prompts where each step's output feeds the next.

**Examples from practice scenarios:**
- Step 1: Identify issues in code
- Step 2: Generate fixes for identified issues
- Result: More focused, consistent output at each stage

---

## 4.8 Escalation and Confidence Routing

### When to Escalate (Explicit Criteria Approach)
Add explicit escalation criteria with few-shot examples to the system prompt showing:
- "Escalate when: [scenario]"
- "Resolve autonomously when: [scenario]"

**Exam scenario:** Agent escalates simple standard replacements (photo-proven damage) but tries to handle complex policy exceptions autonomously. First-contact resolution 55%, target 80%.
- ✅ Add explicit escalation criteria with few-shot examples distinguishing simple vs complex
- ❌ Self-confidence rating + automatic routing threshold (adds infrastructure without addressing root cause)
- ❌ Separate classifier model (overkill; root cause is unclear decision boundaries in prompt)

---

## 4.9 Instruction Specificity vs Abstraction

When vague instructions produce inconsistent output, move from abstract to concrete.

| Problem | Abstract instruction | Concrete fix |
|---|---|---|
| Review flags wrong comments | "Check that comments are accurate" | "Flag comments only when the behavior they claim contradicts the code's actual behavior" |
| Review has inconsistent severity | "Rate severity appropriately" | Define explicit criteria for critical/high/medium/low with examples |

**Exam pattern:** Replace vague intent ("check accuracy") with explicit, testable criteria ("flag only when claimed behavior contradicts actual behavior").

---

## 4.10 Trust Restoration via Category Management

**Exam scenario:** Automated review has 52% false positives on style, 48% on documentation, 8% on security, 18% on performance. Developers dismiss all findings.

- ✅ **Temporarily disable high-false-positive categories** (style, naming, documentation); keep only high-precision categories while improving prompts
- ❌ Display confidence scores (still shows all findings; trust still eroded)
- ❌ Add few-shot examples across all categories over several weeks (slow; trust continues to erode)
- ❌ Uniform strictness reduction (damages high-precision categories unnecessarily)

**Why:** High-false-positive categories cause developers to dismiss everything, including real findings in accurate categories. Surgical disabling stops the trust bleed while you fix the noisy categories.

---

## 4.11 Context-Aware Suggestions (Deduplication)

**Exam scenario:** Automated tool suggests 10 test cases for a PR, but 6 duplicate existing tests.
- ✅ Include the existing test file in context — Claude can only avoid duplicates if it knows what exists
- ❌ Reduce requested count to 5 (assumes priority ordering)
- ❌ Post-process with keyword matching (fragile, misses semantic duplicates)

---

## 4.12 Clarification Strategy — Proceed vs Ask

**When users send vague requests:**
- Do NOT ask 4+ clarifying questions (causes 35–40% abandonment)
- ✅ State assumptions explicitly and proceed, inviting corrections
- ❌ Ask all questions in one compound message (still demands effort from user)
- ❌ Use hidden defaults (user unaware of what was assumed)

**Exam pattern:** "Can you help with the report?" / "Book a venue for the party"
- ✅ Proceed with stated reasonable assumptions
- This applies both to user-facing assistants AND multi-agent systems (synthesis agent should not block awaiting coordinator clarification on all gaps)

---

## 4.13 Behavioral Drift Mitigation

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
