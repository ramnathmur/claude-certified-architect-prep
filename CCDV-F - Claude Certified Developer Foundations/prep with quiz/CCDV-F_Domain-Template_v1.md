# CCDV-F Domain Corpus — File Template

Copy this shape for every `CCDV-F_Domain-N_v1.md`. It reproduces the structure of the CCAR-F `_v2`
files, which is the only structure this project has evidence for: fourteen mock papers were generated
from files in this shape and produced a first-attempt pass at 851.

**The rule it enforces:** a domain file states decisions, not explanations. Every section must be
answerable as "given this situation, do X, not Y." A section that only explains a concept cannot
generate a question, and cannot catch a misconception.

---

## What the official guide tells us about item shape

Read this before writing a single section. It is the difference between a corpus that trains for this
exam and one that trains for a different one.

The guide's three sample items — chosen to show "the style and cognitive level of the exam" — are all
the same shape: **a short scenario stating a constraint, then four options, none of them code.**

> *"A developer must process 10,000 documents overnight to produce a non-urgent analytics report. Cost
> is the primary concern, and results are not needed until the following morning. Which approach best
> fits the requirement?"*

The correct answer is the Message Batches API. The wrong answers are parallel synchronous calls,
lowering `max_tokens`, and downsizing the model. **Every option is a legitimate technique.** What
decides it is the stated constraint — latency-tolerant, cost-primary — and whether you match the
technique to it.

That is the whole exam in one item. Sections should be written to produce exactly that.

**So: state the decision and its discriminator.** Code appears in a section only where the decision is
*about* the code — schema design, defensive parsing, error-handling strategy — and even there the
question is which approach, never what the parameter is called.

---

## Template

````markdown
# Domain N — <Official domain name>

**Weight:** X% (source: official exam guide v1.0, July 2026)
**Skills covered:** <the published skills this file serves, with their individual weights>

## N.M <Published skill name> (X.X%)

*Section numbering follows the guide's own skill order and is permanent.*

### Core Facts

| Attribute | Value |
|---|---|
| ... | ... |

### <Decision axis> — <Option A> vs <Option B>

State the discriminator in one line, before the table. The discriminator is the thing the exam
actually tests; the table is only there to apply it.

| Situation | Answer | Why |
|---|---|---|
| ... | ... | ... |

### Exam scenario: <a constraint-bearing situation, one or two lines>
- ✅ <the correct approach, stated as an action>
- ❌ <a legitimate technique that does not match the stated constraint>
- ❌ <a wrong option from a different distractor family>

### ❌ Misconception
"<the wrong belief, written as someone would actually hold it>" — <the correction, one sentence>
````

---

## Rules for writing sections

1. **One decision per section.** If a section contains two independent decisions, split it into
   sub-sections. Misses are logged by section, and a section covering two things cannot tell you which
   one failed.
2. **Name the discriminator explicitly.** The CCAR-F misses were overwhelmingly *wrong-axis* errors —
   applying "severity" where the real axis was "do the issues interact". Sections that state their axis
   in one line prevent this; sections that only describe both options do not.
3. **Every stem carries a constraint.** All three official samples do: *cost is the primary concern* ·
   *hidden text in user-submitted content* · *reusable across several applications and maintained
   independently*. A stem with no constraint has no correct answer, only a preferred one.
4. **Write both directions of every decision.** On CCAR-F the `tool_choice` trap closed in the
   under-specification direction and immediately reopened in the over-specification direction, because
   only one direction had ever been drilled. Every decision table needs a row where the *other* option
   wins.
5. **Misconceptions are quoted, not paraphrased.** "Built-in tools can reach any internal REST API" is
   a usable misconception — it is the guide's own Sample 3 distractor D. "Confusion about tools" is not.
6. **Cite nothing external inside the file.** Corpus files are self-contained. Provenance belongs in
   `CCDV-F_Corpus-Index_v1.md`.
7. **Numbering is permanent.** Sections follow the guide's published skill order, so `2.5` is Claude
   Application Design forever.

---

## Distractor families

Six carried from CCAR-F, where each one caught Ram at least once:

- **OVERSPEC** — a stronger guarantee than the requirement asks for
- **DISCARD** — replace a working mechanism instead of adjusting it narrowly
- **REPAIR** — fix downstream what a constraint could have prevented upstream
- **ARCHITECTED** — the option that sounds more professional or more thorough
- **HALF-MOVE** — a partial version of the right answer
- **WRONG-AXIS** — right vocabulary, wrong discriminator

Four more, lifted directly from how the official sample rationales reject their wrong options:

- **IRRELEVANT-LEVER** — a real control that does nothing for this problem. *Raise the temperature so
  behaviour is harder to predict* against prompt injection
- **UNENFORCEABLE** — a request where a control is needed. *Add a line to the system prompt asking
  users not to include malicious instructions*
- **BIGGER-HAMMER** — scale or upgrade instead of solving. *Switch to a larger model that follows
  instructions more reliably* — which, as the guide notes, can make injection **worse**, not better
- **FALSE-CAPABILITY** — an option that assumes a capability the thing does not have. *Rely on a
  built-in tool, since built-in tools can reach any internal REST API*

Vary families within each item. Three flavours of the same wrong answer make an item that tests
nothing.

---

## Where code belongs, and where it does not

The exam is closed book, and Python/TypeScript proficiency is recommended experience. But the format is
multiple-choice and multiple-response — you select, you do not produce — and no official sample shows
code.

**Write code into a section when the decision is about the code:**

- Schema design — which shape survives a malformed response
- Defensive parsing and response validation
- Error handling and recovery strategy selection
- Streaming versus non-streaming, and what that changes downstream

**Do not write sections that drill syntax.** A section whose question is "what is this parameter
called" is preparing for an exam Anthropic does not appear to be setting. If a code snippet is needed
for context, show it — the candidate is selecting from options, not reproducing it.

> **If this turns out to be wrong**, the exam log will say so. Every miss is tagged `RECALL` or
> `CONCEPT`, and if `RECALL` misses exceed a quarter of all misses across three consecutive papers,
> this section gets rewritten and the corpus grows recall drills. See `../ROADMAP.md` Phase 4.

---

## Production-tier specifics

The credential validates building *production-grade* applications. Sections should carry, where
relevant:

- **The failure mode.** What breaks first under real traffic — rate limits, context overflow, timeouts,
  partial tool results
- **The cost dimension.** Token accounting, caching, batching. Which approach is affordable at volume
- **The security boundary.** Where untrusted input enters, and what stops it
- **The lifecycle question.** How this is versioned, deployed, monitored and rolled back — the guide
  gives Systems Life Cycle and Configuration Management their own weighted skills

A section that would sit unchanged in a getting-started tutorial is pitched a tier too low.
