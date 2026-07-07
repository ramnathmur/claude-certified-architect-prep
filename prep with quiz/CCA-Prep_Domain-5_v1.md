# Domain 5: Context Management & Reliability (15%)

**Source:** guide_en.MD — Chapters 12–13, Scenarios: Multi-agent Research, Customer Support, Conversational AI  
**Version:** 1.0 | 2026-06-27

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

**Exam pattern:**
- ✅ Case facts block outside summarization (survives context compression)
- ❌ Increase summarization threshold (still eventually gets compressed)
- ❌ Revise summarization prompt to preserve numbers (still relies on summarizer being perfect)
- ❌ External storage + retrieval (overkill for session-level facts)

---

## 5.5 Context Isolation with Subagents

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

## 5.6 Long-Term Conversation Memory

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

## 5.7 Conflict Detection and Source Attribution

When processing multiple conflicting sources, the agent should **not resolve conflicts autonomously**. Instead:
1. Complete analysis with both conflicting values
2. Explicitly annotate the conflict with source attribution
3. Let the coordinator (or human) reconcile

**Exam scenario:** Document analysis agent finds government report = 40% growth, industry analysis = 12% growth. Both credible.
- ✅ Complete analysis with both values, explicitly mark conflict with source attribution, let coordinator decide reconciliation
- ❌ Apply heuristics to pick most likely correct value (abandons responsibility for a decision above its scope)
- ❌ Stop and ask coordinator before completing analysis (blocks pipeline unnecessarily)

---

## 5.8 Scratchpad Files for Large Tasks

For tasks requiring state across many tool calls (large migrations, refactoring projects):
- Write intermediate state to a scratchpad file rather than holding it all in context
- Read from scratchpad at the start of each continuation
- This allows the task to survive context limits

---

## 5.9 Conversation-Level State Management

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

## 5.10 Reliability Patterns Summary

| Problem | Root Cause | Solution Pattern |
|---|---|---|
| Agent loop never terminates | Not checking `stop_reason` | Check `stop_reason: "end_turn"` to exit loop |
| Precision lost in long conversations | Transactional facts compressed in summarization | Persistent case-facts block outside summarized history |
| Subagent lacks upstream results | Context isolation — subagent doesn't inherit coordinator's history | Coordinator explicitly passes needed results in subagent prompt |
| Critical info missed in large input | Lost in the middle | Key-findings summary at start + section headings |
| Context window exhausted during discovery | Discovery output floods main session | Explore subagent for discovery; returns summary |
| Behavioral drift after many turns | Accumulated assistant responses dilute system prompt | Inject reminders at breakpoints; use few-shot over verbose rules |
| Data format inconsistency across tools | Multiple tools return different formats | PostToolUse hook for centralized normalization |
