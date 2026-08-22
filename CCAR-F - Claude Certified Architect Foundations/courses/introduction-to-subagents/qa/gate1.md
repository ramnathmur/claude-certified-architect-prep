# GATE 1 — Content Fidelity & Correctness — QA Report

**Course:** Introduction to Subagents (200-level, CCA-F prep)
**Reviewer role:** Independent QA — AI Professor + Senior Research Analyst (adversarial)
**Source of truth:** `source/introduction-to-subagents_source.md`
**Artifact:** `introduction-to-subagents.html`
**Date:** 2026-06-05

---

## 1. Coverage — Section-by-section diff

### Lesson 1 — What are subagents?

| Source element | In HTML? | Notes |
|---|---|---|
| Definition (specialized assistants, own context, returns summary, intermediate steps isolated) | ✅ | Verbatim para (HTML 237) |
| Why subagents matter (finite context, fills up, loses track) | ✅ | Verbatim (242) |
| Two things received: custom system prompt + task description | ✅ | (244–248) |
| Works on its own, only summary returns, conversation discarded | ✅ | (250) |
| Tradeoff: lose visibility into how it reached conclusions | ✅ | Bolded (252) |
| Practical example: refunds, 15 files, Explore subagent | ✅ | (288–290) |
| Built-in: General purpose / Explore / Plan (all 3, exact descriptions) | ✅ | (321–323) |
| Custom subagents (reviewer/test writer/doc generator) | ✅ | (327) |
| Key Takeaways (3 benefits + closing) | ✅ | Collapsible callout (340–349) |

**Lesson 1: ✅ Full coverage.**

### Lesson 2 — Creating a subagent

| Source element | In HTML? | Notes |
|---|---|---|
| Intro (markdown + YAML frontmatter) | ✅ | (396) |
| `/agents` command → Create new agent | ✅ | (399) |
| Scope: Project-level / User-level (exact definitions) | ✅ | (403–404) |
| Recommended: let Claude generate name/description/system prompt | ✅ | (407) |
| 5 tool categories (Read-only / Edit / Execution / MCP / Other) | ✅ | (429–433) |
| Code reviewer needs no edit; keep execution to spot pending changes | ✅ | (435) |
| Model options: Haiku / Sonnet / Opus / Inherit (exact descriptions) | ✅ | (440–443) |
| Color (UI identification) | ✅ | (445) |
| Config path `.claude/agents/your-agent-name.md` | ✅ | (455) |
| **L2 YAML config + system prompt (code block 1)** | ✅ | Reproduced verbatim (458–468) — see §verification |
| Field breakdown (name/description/tools/model/color) incl. `@agent`, `\n`, single-line | ✅ | (471–477) |
| System prompts = body below frontmatter | ✅ | (504) |
| "proactively" for auto-delegation + example | ✅ | (518–519) |
| Testing your subagent | ✅ | (523) |

**Lesson 2: ✅ Full coverage.**

### Lesson 3 — Designing effective subagents

| Source element | In HTML? | Notes |
|---|---|---|
| Four fixes intro | ✅ | (582) |
| How config data is used (name+description in system prompt) | ✅ | (585) |
| Description's second role (shapes input prompt) | ✅ | Bolded (587) |
| Writing descriptions that shape input prompts (get diff / precise files / cite sources) | ✅ | (609–610) |
| Defining output format (2 benefits) | ✅ | (620–624) |
| **6-section structured output format (code block 2)** | ✅ | Verbatim 1–6 (628–640) — see §verification |
| Reporting obstacles (4 bullets) | ✅ | (644–650) |
| **Separate "7. Obstacles Encountered" block** | ✅ | Reproduced as its own `<pre>` (653–656), verbatim |
| Limiting tool access (3 tiers: read-only / reviewer / styling) | ✅ | (672–674) |
| Putting it together (4 characteristics) | ✅ | Ordered list (704–709) |

**Lesson 3: ✅ Full coverage.**

### Lesson 4 — Using subagents effectively

| Source element | In HTML? | Notes |
|---|---|---|
| Core question / intermediate-work framing | ✅ | (765) |
| When subagents shine (3 bullets) | ✅ | (768–773) |
| Research tasks (JWT/auth example) | ✅ | (776) |
| **JWT summary example (code block 3)** | ✅ | Verbatim (779–780) — see §verification |
| Code reviews (fresh eyes, git diff, team standards) | ✅ | (784) |
| Custom system prompts (copywriting + styling) | ✅ | (789–790) |
| When subagents hurt — Anti-pattern 1: Expert Claims | ✅ | Callout (803–804) |
| Anti-pattern 2: Sequential Pipelines | ✅ | Callout (806–807) |
| Anti-pattern 3: Test Runners (+ "performed worst") | ✅ | Callout (809–810) |
| The decision rule ("does the intermediate work matter?") | ✅ | (841) + flowchart |
| Use for / Avoid for lists | ✅ | Table (868–875) |

**Lesson 4: ✅ Full coverage.**

**No MISSING content found. SOURCE coverage = 100% across all 4 lessons.**

---

## 2. Code-block verification (verbatim fidelity)

- **L2 `code-quality-reviewer` YAML + system prompt** — Matches source lines 84–94 exactly: `name`, `description`, `tools: Bash, Glob, Grep, Read, WebFetch, WebSearch`, `model: sonnet`, `color: purple`, and the 3-line system prompt body. ✅
- **L3 6-section output format** — Matches source 132–144 exactly (Summary / Critical / Major / Minor / Recommendations / Approval Status, with identical sub-text and line wrapping). ✅
- **L3 separate "7. Obstacles Encountered"** — Correctly rendered as a *distinct* code block (not merged into the 1–6 block), matching source 156–159 verbatim. ✅
- **L4 JWT summary** — `JWT validation happens in middleware/auth.js line 42, called from the Express router in route/api.js`. Matches source 188–189 verbatim, including the singular `route/api.js` (not pluralized). ✅

All three "source code blocks" are explicitly labeled in the HTML (1 of 3 / 2 of 3 / 3 of 3), aiding traceability.

---

## 3. Correctness findings

No distortions found. Specifically checked:

- **Tool names** — Bash, Glob, Grep, Read, WebFetch, WebSearch, Edit, Write all correctly spelled and correctly assigned to tiers (read-only = Glob/Grep/Read; reviewer adds Bash; modification adds Edit/Write). ✅
- **Model names** — Haiku/Sonnet/Opus/Inherit descriptions match source exactly. ✅
- **Pattern labels** — "Expert Claims," "Sequential Pipelines," "Test Runners" match source naming. ✅
- **Decision rule** — Quoted exactly. ✅
- **Depth (200-level)** — Not flattened. The dual role of `description` (when + what), the "single most important improvement," and the "test runner performed worst of all configurations" nuance are all preserved with their original emphasis.

No correctness defects (BLOCKER/MAJOR/MINOR) identified.

---

## 4. Traceability / anti-hallucination

- **Author analogy** (L1 "intern off to the archives," HTML 239) is explicitly framed: "(Author analogy, not a product fact.)" ✅ Acceptable.
- **SVG diagram labels** use illustrative file names (auth.js, billing.js, RefundService/refund.js, etc.). These are clearly part of the L1 refunds *example* visualization, not asserted product facts. The "RefundService" naming is an illustrative embellishment of the source's refund example — framed inside a figure, acceptable. (MINOR note only, no action required.)
- **Domain weightings** (Domain 1 = 27%, Domain 2 = 20%) — Not from the lesson body but present in the source header (line 6) and the project CLAUDE.md domain map. The HTML correctly frames these as exam orientation ("Treat the mapping as orientation grounded in the source — not extra syllabus"). ✅ Traceable.

### Quiz / MCQ audit (all fresh-authored questions)

Verified every `data-correct` index against the rendered options and against source:

- **Inline quick-checks (4):** L1 Explore (idx1 ✅), L2 body=system prompt (idx2 ✅), L3 Obstacles rationale (idx1 ✅), L4 dependent-bug → main thread (idx0 ✅). All correct, source-grounded.
- **Lesson 1 quiz (Q1–Q4):** correct answers idx 2/1/0/3 — all match source. ✅
- **Lesson 2 quiz:** idx 0/3/1/2 — `/agents`, scope definition, Inherit, "proactively." All match. ✅
- **Lesson 3 quiz:** idx 2/3/0/1 — name+description, output format, Bash-for-reviewer, four characteristics. All match. ✅
- **Lesson 4 quiz:** idx 1/3/2/0 — decision question, fresh eyes, test runners worst, pipeline handoff. All match. ✅
- **Final check (Q1–Q8):** idx 2/1/0/3/1/2/0/3 — summary-only, two inputs, `/agents`→Create, `.claude/agents/...`, description's two jobs, output-format stopping points, read-only=Glob/Grep/Read, research is the non-anti-pattern. All correct and source-grounded. ✅

**No distractor is presented as true.** Every feedback string (`.fbmsg`) explains the correct answer using source-grounded reasoning and, where helpful, correctly characterizes why the distractors are wrong (e.g., distinguishing Explore vs General purpose vs Plan).

No invented flags, commands, or product features detected. The only non-lesson commands shown in distractors (`/subagent new`, `/create-agent`, `/new subagent`, `@agent create`, `~/.config/claude.json`, `package.json`) are clearly presented *as wrong options* and the feedback steers to the correct `/agents` / `.claude/agents/` answer — acceptable.

---

## 5. Findings summary

| Severity | Count |
|---|---|
| BLOCKER | 0 |
| MAJOR | 0 |
| MINOR | 0 (one observational note on SVG illustrative naming — no change required) |

The HTML is a faithful, complete, undistorted rendition of the source. All 4 lessons, all 3 source code blocks (plus the separate Obstacles block), all enumerated concepts (built-in subagents, 5 tool categories, 4 model options, scope, config path, 4 design patterns, 3 tool-access tiers, 3 anti-patterns, decision rule) are present and accurate. All fresh-authored assessment items are source-grounded with correct answer keys.

---

**GATE 1: PASS**
