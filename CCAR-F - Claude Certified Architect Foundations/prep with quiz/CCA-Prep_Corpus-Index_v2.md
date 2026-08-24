# CCA-F Exam Grounding Corpus — Master Index

**Version:** 2.2 | 2026-08-14 (v2.1: 2026-08-09; v2.0: 2026-07-06; v1: 2026-06-27)
**Source authority (in precedence order):**
1. `source/CCA-F-Official-Exam-Guide_v1.0.pdf` — the OFFICIAL Anthropic Exam Guide **v1.0** (Effective July 2026; official exam code **CCAR-F** — this corpus uses "CCA-F" throughout; retrieved 2026-08-09 from the Anthropic Partner Academy certification page; text mirror `source/CCA-F-Official-Exam-Guide_v1.0_text.txt`). Superseded v0.2 is retained at `source/CCA-F-Official-Exam-Guide.pdf` as the historical snapshot every exam through Exam 11 was authored against; a measured diff found the domain weights, all 6 scenarios, all 30 task statements, and both scope lists identical.
2. Live Anthropic documentation (divergences tracked in `CURRENT-DOCS-DELTA_v1.md`)
3. `source/guide_en.md` — community study guide (github.com/paullarionov/claude-certified-architect); depth source, not authoritative
4. `../Outputs/ccg-mirror/` — local mirror of **claudecertificationguide.com**, a second community study site (crawled 2026-08-14; 57 pages, 72,486 words, `md/` + raw `html/` + the site's own `_site/llms-full.txt` index). Same tier as item 3: **depth and independent cross-check, never authoritative.** Its 30 lessons map one-to-one onto the 30 official task statements, so it adds no new subject matter — its value is a second author's take on the same material. Two standing cautions: (a) it asserts that MCP **transport selection** may be tested, which contradicts the official out-of-scope list (`Streaming API or server-sent events`; `Deploying or hosting MCP servers`) — official framing wins, do not reopen that call; (b) it is undated per-page and community-maintained, so any product-behavior claim taken from it must be re-verified against live Anthropic docs before it enters `CURRENT-DOCS-DELTA_v1.md` (this is how D9 was handled).

**Purpose:** Grounding knowledge base for all MCQ mock test generation. Every question written from this corpus traces to a source entry here.
**Changelog v2.1→v2.2:** added source-authority item **4** — a local mirror of the community site `claudecertificationguide.com` (`../Outputs/ccg-mirror/`), registered at the same non-authoritative depth tier as `guide_en.md`. A coverage cross-check against it found **zero new task statements** and **zero uncovered corpus topics**; the corpus was already ahead on `stop_reason` (delta D2 carries `stop_details`, the site does not) and level on `tool_choice`. One genuine currency gap surfaced and became **delta D9** (`Task` → `Agent` rename). Its 156 "Exam Trap" blocks are logged below as a distractor-geometry seam for future generation. **No domain corpus file, weight, scenario, task statement, or scope list was edited** — filename stays `_v2`. Full crawl and coverage report: `../Outputs/CCA-Prep_CCG-Crawl-Coverage-Report_v1.md`.
**Changelog v2.0→v2.1:** re-pointed the source-authority chain at the republished official Exam Guide **v1.0** (Ram approved 2026-08-09). A measured v0.2→v1.0 diff confirmed **zero change** to domain weights, the 6 scenarios, the 30 task statements, the in-scope list, and the 16-item out-of-scope list — so no domain corpus file required an edit. Only exam-mechanics meta-facts changed; those landed in `CCA-Prep_Exam-Mechanics_v2.md` v2.1. Filename stays `_v2` (subject-matter content untouched, and the path is referenced across the project).
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
| [CCA-Prep_Key-Distinctions_v1.md](CCA-Prep_Key-Distinctions_v1.md) | All | 29 high-yield exam traps and comparisons (v1.1 added #26–29, built-in tools) |
| [CURRENT-DOCS-DELTA_v1.md](CURRENT-DOCS-DELTA_v1.md) | Meta | Exam-framing vs current-docs divergences with [SAFE]/[CONFLICT-RISK] posture per item |
| [PRACTICE-TEST-STEMS_v1.md](PRACTICE-TEST-STEMS_v1.md) | Meta | Dedup ledger: all 76 community practice-test stems (includes the official PDF's 12 samples) + quantified style-calibration profile |

**Superseded (history only — never generate from):** `CCA-Prep_Domain-1..5_v1.md`, `CCA-Prep_Exam-Mechanics_v1.md`, `CCA-Prep_Corpus-Index_v1.md`.

---

## Authoring Constraints (not corpus — but binding on every exam)

These do not supply subject matter; they constrain how questions may be written. Read them alongside the corpus, not instead of it.

| File | Applies from | What it binds |
|---|---|---|
| [QUESTION-ARCHETYPE-BANLIST.md](QUESTION-ARCHETYPE-BANLIST.md) | Exam 14 onward | Nine reskinned question shapes found across the 720 questions in Exams 2–13, each with every prior instance and at least two approved re-frames. Defines a **seventh Phase 4.e.6 check — ARCHETYPE COLLISION**. The corpus points are not banned; the shapes are. Also caps closing-formula rate at 20% and opening-formula rate at 15%. |
| [tools/archetype_gate.py](tools/archetype_gate.py) | Exam 14 onward | Computes fidelity checks 1–5, the new check 7, and a multiple-response validity check directly from a shipped exam HTML or a questions JSON: `python tools/archetype_gate.py mock-exams/CCA-Prep_MockTest-N_v1.html`. Orchestration-prompt v10 still describes these as hand-tallied because it assumes no code execution; when code execution is available, run the script — the hand-tallied process shipped three defects into Exam 13 that the script found in seconds. |

**Known gap:** orchestration-prompt v10 says "six checks" in three places (lines 708, 1009, 1074) and does not reference either file. Editing v10 is an **open decision for Ram** — it changes a stated contract — so the pointer lives here and in `SESSION-STATE.md` until he rules.

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
| Independent second-source coverage cross-check | ✅ 2026-08-14 — checked all 73 corpus sections against the 30 lessons + 5 quick-reference + 5 glossary pages of `claudecertificationguide.com` (source 4). **0 new task statements, 0 uncovered topics.** One currency gap → delta D9. **Open seam:** that site carries **156 "Exam Trap" blocks** against our **29** Key Distinctions. Not a coverage gap — the corpus points are already held — but a 5× independent inventory of *distractor geometry*, which is the exact lever `SESSION-STATE.md` names for the compensating-mechanism error pattern that no domain quota can target. Mine for shapes when seeding Exam 17; the `QUESTION-ARCHETYPE-BANLIST.md` collision check still applies to anything drawn from it. |
| Practice-test dedup ledger complete | ✅ 76 stems (verified count; the community guide's own "60" header is wrong) |

| Primary source is the currently-published guide | ✅ re-verified 2026-08-09 — official guide republished as **v1.0** (Effective July 2026, code CCAR-F); measured diff vs cached v0.2 found weights, all 6 scenarios (100.0% identical), all 30 task statements (0 title diffs), and both scope lists **unchanged**. Only exam-mechanics meta-facts moved — see `CURRENT-DOCS-DELTA_v1.md` Part 1 (E1–E7). |

**Next re-verification due:** before any exam generated after **2026-09-08** (30-day docs-currency rule in `CURRENT-DOCS-DELTA_v1.md`).

**Re-verification must now cover the guide PDF itself, not just live docs.** The v0.2 → v1.0 republication happened two days after the cached download and stayed invisible for a month because prior checks only re-verified product documentation. Re-download the Exam Guide asset from the Partner Academy certification page and compare its printed version marker and §18 Document Control table.
