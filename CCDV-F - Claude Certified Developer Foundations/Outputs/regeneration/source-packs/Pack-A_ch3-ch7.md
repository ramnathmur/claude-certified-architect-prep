# Pack A — Source Pack for Chapter 3 and Chapter 7

**Built:** 2026-08-22 · **All facts fetched:** 2026-08-22
**For:** CCDV-F course regeneration, Chapter 3 ("Two dials, not one") and Chapter 7 ("When asking
nicely stops working")
**Rule applied:** no source, no claim. Every fact below carries the URL it was read on. Anything not
established is in the gap lists at the end, not filled in from memory.

---

## How to read this pack

**Fetch-fidelity marker.** Every URL here was actually fetched today. Two fidelities:

- **[RAW]** — the page returned as raw markdown, frontmatter intact. Quoted strings are the page's own
  words.
- **[VIA-SUMMARIZER]** — the fetch tool returned a model-written answer *about* the page rather than
  the page source. The page was reached and the content is from it, but a "quoted" string may be a
  close paraphrase. **Do not put a [VIA-SUMMARIZER] string in quotation marks in the chapter without
  re-fetching it.** Three pages fall in this bucket: the migration guide, structured outputs, and
  handling stop reasons. They are flagged inline.

**[VOLATILE]** marks a limit, price, header, date, or model-ID specific that will drift. The exam is
judgement-shaped and closed-book; these are quarantine candidates, present so the writer knows the
shape of the fact, not so the reader memorises the number.

**Writer's warning on model names.** The current lineup includes models named **Fable 5** and
**Mythos 5** alongside Opus/Sonnet/Haiku. The exam blueprint's sub-topic is worded
`Opus vs Sonnet vs Haiku use cases` — three tiers. The documented lineup is wider than the blueprint's
wording. Chapter 3 should teach the three the blueprint names and mention the frontier tier as
context, not build the spine on names the blueprint does not use.

---

# CHAPTER 3 — "Two dials, not one"

## RQ1 — Current model tiers and their stated use cases

**Source:** https://platform.claude.com/en/docs/about-claude/models/overview — fetched 2026-08-22
**[RAW]**

### The one-line description Anthropic gives each model

Verbatim from the "Latest models comparison" table, **Description** row:

| Model | Anthropic's own description |
|---|---|
| Claude Fable 5 | "Next-generation intelligence for long-running agents" |
| Claude Opus 5 | "For complex agentic coding and enterprise work" |
| Claude Sonnet 5 | "The best combination of speed and intelligence" |
| Claude Haiku 4.5 | "The fastest model with near-frontier intelligence" |

### The opening guidance sentence, verbatim

> "If you're unsure which model to use, start with **Claude Opus 5** for complex agentic coding and
> enterprise work. For workloads that need the highest available capability, use Claude Fable 5."

**Discriminator this gives you:** the default recommendation is Opus 5, not the frontier model and not
the cheapest. A scenario option that says "always start with the most capable model" contradicts the
docs' own opening line.

### Comparative latency — the ranking that matters more than the numbers

From the same table, **Comparative latency** row: Fable 5 = "Slower", Opus 5 = "Moderate", Sonnet 5 =
"Fast", Haiku 4.5 = "Fastest".

**Discriminator:** latency ranks inversely to capability across the tiers. A scenario naming a latency
constraint pushes down the tier; a scenario naming an accuracy constraint pushes up.

### Specifications [VOLATILE]

| Feature | Fable 5 | Opus 5 | Sonnet 5 | Haiku 4.5 |
|---|---|---|---|---|
| API ID | `claude-fable-5` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5-20251001` |
| Pricing /MTok | $10 in / $50 out | $5 in / $25 out | $2 in / $10 out | $1 in / $5 out |
| Context window | 1M tokens | 1M tokens | 1M tokens | 200k tokens |
| Max output | 128k | 128k | 128k | 64k |
| Extended thinking (`thinking.type: "enabled"`) | No | No | No | **Yes** |
| Adaptive thinking | **Yes (always on)** | Yes | Yes | **No** |

All four rows above are [VOLATILE] except the thinking-support rows, which are the chapter's spine and
are cross-verified against the per-model table in RQ2.

### Model IDs are pinned snapshots — verbatim note

> "Every Claude model ID is a pinned snapshot. Models with a date in the ID (for example,
> `20250929`) are fixed to that specific release. Starting with the Claude 4.6 generation, model IDs
> use a dateless format that is also a pinned snapshot, not an evergreen pointer."

**Discriminator, and it is a good one:** a dateless ID like `claude-opus-5` looks like a floating alias
and is not one. This is directly usable against a distractor that says "pin the model by using the
dated ID; the short ID auto-upgrades."

### Capabilities are queryable at runtime

> "You can query model capabilities and token limits programmatically with the Models API. The
> response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available
> model."

**Discriminator:** for a scenario about keeping an application correct across model releases, querying
the Models API is a documented mechanism, not an invented one.

---

## RQ2 — Extended thinking vs adaptive thinking · THE CHAPTER'S SPINE

**This was established cleanly.** They are two different API modes, not two names for one thing, and
which one a model accepts is a per-model fact with a published table.

### The definitions

**Extended thinking (manual mode).**
Source: https://platform.claude.com/en/docs/build-with-claude/extended-thinking — fetched 2026-08-22
**[RAW]**

> "Extended thinking in manual mode gives you direct control over how much Claude thinks. You set a
> thinking token budget on each request with `thinking: {type: "enabled", budget_tokens: N}`, and
> Claude thinks against that budget before it starts its final answer."

And the page's own framing of when it still earns its place:

> "Manual mode remains useful when your workload requires predictable latency or precise control over
> thinking costs."

**Adaptive thinking.**
Source: https://platform.claude.com/en/docs/build-with-claude/thinking-steering-and-cost — fetched
2026-08-22 **[RAW]**. (Note: the URL `.../build-with-claude/adaptive-thinking` resolves to this page,
titled "Steering thinking". There is no separately-titled "Adaptive thinking" page as of this fetch.)

> "Claude's thinking is adaptive: the model evaluates each request and decides for itself whether to
> think and how much. You set an intent, optionally specify the effort, and the model allocates
> reasoning where it judges reasoning will help."

> "Thinking is optional for the model. On each request, Claude weighs the complexity of the input and
> decides whether deeper reasoning would improve the answer. A simple factual question may get a
> direct response with no thinking block at all; a multistep math problem or a tricky debugging task
> triggers deeper reasoning."

> "The decision happens per request. The same conversation can contain turns with and without
> thinking, and a turn where Claude chose not to think contains no thinking block. Don't build
> application logic that assumes every assistant turn starts with one."

### The difference, stated as the difference

Source: https://platform.claude.com/en/docs/build-with-claude/extended-thinking — fetched 2026-08-22
**[RAW]**, from the "Migrating to adaptive thinking" section:

> "Expect a behavioral difference, not just a syntax change. With a fixed budget, Claude thinks on
> every request. With adaptive thinking, Claude decides whether and how much to think on each request,
> and at lower effort settings it may skip thinking entirely on easy inputs."

**This is the single most usable sentence in the whole pack for Chapter 3.** Fixed budget → thinks
every time. Adaptive → decides per request, and may not think at all.

Three further mechanical differences from the same page:

1. **Depth control moves.** Migration is: "remove `budget_tokens`, set `thinking: {type: "adaptive"}`,
   and control reasoning depth with `output_config: {effort: ...}` instead of a token budget."
2. **Interleaved thinking becomes automatic.** "adaptive thinking interleaves automatically, and the
   Claude API ignores the header on these models." In manual mode on older models it required the
   `interleaved-thinking-2025-05-14` beta header [VOLATILE].
3. **Turn validation relaxes.** Manual mode requires the final assistant turn of a thinking-enabled
   request to begin with a thinking block; adaptive drops that requirement. From the steering page:
   "Assistant turns don't need to start with a thinking block."

### Which model supports which — the published table

Source: https://platform.claude.com/en/docs/build-with-claude/thinking-troubleshooting — fetched
2026-08-22 **[RAW]**, section "Configurations each model rejects":

| Model | Thinking types | Default | Rejected with 400 |
|---|---|---|---|
| Claude Fable 5 | Adaptive only | Always on | `"enabled"`, `"disabled"` |
| Claude Mythos 5 | Adaptive only | Always on | `"enabled"`, `"disabled"` |
| Claude Mythos Preview | Adaptive, extended | Always on | `"disabled"` |
| Claude Opus 5 | Adaptive only | **On** | `"enabled"`, `"disabled"`* |
| Claude Opus 4.8 | Adaptive only | Off | `"enabled"` |
| Claude Opus 4.7 | Adaptive only | Off | `"enabled"` |
| Claude Sonnet 5 | Adaptive only | **On** | `"enabled"` |
| Claude Opus 4.6 | Adaptive, extended (deprecated) | Off | None |
| Claude Sonnet 4.6 | Adaptive, extended (deprecated) | Off | None |
| Claude Opus 4.5 | **Extended only** | Off | `"adaptive"` |
| **Claude Haiku 4.5** | **Extended only** | Off | `"adaptive"` |
| Claude Sonnet 4.5 | **Extended only** | Off | `"adaptive"` |

\* "Claude Opus 5 accepts `"disabled"` at effort `high` or below; combining it with effort `xhigh` or
`max` returns a 400 error."

> "Models marked `Always on` cannot turn thinking off. Models marked `On` default to thinking but
> accept `thinking: {type: "disabled"}`."

**The three-generation rule, verbatim from the same page:**

> "Extended thinking (`thinking.type: "enabled"` with `budget_tokens`) is deprecated on the Claude 4.6
> models (requests using it still succeed). Claude 4.7 and later models do not support it and reject
> requests that use it, returning a 400 error. On Claude 4.5 and earlier models that support thinking,
> extended thinking is the only available thinking mode."

**The discriminator that will win exam items:** the newest models are *not* the ones with the most
thinking knobs. They have *fewer* — adaptive only, no budget, and on the frontier models thinking
cannot be switched off at all. Haiku 4.5, the cheapest current model, is the one that still runs the
*old* mode. "Newer = more configurable" is exactly backwards and is a natural distractor.

### The observable symptom of adaptive thinking

Same page, symptom section "No thinking block appears on some turns":

> "This is normal in adaptive mode: Claude skips thinking on requests it judges simple enough to answer
> directly."

**Discriminator:** in a debugging scenario where an application breaks because a turn had no thinking
block, the fault is the application's assumption, not the model.

---

## RQ3 — Effort levels

**Source:** https://platform.claude.com/en/docs/build-with-claude/effort — fetched 2026-08-22 **[RAW]**

### Definition, verbatim

> "The effort parameter lets you control how many tokens Claude spends when responding to requests. You
> can trade off between response thoroughness and token efficiency with a single model."

> "By default, Claude uses high effort, spending as many tokens as needed for excellent results."

> "Setting `effort` to `"high"` produces exactly the same behavior as omitting the `effort` parameter
> entirely."

### It is not a budget — verbatim, and this is the load-bearing distinction

> "Effort is a behavioral signal, not a strict token budget. At lower effort levels, Claude will still
> think on sufficiently difficult problems, but it will think less than it would at higher effort
> levels for the same problem."

And from the thinking overview
(https://platform.claude.com/en/docs/build-with-claude/thinking — fetched 2026-08-22 **[RAW]**):

> "**You need a hard ceiling on spend:** use `max_tokens`. Effort is soft guidance. `max_tokens` is a
> strict limit."

**Discriminator, high value:** a scenario stating a hard cost ceiling is answered by `max_tokens`, not
by effort. A scenario stating "reduce cost on average without capping any single response" is answered
by effort. Two options will both look like cost controls; only one is a ceiling.

### The five levels — Anthropic's own two tables

Behavioural, from the steering page
(https://platform.claude.com/en/docs/build-with-claude/thinking-steering-and-cost, fetched 2026-08-22,
**[RAW]**):

| Effort level | Thinking behavior |
|---|---|
| `max` | "Claude always thinks with no constraints on thinking depth." |
| `xhigh` | "Claude always thinks deeply with extended exploration." |
| `high` (default) | "Claude almost always thinks. Provides deep reasoning on complex tasks." |
| `medium` | "Claude uses moderate thinking. May skip thinking for simple queries." |
| `low` | "Claude minimizes thinking. Skips thinking for simple tasks where speed matters most." |

Use-case, from the effort page:

| Level | Typical use case (verbatim) |
|---|---|
| `max` | "Tasks requiring the deepest possible reasoning and most thorough analysis" |
| `xhigh` | "Long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions" |
| `high` | "Complex reasoning, difficult coding problems, agentic tasks" |
| `medium` | "Agentic tasks that require a balance of speed, cost, and performance" |
| `low` | "Simpler tasks that need the best speed and lowest costs, such as subagents" |

**[VOLATILE] — level availability is not uniform.** `xhigh` is available on Fable 5, Mythos 5, Opus 5,
Opus 4.8, Opus 4.7, and Sonnet 5. `max` is available on a wider set including Opus 4.6 and Sonnet 4.6.
The page states: "`xhigh` is a newer level; some models that support `max` don't support `xhigh`."

**Supported models for effort at all** [VOLATILE]: `claude-fable-5`, `claude-mythos-5`,
`claude-mythos-preview`, `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`,
`claude-sonnet-5`, `claude-sonnet-4-6`, `claude-opus-4-5-20251101`. Note what is absent: **Haiku 4.5
is not on the effort list.**

### What effort changes — wider than thinking

> "The effort parameter affects **all tokens** in the response, including: Text responses and
> explanations · Tool calls and function arguments · Thinking (when active)"

> "It doesn't require thinking to be enabled." … "It can affect all token spend including tool calls.
> For example, lower effort would mean Claude makes fewer tool calls."

Effort with tool use, verbatim: lower effort levels tend to "Combine multiple operations into fewer
tool calls · Make fewer tool calls · Proceed directly to action without preamble · Use terse
confirmation messages after completion."

**Discriminator:** effort is not a thinking dial. It is a whole-response dial that includes thinking.
A scenario about an agent making too many tool calls has effort as a legitimate lever — which is
non-obvious and therefore examinable.

### Effort and thinking are separate parameters

> "Don't pass `adaptive` as an `effort` value: `adaptive` is a thinking mode, not an effort level."

> "`thinking` controls whether Claude thinks in thinking blocks before answering; the `effort`
> parameter controls how much work Claude puts into the whole response, which in adaptive mode
> includes how often and how deeply it thinks."

Locations: thinking mode is `thinking.type`; effort is `output_config.effort` — "Effort is set at
`output_config.effort`, not inside the `thinking` object". [VOLATILE — parameter path]

### Where effort does nothing

From the troubleshooting page, "Setting effort does not change thinking":

> "This happens because effort is the primary thinking lever only in adaptive mode. On
> extended-thinking-only models, thinking depth is set by `budget_tokens` instead."

**The one exception, stated on both the effort and extended-thinking pages:** "On Claude Opus 4.5, the
only extended-thinking-only model that supports effort, effort composes with the budget."

### Effort and prompt caching — cross-cutting, and it makes a clean scenario

From the steering page:

> "The resolved effort value is rendered into the prompt, so changing it between requests invalidates
> cache breakpoints, just as changing the legacy `budget_tokens` parameter does on models that use it.
> Setting `effort` explicitly to the model's default is equivalent to omitting it and does not break
> the cache."

Best practice, verbatim: "**Hold effort constant within cached conversations** … vary effort across
workloads rather than within a conversation that relies on cache hits."

And the documented alternative when some turns need more thinking: per-message prompt steering.
"guidance appended to the newest user message leaves earlier cache breakpoints intact, where a
configuration or effort change does not."

**Discriminator:** in a scenario with a long cached conversation where one turn needs deeper reasoning,
raising effort for that turn is the wrong answer — it costs the cache. Per-message prompt steering is
the documented right answer.

---

## RQ4 — Fast mode

**Sources:**
https://platform.claude.com/en/docs/build-with-claude/fast-mode — fetched 2026-08-22 **[RAW]**
https://code.claude.com/docs/en/fast-mode — fetched 2026-08-22 **[RAW]**

### What it is, verbatim (API page)

> "Fast mode delivers up to 2.5x higher output tokens per second from Claude Opus 5 and Claude Opus 4.8
> at premium pricing."

> "Fast mode runs the same model with a faster inference configuration. There is no change to
> intelligence or capabilities."

Bulleted, verbatim:
- "Up to 2.5x higher output tokens per second compared to standard speed"
- "Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)"
- "Same model weights and behavior (not a different model)"
- "Compatible with streaming, where the OTPS gain is most visible"

### Where it applies [VOLATILE]

- Models: **Claude Opus 5 and Claude Opus 4.8 only.** Not Sonnet, not Haiku.
- Enabled with `speed: "fast"` plus the `fast-mode-2026-02-01` beta header.
- Research preview; access is not self-serve ("Contact your account manager to request access.").
- Claude API only, including Claude Managed Agents. "It is not available on Amazon Bedrock, Claude
  Platform on AWS, Google Cloud, or Microsoft Foundry."
- Not available with the Batch API. Not available with a Priority Tier commitment.
- Pricing: $10/MTok input, $50/MTok output on both supported models.
- Two non-obvious model behaviours: Opus 4.7 **errors** on `speed: "fast"`; Opus 4.6 **silently runs at
  standard speed** and reports `usage.speed: "standard"`.

### The tradeoff, stated as a tradeoff (Claude Code page)

> "Fast mode is a high-speed configuration for Claude Opus, making the model up to 2.5x faster at a
> higher cost per token."

> "Fast mode is not a different model. It uses Claude Opus with a different API configuration that
> prioritizes speed over cost efficiency. You get identical quality and capabilities with faster
> responses."

**Fast mode vs effort level — the docs' own comparison table, verbatim:**

| Setting | Effect |
|---|---|
| **Fast mode** | "Same model quality, lower latency, higher cost" |
| **Lower effort level** | "Less thinking time, faster responses, potentially lower quality on complex tasks" |

> "You can combine both: use fast mode with a lower effort level for maximum speed on straightforward
> tasks."

**This table is the cleanest discriminator in the chapter.** Both levers reduce latency. Only one of
them trades quality; only one of them raises cost. A scenario saying "reduce latency without any
quality risk, budget is not the constraint" → fast mode. "Reduce latency and cost, some quality give
is acceptable" → lower effort.

### When to use which (Claude Code page, verbatim)

Fast mode is best for: "Rapid iteration on code changes · Live debugging sessions · Time-sensitive work
with tight deadlines."
Standard mode is better for: "Long autonomous tasks where speed matters less · Batch processing or
CI/CD pipelines · Cost-sensitive workloads."

**Discriminator:** fast mode is an *interactive-work* lever. An overnight batch job is the documented
counter-case — and it is also the shape of official sample question 1 (batch, cost-sensitive), so the
two chapters reinforce each other.

### Fast mode and the prompt cache

API page: "Switching between fast and standard speed invalidates the prompt cache. Requests at
different speeds do not share cached prefixes."

Claude Code page adds the cost mechanic: "The first time you enable fast mode in a conversation, you
pay the full fast mode uncached input token price for the entire conversation context. The deeper into
a conversation you are, the more this costs, so enabling fast mode from the start is cheaper."

**Discriminator:** toggling fast mode mid-conversation is a documented anti-pattern. Turn it on at the
start or not at all.

---

## RQ5 — Behaviour changes across model releases

### The deprecation policy

**Source:** https://platform.claude.com/en/docs/about-claude/model-deprecations — fetched 2026-08-22
**[RAW]**

The four lifecycle terms, verbatim:

- **Active:** "The model is fully supported and recommended for use."
- **Legacy:** "The model will no longer receive updates and may be deprecated in the future."
- **Deprecated:** "The model is still functional but no longer recommended. Anthropic provides a
  recommended replacement and assigns a retirement date."
- **Retired:** "The model is no longer available for use. Requests to retired models will fail."

> "Deprecated models are likely to be less reliable than active models. Move workloads to active models
> to maintain the highest level of support and reliability."

Notice period [VOLATILE]: "Anthropic notifies customers with active deployments for models with
upcoming retirements, providing at least 60 days' notice before model retirement for publicly released
models."

Platform split — a real discriminator: "The dates on this page apply to Anthropic-operated platforms:
the Claude API, Claude Platform on AWS, and Microsoft Foundry. Partner-operated platforms (Amazon
Bedrock and Google Cloud) set their own retirement schedules, so a model's lifecycle status and dates
can differ."

Best practices, verbatim: "Regularly check the documentation for updates on model deprecations. · Test
your applications with newer models well before the retirement date of your current model. · Update
your code to use the recommended replacement model as soon as possible."

Auditing mechanism: the Console **Usage** page has an **Export** producing a CSV "to see usage broken
down by API key and model" — the documented way to find which of your code paths still call a
deprecated model.

**Discriminator:** "deprecated" ≠ "broken". Deprecated models still work; retired models fail. A
scenario where requests suddenly start failing after a date points at retirement, not deprecation.

### API parameter deprecations [VOLATILE but conceptually important]

Same page. `temperature`, `top_p`, `top_k` are "Deprecated (Claude Opus 4.7 and later)" and "Return a
400 error when set to a non-default value on Claude 4.7 and later models". Recommended replacement:
"Omit and use prompting to guide model behavior."

**This is a first-class Chapter 3 fact.** A prompt tuned on an older model that leaned on `temperature`
does not merely behave differently on a new model — it fails with a 400. Behaviour change across
releases includes parameters disappearing.

### The migration guide

**Source:** https://platform.claude.com/en/docs/about-claude/models/migration-guide — fetched
2026-08-22 **[VIA-SUMMARIZER]** — a documented migration guidance page exists at this URL. Treat the
following as reported content, not verbatim quotation.

Named behaviour changes reported from that page:

- Prompts tuned on older models may behave differently on newer ones — the guide's recurring theme.
- **Opus 5 vs earlier:** response length calibrates to task complexity rather than a fixed verbosity;
  more literal instruction following (does not silently generalise or infer unstated requests); more
  direct tone; built-in progress updates in agentic traces; delegates to subagents more readily than
  Opus 4.8; respects effort levels more strictly, especially at the low end; makes fewer tool calls by
  default than Opus 4.6.
- **Effort settings do not carry over.** Reported guidance: run a fresh effort sweep on your own evals
  rather than reusing a setting tuned for an earlier model. (This is independently corroborated
  **[RAW]** on the effort page: "If you carried effort settings over from an earlier model, run a fresh
  effort sweep on your evals rather than reusing them.")
- **Thinking defaults changed.** Requests with no `thinking` field now use adaptive thinking on Opus 5
  / Fable 5 / Mythos 5 — so `max_tokens` needs revisiting.
- **Tokenizer changed.** Opus 4.7 and later produce more tokens for the same text. Corroborated
  **[RAW]** on the models overview page, which states Fable 5 "uses the tokenizer introduced with
  Claude Opus 4.7; compared to models before Claude Opus 4.7, the same text produces roughly 30% more
  tokens. The exact increase depends on the content." [VOLATILE — the ~30% figure]
- **Assistant prefill removed** on 4.7+. Corroborated **[RAW]** on the increase-consistency page:
  "Prefilling is not supported on Claude 4.6 and later models and Claude Mythos Preview. Use structured
  outputs on models that support it, or system prompt instructions, instead." (Note: the two pages give
  slightly different generation boundaries for prefill — 4.6-and-later vs 4.7+. **Do not state a
  boundary in the chapter.** Say prefill is no longer supported on current models and cite the
  consistency page.)
- **A new stop reason appeared.** `stop_reason: "refusal"` with a `stop_details.category` field on
  Claude Fable 5. This is a behaviour change that breaks response-handling code written against an
  older model — and it is the bridge into Chapter 7.
- **1M context by default** on Opus 5, no beta header. **Prompt-caching minimum lowered** to 512 tokens
  on Opus 5 from 1,024 on Opus 4.8 [VOLATILE].

Reported migration checklist: update the model ID; re-baseline cost and latency because token counts
and pricing differ across generations; test on your own workloads rather than carrying over settings;
run fresh effort sweeps; verify stop-reason handling for refusals and fallback logic; validate token
budgets against the new tokenization.

**Discriminator for the chapter:** "we changed the model ID and shipped" is the wrong answer in any
migration scenario. The documented answer is evaluate-then-switch, and the specific things to re-check
are cost baseline, effort setting, `max_tokens`, and stop-reason handling.

---

## RQ6 — Choosing between tiers on quality, latency, cost

**Source:** https://platform.claude.com/en/docs/about-claude/models/choosing-a-model — fetched
2026-08-22 **[RAW]**

### The four criteria, verbatim

> "**Capabilities:** What specific features or capabilities will you need the model to have to meet
> your needs?"
> "**Speed:** How quickly does the model need to respond in your application?"
> "**Cost:** What's your budget for both development and production usage?"
> "**Effort:** Recent Opus and Sonnet models support an effort parameter that trades intelligence for
> latency and cost within a single model. **Tuning effort is often a better lever than switching
> models.**"

**That bolded sentence is the chapter's thesis, in Anthropic's own words.** Chapter 3 exists because
the docs say the per-call dial is frequently the better move than the per-application one.

### The two starting strategies, verbatim headings and steps

**Option 1: Start efficiency-first** — "Begin implementation with Claude Haiku 4.5. · Test your use case
thoroughly. · Evaluate if performance meets your requirements. · Upgrade only if necessary for specific
capability gaps."
Best for: "Initial prototyping and development · Applications with tight latency requirements ·
Cost-sensitive implementations · High-volume, straightforward tasks".

**Option 2: Start capability-first** — "Implement with Claude Opus 5. · Optimize your prompts for this
model. · Evaluate if performance meets your requirements. · Consider increasing efficiency by lowering
effort or downgrading models over time".
Best for: "Complex reasoning tasks · Scientific or mathematical applications · Tasks requiring nuanced
understanding · Applications where accuracy outweighs cost considerations · Advanced coding and
high-autonomy agentic work".

**Discriminator:** both directions are documented as legitimate. The scenario's stated constraint picks
between them — latency/volume/cost → efficiency-first; accuracy/complexity → capability-first. An exam
option asserting one universal starting point is wrong on the docs' own terms.

### The model selection matrix, verbatim

| When you need... | Consider starting with... |
|---|---|
| "The highest available capability" | Claude Fable 5 |
| "Complex agentic coding and enterprise work" | Claude Opus 5 |
| "Frontier intelligence at scale, built for coding, agents, and enterprise workflows" | Claude Sonnet 5 |
| "Near-frontier performance with lightning-fast speed and extended thinking at the most economical price point" | Claude Haiku 4.5 |

Example use cases, verbatim: Fable 5 — "Long-running agents, deep reasoning, long-horizon agentic tasks,
advanced research". Opus 5 — "Multihour autonomous coding agents, large-scale refactoring, complex
systems engineering, advanced research, knowledge work, vision-heavy workflows, computer use".
Sonnet 5 — "Code generation, data analysis, content creation, visual understanding, agentic tool use".
Haiku 4.5 — "Real-time applications, high-volume intelligent processing, cost-sensitive deployments
needing strong reasoning, sub-agent tasks".

### How to decide whether to change models, verbatim

> "Create benchmark tests specific to your use case — having a good evaluation set is the most
> important step in the process. · Test with your actual prompts and data. · Compare performance across
> models for: Accuracy of responses, Response quality, Handling of edge cases · Weigh performance and
> cost tradeoffs."

### The measured cost/intelligence guidance

**Source:** https://platform.claude.com/en/docs/about-claude/models/optimizing-for-cost-and-intelligence
— fetched 2026-08-22 **[RAW]**

The page's routing table maps a situation to a lever. The rows that matter for Chapter 3:

| Situation (verbatim) | Documented action (verbatim) |
|---|---|
| "Costs are too high; quality is fine" | "Sweep effort down on your current model" |
| "You are choosing or switching models" | "Compare on cost per completed task, not per token" |
| "Quality isn't good enough" | "If you lowered effort, restore it; otherwise try the next tier up at `low` effort" |
| "Attempts end with `stop_reason: max_tokens`" | "Raise `max_tokens`" |
| "You can check outputs (tests, a verifier)" | "Run everything at low effort and re-run failures at the default (`high`)" |

Two verbatim sentences worth the chapter's space:

> "Price lists are written per token, and per token the frontier model looks expensive… You pay for
> completed tasks, though, so compare models on cost per completed task."

> "Sweep effort on your current model first. It is the cheapest experiment on this page, and most
> workloads end there."

And, on the tempting instinct to add a second model:

> "draw this curve for your own workload before you add a second model: in these internal measurements,
> a multi-model configuration that looked cheaper than the default single model cost more than that
> same model at lower effort."

**Discriminator, and it is the chapter's closing move:** given a cost problem, the documented ordering
is (1) free wins — caching, token trimming; (2) sweep effort down; (3) only then compare models or add
a second one. An option that jumps straight to "switch to a cheaper model" or "add a router model"
skips two cheaper levers the docs put first.

Ordering of current models by cost and capability, verbatim: "From lowest to highest cost and
capability, the current models are Claude Haiku 4.5, Claude Sonnet 5, Claude Opus 5, and Claude
Fable 5 (the frontier model)."

Two multi-model strategies, verbatim from the strategy table:

| Strategy | Control flow | Fits |
|---|---|---|
| **Advisor** | "Smaller model runs the loop, escalates on demand" | "Serial work that is hard in spots, such as a coding agent's many turns between a few real decisions" |
| **Orchestrator** | "Frontier model runs the loop, delegates the bulk work" | "Work that fans out across genuinely independent files, documents, or cases, especially more than one context window of it" |

The choosing rule, verbatim: "does the work split into independent pieces, or is it one answer reached
through a chain of dependent steps?"

---

# CHAPTER 7 — "When asking nicely stops working"

## RQ1 — Mechanisms for guaranteeing output shape

**Source:** https://platform.claude.com/en/docs/build-with-claude/structured-outputs — fetched
2026-08-22 **[VIA-SUMMARIZER]** (fetched twice with different prompts; both returns were summarizer
output, not raw markdown). Corroborating raw sources are noted where available.

**Two mechanisms, named:**

1. **JSON outputs** — `output_config.format` with `{"type": "json_schema", "schema": {...}}`. Controls
   the *response* format.
2. **Strict tool use** — `strict: true` on a tool definition. Controls *tool call inputs*.

Reported guarantee language: "Structured outputs guarantee schema-compliant responses through
constrained decoding" — "Always valid" (no `JSON.parse()` errors), "Type safe" (guaranteed field types
and required fields), "Reliable" (no retries needed for schema violations).

**The mechanism is corroborated [RAW]** on the strict tool use page: schema conformance is enforced "by
constraining the model's token sampling to schema-valid outputs (a technique called grammar-constrained
sampling)."

Supported models [VOLATILE]: reported as all current models — Opus 5, Opus 4.8, Opus 4.7, Opus 4.6,
Sonnet 5, Sonnet 4.6, Sonnet 4.5, Haiku 4.5, Mythos 5, Mythos Preview.

**The doc's own routing sentence, and this one IS [RAW]** — from
https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency
(fetched 2026-08-22):

> "If you need Claude to always output valid JSON that conforms to a specific schema, use Structured
> Outputs instead of the prompt engineering techniques below. Structured outputs provide guaranteed
> schema compliance and are specifically designed for this use case.
>
> The techniques below are useful for general output consistency or when you need flexibility beyond
> strict JSON schemas."

**This is the chapter's thesis sentence and it is verifiably verbatim.** The docs themselves route
"must always conform" away from prompting and into the API.

The prompt-engineering techniques that page offers as the *other* branch, for general consistency:
specify the desired output format precisely; prefill Claude's response (**no longer supported on
current models** — see Ch3 RQ5); constrain with examples; use retrieval for contextual consistency;
chain prompts for complex tasks; keep Claude in character via system prompts.

---

## RQ2 — What strict tool use guarantees, and how it differs from asking

**Source:** https://platform.claude.com/en/docs/agents-and-tools/tool-use/strict-tool-use — fetched
2026-08-22 **[RAW]**

### The guarantee, verbatim

> "Setting `strict: true` on a tool definition guarantees Claude's tool inputs match your JSON Schema
> by constraining the model's token sampling to schema-valid outputs (a technique called
> grammar-constrained sampling)."

Stated guarantees, verbatim bullets:
- "Tool `input` strictly follows the `input_schema`"
- "Tool `name` is always valid (from provided tools or server tools)"

### The failure it prevents, in the docs' own example

> "Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required
> fields, breaking your functions and causing runtime errors."

> "For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might
> provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains
> `passengers: 2`."

> "Strict tool use guarantees type-safe parameters: Functions receive correctly-typed arguments every
> time · No need to validate and retry tool calls · Production-ready agents that work consistently at
> scale."

When to use it, verbatim: "Validate tool parameters · Build agentic workflows · Ensure type-safe
function calls · Handle complex tools with nested properties."

### How non-strict differs

The non-strict counterpart is documented in the tool-use overview
(https://platform.claude.com/en/docs/agents-and-tools/tool-use/overview — fetched 2026-08-22 **[RAW]**),
which shows what "asking nicely" actually gets you. On missing required parameters:

> "If the user's prompt doesn't include enough information to fill all the required parameters for a
> tool, Claude Opus is much more likely to recognize that a parameter is missing and ask for it. Claude
> Sonnet might ask, especially when prompted to think before outputting a tool request. But it might
> also infer a reasonable value."

> "This behavior is not guaranteed, especially for more ambiguous prompts and for less capable models."

**This is the chapter's best single discriminator.** Without the API-level guarantee, correct behaviour
is a *model-tier property* that degrades on cheaper models and ambiguous prompts. With `strict: true`,
it is a property of the request. That is exactly the move the chapter's title describes — the guarantee
leaves the prompt and enters the API.

The same page's own pointer, verbatim: "**Guarantee schema conformance with strict tool use** — Add
`strict: true` to your custom tool definitions to ensure Claude's tool calls always match your schema
exactly."

Prompting is documented as the *steering* lever for a different question — *whether* Claude calls a
tool, not *what shape* the call takes: "If Claude isn't calling tools when you expect, a light
instruction such as `"Use the tools to investigate before responding."` increases tool use… To require
a tool call rather than rely on prompting, set `tool_choice`."

**Discriminator:** three different levers, three different guarantees. `tool_choice` forces *that* a
tool is called. `strict: true` guarantees the *shape* of the call. Prompting nudges both and guarantees
neither.

### Documented limits on strict tool use [RAW]

- The computer use and browser use toolset entries (`computer_toolset_20260801`,
  `browser_toolset_20260801`) "don't accept `strict: true`; a request that sets it on either entry is
  rejected." [VOLATILE — the toolset identifiers]
- Schema caching: "Tool schemas are temporarily cached for up to 24 hours since last use." [VOLATILE]
- HIPAA: strict tool use is HIPAA eligible, but "**protected health information (PHI) must not be
  included in tool schema definitions**" — not in property names, `enum` values, `const` values, or
  `pattern` regexes, because compiled schemas are cached separately from message content and do not get
  the same protections.

**Discriminator with a security flavour:** the schema is not part of the protected message body. That
is a genuine, non-obvious constraint and it crosses into the Security domain.

---

## RQ3 — Where the guarantee does not hold

All from https://platform.claude.com/en/docs/build-with-claude/structured-outputs — fetched 2026-08-22
**[VIA-SUMMARIZER]**, except where a raw corroborating source is named. Treat quoted strings as
reported.

### The limit that matters most

Reported verbatim: "Structured outputs guarantee that Claude's response matches your schema, but do NOT
guarantee the content is correct or accurate — only that it is schema-valid."

**This is the whole justification for the chapter's fourth sub-topic (`skepticism toward confident
output`) and it should be its closing line.** A schema-valid answer is a well-shaped answer, not a true
one. Validation moved a class of failure — malformed output — out of the application. It did not move
wrongness.

### Truncation

Reported: "If the response is truncated due to `max_tokens`, the final JSON may be incomplete or
invalid. Check the `stop_reason` field: if it is `"max_tokens"`, the response was truncated and should
not be trusted."

**Corroborated [RAW]** by the thinking troubleshooting page, which documents the same failure from the
thinking side: "The response ends with `stop_reason: "max_tokens"`, often with a truncated or missing
text block. This happens because thinking tokens count toward `max_tokens`."

**Discriminator, and it links Chapter 3 to Chapter 7:** raising effort makes truncation *more* likely,
because thinking eats the same `max_tokens` budget the JSON needs. A scenario where structured output
started coming back invalid after a model or effort change has this as its cause.

### Refusal

Reported: "If Claude refuses a request (for example, due to safety policies), it will return a text
response rather than structured output."

⚠️ **Conflict flag — do not state a stop_reason for the refusal case.** The structured-outputs
summarizer reported that on refusal `stop_reason` will be `"end_turn"`. The stop-reasons page
**[VIA-SUMMARIZER]** documents a dedicated `refusal` stop reason, and the migration guide reports
`stop_reason: "refusal"` as *newly introduced* on Fable 5. These may both be true (different models,
different eras) or one may be a summarizer error. **Chapter 7 should say: a refusal returns text rather
than schema-conformant output, and the response must be checked before parsing — without asserting
which stop_reason value accompanies it.** See gap list.

### Unsupported schema features [VOLATILE — the specific keyword list]

Reported as **not supported**: recursive schemas; complex types within enums; external `$ref` (e.g.
`'$ref': 'http://...'`); numerical constraints (`minimum`, `maximum`, `multipleOf`); string constraints
(`minLength`, `maxLength`); array `maxItems` (only `minItems` with values 0 or 1 supported).

Reported as **supported**: basic types (object, array, string, integer, number, boolean, null); `enum`
(strings, numbers, bools, nulls only); `const`; `anyOf` and `allOf` with limitations; internal `$ref`,
`$def`, `definitions`; string formats (`date-time`, `time`, `date`, `duration`, `email`, `hostname`,
`uri`, `ipv4`, `ipv6`, `uuid`); `additionalProperties: false` (required for objects).

**The examinable idea, not the list:** the guarantee covers *structure*, not *semantics*. `minimum` and
`maxLength` are business rules, and they are exactly the keywords the constrained decoder does not
enforce. So a schema is not a validator — range and length checks still belong in your code. This is
the strongest available support for `defensive parsing` as a sub-topic.

### Latency caveat [VOLATILE]

Reported: first use of a specific schema incurs grammar-compilation latency; compiled grammars are
cached for 24 hours from last use; the cache is invalidated by changing the JSON schema structure or
the set of tools in the request, but "Changing only `name` or `description` fields does not invalidate
the cache."

### The full stop_reason table

**Source:** https://platform.claude.com/en/docs/build-with-claude/handling-stop-reasons — fetched
2026-08-22 **[VIA-SUMMARIZER]**. Page confirmed to exist at that URL; title reported as "Stop reasons
and fallback". (The same table was returned from
https://platform.claude.com/en/docs/api/handling-stop-reasons, also **[VIA-SUMMARIZER]**, and the two
agreed exactly — which raises confidence in the table's content even though neither return was raw.)

| Value | When it occurs | What to do |
|---|---|---|
| `end_turn` | "Claude finished its response naturally." | "Use the response." |
| `max_tokens` | "The response reached your `max_tokens` limit." | "Raise `max_tokens` or continue the response." |
| `stop_sequence` | "Claude emitted one of your `stop_sequences`." | "Read `stop_sequence` to see which one fired." |
| `tool_use` | "Claude is calling a tool." | "Run the tool and return the result." |
| `pause_turn` | "A server-tool loop reached its iteration limit." | "Send the assistant content back to continue." |
| `refusal` | "Claude declined to respond." | "Read `stop_details` and retry on a fallback model." |
| `model_context_window_exceeded` | "The response filled the model's context window." | "Treat the response as truncated." |

Reported additional details:
- On `refusal`, `stop_details` identifies the policy category that triggered it, and a refused request
  can usually be served by retrying on another Claude model.
- On `max_tokens` with an incomplete `tool_use` block, retry with a higher `max_tokens` to get the full
  tool use.
- **The instruction to check:** "Check this field to decide whether to use the response as-is, continue
  the conversation, retry, or fall back to another model," and "Make it a habit to check the
  `stop_reason` in your response handling logic."
- Stop reasons are *successful* responses. Errors are HTTP 4xx/5xx. These are two different failure
  channels.

**Two discriminators here, both strong:**
1. `max_tokens` and `model_context_window_exceeded` are different truncations with different causes —
   your cap versus the model's ceiling. A scenario where raising `max_tokens` did not help points at
   the second.
2. `refusal` is handled by **falling back to another model**, not by retrying the same one, not by
   rewording the prompt. That is a documented, specific action and a natural correct answer against
   three plausible ones.

---

## RQ4 — Validating and parsing defensively

### The SDK layer

**Source:** structured outputs page — fetched 2026-08-22 **[VIA-SUMMARIZER]**

The SDKs provide typed parse helpers: `client.messages.parse(...)` with a Pydantic model in Python
(returning `response.parsed_output`), `zodOutputFormat` in TypeScript, and native type derivation in
Java, C#, Ruby and PHP. With a raw JSON schema you extract the text block and `json.loads` it yourself.

**The conceptual point for a no-code exam:** the guarantee has a typed landing place. You do not have
to hand-roll validation of the *shape*. You still have to handle the *cases where the shape guarantee
lapses* — which is the previous section.

### The verification layer

**Source:** https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
— fetched 2026-08-22 **[RAW]**

Basic strategies, verbatim:

- "**Allow Claude to say 'I don't know':** Explicitly give Claude permission to admit uncertainty. This
  simple technique can drastically reduce false information."
- "**Use direct quotes for factual grounding:** For tasks involving long documents (>20k tokens), ask
  Claude to extract word-for-word quotes first before performing its task. This grounds its responses
  in the actual text, reducing hallucinations."
- "**Verify with citations:** Make Claude's response auditable by having it cite quotes and sources for
  each of its claims. You can also have Claude verify each claim by finding a supporting quote after it
  generates a response. If it can't find a quote, it must retract the claim."

Advanced techniques, verbatim: "**Chain-of-thought verification** … **Best-of-N verification**: Run
Claude through the same prompt multiple times and compare the outputs. Inconsistencies across outputs
could indicate hallucinations. · **Iterative refinement** … · **External knowledge restriction**:
Explicitly instruct Claude to only use information from provided documents and not its general
knowledge."

The page's closing note, verbatim and load-bearing:

> "Remember, while these techniques significantly reduce hallucinations, they don't eliminate them
> entirely. Always validate critical information, especially for high-stakes decisions."

**Discriminator:** these are *content* controls; structured outputs are *shape* controls. They do not
substitute for each other. A scenario where the JSON is well-formed but the values are wrong is not
fixed by a schema — it is fixed by grounding, citation, or an out-of-band check. Conversely, a scenario
where parsing intermittently fails is not fixed by better prompting; the docs route that to structured
outputs explicitly.

### The chapter's decision table (assembled from the sources above)

| The problem stated | Documented mechanism | Source |
|---|---|---|
| JSON sometimes fails to parse | Structured outputs (`output_config.format`) | increase-consistency [RAW], structured-outputs |
| Tool called with wrong types or missing fields | `strict: true` | strict-tool-use [RAW] |
| Claude doesn't call the tool at all | Prompt steering, then `tool_choice` | tool-use overview [RAW] |
| Response arrives truncated | Check `stop_reason`; raise `max_tokens` or lower effort | handling-stop-reasons, thinking-troubleshooting [RAW] |
| Claude declines the request | Check `stop_reason`/`stop_details`; fall back to another model | handling-stop-reasons |
| Values are well-formed but wrong | Grounding, quotes, citations, best-of-N; validate critical info | reduce-hallucinations [RAW] |
| Business rules (ranges, lengths) must hold | Not covered by the schema guarantee — validate in your code | structured-outputs limitations |

---

# GAP LIST 1 — What I could not establish

1. **The stop_reason that accompanies a structured-output refusal.** The structured-outputs page
   (via summarizer) reported `stop_reason: "end_turn"` on refusal; the stop-reasons page documents a
   dedicated `refusal` value, and the migration guide reports `refusal` as newly introduced on
   Claude Fable 5. I could not reconcile these from raw page text. **Chapter 7 must not assert a value
   here.** Resolution needs a raw fetch of the structured-outputs refusal section.

2. **Raw markdown for three pages.** The migration guide, the structured outputs page (two attempts),
   and the handling-stop-reasons page all returned summarizer output rather than page source. Every
   quoted string sourced only to those three is a *reported* quote. Anything that must appear inside
   quotation marks in the chapter should be re-fetched, ideally against the `.md` variants of those
   URLs.

3. **Whether "adaptive thinking" has its own titled documentation page.** A search result listed
   `https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking`, but fetching that path
   returned the page titled "Steering thinking" at
   `.../build-with-claude/thinking-steering-and-cost`. Cite the steering page, not an adaptive-thinking
   page, until this is checked again.

4. **Effort level availability for Claude Haiku 4.5.** Haiku 4.5 is absent from the effort page's
   supported-models list, which strongly implies effort is unavailable there — but the page does not
   say so explicitly, and I did not find a sentence stating it. **Do not write "Haiku does not support
   effort" as a fact.** Write that the published supported-model list does not include it.

5. **Anthropic's exact wording on the trade fast mode makes.** The docs are explicit that fast mode
   changes nothing about intelligence or capability and costs more per token. I found no sentence
   naming a quality or capability cost, and I am not going to invent one. Fast mode's documented trade
   is **cost**, not quality. If the chapter wants a "what does it give up" beat, the answer is money
   and availability (research preview, Opus-only, no Batch, no Priority Tier), not accuracy.

6. **Whether prefill is unsupported from 4.6 or from 4.7.** The increase-consistency page says "Claude
   4.6 and later models"; the migration guide (via summarizer) reports 4.7+. Unresolved. State the fact
   without the generation boundary.

7. **Anything about `thinking` behaviour on third-party platforms** (Bedrock, Google Cloud, Microsoft
   Foundry) beyond the beta-header acceptance note on the extended-thinking page. Not investigated;
   out of the two chapters' scope but adjacent to blueprint skill 2.3.

8. **A published Anthropic definition of "defensive parsing."** The exam blueprint uses the phrase.
   Nothing on any page fetched today uses it. Chapter 7 should teach the practice from the documented
   pieces (check `stop_reason`, don't assume schema keywords enforce business rules, validate critical
   values) rather than presenting "defensive parsing" as an Anthropic term of art.

9. **Whether Claude Haiku 4.5 supports structured outputs.** Reported in the supported-models list from
   the structured-outputs summarizer only. Not corroborated on a raw page. Low risk, but unverified.

---

# GAP LIST 2 — What I found only on non-authoritative sources

**Nothing.** Every fact in this pack came from a page on `platform.claude.com` or `code.claude.com`.

Search was constrained to `platform.claude.com`, `docs.claude.com`, `claude.com`, `anthropic.com` and
`code.claude.com` on every query, so no community source entered the pipeline. Two searches surfaced
`claude.com/blog` URLs (a post on structured outputs on the developer platform, and one on Claude Code
effort level and model selection) — **neither was fetched and neither contributed a fact here**, because
the same content was available on the documentation pages.

No search returned empty. All four searches run returned results.

---

# VOLATILE INDEX — quarantine candidates

Everything below is a number, header, date, ID, or price that will drift. None of it is judgement.
Recommend the writer keeps at most the ones marked ✅.

| Item | Where it appears | Keep? |
|---|---|---|
| Per-model pricing ($/MTok) | Ch3 RQ1, RQ4 | ✗ — teach the *ordering*, not the numbers |
| Context windows (1M / 200k), max output (128k / 64k) | Ch3 RQ1 | ✗ |
| `fast-mode-2026-02-01` beta header | Ch3 RQ4 | ✗ |
| `speed: "fast"` parameter | Ch3 RQ4 | ✅ — the *name* of the switch is worth one mention |
| "up to 2.5x higher output tokens per second" | Ch3 RQ4 | ✅ — magnitude is the point |
| `interleaved-thinking-2025-05-14` beta header | Ch3 RQ2 | ✗ |
| `budget_tokens` minimum of 1,024 | not used above | ✗ |
| 60-day deprecation notice | Ch3 RQ5 | ✅ — it is the shape of the policy |
| Specific retirement dates | Ch3 RQ5 | ✗ |
| ~30% tokenizer increase on 4.7+ | Ch3 RQ5 | ✅ — as "roughly a third more", not a figure |
| Prompt-cache minimum 512 vs 1,024 tokens | Ch3 RQ5 | ✗ |
| Effort level *names* (`low`…`max`) | Ch3 RQ3 | ✅ — the blueprint names "effort levels" |
| Per-model effort availability lists | Ch3 RQ3 | ✗ |
| Unsupported JSON Schema keyword list | Ch7 RQ3 | ✗ — teach "structure not semantics" |
| 24-hour grammar cache | Ch7 RQ2, RQ3 | ✗ |
| `computer_toolset_20260801` / `browser_toolset_20260801` | Ch7 RQ2 | ✗ |
| `stop_reason` value names | Ch7 RQ3 | ✅ — the values are the decision points |
| Model IDs (`claude-opus-5` etc.) | Ch3 RQ1 | ✅ only for the pinned-snapshot point |

---

# SOURCES — every URL fetched, 2026-08-22

**Raw markdown returned [RAW]:**

1. https://platform.claude.com/en/docs/about-claude/models/overview
2. https://platform.claude.com/en/docs/build-with-claude/extended-thinking
3. https://platform.claude.com/en/docs/build-with-claude/thinking
4. https://platform.claude.com/en/docs/build-with-claude/thinking-steering-and-cost (reached via
   `.../build-with-claude/adaptive-thinking`)
5. https://platform.claude.com/en/docs/build-with-claude/thinking-troubleshooting
6. https://platform.claude.com/en/docs/build-with-claude/effort
7. https://platform.claude.com/en/docs/build-with-claude/fast-mode
8. https://platform.claude.com/en/docs/about-claude/models/choosing-a-model
9. https://platform.claude.com/en/docs/about-claude/models/optimizing-for-cost-and-intelligence
10. https://platform.claude.com/en/docs/about-claude/model-deprecations
11. https://platform.claude.com/en/docs/agents-and-tools/tool-use/overview
12. https://platform.claude.com/en/docs/agents-and-tools/tool-use/strict-tool-use
13. https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency
14. https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
15. https://code.claude.com/docs/en/fast-mode

**Summarizer output returned [VIA-SUMMARIZER] — re-fetch before quoting:**

16. https://platform.claude.com/en/docs/about-claude/models/migration-guide
17. https://platform.claude.com/en/docs/build-with-claude/structured-outputs (fetched twice)
18. https://platform.claude.com/en/docs/build-with-claude/handling-stop-reasons
19. https://platform.claude.com/en/docs/api/handling-stop-reasons

**Searches run** (all domain-constrained to Anthropic-controlled hosts; all returned results):

- `Anthropic Claude "adaptive thinking" docs`
- `Claude API "effort" parameter "fast mode" model documentation`
- `Claude docs increase output consistency JSON validation parse response reliability`

**Local file read:** `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude
Certified Developer Foundations\EXAM-FACTS_v1.md` (sections 1, 2, 5).
