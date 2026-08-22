# CCA-F Exam Grounding Corpus — Master Index

**Version:** 1.0  
**Created:** 2026-06-27  
**Source authority:** Official CCA-F Study Guide (guide_en.MD), Anthropic documentation  
**Purpose:** Grounding knowledge base for all MCQ mock test generation. Every question written from this corpus traces to a source entry here.

---

## Corpus Files

| File | Domain | Coverage |
|---|---|---|
| [CCA-Prep_Exam-Mechanics_v1.md](CCA-Prep_Exam-Mechanics_v1.md) | Meta | Format, scoring, scenarios, out-of-scope |
| [CCA-Prep_Domain-1_v1.md](CCA-Prep_Domain-1_v1.md) | D1 (27%) | Agentic Architecture & Orchestration |
| [CCA-Prep_Domain-2_v1.md](CCA-Prep_Domain-2_v1.md) | D2 (18%) | Tool Design & MCP Integration |
| [CCA-Prep_Domain-3_v1.md](CCA-Prep_Domain-3_v1.md) | D3 (20%) | Claude Code Configuration & Workflows |
| [CCA-Prep_Domain-4_v1.md](CCA-Prep_Domain-4_v1.md) | D4 (20%) | Prompt Engineering & Structured Output |
| [CCA-Prep_Domain-5_v1.md](CCA-Prep_Domain-5_v1.md) | D5 (15%) | Context Management & Reliability |
| [CCA-Prep_Key-Distinctions_v1.md](CCA-Prep_Key-Distinctions_v1.md) | All | High-yield exam traps and comparisons |

---

## Exam Domain Weights

| # | Domain | Weight | Mock Test Question Quota (per 30Q test) |
|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | 8 |
| D2 | Tool Design & MCP Integration | 18% | 5–6 |
| D3 | Claude Code Configuration & Workflows | 20% | 6 |
| D4 | Prompt Engineering & Structured Output | 20% | 6 |
| D5 | Context Management & Reliability | 15% | 4–5 |

---

## Exam Scenarios (from guide_en.MD)

The real exam draws 4 random scenarios from the following pool. Every scenario appears in the practice material.

1. **Multi-agent Research System** — coordinator + web-search + document-analysis + synthesis subagents
2. **Claude Code for Continuous Integration** — CI/CD pipeline, `--print` mode, batch API, structured output
3. **Code Generation with Claude Code** — CLAUDE.md hierarchy, skills, rules, planning vs direct execution
4. **Customer Support Agent** — tool selection, escalation, error propagation, multi-issue requests
5. **Conversational AI Architecture Patterns** — stateless API, context window management, behavioral drift
6. **(Scenario 6 — reserved)** — not yet documented in study guide as of 2026-06-27

---

## QA Validation Log

| Check | Status |
|---|---|
| All domain weights sum to 100% | ✅ 27+18+20+20+15 = 100 |
| Every knowledge claim traced to guide_en.MD or Anthropic docs | ✅ Each file has source citations |
| Out-of-scope topics excluded | ✅ See Exam-Mechanics file |
| Key distinctions cover exam-observed trap patterns | ✅ 25 distinctions documented |
| Scenario coverage complete | ✅ All 5 documented scenarios covered |
