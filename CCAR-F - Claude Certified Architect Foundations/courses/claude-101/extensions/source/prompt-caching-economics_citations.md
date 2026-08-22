# Citations & Research Notes — Prompt Caching Economics (C-E4)

## Manifest
- **Date researched:** 2026-06-06 · **Re-verified 2026-06-09** (multipliers/TTLs/min-lengths/break-even all confirmed; additive `usage` drift noted in the addendum at the end. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
- **CCA-F domains:** 5 (Context Management & Reliability, 15%) primary; 4 (Tool use / agent design) and 3 (Prompt structuring) overlap noted per-section.
- **Lesson:** "Prompt Caching Economics" — architect-level extension C-E4 building on Anthropic's "Claude 101."

### Sources consulted
1. **Anthropic — Prompt caching (Build with Claude)** — `https://platform.claude.com/docs/en/build-with-claude/prompt-caching` — PRIMARY. The canonical mechanism doc: cache_control syntax, breakpoints, min lengths, TTL, invalidation, usage fields, best practices, use cases. (Legacy redirect also at `https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching`.)
2. **Anthropic — Pricing (About Claude)** — `https://platform.claude.com/docs/en/about-claude/pricing` — PRIMARY. Full per-model pricing table including 5m cache write / 1h cache write / cache hit columns, the multiplier explanation, batch + data-residency stacking, worked examples.
3. **Search aggregate (secondary blogs)** for latency/cost-percentage framing — SECONDARY, used only where Anthropic's own doc declined to state a number. Tagged inline as `[SECONDARY]`.

> **Sourcing note:** Anthropic's current prompt-caching doc does **not** publish a headline "X% latency reduction / Y% cost reduction" figure. The widely-cited "up to ~85% latency / up to ~90% cost" figures come from the original 2024 launch framing and secondary writers. They are tagged `[SECONDARY]` / `[VERIFY]`. The doc *does* support the cost math directly via the 0.1× read multiplier (a cache hit costs 10% of base input → up to 90% savings on the cached portion is arithmetic, not a marketing claim).

---

## Section A — What prompt caching is & the problem it solves
*(Reinforces Domain 5: Context Management & Reliability — managing large, repeated context efficiently.)*

**Verbatim definition (Anthropic):**
> "Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts. This significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Verbatim (pricing-page framing):**
> "Prompt caching reduces costs and latency by reusing previously processed portions of your prompt across API calls. Instead of reprocessing the same large system prompt, document, or conversation history on every request, the API reads from cache at a fraction of the standard input price." (source: https://platform.claude.com/docs/en/about-claude/pricing)

**The problem it solves — the repeated-prefix problem:**
- Across multi-turn conversations, agent loops, and document Q&A, the *same* large static content (system prompt, tool definitions, long document/RAG context, few-shot examples) is sent and **re-processed on every single request** — paid for in full each time, in latency and input-token cost.
- Caching lets the model "resume from" an already-processed prefix instead of recomputing it: the cached prefix is billed at the **cache-read rate (0.1× base input)** instead of full input price, and skips the prefill compute. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching; source: https://platform.claude.com/docs/en/about-claude/pricing)

**Twin benefit:** cost reduction on the cached prefix **and** latency reduction (the cached prefix's prefill is skipped). (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Latency / cost magnitude `[SECONDARY]` `[VERIFY]`:** Secondary sources cite "up to ~85% latency reduction" and "up to ~90% cost reduction" for long prompts (a ~100K-token doc dropping from ~11.5s to ~2.4s). These trace to the original launch post, not the current doc — treat as illustrative. (source: aggregate secondary, e.g. https://introl.com/blog/prompt-caching-infrastructure-llm-cost-latency-reduction-guide-2025) `[SECONDARY]`

---

## Section B — The mechanism
*(Reinforces Domain 5 primary; Domain 4 overlap for tool definitions; Domain 3 overlap for prompt structuring.)*

### B1. The `cache_control` ephemeral block
Basic syntax (5-minute default TTL):
```json
{ "cache_control": {"type": "ephemeral"} }
```
With extended 1-hour TTL:
```json
{ "cache_control": {"type": "ephemeral", "ttl": "1h"} }
```
(source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Two ways to enable caching (verbatim, pricing page):**
> "**Automatic caching:** Add a single `cache_control` field at the top level of your request. The system automatically manages cache breakpoints as conversations grow. This is the recommended starting point for most use cases."
> "**Explicit cache breakpoints:** Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached." (source: https://platform.claude.com/docs/en/about-claude/pricing)

**Placement rule:** `cache_control` is placed on the **last content block you want included in the cached prefix** — within the `tools`, `system`, or `messages.content` arrays. Everything from the start of the request up to *and including* that marked block becomes the cached prefix. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### B2. Cache breakpoints — count & prefix matching
- **Maximum breakpoints:** "You can define up to **4 cache breakpoints**" per request. `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Lookback / previous-breakpoint checking (verbatim):** "The system checks at most **20 positions per breakpoint**, counting the breakpoint itself as the first." The system walks backward one block at a time within this window looking for a previously cached entry — so you get cache hits at earlier block boundaries, not only the exact breakpoint. `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Exact-match requirement (verbatim):** "Cache hits require **100% identical prompt segments**, including all text and images up to and including the block marked with cache control." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### B3. What can be cached (verbatim list)
> - "Tools: Tool definitions in the `tools` array
> - System messages: Content blocks in the `system` array
> - Text messages: Content blocks in the `messages.content` array, for both user and assistant turns
> - Images & Documents: Content blocks in the `messages.content` array, in user turns
> - Tool use and tool results: Content blocks in the `messages.content` array, in both user and assistant turns" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**What CANNOT be cached (verbatim):** "Thinking blocks cannot be cached directly with `cache_control`"; "Sub-content blocks (like citations) themselves cannot be cached directly"; "Empty text blocks cannot be cached." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### B4. Prefix / ordering rules
**Verbatim:**
> "Cache prefixes are created in the following order: `tools`, `system`, then `messages`. This order forms a hierarchy where each level builds upon the previous ones." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

Implication: the cache always covers a **contiguous prefix** starting at the very top of the request (tools → system → messages). You cannot cache a middle slice while leaving the start uncached.

### B5. Minimum cacheable prefix length (per model) `[VERIFY]` — version-sensitive
> "Shorter prompts cannot be cached, even if marked with `cache_control`. Any requests to cache fewer than this number of tokens will be processed without caching, **and no error is returned**." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

| Model | Minimum cacheable tokens `[VERIFY]` |
|---|---|
| Claude Mythos Preview | 4,096 |
| Claude Opus 4.7 | 4,096 |
| Claude Opus 4.6 | 4,096 |
| Claude Opus 4.5 | 4,096 |
| Claude Opus 4.8 | 1,024 |
| Claude Sonnet 4.6 | 1,024 |
| Claude Sonnet 4.5 | 1,024 |
| Claude Opus 4.1 (deprecated) | 1,024 |
| Claude Opus 4 (deprecated) | 1,024 |
| Claude Sonnet 4 (deprecated) | 1,024 |
| Claude Haiku 4.5 | 4,096 |
| Claude Haiku 3.5 (retired exc. Bedrock/Vertex) | 2,048 |

(source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

> **Teaching caution:** the "smaller model = higher minimum" intuition is **not** clean — Haiku 4.5 requires 4,096 (same as the Opus 4.5–4.7 generation), while Opus 4.8 requires only 1,024. Do **not** teach the old "1024 large / 2048 Haiku" rule of thumb; it is stale. The 2,048 figure now applies only to the **retired Haiku 3.5**. `[VERIFY]`

### B6. Cache invalidation rules
**Governing principle (verbatim):** "Changes at each level invalidate that level and all subsequent levels." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

| What changes | Invalidates |
|---|---|
| Tool definitions | Tools + System + Messages (entire cache) |
| Web search toggle | System + Messages |
| Citations toggle | System + Messages |
| Speed setting | System + Messages |
| Tool choice | Messages only |
| Images | Messages only |
| Thinking parameters | Messages only |

(source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Architect takeaway:** Because the cache is a contiguous prefix in `tools → system → messages` order, *changing anything earlier busts everything after it.* Editing a tool definition is the most expensive change — it invalidates the **entire** cache.

---

## Section C — TTL & refresh
*(Reinforces Domain 5: reliability/cost over time; the TTL gotcha is a reliability-of-savings concern.)*

- **Default TTL: 5 minutes.** Verbatim: "By default, the cache has a **5-minute lifetime**." `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Refresh on use (verbatim):** "The cache is refreshed for no additional cost each time the cached content is used." So the 5-minute (or 1-hour) clock **resets on every cache hit** — a continuously-used prefix stays warm indefinitely at no extra write cost. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Extended TTL: 1 hour**, opt-in via `"ttl": "1h"`, at additional write cost (2× vs 1.25×, see Section D). `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching; source: https://platform.claude.com/docs/en/about-claude/pricing)
- **Deletion timing:** cached entries have a *minimum* lifetime; after expiry they are "promptly, though not immediately, deleted." `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Concurrency caveat (verbatim):** "For concurrent requests, note that a cache entry only becomes available after the first response begins. If you need cache hits for parallel requests, wait for the first response before sending subsequent requests." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — Fan-out parallel calls before the first response completes will each pay a cache *write*, not a read.

---

## Section D — The economics (the heart of the lesson)
*(Reinforces Domain 5 primary; this is the cost/reliability spine.)*

### D1. The exact multipliers (verbatim, pricing page) `[VERIFY]`
> "Prompt caching uses the following pricing multipliers relative to base input token rates:
> | 5-minute cache write | **1.25x base input price** | Cache valid for 5 minutes |
> | 1-hour cache write | **2x base input price** | Cache valid for 1 hour |
> | Cache read (hit) | **0.1x base input price** | Same duration as the preceding write |"
(source: https://platform.claude.com/docs/en/about-claude/pricing)

> "Cache write tokens are charged when content is first stored. Cache read tokens are charged when a subsequent request retrieves the cached content. **A cache hit costs 10% of the standard input price**, which means **caching pays off after just one cache read for the 5-minute duration (1.25x write), or after two cache reads for the 1-hour duration (2x write)**." (source: https://platform.claude.com/docs/en/about-claude/pricing)

> "These multipliers stack with other pricing modifiers, including the Batch API discount and data residency." (source: https://platform.claude.com/docs/en/about-claude/pricing)

**Summary multiplier table (vs base input = 1.0×):**
| Operation | Multiplier `[VERIFY]` |
|---|---|
| Base input | 1.0× |
| Cache write — 5-min | 1.25× |
| Cache write — 1-hour | 2.0× |
| Cache read (hit / refresh) | 0.1× |

### D2. Per-model dollar pricing (per MTok) `[VERIFY]` — drifts; re-check at lesson build time
| Model | Base Input | 5m Cache Write | 1h Cache Write | Cache Hit/Refresh | Output |
|---|---|---|---|---|---|
| Claude Opus 4.8 | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Opus 4.7 | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Opus 4.6 | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Opus 4.5 | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Opus 4.1 (deprecated) | $15 | $18.75 | $30 | $1.50 | $75 |
| Claude Opus 4 (deprecated) | $15 | $18.75 | $30 | $1.50 | $75 |
| Claude Sonnet 4.6 | $3 | $3.75 | $6 | $0.30 | $15 |
| Claude Sonnet 4.5 | $3 | $3.75 | $6 | $0.30 | $15 |
| Claude Sonnet 4 (deprecated) | $3 | $3.75 | $6 | $0.30 | $15 |
| Claude Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 |
| Claude Haiku 3.5 (retired exc. Bedrock/Vertex) | $0.80 | $1 | $1.60 | $0.08 | $4 |

(source: https://platform.claude.com/docs/en/about-claude/pricing)

> **Tokenizer caveat for the math (verbatim):** "Opus 4.7 and later use a new tokenizer compared to previous models... This new tokenizer may use up to **35% more tokens** for the same fixed text." Token *counts* (and absolute dollar costs) for the same text differ across model generations even when per-token rates match. `[VERIFY]` (source: https://platform.claude.com/docs/en/about-claude/pricing)

### D3. Break-even math (the spine — derive this in the lesson)

Let **N** = input tokens in the stable prefix, **P** = base input price per token, **R** = number of cache reads (reuses after the first write).

**Without caching**, sending the prefix R+1 times (1 first call + R reuses):
- Cost = (R + 1) · N · P

**With caching** (write once, read R times):
- 5-min: Cost = N·P·1.25 + R·N·P·0.1 = N·P·(1.25 + 0.1R)
- 1-hour: Cost = N·P·2.0 + R·N·P·0.1 = N·P·(2.0 + 0.1R)

**Break-even vs no-cache** (normalize by N·P):

*5-min cache:* `1.25 + 0.1R < (R + 1)` → `0.25 < 0.9R` → **R > 0.278**, i.e. break-even at the **first reuse (R = 1)**. With one reuse the cached path costs 1.35 units vs 2.0 uncached.
→ Matches the doc's "pays off after just one cache read for the 5-minute duration." (source: https://platform.claude.com/docs/en/about-claude/pricing)

*1-hour cache:* `2.0 + 0.1R < (R + 1)` → `1.0 < 0.9R` → **R > 1.11**, i.e. break-even at the **second reuse (R = 2)**. With two reuses the cached path costs 2.2 units vs 3.0 uncached.
→ Matches the doc's "pays off after two cache reads for the 1-hour duration." (source: https://platform.claude.com/docs/en/about-claude/pricing)

**Steady-state savings (heavy reuse):** as R grows, cached cost per request → 0.1× base input vs 1.0× uncached → up to **90% savings on the cached prefix portion** (the arithmetic floor of the 0.1× read multiplier, not a marketing claim). (source: https://platform.claude.com/docs/en/about-claude/pricing)

> **Framing nuance:** "Pays off after one/two reads" compares cache write+reads vs sending uncached every time. A single 5-min write costs only +0.25× over a normal send, so one hit (saving 0.9×) more than repays it.

### D4. Worked dollar example (explicit assumptions)
**Assumptions:** Claude Opus 4.8 ($5 base input / $0.50 read / $6.25 5-min write per MTok). Stable prefix = 20,000 tokens (system + tool defs + a long reference doc). A 10-turn conversation = 1 write + 9 reuses within the refreshing 5-min window. Ignore the varying suffix/output (same in both scenarios) to isolate prefix cost.

- **No caching:** 10 turns × 20,000 tok × $5/MTok = **$1.00** on the prefix.
- **With 5-min caching:**
  - Write (turn 1): 20,000 × $6.25/MTok = $0.125
  - Reads (turns 2–10 = 9 reads): 9 × 20,000 × $0.50/MTok = $0.09
  - **Total = $0.215** on the prefix.
- **Savings ≈ $0.785 → ~78.5%** on the cached prefix across the 10-turn session; each *additional* reuse costs one-tenth of the uncached rate. (Derived from doc pricing: source: https://platform.claude.com/docs/en/about-claude/pricing)

> Scale linearly: at 1,000 such sessions/day the prefix line item drops from ~$1,000/day to ~$215/day under the same assumptions. (Derived; assumptions explicit.)

**Anthropic's own worked example (verbatim context):** the pricing page's Managed-Agents example shows a 1-hour Opus 4.8 coding session where moving 40,000 of 50,000 input tokens to cache reads drops token+runtime cost from $0.705 to $0.525 — cache-read line: "40,000 × $5 × 0.1 / 1,000,000 = $0.02" vs uncached "$0.20". (source: https://platform.claude.com/docs/en/about-claude/pricing)

### D5. Stacking with other discounts
- **Batch API:** 50% off input/output, and "Batch API and prompt caching discounts can be combined." A cached read inside a batch job compounds (0.1× × 0.5×). (source: https://platform.claude.com/docs/en/about-claude/pricing)
- **Data residency / `inference_geo: "us"`:** 1.1× multiplier applies on **all** categories including cache writes and reads (Opus/Sonnet 4.6+). (source: https://platform.claude.com/docs/en/about-claude/pricing)
- **Fast mode:** caching multipliers apply *on top of* fast-mode premium pricing. (source: https://platform.claude.com/docs/en/about-claude/pricing)

---

## Section E — When caching pays off vs when it does NOT
*(Reinforces Domain 5 primary; Domain 4 for agent/tool loops.)*

### E1. Pays off (long stable prefix reused many times)
Anthropic's recommended use cases (verbatim):
- **Conversational agents:** "Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents."
- **Coding assistants:** "Improve autocomplete and codebase Q&A by keeping relevant sections or a summarized version of the codebase in the prompt."
- **Large document processing:** "Incorporate complete long-form material including images in your prompt without increasing response latency."
- **Detailed instruction sets:** "...with prompt caching you can get even better performance by including **20+ diverse examples** of high quality answers." (few-shot caching)
- **Agentic tool use:** "Enhance performance for scenarios involving multiple tool calls and iterative code changes, where each step typically requires a new API call."
- **Knowledge base interaction:** "...embedding the entire document(s) into the prompt, and letting users ask it questions."
(all source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Common thread:** a **large, byte-identical prefix** (system + tools + long context/few-shot) **reused across many requests within the TTL window**.

### E2. Does NOT pay off
*(Derived from the mechanism + economics; general reasoning grounded in the doc, not a verbatim Anthropic "don't" list.)*
- **Prefix below the minimum cacheable length** (e.g., <1,024 or <4,096 tokens depending on model) → silently not cached, no error, no savings. (source: min-length rule, https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Single-shot / one-and-done prompts** → you pay the 1.25× (or 2×) write premium and never collect a read. Net *more* expensive than a plain call.
- **Constantly-changing prefixes** → if the *start* of the prefix changes each call (a timestamp or user name injected into the system prompt), exact-match fails and you re-write every time. (Exact-match rule: source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Sporadic traffic + 5-min TTL gotcha:** if reuse gaps exceed the TTL, the cache expires before the next hit → each request becomes a fresh write at 1.25× (worse than no caching). Mitigations: switch to the **1-hour TTL** (2× write, break-even at 2 reads) for bursty traffic, or keep the cache warm. (source: TTL/refresh rules + pricing)
- **Parallel fan-out before the first response returns** → "a cache entry only becomes available after the first response begins," so concurrent first-calls each pay a write. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### E3. The TTL decision rule (architect heuristic, grounded in doc math)
- Reuses arrive **frequently / within 5 min** → default 5-min (1.25× write, break-even at 1 read).
- Reuses arrive **bursty / minutes-to-an-hour apart** → 1-hour TTL (2× write, break-even at 2 reads) to avoid re-paying writes on expiry.
- Reuses are **rare / unpredictable / single** → don't cache.

---

## Section F — Patterns & gotchas
*(Reinforces Domain 5; Domain 3 for prompt structuring, Domain 4 for tools.)*

### F1. Structure the prompt stable-prefix-first (verbatim guidance)
> "Place static content (tool definitions, system instructions, context, examples) at the beginning of your prompt. Mark the end of the reusable content for caching using the `cache_control` parameter." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
> "Place cached content at the prompt's beginning for best performance." (source: same)

### F2. Put the breakpoint on the last *identical* block
For a prompt with a static prefix and a varying suffix (timestamps, per-request context, the incoming message), put the breakpoint at the **end of the prefix, not the varying block**. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Anti-pattern:** injecting dynamic content (current date, user name, session vars) into the static system prompt. Move it **after** the breakpoint / into the user turn, or the prefix changes and busts the cache. (source: structuring guidance; corroborated `[SECONDARY]` https://www.prompthub.us/blog/prompt-caching-with-openai-anthropic-and-google-models)

### F3. Cache the system + tools first
Because invalidation cascades `tools → system → messages`, cache the most-stable, most-expensive-to-recompute layers (tool definitions and system prompt) and avoid editing tool defs casually — a tool-def change invalidates the **entire** cache. (source: invalidation table)

### F4. Use multiple breakpoints for layered stability
Up to 4 breakpoints let you cache layers with different change cadences (breakpoint after tools+system that rarely changes, another after a long doc that changes per-session, another after accumulated conversation). The 20-position lookback means earlier layers still hit even when a later layer changes. `[VERIFY]` (source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### F5. Combine with Batch and watch residency
Stack caching with the 50% Batch discount for non-time-sensitive bulk jobs; remember the 1.1× `inference_geo:"us"` premium applies to cache reads/writes too. (source: https://platform.claude.com/docs/en/about-claude/pricing)

### F6. Measure with usage fields
Confirm caching works by reading the response `usage` object. Field names (verbatim) `[VERIFY]`:
```json
"usage": {
  "cache_creation_input_tokens": 5120,
  "cache_read_input_tokens": 1800,
  "input_tokens": 2048,
  "output_tokens": 503
}
```
- `cache_creation_input_tokens` — tokens written to the cache when creating a new entry.
- `cache_read_input_tokens` — tokens retrieved from the cache for this request.
- `input_tokens` — "...only the tokens that come **after the last cache breakpoint**" (the uncached suffix).
- Identity: `total_input_tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens`.
(source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
**Health signal:** high `cache_read` + low `cache_creation` after warm-up = caching working; persistent high `cache_creation` = prefix busting (something earlier changing) or TTL expiring.

### F7. Gotchas checklist
- Min-length not met → **silent** no-cache, no error.
- Anything before a breakpoint changes → whole downstream cache busts.
- Ordering is fixed `tools → system → messages`; can't cache a non-prefix slice.
- Caches are **workspace-isolated** (as of 2026-02-05 on Claude API / Claude Platform on AWS / MS Foundry beta; org-level on Bedrock/Vertex) — never shared across orgs. `[VERIFY]`
- Caching does **not** enlarge the context window; it's a cost/latency optimization only.
- Thinking blocks, citation sub-blocks, and empty text blocks cannot be cached.
(all source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

---

## [VERIFY] LIST — every drift-prone fact in one place
Re-check ALL against `https://platform.claude.com/docs/en/build-with-claude/prompt-caching` and `https://platform.claude.com/docs/en/about-claude/pricing` at build time.

**Multipliers (vs base input):** 5-min write = **1.25×**; 1-hour write = **2.0×**; read/hit = **0.1×** (10% of base input). `[VERIFY]`

**TTL:** Default = **5 minutes**, refreshed (free) on each hit; Extended = **1 hour** via `"ttl":"1h"`. `[VERIFY]`

**Break-even:** 5-min pays off after **1 read**; 1-hour after **2 reads**. `[VERIFY]`

**Breakpoints / lookback:** Max = **4**; lookback = **20 positions per breakpoint**. `[VERIFY]`

**Minimum cacheable tokens (per model)** `[VERIFY]` — esp. Haiku 4.5 = 4,096 (NOT 2,048); Opus 4.8 = 1,024; Opus 4.5–4.7 = 4,096; Haiku 3.5 (retired) = 2,048.

**Usage field names** `[VERIFY]`: `cache_creation_input_tokens`, `cache_read_input_tokens`, `input_tokens` (post-breakpoint only).

**Per-MTok prices** `[VERIFY]` (all drift): Opus 4.x = $5 / $6.25 / $10 / $0.50 / $25; Sonnet 4.x = $3 / $3.75 / $6 / $0.30 / $15; Haiku 4.5 = $1 / $1.25 / $2 / $0.10 / $5.

**Model names** `[VERIFY]`: Opus 4.5/4.6/4.7/4.8, Mythos Preview, Sonnet 4.5/4.6, Haiku 4.5 — lineup changes fast.

**Stacking modifiers** `[VERIFY]`: Batch 50% (combinable); `inference_geo:"us"` 1.1× on all incl. cache; Fast mode premium (caching applies on top).

**Tokenizer caveat** `[VERIFY]`: Opus 4.7+ new tokenizer may use up to **35% more tokens** for the same text — affects absolute-dollar cross-model comparisons.

**Isolation** `[VERIFY]`: workspace-isolated on Claude API / Claude Platform on AWS / MS Foundry (beta) as of 2026-02-05; org-level on Bedrock/Vertex.

**Latency/cost headline %** `[VERIFY] [SECONDARY]`: "~85% latency / ~90% cost" are secondary/launch-era figures, NOT in the current doc. The 90%-on-cached-prefix figure is defensible as arithmetic from the 0.1× read multiplier; attribute the 85% latency figure to secondary sources or omit.

---

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`; no pricing/multiplier/TTL/min-length core fact reversed)*

- **`usage` now also carries a `cache_creation` sub-object** breaking cache writes down by TTL: `cache_creation.ephemeral_5m_input_tokens` and `cache_creation.ephemeral_1h_input_tokens`. The flat `cache_creation_input_tokens` / `cache_read_input_tokens` fields in the [VERIFY] list above remain valid — the sub-object is additive.
- **Thinking blocks cannot be tagged with `cache_control`** (not a valid breakpoint target) **but ARE cached passively** when they appear in the cached prefix of subsequent requests.

---

**Sources:**
- [Anthropic — Prompt caching (Build with Claude)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — PRIMARY
- [Anthropic — Pricing (About Claude)](https://platform.claude.com/docs/en/about-claude/pricing) — PRIMARY
- [Introl — Prompt caching infrastructure guide](https://introl.com/blog/prompt-caching-infrastructure-llm-cost-latency-reduction-guide-2025) — SECONDARY (latency/cost % framing only)
- [PromptHub — Prompt caching with OpenAI, Anthropic, Google](https://www.prompthub.us/blog/prompt-caching-with-openai-anthropic-and-google-models) — SECONDARY (structuring corroboration)
