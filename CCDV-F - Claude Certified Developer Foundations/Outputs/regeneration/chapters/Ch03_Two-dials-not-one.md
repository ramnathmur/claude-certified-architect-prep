# Chapter 3: Two dials, not one

## Two questions before any work starts

Thinking is an old word doing new work. Outside the API, it means a mind working through a problem before it answers. Inside the API, it names two different arrangements, and a request has to say which one, because they run on different rules and switch on differently.

A translation bureau sells against the same split. A client hands over a document, and before any work starts, the bureau has to settle two separate questions. Who translates it: the fast generalist, the senior all-rounder, or the specialist reserved for the documents nobody else in the building is trusted with. And, separately, how long that translator is allowed to sit with it before the draft goes out.

Neither question answers the other. One is answered by which model the request names. The other is answered by how the `thinking` parameter and the effort setting are configured for that call. They are chosen separately, set separately, and one of them can change on a Tuesday while the other stays exactly where it was.

## Who does the work, and how hard they work it

**Which translator.** The bureau keeps three translators on staff for ordinary jobs, and Claude's mainstream lineup maps onto them directly. The first is fast and general: strong everyday quality, sent high-volume work without a second thought. Anthropic describes the equivalent model, Claude Haiku 4.5, as "the fastest model with near-frontier intelligence." The second is the all-rounder who takes most of what lands on the desk: Claude Sonnet 5, "the best combination of speed and intelligence." The third is the specialist held back for contracts, filings, anything where a mistake is expensive: Claude Opus 5, positioned for "complex agentic coding and enterprise work." Anthropic's own use-case list sharpens this further: Haiku 4.5 for real-time applications and high-volume processing, Sonnet 5 for code generation, data analysis, and agentic tool use, Opus 5 for large-scale refactoring and multihour autonomous coding.

When it is not obvious which of the three fits, Anthropic's own guidance points to the specialist by default: "If you're unsure which model to use, start with Claude Opus 5 for complex agentic coding and enterprise work." That default sits above the cheapest tier and below the frontier tier reserved for the hardest cases anyone brings the bureau. A fourth translator holds that top spot, reserved for long-running, deep-reasoning work, at a price and a wait to match. Turnaround runs opposite to capability across all four: Haiku fastest, Sonnet fast, Opus moderate, the frontier tier slower still. Picking the tier is only half of what a request decides.

**How hard they work it.** The other half is a live, separate arrangement, and the API keeps two genuinely different versions of it under the one word "thinking." The first is a contract: a client sets a fixed number of hours per document, every document, whether it is a one-line label or a forty-page filing. That is extended thinking in manual mode: a request sets `thinking: {type: "enabled", budget_tokens: N}`, and Claude spends against that budget before answering, on every single call. The second is judgement: the translator uses their own sense of the document, spends real time where it is genuinely hard, and does not bother deliberating over a cover sheet. That is adaptive thinking. Claude weighs each request on its own and decides whether reasoning would help and how much. Anthropic states the difference plainly: "With a fixed budget, Claude thinks on every request. With adaptive thinking, Claude decides whether and how much to think on each request." A simple question can come back with no thinking block at all; a tangled, multistep one gets real deliberation; the same conversation can hold turns of both kinds.

Which of the two arrangements a given tier accepts is fixed per tier. A request cannot choose it freely, and the pattern runs against intuition. Claude Haiku 4.5 accepts only the contract: a fixed budget, set by hand, thinking switched off until told otherwise. Claude Opus 5 and Claude Sonnet 5 accept only judgement: adaptive thinking, already on, with no manual budget to set. Newer models carry fewer thinking controls than the ones they replaced. On the frontier tier, thinking cannot be switched off at all. The cheapest current model is the one still running the old, hands-on arrangement; the two stronger tiers already moved to the version where the translator decides. A stem that assumes the newest model must offer the most configuration has the relationship backward.

Inside whichever arrangement a tier runs, there is a further dial: how thoroughly to work at all. The API calls this effort, running from `low` up through `medium`, `high` (the default), `xhigh`, to `max`. Setting effort gives an instruction. It does not start a stopwatch. Anthropic is explicit: effort "is a behavioral signal, not a strict token budget. At lower effort levels, Claude will still think on sufficiently difficult problems, but it will think less than it would at higher effort levels for the same problem." A translator told to work at low effort still stops to untangle a genuinely ambiguous clause; they simply spend less time on everything else. A request that needs a guaranteed ceiling on spend, rather than a general instruction to hurry, needs a different, stricter instrument than effort, covered where token limits are covered.

Effort reaches beyond thinking, too. It governs the whole response: explanations, tool calls, everything Claude produces. At lower effort, Claude tends to fold several steps into fewer tool calls, skip the preamble, and close with a short confirmation instead of a summary, the same way a translator working quickly stops double-checking a term against the glossary and stops asking the client questions they would have asked at a higher setting. A scenario about an agent making too many needless calls to its own tools has effort as a live answer too, alongside thinking depth.

A third lever sits outside both columns: fast mode. It changes neither which translator is hired nor how they think; it pays a premium so the same translator prioritises the job and works faster, full stop. Anthropic's own description: fast mode "runs the same model with a faster inference configuration. There is no change to intelligence or capabilities." Set against effort, the difference is exact enough that Anthropic publishes it as a table: fast mode gives "same model quality, lower latency, higher cost"; a lower effort level gives "less thinking time, faster responses, potentially lower quality on complex tasks." Both cut latency. Only fast mode protects the answer. Only fast mode costs more per token to get there. Fast mode currently runs on the Opus tier only.

## Why the better fix is usually the second dial

Put the two columns next to each other and the rule falls out on its own. Anthropic frames model choice around four questions: what the workload needs to be capable of, how fast it must respond, what it can cost, and how much the effort dial alone closes the gap before a different tier is worth trying. The first three sort into column one. The fourth is column two's whole job, and it is usually the cheaper one to turn first.

Column one, which translator, is chosen once per workload, based on what the job requires: routine volume goes to Haiku, most everyday work goes to Sonnet, anything complex or high-stakes starts with Opus. Column two, how hard that translator works, is set per request, based on how much this particular document needs: a boilerplate cover letter gets low effort or no thinking at all under adaptive mode; a contract with an ambiguous clause gets high effort and real deliberation. Neither column tells you the other. A senior specialist can be told to work fast and loose on an easy job. A junior generalist can be told to take their time on a hard one, and taking more time makes them a more thorough version of themselves, still capped at their own ceiling.

Anthropic states the preference between the two directly: "Recent Opus and Sonnet models support an effort parameter that trades intelligence for latency and cost within a single model. Tuning effort is often a better lever than switching models." The reason is procedural as much as anything: the translator is already known and already trusted, and turning the effort dial down costs nothing but a parameter, where moving to a different translator means re-establishing whether the new one's work is good enough for the job in the first place.

Deciding to make either move is not a guess. Anthropic's own method: build a benchmark specific to the workload, run it against real prompts and real data, and compare accuracy, response quality, and edge-case handling before weighing the cost difference. That method applies whether the change under test is a new effort level or a different tier entirely; only the size of the change under test differs.

Anthropic documents two legitimate places to start, and neither is the universal opening move. Start efficiency-first: begin with Haiku 4.5, test the real workload, upgrade only where a specific capability gap shows up. That fits tight latency, high volume, or a cost-sensitive build. Or start capability-first: begin with Opus 5, optimise the prompt, then look for room to lower effort or step down a tier once the work is proven. That fits complex reasoning, close judgement calls, or anything where being wrong costs more than being slow. The stated constraint decides which of the two applies. The bureau's own new-client conversation settles exactly this, before any translator is assigned: which risk matters more here, being slow or being wrong.

## Same model family, four things that moved

Here is where a plausible plan goes wrong. A team runs an established workload against an older model in a family, with a manual thinking budget set on every request and a prompt tuned against that particular translator's habits. A new model in the same family ships. The team swaps the model ID string, changes nothing else, and deploys. On the surface, every feature says this is safe: same provider, same family, same request shape, same prompt. The mechanism disagrees, in four separate ways at once.

The manual thinking budget is the first casualty. If the new model has moved to adaptive-only, the parameter that used to set a fixed budget is no longer accepted, and the request fails outright instead of quietly running differently. Second, the model's own default has moved: where the old model only thought when told to, the new one may think by default, on every request, whether the team asked for it or not, changing both latency and cost without a single line of the prompt changing. Third, the tokenizer underneath is not the one the prompt was tuned against: Anthropic states that recent models produce roughly a third more tokens for the same text, so a `max_tokens` limit sized for the old tokenizer can now run out mid-response on requests that used to finish comfortably. Fourth, any effort level tuned by trial and error on the old model does not transfer. Anthropic's own advice is direct: "If you carried effort settings over from an earlier model, run a fresh effort sweep on your evals rather than reusing them." A setting called `high` is calibrated per model. It means something different on each one, the way "work quickly" means something different to a translator who has done the job for twenty years than to one on their first week.

That comparison is where the bureau analogy runs out. A translator who no longer follows an old instruction quietly does something different; an API that no longer accepts a parameter returns an error and stops. The shape underneath is the same drift, but only one of the two fails loudly. Four separate things moved under one single-line change; same family and same request shape did not mean any of the four still held.

## What the two dials don't decide

This chapter draws a line in three places. Picking a tier also happens to set the size of the context pot that tier's calls have to work with, but what that pot holds, how it fills, and how to manage a session inside it under pressure is chapter 1's territory.

Whether a request goes out synchronously, streamed, or bundled into an overnight batch is a separate question again, about the shape of the request rather than about who answers it or how long they deliberate. That choice is chapter 5.

And once effort or thinking depth changes between one call and the next, there is a cost to that change beyond the tokens it spends: it can invalidate work a provider had already cached from an earlier call in the same conversation. That interaction is real and it is examinable, but it belongs to chapter 9, where the mechanism doing the work is the cache.

What stays inside this chapter is narrower than it first looks: two purchases, made independently, for every single call. Which tier answers. How hard that tier is asked to work. Picking one does not set the other.

## The words that flag which dial

A stem naming which model to start with, or describing a tier by capability or latency, belongs to column one. A stem about deliberation, quality risk under time pressure, or a request that used to work and now fails after a version bump, belongs to column two. "Reduce latency, quality must not move" is the fast-mode phrase specifically; "reduce cost, some quality give is acceptable" is the effort phrase. A stem citing a fixed limit on a single response calls for a stricter instrument than either column; a stem citing average or ongoing spend across many requests, with quality already acceptable, is effort's own territory.

## Self-test

**1. Select ONE.** A batch of internal reports must never let a single response exceed a fixed number of tokens, regardless of how complex the source document is.

A. Lower the effort level to `low`.
B. Set `max_tokens` to the fixed limit.
C. Switch to Claude Haiku 4.5.
D. Disable thinking for the request.

**Answer: B.** Effort is a behavioural signal and can still let a hard problem run long. Only `max_tokens` sets a strict ceiling. Switching model or disabling thinking changes the quality of the answer; it does not cap the response.

---

**2. Select ONE.** A workload needs precise, hand-set control over exactly how many tokens Claude spends thinking, configured per request, on whichever of the three mainstream tiers is used.

A. Claude Opus 5
B. Claude Sonnet 5
C. Claude Haiku 4.5
D. All three support it equally

**Answer: C.** Opus 5 and Sonnet 5 currently accept only adaptive thinking, with no manual budget. Haiku 4.5 is the one still running extended thinking in manual mode, which fits the chapter's rule: newer tiers carry fewer thinking controls.

---

**3. Select ONE.** A live debugging session needs faster responses. There is no cost constraint, but the team cannot accept any drop in answer quality on complex questions.

A. Lower the effort level.
B. Turn on fast mode.
C. Switch to Claude Haiku 4.5.
D. Switch to adaptive thinking.

**Answer: B.** Fast mode runs the same model at the same quality, faster, for a higher price per token. Lower effort also speeds things up but risks quality on hard questions, which the constraint rules out.

---

**4. Select ONE.** An application's average cost per request has crept up over several months. Output quality is still meeting the bar, and no single request has a hard cost ceiling.

A. Add a second, cheaper model in front of the current one as a router.
B. Switch the whole workload to a less capable tier.
C. Sweep the effort level down on the current model and re-test.
D. Lower `max_tokens` across all requests.

**Answer: C.** Anthropic frames effort as the cheaper experiment to run before comparing or adding models, and its own internal comparisons found a multi-model setup that looked cheaper costing more than the same model at lower effort. Lowering `max_tokens` risks truncating responses rather than reducing typical spend.

---

**5. Select TWO.** A team updated only the model ID in its request payload, keeping a manual `thinking: {type: "enabled", budget_tokens: ...}` setting and an effort level tuned on the old model. After deploying against the new model in the same family, some requests began returning 400 errors, and the rest grew slower and more expensive with no other code changes.

A. The new model no longer accepts the manual thinking-budget parameter the old one used.
B. The new model's default thinking behaviour differs from the old model's, so requests now think when they previously did not.
C. The account's API rate limit was reduced when the new model shipped.
D. The new model silently drops any parameter it does not recognise, without error.

**Answer: A and B.** A rejected parameter explains the 400s; a changed default explains the extra latency and cost on requests that still succeeded. Anthropic documents both as real behaviour changes across releases, along with the guidance to re-run an effort sweep rather than reuse an old setting. Rate limits and silent parameter-dropping are not documented causes here.

## What's specific to today's lineup

This guide is v1.0 and states it is subject to change without notice. The shape taught above is durable: two independent dials, a trend toward fewer thinking controls on newer tiers, and effort as a behavioural signal rather than a hard cap. The specifics below are the ones most likely to move first, current as of this printing only.

- The three tiers this chapter builds on are Claude Haiku 4.5, Claude Sonnet 5, and Claude Opus 5. A fourth, frontier tier exists, currently Claude Fable 5, for work that explicitly needs the most capable model available. It appears here as context only.
- Effort levels currently run `low`, `medium`, `high` (the default), `xhigh`, and `max`. Availability is not uniform across tiers, and Claude Haiku 4.5 does not currently appear on the published list of models that support effort at all.
- Fast mode currently applies to the Opus tier only, at up to roughly 2.5 times the standard output token rate, and is not available through every deployment route.
- Which tier accepts extended, manual thinking versus adaptive-only thinking is a per-model fact with a published table. As of this printing, Claude Haiku 4.5 is extended-only; Claude Sonnet 5 and Claude Opus 5 are adaptive-only.

These four points are the ones to re-verify each time the guide updates.
