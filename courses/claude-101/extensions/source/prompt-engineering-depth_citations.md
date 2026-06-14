# Citations & Research Notes — Prompt Engineering Depth + Model Selection (C-E5)

## Manifest
- **Date researched:** 2026-06-06 · **Re-verified 2026-06-09** (core facts confirmed; additive drifts noted in the addendum at the end of this file. Full sweep: `QA-VERIFY-SWEEP_2026-06-09.md`)
- **CCA-F domains:** Domain 3 (Prompt Engineering & Structured Output, 20%) primary; Domain 1 (model fundamentals) and Domain 5 (deployment/cost/agentic) overlap in Section F; Domain 4 (tool use) overlaps in Section E.
- **Critical version note up front:** Anthropic's docs *consolidated* the old per-technique pages (be-clear-and-direct, multishot-prompting, chain-of-thought, etc.) into a single living reference, **"Prompting best practices."** Two findings overturn legacy Claude-101-era material: (1) **prefill on the last assistant turn is NO LONGER SUPPORTED on Claude 4.6+ models** (returns 400); (2) **manual "extended thinking" with `budget_tokens` is deprecated/removed on Opus 4.7+** in favor of **adaptive thinking + an `effort` parameter.** Both flagged inline and in the [VERIFY] list.

### Sources consulted
1. **Prompt engineering overview** — `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview` — Anthropic, PRIMARY. The "before / when / how to prompt engineer" framing; points to best-practices as the living reference.
2. **Prompting best practices** — `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` — Anthropic, PRIMARY. The single consolidated techniques reference (clarity, examples, XML, role, long context, output control, thinking, agentic, prefill migration).
3. **Models overview** — `https://platform.claude.com/docs/en/about-claude/models/overview` — Anthropic, PRIMARY. Current lineup, pricing, context windows, "Choosing a model."
4. **Migration guide** — `https://platform.claude.com/docs/en/about-claude/models/migration-guide` — Anthropic, PRIMARY. Prompt portability caveats, prefill removal, extended-thinking removal, Sonnet-vs-Opus selection notes.
5. **Structured Outputs** — `https://platform.claude.com/docs/en/build-with-claude/structured-outputs` — Anthropic, PRIMARY. JSON schema + strict tool use via constrained decoding; limits.
6. **Anthropic Prompt Engineering Overview (guide)** — `https://www.aiwithgrant.com/guides/anthropic-prompt-engineering-overview` — SECONDARY. Corroborates the classic technique ordering and the "prompting faster/cheaper than fine-tuning" rationale.
7. **Interactive Prompt Engineering Tutorial** — `https://github.com/anthropics/prompt-eng-interactive-tutorial` — Anthropic, PRIMARY (repo). Chapter ordering of the canonical teaching sequence.
8. **Model selection guide** — `https://www.sitepoint.com/claude-model-selection-framework/` — SECONDARY. Corroborates the Opus/Sonnet/Haiku tradeoff framing (default-to-Sonnet, escalate/descend). Light secondary support.

---

## Section A — Why prompt engineering (vs fine-tuning)
*(reinforces Domain 3; touches Domain 1 success-criteria thinking)*

**Be empirical before you prompt.** Anthropic's overview assumes three prerequisites: "1. A clear definition of the success criteria for your use case 2. Some ways to empirically test against those criteria 3. A first draft prompt you want to improve." If you lack these, "we highly suggest you spend time establishing that first" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). The empirical-iteration loop: define success criteria → build evals → draft prompt → iterate.

**Not every failure is a prompting problem (verbatim):** "Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). This is the bridge to Section F — model selection is a *peer lever* to prompting, not a fallback.

**Prompting beats fine-tuning for iteration speed.** "Prompt engineering is far faster and cheaper than fine-tuning" (source: https://www.aiwithgrant.com/guides/anthropic-prompt-engineering-overview, SECONDARY summarizing Anthropic docs). Framing: reach for prompting first because the change-test cycle is minutes (edit a string) vs the hours/cost of a fine-tune run, and the prompt stays transparent and portable.

**Tooling that supports the loop:** Anthropic ships a **prompt generator**, **prompt templates and variables**, and a **prompt improver** in the Claude Console to "help you build and refine prompts quickly" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview).

---

## Section B — The technique ladder (the spine)
*(reinforces Domain 3 — the core 20%)*

### Two canonical orderings — reconcile both for the lesson

**(1) The classic docs ladder** (the "Claude 101"-era ordered list this lesson extends): be clear and direct → use examples (multishot) → let Claude think (chain of thought) → use XML tags → give Claude a role (system prompts) → chain complex prompts → long context tips (source: https://www.aiwithgrant.com/guides/anthropic-prompt-engineering-overview, SECONDARY). Note: the docs do **not** label this a "ladder" and do **not** print a one-line "cheap-first" rationale — that ordering rationale is *pedagogical framing*, not a verbatim Anthropic quote.

**(2) The interactive tutorial teaching sequence** (PRIMARY repo): Beginner — 1. Basic Prompt Structure, 2. Being Clear and Direct, 3. Assigning Roles; Intermediate — 4. Separating Data from Instructions, 5. Formatting Output & Speaking for Claude, 6. Precognition (Thinking Step by Step), 7. Using Examples; Advanced — 8. Avoiding Hallucinations, 9. Building Complex Prompts; Appendix — Chaining Prompts, Tool Use, Search & Retrieval (source: https://github.com/anthropics/prompt-eng-interactive-tutorial).

**Why order matters (lesson framing, general reasoning — NOT a verbatim Anthropic quote):** techniques are ordered cheapest-and-highest-leverage first. Clarity costs nothing and fixes the most failures; examples are the next-highest lever; thinking/CoT trades tokens and latency for accuracy; structural tools (XML, roles) shape output; chaining and long-context handling are heavier, situational moves. Try them roughly in this order and stop when your evals pass. (Consistent with Anthropic's "when to prompt engineer" note, but the explicit "cheap-first" wording is reasoning, not an Anthropic fact.)

### The rungs (each: verbatim definition → mechanics → when → snippet)

**1. Be clear and direct.** Verbatim: "Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want 'above and beyond' behavior, explicitly request it rather than relying on the model to infer this from vague prompts." Mental model: "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The more precisely you explain what you want, the better the result." **Golden rule (verbatim):** "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too." Mechanics: be specific about output format/constraints; use numbered lists/bullets "when the order or completeness of steps matters" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
Snippet (verbatim contrast): Less effective — `Create an analytics dashboard`; More effective — `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.` (same source).

**1b. Add context / motivation (clarity's twin).** Verbatim: "Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals… Claude is smart enough to generalize from the explanation." Snippet: instead of `NEVER use ellipses`, say `Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.` (source: same).

**2. Use examples / multishot (the highest-leverage rung — see Section C).** Verbatim: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) can dramatically improve accuracy and consistency." (source: same).

**3. Let Claude think / chain of thought (see Section D).** On current models mostly handled by **adaptive thinking**; manual CoT is now a *fallback* when thinking is off (source: same).

**4. Structure prompts with XML tags.** Verbatim: "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (e.g. `<instructions>`, `<context>`, `<input>`) reduces misinterpretation." Best practices (verbatim): "Use consistent, descriptive tag names across your prompts" and "Nest tags when content has a natural hierarchy." Key point: there is **no canonical/required tag vocabulary** — consistency matters more than the specific names (source: same).

**5. Give Claude a role (system prompts).** Verbatim: "Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference." Use the top-level `system` parameter. Verbatim snippet:
```python
import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="You are a helpful coding assistant specializing in Python.",
    messages=[{"role": "user", "content": "How do I sort a list of dictionaries by key?"}],
)
```
(source: same).

**6. Chain complex prompts.** Verbatim: "With adaptive thinking and subagent orchestration, Claude handles most multi-step reasoning internally. Explicit prompt chaining (breaking a task into sequential API calls) is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure." Canonical **self-correction** pattern: "generate a draft → have Claude review it against criteria → have Claude refine based on the review. Each step is a separate API call so you can log, evaluate, or branch at any point." (source: same). Chaining = a hand-built pipeline; subagent orchestration = the model doing it internally.

**7. Long context tips.** Verbatim threshold: "When working with large documents or data-rich inputs (20k+ tokens), structure your prompt carefully." Three rules:
- **Documents-first ordering (verbatim):** "Put longform data at the top: Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This can significantly improve performance across all models." Quantified (verbatim): "Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs." `[VERIFY the 30% figure]`
- **Structure with XML (verbatim):** wrap each document in `<document>` tags with `<document_content>` and `<source>` subtags; use `<document index="n">`.
- **Ground responses in quotes (verbatim):** "For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the noise of the rest of the document's contents."
(source: same).

**Note on prefill:** the classic ladder included "prefill Claude's response" as a rung. On current models this is largely removed — see Section E and [VERIFY].

---

## Section C — Examples / multishot deep-dive
*(reinforces Domain 3)*

**Why it's the highest-leverage rung (verbatim):** "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) can dramatically improve accuracy and consistency." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

**How many (verbatim):** "Include 3–5 examples for best results. You can also ask Claude to evaluate your examples for relevance and diversity, or to generate additional ones based on your initial set." `[VERIFY the exact "3–5"]`

**The three qualities of a good example set (verbatim):**
- "**Relevant:** Mirror your actual use case closely."
- "**Diverse:** Cover edge cases and vary enough that Claude doesn't pick up unintended patterns."
- "**Structured:** Wrap examples in `<example>` tags (multiple examples in `<examples>` tags) so Claude can distinguish them from instructions."
(source: same).

**Positive over negative examples (verbatim):** "Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do." (source: same). Show the model the *target*, don't enumerate what to avoid.

**Examples compound with thinking (verbatim):** "Multishot examples work with thinking. Use `<thinking>` tags inside your few-shot examples to show Claude the reasoning pattern. It will generalize that style to its own extended thinking blocks." (source: same).

---

## Section D — Chain-of-thought deep-dive
*(reinforces Domain 3; touches Domain 1 model-feature awareness)*

**MAJOR version shift — read first.** On current models (Sonnet 4.6, Haiku 4.5, Opus 4.6/4.7/4.8) the dominant mechanism is **adaptive thinking**, not hand-written "think step by step." Manual extended thinking with `budget_tokens` is **deprecated/removed on Opus 4.7+** and returns a 400 (source: https://platform.claude.com/docs/en/about-claude/models/migration-guide). Manual CoT prompting now serves as the **fallback when thinking is off**.

**The think-space spectrum (verbatim fragments):**
- **Off / direct:** "Thinking is off by default when you omit the `thinking` parameter." On Opus 4.8, "thinking is off unless you explicitly set `thinking: {type: \"adaptive\"}`."
- **Manual CoT fallback (verbatim):** "When thinking is off, you can still encourage step-by-step reasoning by asking Claude to think through the problem. Use structured tags like `<thinking>` and `<answer>` to cleanly separate reasoning from the final output."
- **General over prescriptive (verbatim):** "Prefer general instructions over prescriptive steps. A prompt like 'think thoroughly' often produces better reasoning than a hand-written step-by-step plan. Claude's reasoning frequently exceeds what a human would prescribe."
- **Self-check (verbatim):** "Ask Claude to self-check. Append something like 'Before you finish, verify your answer against [test criteria].' This catches errors reliably, especially for coding and math."
- **Adaptive (verbatim):** "Claude calibrates its thinking based on two factors: the `effort` parameter and query complexity. Higher effort elicits more thinking, and more complex queries do the same. On easier queries that don't require thinking, the model responds directly. In internal evaluations, adaptive thinking reliably drives better performance than extended thinking."
(source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

**"Show the thinking" / cost-latency tradeoff.** The structured `<thinking>`/`<answer>` pattern keeps reasoning visible (not hidden) — the modern equivalent of the classic "always have Claude output its thinking." Cost is explicit (verbatim): "Extended thinking adds latency and should only be used when it will meaningfully improve answer quality — typically for problems that require multi-step reasoning. When in doubt, respond directly." Over-thinking is a real failure mode: "Claude Opus 4.6 may think extensively, which can inflate thinking tokens and slow down responses… you can lower the `effort` setting to reduce overall thinking and token usage." (source: same).

**Word-sensitivity caveat (verbatim, version-specific):** "When extended thinking is disabled, Claude Opus 4.5 is particularly sensitive to the word 'think' and its variants. Consider using alternatives like 'consider,' 'evaluate,' or 'reason through' in those cases." `[VERIFY — model-specific]`

**Adaptive thinking + effort code shape (verbatim):**
```python
client.messages.create(
    model="claude-opus-4-8",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # or "max", "xhigh", "medium", "low"
    messages=[{"role": "user", "content": "..."}],
)
```
(source: same).

---

## Section E — Structured output
*(reinforces Domain 3 "Structured Output" + Domain 4 tool use)*

Three tiers of output control, from prompt-only to hard-guaranteed:

**Tier 1 — Prompt-level format control (verbatim, four levers):**
1. "Tell Claude what to do instead of what not to do" — instead of "Do not use markdown," try "Your response should be composed of smoothly flowing prose paragraphs."
2. "Use XML format indicators" — "Write the prose sections of your response in `<smoothly_flowing_prose_paragraphs>` tags."
3. "Match your prompt style to the desired output" — "removing markdown from your prompt can reduce the volume of markdown in the output."
4. "Use detailed prompts for specific formatting preferences."
(source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

**Tier 2 — XML output contracts.** Have the model write its answer inside named tags (`<quotes>`, `<info>`, `<answer>`) so downstream code parses deterministically. Pairs with the long-context "ground in quotes" pattern (source: same).

**Tier 3 — Structured Outputs (the hard guarantee).** Verbatim: "Structured outputs constrain Claude's responses to follow a specific schema, ensuring valid, parseable output for downstream processing." Two features: **JSON outputs** (`output_config.format`) — "Get Claude's response in a specific JSON format"; and **strict tool use** (`strict: true`) — "Guarantee schema validation on tool names and inputs." Both use **constrained decoding**: output is "Always valid: No more `JSON.parse()` errors," "Type safe," "Reliable: No retries needed for schema violations." (source: https://platform.claude.com/docs/en/build-with-claude/structured-outputs).

JSON-outputs code shape (verbatim):
```python
response = client.messages.parse(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[...],
    output_config={"format": {"type": "json_schema",
        "schema": {"type": "object",
            "properties": {"name": {"type": "string"}, "email": {"type": "string"}},
            "required": ["name", "email"], "additionalProperties": False}}},
)
```
**Key limits (verbatim):** NOT supported — "Recursive schemas," "External `$ref`," "Numerical constraints (`minimum`, `maximum`…)", "String constraints (`minLength`, `maxLength`)"; `additionalProperties` must be `false`. Limits: 20 strict tools/request; 24 optional params; 16 union-typed params. "Compiled grammars are cached for 24 hours"; "additional latency while the grammar compiles" on first request. Supported on Opus 4.8/4.7/4.6/4.5, Sonnet 4.6/4.5, Haiku 4.5 (source: same). `[VERIFY model-support list]`

**PREFILL — the big change (verbatim):** "Starting with Claude 4.6 models and Claude Mythos Preview, prefilled responses on the last assistant turn are no longer supported. Requests with prefilled assistant messages to these models return a 400 error… Earlier models continue to support prefills, and adding assistant messages elsewhere in the conversation is not affected." Migration of classic prefill uses (verbatim): forcing JSON → "use the Structured Outputs feature"; eliminating preambles → system-prompt instruction "Respond directly without preamble. Do not start with phrases like 'Here is...'…"; continuations → move to the user turn (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). **Teaching implication:** the classic "prefill" rung is now a *legacy technique* (pre-4.6 only), replaced by Structured Outputs + direct instructions. Legacy constraints worth noting: prefill text "can't end with trailing whitespace," and prefill is incompatible with extended thinking. `[VERIFY these two classic constraints against the legacy page]`

**Classification (verbatim):** "For classification tasks, use either tools with an enum field containing your valid labels or structured outputs." (source: same).

---

## Section F — Model selection
*(reinforces Domain 1 + Domain 5; connects to C-E4 cost and the agent lessons)*

### The current lineup (all `[VERIFY]` — post-Jan-2026 cutoff; confirmed live on docs 2026-06-06)
(source: https://platform.claude.com/docs/en/about-claude/models/overview)

| | **Opus 4.8** | **Sonnet 4.6** | **Haiku 4.5** |
|---|---|---|---|
| Positioning (verbatim) | "most capable model for complex reasoning and agentic coding" | "best combination of speed and intelligence" | "fastest model with near-frontier intelligence" |
| API ID | `claude-opus-4-8` | `claude-sonnet-4-6` | `claude-haiku-4-5` |
| Price (input/output per MTok) | $5 / $25 | $3 / $15 | $1 / $5 |
| Comparative latency | Moderate | Fast | Fastest |
| Context window | 1M tokens | 1M tokens | 200k tokens |
| Max output | 128k | 64k | 64k |
| Extended thinking | No | Yes | Yes |
| Adaptive thinking | Yes | Yes | No |

Note the inverted pattern worth teaching: Opus 4.8 dropped to **$5/$25** (cheaper input than legacy Opus 4.1's $15/$75), narrowing the historical cost gap. `[VERIFY pricing]`

### The tradeoff axis
The three tiers trade **capability ↔ speed ↔ cost**: Opus = max capability, moderate latency, highest price; Sonnet = balance; Haiku = fastest + cheapest with "near-frontier" capability. The `effort` parameter is an *orthogonal* lever within a model — it trades "Claude's intelligence vs. token spend, trading off capability for faster speed and lower costs" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Architect point: tune cost/quality on *two* dials — model tier AND effort level.

### Decision framework
**Anthropic's official default (verbatim):** "If you're unsure which model to use, consider starting with **Claude Opus 4.8** for the most complex tasks. It is Anthropic's most capable model for complex reasoning, long-horizon agentic coding, and high-autonomy work." (source: https://platform.claude.com/docs/en/about-claude/models/overview).

**The "descend from capable" strategy (verbatim, secondary):** "Teams should start with Sonnet as the default, measure actual quality and cost against their specific tasks, and then specialize by routing simpler tasks down to Haiku and only the most demanding tasks up to Opus." (source: https://www.sitepoint.com/claude-model-selection-framework/, SECONDARY). Reconcile: **start with a capable model to establish a quality ceiling, get it working, then optimize *down* to the cheapest model that still passes your evals** — escalate to Opus only for the hardest, longest-horizon work. Matches the overview's note that "latency and cost can be sometimes more easily improved by selecting a different model" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview).

**When to choose Opus over Sonnet (verbatim):** "For the hardest, longest-horizon problems (large-scale code migrations, deep research, extended autonomous work), Opus 4.8 remains the right choice. Sonnet 4.6 is optimized for workloads where fast turnaround and cost efficiency matter most." (source: https://platform.claude.com/docs/en/about-claude/models/migration-guide).

### "Prompt is portable, but re-test on a new model"
Migration guidance repeatedly says new models have "strong out-of-the-box performance on existing… prompts and evals" — prompts *are* broadly portable — **but** every migration section lists behavioral shifts to re-check: verbosity calibration, literal instruction-following, effort recalibration, tone/voice changes, prefill removal (source: https://platform.claude.com/docs/en/about-claude/models/migration-guide; best-practices). Verbatim: "As with any new model, prose style on long-form writing may shift… If your product relies on a specific voice, re-evaluate style prompts against the new baseline." **Architect rule (reasoning grounded in those quotes): a prompt is portable as a starting point, but you MUST re-run your evals on the new model before trusting it in production.**

### Connection to the agent lessons (C-E4 cost + orchestration)
The cost matrix motivates the standard agentic cost pattern: **a smarter, more expensive orchestrator (Opus/Sonnet) directing cheaper workers (Haiku) on bounded subtasks.** Docs support delegating to specialized subagents that "require isolated context… or involve independent workstreams" while doing simple/sequential work directly (source: best-practices). Pair with prompt caching (Opus 4.8 cacheable minimum dropped to 1,024) and the Batch API for further cost control (source: migration guide). The C-E4 cost lever made concrete: route by difficulty, cache the static system prompt, batch the non-interactive work.

---

## Section G — Putting it together / anti-patterns
*(reinforces Domain 3; the empirical loop ties back to Section A)*

**Combine techniques (the integrated prompt):** a strong production prompt typically stacks: a **role** in the `system` field → **XML-structured** sections (`<instructions>`, `<context>`, `<documents>`, `<examples>`) → **3–5 diverse examples** in `<example>` tags → **long docs at the top, query at the end** → **grounding-in-quotes** for long context → **adaptive thinking + effort** for hard reasoning → **Structured Outputs** for a machine-parseable result → optional **prompt chaining** for self-correction (synthesized from best-practices).

**Anti-patterns (each grounded):**
- **Vague instructions** — fails the golden rule; "If they'd be confused, Claude will be too" (source: best-practices).
- **No examples** — skipping the single highest-leverage lever (source: best-practices).
- **Negative-only instructions** — "Tell Claude what to do instead of what not to do"; positive examples beat "what not to do" lists (source: best-practices).
- **Hiding the thinking** — use `<thinking>`/`<answer>` to keep reasoning inspectable; over-thinking is the opposite failure, fixed by lowering `effort` (source: best-practices).
- **Over-prompting / shouting (verbatim):** "Where you might have said 'CRITICAL: You MUST use this tool when…', you can use more normal prompting like 'Use this tool when…'." Aggressive language on current models causes **overtriggering**. Also "Remove over-prompting. Tools that undertriggered in previous models are likely to trigger appropriately now." (source: best-practices).
- **Relying on prefill** — broken on 4.6+; migrate to Structured Outputs / direct instructions (source: best-practices).
- **Assuming the prompt transfers blindly to a new model** — re-baseline verbosity, effort, tone (source: migration guide).
- **Manual `budget_tokens` thinking on new models** — removed on Opus 4.7+; use adaptive + effort (source: migration guide).

**The empirical loop (close the lesson):** define success criteria → build evals → draft prompt → climb the ladder only as far as evals require → if cost/latency is the blocker, change model or lower effort rather than over-prompting → re-run evals on any model change. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview).

---

## [VERIFY] list — version-sensitive / uncertain facts in one place
1. **Model lineup, IDs, pricing, context windows** — Opus 4.8 ($5/$25, 1M ctx, 128k out, no extended thinking, adaptive yes), Sonnet 4.6 ($3/$15, 1M ctx, 64k out), Haiku 4.5 ($1/$5, 200k ctx, 64k out). Post-Jan-2026 cutoff; confirmed live 2026-06-06 but will rotate. (models overview)
2. **"Choosing a model" default = start with Opus 4.8** — verbatim now, but the recommended default rotates each generation. (models overview)
3. **Prefill removed on Claude 4.6+ models** (400 on last assistant turn) — major break from classic Claude-101 prefill teaching. (best-practices)
4. **Classic prefill constraints** ("can't end with trailing whitespace"; incompatible with extended thinking) — from PRIOR docs, NOT re-confirmed in the consolidated page. Verify against legacy/archived prefill page.
5. **Manual extended thinking (`budget_tokens`) removed on Opus 4.7+** / deprecated on Sonnet 4.6 & Opus 4.6 — replaced by adaptive thinking + `effort`. (migration guide)
6. **"3–5 examples for best results"** — exact count version-sensitive. (best-practices)
7. **Long-context "20k+ tokens" threshold** and the **"up to 30%" queries-at-end** figure. (best-practices)
8. **Structured Outputs model-support list and schema limits** (20 strict tools, 24 optional params, 16 union types, 24h grammar cache). (Structured Outputs)
9. **Word-"think" sensitivity is Opus-4.5-specific** when thinking is disabled. (best-practices)
10. **`effort` levels and defaults** (Opus 4.8 defaults to `high`; `xhigh` recommended for coding; recalibrated vs 4.7) — model-specific, changes per generation. (best-practices, migration guide)
11. **The classic "ladder" ordering and its "cheap-first" rationale** — ordering corroborated by a secondary source + the interactive tutorial, but the one-line "try cheapest/highest-leverage first" rationale is pedagogical framing, NOT a verbatim Anthropic quote.

## Re-verification addendum — 2026-06-09 sweep (additive drifts, not reversals)
*(from `QA-VERIFY-SWEEP_2026-06-09.md`; all core lesson facts — prefill removal on 4.6+, `budget_tokens` removal on Opus 4.7+, lineup/pricing, Structured Outputs limits — CONFIRMED current)*

- **[VERIFY] #8 update — Structured Outputs support list now also includes Claude Mythos Preview** (in addition to Opus 4.8/4.7/4.6/4.5, Sonnet 4.6/4.5, Haiku 4.5).
- **[VERIFY] #10 update — Sonnet 4.6 now defaults to `high` effort** (a change vs Sonnet 4.5). Opus 4.8 `high` default unchanged.
- **Haiku 4.5 pinned snapshot ID:** `claude-haiku-4-5-20251001` is the documented dated snapshot form.
- **Opus 4.8 does NOT support extended thinking** (adaptive thinking only — consistent with the Section F lineup table). Routing note: extended-thinking workloads go to Sonnet 4.6.

---

**Sources:** [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview), [Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide), [Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial), [aiwithgrant guide (secondary)](https://www.aiwithgrant.com/guides/anthropic-prompt-engineering-overview), [SitePoint model selection (secondary)](https://www.sitepoint.com/claude-model-selection-framework/)
