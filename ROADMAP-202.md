# ROADMAP-202 — Deep-Mastery Tier (Handoff File)
_Created 2026-06-06 · Working dir: `C:\Claude Cowork\Projects\Claude Certified Architect Prep`_
_This is a clean-start handoff. A new session should be able to read ONLY this file (plus the linked sources) and proceed with zero context loss._

---

## ⚠ DO THIS FIRST (next session)
**Open the pilot lesson in Chrome and eyeball it / give feedback BEFORE building any more 202 lessons.** The 202 template gets replicated ~6 more times, so tuning it now is far cheaper than across seven files.
```
Start-Process chrome "C:\Claude Cowork\Projects\Claude Certified Architect Prep\courses\introduction-to-subagents\deep-mastery\orchestrator-worker-at-scale-202.html"
Start-Process chrome "C:\Claude Cowork\Projects\Claude Certified Architect Prep\Launchpad.html"
```
What to pressure-test: the **cost-vs-reliability simulator** (sliders → verdict flip → inject-failure), the steppable pipeline, the 8 failure-mode cards, the diagnose widget, and whether the **101 vs 202 tier distinction** reads clearly on the Launchpad. Capture any template changes here before scaling. (Chrome MCP mangles `file://` — always open via `Start-Process chrome`.)

---

## The goal (why this tier exists)
One project, **two depth tiers aligned to two goals**, switchable from a single `Launchpad.html`:
- **101 · Exam Prep** — the 8 existing extension lessons + 2 base courses. Goal: pass the CCA-F certification. **Already shipped + `[VERIFY]`-refreshed 2026-06-06.** Do not touch.
- **202 · Deep Mastery** — new tier. Goal: genuine, lasting architect capability per subject (strong standalone takeaway, not just exam recognition). World-class, interactivity-first. **1 of ~7 shipped (pilot).**

---

## STATUS LEDGER

### ✅ Done
- **Pilot 202 lesson shipped:** `courses/introduction-to-subagents/deep-mastery/orchestrator-worker-at-scale-202.html` (~116 KB). 4 core interactive widgets (cost-vs-reliability simulator, steppable pipeline, 8 failure-mode cards, diagnose-the-architecture), 14 inline SVGs, 8 varied checkpoints. Both QA gates PASS (G1 fidelity 0/0/3, G2 build/interactivity 0/0/2). Verified rendered: 0 JS errors, 0 duplicate IDs, all `.cnav` links resolve.
- **`deep-mastery/` folder convention established** (sibling to `extensions/`), one per base course.
- **Launchpad tier system (partial):** every card now renders a tier badge — **11× "101 · Exam Prep" + 1× "202 · Deep Mastery"**. The S-E3·202 card (`id:'s-e3-202'`, `tier:'202'`) is live in the `DATA` array and launches the pilot; the lesson cross-links back to its 101 view + base course via `.cnav`. Rendered check: 12 cards, 0 JS errors.
- **Phase A evaluation locked** (which subjects warrant a 202 — see table below).

### ⬜ Pending
- **6 more 202 lessons** (see Remaining Lessons table).
- **Full Launchpad tier toggle** — an `All / 101 / 202` filter control. Badges exist; the toggle does not. (Lightweight: filter `[data-card]` articles by a `tier` data-attr.)
- **D2 202 companion** (deep-mastery tier) — optional, build after the pilot is eyeballed.

### ✅ Done (2026-06-06, later session) — D2 101 EXAM-DEPTH EXTENSION SHIPPED
- **C-E6 Claude Code Configuration & Workflows** · **D2** · `courses/claude-101/extensions/claude-code-configuration.html` (~146 KB, 8 sections A–H, 7 SVGs, 17 inline MCQs + 10-Q quiz). **Closes the Domain-2 exam gap (20%, previously zero coverage at either tier.)** This was THE priority in the Decision Log below.
  - Fresh web research done → `source/claude-code-configuration_citations.md` (15 PRIMARY sources, all `code.claude.com/docs`; 13-item [VERIFY] list). This was the "1 lesson needs fresh research" item — now resolved.
  - Both QA gates PASS (G1 fidelity 0/0/4, G2 build/interactivity 0/0/2). High-value minors fixed (diagram count, caption lettering, HKCU qualifier). Reports in `courses/claude-101/extensions/qa/`.
  - Wired into Launchpad as C-track card `id:'c-e6'`, `tier:'101'`, domain `d2`, new `config` illo (settings sliders). C-E5 updated with Next→C-E6 + nextbox rewritten (was "no next lesson"). New lesson is the C-track END (Prev←C-E5, no Next).
  - Rendered-verified via preview server: 0 JS errors on lesson + Launchpad, TOC 9/9 resolve, 0 dup IDs, 13 cards render.
  - Built on the **proven 8/8 101-extension pipeline** (NOT the 202 template) — so it was safe to build ahead of the pilot-eyeball gate.

---

## DECISION LOG
**2026-06-06 — re-evaluation of the original three offered fixes (build D2 / add depth-tier labels / add canonical path):**
- **Depth-tier labels → DONE / retired.** Shipped as the per-card 101/202 badges (11 + 1, verified). No separate task remains. The only follow-on is the `All/101/202` toggle (still pending below).
- **Canonical path → folded into the toggle.** Now that there are two tiers, a single linear path must account for both — so it merges into the tier-toggle work rather than being its own task. Lower priority than the D2 content gap.
- **Domain-2 lesson → ✅ DONE (2026-06-06).** Built as the 101 exam-depth extension **C-E6** (see "✅ Done — D2 101" section above). Because it rides the proven 8/8 101-extension pipeline and is independent of the 202 template, Ram chose to build it ahead of the pilot-eyeball gate — low risk, highest exam ROI. The D2 **202 companion** is still optional/pending. Citations researched fresh; both gates PASS; wired into Launchpad; rendered-verified.

---

## THE PROVEN RECIPE (exactly how the pilot was built — repeat per lesson)
This pipeline produced the pilot. Follow it verbatim for each remaining 202 lesson.

1. **Grounding (reuse, don't re-research — except D2).** Each 202 lesson is built on the SAME verified `extensions/source/<slug>_citations.md` as its 101 sibling. These were all re-verified against live docs on 2026-06-06 (53/54 facts confirmed; MCP spec date fixed to `2025-11-25`). **Do NOT invent facts.** The C-E2+C-E4 merge draws on BOTH citations files. **Only the new D2 lesson needs a fresh `web-researcher` pass** → write `courses/claude-101/extensions/source/claude-code-configuration_citations.md` first.
2. **Build (one general-purpose agent, persona panel).** Persona panel = **Senior Tech Writer (lead) + Senior Frontend Engineer + Senior Visual Designer + AI Professor**, all confirmed in `C:\Claude Cowork\Projects\AI agents personas\` (index `AI-Agents-Personas_Overview_v1.html`). Give the agent: (a) the citations file as the ONLY fact source, (b) the 101 sibling for design language, (c) the 202 template spec below, (d) the exact `.cnav` block (below). Output to `courses/<base>/deep-mastery/<slug>-202.html`.
3. **Two QA gates in parallel** (independent agents, never the producer):
   - **Gate 1 — fidelity:** every number matches citations exactly; **any interactive widget's computed numbers must be grounded** in citation multipliers, with author-modeling clearly labeled "illustrative, not an Anthropic fact"; all `[VERIFY]` flags preserved. → `qa/gate1-<slug>-202.md`
   - **Gate 2 — build/interactivity:** self-contained (no CDN/external); trace EACH widget's JS for missing refs / unbound listeners / div-by-zero / NaN at slider extremes / uncleared intervals / state bugs; code-block escaping; `.cnav` exact + resolves on disk; **no duplicate IDs** (critical with many widgets); keyboard-operable + `aria-live`. → `qa/gate2-<slug>-202.md`
   - PASS bar = 0 blockers, 0 majors. Fix high-value minors, log the rest.
4. **Wire into Launchpad (same session).** Add a card object to the right track's `extensions` array with `tier:'202'`, `level:'202 · Deep Mastery'`, the `href`, and a blurb naming the signature widget. (The tier badge renders automatically from the `tier` field.)
5. **Verify rendered** (preview server `cca-prep-static`, port 8099, docroot = project): navigate to the new lesson + Launchpad via `preview_eval`; confirm 0 JS errors, 0 duplicate IDs, widgets present, `.cnav`/launch hrefs resolve. NOTE: the headless preview window reports `innerWidth:0`, so use **DOM/computed-style checks, not screenshots** (screenshots time out). A python link-resolution sweep is the fastest broken-link check.
6. **Update this file + `resume-prompt.md`** with the new shipped lesson.

---

## THE 202 TEMPLATE SPEC ("world-class" bar)
What separates 202 from the already-good 101 extensions: **interactivity that does the teaching, not just illustrates it.**
- **Depth:** mechanism-level (the *why it works / when it pays / how it fails*), never recognition-level. Every key concept gets a place where the learner **manipulates a variable and predicts the result before the reveal.**
- **Visualizations (≥6 inline SVG/Canvas, vanilla JS only):** animated/steppable process diagrams · live simulators · comparison sliders · architecture/protocol "theatres."
- **Interaction types:** predict-before-reveal widgets · scenario-diagnosis ("find the failure") · build-it sandboxes (assemble a config, get critique) · steppable walkthroughs.
- **Checkpoints (varied — NOT rote MCQ):** predict-the-curve · spot-the-flaw · "which pattern/failure is this?" · "fix the broken delegation." Source-grounded feedback with `aria-live`.
- **Real-world examples:** ≥3 per lesson, anchored to Anthropic's own production writeups + analogues to Ram's agent work.
- **Craft floor:** self-contained HTML (inline CSS/JS/SVG, no CDNs/external assets, opens via `file://`); long-form scrollable (NEVER a slide deck / `/frontend-slides`); matches the design-token palette + `.cnav`; a "Sources" section + provenance note (facts verified 2026-06-06); `[VERIFY]` markers on volatile facts; escape all `<`/`>` in `<pre><code>`.

### The exact `.cnav` block (paste right after `<div class="wrap">`, before `<header class="hero">`)
Home + a "📘 101 · Exam-prep view" cross-link to the 101 sibling + base-course link. Paths assume `courses/<base>/deep-mastery/<file>` (3 levels to root):
```html
<nav class="cnav" aria-label="Course navigation">
  <a class="cnav-home" href="../../../Launchpad.html">⌂ Launchpad</a>
  <span class="cnav-side"><a class="cnav-prev" href="../extensions/<101-SLUG>.html">📘 101 · Exam-prep view</a><a class="cnav-next" href="../<BASE-COURSE>.html">← Base course</a></span>
</nav>
<style>
.cnav{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin:10px 0 18px;padding:10px 14px;border:1px solid var(--line,#e7e0d8);border-radius:12px;background:rgba(0,0,0,.02);font:600 13.5px/1.2 system-ui,-apple-system,'Segoe UI',sans-serif}
.cnav a{text-decoration:none;color:var(--ink,#2b2622);padding:7px 13px;border-radius:8px;background:rgba(0,0,0,.05);white-space:nowrap;transition:background .15s,color .15s}
.cnav a:hover{background:var(--accent,#c96442);color:#fff}
.cnav .cnav-home{background:var(--accent,#c96442);color:#fff}
.cnav .cnav-home:hover{filter:brightness(.92)}
.cnav .cnav-side{display:flex;gap:8px;flex-wrap:wrap}
</style>
```

---

## REMAINING 202 LESSONS (Phase A recommendations, build order)
Suggested order = highest standalone value + reuses verified citations first; the research-needed D2 lesson last.

| Order | Subject | Domain | Output slug (`<base>/deep-mastery/…`) | Signature interactive hook | Fact source |
|---|---|---|---|---|---|
| ✅ 0 | Orchestrator-Worker at Scale | D1+D5 | `introduction-to-subagents/deep-mastery/orchestrator-worker-at-scale-202.html` | Cost-vs-reliability simulator | **SHIPPED** — `orchestrator-worker-at-scale_citations.md` |
| 1 | The Five Orchestration Patterns | D1 | `introduction-to-subagents/deep-mastery/orchestration-patterns-202.html` | Pattern-picker (task → which of 5) + animated message-flows per pattern | `orchestration-patterns_citations.md` |
| 2 | The Tool-Use Agent Loop | D4+D1 | `claude-101/deep-mastery/tool-use-agent-loop-202.html` | Steppable animated loop the learner drives; live `stop_reason` transitions | `tool-use-agent-loop_citations.md` |
| 3 | MCP at a Builder Level | D4 | `claude-101/deep-mastery/mcp-at-a-builder-level-202.html` | Clickable host↔client↔server protocol theatre + JSON-RPC handshake + build-a-tool-description workshop | `mcp-at-a-builder-level_citations.md` (spec `2025-11-25`) |
| 4 | Subagents as a Programmable Primitive (SDK) | D1+D2 | `introduction-to-subagents/deep-mastery/subagents-as-sdk-primitive-202.html` | "Compose a subagent" config sandbox → behavior preview | `subagents-as-sdk-primitive_citations.md` |
| 5 | Prompt Engineering + Model Selection | D3 | `claude-101/deep-mastery/prompt-engineering-depth-202.html` | Prompt-ladder playground (toggle techniques → output shape changes) + model-selection decision tool (capability/latency/cost dials) | `prompt-engineering-depth_citations.md` |
| 6 (MERGE) | Context & Economics (C-E2 + C-E4) | D5 | `claude-101/deep-mastery/context-and-economics-202.html` | Live context-window/compaction visualizer + drag-the-reuse-count break-even widget | BOTH `context-management-reliability_citations.md` + `prompt-caching-economics_citations.md` |
| 7 (NEW) | Claude Code Configuration | **D2** | `claude-101/deep-mastery/claude-code-configuration-202.html` | Live config sandbox: `CLAUDE.md` hierarchy resolver, hook-vs-memory demo, permission allow/deny resolver | **NEEDS RESEARCH** → write `claude-code-configuration_citations.md` first (code.claude.com Claude Code docs) |

**Why these and not a literal 8:** caching (C-E4) is too narrow to stand alone → **merged** into #6. The new **D2 lesson (#7)** fills the real gap the course audit found (Domain 2 = 20% of the exam, currently no exam-depth lesson at either tier) — so building it ALSO closes a 101 gap; consider shipping a 101 version of it too.

---

## LAUNCHPAD TIER SYSTEM — state & TODO
- **Done:** `cardHTML()` reads `var tier = card.tier || '101'` and renders a tier-badge pill (plum `--plum` for 202, muted for 101). 202 card added to `DATA`.
- **TODO (do when committing to the full set):** an `All / 101 / 202` toggle above the track list. Cheapest implementation: add `data-tier` to each `<article>` in `cardHTML`, then a 3-button filter that shows/hides articles by tier. Optionally a second "Deep Mastery" track grouping. Re-run the rendered Launchpad check after.
- **Design note (from the prior redesign):** Launchpad is "over-encoded, not over-informed" — keep exam-weight %s, ≥5 domain colors, illustrations; clay `--accent` = action/brand only; D1 = `--wine`; 202 tier = `--plum`. Don't strip signal.

---

## CONVENTIONS & GUARDRAILS (non-negotiable)
- **Provenance:** anchor every claim to Anthropic primary docs or an existing verified citation; label primary vs secondary; `[VERIFY]` on volatile facts (prices, model lineup, multipliers, version gates); flag `[UNVERIFIED]` where lineage can't be established (e.g., the MAST % split). Never present a drifted/unsourced value as current.
- **Self-contained HTML only** — inline CSS/JS/SVG, no CDNs/external images/fonts; opens offline.
- **Long-form scrollable, never a deck.** Do NOT invoke `/frontend-slides`.
- **Keep 101 intact.** 202 is additive; never replace or "deepen in place" the exam-prep lessons — the two-tier distinction IS the product.
- **Project is NOT a git repo** — no commits expected.
- **Preview gotcha:** headless preview window is zero-width → use DOM/computed-style checks, not screenshots.

## DEFINITION OF DONE (per 202 lesson)
☐ Built to the template spec (≥6 SVGs, ≥1 simulator/sandbox, varied checkpoints, ≥3 real-world examples) · ☐ Gate 1 + Gate 2 PASS (0 blk/0 maj) · ☐ `.cnav` correct + all links resolve on disk · ☐ wired into Launchpad `DATA` with `tier:'202'` · ☐ rendered check (0 JS errors, 0 dup IDs) · ☐ this file + `resume-prompt.md` updated.

## OPEN DECISIONS (confirm with Ram)
1. Build all 6 remaining 202 lessons, or a subset? (Order in the table above.)
2. ~~Ship a 101 version of the Domain-2 lesson?~~ **✅ SHIPPED (2026-06-06)** — C-E6, built ahead of the pilot gate (safe: rides the 101 pipeline, not the 202 template). Open: do we also want a **D2 202 companion**?
3. Build the full **All/101/202 toggle** now or after a few more lessons exist? (Canonical-path UX folds into this — see Decision Log.)
4. Any **template changes** from eyeballing the pilot (the "DO THIS FIRST" step)? — still open; this gates the remaining 202 builds (no longer gates D2, which is done).

**Resolved & retired:** depth-tier labels (shipped as card badges); D2 101 exam-depth extension (shipped as C-E6).
