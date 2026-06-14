# CCA-F Practice — Domain 5: Context Management & Reliability (15%)
_8 questions · original, exam-style · grounded in EXAM-DIGEST + D5 citations_

## Questions

**Q1.** A teammate reviewing your design doc writes: "We're on Opus 4.8 with a 1M-token window, so we can just keep dumping every prior turn, every full tool result, and the entire 400-page policy PDF into context — there's plenty of room, and accuracy will be fine." Which single statement is the most accurate correction of the underlying mistake?
- A) The 1M window is only available behind a beta header, so the plan won't work until that's enabled.
- B) Capacity is not the same as attention — recall and accuracy degrade as the window fills (context rot), so curating what's in context matters as much as how much fits.
- C) The plan is fine for Opus 4.8 specifically, because newer models have no context-rot effect at all.
- D) The plan fails only because tool results and thinking tokens don't count toward the window, throwing off the budget math.

**Q2.** An onboarding doc summarizes the CALM framework as "Compress, Anchor, **Limit**, Monitor." A new architect uses "Limit" to justify hard-capping the conversation at 20 turns and refusing any longer session. What is wrong here?
- A) Nothing — "Limit" correctly means capping turn count, and 20 is the recommended ceiling.
- B) The L stands for **Layer** (separating system vs. history vs. injected context), not "Limit"; capping turns is not what the framework prescribes.
- C) The framework is CALM = Compress, Anchor, Limit, Monitor, but the cap should be on tokens, not turns.
- D) CALM has no "L" component at all; the acronym is only CAM.

**Q3.** A research-assistant agent must, much later in a long session, cite the exact p-value (p = 0.013) and a verbatim quote from a paper it ingested 60 turns ago. Your context strategy currently replaces old turns with a running prose summary. The agent now reports "p was around 0.01-ish" and paraphrases the quote. Which strategy best fixes this specific failure?
- A) Increase the sliding-window size so more old turns are kept verbatim.
- B) Switch to a retrieval / fact store and look the exact value and quote up on demand, since summarization loses numeric and verbatim precision.
- C) Add a persistent reference section listing the paper's title and authors.
- D) Raise the progressive-summarization frequency so summaries are generated more often.

**Q4.** A returning user opens a support session that was last active three days ago. An engineer wants to "resume exactly where we left off" by re-injecting the full set of tool results (account balance, open tickets, shipment status) captured at the end of the prior session, verbatim. Why is this the wrong move, and what should happen instead?
- A) It's correct — replaying the old tool results guarantees continuity and saves API calls.
- B) Those embedded tool results are now stale; open with a structured summary of prior context and fetch fresh state from the live tools at resume time.
- C) The only problem is cost; replay the old results but mark them with a cache breakpoint to save tokens.
- D) Tool results can never be re-sent in a new session for security reasons, so the session simply cannot be resumed.

**Q5.** Midway through an active conversation, an external system reports that the customer's subscription tier just changed from Pro to Enterprise. The agent needs to act on the new tier for the rest of the session. How should this update be delivered into the model's context?
- A) Insert it as an unsolicited assistant message in the transcript so it reads naturally.
- B) Inject the fresh state into the system prompt / a dedicated context block, not as a fabricated assistant turn.
- C) Append it as a fake user message so the model treats it as a request.
- D) Do nothing in context; rely on the model to re-call a tool eventually and discover the change.

**Q6.** You are caching a stable prefix (tool definitions + system instructions + a long reference doc) that is identical on every turn, while the user's incoming message changes each turn. An engineer places the `cache_control` breakpoint on the user's per-turn message block "so the newest content gets cached too." On the next turn, `cache_creation_input_tokens` is high again and `cache_read_input_tokens` is near zero. What went wrong?
- A) Nothing — high `cache_creation` on every turn is the expected healthy steady state.
- B) The breakpoint must sit after the stable prefix and before the variable per-turn content; marking the changing message busts the prefix match every turn, forcing a fresh write.
- C) The prefix is below the minimum cacheable length, so caching silently failed.
- D) The 5-minute TTL expired between turns, which is the only possible cause of repeated writes.

**Q7.** A 5-minute-TTL prompt cache holds a 20,000-token stable prefix on Opus 4.8 (base input $5/MTok, 5-min write $6.25/MTok, cache read $0.50/MTok). Compared with sending that prefix uncached every time, at how many cache reads does caching first become cheaper overall, and why?
- A) It never pays off, because the 1.25x write premium always exceeds the read savings.
- B) After the very first cache read: one write (1.25x) plus one read (0.1x) = 1.35x total beats sending the prefix twice uncached (2.0x).
- C) Only after at least 10 reads, because writes are an order of magnitude more expensive than base input.
- D) After two reads, which is the break-even point for the 5-minute cache.

**Q8.** A production agent calls an external payment tool. The tool times out after the charge may or may not have been submitted (uncertain write state). Separately, the same agent's primary model occasionally returns transient 529 overload errors on read-only summary calls. Which pairing of reliability tactics is correct?
- A) Auto-retry the payment call immediately with backoff, and for the overloaded summary call, fail the whole session with a generic error.
- B) For the uncertain payment write, do NOT auto-retry (risk of duplicate charge) — report uncertainty / verify state; for the transient read failure, use retry with backoff and/or a fallback model.
- C) Apply retry-with-backoff uniformly to both, since backoff makes any retry safe.
- D) Open a circuit breaker on the payment tool after one timeout and never call it again this session; retry the summary call without limit.

---

## Answer Key

**Q1 — B.** A larger window raises capacity but not per-token salience; as tokens accumulate, recall and accuracy degrade (context rot), so curation matters as much as raw size. A is wrong (1M is the native window for Opus 4.8, no beta header); C is wrong (rot "applies across all models," only the rate differs); D states a true fact that isn't the core flaw. _Sub-topic: capacity ≠ attention / context rot · Difficulty: easy_

**Q2 — B.** CALM = Compress, Anchor, **Layer**, Monitor — Layer is about separating system vs. history vs. injected context, not limiting turns. "Limit" is the classic mis-memorization the exam tests. A, C, and D all carry the wrong "Limit"/missing-L premise forward. _Sub-topic: CALM (Layer not Limit) · Difficulty: easy_

**Q3 — B.** Exact p-values, thresholds, and verbatim quotes must come from a retrieval / fact store; progressive summarization compresses them into vague prose and loses precision. A is brittle and still token-bound; C keeps metadata but not the value; D summarizes more often, which loses precision faster, not less. _Sub-topic: retrieval/fact stores vs. summarization · Difficulty: med_

**Q4 — B.** Returning users should get a structured summary plus a fresh fetch of live state — embedded tool results captured days ago are stale and may be wrong (balance, tickets, shipment all move). A trusts stale data; C caches stale data (wrong content, not just cost); D invents a non-existent prohibition. _Sub-topic: returning users / fresh state vs. stale tool results · Difficulty: med_

**Q5 — B.** Mid-conversation external updates belong in the system prompt or a dedicated context block, injected as authoritative state — not faked as an assistant message (A) or user message (C), and not left to chance (D). Fabricated turns corrupt the transcript and mislead the model about who said what. _Sub-topic: external updates → system prompt, not assistant message · Difficulty: med_

**Q6 — B.** `cache_control` goes after the stable prefix and before the variable per-turn content. Marking the changing message means the cached prefix no longer matches on the next turn (cache hits require an identical prefix), so every turn re-writes — exactly the high-creation / near-zero-read signature observed. A misreads the health signal; C and D are possible in general but the symptom plus the described placement points squarely at a busted prefix. _Sub-topic: cache_control placement / usage fields · Difficulty: hard_

**Q7 — B.** For the 5-minute cache, one write (1.25x) + one read (0.1x) = 1.35x vs. 2.0x for two uncached sends, so caching wins at the first read. The doc states 5-minute caching "pays off after just one cache read." A ignores the 0.1x read; C overstates write cost; D is the break-even for the 1-hour (2x write) cache, not the 5-minute one. _Sub-topic: prompt-caching break-even math · Difficulty: hard_

**Q8 — B.** Uncertain writes must not be auto-retried (duplicate side effect, e.g., double charge) — report uncertainty and verify actual state; transient infra errors on safe/read calls are the textbook case for retry-with-backoff and fallback models. A retries the dangerous call and over-reacts to the safe one; C wrongly assumes backoff neutralizes duplication risk; D over-applies a circuit breaker to one timeout and removes the limit where it's needed. _Sub-topic: reliability patterns (retry/backoff, fallback, no-retry-on-uncertain-write) · Difficulty: hard_
