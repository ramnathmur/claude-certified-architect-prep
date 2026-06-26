# Prep Material Index — Claude Certified Architect Foundations (CCA-F)

**Last updated:** 2026-06-09  
**Exam name:** Claude Certified Architect — Foundations (CCA-F)  
**Status:** Researched + **community guide DIGESTED** → see [`EXAM-DIGEST.md`](EXAM-DIGEST.md) (condensed cram sheet, 11 KAs mapped to the 5 domains)

---

## Exam Snapshot

| Detail | Value |
|---|---|
| Questions | 60 (multiple choice, single answer, scenario-based) |
| Time limit | 120 minutes (third-party cited — verify on Skilljar after login) |
| Passing score | 720 / 1000 (scaled) |
| Delivery | Proctored online — no Claude, no docs, no external tools during exam |
| Scenario structure | 4 scenarios randomly drawn from a pool of 6 (per the official exam guide) |
| Access | Claude Partner Network employees (first 5,000 free; $99/attempt after) |
| Registration | https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request |

> **Note:** Individual learners not affiliated with a partner org can complete all Anthropic Academy prep courses now, but need to join a partner org to unlock an exam seat. Join the partner network (free) at https://www.anthropic.com/news/claude-partner-network.

---

## Exam Domains

| # | Domain | Weight | Core Topics |
|---|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% | Agent loops, observe-think-act-respond cycle, multi-agent orchestration, subagent delegation, session management |
| 2 | Tool Design & MCP Integration | 18% | MCP server architecture (tools/resources/prompts primitives), stdio vs SSE transport, tool description writing, auth patterns |
| 3 | Claude Code Configuration & Workflows | 20% | CLAUDE.md hierarchy, path-scoped rules, slash commands, plan mode, CI/CD integration |
| 4 | Prompt Engineering & Structured Output | 20% | Few-shot prompting, JSON schema design, validation loops, structured extraction |
| 5 | Context Management & Reliability | 15% | CALM framework, prompt caching with cache_control, conversation compaction, token budgeting, multi-turn design |

### The Six Exam Scenarios (4 appear per sitting)

| # | Scenario | Domain emphasis |
|---|---|---|
| 1 | Customer Support Resolution Agent | Agentic Architecture |
| 2 | Code Generation with Claude Code | Claude Code Configuration |
| 3 | Multi-Agent Research System | Agentic Architecture |
| 4 | Developer Productivity Tools | Tool Design & MCP |
| 5 | Claude Code in CI/CD | Claude Code + Prompt Engineering |
| 6 | Structured Data Extraction | Prompt Engineering & Structured Output |

> **Scoring note:** Production-scenario questions and anti-pattern recognition questions carry higher weight than pure knowledge recall. Prioritise scenario fluency, not just definitions.

---

## Official Resources

### Anthropic Academy (free — no partner access required)
- **URL:** https://anthropic.skilljar.com/
- **Content:** 13 courses, ~15–20 hours total, covers Claude API, MCP, Agent Skills, Claude Code in Action
- **200-level courses are the exam-relevant tier** — complete all of them before sitting
- **Partner Network Learning Path (4 focused courses):** https://anthropic.skilljar.com/page/claude-partner-network-learning-path

### Anthropic Learn Hub
- **URL:** https://www.anthropic.com/learn
- General learning hub; routes to Academy and docs

### Anthropic Documentation (always-current reference)
- Claude API docs: https://docs.anthropic.com/en/api
- MCP documentation: https://docs.anthropic.com/en/docs/build-with-claude/mcp
- Tool use guide: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
- Prompt engineering: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- Context window & caching: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Claude Code docs: https://docs.anthropic.com/en/docs/claude-code
- Agent SDK: https://docs.anthropic.com/en/docs/agents

> No official exam guide PDF has been published by Anthropic. The Skilljar portal is the canonical source for exam content.

---

## Community Resources

### GitHub — Study Guides (free, open source)

| Repo | Notes | URL |
|---|---|---|
| `daronyondem/claude-architect-exam-guide` | ✅ **DIGESTED 2026-06-09** (v1.0.1, 26 May 2026) → `EXAM-DIGEST.md`. 11 knowledge areas, each with "What to Know" + "Common Pitfalls"; PDF/EPUB via Releases; CC BY 4.0 (attribute Daron Yöndem). Most widely cited. | https://github.com/daronyondem/claude-architect-exam-guide |
| `paullarionov/claude-certified-architect` | Another community guide with study materials | https://github.com/paullarionov/claude-certified-architect |

### Practice Questions (free)

| Source | Content | URL |
|---|---|---|
| claudecertifications.com | 25 practice questions, 12-week study plan, 6 scenario walkthroughs, 18-item anti-patterns cheatsheet | https://claudecertifications.com/claude-certified-architect |
| Tutorials Dojo | CCA-F study guide from well-known AWS cert prep provider | https://tutorialsdojo.com/cca-f-claude-certified-architect-foundations-study-guide/ |

### Written Guides & Blogs (free)

| Source | Notes | URL |
|---|---|---|
| DEV Community | 5 domains, 6 scenarios breakdown + comments from exam takers | https://dev.to/aws-builders/the-claude-certified-architect-exam-5-domains-6-scenarios-and-everything-you-need-to-know-4le3 |
| Zen van Riel | CCA architect certification guide | https://zenvanriel.com/ai-engineer-blog/claude-certified-architect-anthropic-certification-guide/ |
| Medium / Data Science Collective | Complete study guide with code + tutor prompts | https://medium.com/data-science-collective/the-complete-claude-architect-study-guide-with-code-and-tutor-prompts-01f524e95c92 |
| lowcode.agency | How to get certified in 2026 | https://www.lowcode.agency/blog/how-to-become-claude-certified-architect |

### YouTube (free)

| Title | Notes | URL |
|---|---|---|
| Zero to Claude Certified Architect — Complete Exam Prep Series | Full playlist | https://www.youtube.com/playlist?list=PLFz7SvAnfqLpjPCPJBkUy077BC5ecuE8c |
| Agentic Loops & stop_reason Explained (Ep 01) | Domain 1 deep dive | https://www.youtube.com/watch?v=ldqOnljDINc |
| How to Register for CCA-F — Step-by-Step | Registration walkthrough | https://www.youtube.com/watch?v=6xDJ6Fgia1A |
| Anthropic's NEW Claude Architect Guide in 39 Minutes | Fast overview | https://www.youtube.com/watch?v=vizgFWixquE |

### Paid Course

| Platform | Course | URL |
|---|---|---|
| Udemy | CCA-F 2026 Exam Prep Masterclass — built domain by domain against exam blueprint | https://www.udemy.com/course/certified-claude-architect-masterclass-2026/ |

---

## Recommended Prep Sequence (for Ram)

1. **Register for partner access** → https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request  
2. **Complete all Anthropic Academy 200-level courses** (free, do in parallel while waiting for exam access) → https://anthropic.skilljar.com/  
3. **Download community PDF guide** from `daronyondem/claude-architect-exam-guide` GitHub repo (most comprehensive free resource)  
4. **Run through 25 practice questions** at claudecertifications.com — use them to identify weak domains, not just to score  
5. **Build the AI-first training course** (Phase 2) — one module per domain, using this index as the source map  
6. **Mock exam under timed conditions** once course modules are complete  

---

## Download Checklist

- [x] daronyondem/claude-architect-exam-guide — **content digested 2026-06-09 → `EXAM-DIGEST.md`** (PDF/EPUB still optional for offline reading via GitHub Releases v1.0.1)
- [ ] paullarionov/claude-certified-architect — clone or download
- [x] **Practice bank staged 2026-06-09** → `practice/` (51 original, domain-weighted, exam-style Qs + answer keys; see `practice/README.md`). claudecertifications.com 25 Qs remain an optional supplement (work on their site).
- [ ] Anthropic Academy course completion — track progress per course
- [ ] Anthropic docs pages for each domain — bookmark/save locally per domain

---

## Flagged Uncertainties (verify when you access Skilljar)

- 120-minute time limit — cited by multiple third-party sources, not confirmed by Anthropic directly
- $99/attempt post-free-tier price — third-party sourced
- Exact question count (60) — widely cited but not on Anthropic's own page
