# CCDV-F — Teaching Architecture (independent design)

Designed blind to any prior syllabus or class for this exam. Sources actually read are listed at the
end; every corpus claim below names the file it came from.

---

## 0. What the design has to satisfy

From `EXAM-FACTS_v1.md` §1, §5, §6:

- 53 items, 120 minutes. That is **2 minutes 16 seconds per item**, closed book.
- Multiple-choice and multiple-response; each item states how many to select. Assume all-or-nothing
  scoring on multiple-response.
- 720 of 1,000 to pass, criterion-referenced. **No domain floors** — a weak 2.6% domain cannot fail
  him on its own.
- All three published sample items are short scenarios with four options, no code, testing which
  approach fits a stated constraint. The distractor families are named: a plausible-but-irrelevant
  lever, a non-enforceable control, a bigger-hammer answer.
- Nothing in the 25 published skills requires recalling a parameter name.

From the student profile: experienced technology consultant and solution architect, reads code,
does not write production code daily, has passed a sibling Anthropic certification. He will study
this and nothing else.

The bar: he can answer a scenario the material never showed him, by reasoning from a mechanism the
material taught him.

Everything below follows from those five lines.

---

## 1. The unit of teaching

**The unit is a chapter built around one decision.**

Not a topic, not a skill, not a module screen. A decision: a question that a scenario can pose, that
has a defensible answer, and that a reader can be made able to answer for cases nobody has shown him.

Why that shape and not the alternatives:

- **Not one chapter per domain (8).** The domains are administrative buckets, not mechanisms. Domain
  2 alone bundles REST/JSON/async, Messages-API mechanics, CLAUDE.md configuration, cross-interface
  behaviour, requirements derivation and systems life cycle. Teaching those as one chapter is
  incoherent, and the student cannot retrieve from a bucket.
- **Not one chapter per skill (25).** Two problems. Some published skills are one decision (Claude
  Code Operation, 3.1%); some are four (Agent Patterns and Frameworks bundles tool-use loops,
  subagents, memory, context management and three named third-party frameworks). Forcing one chapter
  onto each produces chapters of wildly different density, which is exactly the "one repeated
  template" defect.
- **Not cases or scenarios as the primary unit.** Cases are how you *test* transfer, not how you
  build it. A course of 30 cases teaches 30 answers. The exam asks a 31st.

A decision-shaped chapter is retrievable under a two-minute clock because the retrieval cue is the
question, and the question is what the stem hands him.

**Count: 32 chapters in 7 parts.**

What governs the count, in order of precedence:

1. One chapter per decision the exam can pose independently of every other decision. That inventory,
   built from the 25 published skills and checked against what the corpus actually teaches, comes to
   32.
2. Ceiling: no chapter exceeds ~3,400 words — one sitting, one decision, one rule to carry away.
3. Floor: no published skill above 4% weight is discharged by less than one full chapter. That rule
   is what forced Claude Application Design (8.6%) into two chapters and Agent Construction (5.3%)
   into two.
4. The weight table in §3 is the arbiter. Chapter count is downstream of word budget, not the
   reverse.

---

## 2. The sequence

**Principle: dependency first; within what dependency allows, order by how much of the rest of the
course the mechanism unlocks; the student's own professional territory goes last.**

Three things that principle deliberately rejects:

- **Not weight order.** Domain 2 is 33.1% but cannot be taught first — "Claude Application Design"
  and "Software Engineering Foundations" both presuppose tokens, context and the tool loop.
- **Not the corpus's own order.** The four Academy modules run a prototype→production arc
  (`CCDV-F_Module-2_...md` line 42, "The build in this module"; same device in M3 line 43 and M4 line
  41). That arc is the corpus's spine, and following it reproduces the corpus's blind spots, which
  §6 shows are about a quarter of the exam.
- **Not difficulty order.** Difficulty is a property of the reader, not the material, and ordering by
  it front-loads the trivial.

The unlocking rule is why the context window goes first. Its own skill (LLM Fundamentals, 5.2%) is
not the heaviest, but it is a precondition for context engineering, caching, memory scope, subagent
handoffs, MCP loading cost and orchestrator-worker cost — six later chapters across four domains.

The last rule — his own territory last — matters more than it looks. Chapters 30–32 (requirements,
code review, life cycle) are where 20 years of consulting does most of the work. Placed last, he
reads them as translation: here is how the exam phrases the thing you already do. Placed first, they
read as condescension and burn his freshest reading hours on his strongest ground.

### The ordered list

**Part I — The substrate (5 chapters).** Everything downstream spends what these chapters describe.

| # | Chapter | One line |
|---|---|---|
| 1 | The one budget everything spends | Tokens as the unit of input, output and price; the context window as a single fixed pot holding system prompt, history, tool definitions, tool results and output; the two edge behaviours — rejected before generation, or truncated mid-generation. |
| 2 | Why the same prompt answers twice differently | Sampling from a distribution, what temperature does to that distribution, why newest models refuse sampling parameters, and why non-determinism forces you to assert on properties rather than text. |
| 3 | Two dials, not one | Model tier is one decision; how hard the model thinks is a separate per-call decision. Adaptive thinking, effort settings, and why behaviour changes across model releases break prompts that were tuned on the old one. |
| 4 | What is actually on the wire | REST underneath everything; JSON as the contract; what an SDK does for you and what it does not; the Anthropic SDK versus the Agent SDK. |
| 5 | Who is waiting? | Synchronous, streaming, async/await, websockets and batch — five request shapes, one question that picks between them. |

**Part II — Getting output your code can use (4 chapters).**

| # | Chapter | One line |
|---|---|---|
| 6 | Diagnosing a prompt by its failure | The failure type names the missing technique: wrong shape means a missing output constraint, drift means an underspecified system prompt, invented structure means missing examples. Plus system-versus-user placement, shot count, and input sanitisation. |
| 7 | When asking nicely stops working | Structured outputs and strict tool use move the guarantee from the prompt into the API; what they cost, and the two cases they still do not cover (refusal, truncation). Defensive parsing and checking `stop_reason`. |
| 8 | Keeping a long session inside the budget | Pruning, compaction, clearing, subagent handoff — four instruments, and the specific continuity each one destroys. |
| 9 | Paying once for what does not change | Prompt caching as a prefix contract; what invalidates it; what it cannot help; measuring context pressure before a request goes out. |

**Part III — Giving Claude hands (5 chapters).**

| # | Chapter | One line |
|---|---|---|
| 10 | The loop your code owns | Claude does not run tools; it asks. The six-step loop and the block-pairing contract that makes the API accept the next request. |
| 11 | Why Claude picked the wrong tool | Selection is driven by the description field. Exclusion conditions, required versus optional fields, overlapping parameter shapes, over-tooling, and when to merge two tools into one. |
| 12 | Streaming without corrupting state | A stream ending is not a message completing. Assembling events into blocks, committing a turn only after the message closes, and the retry bug that looks like a schema bug. |
| 13 | Four ways to hand Claude a capability | Built-in tool, custom tool, Skill, MCP server. Who owns the capability when it changes. |
| 14 | Build once, connect many | MCP servers exposing tools, resources and prompts; stdio versus HTTP; local, user, project and enterprise scope; per-tool permission rules; why the secret never goes in the config file. |

**Part IV — Agents (5 chapters).**

| # | Chapter | One line |
|---|---|---|
| 15 | Workflow or agent | The enumerate-the-steps test; the four workflow sub-patterns; orchestrator-worker and what its token multiple buys. |
| 16 | Who runs the loop | Raw Messages API loop, Agent SDK, Claude Managed Agents; self-hosted versus Anthropic-hosted; and where the third-party abstraction frameworks sit. |
| 17 | Building the loop by hand | Register, scope, iterate, exit. What breaks when each of the four is missing. |
| 18 | State that outlives a turn | In-context, external, summarised and stateless memory; subagent context isolation; and why carrying instructions is a different problem from carrying state. |
| 19 | Where the human stands | Three HITL insertion points chosen by worst-case outcome; hooks as the deterministic version of the same idea; deny over ask over allow. |

**Part V — The developer's surfaces (5 chapters).**

| # | Chapter | One line |
|---|---|---|
| 20 | Claude Code as a governed agent | Explore, plan, code; permission mode as a risk decision; deny rules that no mode can bypass; headless and streaming operation; repository initialisation. |
| 21 | Four places a durable instruction can live | CLAUDE.md and its dilution point, path-scoped rules files, hooks, subagents; plugins as the packaging layer; model pinning, prompt versioning, plugin dependencies. |
| 22 | The same model, five front doors | How Claude interprets instruction differently in Claude Code, Desktop, claude.ai, the API and the SDKs — what carries across and what does not. |
| 23 | Drawing the lines inside an application | Content boundaries between instruction, data and output; schema design for the application's own contracts; session hygiene; plugin management. |
| 24 | Sending Claude things that are not text | Images and their token arithmetic, PDFs, the Files API, and matching the API to the workload rather than looping the synchronous one. |

**Part VI — Proving it holds, and defending it (5 chapters).**

| # | Chapter | One line |
|---|---|---|
| 25 | Defining done before you build it | An eval turns "done" from a feeling into a score; picking the grader the output deserves; calibrating a model judge against human labels. |
| 26 | Finding where it broke | Four test levels, the integration seam where silent failures live, and reading a trace to separate an integration-layer fault from a model-output fault. |
| 27 | Failures you can wait out, failures you cannot | Retriable versus terminal as the first question; backoff with a cap and a budget; returning the error to the model rather than hiding it; a named fallback for everything a retry cannot fix. |
| 28 | Untrusted content and the action boundary | Why the model cannot tell your instruction from the page it fetched; why delimiters are a soft boundary; why the real boundary is what the agent is permitted to do. |
| 29 | Identity, secrets, and the reviewer's three questions | Least privilege as blast-radius control; secrets that can be rotated; OAuth versus service credential; and the three questions a regulated customer asks first. |

**Part VII — The engagement around the code (3 chapters).**

| # | Chapter | One line |
|---|---|---|
| 30 | From business requirement to functional and infrastructure requirement | How a sentence from a business stakeholder becomes a constraint that decides an endpoint. |
| 31 | Reading and reviewing code you did not write | What an AI reviewer can prove from the diff in front of it, what it is guessing at, and where the human gate goes. |
| 32 | Changing a live system without breaking it | Refactoring at both scales, version control as the safety net, SDLC integration, and what an AI feature adds to the maintain phase that no conventional life-cycle framework anticipates. |

---

## 3. Weight allocation, with the arithmetic

Total design budget: **74,700 words** of teaching prose, excluding self-test items and the reference
appendix. Every chapter carries a word budget; every budget is attributed to one or more of the 25
published skills.

### Chapter budgets and skill attribution

| Ch | Words | Attributed to |
|---|---|---|
| 1 | 2,400 | LLM Fundamentals 1,600 · Context Engineering 800 |
| 2 | 1,600 | LLM Fundamentals 1,600 |
| 3 | 2,600 | Model Selection and Tradeoffs 1,800 · LLM Fundamentals 800 |
| 4 | 2,400 | Technical Fundamentals 2,400 |
| 5 | 2,600 | Technical Fundamentals 1,800 · Software Engineering Foundations 800 |
| 6 | 3,000 | Prompt Engineering 2,600 · LLM Fundamentals 400 |
| 7 | 2,200 | Output Handling 2,200 |
| 8 | 2,400 | Context Engineering 2,400 |
| 9 | 2,200 | Cost and Token Management 2,200 |
| 10 | 2,200 | Tool Implementation 1,400 · Claude API Mechanics 800 |
| 11 | 2,200 | Tool Implementation 2,200 |
| 12 | 1,800 | Claude API Mechanics 1,800 |
| 13 | 2,400 | Agentic Customization 2,400 |
| 14 | 2,600 | MCP Server Development 1,800 · Agentic Customization 800 |
| 15 | 3,200 | Agent Architecture 2,200 · Agent Patterns and Frameworks 1,000 |
| 16 | 2,600 | Agent Construction with Claude 2,600 |
| 17 | 1,800 | Agent Construction with Claude 1,400 · Agent Patterns 400 |
| 18 | 2,200 | Agent Patterns and Frameworks 1,800 · Claude Code Operation 400 |
| 19 | 1,800 | Agent Architecture 900 · Claude Hooks 900 |
| 20 | 2,600 | Claude Code Operation 2,600 |
| 21 | 3,200 | Configuration Management 2,600 · Claude Code Operation 600 |
| 22 | 2,800 | Claude Application Design 2,800 |
| 23 | 3,000 | Claude Application Design 3,000 |
| 24 | 2,200 | Claude API Mechanics 2,200 |
| 25 | 1,800 | Debugging and Error Handling 1,800 |
| 26 | 1,800 | Debugging and Error Handling 1,800 |
| 27 | 1,400 | Debugging and Error Handling 1,400 |
| 28 | 2,600 | AI Application Security 2,000 · Guardrails and Safe Deployment 600 |
| 29 | 2,400 | Identity, Secrets and Key Management 1,200 · Guardrails 800 · Claude API Mechanics 400 |
| 30 | 1,900 | Understanding Requirements 1,900 |
| 31 | 2,000 | Software Engineering Foundations 2,000 |
| 32 | 2,800 | Software Engineering Foundations 1,400 · Systems Life Cycle 1,400 |
| | **74,700** | |

### Domain totals against published weight

| Domain | Words | % of course | Published % | Δ (pp) |
|---|---|---|---|---|
| 1 · Agents and Workflows | 10,300 | 13.8 | 14.7 | −0.9 |
| 2 · Applications and Integration | 21,100 | 28.2 | 33.1 | **−4.9** |
| 3 · Claude Code | 3,600 | 4.8 | 3.1 | **+1.7** |
| 4 · Eval, Testing, Debugging | 5,000 | 6.7 | 2.6 | **+4.1** |
| 5 · Model Selection and Optimization | 12,600 | 16.9 | 16.8 | +0.1 |
| 6 · Prompt and Context Engineering | 8,000 | 10.7 | 11.0 | −0.3 |
| 7 · Security and Safety | 5,500 | 7.4 | 8.1 | −0.7 |
| 8 · Tools and MCPs | 8,600 | 11.5 | 10.6 | +0.9 |
| | **74,700** | **100.0** | **100.0** | |

Five domains land within one point. Three do not, and all three are deliberate.

### Deliberate mismatch 1 — Domain 4 over-allocated by 4.1pp (+3,060 words)

Domain 4 publishes one skill at 2.6%: Debugging and Error Handling. That is 1.4 items. Three
chapters is 3.2× its share.

Defence. First, the mechanisms in those three chapters are the diagnostic vocabulary for four other
domains. "The tool returned an empty result and the model treated it as data" is scored under Tools
and MCPs, and it is answered with a Domain 4 mechanism. "Which layer produced the wrong output" is
the shape of a Claude API Mechanics item. Domain 4's content is doing double duty and the words are
billed where they are spent, not where they pay off. Second, `EXAM-FACTS_v1.md` §1 records no domain
floors, so the risk of over-teaching a 2.6% domain is bounded to the opportunity cost of 3,060 words
— about 4% of the course. Third, the eval material in chapter 25 is what makes the non-determinism
mechanism from chapter 2 actionable; without it, "you cannot assert on exact text" is a fact with
nowhere to go. Cap: three chapters, 5,000 words, and no fourth. If the budget needs trimming, this
is the first place to cut.

### Deliberate mismatch 2 — Domain 3 over-allocated by 1.7pp (+1,270 words)

Claude Code is 3.1%, roughly 1.6 items. It gets 3,600 words.

Defence. Claude Code is the concrete stage on which four other domains' abstractions are
demonstrated: hooks (Domain 7), plugins and configuration (Domain 2), subagents (Domain 1), MCP
scope (Domain 8). The corpus agrees — `CCDV-F_Module-3_Claude-Code-MCP-Integration.md` is 102,190
characters and its takeaways (lines 1273–1345) are about permission risk, durable context, portable
packaging and enterprise integration, not about Claude Code trivia. Over-allocating 1,270 words buys
a working example for four domains. The alternative is teaching hooks in the abstract, which is
where courses lose readers.

### Deliberate mismatch 3 — Domain 2 under-allocated by 4.9pp (−3,660 words)

This is the one that could sink the course, so the deficit is placed precisely rather than spread.

Within-domain arithmetic, against each skill's own published share of 74,700 words:

| Skill | Published % | Published share | Allocated | Δ |
|---|---|---|---|---|
| Claude Application Design | 8.6 | 6,424 | 5,800 | −624 |
| Software Engineering Foundations | 7.4 | 5,528 | 4,200 | −1,328 |
| Claude API Mechanics | 6.8 | 5,080 | 5,200 | +120 |
| Configuration Management | 4.1 | 3,063 | 2,600 | −463 |
| Understanding Requirements | 3.4 | 2,540 | 1,900 | −640 |
| Systems Life Cycle | 2.8 | 2,092 | 1,400 | −692 |

**73% of the deficit (2,660 of 3,627 words) sits in three skills — Software Engineering Foundations,
Understanding Requirements, Systems Life Cycle — that are generic IT-consulting knowledge this
student already holds professionally.** He has shipped systems, run code reviews, derived
infrastructure requirements from business requirements and operated things through a life cycle for
two decades. Teaching him what a functional requirement is would be a waste of his reading hours.
Those three chapters (30, 31, 32) are written as translation: here is the exam's vocabulary for what
you already do, and here is the specifically-AI part your existing frameworks do not cover.

The remaining 967 words of deficit sit in Claude Application Design and Configuration Management,
both under 8% off their share. That is within tolerance.

Note what is **not** discounted: Claude API Mechanics is over-allocated, and Claude Application
Design — the single largest skill on the exam at 8.6% — gets two full chapters (22 and 23). The
discount applies only where his prior experience is a genuine substitute, and nowhere else.

---

## 4. The internal shape of a unit

### What a chapter contains, in order

1. **The situation** — ~150 words. A setting where the decision is live and has consequences. Chosen
   from the opening rotation (below).
2. **The mechanism** — ~40% of the chapter. How the thing actually works, taught one level below the
   rule. Not "batch is cheaper" but why the provider can charge less when nobody is waiting.
3. **The derivation** — ~15%. The rule, derived out loud from the mechanism, with the step shown.
4. **The break** — ~15%. A case where the surface features point one way and the mechanism points the
   other. The mechanism wins, visibly.
5. **The boundary** — ~10%. Where the rule stops applying, what applies instead, and which chapter
   owns that.
6. **The tell** — ~50 words. The phrase in a scenario stem that says "this chapter."
7. **Self-test** — 3–5 items in the exam's own shape.

### What does not earn a place

- A learning-objectives list. The chapter title and the decision line already do that job.
- A summary box. It duplicates the rule and trains skimming.
- Any definition of a term the chapter does not then use.
- Any parameter name, header string, numeric limit or flag that could not be the difference between
  two of four options in a scenario item. `EXAM-FACTS_v1.md` §5: none of the three sample items shows
  a line of code. These go to a marked reference appendix (see §8, FM3).
- Any restatement of the mechanism in different words for emphasis. Say it once, sharply.
- A "why this matters" preamble. If it does not matter, cut the section.

### Keeping 32 chapters from feeling identical — the mechanism

This is the hardest constraint, so it gets four enforceable rules and a ledger, not an intention.

**(a) A catalogue of twelve presentation forms, each with a stated fit condition.** The form is
chosen by the shape of the idea, not by the author's mood.

| Form | Fits an idea that… |
|---|---|
| 1 · The postmortem | is fundamentally a development-versus-production gap |
| 2 · The two-column fork | is a genuine binary with one variable separating the sides |
| 3 · The budget ledger | is about a finite resource spent line by line |
| 4 · The contract | is a set of obligations between two parties, with breach consequences |
| 5 · The escalation ladder | has a cheapest control that you only leave when it fails |
| 6 · The dialogue | turns on one reframing question |
| 7 · The taxonomy by symptom | is best entered from the observable failure, working back |
| 8 · The blast-radius walk | is only understood by assuming the defence already failed |
| 9 · The sustained physical analogue | has a clean isomorphism to a real-world system |
| 10 · The specification read backwards | starts from what must be produced and derives upstream |
| 11 · The inventory audit | is a set of things, each with a purpose and a characteristic misuse |
| 12 · The single case carried end to end | is a sequence of dependent choices |

**(b) A hard non-repetition rule, enforced by a ledger.** No form may be used by two consecutive
chapters. No form may be used more than three times across the 32. Twelve forms × three uses = 36
slots against 32 chapters, so the constraint is satisfiable but binding — it forces the author to
justify each reuse rather than defaulting. The ledger is one line per chapter (`ch. 14 → form 9`),
written before the chapter is drafted and checked after.

**(c) The anchor ledger — no real-world analogy is ever reused.** Every chapter lands its abstraction
on exactly one physical or business anchor, and each anchor is registered once and retired. Thirty-two
chapters, thirty-two distinct anchors, drawn from territory this student already reads fluently:
freight and customs, restaurant service, hospital triage, building inspection, bank reconciliation,
air traffic control, print production, warehouse picking, insurance underwriting, utility metering,
theatre stage management, courier chain of custody. A duplicate anchor is a defect caught in review.
This is the rule that prevents the "everything is like a restaurant kitchen" collapse that makes
courses feel like one voice with one idea.

**(d) Rotation on the opening move.** Every chapter's first 150 words use one of six openings, and
the same opening may not appear in adjacent chapters: a symptom; a decision already made badly; a
physical process; a number; a constraint from outside engineering; a term the reader thinks he
already owns.

**(e) The negative rule that does most of the work.** *No heading may appear in more than one
chapter.* No "Why this matters", no "Key takeaway", no "In practice", no "Common pitfalls". Every
heading is specific to its chapter's content. This is enforceable with a single grep across the
built corpus, and it kills template feel faster than any positive rule, because template feel is
mostly a headings phenomenon.

---

## 5. How understanding is built

### The pedagogical move: the derivation chain

Four steps, in every chapter.

**Step 1 — Teach the causal mechanism, one level below the rule.** Rules are what the exam tests;
mechanisms are what generate rules for cases the course never showed. "Use batch for bulk jobs" is a
rule. "Batch is cheaper because you gave the provider permission to schedule your work when it has
spare capacity, and that permission is what you are selling" is the mechanism. Only the second
survives contact with a stem that says "cost-sensitive, overnight, but the results feed a 9 a.m.
dashboard."

**Step 2 — Derive the rule out loud.** The text performs the derivation once, with the step visible,
so the reader sees that the rule is a consequence rather than a decree. This is what lets him
re-derive it at the desk when the rule alone has gone fuzzy.

**Step 3 — Break it.** Present a case where the surface features and the mechanism disagree, and let
the mechanism win. This is the load-bearing step. It is what trains the reader to distrust
pattern-matching, and pattern-matching is precisely what the exam's distractors are built to reward.
`EXAM-FACTS_v1.md` §5 names the three distractor families — a plausible-but-irrelevant lever, a
non-enforceable control, a bigger-hammer answer. Each of the three is a surface match that a
mechanism defeats. Step 3 is the drill for that.

**Step 4 — Name the tell.** The specific words in a stem that indicate this mechanism is live.
"Reusable across applications", "no user is waiting", "must hold under audit", "the same prompt
returns different text". At two minutes an item, routing speed is a scored skill.

### Specimen passage

**Skill:** Agentic Customization (Domain 8, 4.1%) — "Tradeoffs among built-in Tools, custom Tools,
Skills, and MCPs — selecting the right one for a use case." Chosen because it is genuinely hard, it
is four-way rather than binary, and the corpus does not cover it: `built-in tool` returns zero
matches across all four module transcripts, and the four options are never placed in a single
comparison anywhere in the corpus.

**Form:** 9, the sustained physical analogue. **Anchor:** how a firm acquires a capability. **Opening
move:** a decision already made badly.

---

> A firm needs the ability to check a customer's credit before it signs a contract.
>
> It has four ways to get one. It can use the check its accounting package already ships with. It can
> pay a developer to write one against the credit bureau's API. It can write down the procedure its
> analysts already follow and put it in the handbook. Or it can subscribe to a credit-checking
> service that other firms also use, run by someone whose whole business is keeping it current.
>
> Those four are not four flavours of the same thing. They differ on one question: who owns the
> capability when it changes. The packaged check is owned by the vendor. The developer's script is
> owned by you. The handbook procedure is owned by whoever wrote it, and it does not do anything —
> it tells a person what to do. The subscription is owned by the service, and the same service can be
> used by the sales team, the risk team and both subsidiaries.
>
> Claude has the same four, and they map exactly.
>
> A **built-in tool** is one Anthropic ships and runs. You turn it on. You do not write a schema and
> you do not run the code. You accept what it does.
>
> A **custom tool** is a schema you write plus a function your application runs. You own the
> description, the parameters, the execution, and every change to any of them.
>
> A **Skill** is a markdown file with a description. Claude loads it when the description matches the
> task. A Skill carries instructions — a procedure, a standard, a house style. It does not execute
> anything itself. It tells Claude how to proceed, and Claude then uses whatever tools it has.
>
> An **MCP server** is a separate process that publishes tools, resources and prompts. Any MCP client
> can connect to it. You build it once, and Claude Code, your own application and a teammate's
> application all get the same tools without any of them rebuilding the integration.
>
> Now derive the rule. Two questions, in order.
>
> First: does the capability *do* something, or does it *tell Claude how* to do something? If it
> tells, it is a Skill, and the other three are wrong however convenient they look. A procedure
> written as a tool is a tool that returns a paragraph of advice, which is a Skill wearing a costume.
>
> Second, if it does something: how many callers need it, and who keeps it current? One application
> and you own the logic — custom tool. Anthropic already runs it and its behaviour is acceptable —
> built-in tool. More than one client needs it, or it must be maintained against somebody else's
> changing API — MCP server.
>
> Now break it. A team needs Claude to fetch pages from the open web, inside one internal
> application. The surface features say MCP: it is an integration, it reaches outside the company,
> integrations are what MCP is for. The mechanism says no. Nobody else needs it. Nothing needs
> maintaining against a third party's API. Anthropic already ships and runs a web search tool.
> Turning that on is the answer. Building an MCP server here buys a process to operate and a tool
> list occupying the context window, in exchange for nothing.
>
> The tell in a scenario stem is the word *reusable*, or any phrase naming a second consumer —
> "across several applications", "the other teams need it too", "maintained independently". That
> phrase is what moves the answer from custom tool to MCP server. Without it, MCP is the bigger
> hammer.

---

Note what the passage does *not* do. It does not define "schema" (earned in chapter 11). It does not
name a single API parameter. It does not say the four options "each have their place." The break
paragraph is the transfer engine: the reader watches a plausible answer lose to a mechanism, which
is the exact motion the exam scores.

---

## 6. Corpus gaps

Grounded in keyword sweeps and full reads of `sources/course-transcripts/` (M1 read in full; M2, M3,
M4 read at objectives, takeaways, glossary and five long teaching screens, plus exhaustive keyword
counts across all four files). Counts below are literal `grep -ci` results across the four transcripts.

### Skills the corpus does not cover at all

**1 · Agent Patterns and Frameworks (4.9%) — the named abstraction frameworks.** `Strands` = 0,
`LangGraph` = 0, `PydanticAI` = 0 across all four modules. The published scope names all three.
*Material must:* author a section placing each framework by the layer it occupies and what it
abstracts away from a raw loop or the Agent SDK — graph-of-nodes orchestration with explicit state
(LangGraph), typed agent contracts with validated outputs (PydanticAI), a model-driven loop with
provider abstraction (Strands). Taught at decision level: what problem makes a framework worth its
dependency. No API surface. Grounded against each project's own documentation, cited per claim.

**2 · Agentic Customization (4.1%) — built-in tools, and the four-way comparison.** `built-in tool` =
0 across all four. The corpus teaches custom tools well
(`CCDV-F_Module-2_...md` screen 07), Skills heavily (`Skill` = 65 hits in
`CCDV-F_Module-3_...md`) and MCP well (M3 screen 12), but never in one comparison, and never names
built-in tools. *Material must:* author the four-way selection frame. Specimen in §5 is that chapter.

**3 · Configuration Management (4.1%) — the versioning half.** `pinning` = 0, `prompt versioning` =
0, `plugin dependenc` = 0 across all four. The corpus covers CLAUDE.md and `settings.json` heavily
(`settings.json` = 9 in M3) but the published skill also names model version pinning, prompt
versioning and plugin dependencies, and none appears. *Material must:* author it, and connect it to
the one adjacent thing the corpus does have — M2's warning about behaviour changing across model
releases. A pinned model id is the control that stops a release from silently retuning a prompt.

**4 · Systems Life Cycle (2.8%).** `SDLC` = 0, `life cycle` = 0 across all four. Every `lifecycle`
hit is Claude Code hook lifecycle events, not system life cycle. Complete absence. *Material must:*
translate rather than teach — map the exam's develop/implement/operate/maintain phrasing onto
frameworks he already uses, then spend the words on the part his existing frameworks do not
anticipate: an AI feature's maintain phase includes model version drift and eval regression, which
no conventional life-cycle model has a phase for.

**5 · Understanding Requirements (3.4%).** `business requirement` = 0, `functional requirement` = 0
across all four. One adjacent line in M3 (line 1007) calls data residency an infrastructure
requirement. *Material must:* author it, and use the corpus's one genuine worked example as the
spine — the regulated-data table in `CCDV-F_Module-2_...md` screen 16 (lines ~1096–1110), where
attorney-client privilege, HIPAA, GDPR, FedRAMP and internal residency policy each rule out an
endpoint before any design choice is made. That table is the best "business requirement becomes
infrastructure requirement" case anywhere in the corpus and it is currently filed under agent
construction.

**6 · Technical Fundamentals (6.1%) — websockets.** `websocket` = 0, `socket` = 0 across all four.
The blueprint names websockets explicitly under Technical Fundamentals, and MCP Server Development's
scope names "stdio, sockets". The corpus teaches SSE streaming thoroughly (M2 screen 10) and stdio
versus HTTP thoroughly (M3 screen 12) but never websockets. *Material must:* author a short honest
treatment — persistent bidirectional connection versus server-push-only SSE versus request/response,
and why Claude's streaming uses SSE.

**7 · AI Application Security (3.2%) — PII handling.** `PII` = 0 across all four. The corpus is
excellent on injection, jailbreak, least privilege, secrets and blast radius (M4 screen 16) and
covers PHI through HIPAA (M2 screen 16), but PII as a handling discipline — detection, minimisation,
redaction before the call, what never enters a prompt — is absent. *Material must:* author it inside
chapter 28.

### Skills the corpus covers thinly relative to weight

**8 · Claude Application Design (8.6%) — the largest single skill on the exam.** `Claude Desktop` = 1
hit total, in `CCDV-F_Module-2_...md` line 502, only to say stdio MCP servers need Desktop or Claude
Code as client. `claude.ai` = 2 hits, both incidental (M2 line 1101 as a compliance negative; M3 line
782 on Projects retrieval). `session hygiene` = 0. The published scope is "how Claude interprets
instructions across interfaces (Claude Code, Desktop, claude.ai, API, SDKs), content boundaries,
schema design, session hygiene, plugin management" — and the corpus addresses roughly one fifth of
that. **This is the highest-priority gap by weight: 4.6 items.** *Material must:* author chapters 22
and 23 substantially from Anthropic product and platform documentation, not from the corpus.

**9 · Software Engineering Foundations (7.4%).** Partial. `version control` = 2 hits, both about
committing or not committing `.mcp.json`. `code review` appears as *AI-assisted* review with
calibrated trust (M3 takeaway 2, line 1287) but not as the engineering practice. `large-scale
refactor` = 0; `refactor` is defined in M2's glossary and used in M3's code-modernization section
(lines 1010–1021) but never taught. *Material must:* author chapters 31 and 32, using M3's
modernization section as the anchor case — it is the corpus's only real large-refactor scenario and
it already ties plan mode, hooks and CLAUDE.md to blast-radius control.

**10 · Claude Code Operation (3.1%).** Partial. `headless` = 2 hits, both passing (M3 lines 549, 613).
`auto-mode` = 0, `streaming mode` = 0, `agent memory` = 0 as a Claude Code feature. Permission modes,
`/init`, skills-as-slash-commands, plugins and subagent context loading are all covered well. *Material
must:* fill headless, streaming and auto-mode from product documentation, and keep it tight — 3.1% is
1.6 items and the rest of the skill is already the corpus's strongest ground.

### One inversion worth naming

The corpus teaches **eval design** substantially (`CCDV-F_Module-4_...md` screen 02, the pipeline,
grader selection and judge calibration) and the blueprint publishes **no eval-design skill** —
`EXAM-FACTS_v1.md` §2 flags this explicitly: under Domain 4 the only examinable skill is Debugging
and Error Handling. This is corpus surplus, not gap. Chapter 25 keeps it at 1,800 words because it
makes chapter 2's non-determinism actionable and because Anthropic's own prep advice (§6) names eval
practice, but it does not get more.

### The corpus asset worth exploiting

Every module carries **"Watch Out" screens** — named production postmortems with a full causal chain.
`CCDV-F_Module-2_...md` screen 08 ("The description that sent Claude to the wrong tool") and screen 14
("The session that ran fine in development, then hit a ceiling in production");
`CCDV-F_Module-3_...md` screen 13 ("The API key that traveled with the configuration file into the
repository"). These are the best available raw material for step 3 of the derivation chain, and the
README (`sources/course-transcripts/README.md`) confirms they exist in every module.

---

## 7. Retention and self-test

### What each chapter carries

**One decision rule, stated once, in operational language.** Thirty-two rules across the course.
This is the memorisable payload. Closed book at 2:16 per item, what he needs at the desk is an
applicable rule, not a definition.

**One tell.** The phrase in a stem that activates this chapter. Reading speed is the binding resource
in a 53-item, 120-minute paper; tells convert reading into routing.

**Three to five items in the exam's own shape.** Short scenario, four options, one plausible-but-
irrelevant lever, one non-enforceable control, one bigger-hammer. Written as multiple-choice or
multiple-response with the count stated, mirroring `EXAM-FACTS_v1.md` §1. Never fill-in-the-blank —
the exam is select-not-produce. Justification: the three distractor families are published in §5;
drilling against them directly is the highest-value practice available, and the corpus's own
checkpoints already have that shape and can seed the first pass.

### What the course carries, but not per chapter

**Eight cross-chapter interference sets.** Paired chapters that a reader will confuse, drilled
together: caching versus batch (both marketed as "cheaper"); Skill versus MCP server; workflow versus
agent; hook versus prompt instruction; pruning versus compaction; retriable versus terminal; stdio
versus HTTP; ZDR versus BAA. Justification: quizzing one chapter immediately after reading it
measures recency, not discrimination. The exam mixes domains inside a paper, and discrimination is
what actually gets scored. This is the single most under-built thing in most exam courses.

**One full 53-item mock at exam length and exam weighting, once, late.** Pacing under a 120-minute
clock is a separate skill from knowing the material, and it can only be practised at full length.

### What is deliberately absent, and why

- **No spaced-repetition scheduling machinery.** One student, one course. A schedule is overhead he
  will abandon in week two, and abandoning it feels like failing.
- **No flashcard deck of API parameters.** §5 says the exam does not ask for them. A deck would train
  the wrong retrieval.
- **No per-chapter summary box.** It duplicates the decision rule and teaches the reader to skip to
  it.
- **No learning-objectives header.** Coverage theatre. The title plus the decision line is the
  objective.
- **No standalone glossary.** Terms are defined where they are earned. A glossary invites
  definition-recall study, which this exam does not reward, and it is where courses quietly restore
  the parameter-memorisation habit the design just removed.

---

## 8. Failure modes

### FM1 — The course teaches the corpus, and the exam asks the blueprint

The corpus is 381,000 characters of genuinely excellent Anthropic teaching, and it is seductive
precisely because it is good. It also does not cover the three named agent frameworks, built-in
tools, model pinning, prompt versioning, systems life cycle, requirements derivation, websockets, PII
handling, session hygiene, or the cross-interface comparison that is the largest single skill on the
paper. By published weight those add to roughly a quarter of the exam. A course written from the
corpus alone leaves him confident and short — the worst combination, because he will not know to
study more.

**Guard.** The unit of work is the *skill*, never the transcript screen. The §3 weight table is a
contract: every chapter names the skills it discharges and the words it spends on each. Chapters 13,
16, 21, 22, 23, 30, 31 and 32 are explicitly gap-filling and every factual claim in them must cite a
non-corpus source. Build-time audit, mechanical: all 25 skills have at least one chapter, and every
skill's allocated words are within ±20% of its published share, or the deviation is written down and
defended in the design like the three in §3.

### FM2 — He learns 32 rules and cannot tell which one the question is asking about

This is the realistic closed-book failure at 2:16 an item. He will know caching. He will know batch.
The stem will say nightly, high volume, cost-sensitive, and both will feel right, and he will spend
four minutes and pick the wrong one and lose the time as well as the mark. On the score report this
reads as a knowledge gap in Domain 5. It is a retrieval gap.

**Guard.** Three things, all built into the chapter rather than bolted on at revision. The *tell* is
a required section of every chapter, not an optional one. The *break* (step 3 of the derivation
chain) forces the reader to watch a surface match lose to a mechanism, in every single chapter. And
the eight cross-chapter interference sets exist specifically to test discrimination rather than
recall. Discrimination is a per-chapter obligation in this design, which is what stops it being
something the student is expected to develop on his own.

### FM3 — The material drifts into parameter recall, because the corpus is full of it

The corpus carries a large volume of version-sensitive product specifics: beta header strings,
`disable_parallel_tool_use`, four cache breakpoints, a 1,024-token cache floor, a five-minute default
TTL, `defer_loading`, `model_context_window_exceeded`. It is concrete, it is quotable, and it feels
like rigour. `EXAM-FACTS_v1.md` §5 records that none of the three published sample items shows a line
of code or asks the candidate to produce one, and §2 records that nothing in the 25 skills requires
recalling a parameter name. An hour spent memorising header strings is an hour not spent on the
workflow-or-agent decision, which alone carries 4.5%.

**Guard.** A single admission test, applied to every fact before it enters the main body: *could this
fact be the difference between two of four options in a scenario item?* If not, it goes to a marked
reference appendix headed "reference, not revision", and the self-test items are forbidden from
testing anything that lives there. This has a second benefit: `EXAM-FACTS_v1.md` records the guide as
version 1.0, effective July 2026, subject to change without notice. Concentrating the volatile
specifics in one appendix means the quarterly re-check has a small, bounded surface instead of 32
chapters.

---

## Sources actually read

- `EXAM-FACTS_v1.md` — sections 1, 2, 5 and 6 only, as instructed. Sections 3 and 4 not opened.
- `sources/course-transcripts/README.md` — full.
- `sources/course-transcripts/CCDV-F_Module-1_MSO-Foundations.md` — full (23,265 chars).
- `sources/course-transcripts/CCDV-F_Module-2_Production-Grade-Prompting-Agents-Tool-Use.md` —
  objectives (screen 01), tool-use and schema design (screens 07–09), context engineering and model
  selection (screen 13), agent construction (screen 16), takeaways and glossary (screens 27–28);
  full-file keyword counts across ~70 terms; screen index of all 29 screens.
- `sources/course-transcripts/CCDV-F_Module-3_Claude-Code-MCP-Integration.md` — objectives (screen
  01), MCP server construction (screen 12), takeaways and glossary (screens 20–21); targeted greps on
  permission modes, CLAUDE.md, skills, plugins, code modernization; full-file keyword counts; screen
  index of all 22 elements.
- `sources/course-transcripts/CCDV-F_Module-4_Production-Engineering-Evals-Security.md` — objectives
  (screen 01), security (screen 16), takeaways and glossary (screens 21–22); full-file keyword
  counts; screen index of all 23 elements.

**Not read:** `sources/CCDV-F_Official-Exam-Guide_v1.0.pdf`. The blueprint was taken from
`EXAM-FACTS_v1.md` §2, which states it is reconciled against the PDF and that the skill weights sum
exactly to their domains and the domains to 100.0.

**Not read, as instructed, and not encountered:** anything under `Outputs/`, either `CLAUDE.md`,
`ROADMAP.md`, `BACKGROUND-MATERIAL-INDEX_v1.md`, `README.md` at project root, anything under `prep
with quiz/`, or any sibling exam folder. The transcripts README references
`prep with quiz/CCDV-F_Domain-N_v1.md` as a downstream artefact; that file was not opened.
