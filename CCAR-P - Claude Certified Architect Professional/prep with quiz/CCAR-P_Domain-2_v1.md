# Domain 2 — Claude Models, Prompting & Context Engineering

**Weight:** 13% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Select appropriate Claude models based on trade-offs · Design system prompts, templates, and guardrails · Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought) · Optimize context windows and manage token usage · Implement prompt reuse strategies (caching, modular prompts, Skills)

---

## 2.1 Model Selection Trade-offs

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Select appropriate Claude models based on trade-offs |
| Discriminator | Task complexity/ambiguity vs. cost and latency at the task's actual operating volume |
| Wrong default | "Always pick the most capable model available" |

### Task Fit vs Headroom

Match model capability to what the task's complexity demands at its actual operating volume — not to the model's ceiling.

| Situation | Answer | Why |
|---|---|---|
| Narrow, bounded, high-volume, latency-gated classification | Smallest/fastest model that clears the accuracy bar | Cost and latency compound at volume; the task doesn't need frontier reasoning |
| Multi-step synthesis across ambiguous sources, low volume | Higher-capability model | Task complexity, not volume, is the binding constraint here |
| A stakeholder asks for "the biggest model, to be safe," with no stated complexity driver | Push back — ask what specifically requires it | Headroom bought without a requirement is unpriced cost, not safety |

### Upgrade Trigger vs Reasoning-Depth Trigger

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A production workload already meets its accuracy bar on the current model, and a newer, more capable model becomes available | Only upgrade if a specific unmet requirement drives it (an accuracy gap, a missing capability); benchmark before switching | A newer/larger model is not a free upgrade — a switch not tied to an actual gap adds cost and latency risk for no proven gain, and can silently change behavior on edge cases |
| A task requires deep multi-step reasoning across ambiguous, high-stakes trade-offs, and latency is not stated as gated | Enable extended thinking for that step rather than moving the whole workload to a larger model | Extended thinking targets the actual bottleneck — reasoning depth — without paying the cost of upsizing every other call in the workload |

### Exam scenario: choosing a model for a high-volume, latency-gated classification task

- ✅ Select the smallest/fastest model that clears the accuracy bar on representative tickets, benchmarked before committing
- ❌ Default to the most capable model available "to be safe" — **ARCHITECTED**: sounds more thorough, but nothing about a bounded, high-volume, latency-gated classification task calls for extra reasoning capability, and the extra cost/latency compounds at volume
- ❌ Fine-tune a smaller model without first testing whether a base model already clears the bar — **HALF-MOVE**: fine-tuning is a legitimate lever, but it's the expensive answer to a problem base-model evaluation might already solve

### ❌ Misconception
"The safest choice is always the largest model." — Model choice is a cost-latency-quality trade-off argued from the task's actual requirement; oversized capability is unpriced cost, not safety.

---

## 2.2 System Prompt Design & Guardrails

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Design system prompts, templates, and guardrails |
| Where persistent constraints live | System prompt — the only location with durable authority across the whole conversation |
| Source | Foundations corpus §4.3, carried forward unchanged |

### Placement — System Prompt vs. Everywhere Else

| Situation | Answer | Why |
|---|---|---|
| Tone, persona, or response-format rule for the whole conversation | System prompt | Only location with authority across every turn |
| A rule stated in the first user message | Not durable | Loses authority once the conversation moves past that turn |
| A rule "set" via an environment variable | No effect at all | Environment variables don't reach model behavior |
| A refusal boundary or escalation trigger (a guardrail) | System prompt | Guardrails are a design decision made at system-prompt time, not a monitoring afterthought |

### Guardrail Scope — Global vs Layer-Specific

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A guardrail needs to react differently depending on which tool or sub-agent is currently active | Scope the guardrail to the relevant layer (e.g. a per-tool or per-agent system prompt), not one blanket top-level rule | A single global guardrail either over-restricts contexts that don't need it or under-restricts the one that does; guardrails belong at the layer where the risk actually occurs |

### Exam scenario: where a behavioral rule belongs

- ✅ System prompt
- ❌ First user message — **WRONG-AXIS**: right idea (state the rule), wrong location — it loses authority mid-conversation
- ❌ An environment variable configured at deploy time — **WRONG-AXIS**: confuses infrastructure configuration with a model-facing instruction; it never reaches the model at all

### ❌ Misconception
"If it's documented anywhere in the pipeline, the model will follow it." — Only content that actually reaches the model as part of its system prompt shapes its behavior; documentation elsewhere is invisible to the model.

---

## 2.3 Few-Shot Prompting

### Core Facts

| Attribute | Value |
|---|---|
| When to use | Prose instructions produce inconsistent output; a specific case is ambiguous |
| Critical principle | Target 4–6 examples at the ambiguous cases, not 10–15 easy ones |
| Source | Foundations corpus §4.1, carried forward unchanged |

### Example Count vs Example Targeting

| Situation | Answer | Why |
|---|---|---|
| Model inconsistently formats output despite clear instructions | Add 3–4 examples of the exact required format | Instructions have already failed; examples fix format precision directly |
| Model misroutes an ambiguous request between two tools | Add 4–6 examples targeted at exactly that ambiguity | Targeting the failure case is what fixes it, not example volume |
| Proposal to add 10–15 examples of clear-cut, unambiguous cases | Reject | Doesn't touch the actual ambiguous cases causing the error |

### Example Selection Discipline — Failure-Matched vs Convenient

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| Few-shot examples are already in place but are drawn from the easiest, most common cases rather than the cases actually causing failures | Replace them with examples drawn from the observed failure distribution | Examples teach by pattern-matching to what they show; examples that don't resemble the actual failure mode don't transfer to it, regardless of count |
| A single well-chosen example already resolves an ambiguous formatting case in testing | Ship with that one targeted example rather than padding to an arbitrary count | Targeting the ambiguity is the lever, not example count; one example that resolves the case in testing needs no padding |

### Exam scenario: an agent misroutes an ambiguous request between two tools

- ✅ Add 4–6 few-shot examples targeted at exactly this kind of ambiguous phrasing, each with a stated rationale for the tool chosen
- ❌ Add 10–15 examples covering a broad range of clear, unambiguous requests — **HALF-MOVE**: more examples, the wrong ones; never touches the actual failure case
- ❌ Rewrite the system prompt instructions to be more explicit — **REPAIR**: instructions are already failing; more prose doesn't fix a consistency problem examples are built to solve

### ❌ Misconception
"More examples always help." — Only examples targeted at the specific ambiguous cases fix the failure; volume without targeting is wasted context.

---

## 2.4 Chain-of-Thought Reasoning Cues

### Core Facts

| Attribute | Value |
|---|---|
| Add a reasoning cue when | Multi-step math, multi-stage analysis, comparison across N items, stepwise transformation |
| Do not add when | Single-step task (translation, simple classification) |
| Source | Foundations corpus §4.2, carried forward unchanged |

### Task Shape — Single-Step vs Multi-Step

| Situation | Answer | Why |
|---|---|---|
| Multi-step reasoning or comparison task | Add a "think step by step" cue | Improves accuracy on tasks that require deliberation |
| Single-step task (e.g., translate one sentence) | Don't add a reasoning cue | Adds latency/cost with no accuracy benefit on a task with no steps to reason through |

### Verified Sufficiency and Budget Conflict

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A multi-step task already reasons correctly and consistently without an explicit step-by-step cue, verified in testing | Don't add the cue | The cue's cost in tokens and latency is only justified by a measured accuracy gap; a task already performing correctly doesn't need it added by default |
| A multi-step reasoning task also carries a latency budget the extra reasoning tokens would breach | Use a bounded or structured reasoning cue (e.g. a short, fixed scratchpad) rather than open-ended chain-of-thought | The task shape still calls for deliberation, but an unbounded cue trades away the stated latency budget; a bounded version keeps most of the accuracy benefit inside it |

### Exam scenario: a single-step translation feature

- ✅ Don't add a chain-of-thought cue — the task is single-step and gains nothing from one
- ❌ Add it anyway "for consistency with other features" — **ARCHITECTED**: sounds thorough and consistent, but adds cost and latency to a task the guide explicitly treats as not needing it
- ❌ Add it only after accuracy is observed to drop — **REPAIR**: a reactive patch to a symptom, instead of matching the technique to task shape from the start

### ❌ Misconception
"Chain-of-thought never hurts, so add it everywhere." — It's a targeted tool for multi-step tasks; adding it to single-step tasks is pure overhead.

---

## 2.5 Stateless API — The Fundamental Constraint

### Core Facts

| Attribute | Value |
|---|---|
| Fact | Claude's API is fully stateless; every call is independent, with no server-side memory |
| Implication | Every request must carry the complete conversation history in `messages` |
| Source | Foundations corpus §5.1, carried forward unchanged |

### Root-Cause Diagnosis — Missing History vs Context Limit

| Symptom | Root cause | Not the cause |
|---|---|---|
| Claude "forgot" something from 2 turns ago, in a short conversation | Application isn't including prior messages in the `messages` array | Context window exceeded (impossible this early) |
| Latency/cost rising as a conversation passes 50 turns | Full history resent every call — more turns means more tokens | Model generating longer responses; database slowdown |

### Reducing Resent Tokens Without Losing Statelessness

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A team wants to reduce the tokens resent every call as a conversation grows, without losing continuity | Summarize or truncate older turns, but keep resending the full `messages` array, including the summary, on every call | Statelessness isn't the thing to remove — every call still needs complete context resent; the fix is shrinking what's resent, not skipping the resend |
| Two separate client sessions for the same user, hitting the API independently, need to share conversation context | The application must merge and pass the combined history explicitly in `messages`; the API will not correlate the sessions itself | There is no server-side session identity in a stateless API; cross-session continuity is an application responsibility, not something a shared identifier on the request enables |

### Exam scenario: Claude has no memory of a fact mentioned two turns earlier

- ✅ The application is not including the full prior message history in the `messages` array
- ❌ The context window was exceeded — **DISCARD**: replaces a straightforward application-layer fix with an unrelated model-capacity explanation that doesn't fit a short conversation
- ❌ Claude needs a `session_id` parameter for persistent memory — **WRONG-AXIS**: invents a mechanism the stateless API doesn't have, instead of recognizing the actual constraint

### ❌ Misconception
"Claude has some memory across calls by default." — The API has none; all continuity is the application's responsibility to construct and resend on every request.

---

## 2.6 "Lost in the Middle"

### Core Facts

| Attribute | Value |
|---|---|
| Phenomenon | Reliable attention at the beginning and end of long input; degraded attention in the middle |
| Mitigation | Key findings first, explicit section headings, structured data over verbose prose |
| Source | Foundations corpus §5.2, carried forward unchanged |

### Structural Fix vs Length Fix

| Situation | Answer | Why |
|---|---|---|
| Long synthesis input misses critical mid-document findings | Restructure: findings-first + headings + structured facts | Fixes the attention pattern directly, at the source |
| Same situation | Shorten the input under an arbitrary token limit | Risks losing exactly the critical information that's missing |

### Scope of the Fix — One Fact, No Dominant Fact, or Short Input

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A single precision-critical fact sits in the middle of an otherwise verbose document, and the task's failure is fabricating that one value | Pull that specific fact into a short structured highlight near the top or end, in addition to leaving it in place | The general restructure-everything fix targets pervasive degradation; one known critical fact needs to be explicitly surfaced at the positions attention actually holds |
| Whether ordering matters when the task's total input is short, well under the model's effective context | No — the phenomenon is a function of total input length relative to the attention pattern, and a short input doesn't trigger it | Applying restructuring discipline to inputs too short to trigger the effect is unneeded overhead with no measured benefit |
| Bullet-point facts scattered with no structure across a long input each matter equally, with no single fact identifiable as the key finding | Convert to explicit headed sections grouped by topic, even without one findings-first summary | Structure — headings and grouping — is the fix, not exclusively a top summary; when no single fact dominates, section-level organization still restores retrievability across the middle |

### Exam scenario: a synthesis agent misses critical findings buried in the middle of a long input

- ✅ Place a key-findings summary at the start and add explicit section headings throughout
- ❌ Summarize the whole input down to a much shorter length — **DISCARD**: risks cutting exactly the critical information the agent is missing, instead of fixing how it's positioned
- ❌ Alternate which source appears first across runs — **HALF-MOVE**: only rotates whose content sits in the penalized middle position; doesn't fix the underlying attention pattern

### ❌ Misconception
"The fix for 'lost in the middle' is a shorter prompt." — The fix is structural position and format, not raw length; shortening risks losing exactly the content that needed surfacing.

---

## 2.7 Context Window Management Strategy

### Core Facts

| Attribute | Value |
|---|---|
| Tested pattern | Hybrid: extract critical structured facts verbatim + summarize general discussion + keep recent turns verbatim |
| Why not pure summarization | Precision-critical facts degrade into vague paraphrase |
| Source | Foundations corpus §5.3, carried forward unchanged |

### Uniform Summarization vs Hybrid Extraction

| Situation | Answer | Why |
|---|---|---|
| Long conversation with precision-critical facts (amounts, IDs, allergies) plus general chatter | Extract critical facts into a structured block, summarize the rest, keep recent turns verbatim | Preserves precision where it matters, compresses where it doesn't |
| Same situation | Summarize the entire history uniformly | Precision-critical facts blur into unusable paraphrase — a real risk in some domains |
| Same situation | Keep only the most recent N tokens | Drops early precision-critical facts entirely if they were mentioned early |

### Pinned Facts, Re-summarization Cadence, and Multi-Source Budgets

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| An early-conversation decision (e.g. a chosen configuration) must never change for the rest of a session that runs for hundreds of turns | Pin that decision into a persistent structured block, re-included on every call, separate from the rolling summary | A rolling summary can drift or drop a fact across repeated re-summarization passes; a fact that must never change needs a stable slot the summarization process never touches |
| A team plans to summarize older turns automatically, but is unsure how often to re-run the summarization step | Re-summarize incrementally as new turns roll off the retained window, not once at the very end of the conversation | A single end-of-conversation pass either processes an unbounded amount of history at once or arrives too late to control token growth during the conversation |
| Retrieved documents and conversation history both need space in one bounded context window | Budget each source independently against the window rather than truncating whichever was added last | Truncating by insertion order lets one source crowd out the other unpredictably; an explicit per-source budget keeps both available regardless of assembly order |

### Exam scenario: a long assistance session mixes a safety-critical fact with general chatter

- ✅ Extract the critical fact and quantities into a compact structured block, summarize the general chatter, keep the most recent exchanges verbatim
- ❌ Summarize the entire history — **REPAIR**: compresses everything uniformly, degrading the critical fact into unsafe vagueness
- ❌ Keep only the most recent portion of the conversation — **DISCARD**: drops the critical fact entirely if it was mentioned early and falls outside the retained window

### ❌ Misconception
"Summarization is always safe as long as it's shorter." — Uniform summarization loses precision on facts that must stay exact; some information must be extracted verbatim, not compressed.

---

## 2.8 Prompt Caching

### Core Facts

| Attribute | Value |
|---|---|
| Mechanism | Claude reuses a cached prefix across requests when that prefix is byte-identical and stable |
| Requirement | Static content first, dynamic content last, outside the cached prefix |
| Benefit | Cuts latency (time-to-first-token) and cost together |
| Source | Official exam guide v1.0, §8 Sample 2 — VERIFIED |

### Content Ordering — Static-First vs Dynamic-First

| Situation | Answer | Why |
|---|---|---|
| Identical large system prompt/policy sent on every request, varying user message follows | Order static content first, enable prompt caching | A stable prefix gets reused; cuts latency and cost together |
| Same situation | Truncate the static content to reduce tokens | Loses required policy content instead of reusing it |
| Same situation | Move the static content into a few-shot block | Doesn't create a stable, cacheable prefix the way ordering does |

### Cache Invalidation and Retention-Window Limits

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A system prompt's static portion is byte-identical across requests, but a small dynamic timestamp is inserted at the very start of that same block | Move the dynamic timestamp out of the static block entirely, to after the cached prefix | Any change inside the supposedly-static prefix, even one token, invalidates the cache for the whole block; dynamic content must sit strictly after the stable prefix |
| A large static prefix is a caching candidate, but the traffic pattern sends requests to it only once every 20 minutes, longer than the cache's retention window | Accept that caching won't help this workload and evaluate other cost/latency levers | Caching only pays off within its retention window; a request cadence longer than that window recomputes the prefix from scratch regardless |
| A stable prefix is shared, but two different downstream tools each need a different additional static block appended before the shared dynamic content | Structure the prompt as shared prefix, then per-tool static block, then dynamic content, in that order | Ordering the common part first preserves the cache hit rate on the shared portion across tool variants, instead of forcing a full-prompt divergence per tool |

### Exam scenario: an identical large policy preamble is sent on every request, and both latency and cost are concerns

- ✅ Order the static preamble first and enable prompt caching
- ❌ Split the preamble across two requests — **HALF-MOVE**: doesn't address caching at all, just relocates the same token cost
- ❌ Summarize the preamble with the model at request time — **REPAIR**: adds an entire extra model call to solve a problem caching already solves for free, and risks losing policy precision

### ❌ Misconception
"Caching means storing the response for reuse." — Prompt caching reuses a stable *input prefix*, not the output; it only works if the cached portion is identical and ordered first, every time.

---

## 2.9 Modular Prompts & Skills

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Implement prompt reuse strategies (caching, modular prompts, Skills) |
| Team-scale answer | Versioned, shared, reviewable prompt components — not per-project copy-paste |
| Parallel | The same logic Domain 7 (Developer Productivity) applies to Claude Code configuration |

### Ad Hoc Duplication vs Versioned Reuse

| Situation | Answer | Why |
|---|---|---|
| Multiple teams each maintain their own copy of similar system prompts | Consolidate into versioned, shared modular prompts/Skills | A behavior change becomes one reviewable event, not N silent drifts |
| Same situation | Let each team keep its own copy, for flexibility | Behavior drifts silently across teams with no single source of truth |

### Versioned Adoption, Extension vs Forking, and Discoverability

*(Added 2026-09-01, D2 corpus expansion — Ram's decision, `EXAM-LOG.md` Paper 5 entry.)*

| Situation | Answer | Why |
|---|---|---|
| A shared modular prompt component is updated, but some consuming teams are deliberately still pinned to an older version for a staged rollout | Version the shared component explicitly so teams can pin and upgrade independently, rather than force every consumer onto the latest edit immediately | Versioned reuse means controlled adoption, not universal instant propagation; an unversioned shared prompt forces every consumer to accept every edit immediately |
| A team's use case needs 90% of an existing shared Skill's behavior, with one differing constraint | Parameterize or extend the existing shared Skill for the differing constraint rather than forking a full copy | A fork immediately becomes a second, silently-drifting copy — the exact failure versioned reuse exists to prevent |
| An organization has many small, single-purpose prompt snippets with no discovery mechanism, and teams keep re-authoring the same snippet independently | Maintain a discoverable, indexed catalog of shared modular components, not just version control on each one | Version control solves drift once a component is found; it does nothing for teams who never find that the component already exists and duplicate the authoring effort instead |

### Exam scenario: a partner team wants to adopt your prompt/tooling setup

- ✅ Version-controlled shared configuration/prompts and Skills, with an onboarding path new team members actually follow
- ❌ A recorded walkthrough — **HALF-MOVE**: transfers knowledge once but doesn't stay current as prompts evolve
- ❌ A shared chat channel for questions — **REPAIR**: reactive support, not a durable, versioned artifact

### ❌ Misconception
"Documentation of the prompt is enough; everyone can copy it once." — A copied prompt drifts the moment either side edits it; durability requires a single versioned source both sides actually reference.
