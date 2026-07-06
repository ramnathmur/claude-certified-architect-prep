# CCA-F Exam Grounding Corpus — Master Index

**Version:** 2.0 | 2026-07-06 (v1: 2026-06-27)
**Source authority (in precedence order):**
1. `source/CCA-F-Official-Exam-Guide.pdf` — the OFFICIAL Anthropic Exam Guide v0.2 (downloaded 2026-07-06 from the Skilljar certification page; text mirror `source/CCA-F-Official-Exam-Guide_text.txt`)
2. Live Anthropic documentation (divergences tracked in `CURRENT-DOCS-DELTA_v1.md`)
3. `source/guide_en.md` — community study guide (github.com/paullarionov/claude-certified-architect); depth source, not authoritative

**Purpose:** Grounding knowledge base for all MCQ mock test generation. Every question written from this corpus traces to a source entry here.
**Changelog v1→v2:** v1 wrongly cited the community guide as "Official"; corrected the scenario pool (official = 6, not 5+reserved); corpus remediated after an independent coverage audit (2026-07-06) found 3 missing task statements, 8 partial, and 2 missing official scenarios — all closed in the v2 domain files.

---

## Corpus Files (generate ONLY from these)

| File | Domain | Coverage |
|---|---|---|
| [CCA-Prep_Exam-Mechanics_v2.md](CCA-Prep_Exam-Mechanics_v2.md) | Meta | Format, scoring, official scenario bank, heuristics, in/out-of-scope, style calibration |
| [CCA-Prep_Domain-1_v2.md](CCA-Prep_Domain-1_v2.md) | D1 (27%) | Agentic Architecture & Orchestration — 18 sections; adds AgentDefinition, goal-oriented coordinator prompts, structured handoff, fixed-vs-adaptive decomposition, iterative refinement loop, session resume/fork |
| [CCA-Prep_Domain-2_v2.md](CCA-Prep_Domain-2_v2.md) | D2 (18%) | Tool Design & MCP Integration — 9 sections; adds built-in tools (§2.9, official task 2.5), tool_choice depth, business-error category, MCP resources/community-server guidance |
| [CCA-Prep_Domain-3_v2.md](CCA-Prep_Domain-3_v2.md) | D3 (20%) | Claude Code Config & Workflows — 12 sections; adds iterative refinement (§3.7, official task 3.5), @import//memory, CI re-run consistency; corrects CLAUDE.md concatenation semantics and carries the dual allowed-tools framing |
| [CCA-Prep_Domain-4_v2.md](CCA-Prep_Domain-4_v2.md) | D4 (20%) | Prompt Engineering & Structured Output — 20 sections; adds tool_choice output guarantees, syntax-vs-semantic errors, Pydantic, retry limits, self-correction, batch strategy depth (§4.11), independent review |
| [CCA-Prep_Domain-5_v2.md](CCA-Prep_Domain-5_v2.md) | D5 (15%) | Context Management & Reliability — 14 sections; adds confidence calibration & human oversight (§5.9, official task 5.5), provenance depth, escalation-proxy traps, tool-output trimming, crash-recovery persistence |
| [CCA-Prep_Key-Distinctions_v1.md](CCA-Prep_Key-Distinctions_v1.md) | All | 25 high-yield exam traps and comparisons |
| [CURRENT-DOCS-DELTA_v1.md](CURRENT-DOCS-DELTA_v1.md) | Meta | Exam-framing vs current-docs divergences with [SAFE]/[CONFLICT-RISK] posture per item |
| [PRACTICE-TEST-STEMS_v1.md](PRACTICE-TEST-STEMS_v1.md) | Meta | Dedup ledger: all 76 community practice-test stems (includes the official PDF's 12 samples) + quantified style-calibration profile |

**Superseded (history only — never generate from):** `CCA-Prep_Domain-1..5_v1.md`, `CCA-Prep_Exam-Mechanics_v1.md`, `CCA-Prep_Corpus-Index_v1.md`.

---

## Exam Domain Weights and Quotas

| # | Domain | Weight | FULL-60 quota | DRILL-30 quota |
|---|---|---|---|---|
| D1 | Agentic Architecture & Orchestration | 27% | 16 | 8 |
| D2 | Tool Design & MCP Integration | 18% | 11 | 5–6 |
| D3 | Claude Code Configuration & Workflows | 20% | 12 | 6 |
| D4 | Prompt Engineering & Structured Output | 20% | 12 | 6 |
| D5 | Context Management & Reliability | 15% | 9 | 4–5 |

---

## Exam Scenarios (OFFICIAL — Exam Guide v0.2 pp.4–5)

The real exam draws **4 at random from this bank of 6**:

1. **Customer Support Resolution Agent** — MCP tools, escalation, first-contact resolution (D1, D2, D5)
2. **Code Generation with Claude Code** — slash commands, CLAUDE.md, plan mode (D3, D5)
3. **Multi-Agent Research System** — coordinator + subagents, cited reports (D1, D2, D5)
4. **Developer Productivity with Claude** — built-in tools, codebase exploration, MCP (D2, D3, D1) *(added in v2 — absent from v1)*
5. **Claude Code for Continuous Integration** — automated review, test generation, PR feedback (D3, D4)
6. **Structured Data Extraction** — JSON schemas, validation, accuracy (D4, D5) *(added in v2 — absent from v1)*

The community guide's "Conversational AI Architecture Patterns" (its #7) and "Agentic AI Tools" placeholder (its #8) are candidate-reported and NOT in the official bank; their underlying content maps to D1/D5 task statements and remains valid study material, but generated exams must not use them as scenario blocks.

---

## Coverage Audit Trail

| Check | Status |
|---|---|
| All domain weights sum to 100% | ✅ 27+18+20+20+15 = 100 |
| All 30 official task statements covered at exam depth | ✅ as of v2 (independent audit 2026-07-06 found 19 covered / 8 partial / 3 missing in v1; all 11 remediated in v2 domain files) |
| All 6 official scenarios represented in corpus | ✅ as of v2 (v1 had 4 of 6) |
| Every knowledge claim traced to a source | ✅ each file carries source citations; official PDF is primary |
| Product-behavior claims verified against live docs | ✅ 9 spot-checks 2026-07-06; divergences recorded in CURRENT-DOCS-DELTA_v1.md |
| Out-of-scope topics excluded | ✅ official 16-item list in Exam-Mechanics v2 |
| Key distinctions cover observed trap patterns | ✅ 25 documented |
| Practice-test dedup ledger complete | ✅ 76 stems (verified count; the community guide's own "60" header is wrong) |

**Next re-verification due:** before any exam generated after 2026-08-05 (30-day docs-currency rule in `CURRENT-DOCS-DELTA_v1.md`).
