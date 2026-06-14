# CCA-F Integration Checkpoint A — Customer Support Resolution Agent (D1 × D5)
_Cross-domain · exam Scenario 1 · ~20 min · design cold, then compare_

## Why this checkpoint exists

Domain 1 (escalation logic, structured handoffs, graceful degradation) and Domain 5 (multi-turn context management, compaction, prompt caching) are taught in separate modules, so you can pass each in isolation while still failing where they collide. Exam Scenario 1 — the Customer Support Resolution Agent — is built precisely on that collision: a single 10-turn conversation that must manage its own context *and* escalate correctly *and* survive a tool failure, all at once. The transfer failure this checkpoint hunts: designing a clean compaction strategy that quietly discards the very facts the escalation handoff later needs.

## The scenario

You are architecting a customer support resolution agent for a SaaS billing product. Constraints:

- **Model:** Claude Sonnet 4.6 (1M-token window, context-aware), Messages API, multi-turn.
- **Conversation length:** up to **10 turns**. The customer states a complaint in **turn 1** (a duplicate charge of **$240** on invoice INV-8842), and the resolution may not arrive until turn 9–10.
- **Knowledge base:** a **~30,000-token** product/billing policy KB (refund rules, dunning policy, tier definitions) that is **identical on every turn** and must be available to the model throughout.
- **Tools:** `lookup_account`, `get_invoice`, `issue_refund` (a write), `escalate_to_human`. The `issue_refund` tool can return an **uncertain write state** (timeout after the request was sent).
- **Token discipline:** keep per-turn input lean; you have decided to enable **server-side compaction** with the trigger configured so history is summarized once the conversation grows large (the default trigger is 150,000 input tokens, configurable down to a minimum of 50,000), and you also keep the KB cached so you are not re-billed full price for 30K tokens every turn.
- **Escalation:** some cases must go to a human — and when they do, the human must receive a usable handoff, **not** a transcript dump.
- **Reliability:** if `issue_refund` times out, the agent must **degrade gracefully** — never claim the refund succeeded if it cannot confirm it.

Design the agent so that after history is compacted following the early turns, the agent at turn 10 can *still* correctly escalate the original $240 duplicate-charge complaint with a complete handoff.

## Design it cold (do this before scrolling)

Answer from memory. Span BOTH domains, and especially their interaction.

1. **Cache placement (D5):** Where exactly does `cache_control` go relative to the 30K KB, and why must the KB sit *before* the per-conversation content rather than after it? What ordering does the cache prefix follow?
2. **Compaction vs. the complaint (D1×D5):** Compaction summarizes and then **drops** everything before the `compaction` block on the next request. The turn-1 complaint ($240 duplicate on INV-8842) is the oldest message. What mechanism guarantees that fact survives compaction so the turn-10 escalation handoff can carry it?
3. **What must never be compacted away (D5):** Name the class of facts (exact amounts, invoice IDs, the verbatim complaint) that lose fidelity if folded into vague prose, and the strategy that protects them.
4. **Escalation trigger (D1):** What actually fires an escalation here — and what is the wrong trigger that the exam baits you with?
5. **Handoff payload (D1):** List the structured fields the handoff to the human carries. What must it NOT be?
6. **Cache ↔ compaction collision (D1×D5):** Compaction changes the `messages` array. Does that invalidate your KB cache? Where in the `tools → system → messages` hierarchy is the KB, and why does that placement protect it from history changes?
7. **Token budget layout (D5):** Sketch how you allocate the window across (a) stable cached prefix, (b) growing history, (c) reserved output. Which part do you cache and which part do you compact?

---

## Model architecture (compare your design)

### Context strategy (D5)

**Cache the stable prefix, before the variable per-turn content.** `cache_control` is placed on the **last content block of the reusable prefix** — everything from the start of the request up to and including that marked block becomes the cached prefix (citation: prompt-caching-economics §F1, §B1). The cache always covers a **contiguous prefix in `tools → system → messages` order** — "Cache prefixes are created in the following order: `tools`, `system`, then `messages`" — so you cannot cache a middle slice (prompt-caching-economics §B4). Put the 30K KB in the **`system`** block (or a system content block) and the breakpoint at its end; the per-turn customer message lands in `messages`, *after* the breakpoint, so it never busts the prefix.

- On Sonnet 4.6 the **minimum cacheable prefix is 1,024 tokens** — the 30K KB clears it easily (prompt-caching-economics §B5; context-management-reliability §9).
- Economics: a cache **read costs 0.1× base input**; 5-min write is 1.25×, so caching **pays off after the first reuse** — exactly the 10-turn shape here (prompt-caching-economics §D1, §D3). The default 5-min TTL **refreshes for free on every hit**, so a continuously-used KB stays warm across all 10 turns (prompt-caching-economics §C).
- **Anti-pattern caught:** never inject dynamic content (timestamp, customer name, session vars) *into* the cached system prefix — it changes the prefix and busts the cache; that content goes *after* the breakpoint (prompt-caching-economics §F2; EXAM-DIGEST D5 anti-patterns: "Placing `cache_control` before content that changes every turn").

**Preserve the complaint across compaction — do not rely on the summary to remember it.** Server-side compaction (1) detects the trigger threshold, (2) generates a summary, (3) creates a `compaction` block, (4) continues from it; on subsequent requests "the API automatically drops all message blocks prior to the `compaction` block" (context-management-reliability §4). The risk: "overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later" (context-management-reliability §4, citing effective-context-engineering). Two reinforcing protections:

1. **Structured state object** — keep a canonical JSON (issue, invoice_id, amount, root_cause, actions_taken, status) that is "more reliable than inferring from a long transcript" (EXAM-DIGEST D5). It lives *after* the compaction point (in the recent, non-dropped messages or re-injected each turn), so the $240 / INV-8842 facts survive verbatim regardless of how the prose summary turns out.
2. **Custom compaction `instructions`** — the `instructions` parameter (default `null`) replaces the default summarization prompt; instruct it to preserve the original complaint, invoice ID, exact amount, and any actions already taken (context-management-reliability §4, parameters). This raises recall; the structured state object is the belt-and-suspenders backstop.

**Exact facts go to a fact/state store, not into prose.** Amounts, invoice IDs, and the verbatim complaint are exactly the values that "summarizing *exact facts* into vague prose" destroys (EXAM-DIGEST D5 anti-patterns). The retrieval/fact-store and structured-state-object strategies exist for "exact p-values, quotes, thresholds — summaries lose precision" (EXAM-DIGEST D5). $240 must stay $240, not "around $240."

**Compaction ↔ cache interaction.** Compaction edits the **`messages`** array (it inserts a `compaction` block and drops earlier messages). Cache invalidation cascades **`tools → system → messages`** and "changes at each level invalidate that level and all subsequent levels" (prompt-caching-economics §B6). Because the KB cache breakpoint sits in **`system`** (a strictly earlier level), changes to `messages` from compaction do **not** invalidate the KB cache — the expensive 30K prefix stays cached even as history is rewritten. (This is the payoff of putting the KB in `system`, not in an early user message.)

> Token-budget note: caching reduces the **cost** of re-sending the stable prefix but "does not reduce window occupancy" / "does not enlarge the context window" (context-management-reliability §2, §9; prompt-caching-economics §F7). Compaction is what keeps the *window* from filling; caching is what keeps the *bill* down. They solve different axes — you need both.

### Escalation logic (D1)

**Escalate by category and impact, not by a fail counter.** Escalate when the user asks for a human, the issue needs authority the agent lacks, a policy exception / regulated approval / high-value transaction is involved, the agent can't make progress, or a tool reports an uncertain/unsafe state. **Do NOT use a simple "escalate after N failed tool calls" counter — category and impact matter more than count** (EXAM-DIGEST D1; orchestration-patterns context). For this scenario, the **uncertain-write state from `issue_refund`** is itself an escalation trigger (tool reports an uncertain/unsafe state).

**Structured handoff payload — not the transcript.** The handoff carries: `customer_id, issue_type, root_cause, relevant_records, amount, actions_taken, recommended_next_action` (EXAM-DIGEST D1). For this case: `issue_type=duplicate_charge`, `amount=$240`, `relevant_records=INV-8842`, `actions_taken=[refund attempted, state uncertain]`, `recommended_next_action=verify refund status before re-issuing`. **Anti-pattern:** "Escalating with no useful handoff; dumping the transcript" (EXAM-DIGEST D1 anti-patterns). Note the dependency: this payload is exactly what compaction would erase if you let the summary swallow the complaint — which is why the structured state object (above) feeds the handoff.

### Graceful degradation (D1)

On the `issue_refund` timeout (uncertain write): **state what was verified, what couldn't complete, offer next steps. Partial completion > fake success or a generic error. Never claim a side effect happened if it didn't** (EXAM-DIGEST D1). Critically, **do NOT auto-retry the uncertain write** — retrying uncertain writes creates duplicates (EXAM-DIGEST D1, D4). Report the uncertainty, surface it as an escalation, and let a human confirm whether the $240 refund actually posted.

### Token budget layout (D5)

- **(a) Stable cached prefix** — `tools` + `system` (incl. 30K KB) → cache it once, read at 0.1× for turns 2–10.
- **(b) Growing history** — the `messages` array → compact it (summary + structured state object after the compaction point).
- **(c) Reserved output** — `max_tokens` for the response. Sonnet 4.6 is context-aware: it receives `<budget:token_budget>` at start and `<system_warning>Token usage: X/Y; Z remaining</system_warning>` after each tool call, so it can self-manage remaining budget (context-management-reliability §1, §7).

## The cross-domain traps this checkpoint tests

- **Compacting away the complaint the handoff needs (D5 erases what D1 requires).** The $240 / INV-8842 facts are in the *oldest* messages — first to be summarized and dropped. If the only copy lives in the prose summary, the turn-10 escalation handoff arrives incomplete. Fix: structured state object + custom compaction `instructions` preserving exact facts.
- **Caching dynamic per-conversation content.** Putting the customer name / timestamp / per-turn state inside the cached system prefix busts the cache every turn (exact-match requires 100% identical segments). The cached layer must be the *stable* KB only; volatile content goes after the breakpoint.
- **Assuming compaction invalidates the KB cache (or vice-versa).** It does not — KB lives in `system`, compaction edits `messages` (a later level), and invalidation only cascades downward. Mis-modeling this leads architects to either skip caching ("compaction will bust it anyway") or skip compaction ("it'll wreck my cache"). You need both.
- **Escalating on a fail counter instead of by category.** "Refund tool failed twice → escalate" is the baited wrong answer. The real trigger is the **uncertain write state / authority needed**, regardless of attempt count.
- **Auto-retrying the uncertain refund.** Treating the timeout as a transient error and retrying `issue_refund` risks a duplicate $240 refund. Uncertain writes are reported, never blindly retried — and the partial state must be carried honestly into the handoff.

## Self-score

Award yourself a point for each, from your cold design:

- [ ] **Cache placement** — `cache_control` after the stable 30K KB prefix, in `system`, before per-turn content; ordering `tools → system → messages`.
- [ ] **Compaction-preserve rule** — a structured state object (and/or custom `instructions`) keeps the exact complaint ($240 / INV-8842) alive after the `compaction` block drops old messages.
- [ ] **Escalation by category** — fired by uncertain-write / authority / policy-exception, NOT a fail counter.
- [ ] **Handoff payload** — structured fields (`customer_id, issue_type, root_cause, relevant_records, amount, actions_taken, recommended_next_action`), not a transcript dump.
- [ ] **Bonus — cache/compaction non-collision** — explained why editing `messages` (compaction) does not invalidate the `system`-level KB cache.
- [ ] **Bonus — no auto-retry on uncertain write** — degrade gracefully, report uncertainty, never fake success.

**Target: 4/4 core checks.** Log any miss to `../GAPS.md` with: what was asked, what you designed, the correct mental model, and the one-sentence pattern to remember.
