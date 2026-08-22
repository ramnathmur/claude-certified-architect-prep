# CCDV-F Corpus Index

**Status:** ✅ **Unblocked.** The official guide (v1.0, July 2026) is filed at
`../sources/CCDV-F_Official-Exam-Guide_v1.0.pdf` and reconciled into `../EXAM-FACTS_v1.md`.
Domain files can now be created against confirmed weights.

**No domain files exist yet** — Phase 3 builds them. The structure below is fixed and permanent.

---

## Phase 0 reconciliation — CLOSED 2026-08-19

| Check | Result |
|---|---|
| Domain list | ✅ **8 domains, 25 skills**, all with published percentages |
| Weightings | ✅ 14.7 / 33.1 / 3.1 / 2.6 / 16.8 / 11.0 / 8.1 / 10.6. Skill weights sum exactly to their domain; domains sum to 100.0 (verified) |
| Item count | ✅ **53 items, 120 minutes** |
| Item structure | ✅ **Standalone.** "Multiple-choice and multiple-response items; each item states how many responses to select." **No scenario blocks** — the CCAR-F block architecture is not needed |
| "Applications and Integration" at 33.1% | ✅ Six named skills. **13.6 of its 33.1 points are generic software engineering and solution work**, not Claude-specific |
| Eval at 2.6%, Claude Code at 3.1% | ✅ **Correct as published.** The prep-path lesson minutes do not track exam weight |
| "Accelerators & IP Contribution" | ✅ **Not on the blueprint.** 155 min of the prep path is partner enablement, not exam prep |
| Objective list | ✅ 25 skills with individual weights — finer granularity than CCAR-F's 37 objectives had |
| Guide version and date | ✅ **v1.0, effective July 2026.** Initial publication. Re-check quarterly — the guide is "subject to change without notice" |
| Program-wide facts | ✅ Confirmed per-exam: 720 on 100–1,000, 12-month validity, closed book, 4 attempts/rolling year with 14/30/90-day waits |
| Code items / languages | ✅ Effectively answered. All three sample items are judgement scenarios with **no code shown and none asked for**. Python/TypeScript proficiency is recommended experience, not an item format |
| MCP spec revision | ✅ **Not named in the guide.** The published skill scope is conceptual — resources/tools/prompts, stdio vs sockets, client vs server. Spec-version trivia is out of scope |

### Still open — the guide does not say

- [ ] **Multiple-response scoring: all-or-nothing or partial credit?** Not stated in v1.0. On CCAR-F it
      was all-or-nothing and cost eight marks. **Keep assuming all-or-nothing.** Confirm from the real
      score report after the sitting.
- [ ] **Does the score report break down below domain level?** The guide says percent-correct "within
      each content domain" — 8 domains, likely not the 25 skills. CCAR-F's report exposed 37
      objectives, so this may be coarser.

---

## Corpus files — fixed structure

Eight files, one per domain. **Section numbering follows the guide's own skill order and is permanent
from creation.** Misses are logged by section, so this numbering must never be revised.

| File | Domain | Weight | ≈items |
|---|---|---|---|
| `CCDV-F_Domain-1_v1.md` | Agents and Workflows | 14.7% | 7.8 |
| `CCDV-F_Domain-2_v1.md` | Applications and Integration | 33.1% | 17.5 |
| `CCDV-F_Domain-3_v1.md` | Claude Code | 3.1% | 1.6 |
| `CCDV-F_Domain-4_v1.md` | Eval, Testing, and Debugging | 2.6% | 1.4 |
| `CCDV-F_Domain-5_v1.md` | Model Selection and Optimization | 16.8% | 8.9 |
| `CCDV-F_Domain-6_v1.md` | Prompt and Context Engineering | 11.0% | 5.8 |
| `CCDV-F_Domain-7_v1.md` | Security and Safety | 8.1% | 4.3 |
| `CCDV-F_Domain-8_v1.md` | Tools and MCPs | 10.6% | 5.6 |

### Section map — 25 skills, permanent numbering

| § | Skill | % | Build priority | Status |
|---|---|---|---|---|
| 1.1 | Agent Architecture | 4.5 | 5 — carries a 0% objective | not created |
| 1.2 | Agent Construction with Claude | 5.3 | **4** | not created |
| 1.3 | Agent Patterns and Frameworks | 4.9 | 5 — carries a 0% objective | not created |
| 2.1 | Understanding Requirements | 3.4 | 6 — cheap points | not created |
| 2.2 | Systems Life Cycle | 2.8 | 6 — cheap points | not created |
| 2.3 | Claude API Mechanics | 6.8 | **2** | not created |
| 2.4 | Software Engineering Foundations | 7.4 | 6 — cheap points | not created |
| 2.5 | **Claude Application Design** | **8.6** | **1 — largest skill, entirely new** | not created |
| 2.6 | Configuration Management | 4.1 | **5 — the documented 0%** | not created |
| 3.1 | Claude Code Operation | 3.1 | **5 — the documented 0%** | not created |
| 4.1 | Debugging and Error Handling | 2.6 | 7 | not created |
| 5.1 | LLM Fundamentals | 5.2 | 7 — port | not created |
| 5.2 | Technical Fundamentals | 6.1 | **2** | not created |
| 5.3 | Model Selection and Tradeoffs | 2.7 | 7 — port | not created |
| 5.4 | Cost and Token Management | 2.8 | 7 — port | not created |
| 6.1 | Context Engineering | 3.8 | 5 — carries a 0% objective | not created |
| 6.2 | Prompt Engineering | 4.6 | 7 — port | not created |
| 6.3 | Output Handling | 2.6 | 7 — port | not created |
| 7.1 | AI Application Security | 3.2 | **3** | not created |
| 7.2 | Guardrails and Safe Deployment | 2.3 | **3** | not created |
| 7.3 | Claude Hooks | 1.0 | **3** | not created |
| 7.4 | Identity, Secrets, and Key Management | 1.6 | **3** | not created |
| 8.1 | Tool Implementation | 4.4 | 7 — port | not created |
| 8.2 | MCP Server Development | 2.1 | 4 — write after Phase 2 builds one | not created |
| 8.3 | Agentic Customization | 4.1 | 4 — write after Phase 2 builds one | not created |

Priority is **weight × gap**, not weight alone. Full reasoning in `../ROADMAP.md`.

---

## The six CCAR-F 0% objectives — placed against real sections

These are the only documented, specific weaknesses that exist. They are written first, whatever the
build order otherwise says.

| CCAR-F 0% objective | Lands in | § |
|---|---|---|
| Claude Code configuration mechanism — CLAUDE.md / `.claude/rules/` / Skills / hooks / settings | Configuration Management + Claude Code Operation | 2.6, 3.1 |
| Agentic review architecture — plan mode vs direct execution vs multi-phase | Agent Architecture | 1.1 |
| Diagnosing misconfigured subagent spawning | Agent Architecture + Agent Construction | 1.1, 1.2 |
| Dynamic subtask decomposition | Agent Patterns and Frameworks | 1.3 |
| Claude Code review configurations | Claude Code Operation | 3.1 |
| Context window optimisation — summarisation, sliding windows, structured state | Context Engineering | 6.1 |

Between them they touch roughly **17% of the paper**. Two of the six were open in the CCAR-F mock
corpus for weeks before they cost marks on the real sitting.

---

## Head starts — material that already exists

| Target § | Existing asset | Where |
|---|---|---|
| 6.2 Prompt Engineering · 6.1 Context Engineering | CCAR-F `CCA-Prep_Domain-4_v2.md` + `Domain-5_v2.md` | `..\..\CCAR-F - Claude Certified Architect Foundations\prep with quiz\` |
| 8.1 Tool Implementation | CCAR-F `CCA-Prep_Domain-2_v2.md` | Same folder |
| 1.1 Agent Architecture · 1.3 Agent Patterns | CCAR-F `CCA-Prep_Domain-1_v2.md` | Same folder |
| 2.6 · 3.1 Configuration / Claude Code | CCAR-F `CCA-Prep_Domain-3_v2.md` — **and the 0% lives here** | Same folder |
| 5.1 · 5.3 · 5.4 Model and token material | CCAR-F corpus, scattered | Same folder |
| 6.3 Output Handling | CCAR-F extraction-schema material — scored 100% on the real paper | Same folder |
| 4.1 Debugging | Eval Design Blueprint | `my blueprints\eval-blueprint\` — design altitude, and note v1.0 lists **no eval-design skill**, only debugging |
| 2.4 · 2.1 · 2.2 Generic SE, requirements, life cycle | Ram's own consulting practice | Needs exam-shaping, not learning |
| 8.2 MCP Server Development · 8.3 Agentic Customization | **Phase 2 build output** | Write these after building one |
| 2.5 Claude Application Design · 5.2 Technical Fundamentals · 7.x Security | **nothing** | Build from docs + the official lessons |

---

## Notes for whoever writes the corpus

**Section numbering is the guide's, not ours.** Sections follow the published skill order inside each
domain. That means numbering can be fixed on day one and never revised, which is what makes the miss
log durable.

**No block architecture.** Items are standalone and each states its own response count. Do not build
scenario groupings — CCAR-F needed them, this exam does not.

**Write for judgement, not syntax.** All three official sample items are scenario-plus-four-options
with no code. Sections should state the decision and its discriminator. Code belongs in a section only
where the decision is *about* the code — schema design, defensive parsing, error handling — and even
then the question is which approach, not what the parameter is called. See
`CCDV-F_Domain-Template_v1.md`.

**Distractor families, taken from the guide's own samples.** The three official rationales reject
wrong options in recognisable ways worth copying: an irrelevant lever (raise temperature against
prompt injection), a non-enforceable control (ask users politely in the system prompt), a
bigger-hammer answer (switch to a larger model), and a false-capability claim (built-in tools reach any
internal API). Those sit alongside the six families carried from CCAR-F.
