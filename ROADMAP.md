# ROADMAP — Claude Certified Architect Prep

**Target:** Pass CCA-F exam
**Last updated:** 2026-06-06

> Detailed per-course/extension tracker (KB sizes, gate scores, artifacts): `courses/COURSE-ROADMAP.md`.
> Extension topic briefs + sources: `courses/EXTENSION-RECOMMENDATION.md`.
> Resume state for next session: `resume-prompt.md`.

---

## 📍 Status at a glance (2026-06-06)

| Track | Done | Pending |
|---|---|---|
| **Base courses** | ✅ 2/2 — Claude 101, Introduction to Subagents | — |
| **Launchpad dashboard** | ✅ Shipped + redesigned (all live cards in sync) | 🟡 optional "should-do" polish tier (deferred) |
| **Extensions** | ✅ **9 COMPLETE** — S-E1, C-E1, C-E2, S-E2, C-E3, S-E3, C-E4, C-E5, **C-E6 (D2, 2026-06-06)** | — |
| **Domain coverage** | ✅ **all 5 domains now have exam-depth lessons** — D2 gap closed by C-E6 | 🟡 optional D2 202 companion |
| **Slice 1** (D1/D4 heavy) | ✅ COMPLETE — S-E2, C-E3, S-E3 | — |
| **Slice 2** (economics + prompt craft) | ✅ COMPLETE — C-E4, C-E5 (both 2026-06-06) | — |
| **Cross-navigation** | ✅ `.cnav` Home/Prev/Next bar on all 11 lesson files; full chain verified end-to-end | — |
| **Forward-link debt** | ✅ ZERO — every forward/back link across all files resolves on disk | — |
| **Phase 1 prep tasks** | ✅ pipeline + Claude 101 + index | ⬜ scope decision, 200-level courses, community PDF, 25 practice Qs, exam access via Infosys |
| **Phase 2 curriculum** (separate track) | ✅ CURRICULUM.md + GAPS.md scaffolded | ⬜ Modules 0–7 not yet run |

**▶ Next action:** The interactive course + extension build track is **COMPLETE (9 extensions, both gates PASS, full cross-navigation)** and **all 5 exam domains now have an exam-depth lesson** (D2 gap closed by C-E6, 2026-06-06). Shift to either (a) **Phase-2 curriculum** Modules 0–7 (active-recall study track) or (b) **Phase-1 exam-prep tasks** (200-level courses, community PDF, 25 practice Qs, exam access via Infosys). Full brief in `resume-prompt.md`.

---

## Phase 1 — Acquire Prep Material
- [x] Create project folder and CLAUDE.md
- [x] Research exam structure, domains, and resources
- [x] Create PREP-MATERIAL-INDEX.md
- [x] Build Academy course → interactive HTML pipeline (`prompts/Academy-Course-to-HTML_Prompt_v1.md`)
- [x] Convert **Claude 101** to interactive HTML (both QA gates passed) → `courses/claude-101/claude-101.html`
- [ ] Decide scope for remaining Academy courses (see `courses/COURSE-ROADMAP.md`)
- [ ] Complete Anthropic Academy 200-level courses (https://anthropic.skilljar.com/)
- [ ] Download community PDF guide (daronyondem/claude-architect-exam-guide)
- [ ] Work through claudecertifications.com 25 practice questions
- [ ] Request exam access via Infosys / Claude Partner Network

---

## Interactive Course + Extension Track (primary build effort)

Self-contained, QA-gated interactive HTML. Two base courses captured from Academy; "extension" files add web-researched, source-cited, architect-depth material on top. **Front door:** `Launchpad.html` (kept in sync as each file ships).

### Base courses — COMPLETE (both gates PASS)
- [x] **Claude 101** — 14 lessons → `courses/claude-101/claude-101.html`
- [x] **Introduction to Subagents** — 4 lessons → `courses/introduction-to-subagents/introduction-to-subagents.html`
- [x] **Launchpad dashboard** — `Launchpad.html` (data-driven; Gate-2 PASS)

### Extensions — 9 SHIPPED (all 5 domains covered)
| ID | Title | Base | Domain | Status |
|---|---|---|---|---|
| S-E1 | The Five Orchestration Patterns | Subagents | D1 (27%) | [x] Shipped (pilot) — G1 0/0/2, G2 0/0/3 |
| C-E1 | The Tool-Use Agent Loop | Claude 101 | D4 (18%)+D1 | [x] Shipped (pilot) — G1 0/0/0, G2 0/0/3 |
| C-E2 | Context Management & Reliability | Claude 101 | D5 (15%)+D1 | [x] Shipped 2026-06-05 — G1 0/0/3, G2 0/0/2 |
| S-E2 | Subagents as a Programmable Primitive (SDK) | Subagents | D1 (27%)+D2 | [x] Shipped 2026-06-05 — G1 0/0/3, G2 0/0/3 |
| C-E3 | MCP at a Builder Level | Claude 101 | D4 (18%) | [x] Shipped 2026-06-05 — G1 0/0/3, G2 0/0/3 |
| C-E4 | Prompt Caching Economics | Claude 101 | D5 (15%) | [x] Shipped 2026-06-06 — G1 0/0/3, G2 0/0/2 |
| C-E5 | Prompt Engineering Depth + Model Selection | Claude 101 | D3 (20%) | [x] Shipped 2026-06-06 — G1 0/0/3, G2 0/0/1 |
| S-E3 | Orchestrator-Worker at Scale + Failure Modes | Subagents | D1 (27%)+D5 | [x] Shipped 2026-06-06 — G1 0/0/2, G2 0/0/3 |
| C-E6 | Claude Code Configuration & Workflows | Claude 101 | **D2 (20%)** | [x] Shipped 2026-06-06 — G1 0/0/4, G2 0/0/2. **Closes the D2 exam gap.** Fresh research (15 PRIMARY sources). C-track END. |

**Pipeline per extension (do later):** `prompts/Extension-Material-Generation_Prompt_v1.md` → web-researcher → cited `source/<slug>_citations.md` → 4-persona build team → 2 QA gates (PASS = 0 blk/0 maj) → ship → **wire into `Launchpad.html` same session**.

---

## Remaining extensions — two-slice plan (for a later session)

Sliced by exam weight + dependency-resolution, not just count. Each slice is one focused working session.

### ▸ Slice 1 — Heaviest domains + builder depth (✅ 3 of 3 shipped — COMPLETE)
Covers Domain 1 (27%, the heaviest) end-to-end plus Domain 4 MCP (18%). Highest exam ROI; clears C-E2's forward link.
- [x] **S-E2 — Subagents as a Programmable Primitive (SDK)** · D1 (27%) + D2 (20%). Shipped 2026-06-05 (G1 0/0/3, G2 0/0/3). Resolves S-E1's forward link.
- [x] **C-E3 — MCP at a Builder Level** · D4 (18%). Shipped 2026-06-05 (G1 0/0/3, G2 0/0/3). Resolves C-E2's "What's next" forward link (`mcp-at-a-builder-level.html`).
- [x] **S-E3 — Orchestrator-Worker at Scale + Failure Modes** · D1 (27%) + D5 (15%). Shipped 2026-06-06 (G1 0/0/2, G2 0/0/3). Anthropic's multi-agent research system as a reference architecture + named failure modes. Resolves S-E2's forward link (`orchestrator-worker-at-scale.html`).

**Suggested order within slice:** ~~S-E2~~ → C-E3 → S-E3.
**Exit check:** all 3 ship with both gates PASS; Launchpad cards flipped to `live`; S-E1/S-E2 and C-E2 forward links resolve.

### ▸ Slice 2 — Economics + prompt craft (✅ 2 of 2 shipped — COMPLETE)
The applied cost lever + prompt-engineering judgment. Lower weight but high scenario-test likelihood.
- [x] **C-E4 — Prompt Caching Economics** · D5 (15%). Shipped 2026-06-06 (G1 0/0/3, G2 0/0/2). Closes C-E2's "full treatment in C-E4" caching deferral (`cache_control`, breakpoints, write/read multipliers 1.25×/2×/0.1×, min-prefix sizes, break-even math). Resolves C-E3's forward link.
- [x] **C-E5 — Prompt Engineering Depth + Model Selection** · D3 (20%). Shipped 2026-06-06 (G1 0/0/3, G2 0/0/1). The technique ladder, examples-as-highest-leverage, adaptive-thinking vs manual CoT, structured-output tiers (incl. prefill-now-legacy on 4.6+), and the Opus/Sonnet/Haiku selection framework. Resolves C-E4's forward link. **Final file — completes the 8/8 set.**

**Order within slice:** ~~C-E4~~ → ~~C-E5~~ — both done.
**Exit check:** ✅ both shipped (both gates PASS, Launchpad live, all forward links resolve). Extension build track COMPLETE.

> ⚠ **Standing rule:** every shipped file updates `Launchpad.html` in the same session (flip `status:'queued'`→`'live'` + add `href`). See `Launchpad-DESIGN-NOTES.md` §5.
> ⚠ **Re-verify `[VERIFY]` facts** (model lineup/sizes, dated beta headers, prices) against live docs at each build — they drift.

---

## Phase 2 — Build Training Course (separate track, not yet started)
- [x] Design curriculum structure (CURRICULUM.md)
- [x] Create GAPS.md and folder structure
- [ ] Run Module 0 — Foundations & Exam Orientation
- [ ] Run Module 1 — Agentic Architecture & Orchestration
- [ ] Run Module 2 — Claude Code Configuration & Workflows
- [ ] Run Module 3 — Prompt Engineering & Structured Output
- [ ] Run Module 4 — Tool Design & MCP Integration
- [ ] Run Module 5 — Context Management & Reliability

## Phase 3 — Practice + Assessment
- [ ] Run Module 6 — Scenario Simulation Lab (all 6 scenarios)
- [ ] Run Module 7 — Mock Exam + Gap Review
- [ ] Second mock exam if any domain < 70%
- [ ] Final gap review
- [ ] Book exam seat
- [ ] Sit exam
