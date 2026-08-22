# CCDV-F — Teaching Architecture v2

**Created:** 2026-08-22 · **Status:** Stage 1 complete. Authoritative for chapter list and budgets.

> **v1 is not superseded and must not be edited.** `CCDV-F_Pedagogy-Design_v1.md` is the record of what
> the independent architect produced blind, and it is the evidence that this design was not coloured by
> the previous attempt. **Read v1 for the reasoning** — the unit of teaching, the sequence principle,
> the twelve presentation forms, the three ledgers, the derivation chain, the specimen passage, the
> corpus-gap analysis and the three failure modes. All of that stands unchanged.
>
> **Read v2 for the chapter list and the budgets.** Where the two disagree on a number, v2 wins.

---

## 1. What changed, and why

Seven repairs, all from the cold-start adversary's audit. Six close coverage defects; one corrects an
arithmetic claim.

| # | Repair | Chapters | Words | Cause |
|---|---|---|---|---|
| 1 | Third-party vendor invocation authored | 4 | +700 | "Invoking Claude through third-party vendors" is bolded in a 6.8% skill and appeared nowhere in v1. `Bedrock` and `Vertex` are in the corpus (M2 ×4, M4 ×2) — v1 dropped them while its word audit showed the skill healthy at +2.4% |
| 2 | Prompt Engineering restored | 6 | +400 | v1 had it at −24.3% and undefended. Invisible because Domain 6 netted to −0.3pp. Now −17.7%, inside tolerance |
| 3 | Named frameworks given a budget | 16 | +800 | v1 §6 said Strands / LangGraph / PydanticAI must be authored; v1 §3 allocated them nothing. Ch.16 was billed 100% to a different skill |
| 4 | Old ch.23 split in two | 23, 24 | +1,000 | Four unrelated sub-topics at 750 words each — the grab-bag shape v1 §1 argues against |
| 5 | Layered guardrails given a chapter | 30 (new) | +1,300 | "Guardrail layering" and "content policy" appeared in no chapter line. Layering is the exact shape of the guide's own sample item 2 |
| 6 | PII, data leakage, confidentiality authored | 29 | +600 | All three named in AI Application Security's published scope; all three return zero in the corpus |
| 7 | Configuration Management off the line | 21 | +100 | Sat at −19.9%, one rounding away from an undefended breach |

**Result: 34 chapters, 79,500 words** — 79,200 after Stage 1, plus 300 in ch.29 from the Stage 2
coverage sweep (§8). Chapter ceiling of ~3,400 words held; the largest chapters are 6 and 16, both
exactly at it.

### The arithmetic error corrected

v1's Domain 2 defence reads: *"The remaining 967 words of deficit sit in Claude Application Design and
Configuration Management, both under 8% off their share. That is within tolerance."*

The 967 is right. **"Under 8%" is wrong** — the two were 9.7% and 15.1% off. That sentence was what
dismissed the residual deficit on the largest skill on the exam. Both are now positive or comfortably
inside tolerance, so the claim is retired rather than repaired.

### One forward reference resolved here

**FR3 — ch.6 taught input sanitisation 22 chapters before the mechanism that justifies it (ch.29).**
Resolved by teaching the minimal mechanism in place: the model sees one flat text, so anything pasted
into it can read as instruction. Ch.6's 400 words of LLM Fundamentals attribution carry it. Ch.29 then
deepens the same idea into the action boundary. That is a spiral, not a forward reference.

**FR1, FR2, FR4 and FR5 remain open and are Stage 3.**

---

## 2. The chapter list

Sequence principle unchanged from v1 §2: dependency first; within what dependency allows, order by how
much of the rest of the course the mechanism unlocks; the student's own professional territory last.

### Part I — The substrate (5)

| # | Chapter | One line |
|---|---|---|
| 1 | The one budget everything spends | Tokens as the unit of input, output and price; the context window as a single fixed pot; the two edge behaviours — rejected before generation, or truncated mid-generation. |
| 2 | Why the same prompt answers twice differently | Sampling from a distribution, what temperature does to it, why newest models refuse sampling parameters, and why non-determinism forces you to assert on properties rather than text. |
| 3 | Two dials, not one ⟵ *named* | Model tier is one decision; how hard the model thinks is a separate per-call decision. **Opus, Sonnet and Haiku by use case; the quality / latency / cost triangle; extended thinking and adaptive thinking as two distinct things, and which models support adaptive; effort levels; fast mode**; and why behaviour changes across releases break prompts tuned on the old one. |
| 4 | What is actually on the wire ⟵ *repaired* | REST underneath everything; JSON as the contract; what an SDK does and does not do; the Anthropic SDK versus the Agent SDK; **and where you get Claude from — first-party API versus Bedrock versus Vertex, and what that choice decides about region, auth and compliance.** |
| 5 | Who is waiting? | Synchronous, streaming, async/await, websockets and batch — five request shapes, one question that picks between them. |

### Part II — Getting output your code can use (4)

| # | Chapter | One line |
|---|---|---|
| 6 | Diagnosing a prompt by its failure ⟵ *repaired* | The failure type names the missing technique. System-versus-user placement, **placement across components**, shot count, **iterative refinement**, and input sanitisation **with the mechanism that justifies it**. |
| 7 | When asking nicely stops working ⟵ *resequenced* | Structured outputs and strict tool use move the guarantee from the prompt into the API; what they cost; the two cases they still do not cover. Defensive parsing and `stop_reason`; **response validation as a separate act from parsing — parsing tolerates a malformed shape, validation rejects wrong content — and skepticism toward confident output as the posture the chapter argues for.** Introduces only the primitive it needs — a tool is a named schema the model must fill — and leaves selection and description-writing to ch.11. |
| 8 | Keeping a long session inside the budget ⟵ *resequenced* | Pruning, compaction, clearing, **and handing work to a second window that returns only its answer** — four instruments, and the specific continuity each destroys. **The fourth is stated as a mechanism derivable from ch.1; it acquires the name "subagent" in ch.18. Drift and bloat are taught as two distinct failures, not one — bloat is volume, drift is the window quietly ceasing to describe the task.** |
| 9 | Paying once for what does not change ⟵ *named* | Prompt caching as a prefix contract; **cache check-pointing as the deliberate placement of breakpoints, taught alongside what invalidates them**; what caching cannot help; measuring context pressure before a request goes out; **and reading the usage block after — token usage tracking and cost modelling as the arithmetic that turns tokens into a number a business recognises.** |

### Part III — Giving Claude hands (5)

| # | Chapter | One line |
|---|---|---|
| 10 | The loop your code owns | Claude does not run tools; it asks. The six-step loop and the block-pairing contract. |
| 11 | Why Claude picked the wrong tool | Selection is driven by the description field. Exclusion conditions, required versus optional, overlapping shapes, over-tooling, when to merge. Client-side versus server-side tools and approval patterns. |
| 12 | Streaming without corrupting state | A stream ending is not a message completing. Assembling events into blocks, committing a turn only after the message closes, and the retry bug that looks like a schema bug. |
| 13 | Four ways to hand Claude a capability | Built-in tool, custom tool, Skill, MCP server. Who owns the capability when it changes. |
| 14 | Build once, connect many ⟵ *named* | MCP servers exposing tools, resources and prompts; **communication patterns as the guide words them — stdio and sockets — with HTTP named as what a socket carries rather than as a substitute for the term; the client's half of the protocol, not only the server's; and deployment — where the server actually runs**; local, user, project and enterprise scope; per-tool permissions; why the secret never goes in the config file. |

### Part IV — Agents (5)

| # | Chapter | One line |
|---|---|---|
| 15 | Workflow or agent | The enumerate-the-steps test; the four workflow sub-patterns; orchestrator-worker and what its token multiple buys; manager and supervisor hierarchies. |
| 16 | Who runs the loop ⟵ *repaired* | Raw Messages API loop, Agent SDK, Claude Managed Agents; self-hosted versus Anthropic-hosted; **and the three named abstraction frameworks — Strands, LangGraph, PydanticAI — placed by the layer each occupies.** |
| 17 | Building the loop by hand | Register, scope, iterate, exit. What breaks when each of the four is missing. |
| 18 | State that outlives a turn | In-context, external, summarised and stateless memory; subagent context isolation; why carrying instructions is a different problem from carrying state. |
| 19 | Where the human stands ⟵ *resequenced* | Three HITL insertion points chosen by worst-case outcome; **hooks as the deterministic version, taught here and only here**; deny beats ask beats allow, stated as a precedence principle that ch.20 then grounds in Claude Code's own deny rules. |

### Part V — The developer's surfaces (6)

| # | Chapter | One line |
|---|---|---|
| 20 | Claude Code as a governed agent ⟵ *named* | **The five primitives the guide names — Rules, Skills, Commands, Agents, Agent Memory — and what each is for**; explore, plan, code; permission mode as a risk decision; deny rules no mode can bypass; **built-in and custom slash commands; session management, meaning the CLI session and never the application session of ch.24**; headless, streaming and auto-mode; repository initialisation. |
| 21 | Three places a durable instruction can live ⟵ *resequenced, named* | **The CLAUDE.md hierarchy — the precedence order across enterprise, user, project and directory, which is a different thing from one file's dilution point**; path-scoped rules files; subagents; **`settings.json` — its schema and where it wins**; plugins as packaging; model pinning, prompt versioning, plugin dependencies. **Hooks are named here as the thing that is not an instruction — enforcement rather than guidance — and are taught in ch.19, not re-taught here.** |
| 22 | The same model, five front doors | How Claude interprets instruction differently in Claude Code, Desktop, claude.ai, the API and the SDKs — what carries across and what does not. |
| 23 | Contracts inside your own application ⟵ *new split* | Content boundaries between instruction, data and output at the application layer; schema design for the application's own contracts, as distinct from the tool schemas of ch.11. |
| 24 | What an application remembers ⟵ *new split* | Session hygiene — what a session holds, when it should be ended rather than trimmed — and plugin management across a team. |
| 25 | Sending Claude things that are not text | Images and their token arithmetic, PDFs, the Files API, and matching the API to the workload. |

### Part VI — Proving it holds, and defending it (6)

| # | Chapter | One line |
|---|---|---|
| 26 | Defining done before you build it | An eval turns "done" from a feeling into a score; picking the grader the output deserves; calibrating a model judge against human labels. |
| 27 | Finding where it broke | Four test levels, the integration seam where silent failures live, reading a trace to separate an integration-layer fault from a model-output fault. |
| 28 | Failures you can wait out, failures you cannot | Retriable versus terminal as the first question; backoff with a cap and a budget; returning the error to the model; a named fallback for what retry cannot fix. |
| 29 | Untrusted content and the action boundary ⟵ *repaired* | Why the model cannot tell your instruction from the page it fetched; why delimiters are soft; why the real boundary is what the agent may do. **Jailbreak defence as a separate problem from injection — injection is text that arrived, a jailbreak is the user themselves. PII and data leakage: detection, minimisation, redaction before the call. Confidentiality and integrity as two properties, not one — confidentiality is what an attacker can read, integrity is what an attacker can change.** |
| 30 | Layered guardrails ⟵ *new* | **Content policy and guardrail layering. Why one control is never enough, where each layer sits, and why a control the model can decline is not a control.** The shape of the guide's own sample item 2. |
| 31 | Identity, secrets, and the reviewer's three questions | Least privilege as blast-radius control; secrets that can be rotated; identity validation; OAuth versus service credential; the three questions a regulated customer asks first. |

### Part VII — The engagement around the code (3)

| # | Chapter | One line |
|---|---|---|
| 32 | From business requirement to functional and infrastructure requirement ⟵ *named* | How a sentence from a business stakeholder becomes a constraint that decides an endpoint. **The guide names two input sources, not one — business requirements and the solution architecture — and they constrain differently.** |
| 33 | Reading and reviewing code you did not write | What an AI reviewer can prove from the diff, what it is guessing at, and where the human gate goes. |
| 34 | Changing a live system without breaking it ⟵ *named* | Refactoring at both scales, version control as the safety net, SDLC integration. **All four life-cycle phases the guide names — developing, implementing, operating, maintaining — not the maintain phase alone**, and what an AI feature adds to maintain that no conventional framework anticipates. |

---

## 3. Budgets

**Total 79,500 words** across 34 chapters. Average 2,338; ceiling 3,400, hit by ch.6 and ch.16 only.
Verified programmatically: every chapter's skill attributions sum exactly to its chapter total, all 34.

| Ch | Words | Attributed to |
|---|---|---|
| 1 | 2,400 | LLM Fundamentals 1,600 · Context Engineering 800 |
| 2 | 1,600 | LLM Fundamentals 1,600 |
| 3 | 2,600 | Model Selection and Tradeoffs 1,800 · LLM Fundamentals 800 |
| 4 | **3,100** | Technical Fundamentals 2,400 · **Claude API Mechanics 700** |
| 5 | 2,600 | Technical Fundamentals 1,800 · Software Engineering Foundations 800 |
| 6 | **3,400** | **Prompt Engineering 3,000** · LLM Fundamentals 400 |
| 7 | 2,200 | Output Handling 2,200 |
| 8 | 2,400 | Context Engineering 2,400 |
| 9 | 2,200 | Cost and Token Management 2,200 |
| 10 | 2,200 | Tool Implementation 1,400 · Claude API Mechanics 800 |
| 11 | 2,200 | Tool Implementation 2,200 |
| 12 | 1,800 | Claude API Mechanics 1,800 |
| 13 | 2,400 | Agentic Customization 2,400 |
| 14 | 2,600 | MCP Server Development 1,800 · Agentic Customization 800 |
| 15 | 3,200 | Agent Architecture 2,200 · Agent Patterns and Frameworks 1,000 |
| 16 | **3,400** | Agent Construction 2,600 · **Agent Patterns and Frameworks 800** |
| 17 | 1,800 | Agent Construction 1,400 · Agent Patterns and Frameworks 400 |
| 18 | 2,200 | Agent Patterns and Frameworks 1,800 · Claude Code Operation 400 |
| 19 | 1,800 | Agent Architecture 900 · Claude Hooks 900 |
| 20 | 2,600 | Claude Code Operation 2,600 |
| 21 | **3,300** | **Configuration Management 2,700** · Claude Code Operation 600 |
| 22 | **3,000** | Claude Application Design 3,000 |
| 23 | **2,200** | Claude Application Design 2,200 |
| 24 | **1,800** | Claude Application Design 1,800 |
| 25 | 2,200 | Claude API Mechanics 2,200 |
| 26 | 1,800 | Debugging and Error Handling 1,800 |
| 27 | 1,800 | Debugging and Error Handling 1,800 |
| 28 | 1,400 | Debugging and Error Handling 1,400 |
| 29 | **2,900** | **AI Application Security 2,900** |
| 30 | **1,300** | **Guardrails and Safe Deployment 1,300** |
| 31 | 2,400 | Identity, Secrets and Keys 1,200 · Guardrails 800 · Claude API Mechanics 400 |
| 32 | 1,900 | Understanding Requirements 1,900 |
| 33 | 2,000 | Software Engineering Foundations 2,000 |
| 34 | 2,800 | Software Engineering Foundations 1,400 · Systems Life Cycle 1,400 |
| | **79,500** | |

### Per-skill, against published share

| Skill | Pub % | Share | Allocated | Δ |
|---|---|---|---|---|
| Claude Application Design | 8.6 | 6,837 | 7,000 | +2.4% |
| **Software Engineering Foundations** | 7.4 | 5,883 | 4,200 | **−28.6%** |
| Claude API Mechanics | 6.8 | 5,406 | 5,900 | +9.1% |
| Technical Fundamentals | 6.1 | 4,850 | 4,200 | −13.4% |
| Agent Construction with Claude | 5.3 | 4,214 | 4,000 | −5.1% |
| LLM Fundamentals | 5.2 | 4,134 | 4,400 | +6.4% |
| Agent Patterns and Frameworks | 4.9 | 3,896 | 4,000 | +2.7% |
| Prompt Engineering | 4.6 | 3,657 | 3,000 | −18.0% |
| Agent Architecture | 4.5 | 3,578 | 3,100 | −13.3% |
| Tool Implementation | 4.4 | 3,498 | 3,600 | +2.9% |
| Configuration Management | 4.1 | 3,259 | 2,700 | −17.2% |
| Agentic Customization | 4.1 | 3,259 | 3,200 | −1.8% |
| Context Engineering | 3.8 | 3,021 | 3,200 | +5.9% |
| **Understanding Requirements** | 3.4 | 2,703 | 1,900 | **−29.7%** |
| AI Application Security | 3.2 | 2,544 | 2,900 | +14.0% |
| **Claude Code Operation** | 3.1 | 2,464 | 3,600 | **+46.1%** |
| **Systems Life Cycle** | 2.8 | 2,226 | 1,400 | **−37.1%** |
| Cost and Token Management | 2.8 | 2,226 | 2,200 | −1.2% |
| Model Selection and Tradeoffs | 2.7 | 2,147 | 1,800 | −16.1% |
| **Debugging and Error Handling** | 2.6 | 2,067 | 5,000 | **+141.9%** |
| Output Handling | 2.6 | 2,067 | 2,200 | +6.4% |
| Guardrails and Safe Deployment | 2.3 | 1,828 | 2,100 | +14.8% |
| MCP Server Development | 2.1 | 1,670 | 1,800 | +7.8% |
| Identity, Secrets and Key Management | 1.6 | 1,272 | 1,200 | −5.7% |
| Claude Hooks | 1.0 | 795 | 900 | +13.2% |

**Five ±20% breaches, all defended, none new.** Debugging and Claude Code Operation are v1's
over-allocations and its defences stand (v1 §3). The three under-allocations are the Domain 2
substitution, whose treatment changed — see below. Every skill v1 left undefended is now inside
tolerance.

### Domain rollup

| Domain | Words | Course % | Published % | Δ |
|---|---|---|---|---|
| 1 Agents and Workflows | 11,100 | 14.0 | 14.7 | −0.7pp |
| 2 Applications and Integration | 23,100 | 29.1 | 33.1 | −4.0pp |
| 3 Claude Code | 3,600 | 4.5 | 3.1 | +1.4pp |
| 4 Eval, Testing, Debugging | 5,000 | 6.3 | 2.6 | +3.7pp |
| 5 Model Selection and Optimization | 12,600 | 15.8 | 16.8 | −1.0pp |
| 6 Prompt and Context Engineering | 8,400 | 10.6 | 11.0 | −0.4pp |
| 7 Security and Safety | 7,100 | 8.9 | 8.1 | +0.8pp |
| 8 Tools and MCPs | 8,600 | 10.8 | 10.6 | +0.2pp |

Domain 7 moved from −0.7pp in v1 to +0.8pp on the guardrails, PII, integrity and jailbreak repairs —
the only domain to cross zero. The rest held within a rounding step of their v2-initial values.

---

## 4. The Domain 2 substitution — treatment changed

v1 discounted Software Engineering Foundations, Understanding Requirements and Systems Life Cycle by
2,660 words on the strength of twenty years of consulting. The word cut is **held**. The reasoning
behind it is **not** accepted as sufficient.

The adversary's objection: experience substitutes for *understanding* the material, not for
*recognising this exam's vocabulary* for it, and these are the most definitional skills on the
blueprint. Systems Life Cycle publishes as "life-cycle management concepts and frameworks" — a naming
skill, with no Claude-specific tradeoff inside it to test. Understanding Requirements turns on the
exam's *functional* versus *infrastructure* pairing, and a practitioner of twenty years has his own
firm's vocabulary for it. Together they are **7.2 items against a 16-item margin**, with no corpus
cross-check at all.

**Adopted resolution: hold the word cut, triple the item counts.** Chapters 32, 33 and 34 carry
**8–10 exam-shaped items each** instead of the standard 3–5. For definitional skills, item drill tests
vocabulary recognition and prose does not. v1's instinct that he does not need instruction here is
right; its conclusion that he therefore needs less of the chapter is not.

---

## 5. Gap-filling chapters — the corrected list

Chapters where the corpus is absent or near-absent, and **every factual claim must cite an
Anthropic-controlled source**. v1 named eight. The adversary's sub-scope sweep found the corpus also
silent on `sanitiz`, `iterative refinement`, `self-hosted`, `fast mode`, `client-side tool` /
`server-side tool`, `approval pattern`, `data leakage`, `confidentiality`, `content policy`,
`guardrail layer` and `identity validation` — eleven more, landing in six further chapters.

**3 · 6 · 7 · 11 · 13 · 16 · 21 · 22 · 23 · 24 · 29 · 30 · 31 · 32 · 33 · 34**

Sixteen of thirty-four. An author working from v1's list alone would have written 3, 6, 7, 11, 29, 30
and 31 from the corpus and inherited its blind spots — which is precisely the failure v1's own FM1 was
written to prevent.

---

## 6. What v1 still governs

Unchanged and authoritative in v1:

- **§1** the unit of teaching, and why not per-domain or per-skill
- **§2** the sequence principle and the unlocking rule
- **§4** the seven-part internal chapter shape; what does not earn a place; the twelve presentation
  forms; the form, anchor and opening ledgers; the no-repeated-headings rule
- **§5** the four-step derivation chain and the specimen passage
- **§6** the corpus-gap analysis and the Watch Out postmortems worth exploiting
- **§7** retention and self-test, including the eight interference sets
- **§8** the three failure modes

Two notes carried forward for the briefs rather than the budget:

1. **Technical Fundamentals (6.1%) has an unenumerable published scope** — "foundational technical
   concepts for AI application development" plus two examples. 3.2 items whose content cannot be
   predicted from the guide. It needs a breadth strategy, not a depth allocation, and neither v1 nor
   v2 has one. Open.
2. **Agent Architecture's "manager/supervisor hierarchies"** was thin in v1 — only orchestrator-worker.
   Named explicitly in ch.15's line now; the budget was already adequate.

---

## 7. Sequence — Stage 3, closed 2026-08-22

Five forward references were found by the cold-start audit: a chapter using a mechanism the course
teaches later. All five sat in chapters 1–22, which v2 did not renumber, so they carry across from the
32-chapter numbering unchanged.

**None was resolved by reordering.** Every fix teaches the minimal true statement in place and defers
the rest — a spiral, which is what v1 §5 Step 1 already asks for ("teach the causal mechanism one
level below the rule"). Reordering was considered and rejected in each case for the reason given.

| Ref | Was | Fix | Why not reorder |
|---|---|---|---|
| **FR1** | ch.7 used *strict tool use*; tool schemas are ch.11 | Ch.7 introduces one primitive — a tool is a named schema the model must fill — and defers selection and description-writing to ch.11 | Ch.11 depends on ch.6 (a tool description *is* a prompt), and ch.7 depends on ch.11. Reordering wholesale creates a cycle; the primitive does not |
| **FR2** | ch.8 listed *subagent handoff* as a context instrument; subagents are ch.18. **Forward by 10** | Ch.8 teaches it as "hand the work to a second window that returns only its answer" — fully derivable from ch.1's context window, needing no agent machinery. Ch.18 gives it the name | The mechanism was never the problem; the product name was. v1's §2 obscured this by crediting ch.1 with unlocking subagent handoffs — ch.1 teaches the window, not subagents |
| **FR3** | ch.6 taught *input sanitisation*; the mechanism is ch.29. **Forward by 23** | Closed in Stage 1. Ch.6 teaches the mechanism — the model sees one flat text, so anything pasted in can read as instruction — and ch.29 deepens it into the action boundary | Sanitisation is published under Prompt Engineering; moving the topic would misattribute a skill |
| **FR4** | ch.13's four-way comparison uses Skills and MCP servers; MCP is ch.14, Skills later | **Accepted as written.** The chapter defines all four from scratch in a paragraph each, and the specimen passage doing exactly that passed the prose gate | Swapping 13 and 14 fixes a one-chapter reference the specimen already handles, and does nothing about Skills, which is the real problem. See the open item below |
| **FR5** | ch.19 used *deny over ask over allow*; deny rules are ch.20 | Ch.19 states it as a precedence principle; ch.20 grounds it in Claude Code's specific deny rules. Ch.14 already teaches per-tool permissions and precedes both | One chapter, across a part boundary, for a principle that is true independently of any product's implementation |

### Duplicate ownership resolved

**Hooks were owned by two chapters** — ch.19 ("hooks as the deterministic version") and ch.21 ("four
places a durable instruction can live"). That is the retrieval ambiguity FM2 exists to prevent: the
student meets the mechanism twice and cannot tell which question is asking for it.

**Ch.19 owns hooks.** Ch.21 becomes *three* places a durable instruction can live, and names hooks as
the thing that is **not** an instruction — enforcement rather than guidance. That distinction is real
and sharpens both chapters rather than merely deduplicating them. No budget moved: Claude Hooks' 900
words were always attributed to ch.19.

### Open, carried to Stage 4

**Skills have no home chapter.** They are defined inside ch.13's four-way comparison and appear in no
other chapter line — not ch.20, not ch.21. Skills are named in the published scope of two skills
totalling 7.2%: Agentic Customization (4.1%) and Claude Code Operation (3.1%). A mechanism that gets
its only treatment inside a comparison of four things is under-taught.

This is a coverage question rather than a sequence one, so it is **held for reconciliation against the
Stage 2 sub-scope contract** rather than fixed here on a guess. **Resolved in §8** — the sweep confirmed
it and settled ownership.

---

## 8. Coverage — Stage 2, closed 2026-08-22

The blueprint's 25 published scope cells were atomised into **153 named sub-topics** and each was
mapped to a chapter. Full contract: `CCDV-F_Coverage-Contract_v1.md`. Result: **108 explicit ·
44 implied · 1 absent**, and every one of the 153 placed exactly once. No new chapter was needed.

**Why this audit exists.** Stage 1's ±20% word test passed Claude API Mechanics at +2.4% while a
bolded phrase in its scope appeared nowhere in the design. Word-count parity with a published weight
is not the same claim as covering the published scope, and only a phrase-level sweep tests the second.

### The one genuinely absent sub-topic

**`integrity`** — AI Application Security. The guide's cell ends `…confidentiality, integrity`; Stage 1
added confidentiality and stopped one word short. Confidentiality is what an attacker can read;
integrity is what an attacker can change. Placed in ch.29 with the action boundary. **Ch.29 raised
2,600 → 2,900**, also absorbing jailbreak defence, which the sweep found named in no chapter and which
is a different problem from injection: injection is text that arrived, a jailbreak is the user.

### The nine bolded sub-topics that were implied-only

These are the dangerous class — the chapter looks covered, so an author would skip them. All nine now
appear verbatim in their chapter line.

| Sub-topic | Ch | What the line said instead |
|---|---|---|
| cache check-pointing | 9 | "what invalidates it" — the opposite operation |
| sockets | 14 | "stdio versus **HTTP**" — a different word substituted for the bolded one |
| extended thinking | 3 | named *adaptive* thinking only; the guide names both |
| the CLAUDE.md hierarchy | 21 | "CLAUDE.md and its dilution point" — one file's property, not the precedence order |
| skepticism toward confident output | 7 | all mechanical; the judgement half of the bold span was absent |
| preventing context drift and bloat | 8 | four instruments; neither "drift" nor "bloat" appeared, and drift is a distinct failure |
| client vs server (MCP) | 14 | servers exposing things; the client's half never described |
| Messages | 10 | block-pairing only — one property of a message |
| Opus vs Sonnet vs Haiku | 3 | "model tier", never naming a tier |

Also made explicit: `settings.json`, named in two skills' scopes and in **no** chapter line;
`solution architecture`, the second of two input sources ch.32 named only one of; and the four
life-cycle phases in ch.34, which named only *maintain*.

### The finding that mattered most

**Ch.20's line named none of the five Claude Code primitives the guide names** — Rules, Skills,
Commands, Agents, Agent Memory — nor slash commands, nor session management. All seven were
implied-only inside a chapter whose title suggested they were covered. This also settles the Skills
question left open in §7: **ch.13 owns Skills as a capability choice; ch.20 names it as a Claude Code
primitive and points at ch.13.** No words moved — Claude Code Operation's +46.1% surplus already
carried the budget; only the line was silent.

### Double-owned ground

Thirteen sub-topics were claimed by two or more chapters — the retrieval ambiguity FM2 exists to
prevent. Ownership is assigned in the contract file. Two worth restating here because they are
counter-intuitive:

- **context-window management** was claimed by ch.1, ch.8 and ch.18. **Ch.8 owns it.** Ch.1 owns the
  fixed-pot concept only; ch.18 owns only what a loop carries forward.
- **session management vs session hygiene** — ch.20 and ch.24. **Both keep it, with a stated
  discriminator:** ch.20 must say "the CLI session", ch.24 "the application's own session", and
  **neither may use the bare word "session" as its unit.**

### Two neutral observations, not defects

**Ch.26 owns zero sub-topics.** It teaches eval design, and `EXAM-FACTS_v1.md` §2 records that v1.0
publishes no eval-design skill — only Debugging and Error Handling. That is the blueprint's shape, not
a design error, and it is why Domain 4 runs at +141.9%. Ch.26 is the first thing to cut if the budget
ever tightens.

Four chapters own a single sub-topic each: 12, 17, 25, 33.
