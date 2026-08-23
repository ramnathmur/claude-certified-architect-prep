# Chapter 9: Paying once for what does not change

## A budget cut with no matching drop in ticket volume

Finance caps a support bot's monthly API spend at a fixed figure, effective the following billing cycle, with no corresponding reduction in ticket volume. The engineering team did not ask for the constraint and cannot negotiate the ticket count down. Every request the bot handles carries the same long system prompt and the same set of tool definitions, unchanged from the message before it and the message before that. Only the customer's own question is different, turn to turn.

That repetition is the whole opportunity. Most of what the model reads on every single call is identical to what it read on the last one, and paying full price to reprocess it every time is spending the budget on work already done.

## A set left standing between performances

A theatre running the same production for a month does not strike the set and rebuild it before every show. The backdrop, the furniture, and the fixed pieces of the stage stay exactly where they were left, night after night, and only the specific beats of that night's blocking get attention before the curtain rises. Leaving the set standing only pays off because the same production runs again soon, and only because the set stays genuinely untouched. Move one flat between shows, and the crew spends the night rebuilding it.

Prompt caching is that arrangement applied to a request. The model does real work turning your prompt into the internal form it reasons over, and on an ordinary request that work is thrown away once the response is sent. Caching keeps it instead: the first request writes the processing done on a stretch of the prompt to a cache, and a later request that sends the identical content up to the same point reads that work back rather than redoing it. Whether this is worth doing at all rests on three properties, and all three have to hold.

**The set has to be identical.** A cache is matched on an exact prefix. Anything different before the point marked as the boundary, even a single added word or a reordered sentence, means the whole prefix is treated as a new set: rebuilt from nothing, cached work included. This is why the technique fits a system prompt and a tool schema, which do not change turn to turn, and fails against anything meant to reflect the current moment, because content that changes every request never matches a previous one closely enough to read from cache.

**The show has to run again, and soon.** A cache write costs more than an ordinary request: a premium of roughly a quarter more for a five-minute hold, doubled for an hour-long one. It only earns that premium back if the same prefix is read again before the hold expires. A cached prefix reused several times a minute is a set reused every night. A prefix sent once and never again is a set built for a single, unrepeated performance, at a cost no read ever recovers.

**The set has to be worth building at all.** A cached prefix below a minimum length clears no threshold worth the write's premium. A short, stable prompt repeated often still earns little back, because there was little processing cost to save in the first place.

## Where the boundary actually goes is a deliberate decision

The boundary between the standing set and the night's specific performance is placed deliberately, before the first request goes out, by marking the last piece of content meant to be cached. The mechanism is a `cache_control` marker on that block, applied automatically as the conversation grows or set explicitly at a chosen point. Everything up to and including that mark is the set. Everything after it is the night's own performance, reprocessed every time because it is expected to be different every time.

Placing that boundary carries real consequences on both sides of it. Put the mark too early, ahead of content that actually varies, and the read never happens: the supposedly cached prefix keeps changing, so every request rewrites instead of reusing. Put it too late, past content that is genuinely stable, and stable material sits on the wrong side of the boundary, reprocessed at full price for no reason. This placement decision is what people mean by cache check-pointing: a choice made about a specific request shape, revisited whenever that shape changes.

Invalidation is what happens when the placement stops matching reality. A system prompt cached with yesterday's date embedded in it invalidates on every request the moment the date changes: a volatile detail was built into what was supposed to be fixed scenery. The fix is to move the date below the mark, into the part of the request that was always going to be rebuilt every time.

## Reading the bill after the show

A response carries a usage figure alongside its content, and reading it is how a caching decision gets checked rather than assumed. The figure separates input tokens from output tokens, and within input tokens, separates what was written to cache, what was read from cache, and what was processed at the ordinary rate. A request that shows a large cache-read figure against a small ordinary-rate figure is a set genuinely being reused. A request that shows the same size cache write on every single call, with no corresponding reads, is a set being rebuilt every night at a premium, never reused. The placement has failed one of the three properties above, most often the "identical" one.

That per-request figure is what cost modelling turns into a number a business recognizes. A cache read costs a small fraction of an ordinary input token; a cache write costs more than one. Multiplying each category by its own rate and summing across a day's or a month's traffic is the arithmetic that turns a technical decision about where a boundary sits into a monthly bill finance can compare against a budget. Checking that arithmetic before a request goes out, rather than after the invoice arrives, is available through a dedicated endpoint that returns a token count for a request body without running inference at all: the same measurement, taken in advance instead of read off a bill already spent.

## What caching cannot do

Caching reduces what a stable prefix costs to reprocess. It has no opinion on which model reads that prefix, and it changes nothing about the tradeoffs a model choice carries; that decision belongs to a separate chapter entirely. Caching also cannot make volatile content cheap. The fix for a prompt that reprocesses in full every time is moving the volatile part to where it was always going to be reprocessed anyway, leaving only what is genuinely stable above the mark.

## The tell

A stem describing a system prompt, a tool schema, or reference material sent unchanged across many requests, with a cost or latency concern attached, is asking about a cache boundary and where it should sit. A stem where a cache stopped paying off with no code change is asking which of the three properties broke. A stem asking how to check spend before a request goes out is asking about token counting.

## Self-test

**1. Select ONE.** A team caches a long system prompt used on every request. Reviewing usage data, they find every request shows a full cache write and no cache reads at all, for weeks.

A. The prefix is too short to clear the caching threshold.
B. The cache's hold duration has expired between requests.
C. Something in the cached prefix changes on every request, so the exact-prefix match never succeeds.
D. The account needs a longer cache lifetime enabled.

**Answer: C.** A write with never a matching read, sustained over weeks rather than an occasional gap, points at the prefix failing to match itself from one request to the next: some volatile detail sits above the boundary. A and D would still show occasional reads under normal traffic. B would show intermittent misses tied to request timing, differing from the sustained, total absence of reads described here.

---

**2. Select ONE.** A request body includes a system prompt with today's date embedded in it, followed by a cache boundary, followed by the user's message. The team wants to fix a caching setup that never produces a cache hit.

A. Increase the cache's hold duration to a longer window.
B. Move the date below the cache boundary, into the part processed fresh on every request.
C. Add a second cache boundary earlier in the system prompt.
D. Switch to a smaller model so the prefix is cheaper to reprocess.

**Answer: B.** A date that changes daily sitting above the boundary breaks the exact-match requirement every day; moving it below the boundary leaves only genuinely stable content marked for caching. A longer hold does not help a prefix that changes daily regardless of hold length. C adds a boundary without removing the volatile content. D changes the per-token rate; it leaves the exact-match failure untouched.

---

**3. Select ONE.** A workload sends the same long reference document as part of its prompt, but only once, as a one-off request with no follow-up calls expected.

A. Mark a cache boundary after the reference document, since it is long and stable.
B. Do not cache; a prefix sent once with no expected repeat never earns back the write's premium.
C. Cache the user's own message instead, since it is the shortest part of the request.
D. Split the reference document into two shorter cache boundaries.

**Answer: B.** Caching only pays off when the same prefix is read again before its hold expires; a single, non-repeating request pays the write premium with no read ever following it. A assumes stability alone justifies caching, but recurrence is the second required property and it is absent here. C and D leave the same absence of repetition unaddressed.

---

**4. Select ONE.** A team wants to verify, before sending a batch of requests, whether a prompt's size is likely to approach the model's context window.

A. Send the request and read the usage block in the response afterward.
B. Use the token-counting endpoint to get a token count for the request body without running inference.
C. Estimate token count from the character length of the prompt.
D. Reduce the effort level, which lowers how many tokens a request consumes.

**Answer: B.** A dedicated counting endpoint returns the token count for a request body directly, before any generation happens, which is the only option here that checks size in advance rather than after the fact or by rough estimate. A only tells you after the call already ran. C is not a reliable substitute for an actual count. D affects generation; it leaves the size of the incoming request itself unchanged.
