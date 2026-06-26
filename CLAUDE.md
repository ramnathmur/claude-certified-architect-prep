# Project: Claude Certified Architect Prep

**Owner:** Ram  
**Created:** 2026-06-04  
**Status:** Phase 2 — Training Course Active

---

## Purpose

Prepare Ram to pass the **Claude Certified Architect** exam through a structured, AI-first learning experience — not passive study. Every session should deepen understanding of Claude's architecture, capabilities, and design principles at the level required to architect production-grade Claude-powered systems.

---

## Project Phases

### Phase 1 — Acquire Prep Material ⬜
- Map all official and community exam preparation resources
- Download or link: official exam guide, topic domains, sample questions, Anthropic documentation
- Identify any practice environments or sandbox resources
- Produce a consolidated `PREP-MATERIAL-INDEX.md` cataloguing everything by domain

### Phase 2 — Build the Training Course ⬜
- Design a full AI-first learning curriculum using Ram's learning methodology (see below)
- One module per exam domain
- Produce `CURRICULUM.md` with phased module plan, learning objectives, assessments
- Build module content as interactive sessions, not lecture dumps

### Phase 3 — Practice + Assessment ⬜
- Work through every domain module with active recall, not passive reading
- Track gaps and misconceptions in `GAPS.md`
- Run mock exam questions under timed conditions
- Iterate until exam-ready

---

## AI-First Learning Methodology

Ram learns by **doing, not reading**. Apply these principles to every session:

| Principle | How to apply |
|---|---|
| Why before How | Explain the reasoning behind every Claude design decision before showing how to use it |
| Big picture first | Orient the domain, then zoom in. Never start mid-detail |
| Predict before run | Ask Ram to predict outcomes, API responses, or model behaviors before showing the answer |
| Pattern naming | Name reusable patterns ("context window management", "tool-use delegation", "multi-agent handoff") so Ram can apply them in new situations |
| Real-world anchors | Connect concepts to Ram's existing work: agents, agentic workflows, Claude Code, the AI-first blueprint |
| Active recall | End each module with a 5-question quiz — no hints. Score it. Surface gaps immediately |
| Spaced repetition | Re-surface prior module concepts briefly at the start of each new module |

---

## Exam Domain Map

| # | Domain | Weight | Status |
|---|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% | ⬜ |
| 2 | Tool Design & MCP Integration | 18% | ⬜ |
| 3 | Claude Code Configuration & Workflows | 20% | ⬜ |
| 4 | Prompt Engineering & Structured Output | 20% | ⬜ |
| 5 | Context Management & Reliability | 15% | ⬜ |

---

## File Conventions

| File | Purpose |
|---|---|
| `CLAUDE.md` | This file — project brief and methodology |
| `ROADMAP.md` | Phased checklist with status indicators |
| `PREP-MATERIAL-INDEX.md` | Full catalogue of exam prep resources by domain |
| `CURRICULUM.md` | AI-first training course plan with modules and objectives |
| `GAPS.md` | Running log of misconceptions and weak areas |
| `modules/` | One `.md` per exam domain — lesson content, examples, quizzes |
| `practice/` | Mock exam questions, timed attempts, results |

---

## Operating Rules for This Project

- **Never summarise when you can quiz.** At the end of any explanation, ask a question rather than summarising.
- **Challenge assumptions.** If Ram states something incorrect about Claude's behaviour, correct it immediately with the right mental model.
- **Cite Anthropic docs.** Every factual claim about Claude's capabilities should be grounded in official documentation — not hallucinated.
- **No passive dumps.** Don't paste documentation. Synthesise, explain, connect, test.
- **Flag knowledge gaps honestly.** If something is uncertain or may have changed since training, say so and point to where to verify.

---

## Reference Resources

- Anthropic Documentation: https://docs.anthropic.com
- Claude API Reference: https://docs.anthropic.com/en/api
- Model Spec: https://docs.anthropic.com/en/anthropic-model-spec (verify URL)
- AI-First Learning Playbook: `C:\Claude Cowork\Playbook for AI-first learning applications\`
- Ram's About Me: `C:\Claude Cowork\About Me\about-me.md`
