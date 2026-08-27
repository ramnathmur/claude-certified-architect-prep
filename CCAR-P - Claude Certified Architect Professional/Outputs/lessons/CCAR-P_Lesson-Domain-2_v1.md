# Lesson — Domain 2: Claude Models, Prompting & Context Engineering

**Exam:** CCAR-P (Claude Certified Architect – Professional)
**Domain weight:** 13% (official exam guide v1.0, effective July 2026)
**Objectives covered (verbatim from the guide, §6):**

- Select appropriate Claude models based on trade-offs
- Design system prompts, templates, and guardrails
- Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)
- Optimize context windows and manage token usage
- Implement prompt reuse strategies (caching, modular prompts, Skills)

**Corpus this lesson teaches against:** `prep with quiz/CCAR-P_Domain-2_v1.md`, sections 2.1–2.9.

---

## 0. What this domain is actually about

Every other domain on this exam asks what to build. This one asks what to send.

An architect who has already chosen the pattern, drawn the boundaries, and picked the integration protocol still has to decide, for each call the system makes: which model receives it, what instructions frame it, what examples accompany it, what history rides along, and which parts of all that can be reused rather than rebuilt. Those five decisions are the five objectives, and they are not independent — each one moves the same three dials.

The three dials are **quality**, **latency**, and **cost**. Nearly every question in this domain is a disguised question about which dial the scenario says is binding.

That is the through-line. Read it once and it explains the whole domain:

| Objective | The lever it gives you | What it costs you if you pull it wrong |
|---|---|---|
| Model selection | Capability per call | Unpriced cost and latency at volume, or accuracy below the bar |
| System prompts & guardrails | Durable behavioral authority | Rules that exist somewhere but never reach the model |
| Prompt techniques | Targeted accuracy on a specific failure mode | Overhead on tasks that never had that failure mode |
| Context optimization | Tokens spent per call | Either an unaffordable conversation or a conversation that has forgotten something critical |
| Prompt reuse | The same work paid for once instead of *N* times | Duplicated tokens, drifting behavior across teams |

There is a second, quieter through-line, and it is the one the exam's distractors are built around. **Every technique in this domain is a targeted instrument, not a general improvement.** Few-shot examples fix inconsistency, not ignorance. Chain-of-thought fixes broken derivations, not missing facts. A bigger model fixes capability shortfalls, not attention position. Caching fixes repeated prefixes, not long prompts in general. The most common way to get a Domain 2 question wrong is to select a technique that is genuinely good, applied to a failure it cannot touch.

Two things about this exam's format remain genuinely unsettled and this lesson does not pretend otherwise. Whether the 63 items are standalone or grouped into shared-scenario blocks is not stated in the guide. Whether multiple-response items carry partial credit or are scored all-or-nothing is also not stated. Prepare as though every multiple-response item is all-or-nothing, because that is the safe assumption, not because it is a known fact.

---

## 1. Select appropriate Claude models based on trade-offs

### 1.1 The concept, from first principles

Model families ship in capability tiers. Higher tiers reason further across ambiguity, hold longer chains of inference together, and handle instructions that are underspecified. Lower tiers are faster and cheaper per call. This lesson names no specific model, size, or price, and neither should your reasoning — the tier names and their numbers change on a schedule you do not control, and an architect who has memorized a price list has memorized the one part of the job that expires.

What does not expire is the selection procedure.

A model choice is a purchase of *capability headroom*. Headroom that no requirement demands is cost you pay on every call, forever, for nothing. That framing is what makes "use the most capable model, to be safe" an incorrect answer rather than a conservative one: safety in an architecture is a property you can point to a requirement for. If nobody can name the requirement the headroom serves, it is not safety.

The problem this solves is real. A classification service running at production volume makes the same call millions of times. A per-call decision that looks trivially small — a few hundred milliseconds, a fraction of a cent — compounds into the dominant line item in the system's operating budget and the dominant term in its p95 latency. Meanwhile a legal-analysis workflow that runs eighty times a month has essentially no volume pressure at all; its binding constraint is whether the model can hold a multi-document argument together without dropping a clause.

So the selection procedure has four inputs, in this order:

1. **Task complexity.** How many inference steps, how much ambiguity, how much synthesis across sources? This sets the *floor* on capability.
2. **The accuracy bar, expressed as a number.** Not "high accuracy" — the specific threshold below which the downstream cost of an error exceeds the savings. This is the thing you benchmark against.
3. **Latency budget.** A hard gate. A model that cannot answer inside the budget is disqualified regardless of how accurate it is.
4. **Volume.** The multiplier that turns per-call differences into architectural ones.

And then one non-negotiable step: **benchmark candidate models on representative data before committing.** Not on a vendor benchmark, not on a hand-picked set of clean examples — on a sample of the actual traffic, including the messy tail.

### 1.2 Worked example

A support platform classifies inbound tickets into one of fourteen routing categories. Volume is 40,000 tickets per day. The routing decision is made synchronously while the customer waits on a confirmation screen, and the product team has set a p95 latency budget of 800 ms for the classification step.

The team benchmarks two candidates on a labeled sample of 2,000 real tickets drawn across a full week, including weekend traffic and the long tail of oddly-worded tickets:

| Candidate | Accuracy on sample | p95 latency | Relative cost per call |
|---|---|---|---|
| Lower tier | 94.1% | ~310 ms | 1× |
| Higher tier | 96.3% | ~1,900 ms | ~12× |

Two facts settle this before any cost analysis. The higher tier misses the 800 ms gate by more than double, which disqualifies it for the synchronous path outright. And the accuracy bar, derived separately, is 93%: below that, the volume of misroutes overwhelms the tier-2 queue that catches them. The lower tier clears the bar.

Now change one number and watch the answer move. Suppose the accuracy bar is 95.5% instead, because a misroute in this system means a compliance-sensitive ticket sits in the wrong queue for a day. The lower tier no longer clears it. The higher tier does, but still fails the latency gate — so neither candidate is simply "the answer," and the design has to change: classify asynchronously and show an optimistic routing state, or run the lower tier first and escalate only the low-confidence minority to the higher tier.

That escalation design is worth understanding as engineering even though it rarely appears as an exam option. Run the fast model on everything. If it emits a confident label, take it. If it does not, re-run on the higher tier. If 96% of tickets come back confident, you pay the expensive model on 4% of traffic — roughly 1,600 calls a day instead of 40,000 — and the p95 latency stays on the fast path, because only the escalated 4% sits above the 95th percentile.

Watch that last clause, because it is a constraint rather than a rounding detail. The escalated fraction has to stay below the percentile the SLA names. Escalate 12% instead and the 95th percentile is itself an escalated call, so p95 becomes fast path plus slow path — around 2.2s here — and the 800ms gate the design existed to clear is missed by a factor of nearly three. The reason this is worth knowing is that it makes the underlying arithmetic visible: model selection is not a single choice per system, it is a choice per call path, and a system can hold several.

### 1.3 How the exam probes it

The scenario gives you a task, a volume, and at least one explicit constraint — a latency SLA, a per-unit cost target, an accuracy threshold, or a stakeholder's stated preference. Then it asks which model to select, or asks you to critique a selection someone has already made.

The tell is that the scenario spends a sentence establishing volume or latency and then offers an option that ignores it. Options in this domain are written so that the wrong ones are *defensible in the abstract* and *wrong against the stated requirement*. Your job is to argue from the requirement the scenario states, not from general good practice.

Expect the stakeholder-pressure variant too, since Domain 6 exists on the same exam: someone senior asks for the biggest model "to be safe," with no complexity driver named. The correct move is to ask what specifically requires it, because headroom bought without a requirement is unpriced cost.

### 1.4 The wrong turns and why they are tempting

**"Default to the most capable model available, to be safe."** Tempting because it sounds thorough and risk-averse, and because in a design review nobody ever got criticized for over-provisioning. It is wrong when the task is bounded, high-volume, and latency-gated, because nothing about that task shape calls for extra reasoning capability and the extra cost and latency compound on every one of the millions of calls. This is the *architected* distractor — it wins on vibes and loses on requirements.

**"Fine-tune a smaller model."** Tempting because it is a real, sophisticated lever and it sounds like the answer an expert would give. It is wrong as a *first* move, because you have not yet tested whether a base model clears the bar. Fine-tuning is the expensive answer to a question base-model evaluation might have already closed. This is the *half-move*: a legitimate technique deployed one step too early.

**Choosing on a published benchmark instead of your own data.** Tempting because the benchmark is right there and running your own evaluation takes a week. It fails because your accuracy bar is defined over *your* distribution, including the awkward tail your users actually produce.

**Treating the model choice as permanent.** Model selection is revisited when the task changes, when volume changes by an order of magnitude, or when a new tier ships. An architecture that hard-codes a model identifier in forty places has made that revisit expensive, which is a Domain 1 sin committed in Domain 2 territory.

### 1.5 Takeaways

- Match capability to what the task's complexity demands **at its actual operating volume** — never to the model's ceiling.
- Latency budgets are gates, not preferences. A model that misses the gate is out before accuracy is discussed.
- Write the accuracy bar as a number derived from the downstream cost of an error, then benchmark candidates against representative data.
- "Biggest model to be safe" with no stated complexity driver is unpriced cost. Push back and ask what requires it.
- Fine-tuning is legitimate but is not the first move; base-model evaluation comes first.

---

## 2. Design system prompts, templates, and guardrails

### 2.1 The concept, from first principles

The system prompt is the only place in a request with durable authority over the whole conversation. Everything else — the first user message, a note in a design doc, an environment variable, a comment in the code that assembles the request — either loses force as the conversation moves on or never reaches the model at all.

That last category deserves a beat, because it is the failure architects actually commit. A rule set as an environment variable at deploy time has no path to the model's behavior. The model sees the bytes in the request. A rule that is not in those bytes does not exist, however carefully it was written down.

Three artifacts live in this objective and they are commonly conflated:

**The system prompt** carries persistent behavioral constraints: persona, tone, response format, scope boundaries, refusal conditions, escalation triggers. It is the constitution.

**The template** is the structure that assembles a request. It separates the stable skeleton from the per-request variable slots. A template exists so that a thousand requests share one authored artifact rather than a thousand string concatenations, and — as §5 will show — so that the stable portion sits in a fixed position where it can be cached.

**Guardrails** are the constraints that define what the system will refuse, escalate, or route to a human. They are a design decision made when the system prompt is written, not a monitoring feature bolted on after an incident.

That last distinction carries real architectural weight, and it is where Domain 2 hands off to Domain 5. A guardrail expressed in a system prompt is a **strong default**, not an enforcement boundary. It shapes behavior reliably in the overwhelming majority of cases and it can be argued with. Anything that must *never* happen — a refund above a threshold, a write to a production table, disclosure of a record the requester is not entitled to — needs enforcement outside the model: a tool that is not exposed at all, a code-level check on the tool's arguments, an approval hook. The architect's version of this objective is knowing which layer each constraint belongs in.

A useful way to hold it:

| Constraint type | Where it belongs | Why |
|---|---|---|
| Tone, persona, response format | System prompt | Needs authority across every turn |
| Scope boundary ("only answer questions about X") | System prompt | Behavioral, and the model needs it to decline gracefully |
| Refusal boundary / escalation trigger | System prompt, plus a structural signal where possible | Guardrails are designed in, not observed after the fact |
| "This action must never occur" | Do not expose the capability; enforce in code | A prompt instruction is persuadable; an absent tool is not |
| Per-request variable data | Template slot, positioned last | Keeps the stable prefix stable |

### 2.2 Worked example

A claims assistant must: speak in a specific institutional register; never quote a settlement figure; ask a clarifying question when the policy number is missing rather than guessing; and escalate to a human whenever the claim value exceeds a threshold or the customer explicitly asks for one.

A weak implementation puts the register in the system prompt, the settlement rule in a paragraph of the first user message, and the escalation threshold in a config file that the deployment pipeline reads. Two of those four rules do not reach the model. The settlement rule reaches it once, in turn one, and its authority decays as thirty turns of assistant output accumulate above it.

The sound implementation looks like this. Register, settlement prohibition, clarifying-question rule, and escalation triggers all live in the system prompt, stated as concrete testable conditions rather than as aspirations — "when `policy_number` is absent from the retrieved case record, ask for it before proceeding" beats "be careful about missing information." The escalation threshold *also* exists as a code-level check on the arguments passed to the settlement tool, so that a model that talks itself past the instruction still cannot execute the action. The customer's message and the retrieved case record occupy template slots at the end.

Note what the second layer bought: the prompt makes the right behavior the default and explains it to the user coherently; the code makes the wrong behavior impossible. Neither layer does the other's job.

### 2.3 How the exam probes it

The classic shape is a placement question. A behavioral rule is described and you choose where it belongs. The correct answer is the system prompt; the distractors are the first user message, an environment variable, the first assistant message, or a document nobody sends to the model.

A second shape is a drift scenario: an assistant honors its persona early and stops honoring it by turn ten or twelve, in a conversation nowhere near any capacity limit. The root cause is that accumulated assistant output dilutes the system prompt's relative influence, and the fixes are structural — replace verbose abstract rules with a small number of concrete examples that demonstrate the behavior, and reinforce at conversation breakpoints. Reaching for a bigger context window here is a category error, since the conversation was never close to full.

A third shape is a guardrail-layering question, where the scenario describes something that must never happen and the options offer a prompt instruction, a log, a confirmation step, and a removal of the capability. The exam guide's own recurring logic for the least-privilege family is that removing an unneeded capability beats logging or confirming its use.

### 2.4 The wrong turns and why they are tempting

**Putting the rule in the first user message.** The instinct is right — state the rule — and the location is wrong. It has authority for one turn and then competes with everything that follows.

**Setting it as an environment variable.** This confuses infrastructure configuration with a model-facing instruction. It is tempting because deployment config is where operational settings normally live, and because the rule *feels* configured once it appears in a settings file. It reaches the model only if something explicitly renders it into the request.

**Writing the rule abstractly.** "Rate severity appropriately" and "check that the output is accurate" are unfalsifiable, and models drift on unfalsifiable instructions faster than on concrete ones. Replace intent with a testable criterion.

**Treating a prompt guardrail as an enforcement boundary.** Tempting because the prompt instruction is genuinely effective and testing it will show it working. It fails on the adversarial tail and on the long-conversation tail, which is exactly where the consequences live.

### 2.5 Takeaways

- The system prompt is the only location with durable authority across every turn; that is the whole reason it exists.
- A rule that does not reach the model as request bytes does not exist. Environment variables and design docs are invisible to it.
- Guardrails are designed at system-prompt time, and anything that must never happen gets a second, non-persuadable layer in code or tool exposure.
- State rules as concrete testable conditions; abstract rules drift first and fastest.
- Behavioral drift in a short conversation is dilution by accumulated assistant output, not a capacity problem.

---

## 3. Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)

### 3.1 The concept, from first principles

Three techniques, three distinct failure modes. The skill this objective tests is diagnostic: read the symptom, name the failure mode, then pick the instrument built for it.

**Zero-shot** is instruction only — you describe the task and the model performs it. It is the default and it is often sufficient. Zero-shot fails when the instruction, however carefully written, underdetermines the output: two readings of the same instruction both satisfy it, and the model alternates between them across calls.

**Few-shot** supplies demonstrations. Its mechanism is not "teaching the model the task" — the model already knows the task. Examples *pin down the specific choice the instruction left open*: exact output shape, exactly where a boundary between two categories falls, exactly which tool an ambiguous phrasing maps to. This is why the number of examples matters far less than their placement. Four examples sitting precisely on the ambiguous boundary resolve the ambiguity. Fifteen examples of obvious cases confirm what the model was already getting right and consume context doing it.

The rule of thumb from the corpus: **4–6 examples targeted at the ambiguous cases, not 10–15 easy ones.** For a pure format-consistency problem, 3–4 examples of the exact required format is usually enough. Where the ambiguity is a judgment call, give each example a stated rationale for the choice made — the rationale is what generalizes to the ambiguous case you did not think of.

**Chain-of-thought** asks the model to reason in steps before answering. Its mechanism is that it gives the model tokens in which to perform intermediate computation, so a multi-step derivation is worked rather than guessed. It helps on multi-step arithmetic, multi-stage analysis, comparison across many items, and stepwise transformation.

It does nothing for a single-step task, because there are no steps to work through. And it is not free: a reasoning cue lengthens the output, and output tokens are generated serially, so it adds latency to every call as well as cost. On a translation or a simple classification, that is pure overhead purchased with no return.

There is a fourth technique worth carrying from the Foundations material because it shows up as a distractor and as an answer: **prefilling**, where you supply the opening of the assistant's message so the model continues from it rather than starting fresh. Its canonical use is suppressing a stereotyped opening. It is a shape control, not a content control.

Here is the diagnostic mapping, which is the actual exam-relevant asset:

| Symptom | Failure mode | Instrument |
|---|---|---|
| Output shape varies across calls despite explicit instructions | Instruction underdetermines the form | Few-shot: 3–4 examples of the exact required format |
| Two categories/tools confused on ambiguous inputs | Boundary is undefined | Few-shot: 4–6 examples on the boundary, each with rationale |
| Multi-step derivation arrives at a wrong final number | No space to compute intermediates | Chain-of-thought cue |
| Model does not know a fact | Missing information | Retrieval — no prompting technique creates knowledge |
| Model opens every reply with the same filler phrase | Response shape | Prefill the opening |
| Model honors a rule early, forgets it by turn twelve | System-prompt dilution | Concrete examples over verbose rules; reinforce at breakpoints |

The fourth row is the one that separates architects from prompt tinkerers. A model that lacks a fact will not acquire it from more examples, a stricter instruction, or permission to think step by step. That failure belongs to Domain 3's retrieval design, and recognizing when a Domain 2 instrument cannot help is itself a Domain 2 competency.

### 3.2 Worked example

An agent has two tools: `get_customer`, which returns account-level information, and `lookup_order`, which returns order-level information. Requests phrased like "I need help with my recent purchase" are genuinely ambiguous — the user might want the order status or might want their account's return eligibility.

Suppose you try four fixes and score each on a 400-item labeled sample of ambiguous phrasings. Illustrative figures, but the shape is the point:

| Change | Routing accuracy on the ambiguous subset |
|---|---|
| Instruction only, tool descriptions clear | 71% |
| Instruction rewritten to be more explicit and detailed | 74% |
| Twelve few-shot examples of clear, unambiguous requests added | 72% |
| Five few-shot examples on the ambiguity, each with a one-line rationale | 93% |

The second row is the instructive one. Rewriting instructions gained three points, because the problem was never that the instruction was unclear — it was that the boundary genuinely sits between two reasonable readings and prose cannot place it as precisely as a demonstration can. The third row moved nothing while adding tokens to every call: the twelve examples described cases the agent already routed correctly.

Now the cost side of chain-of-thought, on the classification service from §1. Adding a "think step by step" cue to a single-step classification adds, say, 150 output tokens per call. At 40,000 calls a day that is six million additional output tokens daily, generated serially, pushing every call's latency up against an 800 ms gate that was already the binding constraint. Accuracy gain on a single-step task: none worth measuring. The technique is sound; the application is not.

### 3.3 How the exam probes it

The dominant shape is symptom-to-technique. The scenario describes a specific observed failure and the options offer several genuinely real techniques, only one of which addresses that failure. You are being tested on the diagnosis, not on knowing the techniques exist.

A second shape is the *proportion* question: given a technique is warranted, how much of it? Ten to fifteen broad examples versus four to six targeted ones is the canonical pair, and the targeted set wins because targeting is what fixes the failure — volume is not.

A third shape is the negative case: a single-step feature, and the question is whether to add a reasoning cue. The answer is no, and both distractors are attractive. "Add it for consistency with other features" sounds like disciplined engineering. "Add it if accuracy drops later" sounds appropriately measured. The first buys latency and cost on a task that gains nothing; the second is a reactive patch where matching technique to task shape up front was available.

### 3.4 The wrong turns and why they are tempting

**"Add more examples."** More examples reads as more effort and more thoroughness. If the added examples do not sit on the failure boundary, they are wasted context and the failure persists unchanged.

**"Refine the instructions further."** Tempting because it is nearly free and because writing clearer prose feels like the responsible first move. When instructions have already failed on a consistency problem, more prose is more of the thing that did not work; examples are the instrument built for that failure.

**"Chain-of-thought never hurts."** It hurts on every single-step call, measured in latency and output tokens, at whatever volume the system runs.

**Applying a technique uniformly across a system "for consistency."** Consistency across features is a real engineering value in code. Applied to prompt techniques it overrides the per-task diagnosis that this entire objective consists of.

### 3.5 Takeaways

- Diagnose the failure mode before selecting the technique; the technique is the easy half.
- Few-shot fixes inconsistency and undefined boundaries. Target 4–6 examples at the ambiguous cases with stated rationales; 3–4 suffice for a pure format problem.
- Chain-of-thought fixes multi-step derivations and adds pure overhead to single-step tasks.
- No prompting technique supplies a fact the model does not have — that is a retrieval problem.
- Prefilling controls the shape of a response opening, not its content.

---

## 4. Optimize context windows and manage token usage

This objective carries the most conceptual weight in the domain, so it gets the most room.

### 4.1 The stateless constraint, and what follows from it

The Claude API is stateless. Every call is independent and nothing on the server remembers the previous one. There is no session identifier that restores prior turns, and no server-side conversation store the model consults.

Everything a conversation appears to remember is therefore something the *application* re-sent. Continuity is constructed by the client on every single request: the full prior message history goes into the `messages` array, every time, or the model does not have it.

Two consequences follow directly, and both are examinable.

**Consequence one: apparent amnesia in a short conversation is an application bug.** If the model does not know something the user said two turns ago, and the conversation is three turns long, the cause is that the application did not include the prior messages. It is not a capacity limit — a three-turn conversation is nowhere near one — and it is not a missing parameter, because no such parameter exists.

**Consequence two: cost and latency grow quadratically in turn count.** This is the part that surprises people, so let us do the arithmetic.

Suppose each turn adds about 300 tokens to the transcript (user message plus assistant reply). Ignore the system prompt for a moment. On turn *N*, the request carries roughly 300 × (*N* − 1) tokens of history plus the new message. So:

| Turn | Input tokens sent on that turn | Cumulative input tokens sent so far |
|---|---|---|
| 5 | ~1,200 | ~3,000 |
| 10 | ~2,700 | ~13,500 |
| 25 | ~7,200 | ~90,000 |
| 50 | ~14,700 | ~367,500 |

Going from 10 turns to 50 — five times the turns — costs about **twenty-seven times** the cumulative input tokens. The per-turn figure grows linearly; the running total grows with the square of the turn count, because turn 50's history includes turn 10's history for the fortieth time.

Latency moves the same way, for a different reason. The model must process the entire input before it emits the first output token, so time-to-first-token scales with prompt length. Turn 50 feels slower than turn 5 even when both answers are two sentences long. A user's subjective experience of a long conversation degrading is often this, not a quality change.

So when a scenario says "latency and cost are rising as conversations pass fifty turns," the root cause is the full history being resent on every call. It is not the model writing longer replies, and it is not a database.

### 4.2 Lost in the middle

The second structural fact: attention across a long input is not uniform. Content at the **beginning** and at the **end** of a long input is processed reliably. Content in the **middle** is attended to less reliably, and the effect grows with input length.

The practical shape of the failure: a synthesis task over a long document set produces an output that reflects the opening summary and the closing conclusions accurately, while a critical finding sitting in the middle is simply absent. Nothing errors. The output looks complete and reads fluently, which is what makes this failure expensive — it is invisible without ground truth.

**The fix is structural, not dimensional.** Three moves, in order of leverage:

1. **Put a key-findings summary at the very start.** Move the content that must not be missed into the position that is reliably read. This is a positional fix and it is the highest-leverage one.
2. **Add explicit section headings throughout.** Headings give the model navigational structure in the region where unstructured prose loses it.
3. **Convert verbose prose into structured facts.** Where an upstream stage produces the input — a retrieval step, a subagent, a tool — have it return key facts, quotes, and citations rather than full page bodies and reasoning traces. This shrinks the middle and raises its information density at the same time.

Why the obvious fix is the wrong one deserves an explicit statement. Shortening the input to fit under some arbitrary token target means deciding what to cut, and the content most at risk of being cut is exactly the mid-document detail that was already being missed. Shortening trades an attention problem for a deletion problem and gets no signal about whether the trade helped.

Rotating which source appears first across runs fails differently and more subtly. It changes *who* occupies the penalized middle position without changing the fact that a penalized middle position exists. Every run still loses something; the losses are just harder to reproduce.

And the fourth wrong turn: moving to a model with a larger context window. A larger window changes how much fits, not how attention distributes across what is there. The attention pattern is a property of long inputs, not of window capacity.

### 4.3 The hybrid context strategy

Given a conversation that will outgrow any budget you set, something has to be compressed. The tested answer is that the compression must be **non-uniform**, because the information in a conversation is not uniform.

Three tiers:

1. **Extract precision-critical facts verbatim into a structured block.** Amounts, dates, identifiers, agreed terms, allergies, thresholds, account numbers. These go into a compact, explicitly formatted block that is included in every prompt and sits *outside* the summarized region. They are never paraphrased.
2. **Summarize low-density discussion.** Pleasantries, exploratory back-and-forth, the four turns spent narrowing a question. This is where compression actually pays, because the token-to-meaning ratio is poor.
3. **Keep recent turns verbatim.** The current exchange needs full fidelity for the model to respond coherently to what was just said.

The reason pure summarization fails is a precision failure with a specific signature. "The 15% discount I agreed to on the second call" becomes "promotional pricing was discussed." The summary is not wrong. It is unusable, and worse, it is *confidently* unusable — nothing downstream signals that a number was lost.

The reason a pure recency window fails is different: it drops early content wholesale. A fact stated in turn three of a sixty-turn conversation falls out of a last-twenty-turns window entirely, and in some domains that fact is the one that matters most. The corpus's example is a safety-critical allergy mentioned at the start of a long session.

A serviceable shape for the persistent block:

```
=== CASE FACTS (updated whenever a new fact appears) ===
Customer ID: CUST-12345
Order ID: ORD-67890
Order amount: $89.99
Agreed adjustment: 15% goodwill discount (agreed turn 12)
Issue: Item damaged on delivery
Status: Pending manager approval
===
```

Two properties make this work. It is **updated** as new facts appear, so it stays current rather than being a snapshot of turn one. And it is **positioned outside the summarizer's reach**, so no future compression pass can degrade it. Instructing the summarizer to "be sure to preserve numbers" is a weaker design, because it makes correctness depend on the summarizer performing perfectly every time rather than on the fact never entering the compressible region.

### 4.4 Adjacent token levers worth knowing

Two more levers belong to the same objective and appear in production far more often than they appear on a syllabus.

**Trim verbose tool results before they enter context.** A single lookup can return forty fields when five are relevant, and every one of those fields then rides along in every subsequent turn of the conversation. Filtering the result down to the relevant fields at the point it is produced conserves context and reduces noise. Instructing the model to "ignore the irrelevant fields" does not help, because the tokens are already spent and the attention cost is already paid.

**Isolate verbose exploration in a subagent.** When a phase of work produces a large volume of output that only matters in summary — scanning a large codebase, surveying many documents — running it in a subagent that returns a condensed result keeps the main conversation's context available for the work that actually needs it.

Both are the same principle applied at different points: decide what enters context on purpose, rather than letting everything a tool or a phase produces accumulate by default.

### 4.5 How the exam probes it

**Root-cause diagnosis** is the dominant shape. A symptom is described and you identify the cause. Short conversation plus apparent amnesia equals missing history in the request. Long conversation plus rising latency and cost equals full history resent every call. Long input plus specific mid-document content missing equals lost in the middle.

**Strategy selection** is the second shape: a long session with mixed content, and four context-management options. The hybrid wins; uniform summarization and recency-only lose for the reasons above.

Watch for the distractor that is offered as a fix for the wrong layer. A larger context window is offered against attention problems. A vector database is offered against a three-turn amnesia bug. A session parameter is offered against the stateless constraint. Each is a real thing (or, in the last case, a plausible-sounding invention) aimed at a problem it does not touch.

### 4.6 The wrong turns and why they are tempting

**"The context window was exceeded."** Tempting because it is the explanation people reach for whenever a model forgets something. Check the arithmetic first: if the conversation is short, capacity is not the cause and the answer is at the application layer.

**"Shorten the input."** Tempting because it is a direct response to "the input is too long," and length was mentioned. It risks deleting the exact content that was being missed.

**"Summarize everything uniformly."** Tempting because it is simple, symmetric, and easy to implement as a single pass. It degrades precision-critical facts into vagueness with no error signal.

**"Keep the most recent N tokens."** Tempting because it bounds memory usage with one parameter and preserves perfect fidelity in the region the user is currently looking at. It silently drops early facts.

**"Instruct the summarizer to preserve important details."** Tempting because it is a one-line change. It makes correctness contingent on a model performing reliably at exactly the task it was observed to be unreliable at.

### 4.7 Takeaways

- The API is stateless. Every request carries the full history, and all continuity is the application's construction.
- Cumulative token cost grows with the square of the turn count; per-turn latency grows with prompt length.
- Apparent amnesia in a short conversation is a missing-history bug, never a capacity limit.
- Attention is reliable at the start and end of a long input and degraded in the middle; the fix is position and structure, not length.
- A larger context window does not repair the attention pattern.
- Hybrid context management: extract precision-critical facts verbatim into a persistent block, summarize low-density discussion, keep recent turns intact.
- Keep the facts block outside the summarized region rather than asking the summarizer to be careful.

---

## 5. Implement prompt reuse strategies (caching, modular prompts, Skills)

### 5.1 Prompt caching, from first principles

Prompt caching reuses a **stable input prefix** across requests. It does not store outputs, and understanding that one word — *prefix* — explains every rule that follows.

The mechanism: when a request arrives, the system checks whether the leading portion of the input matches a previously processed prefix. If it does, the processing already done for that portion is reused rather than recomputed. The match is on the prefix, in order, from the first byte.

Three properties fall straight out of that.

**Order matters absolutely.** The cacheable region is a prefix, so it must come first. Static content — system prompt, policy text, tool definitions, stable few-shot examples — goes at the front. Variable content — the user's message, retrieved documents, timestamps — goes at the back.

**Byte-identity matters.** A prefix that differs by one character is a different prefix. A session identifier, a request UUID, or a "current time" line injected at the top of the system prompt invalidates the cache on every single call while looking, in the code, like an innocuous logging nicety.

**Invalidation cascades forward.** Change something at position 100 and everything after position 100 is a new prefix, no matter how much of it is unchanged. This is why the ordering of the *static* content among itself matters too: put the most stable material first and the least stable static material last within the cached region.

There is an economics wrinkle worth internalizing without memorizing any number. Writing a prefix into the cache carries a premium over ordinary input processing; reading from it carries a discount. So caching pays once the prefix is reused enough times to amortize the write, and cache entries do not live forever — a low-traffic endpoint may pay the write repeatedly and read rarely. Treat the specific multipliers and lifetimes as a documentation lookup, not a memorized fact; treat the break-even *reasoning* as the thing you own.

### 5.2 Worked example

This is the shape of the official guide's own sample question in this domain, so it is worth walking through carefully.

An application sends an identical large preamble on every request: a compliance policy, a set of tool definitions, and a stable block of few-shot examples. Call it 8,000 tokens. The user's message averages 200 tokens. Both latency and cost are named as concerns.

Without caching, every request processes 8,200 input tokens from scratch. The user's 200 tokens are 2.4% of the work; the other 97.6% is the same computation performed again.

With the static preamble ordered first and caching enabled, the 8,000-token prefix is reused. Per request, roughly 200 tokens of genuinely new input are processed. Time-to-first-token drops because prefill over the cached region is skipped, and input cost drops because the reused portion bills at the read rate. Latency and cost move together, which is precisely why "both latency and cost are concerns" is the phrase that flags this answer.

Now the anti-patterns, each of which is a real bug people ship:

- The template renders `Request ID: 7f3a...` as the first line of the system prompt. The prefix differs on every call; the hit rate is zero; the metric that would reveal this is one nobody is watching.
- Retrieved documents are placed *before* the policy text, because the assembly code appends them in retrieval order. The policy is no longer a prefix, so the largest stable block in the request is uncacheable.
- Someone "optimizes" by truncating the policy to cut tokens. The token count falls and required policy content is now missing — a correctness regression sold as an efficiency win.
- Someone adds a preliminary call asking the model to summarize the preamble at request time. This adds an entire round trip, adds its own latency, and risks compressing policy language that needed to be exact — to solve a problem caching solves without any of that.

### 5.3 Modular prompts and Skills

Caching is reuse *within* a system. Modular prompts and Skills are reuse *across* systems and teams, and the failure they address is organizational rather than computational.

The failure pattern: four teams each maintain their own copy of a system prompt that started as one prompt. Someone edits one copy to fix a tone problem. Nine months later the four copies disagree about escalation thresholds, refusal language, and output format, nobody can say which is authoritative, and a behavior change now requires four uncoordinated edits that will land at four different times. Copy-paste reuse is reuse that decays from the moment it is created.

The architectural answer is a **versioned, shared, reviewable component**: prompt fragments and Skills held in version control, referenced rather than duplicated, and changed through a review process. The property that matters is that a behavior change becomes one reviewable event with a diff and an author, instead of *N* silent drifts.

Skills extend this from prompt text to packaged capability — instructions plus supporting resources, versioned as a unit and loaded when relevant rather than pasted into every prompt. That loading-when-relevant property connects to Domain 3's progressive-discovery objective and to the caching discipline above: a monolithic prompt that carries every capability's instructions all the time is both a token cost and, if it changes as capabilities are added, a caching liability.

Modularity also has a caching payoff worth making explicit. Splitting a prompt into a stable core and a volatile periphery is the same operation as splitting it into a cacheable prefix and an uncacheable tail. Design the modules along the stability seam and you get both benefits from one decision.

### 5.4 How the exam probes it

The caching shape is highly recognizable: identical large content sent repeatedly, and both latency and cost named as concerns. Order static content first and enable prompt caching. The exam guide's own recurring answer logic states this pairing explicitly, so treat the co-occurrence of "identical preamble" and "latency and cost" as a strong signal.

The reuse shape is a team or partner adopting your setup, or several teams having drifted apart. The answer is version-controlled shared prompts and Skills with an onboarding path people actually follow. The distractors are knowledge-transfer mechanisms that do not stay current: a recorded walkthrough transfers understanding once and then ages, and a shared chat channel is reactive support rather than a durable artifact.

### 5.5 The wrong turns and why they are tempting

**"Caching means storing the response."** The intuition comes from HTTP and application caching, where caching responses is exactly what you do. Prompt caching reuses the input prefix. If you carry the response-caching intuition in, you will conclude that caching only helps on repeated identical *questions*, and miss that it helps on every request that shares a preamble regardless of what the user asked.

**"Truncate the static content."** Tempting because it targets the visible number — token count — and produces an immediate reduction. It removes required content instead of reusing it.

**"Split the request in two."** Tempting because it sounds like a load-management move. It relocates the same token cost and does not engage caching at all.

**"Move the static content into a few-shot block."** Tempting because few-shot is a legitimate technique and the reorganization feels like it is doing something. Where the content sits in a *structure* is not what makes it cacheable; where it sits in the *ordering* is.

**"Each team keeps its own copy, for flexibility."** Tempting because it is genuinely faster in the first month and because flexibility is a real value. It guarantees silent divergence with no single source of truth, and the divergence is discovered by an incident rather than by a diff.

### 5.6 Takeaways

- Prompt caching reuses a stable, byte-identical input *prefix* — never the output.
- Order static content first and variable content last; that ordering is what makes caching possible.
- A dynamic value at the top of the prompt (timestamp, request ID) silently defeats caching on every call.
- Truncating or summarizing the static content is a correctness regression dressed as an optimization.
- Caching cuts latency and cost together, which is why "both latency and cost matter" is the flag for it.
- Team-scale reuse means versioned, shared, reviewable prompt components and Skills — a copied prompt drifts the moment either side edits it.

---

## 6. Synthesis: the five objectives in one production design

An insurer builds a policy-servicing assistant. It answers coverage questions, updates contact details, initiates claims, and escalates anything above a value threshold. It handles roughly 12,000 conversations a day, averaging fourteen turns. Compliance requires that a standing policy text be present on every model call. Here is how all five objectives land in one architecture.

**Model selection** is decided per call path, not once for the system. The intent-classification step at the front of each turn is bounded, high-volume, and sits in front of a user waiting on a screen, so it takes the lowest tier that clears its benchmarked accuracy bar on real transcripts. The coverage-reasoning step, which reads policy language against a described situation and must hold several conditions together, takes a higher tier — its volume is a fraction of the classifier's and its task complexity is the binding constraint. Nobody buys headroom without naming the requirement it serves.

**System prompt and guardrails.** Register, refusal boundaries, the clarifying-question rule, and the escalation triggers live in the system prompt as concrete testable conditions. The value threshold for escalation also exists as a code-level check on the claim-initiation tool's arguments, because that one must never be argued past. Capabilities the assistant does not need are not exposed at all rather than exposed and monitored.

**Prompt techniques** are applied per observed failure. Zero-shot handles most turns. The classifier carries five few-shot examples sitting on the one boundary that measurement showed it confusing — "change my address" versus "change the address on an open claim" — each with a one-line rationale. The coverage-reasoning step carries a reasoning cue, because it genuinely derives across multiple conditions. The classifier does not, because it is single-step and the cue would cost latency on all 12,000 conversations a day for nothing.

**Context management** runs the hybrid strategy. A case-facts block holds policy number, claim ID, amounts, agreed adjustments, and current status, updated as facts appear and positioned outside the summarized region. Discussion from earlier in the session is summarized. The last several turns stay verbatim. Tool results are trimmed to relevant fields before entering context. When a long policy document is read into a call, a key-findings block goes at the top and section headings run throughout, because that document is exactly the shape that loses its middle.

**Prompt reuse** ties it together. The request template puts the compliance policy, tool definitions, and stable few-shot examples first, in a fixed order, so they form a cacheable prefix — at fourteen turns per conversation and 12,000 conversations a day, that prefix would otherwise be reprocessed roughly 168,000 times daily. The case-facts block, summarized history, retrieved documents, and current user message follow, in ascending order of volatility. The compliance policy and the escalation rules are shared, versioned Skills that the claims team and the servicing team both reference rather than copy, so a regulatory wording change is one reviewed commit rather than two divergent edits.

Notice how often one decision served two objectives. Ordering the template by stability served both caching and modularity. Trimming tool results served both token cost and attention quality. Putting the guardrail in the system prompt *and* in code served both behavioral coherence and enforcement. That coupling is why this domain reads as five objectives and behaves as one.

---

## 7. Misconceptions

| Misconception | Correction |
|---|---|
| "The safest choice is always the largest model." | Model choice is a cost–latency–quality trade-off argued from the task's stated requirement. Oversized capability is unpriced cost, not safety. |
| "Pick the model once, for the whole system." | Selection is per call path. One system routinely runs different tiers on different steps. |
| "A published benchmark tells me which model to use." | The accuracy bar is defined over your traffic. Benchmark candidates on representative data including the messy tail. |
| "If it's documented anywhere in the pipeline, the model will follow it." | Only content that reaches the model as part of the request shapes behavior. Environment variables and design docs are invisible to it. |
| "A rule stated in the first user message is set for the conversation." | It has authority for that turn and decays as the conversation grows. Persistent constraints belong in the system prompt. |
| "A guardrail in the system prompt prevents the action." | It is a strong default, not an enforcement boundary. Anything that must never happen needs a non-persuadable layer in code or tool exposure. |
| "More examples always help." | Only examples targeted at the specific ambiguous cases fix the failure. Volume without targeting is wasted context. |
| "If the instructions aren't working, write clearer instructions." | When prose has already failed on a consistency problem, more prose repeats the failure. Examples are the instrument for that failure mode. |
| "Chain-of-thought never hurts, so add it everywhere." | It is a targeted tool for multi-step tasks. On single-step tasks it is pure latency and token overhead. |
| "A better prompt can fix a missing fact." | No prompting technique creates knowledge the model does not have. That is a retrieval problem. |
| "Claude has some memory across calls by default." | The API has none. All continuity is the application's responsibility to construct and resend on every request. |
| "Forgetting means the context window was exceeded." | In a short conversation, capacity is not the cause; the application is omitting prior messages from the request. |
| "Cost grows in proportion to conversation length." | Per-turn input grows linearly; cumulative input grows with the square of the turn count, because each turn resends all prior turns. |
| "The fix for 'lost in the middle' is a shorter prompt." | The fix is structural position and format. Shortening risks cutting exactly the content that was being missed. |
| "A bigger context window fixes attention problems." | A larger window changes how much fits, not how attention distributes across what is there. |
| "Rotating source order fixes the middle-of-input problem." | It changes who occupies the penalized position without removing the penalized position. |
| "Summarization is always safe as long as it's shorter." | Uniform summarization degrades precision-critical facts into vague paraphrase, with no error signal. |
| "Telling the summarizer to preserve numbers is enough." | That makes correctness depend on the summarizer being perfect. Keep critical facts outside the summarized region entirely. |
| "Keeping the most recent N tokens is a safe default." | It silently drops early facts, which in some domains are the ones that matter most. |
| "Caching means storing the response for reuse." | Prompt caching reuses a stable input *prefix*. It only works if that portion is byte-identical and ordered first, every time. |
| "Caching helps whenever the prompt is large." | It helps when a *prefix* is stable and reused. A large prompt that varies at the top caches nothing. |
| "Truncating the preamble is a cheaper version of caching." | It removes required content rather than reusing it — a correctness regression, not an optimization. |
| "Documentation of the prompt is enough; everyone can copy it once." | A copied prompt drifts the moment either side edits it. Durability requires one versioned source both sides reference. |

---

## 8. Quick reference

**Model selection**
Task complexity sets the capability floor · latency budget is a hard gate · accuracy bar is a number derived from the downstream cost of an error · volume is the multiplier · benchmark on representative data before committing · "biggest model to be safe" with no stated driver is unpriced cost · fine-tuning is not the first move.

**System prompts and guardrails**
System prompt = the only durable authority across turns · first user message decays · environment variables never reach the model · state rules as concrete testable conditions · guardrails are designed in, not monitored after · anything that must never happen gets enforced outside the model · drift in a short conversation is dilution by accumulated assistant output.

**Prompt techniques**
Diagnose first, then select · inconsistent form → 3–4 format examples · confused boundary → 4–6 targeted examples with rationales · broken multi-step derivation → reasoning cue · single-step task → no reasoning cue · missing fact → retrieval, not prompting · stereotyped opening → prefill.

**Context engineering**
Stateless API: full history resent every call · short-conversation amnesia = missing history, not capacity · cumulative tokens grow with the square of turn count · time-to-first-token scales with prompt length · lost in the middle: reliable at start and end, degraded in the middle · fix = key findings first + section headings + structured facts · not shorter, not rotated, not a bigger window · hybrid strategy = extract precision-critical facts verbatim + summarize low-density discussion + keep recent turns intact · facts block sits outside the summarized region · trim verbose tool results before they enter context.

**Prompt reuse**
Caching reuses a byte-identical input prefix, never the output · static first, variable last · any dynamic value at the top kills the hit rate · invalidation cascades forward from the first changed byte · cuts latency and cost together, which is the flag for it · modular prompts and Skills = versioned, shared, reviewable, referenced not copied · a behavior change should be one reviewable event, not *N* silent drifts.

**The one-line version of the domain**
Every technique here is a targeted instrument. Read the constraint the scenario states, name the failure mode, and pick the instrument built for that failure — not the one that sounds most thorough.
