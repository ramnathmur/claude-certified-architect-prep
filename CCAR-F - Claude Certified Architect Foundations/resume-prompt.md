# Resume Prompt — Claude Certified Architect Prep (Academy → HTML + Extensions)
_Generated: 2026-06-06 (updated after **C-E6 ship — D2 exam gap CLOSED; extension set now 9 files**) • Working dir: C:\Claude Cowork\Projects\Claude Certified Architect Prep_

> 🆕 **NEW TRACK STARTED — 202 Deep-Mastery tier.** A second depth tier is underway (interactive, mastery-level companions to the 101 exam lessons). **1 of ~7 shipped (S-E3 pilot).** Its dedicated handoff is **`ROADMAP-202.md`** — read that FIRST if continuing the 202 work; it opens with a reminder to eyeball the pilot lesson and give feedback before building more.

## Context
Ram is prepping for the Claude Certified Architect — Foundations (CCA-F) exam. This project converts free Anthropic Academy courses into self-contained interactive HTML, then adds web-researched, source-cited, architect-depth **"extension" (level-up)** lessons on top of each base course, all surfaced through a single `Launchpad.html` dashboard. Exam access is unlocked via Infosys (Claude Partner Network).

## What's done — INTERACTIVE BUILD TRACK COMPLETE ✅
- **Base courses SHIPPED (both gates PASS):** Claude 101 (14 lessons) · Introduction to Subagents (4 lessons).
- **🆕 C-E6 Claude Code Configuration & Workflows** · **D2** · `courses/claude-101/extensions/claude-code-configuration.html` (~146 KB, 8 sections A–H, 7 SVGs, 17 inline MCQs + 10-Q quiz). Shipped 2026-06-06. **Closes the Domain-2 exam gap (20% of the exam, previously zero coverage at either tier.)** Both gates PASS (G1 fidelity 0/0/4, G2 build/interactivity 0/0/2; high-value minors fixed). Fresh web research → `source/claude-code-configuration_citations.md` (15 PRIMARY sources, all from `code.claude.com/docs`). Now the C-track END (Prev ← C-E5, no Next). Rendered-verified: 0 JS errors, TOC 9/9 resolve, 0 dup IDs.
- **Extensions SHIPPED — original full set, 8 of 8 (every file both gates PASS):**
  - **S-E1 Orchestration Patterns** · D1 · `courses/introduction-to-subagents/extensions/orchestration-patterns.html`
  - **C-E1 Tool-Use Agent Loop** · D4+D1 · `courses/claude-101/extensions/tool-use-agent-loop.html`
  - **C-E2 Context Management & Reliability** · D5+D1 · `courses/claude-101/extensions/context-management-reliability.html` (G1 0/0/3, G2 0/0/2)
  - **S-E2 Subagents as a Programmable Primitive / SDK** · D1+D2 · `courses/introduction-to-subagents/extensions/subagents-as-sdk-primitive.html` (G1 0/0/3, G2 0/0/3)
  - **C-E3 MCP at a Builder Level** · D4 · `courses/claude-101/extensions/mcp-at-a-builder-level.html` (G1 0/0/3, G2 0/0/3)
  - **S-E3 Orchestrator-Worker at Scale + Failure Modes** · D1+D5 · `courses/introduction-to-subagents/extensions/orchestrator-worker-at-scale.html` (G1 0/0/2, G2 0/0/3). Closed Slice 1.
  - **C-E4 Prompt Caching Economics** · D5 · `courses/claude-101/extensions/prompt-caching-economics.html` (G1 0/0/3, G2 0/0/2). Multipliers + break-even math + TTL gotcha.
  - **C-E5 Prompt Engineering Depth + Model Selection** · D3 · `courses/claude-101/extensions/prompt-engineering-depth.html` (~131 KB, 7 SVGs, 12 inline MCQs + 10-Q quiz) — G1 0/0/3, G2 0/0/1. Shipped 2026-06-06. **FINAL file — completes the 8/8 set.** The technique ladder, examples-as-highest-leverage, adaptive-thinking vs manual CoT, the three structured-output tiers (incl. **prefill-now-legacy on 4.6+** and **manual `budget_tokens` removed on Opus 4.7+ → adaptive+effort**), and the Opus/Sonnet/Haiku selection framework. Resolves C-E4's forward link.
- **Cross-navigation system COMPLETE + verified:** every lesson file carries the standardized `.cnav` bar (`⌂ Launchpad · ← Prev · Next →`) after `<div class="wrap">`, plus a back-link to its base course. Full chain verified by synthetic traversal (BFS reachability + per-file home round-trip + prev/next continuity, all links resolve on disk) AND rendered Gate-2 rechecks (DOM geometry / computed styles via local preview server). Track-starts omit Prev; the two track-ends (S-E3, C-E5) omit Next. **Zero forward-link debt.**
- **Launchpad SHIPPED + REDESIGNED:** `Launchpad.html` (root). All 8 extension cards `live`.
- Pipeline prompt: `prompts/Extension-Material-Generation_Prompt_v1.md`. `ROADMAP.md` has a 📍 Status-at-a-glance table.

## Session 2026-06-09 — Phase-1 digest + practice + persona-driven enhancements
- **Phase-1 community guide DIGESTED** → `EXAM-DIGEST.md` (11 KAs mapped to 5 domains, anti-pattern cram sheet; from daronyondem guide v1.0.1, CC BY 4.0). `PREP-MATERIAL-INDEX.md` refreshed.
- **Practice bank staged** → `practice/` : 51 domain-weighted exam-style Qs (`CCA-F_practice_d1..d5*.md`) + 3 cross-domain integration checkpoints (`CCA-F_checkpoint_A/B/C_*.md`) + `practice/README.md` index. (A timed 30-Q mock was queued then deprioritized — not built.)
- **Persona-driven enhancement review** (Senior Curriculum Architect + Editorial Director) → `ENHANCEMENT-RECOMMENDATIONS_v1.md`. **DONE:** Launchpad All/101/202 tier toggle; 2 new C-E6 decision diagrams (settings-merge + exit-code, lesson now 9 figs a–i). **STAGED (approved, not built) — Visual P1:** static 202 diagram ports into 101 + escalation/four-surfaces diagrams; course spine in 11 lesson sidebars; lookup/cram path (convert EXAM-DIGEST→HTML first). See the doc's BUILD STATUS line.

## Session 2026-06-09 (cont.) — Visual P1 BUILT + [VERIFY] sweep (Sonnet-routed to use weekly headroom)
- **Visual P1 COMPLETE:** ported 202 cost-curve/pipeline/escalation as static SVGs into `orchestrator-worker-at-scale.html` (now 11 figs); added four-extension-surfaces diagram to C-E6 (now 10 figs, a–j); **course spine** in all 11 lesson sidebars (`.cspine`); **`EXAM-DIGEST.html`** cram page built + linked from Launchpad hero ("Cram sheet" button).
- **Pre-exam [VERIFY] sweep** → `QA-VERIFY-SWEEP_2026-06-09.md` (5 Sonnet researchers): ~89 confirmed; applied the `PostToolBatch`-is-blockable fix + resolved `@agent-name`; additive drifts (fork subagents, Mythos Preview, cache_creation sub-object, Sonnet 4.6 effort default, Opus 4.8 no-extended-thinking) logged for a later citations-touch pass. Re-run near exam day.

## What's open (build track done — these are the remaining project tracks)
- **Optional sliver:** per-lesson "Reference & anti-patterns" anchored mini-index (the course-wide `EXAM-DIGEST.html` already covers retrieval). ~~Apply the additive [VERIFY] drifts to the 9 citation files~~ → **DONE 2026-06-10 (citations-touch pass):** all 9 citation files now carry a "Re-verified 2026-06-09" manifest line + a dated re-verification addendum with the additive drifts (fork subagents, Mythos Preview tool_choice/Structured-Outputs, `cache_creation` sub-object, Sonnet 4.6 `high`-effort default, Opus 4.8 no-extended-thinking, no per-turn concurrency cap, 1M no-beta-header resolved, MCP `2025-11-25` re-confirmed). Note: citation FILES updated only — the lesson HTML bodies were NOT touched (drifts are additive, not reversals; no inline lesson claim was wrong).
- **Phase-3 real baseline:** every Module 0–5 quiz score is ⚠ synthetic. Run a per-domain bank or checkpoint LIVE for a true baseline; log to `GAPS.md`. The instrument exists (`practice/`).
- **Phase-2 curriculum (active-recall study track):** `CURRICULUM.md` + `GAPS.md` scaffolded; **Modules 0–7 not yet run for real** (all prior runs synthetic).
- **Phase-1 exam-prep tasks remaining:** complete Academy 200-level courses; **request exam access via Infosys / Claude Partner Network** (Ram's action — account/access). 25 claudecertifications.com Qs optional supplement (now superseded by the original 51-Q bank).
- Optional Launchpad 🟡 Should-do polish tier still deferred.

## Next action (do this first)
The interactive course + extension build track is **COMPLETE (9 files now — 8 original + the new D2 lesson; both gates PASS, full cross-navigation, zero broken links)**. **The Domain-2 exam gap is now closed.** Two follow-ons remain optional: (i) eyeball the pilot 202 lesson to unlock the rest of the 202 deep-mastery tier (see `ROADMAP-202.md`); (ii) build a **D2 202 companion** later. Confirm with Ram which track to pursue next:
- **(a) Phase-2 curriculum** — run Module 0 (Foundations & Exam Orientation) using the AI-first methodology in `CLAUDE.md` (active recall, predict-before-reveal, 5-Q quizzes, log gaps in `GAPS.md`), then Modules 1–7.
- **(b) Phase-1 exam-prep** — the resource-gathering + practice-question + exam-access tasks above.
- **(c) Polish** — the optional Launchpad should-do tier, or a `[VERIFY]`-fact refresh sweep across all 8 extensions before exam day.
Use `AskUserQuestion` to let Ram choose.

## Decisions locked in
- **Extension scope = FULL SET (8 files) — DONE.** No more extensions planned. If Ram ever wants more, follow the same pipeline + the cross-navigation contract below.
- **Cross-navigation contract:** every lesson file has the standardized `.cnav` bar (Home/Prev/Next) right after `<div class="wrap">`; self-contained inline `<style>`; fallback CSS vars (`var(--accent,#c96442)`); `margin:10px 0 18px` to clear the 4px fixed progress bar. When a new file ships, update the prior file's Next link + remove any "may 404" caveat. Launchpad stays the single source of truth (no separate master-nav file).
- **Extension grounding rule:** WEB-RESEARCHED, not Academy-captured. Each has a cited `extensions/source/<slug>_citations.md` that Gate 1 diffs against; every claim traces to a source; version-sensitive facts carry `[VERIFY]` surfaced as visible inline notes; enrichment labeled "Extension — beyond the Academy course."
- **Launchpad design philosophy:** "over-encoded, not over-informed." Keep exam-weight %s, ≥5 domain colors, illustrations. Clay `--accent` = action/brand only; Domain-1 uses `--wine`.
- Researcher = the live `web-researcher` agent embodying the Senior Research Analyst persona (`C:\Claude Cowork\Projects\AI agents personas\`).
- Course/extension HTML = long-form scrollable document → never `/frontend-slides`. Self-contained HTML only. Open via `Start-Process chrome <path>`. Rendered-QA preview server config at `C:\Claude Cowork\Projects\.claude\launch.json` (name `cca-prep-static`, port 8099, docroot = project folder).

## Files touched (most recent session — C-E6 / Domain-2 lesson)
- **NEW C-E6:** `courses/claude-101/extensions/claude-code-configuration.html` (~146 KB) + `source/claude-code-configuration_citations.md` (15 PRIMARY sources) + `qa/gate1-claude-code-configuration.md`, `qa/gate2-claude-code-configuration.md`.
- C-E5 nav updated: added Next→C-E6 (`prompt-engineering-depth.html` cnav + nextbox rewritten — was "no next lesson").
- `Launchpad.html`: new `c-e6` card (tier:'101', domain d2) + new `config` illo case (settings sliders).
- Handoff/status files: `ROADMAP-202.md`, `resume-prompt.md`, `ROADMAP.md`.

_(Prior session — C-E5 + chain completion: `prompt-engineering-depth.html` + citations + qa; C-E4 nav; Launchpad c-e5 card.)_

## Gotchas / watch-outs
- **`[VERIFY]` facts WILL drift — biggest exam-day risk.** C-E4 (prices/multipliers/min-lengths/TTLs) and C-E5 (model lineup/IDs/pricing, prefill-removed-on-4.6+, `budget_tokens`-removed-on-4.7+, effort defaults, structured-output limits) are the most volatile. They're flagged inline; re-verify against live docs (`platform.claude.com`) before exam day.
- **✓ `[VERIFY]` refresh completed 2026-06-06:** 54 version-sensitive facts re-checked across all 8 extensions against live docs via 3 parallel web-researcher agents — **53 confirmed, 1 drifted + fixed** (MCP canonical protocol version `2025-06-18` → **`2025-11-25`** in C-E3 lesson + citations; `2025-03-26` remains the documented fallback). All pricing/model/caching/prompt-engineering/agent/SDK facts CONFIRMED current. Re-run this sweep before exam day.
- **C-E6 `[VERIFY]` watch-list (the new lesson's volatile facts):** the docs-host migration to `code.claude.com/docs`, the ~30-event hook roster (only the classic ~9 are stable), permission-mode names (`auto`/`dontAsk` are new), MCP scope renames (`local`←`project`, `user`←`global`), the June-15-2026 Agent-SDK-credit billing change, and managed-settings file paths. All flagged inline; re-verify before exam day. Full list in `source/claude-code-configuration_citations.md`.
- **C-E6 logged minors (NOT fixed — cosmetic):** live-reload-key-list tone + the "formerly Claude Code SDK" label nit (see `qa/gate1-claude-code-configuration.md`). High-value minors (diagram count, caption lettering, HKCU qualifier) were fixed.
- **Subagent gotcha:** the `web-researcher` agent type has **NO Write tool** — it returns citations content in its final message; the parent agent must persist it. (Build agent = `general-purpose`, which CAN write.)
- **Code-heavy lessons:** escape all `<`/`>` in `<pre><code>` (C-E6 is JSON/YAML/CLI-heavy: frontmatter `---`, `mcp__server`, hook JSON, `Bash(rm *)`). Gate 2 checks this.
- **Quiz denominator:** scoring uses `mcqs.length`, scoped per quiz block; no off-by-one.
- **Nav upkeep:** the contract is documented above; the synthetic link-resolution + rendered recheck scripts are in this session's history if more files are ever added.
- Preview screenshots were unreliable this session (zero-width headless window) — used DOM/computed-style + static-CSS verification instead, which is sufficient and per the tool docs more accurate for layout properties.
- This project folder is NOT a git repo — no commits expected.
