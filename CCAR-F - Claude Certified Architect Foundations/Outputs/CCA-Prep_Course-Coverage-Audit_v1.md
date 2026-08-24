# CCA-F Course Coverage Audit

**Date:** 2026-08-10
**Question asked:** are the Anthropic Academy courses covered by our corpus, and should the missing ones be added?
**Verdict:** **no additions recommended.** 1 of 7 official prep courses is in the corpus, but the corpus is grounded on a higher authority (the official Exam Guide v1.0) and is already complete against that guide's in-scope whitelist. Four genuinely-absent items are listed in §5 for your call.

**Method and its limits.** I read Skilljar **catalog pages only** — course titles, learning objectives, section headings, lesson counts. I did **not** enrol in, open, or download any course. Professional-path modules are gated ("Complete prior courses in this path to access this course"), so their lesson-level content was not observable. Every claim below traces to a catalog page or a corpus file line. Nothing was written to the corpus.

---

## 1. The page that prompted this is a different exam

The URL reviewed was `anthropic-partners.skilljar.com/path/claude-certified-architect-**professional**`. The site's Certifications menu lists four distinct credentials: Associate–Foundations, Architect–Foundations, Developer–Foundations, and Architect–**Professional**.

Its five modules, none in the corpus:

| Module | Length |
|---|---|
| Claude Platform & Solution Design | 238 min |
| Enterprise Integration & Production | 158 min |
| Responsible AI, Safety & Risk for Architects | 114 min |
| Stakeholder Engagement, Lifecycle & GTM | 178 min |
| Team Enablement & Operational Productivity | 45 min |
| **Total** | **733 min (~12.2 h)** |

Stated prerequisites: Claude 101, Claude Code in Action, AI Fluency.

**Assessment:** correctly absent. Stakeholder discovery, GTM, lifecycle and team enablement are not tested by any of the five CCA-F domains. This is next-certification material, and if pursued it needs its own corpus and its own exam guide — not an extension of this one.

---

## 2. The list that actually matters

Separate official page: `/page/claude-certified-architect-foundations-prep-courses`. Anthropic lists **seven** prep courses for your exam.

| # | Course | In corpus? |
|---|---|---|
| 1 | AI Fluency: Framework & Foundations | ✗ |
| 2 | Building with the Claude API | ✗ |
| 3 | Claude on Google Cloud | ✗ |
| 4 | Claude Code in Action | ✗ |
| 5 | **Claude 101** | ✅ `courses/claude-101/` |
| 6 | Claude with Amazon Bedrock | ✗ |
| 7 | Introduction to Model Context Protocol | ✗ |

Also note: **Introduction to Subagents**, which the project did build, is *not* on the official prep list.

`courses/COURSE-ROADMAP.md` queued four courses (Agent Skills, MCP, Claude API, Claude Code in Action) and shipped none of them. It never listed AI Fluency, Google Cloud, or Bedrock at all.

---

## 3. Why "not in the corpus" is not the same as "a gap"

The corpus's source-authority chain (`CCA-Prep_Corpus-Index_v2.md:4-7`) is:

1. `CCA-F-Official-Exam-Guide_v1.0.pdf` — the official guide
2. Live Anthropic documentation
3. Community study guide — depth only, not authoritative

Prep courses are not on that chain, and they outrank nothing on it. The guide carries two lists the corpus treats as binding: an **in-scope topic whitelist** plus a Technologies appendix, and a **16-item out-of-scope list** the exam generator holds as a hard constraint (`CCA-Prep_Exam-Mechanics_v2.md:119-136`).

Three of the six missing courses teach material that list explicitly excludes:

> **Cloud-provider-specific configurations (AWS, GCP, Azure)** — `Exam-Mechanics_v2.md:133`

That single line disqualifies **Claude on Google Cloud** and **Claude with Amazon Bedrock** outright. Two of Anthropic's own seven prep courses teach content its own exam guide says will not be tested.

**Building with the Claude API** hits three more exclusions. Its seven sections include *Retrieval augmented generation* (hybrid search, reranking), *Claude Code & Computer Use*, and a streaming objective — against these out-of-scope entries:

> Embedding models or vector database implementation details
> Computer use (browser automation, desktop interaction)
> Streaming API or server-sent events

Its remaining sections — prompt engineering & evaluation, tool use, MCP, agents and workflows — map onto D4, D2 and D1, which the corpus already covers at 20, 9 and 18 sections respectively.

---

## 4. Course-by-course verdict

### AI Fluency: Framework & Foundations
Two sections; "AI Fundamentals & Framework" is 10 lessons introducing the **4D Framework** (Delegation, Description, Discernment, Diligence) and the capabilities/limitations of generative AI.
**Verdict: already captured, no action.** The 4D Framework is present in `courses/claude-101/source/claude-101_source.md` and surfaces in the concept ledger. It appears nowhere in the guide's Technologies appendix — it is conceptual framing, not tested content.

### Building with the Claude API
Seven sections: Getting started · Prompt engineering & evaluation · Tool use · RAG · MCP · Claude Code & Computer Use · Agents and workflows.
**Verdict: 3 of 7 sections explicitly out of scope; the other 4 are already corpus-covered. No action.**

### Claude on Google Cloud · Claude with Amazon Bedrock
**Verdict: do not add.** Barred by the out-of-scope list. Ingesting them would risk the generator producing questions the exam cannot ask, in a corpus currently producing 54/60.

### Claude Code in Action
Four sections (Steer the Work · Configure Claude · Automate Repeat Work · Verify and Share), eight objectives. Maps hard onto D3 (20% of the paper).
Objectives already covered: plan mode and `/compact` (D3 §3.6, §3.12) · lean CLAUDE.md and instruction surfaces (§3.1, §3.2, §3.11) · skills as packaged procedures (§3.3) · headless runs with structured output (§3.8, §3.9).
**Verdict: mostly covered — but this is the one course carrying genuine candidates (see §5).**

### Introduction to Model Context Protocol
16 lessons across 2 sections. Objectives centre on building MCP **servers and clients in Python**, the **MCP Inspector**, async communication and resource cleanup. Prerequisites are Python and async/await.
Only one objective is exam-shaped — *"choose between tools, resources, and prompts based on control patterns"* — and the corpus already holds it at D2 §2.6 (three MCP primitives; resources as catalogs, tools as actions).
**Verdict: no action.** The rest is implementation, barred twice over:
> Deploying or hosting MCP servers (infrastructure, networking, containers)
> Language/framework-specific implementation details (beyond tool/schema config)

---

## 5. The four genuine candidates — your call

Absent from the corpus, verified by grep across `CCA-Prep_Domain-*_v2.md`, `Exam-Mechanics_v2.md` and `Key-Distinctions_v1.md`. None appears in the guide's Technologies appendix, which is why I am flagging rather than adding.

| # | Topic | Source | Corpus | In Technologies appendix? | Read |
|---|---|---|---|---|---|
| 1 | **git worktrees** for safe parallel agents | Claude Code in Action | absent | no | Likely out of scope — a git feature, not a Claude one |
| 2 | **Permission modes** (`acceptEdits`, `bypassPermissions`) | Claude Code in Action | absent | no | Adjacent to `allowed_tools`, which *is* in scope and heavily covered (D1 §1.3, §1.11). Plan mode is covered at §3.6 |
| 3 | **Hook permission-decision JSON + exit codes** | Claude Code in Action | absent | hooks yes, mechanism no | Hooks are in scope (D2 §2.7); the exit-code contract is implementation-level and likely excluded |
| 4 | **Routines / scheduled prompts** | Claude Code in Action | partial — "routine" appears in D3 | no | Weakest candidate; newer surface than the guide |

My recommendation: **add none of them before you sit.** Each is a coin-flip on scope, all four sit in D3, and D3 is not where your marks are leaking. The cost of being wrong is asymmetric — a corpus edit propagates into every future generated exam.

---

## 6. What this does not change

The audit found **no missing item from the guide's in-scope whitelist**. The corpus's 78 sections across five domain files map onto it completely. Your remaining 14 open concepts (see `CCA-F_Companion_v1.html`) are a **drill problem, not a coverage problem** — and the one live trend worth acting on is D2 sliding 100% → 90.9% → 81.8% across Exams 7, 8 and 10, which more source material would not fix.

**Recommended action before the exam: none to the corpus.** Drill the shortlist.

---

## Sources

- `anthropic-partners.skilljar.com/path/claude-certified-architect-professional` (catalog, 2026-08-10)
- `anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses` (catalog)
- `anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses` (catalog)
- Course pages: `/ai-fluency-framework-foundations`, `/claude-with-the-anthropic-api`, `/claude-code-in-action`, `/introduction-to-model-context-protocol`
- `prep with quiz/CCA-Prep_Exam-Mechanics_v2.md` §In-Scope, §Technologies, §Out-of-Scope (lines 113–136)
- `prep with quiz/CCA-Prep_Corpus-Index_v2.md` lines 4–29
- `courses/COURSE-ROADMAP.md`
