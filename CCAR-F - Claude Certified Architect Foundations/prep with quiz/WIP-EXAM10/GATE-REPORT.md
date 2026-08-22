# Exam 10 — Fidelity Verification Gate Report (Phase 4.e.6)

Run 2026-07-28 against the merged 60-question set (`exam10-verified.json`).

| # | Check | Computed value | Threshold | Pass/Fail | Fix applied |
|---|---|---|---|---|---|
| 1 | No invented names | 0 hits | 0 | **PASS** | — |
| 2 | Correct-letter tally (per block / exam-wide) | B0 4/4/4/3 · B1 4/4/3/4 · B2 4/3/4/4 · B3 3/4/4/4 · Exam-wide 15/15/15/15 | Each block within 1 of 4/4/4/3 (no letter <3/>5); exam-wide within 1 of 15/15/15/15 | **PASS** | — |
| 3 | Stem/option word count | Stems 36-53(median)-69; options 9-27 | Stem median 50-55 (cap 95); option cap 35 | **PASS** | — |
| 4 | Block domain tally vs primary | B0 primary-min 2 > nonprimary-max 1; B1 3>1; B2 2>1; B3 2>1; exam-wide D1:16 D2:11 D3:12 D4:12 D5:9 | Every primary domain outnumbers every non-primary in its block | **PASS** | — |
| 5 | Inline code/config token rate | 64/240 options = 26.7% | Target 20-25%; acceptable 15-30% | **PASS** (top of band, no rewrite needed) | — |
| 6 | Scenario-rotation disclosure line | Not yet on any artifact | Must appear verbatim on landing card | **PENDING → Slice G** | To be added during HTML build |

**Citation-collision tally (PB-19):** 2 sections tested as primary (whyRight) twice — both are the pre-declared D2 repeats (D2 has 11 questions across only 9 sections):
- **§2.3** — g4 (business-error vs protocol-error semantics: refund denial is a valid outcome, not a failure) vs g49 (structured error *content* enabling retry-with-feedback: OCR failure needs failure-type/attempted/partial-output for a corrective retry). Read both in full: different underlying lesson, different correct-answer shape. **No collision.**
- **§2.6** — g3 (MCP primitive taxonomy: tools vs resources vs prompts) vs g32 (`.mcp.json` project scope vs `~/.claude.json` user scope for an experimental server). Read both in full: different underlying lesson. **No collision.** (Block 3's author flagged this as a tight facet given how narrow §2.6's config/deployment content is — confirmed genuinely distinct on read, not just citation-distinct.)

**Structural section-repeat check:** confirmed via script — the ONLY sections used more than once anywhere in the exam are the two D2 pairs above. D1 uses all 16 assigned sections exactly once, D3 all 12 once, D4 all 12 once, D5 all 9 once. No accidental collisions from planning error.

**Internal Jaccard near-duplicate scan (stem-level, threshold 0.30):** 0 pairs flagged across all 60 stems.

**Cross-block content read (semantic, catches what citation/Jaccard checks structurally can't — per GENERATION-INTELLIGENCE.md's Exam 8/9 findings):** manually read all 11 D2 questions side by side (D2 is this project's historically highest-collision domain) — 11 distinct lessons, no thematic overlap beyond the two already-cleared citation pairs above.

**Verdict: all 6 gate checks pass or are correctly deferred to Slice G. No content fixes required — the exam ships as authored.**

Next: Slice G (HTML build), then Slice H (logging).
