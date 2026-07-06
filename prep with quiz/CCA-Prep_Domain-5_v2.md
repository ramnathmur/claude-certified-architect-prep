# Domain 5: Context Management & Reliability (15%)

**Source:** guide_en.MD — Chapters 9, 11–13, Scenarios: Multi-agent Research, Customer Support, Conversational AI; Official CCA-F Exam Guide Task Statements 5.1–5.6  
**Version:** 2.0 | 2026-07-06  
**Changelog v2:** Added §5.5 (Trimming Verbose Tool Outputs — task 5.1/5.4 depth), §5.8 (Escalation & Ambiguity Resolution — task 5.2, previously missing), §5.9 (Human Oversight & Confidence Calibration — task 5.5, previously missing), §5.11 (Provenance depth: claim→source mapping, publication dates, render-by-content-type — task 5.6). Expanded §5.12 with structured state persistence for crash recovery. Updated §5.14 summary table. All v1 content retained; sections renumbered.

---

## 5.1 Stateless API — The Fundamental Constraint

Claude's API is **fully stateless**. Every API call is independent. Claude has no server-side memory or session state.

**Implication:** Every request must include the complete conversation history in the `messages` array. Without this, Claude has no knowledge of prior turns.

**Exam scenario:** User says "I love jazz" in turn 1. Two turns later, Claude asks "What genres do you enjoy?"
- Root cause: ✅ Application is not including prior messages in the `messages` array
- Not: context window exceeded (impossible in a 3-turn conversation)
- Not: Claude needs a `session_id` parameter (doesn't exist)
- Not: Claude needs a vector database for memory (not the core API behavior)

**Exam scenario:** Latency and cost increase as conversations grow past 50 turns.
- Root cause: ✅ The entire conversation history is included with each API request — more turns = more tokens = more cost and latency
- Not: model generates progressively longer responses
- Not: database operations slowing down

---

## 5.2 "Lost in the Middle" Phenomenon

### What It Is
When large input is provided, Claude reliably processes content at the **beginning and end** of the context but has degraded attention on content in the **middle** of long inputs.

### Mitigation Strategies

1. **Key-findings summary at the start** — put the most critical information in the most reliably processed position (primacy)
2. **Explicit section headings** throughout — help the model navigate mid-input content
3. **Structured data over verbose content** — have upstream agents return key facts + citations rather than full page content + reasoning traces

**Exam scenario:** Synthesis agent processing 75K token input reliably uses first 15K (headlines) and last 10K (conclusions) but misses critical findings in middle 50K.
- ✅ Place key-findings summary at the start; add explicit section headings throughout
- ❌ Summarize to under 20K (might lose critical information)
- ❌ Alternate which agent appears first (rotation doesn't fix the fundamental attention pattern)

**Exam scenario:** 155K token combined output (85K web + 70K docs) but synthesis works best under 50K.
- ✅ Modify upstream agents to return structured data (key facts, quotes, relevance scores) instead of verbose content and reasoning traces — fixes root cause at the source
- ❌ Add intermediate summarization agent (adds latency, another potential point of failure)

---

## 5.3 Context Window Management Strategies

### Hybrid Approach (Most Tested)
For long conversations needing context management:
1. **Extract critical structured data** (amounts, dates, IDs, allergies, agreed prices) into a compact structured block — preserved verbatim
2. **Summarize general discussion** — compress lower-information-density exchanges
3. **Keep recent exchanges verbatim** — maintain conversational coherence for current turn

**Why not pure summarization:** Precision is lost. Amounts like "the 15% discount I mentioned" become "promotional pricing was discussed."

**Exam scenario:** 40-minute cooking session reaches 78K tokens. Contains: allergies, recipe scaling, clarified terms, general chatter.
- ✅ Extract allergies/quantities into structured block, summarize general discussion, keep recent exchanges verbatim
- ❌ Summarize entire history (loses allergy precision — safety risk)
- ❌ Keep only most recent 20K tokens (loses allergies if mentioned early)

---

## 5.4 Transactional Facts Persistence

**Problem pattern:** In long customer support conversations, precise amounts/dates/numbers get summarized into vague references.
- "The 15% discount I mentioned 20+ turns ago" → "promotional pricing was discussed"

**Solution:** Extract transactional facts into a **persistent "case facts" block** included in every prompt, outside the summarized history.

```
=== CASE FACTS (updated whenever a new fact appears) ===
Customer ID: CUST-12345
Order ID: ORD-67890
Order Amount: $89.99
Issue: Damaged item on delivery
Status: Pending manager approval
===
```

**Exam pattern:**
- ✅ Case facts block outside summarization (survives context compression)
- ❌ Increase summarization threshold (still eventually gets compressed)
- ❌ Revise summarization prompt to preserve numbers (still relies on summarizer being perfect)
- ❌ External storage + retrieval (overkill for session-level facts)

---

## 5.5 Trimming Verbose Tool Outputs

Tool results accumulate in context and **consume tokens disproportionately to their relevance**. A single `lookup_order` call can return 40+ fields when only 5 matter for the current task — and every one of those fields stays in the conversation for every subsequent turn.

**Solution:** Trim tool outputs to only the relevant fields **before** they enter context — e.g., via a `PostToolUse` hook:

```python
# PostToolUse hook: keep only return-relevant fields
@hook("PostToolUse", tool="lookup_order")
def trim_order_fields(result):
    return {
        "order_id": result["order_id"],
        "status": result["status"],
        "total": result["total"],
        "items": result["items"],
        "return_eligible": result["return_eligible"]
    }
```

This conserves context and reduces noise — the model isn't distracted by irrelevant fields, and long multi-issue sessions don't exhaust the window on tool clutter.

**Exam pattern:**
- ✅ PostToolUse hook filters tool results to relevant fields before they accumulate in context
- ❌ Ask the model in the system prompt to "ignore irrelevant fields" (the tokens are still consumed; attention cost remains)
- ❌ Summarize the whole conversation more aggressively (treats the symptom — verbose tool results keep flooding in)
- ❌ Increase the context window / switch to a larger model (cost goes up; noise problem remains)

---

## 5.6 Context Isolation with Subagents

Subagents receive only what the coordinator explicitly passes. This is both a constraint and a feature.

**As a feature (context isolation for exploration):**
- Use an Explore subagent to run verbose discovery (hundreds of call sites, large output)
- Subagent returns a concise summary to the main conversation
- Main session context preserved for design and implementation phases

**Exam scenario:** Adding error-handling wrappers across 120-file codebase. Phase 1 (discovery) fills context window before completion.
- ✅ Use Explore subagent for Phase 1 to isolate verbose output; returns summary; Phases 2–3 run in main conversation
- ❌ Use `/compact` mid-task (loses precision needed for implementation)
- ❌ Multiple sessions with `--continue` (coordination overhead, consistency risk)

---

## 5.7 Long-Term Conversation Memory

For conversations spanning many sessions (e.g., book club discussions over 3 months, 85K tokens):
- Rolling window: loses early sessions
- Progressive summarization: loses specific quoted conclusions
- ✅ **Semantic retrieval** (embeddings over full history) — retrieves specifically relevant past exchanges on demand

**Exam scenario:** "What did we conclude about the theme of isolation?" — needs specific past exchange.
- ✅ Semantic embeddings with retrieval of relevant exchanges
- ❌ Rolling window (discards most history)
- ❌ Progressive summarization (compresses specific conclusions into abstractions)
- ❌ XML tags marking discussion conclusions (doesn't solve retrieval at this scale)

---

## 5.8 Escalation and Ambiguity Resolution

### Reliable Escalation Triggers (Structural Signals)

| Situation | Action |
|---|---|
| Customer explicitly asks for a human/manager | Escalate immediately; do NOT attempt to solve first |
| Policy is silent or ambiguous on the request | Escalate (e.g., competitor price matching when policy only covers own-site adjustments) |
| Agent cannot make meaningful progress | Escalate after a reasonable number of attempts |
| Financial operation above a threshold | Escalate — preferably enforced via a hook, not just a prompt |
| Repeated tool/lookup failures | Escalate with what was attempted |

### Unreliable Complexity Proxies

**Sentiment and model self-confidence are NOT reliable escalation signals:**

| Unreliable proxy | Why it fails |
|---|---|
| Sentiment analysis | Customer mood does not correlate with case complexity — a calm message can describe a genuinely complex case; an angry one can be trivially resolvable |
| Model self-rated confidence (e.g., 1–10) | The model can be confidently wrong; uncalibrated self-reported confidence is poorly correlated with actual difficulty |
| Automatic complexity classifier | Overengineering; requires training data you likely don't have |

Escalate on **structural signals** — policy limits, missing data, explicit human requests, repeated failures — not on inferred emotion or self-assessed confidence.

### Escalation Patterns

**Immediate escalation** (explicit request):
```
Customer: "I want to speak to a manager"
Agent: [immediately calls escalate_to_human]
NOT: "I can help with your issue, let me first..."
```

**Nuanced escalation** (frustration ≠ human request):
```
Customer: "This is outrageous, I'm very unhappy!"
Agent: [acknowledges frustration] → [offers concrete resolution]
Customer: "No, I want to talk to someone!"
Agent: [customer reiterates → escalate immediately]
```
Key principle: acknowledge emotion, propose a solution, escalate only if the customer reiterates the desire for a human. First expression of dissatisfaction is not a request for a manager.

### Multiple-Match Disambiguation

When a customer lookup returns **several matching records**, the agent must **request additional identifiers** (email, order number, phone) — never pick a match by heuristic.

**Exam pattern:**
- ✅ "I found several accounts under that name — could you confirm the email or order number?" (clarification via additional identifiers)
- ❌ Select the most recently active account (heuristic selection → misidentified accounts, incorrect refunds)
- ❌ Select the first result returned by the tool (arbitrary; same misidentification risk)
- ❌ Escalate to a human immediately (unnecessary — the ambiguity is resolvable by asking)

**Exam pattern (escalation design):**
- ✅ Add explicit escalation criteria with few-shot examples to the system prompt showing when to escalate vs. resolve autonomously
- ❌ Escalate whenever sentiment analysis detects anger (mood ≠ complexity; floods human queue with resolvable cases)
- ❌ Have the model rate its own confidence 1–10 and escalate below 7 (self-reported confidence is uncalibrated and unreliable)
- ❌ Never escalate until three resolution attempts have been made (violates the immediate-escalation rule for explicit human requests)

---

## 5.9 Human Oversight and Confidence Calibration

For high-volume extraction/processing systems (e.g., document data extraction), design the human review workflow around **calibrated confidence** and **stratified measurement** — official task 5.5.

### Field-Level Confidence Scores, Calibrated

1. **Field-level confidence:** the model outputs a confidence score per extracted field (not one score per document)
2. **Calibration:** tune review thresholds against a **labeled validation set** — raw self-reported confidence is unreliable until calibrated against ground truth
3. **Routing:**
   - High confidence + validated stable accuracy → automated processing
   - Low confidence, or ambiguous/contradictory source documents → human review

This prioritizes limited reviewer capacity where it matters most.

### Stratified Random Sampling

Even for high-confidence extractions, **regularly audit a random sample** — stratified across document types and field categories, not just the top of the review queue. This measures the true error rate of the automated path and detects **novel error patterns** before they compound.

### The Aggregate-Accuracy Masking Trap

**An aggregate 97% accuracy can hide a 40% failure rate on one rare document type.** Overall metrics average away segment-level failures. Before reducing human review, validate accuracy **by document type and by field** — every segment must independently meet the bar.

**Exam scenario:** Extraction system shows 97% overall accuracy; team proposes auto-processing all high-confidence extractions.
- ✅ First analyze accuracy by document type and field segment; implement stratified random sampling of high-confidence extractions for ongoing error measurement
- ❌ Auto-process everything above the aggregate confidence threshold (aggregate masks per-segment failure — a rare document type may fail 40% of the time)
- ❌ Trust the model's self-reported confidence directly without calibration (uncalibrated confidence is unreliable; thresholds must be tuned on a labeled validation set)
- ❌ Review only the extractions flagged lowest-confidence and skip auditing the high-confidence stream (novel error patterns in the automated path go undetected)
- ❌ Sample only from the most common document type (the rare, worst-performing segments are exactly the ones under-sampled)

**Exam pattern (review routing):**
- ✅ Route low-confidence and ambiguous/contradictory-source extractions to human review; auto-process only segments with validated accuracy
- ❌ Route a fixed 10% of all documents to review at random, unstratified (wastes reviewer capacity on easy segments, undersamples problem segments)
- ❌ Have humans re-review every document (defeats automation; doesn't scale — the point of calibration is targeted oversight)

---

## 5.10 Conflict Detection and Source Attribution

When processing multiple conflicting sources, the agent should **not resolve conflicts autonomously**. Instead:
1. Complete analysis with both conflicting values
2. Explicitly annotate the conflict with source attribution
3. Let the coordinator (or human) reconcile

**Exam scenario:** Document analysis agent finds government report = 40% growth, industry analysis = 12% growth. Both credible.
- ✅ Complete analysis with both values, explicitly mark conflict with source attribution, let coordinator decide reconciliation
- ❌ Apply heuristics to pick most likely correct value (abandons responsibility for a decision above its scope)
- ❌ Stop and ask coordinator before completing analysis (blocks pipeline unnecessarily)

---

## 5.11 Provenance: Claim→Source Mapping, Dates, and Rendering

Official task 5.6 goes beyond conflict annotation: provenance must **survive synthesis**.

### The Attribution Loss Problem

Source attribution is lost during summarization when findings are compressed without preserving claim→source mappings:

```
Bad:  "The AI music market is estimated at $3.2B."   (no source, no year)

Good:
{
  "claim": "The AI music market is estimated at $3.2B.",
  "source_url": "https://example.com/report",
  "source_name": "Global AI Music Report 2024",
  "publication_date": "2024-06-15",
  "confidence": 0.9
}
```

Require subagents to output **structured claim→source mappings** (source URL/document name + relevant excerpt/location), and require downstream synthesis agents to **preserve and merge** these mappings — so the final report can attribute every claim.

### Publication Dates Prevent False Contradictions

Without dates, **temporal differences get misinterpreted as contradictions**:

```
Bad:  "Source A says 10%, source B says 15%. Contradiction."
Good: "Source A (2023) says 10%, source B (2024) says 15%. Likely +5% growth over a year."
```

Require publication or data-collection dates in every structured output. Two sources "disagreeing" may simply describe different time periods.

### Render by Content Type

Don't flatten everything to uniform prose in synthesis outputs:
- Financial/tabular data → **tables**
- News and analysis → **prose**
- Technical findings → **structured lists**
- Time series → **chronological ordering**

**Exam pattern:**
- ✅ Subagents emit structured claim→source mappings with publication dates; synthesis preserves them; report renders each content type appropriately
- ❌ Have the synthesis agent add a general bibliography at the end (individual claims are no longer traceable to specific sources)
- ❌ Flag every numeric disagreement between sources as a conflict (without dates, normal temporal change is misreported as contradiction)
- ❌ Convert all findings to uniform narrative prose for consistency (tabular financial data becomes imprecise and harder to verify)
- ❌ Re-derive attributions at the end by searching sources again (expensive, error-prone; the mapping should be preserved through the pipeline, not reconstructed)

Also structure final reports with explicit sections distinguishing **well-established findings** from **contested ones**, preserving original source characterizations and methodological context.

---

## 5.12 Scratchpad Files and Structured State Persistence

### Scratchpad Files for Large Tasks

For tasks requiring state across many tool calls (large migrations, refactoring projects, long investigations):
- Write intermediate state and key findings to a scratchpad file rather than holding it all in context
- Read from scratchpad at the start of each continuation
- This allows the task to survive context limits — and counteracts **context degradation**, where the model starts giving inconsistent answers and referencing "typical patterns" instead of the specific classes it discovered earlier

```
# investigation-scratchpad.md
## Key findings
- PaymentProcessor in src/payments/processor.ts inherits from BaseProcessor
- refund() is called from 3 places: OrderController, AdminPanel, CronJob
- External PaymentGateway API has a rate limit of 100 req/min
```

### Structured State Persistence for Crash Recovery

In multi-agent systems, each agent **exports its state to a known location**, and the coordinator **loads a manifest on resume**:

```json
// agent-state/web-search-agent.json
{ "status": "completed", "queries_executed": [...], "key_findings": [...],
  "coverage": ["music composition"], "gaps": ["music licensing"] }

// agent-state/manifest.json
{ "web-search": "completed", "doc-analysis": "in_progress", "synthesis": "not_started" }
```

On crash or restart, the coordinator reads the manifest, injects persisted findings into agent prompts, and **resumes from the checkpoint** instead of re-running the full investigation.

**Exam pattern:**
- ✅ Each agent exports structured state (status, findings, coverage, gaps) to a known location; coordinator loads manifest on resume and injects summaries into agent prompts
- ❌ Rely on conversation history to survive the crash (the API is stateless; an interrupted session's context is gone)
- ❌ Re-run the entire investigation from scratch after every failure (wastes hours of completed work that could have been persisted)
- ❌ Have agents keep all findings in their own context windows (context fills; nothing survives a crash)

---

## 5.13 Conversation-Level State Management

### The Sliding Window Problem
Keeping only the last N message pairs drops early preferences that may be critical later.

**Hybrid window approach:**
- Keep recent exchanges verbatim (sliding window)
- Maintain a running summary of earlier exchanges (compressed)
- Never drop the structured facts block

### System Prompt Instruction Drift
As conversations lengthen, system prompt authority diminishes relative to accumulated assistant responses.

**Preventive patterns:**
- Inject reminder messages at conversation breakpoints (reinforcement)
- Keep system prompt rules concrete and minimal (abstract rules drift faster than examples)
- Replace verbose rule lists with few-shot examples (examples maintain behavioral pattern longer)

---

## 5.14 Reliability Patterns Summary

| Problem | Root Cause | Solution Pattern |
|---|---|---|
| Agent loop never terminates | Not checking `stop_reason` | Check `stop_reason: "end_turn"` to exit loop |
| Precision lost in long conversations | Transactional facts compressed in summarization | Persistent case-facts block outside summarized history |
| Context bloat from tool calls | Verbose tool results (40+ fields) accumulate turn after turn | PostToolUse hook trims results to relevant fields |
| Subagent lacks upstream results | Context isolation — subagent doesn't inherit coordinator's history | Coordinator explicitly passes needed results in subagent prompt |
| Critical info missed in large input | Lost in the middle | Key-findings summary at start + section headings |
| Context window exhausted during discovery | Discovery output floods main session | Explore subagent for discovery; returns summary |
| Human queue flooded / wrong cases escalated | Sentiment or self-rated confidence used as complexity proxy | Escalate on structural signals: explicit requests, policy gaps, repeated failures |
| Wrong customer actioned | Heuristic selection among multiple lookup matches | Request additional identifiers to disambiguate |
| Errors slip through automated processing | Aggregate accuracy masks per-segment failure | Calibrated field-level confidence + stratified sampling + per-type/per-field accuracy tracking |
| Final report can't attribute claims | Claim→source mapping lost in summarization | Structured claim→source mappings preserved through synthesis |
| Sources falsely flagged as contradicting | Missing publication dates hide temporal differences | Require publication/collection dates in structured outputs |
| Work lost on crash | No persisted agent state | Structured state exports + manifest loaded on resume |
| Behavioral drift after many turns | Accumulated assistant responses dilute system prompt | Inject reminders at breakpoints; use few-shot over verbose rules |
| Data format inconsistency across tools | Multiple tools return different formats | PostToolUse hook for centralized normalization |
