# CCA-F Prep — Content & Visual Enhancement Recommendations (for review & approval)

**Date:** 2026-06-09
**Method:** Two personas from Ram's AI Persona Library evaluated the existing material, in character, grounded in the actual files:
- **Content/learning** → *Senior Curriculum Architect* (structure, prereq graph, assessment placement). *AI Professor considered.*
- **Visual experience** → *Editorial Director / Long-Form HTML Synthesist* (IA, density, illustration cadence). *Senior Visual Designer considered but rejected — it's deck-scoped; the material is long-form HTML. UI Designer also considered.*
- Both invocations self-reported to `~/.persona-library/invocation-log.jsonl` per the library's logging contract.

> **BUILD STATUS (2026-06-09):** Approved & **DONE** — V-P0-1 (Launchpad tier toggle), V-P0-2 (C-E6 settings-merge + exit-code diagrams), C-P0-1 (3 integration checkpoints), **V-P1 COMPLETE** (static 202 cost-curve/pipeline/escalation diagrams ported into the 101 orchestrator lesson; four-extension-surfaces diagram added to C-E6; course spine in all 11 lesson sidebars; `EXAM-DIGEST.html` cram page built + linked from the Launchpad). Plus a **pre-exam [VERIFY] sweep** (`QA-VERIFY-SWEEP_2026-06-09.md`): ~89 facts confirmed, `PostToolBatch`-blockable fix applied, `@agent-name` resolved. **PENDING (live, Ram's to run)** — C-P0-2 real baseline. **OPTIONAL remaining sliver** — per-lesson "Reference & anti-patterns" anchored mini-index (the course-wide `EXAM-DIGEST.html` already serves the retrieval need). **Not approved this round** — C-P1 (anti-pattern drill), C-P2 (spaced-review, 202 sibling).

> **Headline:** Topic coverage is essentially **complete** — all 5 domains have an exam-depth lesson + weighted practice. The gaps are **structural** (how units connect, how the learner integrates and re-finds), not "missing topics." Recommendations below are connective tissue + retrieval affordances, not rewrites.

---

## A. Content recommendations (Senior Curriculum Architect)

| ID | Recommendation | Type | Why (transfer failure it prevents) | Priority |
|---|---|---|---|---|
| C-P0-1 | **3 cross-domain integration checkpoints** — CP-A D1×D5 (support: escalation+compaction), CP-B D2×D3 (CI/CD: headless+structured output), CP-C D1×D4 (multi-agent: delegation+tool/error design). Placed *after* the paired lessons, *before* the Scenario Lab. | Integrative checkpoints | **Single-integration-point risk** — today it's ~12 isolated lessons → one terminal lab → one mock. Domains never combine until the end; the exam *is* the combination. | **P0** |
| C-P0-2 | **Real baseline run for D1 + D3** (47% of exam). | Diagnostic assessment | Every Module 0–5 score is ⚠ *synthetic* — the prereq graph is built on unmeasured edges. Can't place formative gates until ≥1 real measurement exists. | **P0** |
| C-P1-1 | **Mixed anti-pattern drill** — shuffled, *domain-blind* "spot-the-flaw" items (learner must first classify the domain). | Formative assessment | Anti-patterns are scattered per-lesson; the exam presents them unlabeled and over-weights them. Removes the "I know which domain I'm in" crutch. | **P1** |
| C-P1-2 | **"Two killer edges" drill** — compliance-in-code-not-prompt (D1×D4) + Structured-Outputs-vs-retry (D3×D4). | Integrative checkpoint | Both are *logged GAPS.md* misses + high-yield digest traps; taught inside lessons but never as the collision edge. | **P1** |
| C-P2-1 | **Spaced-review cycler** — reads open `GAPS.md` entries, runs the "3 clean recalls → Resolved" protocol on a cadence. | Spaced-review unit | Methodology mandates spaced repetition but nothing operationalizes it; mastery decays before exam day. | **P2** |
| C-P2-2 | **Resolve the orphan 202 tier** — add 1 sibling 202 (D3 or D4, the densest mechanism areas) *or* explicitly park the pilot. | Sequencing decision | The 202 pilot is a D1-only dead-end branch with no prereq contract or successor. | **P2** |

**Build order (dependency-justified):** C-P0-2 (baseline) → C-P0-1 (checkpoints) → C-P1-1 (anti-pattern drill) → C-P1-2 (killer edges) → C-P2-1 (spaced review) → C-P2-2 (202 decision).

---

## B. Visual / experience recommendations (Editorial Director)

**Archetype call:** the lessons are a **tutorial/reference hybrid** but the navigation is **tutorial-only** (single sticky TOC, scroll-to-learn). The dense reference tables (precedence ladders, exit-code table, scope maps) can't be *re-found* fast in the exam-eve cram window the `EXAM-DIGEST` is built for. That mismatch is the central IA gap.

| ID | Recommendation | Lever | Priority |
|---|---|---|---|
| V-P0-1 | **Ship the All / 101 / 202 tier toggle** on the Launchpad. Data already carries `tier`; the badge + CSS exist; only the control is missing. Default "All", 202 badged. | Navigation/IA | **P0** |
| V-P0-2 | **Add the 2 highest-yield decision diagrams in C-E6:** (a) hook exit-code branching (0/1/2 → outcome), (b) settings-override-vs-permission-rules-merge side-by-side. Both are counter-intuitive traps + logged gaps, currently buried in tables/side-boxes. | Illustration cadence | **P0** |
| V-P1-1 | **Whole-course spine in the lesson sidebar** — collapsed list of sibling lessons in the track, current highlighted ("lesson X of N"). Today "where am I in the course" is only answerable at the hub. | Navigation/IA | **P1** |
| V-P1-2 | **Returning-learner lookup path** — per-lesson "Reference & anti-patterns" mini-index (anchors to every table + warn callout) + link `EXAM-DIGEST` as the course-wide cram index from the Launchpad. | Navigation/IA | **P1** |
| V-P1-3 | **Port the 202's cost-curve + pipeline as STATIC SVGs into the 101 agentic lessons; add escalation + four-extension-surfaces decision diagrams.** (Static only — no live widgets in 101.) | Illustration cadence | **P1** |
| V-P2-1 | **Trim the hero preamble** (5–6 stacked banners before any teaching → merge crosslink+examnote into one "exam map"; keep provenance/currency). **Sub-divide C-E6 Section E (Hooks, ~22 min) into E1/E2** for two TOC handholds. | Density | **P2** |
| V-P2-2 | **Derive prev/next from a single lesson-order manifest** (the Launchpad DATA array) instead of hand-wiring each file's cnav. | Navigation/IA (eng half) | **P2** |

**Referrals (explicitly out of the Editorial Director's scope):**
- *Aesthetic styling* (colors, type, the tier-toggle chrome, the "reference density tier" look) → **Senior Visual Designer**.
- *Interactivity / JS* (tier-toggle logic, manifest-driven nav, sidebar spine wiring; live 101 widgets — earn-condition contested) → **Senior Frontend Engineer**.
- *Prose/captions* for new diagrams + the merged exam-map block → **Senior Tech Writer**.

---

## C. Where the two lenses agree (do-these-first synergies)
- **The terminal mock should be gated** (Curriculum) — and the **timed Mock Exam 1** already queued in `practice/` is exactly that capstone; just sequence it after the integration checkpoints.
- **C-E6 is the densest, highest-stakes lesson** — both personas point at it: add its 2 missing decision diagrams (V-P0-2) *and* it's the D2 anchor for the integration work.
- **Anti-patterns are the exam's center of gravity** — the content drill (C-P1-1) and the visual decision-diagrams (V-P1-3) both target the same weak spot from different sides.

---

## D. Honest caveats (from the personas' own reflection axes)
- Curriculum: cross-edges (D1→D4/D5) are inferred from the curriculum's own claim, not a *measured* dependency — which is why **the real baseline (C-P0-2) is sequenced first**.
- Editorial: the "densest lesson" claim sums *stated* section minutes (directional, not measured); the prev/next-manifest fix assumes no manifest exists beyond the Launchpad DATA array; possible duplicate schematics in the 10–11-figure lessons weren't deep-read (flagged for a cadence audit).

---

_Full raw persona outputs (Generation-family JSON with reflection axes) are in this session's transcript. This file is the synthesis for approval._
