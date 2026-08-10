# Exam 10 Generation Plan (WIP — Slice A checkpoint)

**Date:** 2026-07-28 | **Operating prompt:** CCA-Orchestration-Prompt_v10.md | **Format:** FULL-60
**Purpose:** Durable checkpoint plan so generation can resume across sessions if the weekly usage limit interrupts. Read this file + SESSION-STATE.md to resume.

## Slice status (update as each completes)

| Slice | Work | Artifact | Status |
|---|---|---|---|
| A | This plan + SESSION-STATE checkpoint | WIP-EXAM10/PLAN.md | DONE |
| B | Block 1 Customer Support (g1-15) | WIP-EXAM10/block-1.json | DONE (2026-07-28; §2.6 used capability-categories facet — transports absent from corpus) |
| C | Block 2 Code Generation (g16-30) | WIP-EXAM10/block-2.json | DONE (2026-07-28; §3.1/§3.6 3rd re-tests fresh vs Exam7/8; proportionate-response cluster g16/g23/g27) |
| D | Block 3 Multi-Agent Research (g31-45) | WIP-EXAM10/block-3.json | DONE (2026-07-28; §2.6 facet reversed-direction .mcp.json scope — flagged residual overlap w/ Exam5/9, narrow corpus content, no better-fenced option existed; verified clean, no injected content) |
| E | Block 4 Structured Data Extraction (g46-60) | WIP-EXAM10/block-4.json | DONE (2026-07-28; §4.6 3rd re-test fresh mechanism vs Exam7/8; §4.2/§4.9 fresh facets vs Exam8) |
| F | Fidelity gate 4.e.5/4.e.6 + citation-collision tally + Jaccard scan + cross-block content read + fixes | WIP-EXAM10/exam10-verified.json + WIP-EXAM10/GATE-REPORT.md | DONE (2026-07-28; all 6 checks pass, 2 pre-declared D2 repeats confirmed non-colliding on content read, 0 Jaccard near-dups, no fixes needed) |
| G | HTML build | mock-exams/CCA-Prep_MockTest-10_v1.html | DONE (2026-07-28; 171,391 bytes, DATA valid/60 Qs, disclosure line present, UTF-8 verified byte-level) |
| H | EXAM-LOG skeleton, DASHBOARD-DATA line, GENERATION-INTELLIGENCE Session 12, SESSION-STATE close, WIP cleanup | logged exam | DONE (2026-07-28; all logs updated, WIP folder kept as audit trail not deleted) |

**GENERATION COMPLETE.** Exam 10 shipped at `mock-exams/CCA-Prep_MockTest-10_v1.html`, fully logged. See SESSION-STATE.md for the full closing summary.

## Governing inputs (Phase 1 state, already loaded)

- **Professor's Note — Intent for Exam 10** (EXAM-LOG.md, written 2026-07-28 after Exam 8 scored 52/60): base quota unchanged (confirmed_weakness=false — D3/D4 two-domain tie has no single +4 target). Bias D3's 12 and D4's 12 toward: (a) THIRD re-test of D3 §3.1, D3 §3.6, D4 §4.6 (missed in Exams 7 AND 8 — fresh facets mandatory); (b) broad breadth across the rest of D3/D4 incl. fresh misses §3.11, §4.2, §4.9; (c) a 2-3 question "proportionate response vs over-engineering" cluster in D3. Do NOT re-narrow to only the four originally-flagged sections.
- **exams_scored = 5** (Exams 4-8) — not a multiple of 3 → NO Insights Round this session.
- **Corpus fully saturated** (all 71 sections Heavy) → spread each domain's quota across distinct sections (PB-17 discipline); where a repeat is forced (D2: 11 Q over 9 sections), pre-declared disjoint facets below (PB-19/Exam-9 preventive pattern).
- **KD tracker clean** — seed KDs for periodic confirmation only; KD#23 (D5, behavioral drift vs context overflow) is the priority confirmation, seeded in B1 §5.13. KD cap 15/exam (target ~6-10).
- All four drawn scenarios are at their **6th use** → expect active anti-convergence rewriting vs prior exams' stems (Weak Pattern warning, Exam 7 lesson).

## Scenario draw (4 of 6, rotation-preferred)

Drawn (all at count 5, the four least-used; rests Developer Productivity and Claude Code CI at 6):
1. **Customer Support Resolution Agent** (Primary: D1, D2, D5) — g1-15
2. **Code Generation with Claude Code** (Primary: D3, D5) — g16-30
3. **Multi-Agent Research System** (Primary: D1, D2, D5) — g31-45
4. **Structured Data Extraction** (Primary: D4, D5) — g46-60

D4-carrier constraint satisfied (SDE included). GENERATION-INTELLIGENCE Session-10 note explicitly anchors Exam 10 on SDE.

## Block × domain allocation (gate-verified: every Primary > every non-Primary per block)

| Block | D1 | D2 | D3 | D4 | D5 | Total |
|---|---|---|---|---|---|---|
| B1 Customer Support (P: D1,D2,D5) | 7 | 4 | 1 | 1 | 2 | 15 |
| B2 Code Generation (P: D3,D5) | 1 | 1 | 9 | 1 | 3 | 15 |
| B3 Multi-Agent Research (P: D1,D2,D5) | 7 | 5 | 1 | 0 | 2 | 15 |
| B4 Structured Data Extraction (P: D4,D5) | 1 | 1 | 1 | 10 | 2 | 15 |
| **Totals** | **16** | **11** | **12** | **12** | **9** | **60** |

## Correct-answer letter pre-plan (4.d.5 — pre-assign BEFORE writing options)

| Block | Multiset | Short letter |
|---|---|---|
| B1 | A×4 B×4 C×4 D×3 | D |
| B2 | A×4 B×4 C×3 D×4 | C |
| B3 | A×4 B×3 C×4 D×4 | B |
| B4 | A×3 B×4 C×4 D×4 | A |

Exam-wide: 15/15/15/15. Each author fixes a per-question letter sequence from its multiset before drafting options and reports it.

## Section assignments (grep-verified against live corpus headings, PB-18)

Every domain spreads across distinct sections except D2 (11 over 9 → two forced repeats with disjoint declared facets).

**B1 Customer Support (15):**
- D1 (7): §1.1 agentic loop · §1.9 error propagation · §1.11 least privilege · §1.12 escalate to human · §1.13 structured handoff · §1.14 critical sequencing & preconditions · §1.16 session resume/fork/fresh
- D2 (4): §2.1 API tool use · §2.3 **facet: business-error vs protocol-error semantics (e.g., refund-not-eligible is data, not failure)** · §2.6 **facet: protocol/capability side — transports (stdio vs remote HTTP/SSE) or capability categories; NOT config files/scope/vetting** · §2.8 tool bundling/composite
- D3 (1): §3.8 headless `-p`/CI practices (support-automation pipeline framing)
- D4 (1): §4.15 escalation & confidence routing
- D5 (2): §5.8 escalation & ambiguity resolution · §5.13 conversation-level state **(seed KD#23 here — behavioral drift from accumulated responses vs context overflow; fresh scenario ≠ Exam 8's PR-description-generator)**

**B2 Code Generation (15):**
- D3 (9): §3.1 **THIRD RE-TEST** (@import/memory-diagnosis distinction; fresh facet ≠ Exam 7/8/9 stems — check EXAM-LOG) · §3.2 path-scoped rules · §3.3 skills · §3.4 slash commands · §3.5 personal-vs-project precedence · §3.6 **THIRD RE-TEST** (plan mode vs direct execution on a fully-scoped task; fresh facet) · §3.7 iterative refinement · §3.11 CLAUDE.md content organization (Exam 8 fresh miss — re-test different facet) · §3.12 session management
- **Proportionate-response cluster (Professor's Note item c):** frame ≥3 of the D3 questions (§3.1, §3.6, §3.11 natural carriers; optionally §3.2) with over-engineering distractors — hook/re-typed-reminder/plan-mode/half-split traps vs the proportionate direct fix. Ground in Exam-Mechanics "proportionate first response" heuristic.
- D1 (1): §1.17 independent review instances
- D2 (1): §2.9 built-in tools
- D4 (1): §4.14 prompt chaining (generate→review pipeline framing)
- D5 (3): §5.3 context window management · §5.6 context isolation w/ subagents · §5.12 scratchpad/structured state persistence

**B3 Multi-Agent Research (15):**
- D1 (7): §1.2 hub-and-spoke · §1.3 AgentDefinition · §1.5 structured context passing & attribution · §1.6 task decomposition · §1.7 fixed vs adaptive decomposition · §1.8 iterative refinement loop · §1.10 coverage annotations
- D2 (5): §2.2 description design · §2.4 two-tool token-binding · §2.5 tool distribution & tool_choice config · §2.6 **facet: config/deployment side — remote-server auth or enterprise/managed scope; NOT transports/capabilities (B1 owns those), NOT resource-exposure/community-vs-custom (burned Exam 8), NOT .mcp.json ${VAR} project scope (burned Exam 9)** · §2.7 hooks
- D3 (1): §3.10 Message Batches API (bulk corpus processing framing)
- D5 (2): §5.10 conflict detection & source attribution · §5.11 provenance
- No D4 in this block.

**B4 Structured Data Extraction (15):**
- D4 (10): §4.2 CoT for N-item comparison (Exam 8 fresh miss — re-test) · §4.5 JSON schema design · §4.6 **THIRD RE-TEST** (tool_choice specific-tool vs `"any"` — `"any"` guarantees SOME tool, not THE tool; fresh facet ≠ Exam 7/8 stems) · §4.7 syntax vs semantic errors · §4.8 Pydantic/typed validation · §4.9 retry-with-feedback limits (Exam 8 fresh miss — re-test) · §4.10 self-correction · §4.11 batch strategy · §4.16 instruction specificity vs abstraction · §4.19 clarification: proceed vs ask
- D1 (1): §1.15 parallel execution
- D2 (1): §2.3 **facet: machine-readable structured-error content design enabling retry-with-feedback; NOT business-vs-protocol semantics (B1 owns that)**
- D3 (1): §3.9 structured output from CLI (`--json-schema`)
- D5 (2): §5.2 lost-in-the-middle (long-document extraction) · §5.5 trimming verbose tool outputs

Sections deliberately unused this exam (breadth headroom): D1 §1.4, §1.18 · D4 §4.1, §4.3, §4.4, §4.12, §4.13, §4.17, §4.18, §4.20 · D5 §5.1, §5.4, §5.7, §5.9, §5.14.

## Style + format contract (binding, orchestration v10 §4.a.5/4.e)

- Stem: generic Situation + one decision question. Median 50-55 words exam-wide, hard cap 95. NO invented company/product/persona names.
- Exactly 4 options, ≤35 words each, grammatically parallel, 1 correct + 3 documented-misconception distractors.
- Rationales: whyRight + 3 whyWrong, every one cites `D<n> §<sec>` (or KD#n). A distractor that can't name a real documented misconception must be replaced.
- Inline code/config tokens in 20-25% of options exam-wide, concentrated in D2/D3 (B4's schema/JSON content counts too).
- Out-of-scope 16-item list in Exam-Mechanics_v2 is a hard exclusion.
- Block narrative: "same-tools-progressing-narrative" continuity pattern across the block's 15 questions.

## Question JSON schema (per block file, matches MockTest-9 DATA)

```json
{"label": "<scenario name>", "narrative": "<block narrative for landing card>",
 "questions": [{"g": <global#>, "block": <0-3>, "blockLabel": "<scenario>", "domain": "D1",
   "stem": "...", "options": ["...","...","...","..."], "correct": <0-3>,
   "whyRight": {"text": "...", "cite": "D3 §3.1"},
   "whyWrong": [{"option": <i>, "text": "...", "cite": "..."}, ...],
   "kd": <n or null>, "section": "§3.1", "letterPlanned": "A"}]}
```

## Dedup obligations (each author, before returning)

1. Grep EXAM-LOG.md "Questions Used" for every assigned section — do not reuse/closely-paraphrase any prior stem (Exams 1-9, 480 stems).
2. Check PRACTICE-TEST-STEMS_v1.md §2 (76 locked stems incl. official 12 samples).
3. All four scenarios are on their 6th use: actively rewrite anything tracking close to prior same-scenario stems (expect rewrites, not just checks).
4. Facet declarations above are HARD constraints — never write into a sibling block's declared facet.

## Landing card must include (verbatim or equivalent)

"These 4 were curated to guarantee coverage across your exams — the real exam draws 4 of 6 at random each sitting, with no such guarantee."

## HTML build notes (Slice G)

- File: `mock-exams/CCA-Prep_MockTest-10_v1.html`. Template: MockTest-9 structure (AI Oracle Quiz v2 design system): one-question-per-page, auto-resume via localStorage `KEY = "cca-mock-10"`, running-accuracy pill (v10 addition), passive timing, jump map, per-option selection-aware feedback, results-JSON export (schema: exam_n 10, format FULL60, blocks by scenario, questions with q/domain/block/selected/correct/seconds).
- JS comment block at top listing all 60 stems + the 4 scenarios drawn (Phase 4.g).
