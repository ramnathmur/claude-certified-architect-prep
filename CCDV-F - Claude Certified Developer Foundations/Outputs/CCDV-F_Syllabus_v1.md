# CCDV-F — Teaching Syllabus

**Exam:** Claude Certified Developer – Foundations
**Source of the blueprint:** `../sources/CCDV-F_Official-Exam-Guide_v1.0.pdf`, v1.0 effective July
2026, pages 5–9. Read directly from the PDF on 2026-08-20, not from a secondary summary.
**Created:** 2026-08-20 · **Status:** ⚠️ **SUPERSEDED 2026-08-22** — see below

> **This syllabus is no longer live.** The teaching material was regenerated from scratch, built blind
> from only the corpus, the published weights, and the exam expectations, without reading this file or
> the 14 classes it produced. Plan of record now:
> `../Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md`. Kept here as a historical record, not as
> the current teaching plan — do not build on it or resume Class 15 from where this left off.

> Re-check against the guide quarterly. v1.0 is the initial publication and states it is "subject to
> change without notice." If the blueprint moves, this syllabus moves with it.

---

## 1. What the exam asks

> **Exam mechanics are not repeated here.** Item count, time limit, pass mark, book policy, retake
> rules and result reporting live in `../EXAM-FACTS_v1.md`, which is the single source of truth for
> them. This file carries the teaching plan only.

Every sample item in the guide is a short scenario stating a constraint, followed by four options that
are all legitimate techniques — only one of which fits the constraint. No code appears in any sample,
and none is asked for. The candidate selects; the candidate never produces.

**That decides how this syllabus is taught.** Classes state a decision and the thing that discriminates
between the options. Code appears in a class only where the decision is *about* the code — schema
shape, defensive parsing, error-handling strategy — and even there the question is which approach, not
what the parameter is called.

---

## 2. The blueprint — 8 domains, 25 skills

Weights are the guide's own. Skill weights sum exactly to their domain; domains sum to 100.0. Both
checked.

> **`../EXAM-FACTS_v1.md` is the source of truth for these weights.** They are reproduced here because
> a skill→class map is unreadable without them. If the guide bumps past v1.0, update `EXAM-FACTS_v1.md`
> first and this file second — never the other way round.

### Domain 1 — Agents and Workflows · 14.7%

| Skill | Weight | Class |
|---|---|---|
| Agent Architecture | 4.5% | 18 |
| Agent Construction with Claude | 5.3% | 21 |
| Agent Patterns and Frameworks | 4.9% | 19, 20 |

### Domain 2 — Applications and Integration · 33.1%

| Skill | Weight | Class |
|---|---|---|
| Claude Application Design | 8.6% | 1, 2, 3 |
| Software Engineering Foundations | 7.4% | 24 |
| Claude API Mechanics | 6.8% | 12, 13 |
| Configuration Management | 4.1% | 4 |
| Understanding Requirements | 3.4% | 22 |
| Systems Life Cycle | 2.8% | 23 |

### Domain 3 — Claude Code · 3.1%

| Skill | Weight | Class |
|---|---|---|
| Claude Code Operation | 3.1% | 5 |

### Domain 4 — Eval, Testing, and Debugging · 2.6%

| Skill | Weight | Class |
|---|---|---|
| Debugging and Error Handling | 2.6% | 17 |

Despite the domain title, the guide names **no eval-design skill**. The only examinable skill here is
debugging and error handling — error type identification, recovery strategy selection, trace analysis,
and isolating problem origin between the integration layer and model output.

### Domain 5 — Model Selection and Optimization · 16.8%

| Skill | Weight | Class |
|---|---|---|
| Technical Fundamentals | 6.1% | 9 |
| LLM Fundamentals | 5.2% | 6, 7 |
| Cost and Token Management | 2.8% | 14 |
| Model Selection and Tradeoffs | 2.7% | 8 |

### Domain 6 — Prompt and Context Engineering · 11.0%

| Skill | Weight | Class |
|---|---|---|
| Prompt Engineering | 4.6% | 10 |
| Context Engineering | 3.8% | 11 |
| Output Handling | 2.6% | 16 |

### Domain 7 — Security and Safety · 8.1%

| Skill | Weight | Class |
|---|---|---|
| AI Application Security | 3.2% | 25 |
| Guardrails and Safe Deployment | 2.3% | 26 |
| Identity, Secrets, and Key Management | 1.6% | 27 |
| Claude Hooks | 1.0% | 26 |

### Domain 8 — Tools and MCPs · 10.6%

| Skill | Weight | Class |
|---|---|---|
| Tool Implementation | 4.4% | 15 |
| Agentic Customization | 4.1% | 28 |
| MCP Server Development | 2.1% | 29 |

---

## 3. The class sequence

Ordered by dependency, not by weight. Caching cannot be judged before tokens are understood, and agent
architecture cannot be judged before a tool loop has been seen to run.

**Every class names the one idea it derives from.** That column is not decoration — it is clause 1 of
the teaching contract in section 6. A class without a central idea becomes a list of topics, which is
what the first version of Class 1 was and why it was rejected. If a class cannot state its idea in one
sentence, the class is not designed yet.

### Application shape — classes 1-5

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 1 | Whose hands: where instructions live and what changes across surfaces | Claude is text-in, text-out, running on someone else's computer. An instruction is text you got into a finite window; a capability is whatever the machine at the far end can touch | ✅ 2026-08-20 |
| 2 | Session hygiene: what an agent knows when a new session starts | Memory scope is a design-time decision about what survives the window being erased. Every scope trades token cost against reach, and choosing late costs more than choosing early | ✅ 2026-08-20 |
| 3 | Content boundaries and schema design | The shape you ask for decides whether a wrong answer is detectable. A schema is a contract you can check without trusting the thing that filled it | ✅ 2026-08-20 |
| 4 | Configuration management: plugins, model pinning, prompt versioning, dependencies | Configuration is the record of which version of everything produced a given result. Without pinning, a run is not reproducible and a regression is not attributable | ✅ 2026-08-20 |
| 5 | Claude Code operation | Claude Code is a harness with a permission model. Every feature in it is a way of controlling what enters the window, or what the hands are allowed to do | ✅ 2026-08-20 |

### How the model behaves — classes 6-9

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 6 | Tokens, context windows, sampling, non-determinism | The model predicts one token at a time from everything in the window. Non-determinism is sampling working as designed, not the system failing | ✅ 2026-08-21 |
| 7 | Reasoning modes and prompting modes | Thinking is tokens spent before answering. Effort is a dial on how many, and it pays only where the task has a search space to explore | ✅ 2026-08-21 |
| 8 | Choosing a model | Capability, latency and cost are one budget with three names. Choosing a model is deciding how to spend it, and a new release can move the exchange rate | ✅ 2026-08-21 |
| 9 | The technical substrate: SDKs, REST, websockets, async | An SDK is a typed wrapper over an HTTP request. Everything it hides is still happening, and the things that break are in the part it hid | ✅ 2026-08-21 |

### Getting good output — classes 10-14

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 10 | Prompt engineering | The model sees one flat text. Position is as load-bearing as wording, because position is how the text tells the model what is authoritative and what is data | ✅ 2026-08-21 |
| 11 | Context engineering | The window is a working set you curate, not a log you append to. Everything you leave in it is re-read and re-charged on every turn | ✅ 2026-08-21 |
| 12 | Messages API mechanics | Every feature on the API is a way of getting more into the window, more out of it, or the same thing more cheaply | ✅ 2026-08-21 |
| 13 | Batch against realtime, and Claude through third parties | Latency tolerance is the axis. If nobody is waiting for the answer, speed is something you are paying for and not using | ✅ 2026-08-21 |
| 14 | Cost and token management | Cost is tokens times price times turns. Caching attacks the first term by making an unchanged prefix nearly free to resend | ✅ 2026-08-21 |

### Tools — classes 15-17

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 15 | Tool implementation | A tool description is a prompt. Tools are selected the same way skills are — by prediction over the text in the window, not by a lookup | ⬜ |
| 16 | Output handling | Model output is untrusted input from a confident stranger. Confidence in the text carries no information about whether it is right | ⬜ |
| 17 | Debugging and error handling | A failure lives in one of three places: what you sent, what came back, or what you did with it. Isolate which before changing anything | ⬜ |

### Agents — classes 18-21

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 18 | Workflow or agent | You buy an agent when you cannot enumerate the steps in advance. You pay for it in determinism, and that is the whole trade | ⬜ |
| 19 | Agent patterns | Every agent pattern is a way of keeping the window small while the task stays big | ⬜ |
| 20 | Abstraction frameworks: Strands, LangGraph, PydanticAI | A framework is somebody's opinion about the loop, made concrete. Choose by which opinion matches your architecture | ⬜ |
| 21 | Building with the Agent SDK | The loop is the product. Hooks are where you put the things too important to leave to a prediction | ⬜ |

### Solution and engineering work — classes 22-24

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 22 | Requirements from a business brief | A requirement becomes testable at the moment it names a constraint. Until then it is a preference | ⬜ |
| 23 | Systems life cycle | The cost of a decision rises with how late it is made. Life-cycle frameworks exist to move decisions earlier | ⬜ |
| 24 | Software engineering foundations as this exam frames them | The exam tests these as judgement under constraint, the same as everything else — not as definitions | ⬜ |

### Security — classes 25-27

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 25 | AI application security | Any text the model read is untrusted, whoever fetched it. The boundary that matters is between instructions you wrote and text that arrived | ⬜ |
| 26 | Guardrails, layering, least privilege, hooks | A control the model can choose to ignore is not a control. Enforcement has to sit outside the thing being constrained | ⬜ |
| 27 | Identity, secrets and key management | An agent's blast radius equals the credentials it holds, not the instructions it was given | ⬜ |

### Reusability — classes 28-29

| # | Class | The idea it derives from | Status |
|---|---|---|---|
| 28 | Built-in tools against custom tools against skills against MCP servers | Choose by who maintains it and how many applications need it, not by which is most capable | ⬜ |
| 29 | MCP server development | MCP turns a capability into an independently versioned service instead of a feature of one application | ⬜ |

**Delivered classes are saved twice.** `classes/CCDV-F_Class-NN_v1.md` is the plain-text transcript;
`classes/html/CCDV-F_Class-NN.html` is the reading edition, and `classes/html/index.html` is the course
hub that links them.

**The HTML is the canonical reading artifact.** It is paged one idea per screen, carries hand-authored
SVG diagrams the markdown cannot, and holds the checkpoint reveals. The markdown transcripts predate it.

> ⚠ **Open decision.** Two formats for one class is the stale-duplicate pattern this project has been
> bitten by before. Either the markdown transcripts get retired, or every future edit has to land in
> both. Not yet decided — raised 2026-08-20.

---

## 4. Coverage check

Twenty-nine classes covering all 25 published skills. Every skill has at least one class. No class
teaches material outside the blueprint.

The one deliberate omission: **"Accelerators & IP Contribution,"** 155 minutes of the official prep
path, maps to no domain and no skill in the blueprint. It is partner enablement. It is not taught here.

---

## 5. Where the time goes

**13.6% of the paper is not Claude-specific.** Software Engineering Foundations (7.4), Understanding
Requirements (3.4) and Systems Life Cycle (2.8) come to roughly seven items on REST, JSON, async,
version control, SDLC, code review, refactoring, requirements analysis and life-cycle frameworks.
Classes 22–24 shape that material into exam form rather than teaching it.

**Claude Code is 3.1% of the paper** — one or two items. The official prep path teaches it at length
because most of the material is redistributed into application design and agents, where it is tested.
One class, not five.

**The genuinely new ground** is Claude Application Design, the four security skills, Agent Construction
with the Agent SDK, and Technical Fundamentals. That is where class time concentrates.

---

## 6. How classes run

- Concepts are taught first. Mock papers come after the teaching, not interleaved with it. Sitting a
  paper on untaught material measures nothing and burns the item pool.
- Each class ends with one understanding check answered in the student's own words. The reasoning is
  the diagnostic; a letter alone shows nothing.
- No section numbers, no source citations, no weightings inside the teaching itself. Those live here.

### The teaching contract

Set 2026-08-20 after the first version of Class 1 was rejected as dry and textbookish, and after two
commissioned reviews — one from a student persona, one from an AI-professor persona — independently
found the same defect: the class stated rules instead of deriving them, so the student finished knowing
*that* four surfaces behave differently and unable to derive a single cell without the table in front
of them.

**Classes are taught the way Feynman taught. The rule is derived until it becomes obvious, never
announced and defended.**

1. **One idea per class, stated early.** Everything else is that idea seen from another angle. A class
   organised as a list of topics is a reference page with paragraph breaks.
2. **Show the constraint before the rule.** The test of a derivation: could the student answer a
   question about a case the class never covered? If the answer is no, a fact was delivered instead of
   a mechanism.
3. **Analogies carry the full load or they are cut.** At least one drawn from outside software, chosen
   so it also covers the hard part of the class rather than only the easy opening. An analogy used once
   and abandoned before the difficult section is decoration.
4. **Tie every mechanism back to how the machine actually works** — the model runs on Anthropic's
   hardware and never on the student's, the API keeps no memory between calls, the context window is
   finite and re-read every turn, and loading decisions are predictions rather than lookups.
5. **Separate what is forced from what is a convention.** That a delegate cannot exceed its delegator
   is close to a security invariant. That a settings default is off, or that a file is spelled a
   particular way, is this release's choice. Uniform reverence teaches the student to spend memory in
   the wrong places.
6. **Name the vocabulary.** The paper is closed book and multiple-choice, and its distractors are named
   mechanisms. A student given the concept and denied the setting name cannot pick it out of a lineup.
7. **Narrative budget follows exam weight.** The first version spent multiple paragraphs on one war
   story and twelve table cells on the highest-value discrimination in the class. Reverse that.
8. **The prose bans in the global instructions still hold** — no invented misconception set up only to
   be knocked down, no "that is not X, that is Y" cadence for plain facts, no isolated dramatic
   one-liners, each idea said once in each register.

### The voice — added 2026-08-20, second correction

The derivations were right and the language was still wrong. Ram's diagnosis, quoting the offending
paragraph back at me: *"A path written in a file is an unresolved reference — a promise that some name
will mean something later. Copying bytes resolves nothing. Resolution happens at run time, against a
namespace that exists on one particular machine."* His verdict: textbookish and abrupt, not a person
teaching.

He is right, and the fault is a specific and fixable one. That paragraph is built from abstract nouns —
*reference, resolution, namespace, run time* — where it should be built from things you can picture. It
also states the idea once, densely, and moves on, which reads as abrupt because the reader gets no
second angle on it.

**Write the way Feynman lectured.**

- **Plain words.** If a nine-year-old would need the word explained, either explain it or find another
  word. Say the idea first in ordinary language, then name the jargon: *"they call it late binding, but
  all it means is that nobody checks the directions until somebody tries to walk them."*
- **Nouns you can picture, verbs that do something.** Not *"resolution happens against a namespace."*
  Rather: *"the computer goes looking for that folder, and on your machine it's there, and on mine it
  isn't."*
- **Talk to the student.** Second person. Ask questions out loud and answer them. Say "now", "look",
  "here's the thing" — the connective tissue that stops a class reading as a list.
- **Say the important ideas twice, from different angles.** Once as a picture, once as the mechanism.
  This is not the repetition the prose bans forbid — that ban is about re-performing the same sentence
  for effect. Explaining the same idea a second way is how teaching works.
- **Give the idea room.** The complaint "abrupt" means points arriving without setup and leaving
  without landing. Build up to the hard part, then sit on it.
- **Cut most of the formatting.** Bold on every third phrase, a callout box per paragraph, a table
  where a sentence would do — all of it reads as documentation. Prose carries a class. A summary table
  is fine at the *end* of a section, after the reasoning has already happened.
- **Say what you don't know, and what is arbitrary.** Feynman's habit, and it teaches the student where
  to spend memory.
- Alongside the classes, **one built application**, exercising the API, at least one tool, prompt and
  context engineering, and basic security and evaluation practices. The guide asks for one application,
  not a portfolio. It gives the tool and agent classes something concrete to argue about.

---

## 7. What the guide recommends, quoted in substance

There is no required course, and Anthropic does not guarantee any resource ensures a pass. The guide
asks candidates to study the blueprint and self-assess against each objective, review the official
documentation for the Claude API, models, prompt engineering, Claude Code, Skills and MCP, build and
operate at least one Claude application, practise the developer competencies directly, and work the
sample questions to learn the item style.

---

## 8. Related files

| Question | File |
|---|---|
| Exam mechanics | `../EXAM-FACTS_v1.md` |
| Current standing and scores | `../prep with quiz/EXAM-LOG.md` |
| What study material exists | `../BACKGROUND-MATERIAL-INDEX_v1.md` |
| Phases and gates | `../ROADMAP.md` |
| Corpus structure and section numbering | `../prep with quiz/CCDV-F_Corpus-Index_v1.md` |
