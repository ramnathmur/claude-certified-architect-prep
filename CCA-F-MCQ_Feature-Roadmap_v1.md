# MCQ Practice App — Feature Roadmap v1
**Status:** Advisory report  
**Date:** 2026-06-06  
**Scope:** Post-answer learning uplift + option quality QA + prioritized v2 roadmap  

---

## Section 1 — Post-Answer Learning: Research Findings

### Platform-by-Platform Evidence

**Whizlabs** — the clearest commitment found:
> "Explanations cover not only the correct options but also the incorrect options — to understand why particular options are incorrect."  
Per-distractor explanation is explicit and confirmed in product copy. Every wrong answer gets its own rationale, not a combined paragraph.

**Tutorials Dojo** (has a CCA-F-specific practice set at $4.99):  
- Review Mode: per-question explanations covering the correct answer and each distractor  
- Reference links to official Anthropic / AWS documentation accompany every question  
- Section-Based mode: filter by domain before the session  
- End-of-session domain weakness report  
- "Retake wrong answers only" filter — manual quasi-adaptive loop (not algorithmic)

**AWS Skill Builder** (official):  
- "Review Answer" per-question toggle (don't wait until end of session)  
- Recommends documentation links alongside each question  
- Per-option breakdown language is ambiguous in docs — may be aggregate, not per-distractor  

**ExamTopics**:  
- No structured explanation — community comments only  
- Unreliable for niche certifications; not a model to follow

### Patterns That Appear on Every Serious Platform

| Pattern | Present at |
|---|---|
| Correct-answer rationale | All serious platforms (universal) |
| Per-distractor wrong-answer explanation | Whizlabs (explicit), Tutorials Dojo (Review Mode) |
| Reference links to official docs | Tutorials Dojo, AWS Skill Builder, Whizlabs |
| Topic/domain filtering before session | Universal |
| "Retake wrong answers" filter | Tutorials Dojo, most paid platforms |
| Domain weakness report (end-of-session) | Tutorials Dojo, Whizlabs |
| Algorithmic spaced repetition | **No major cert platform does this** — gap filled only by Connectry-io CCA-F MCP tool |
| Difficulty rating per question | Not prominently surfaced post-answer on any platform reviewed |

### Key Takeaway for This App

The current app already has the end-of-session domain breakdown and wrong-answer review section — both are best-practice features. The single largest gap versus platforms like Whizlabs and Tutorials Dojo is **per-distractor explanation**: explaining WHY each of the three wrong options is wrong, not just the one most commonly chosen.

---

## Section 2 — CCA-F MCQ Option Quality: Research Findings

### Confirmed Exam Structure
- 60 questions, 120 minutes, scaled score 720/1000 to pass  
- One correct answer, three distractors (no confirmed multi-select in current exam)  
- Questions anchored to 4 of 6 randomly assigned scenario pools per sitting  
- Exam results include domain-level breakdown, not per-question explanations

### The 6 Scenario Pools (confirmed from community sources)
1. Customer Support Resolution Agent  
2. Claude Code Configuration for a development team  
3. Multi-Agent Research System (coordinator + subagents)  
4. Developer Productivity Tools (Claude Code built-ins + MCP)  
5. CI/CD Pipeline Automation (headless, `--output-format json`, `-p` flag)  
6. Structured Data Extraction (JSON schema, nullable fields, batch processing)

### How Answer Choices Are Constructed (confirmed from sample question)

Confirmed sample question paraphrased:  
> *Refactoring a monolith into microservices across dozens of files. Which Claude Code approach is most appropriate?*  
> A) Enter plan mode, explore codebase, design before making changes ← correct  
> B) Start with direct execution, let implementation reveal service boundaries  
> C) Use direct execution with exhaustive upfront instructions for every service  
> D) Start in direct execution, switch to plan mode only if unexpected complexity arises  

Note: B, C, and D are all execution-first approaches, differentiated by degree of upfront specification — none is obviously absurd. This is the CCA-F signature pattern: **architectural trade-off questions where all options are plausible to a developer who has studied the domain.**

### Confirmed Distractor Typology (7 categories)

| # | Type | Description |
|---|---|---|
| 1 | Anti-pattern mistaken as pattern | Raw transcript passed as context; feels efficient, is a context-window anti-pattern |
| 2 | Correct concept, wrong scope | Applying a project CLAUDE.md rule where a global or CI-level config is required |
| 3 | Correct tool, wrong mode | Using direct execution instead of plan mode for complex multi-file architectural work |
| 4 | Assumed shared state | Treating multi-agent systems as sharing context automatically |
| 5 | Prompt-only when schema required | Trusting prompt instructions alone for structured JSON output |
| 6 | Interactive mode in CI/CD | Running Claude interactively in a pipeline instead of headless with `-p` |
| 7 | Sequential where parallel applies | Missing parallelization opportunities in multi-agent orchestration |

### Question Type Distribution (from community evidence)
- ~90%+ scenario-based architectural decisions  
- Small number of conceptual boundary questions (e.g., MCP resources vs. tools vs. prompts)  
- No pure definition-recall questions reported by exam-takers  
- Exam officially described as "tests trade-offs, not rote definitions"

### What Available Question Banks Do
- **Tutorials Dojo CCA-F** ($4.99): per-option explanation + reference links — closest model to follow  
- **CertLand**: claims per-distractor coverage explicitly  
- **Connectry-io MCP tool** (GitHub): 390 questions, spaced repetition built in, runs inside Claude Code — worth examining as a comparison point  
- **daronyondem/claude-architect-exam-guide** (GitHub): teaching-oriented guide, not a question bank; useful for domain concept framing

---

## Section 3 — Gap Analysis

| Area | Current App Behaviour | Best Practice | Gap Severity |
|---|---|---|---|
| **Correct-answer rationale** | Present — 1–2 sentences on why correct answer is right | Universal standard | ✅ Met |
| **Per-distractor explanation** | One wrong answer addressed ("wrong answer chosen most often") | All 3 wrong options explained individually (Whizlabs, Tutorials Dojo) | 🔴 High |
| **Distractor typology in generation** | Prose quality rules per difficulty level (A/B) but no named distractor categories | 7 confirmed CCA-F distractor types should guide option construction | 🔴 High |
| **Reference links** | None | Official doc links with every question (Tutorials Dojo, AWS Skill Builder) | 🟡 Medium |
| **Concept/topic tag per question** | None | Topic tags allow post-session targeted review | 🟡 Medium |
| **Scenario pool anchoring** | Full-exam and per-domain modes only | CCA-F questions are anchored to 6 named scenario pools — training should reflect this | 🟡 Medium |
| **QA layer for option plausibility** | None — Claude self-generates and no validation step | All 4 options must be plausible to a trained developer; obvious distractors undermine exam realism | 🔴 High |
| **"Retake wrong answers" filter** | Wrong-answer review section exists at end (read-only) | Interactive retake mode for all incorrect questions in one pass | 🟡 Medium |
| **Domain weakness report** | Collapsible domain breakdown panel in header during session | End-of-session domain breakdown — present in summary | ✅ Met |
| **Adaptive ordering / spaced repetition** | None | No major cert platform has it built-in; Connectry-io MCP is the only CCA-F implementation | 🟢 Low (not standard) |
| **Difficulty rating per question** | Not surfaced | Not prominently surfaced on most platforms either | 🟢 Low |
| **Time-pressure mode** | None | Not standard on platforms but useful for exam simulation | 🟢 Low |
| **Stems deduplication** | Present — stems log with last 50 injected into prompt | Not a standard platform feature; app already ahead | ✅ Ahead of market |
| **Offline HTML output** | Present — fully self-contained | Not standard; most platforms require login | ✅ Ahead of market |

---

## Section 4 — Prioritized Feature Roadmap

**Constraint:** All P1 features buildable within existing stack (Python, Claude Code CLI, Jinja2). P1 = completable in one focused session under 4 hours.

---

### P1 — Do First (exam fidelity and post-answer learning gaps)

#### P1-A: Per-Distractor Explanation Schema

**What it does:** Expand the `explanation` field from a single combined string to a structured object with `correct_rationale` (why the right answer is right) and `why_wrong` (one sentence per wrong option, keyed by letter). The HTML session displays all four rationales after submission.

**Why it matters:** The single highest-impact gap. Whizlabs and Tutorials Dojo both do this; it is how learners understand *why they were wrong*, not just *that they were wrong*. For CCA-F specifically — where all 4 options are plausible — understanding each distractor is the learning.

**Implementation type:** Prompt change + HTML-JS change  
**Effort:** M (prompt schema update, JSON parsing adjustment in html_renderer, HTML card layout for 4 rationale blocks)

**Prompt change (add to output format section in `prompt_builder.py`):**
```
"explanation": {
  "correct_rationale": "<why correct_answer is right — 1-2 sentences>",
  "why_wrong": {
    "<letter of wrong option 1>": "<why this option is wrong — 1 sentence>",
    "<letter of wrong option 2>": "<why this option is wrong — 1 sentence>",
    "<letter of wrong option 3>": "<why this option is wrong — 1 sentence>"
  }
}
```

---

#### P1-B: Distractor Typology Injection (Anthropic-Grade Mode)

**What it does:** For difficulty `A`, inject the 7 confirmed CCA-F distractor types into the prompt builder's distractor quality section. Each question's wrong options must collectively represent 2–3 of the 7 types, named explicitly. Claude constructs options that match real exam distractor patterns.

**Why it matters:** Current distractor rules say "must be wrong for a specific architectural reason" — correct direction but vague. The 7 types are confirmed from exam community evidence; baking them in makes generated questions structurally faithful to the actual exam.

**Implementation type:** Prompt change only  
**Effort:** S (add a constant to `prompt_builder.py`, inject into `_distractor_instructions("A")`)

**The 7 types to inject:**
1. Anti-pattern mistaken as pattern  
2. Correct concept, wrong scope  
3. Correct tool, wrong mode  
4. Assumed shared state  
5. Prompt-only when schema required  
6. Interactive mode in CI/CD context  
7. Sequential where parallel applies

---

#### P1-C: Concept Tag per Question

**What it does:** Add a `concept_tags` field to the JSON schema — a list of 1–3 reusable pattern names (e.g., `["context window management", "multi-agent handoff", "plan mode selection"]`). Tags appear as chips on each question card in HTML. Post-session summary shows which concept areas had the most wrong answers.

**Why it matters:** Transforms the wrong-answer review from a list of missed questions into a diagnostic of which *architectural concepts* need attention. Directly supports the CLAUDE.md learning principle of pattern naming.

**Implementation type:** Prompt change + HTML-JS change  
**Effort:** M (prompt schema, Jinja2 template chip rendering, summary page aggregation by concept tag)

---

#### P1-D: Interactive Retake Mode

**What it does:** "Retry Wrong Answers" button on the summary page generates a new mini-session pre-loaded with only the questions from the current session that were answered incorrectly. The mini-session runs fully interactively within the same HTML file — no new Claude call needed, data is already in the page.

**Why it matters:** The wrong-answer review section currently shows answers read-only. The learning loop closes only when the learner can re-attempt under the same conditions. Tutorials Dojo's "retake wrong answers" filter is one of the most-cited quality features by learners.

**Implementation type:** HTML-JS change only  
**Effort:** M (filter `selectedAnswers` for incorrect, reset state for filtered subset, render second pass in same UI)

---

#### P1-E: Option Quality QA Pass

**What it does:** After Claude generates questions (in `mcq_launcher.py`), a second Claude call validates each question against a short rubric: (1) Are all 4 options plausible to a developer who studied the domain? (2) Are wrong options distinct from each other — not near-duplicates? (3) Does the stem unambiguously identify one correct answer? Questions that fail 2 of 3 checks are flagged; a warning is printed and flagged questions are optionally excluded from the session.

**Why it matters:** The generation prompt sets quality rules but Claude has no self-auditing layer. A lightweight validation pass catches the cases where a distractor is obviously wrong (undermining Anthropic-Grade fidelity) or where two wrong options are so similar they're effectively one choice.

**Implementation type:** New Python module (`src/qa_validator.py`) + integration hook in `mcq_launcher.py`  
**Effort:** L (new module, second `_call_claude` invocation with a validation prompt returning a JSON flags array, integration, optional exclusion logic)

---

### P2 — Do Second (quality depth and study continuity)

| Feature | What | Why | Implementation Type | Effort |
|---|---|---|---|---|
| **P2-A: Scenario pool mode** | Add a 3rd scope option: choose one of the 6 CCA-F scenario pools; all questions are anchored to that scenario context | Exam questions are scenario-anchored; practicing by scenario pool is the most realistic training mode | Prompt change + collect_config update | M |
| **P2-B: Reference links** | Add an optional `reference_url` field; render as "Read more →" link in HTML after explanation | Tutorials Dojo includes this on every question; connects learning to official source of truth | Prompt change + HTML | S |
| **P2-C: Cross-session wrong-answer tracking** | Persist a `data/missed.json` with question stems + domain of every wrong answer; show running total at session start | Enables targeting of persistent weak areas across sessions, not just within a session | New Python module | M |
| **P2-D: Printable session summary** | "Print / Save PDF" button produces a clean print stylesheet version of the summary + wrong-answer review | Paper-based review between sessions; offline study without reopening HTML | HTML-JS change | S |

---

### P3 — Future (significant scope, not P1 constraint-compatible)

| Feature | What | Why | Implementation Type | Effort |
|---|---|---|---|---|
| **P3-A: Leitner spaced repetition** | Algorithmically schedule questions into boxes; promote on correct answer, demote on wrong; session surfaces due questions | The only CCA-F resource doing this is Connectry-io MCP (390 questions); fills the market gap entirely | New Python module (substantial) | XL |
| **P3-B: Time-pressure mode** | Visible countdown timer per question; 2 min/question exam pace; auto-submit on expiry | Exam simulation fidelity; trains pacing as well as recall | HTML-JS change | M |
| **P3-C: Diagnostic report export** | After N sessions, generate a Markdown/HTML study report: domain scores over time, concept tags most missed, recommended focus areas | Longitudinal progress tracking; turn the app into a full study dashboard | New Python module | L |

---

## Recommended Sequencing

```
Week 1: P1-B (distractor typology) → P1-A (per-distractor explanation) → P1-D (retake mode)
Week 2: P1-C (concept tags) → P1-E (QA validator)
Week 3: P2-A (scenario pool mode) → P2-C (cross-session tracking)
Later:  P2-B, P2-D, then P3 items as exam date approaches
```

Start with P1-B because it is prompt-only (lowest risk, immediate fidelity uplift) and it makes P1-A better — the per-distractor explanations will naturally reference the named distractor type when the typology is already baked into generation.
