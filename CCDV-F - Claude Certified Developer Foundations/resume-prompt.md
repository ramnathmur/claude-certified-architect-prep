# Resume Prompt — Chapter 15 authoring, chapters 11–14 now have HTML
_Generated: 2026-08-24 • Working dir: `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude Certified Developer Foundations`_

## Context

This session resumed from a prior pause where chapter 14 was stuck at its gate's round cap. Two things
happened, in order:

1. **Chapter 14's round-2 findings were resolved.** Presented verbatim to Ram (a zero-tolerance C14 hit
   inside the self-test itself, plus a C7+C13 bucket FAIL) with the fix-vs-waive tradeoff spelled out
   explicitly, since this was the first waiver candidate to include a zero-tolerance check. **Ram waived
   both anyway** — the waiver pattern from chapters 11 and 13 now extends to zero-tolerance findings, not
   just narrow discretionary ones. Chapter 14 is closed, unfixed, as-authored.
2. **Chapter 15 authoring started, then was explicitly deferred.** Its brief, ledger row, and coverage-
   contract entry were read, and its corpus source was located (see NEXT ACTION below) — but Ram
   interrupted before an author agent was dispatched, to redirect this session at catching up HTML
   generation for chapters 11–14 instead. **No chapter 15 content exists yet.** Its research is preserved
   below so the next session doesn't repeat it.

A third piece of work followed the redirect: **chapters 11–14 were converted to HTML**, the same day,
using the established chapters 1–10 template. That work is done and independently verified (not just
each build agent's own self-report) — see "What's done" below.

## What's done

- Chapters 1–10: HTML pushed (Part I `718da8f`, Part II `e5142c7`); Part II still awaits Ram's own
  final read-through before anything past it gets pushed (pre-existing, unrelated to this session).
- **Chapter 11 (Tool Selection):** PASS w/ 2 Ram-waived exceptions (C5, C7) — from the prior session.
- **Chapter 12 (Streaming):** clean PASS, zero exceptions — from the prior session.
- **Chapter 13 (Capability Shapes):** closed via the waiver pattern after a round-cap overrun — from the
  prior session.
- **Chapter 14 (MCP Architecture): closed this session** — both round-2 findings (C14 self-test
  contradiction + C7/C13 bucket) waived by Ram without a fix. Three new exception notes written into
  `CCDV-F_Prose-Gate_v1.md` (C7, C13, C14) documenting this is the first zero-tolerance waiver, distinct
  from Ch7's reviewed-and-confirmed-sound C14 exception.
- **Chapters 11–14 converted to HTML this session** (2026-08-24), all in
  `Outputs/regeneration/html/`. Method: four parallel agents, one per chapter, each given the exact
  markdown source, `Ch10_The-loop-your-code-owns.html` as the literal template to copy `<style>`/
  `<script>` from verbatim, and a full section-by-section spec (ids, nav labels, box-type assignments,
  one custom SVG diagram concept per chapter) — same method proven on chapters 6–10.
  - **Independently re-verified after the build**, not just trusted from agent self-reports: diffed the
    `<style>` and `<script>` blocks across all five files (Ch10–14) — byte-identical. Confirmed the full
    prev/next chain resolves end to end, Ch10↔11↔12↔13↔14↔(disabled "Chapter 15, coming soon") — this
    required fixing Ch10's own forward link, which had been sitting disabled since chapters 11–14 didn't
    exist yet when its HTML was built. Loaded all four pages in a live browser (served via the
    `cca-cert-hub` localhost config, not `file://`): every section id present in the planned order, no
    duplicate ids anywhere, every self-test MCQ scores correctly for both single- and multi-select items,
    zero console errors on any of the four pages.
  - **One real content gap found and repaired, not silently patched:** chapter 13's self-test has no
    "Answers" section in its markdown — unlike every sibling chapter, it was never written. The four
    answers used in the HTML (Q1=A, Q2=B, Q3=A, Q4=A,B) were derived from the chapter's own stated
    decision rule, each traced to a specific sentence, and flagged to Ram (and recorded in
    `CCDV-F_Regeneration-Plan_v1.md`) rather than silently invented. **The markdown source itself still
    has no Answers section** — worth adding there too so the two files agree; not done yet.
  - **Chapter 14's HTML preserves both Ram-waived defects verbatim**, including the self-test's "launches
    the same server automatically" contradiction — confirmed by reading the rendered DOM directly, not
    just the source file. Its one new diagram (stdio private-copies vs. sockets shared-instance) was
    checked to confirm the word "launches" appears nowhere near the shared-server label: new content
    stays correct even where the untouched, deliberately-unfixed self-test stem does not.
  - **Not committed** — commits happen only on explicit request, held all session.

## What's open

- **Chapter 15 ("Workflow or agent") authoring has not started — deferred to a later session, at Ram's
  request.** This is the actual next action, not chapter 16. Full brief and source pointers below so the
  next session can dispatch its author agent immediately without repeating the research.
- Chapters 16–20 not started at all.
- Chapter 13's markdown source is still missing its self-test Answers section (see above) — a small,
  low-urgency fix, independent of chapter 15.
- Chapters 6–10's HTML still awaits Ram's own final read-through before he'd push it past `e5142c7`
  (pre-existing from before this session, unrelated to anything done here).
- No index/hub page exists yet for `Outputs/regeneration/html/` — each chapter links only to its
  immediate neighbors. Not asked for; don't build one unprompted.

## Next action (do this first) — Chapter 15: "Workflow or agent"

**All the research is already done — go straight to dispatching the author agent next session.**

**Brief** (full detail in `CCDV-F_Chapter-Briefs_v1.md`, Part IV, "Ch 15"): 3,200 words — Agent
Architecture 2,200 + Agent Patterns 1,000. **Idea:** you buy an agent when you cannot enumerate the steps
in advance, and you pay for it in determinism. **Owns** (confirmed against `CCDV-F_Coverage-
Contract_v1.md` §4's build-contract row, 6 sub-topics): `Principles` · `patterns` · `tradeoffs` ·
`Decision criteria for workflow vs agent` · `manager/supervisor hierarchies` · `role of subagents`.
**Form 2 two-column fork · Open B a decision made badly · Anchor:** an assembly line against a repair
shop (confirmed against the ledger, §1 — no adjacency collision). **Boundary:** owns the architectural
*role* of subagents only; chapter 18 owns the mechanism. **Must land** (the brief's own flagged gaps):
`manager/supervisor hierarchies` were thin in the design — orchestrator-worker alone is not the whole
set; `role of subagents` was implied-only and must state what a subagent is architecturally *for*, not
just name the orchestrator-worker pattern.

**Source pointers found this session** (grep them yourself before dispatching, per the standing
process's step 2 — don't re-search from scratch):
- `sources/course-transcripts/CCDV-F_Module-2_Production-Grade-Prompting-Agents-Tool-Use.md`, lines
  950–1099: the core "Workflow or agent: make this decision before you write the first line" screen —
  the workflow-vs-agent table, the three wiring paths (raw loop / Agent SDK / Managed Agents), the loop-
  wiring checklist, the HITL insertion-point table, and the "when agents are the right call" table. This
  is the chapter's primary source.
- **The brief's own "must land" gap is real and confirmed**: M2 only mentions multi-agent hierarchies in
  one line (966) — "a planner, executor, and evaluator run as separate agents handing off through
  structured artifacts" — not enough to teach manager/supervisor hierarchies on its own.
  `sources/course-transcripts/CCDV-F_Module-4_Production-Engineering-Evals-Security.md`, lines 853–989
  and 1328–1396 has the real content: a full orchestrator-worker treatment with concrete numbers (a lead
  agent decomposes and delegates to parallel subagents, each with its own context window; **roughly 15x
  token cost** in Anthropic's reported case), a cost-instrumentation table, a customer-quote misconception
  ("why is my orchestrator-worker setup so expensive?"), and a glossary definition (line 1394). **Point
  the author agent at both M2 and this M4 range** — this is the fix for the brief's own flagged gap, and
  it wasn't obvious from the brief alone; a future author working from M2 only would inherit the same
  thinness the brief warns about.

Once dispatched and gated, follow the exact same 9-step process as chapters 11–14 (full steps in the
prior session's history, summarized): brief → source pointer → dispatch one author agent → dispatch one
genuinely blind reviewer → PASS moves on, FIX/FAIL round 1 gets one fresh fix + one fresh round-2 review,
**round 2 anything but PASS stops — Ram's call, not another agent dispatch, no exceptions** → update
`CCDV-F_Regeneration-Plan_v1.md` Part III + `ROADMAP.md` + memory every time, not batched → HTML
conversion and commits both wait for explicit request.

## Decisions locked in this session

- **The gate waiver pattern now covers zero-tolerance findings, not just narrow discretionary ones.** On
  chapter 14, offered a fix-vs-waive choice with the zero-tolerance distinction spelled out explicitly,
  Ram still chose to waive. See [[feedback-ccdv-f-gate-waiver-pattern]] (updated this session) — treat
  this as "the tier changes what needs to be surfaced, not whether waiving is on the table," not as
  "zero-tolerance findings are now routinely waivable."
- **A missing answer key in a chapter's self-test gets derived and flagged, not left blank or silently
  invented.** Trace every derived answer to the specific source sentence it comes from, record the gap
  in the regeneration plan, and don't let the reconstruction read as if it were always there.
- **HTML conversion never "fixes" a chapter's content along the way**, including a Ram-waived defect —
  convert faithfully, and keep any genuinely new content the conversion adds (like a diagram) held to a
  higher bar than the untouched prose, since new content has no waiver covering it.
- **Chapter 15's authoring is deferred by explicit request, not by a gate stop** — different from every
  other pause this project has hit so far, which were all round-cap escalations. Don't treat this as
  something that needs Ram's decision to resume; it just needs picking back up.

## Files touched this session

- `Outputs/regeneration/CCDV-F_Prose-Gate_v1.md` (three new exception notes: C7, C13, C14 for chapter 14)
- `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` (chapter 14 closure; HTML batch-build note;
  chapter 13 answer-key gap recorded)
- `ROADMAP.md` (chapter 14 closure + HTML batch note + chapter 15 deferral)
- `resume-prompt.md` (this file, fully rewritten)
- `Outputs/regeneration/html/Ch10_The-loop-your-code-owns.html` (forward link un-disabled, now points to
  the real Ch11 file)
- `Outputs/regeneration/html/Ch11_Why-Claude-picked-the-wrong-tool.html` (new)
- `Outputs/regeneration/html/Ch12_Streaming-without-corrupting-state.html` (new)
- `Outputs/regeneration/html/Ch13_Four-ways-to-hand-Claude-a-capability.html` (new)
- `Outputs/regeneration/html/Ch14_Build-once-connect-many.html` (new)
- Memory: `feedback_ccdv-f-gate-waiver-pattern.md` (extended to the zero-tolerance case),
  `project_claude-cert-four-exam-structure.md` and `MEMORY.md` (both updated for the chapter 14 close and
  the HTML batch)

## Gotchas / watch-outs

- **`CCDV-F_Resume-Prompt_v1.md`** (a different, untracked file, predates this session) — its provenance
  is still unknown; still leave it alone, still don't sweep it into anything. Unchanged from the last
  resume prompt's note.
- **Chapter 13's markdown source still has no self-test Answers section.** The HTML has a derived key
  (see above); the markdown doesn't. If chapter 13's markdown gets touched for any other reason, add the
  Answers section then so the two files stop disagreeing.
- **Don't re-run the chapter 15 source search.** It's done — see NEXT ACTION above. The brief's own "must
  land" note undersells how thin M2 actually is on manager/supervisor hierarchies; the real material is
  in M4, a module the brief didn't point at.
- **The `cca-cert-hub` localhost config** (`C:\Claude Cowork\Projects\.claude\launch.json`, port 18792,
  serving the whole `Claude Certified Architect Prep` folder) is what this session used to browser-verify
  HTML — reuse it rather than adding a new config; the Browser pane in this environment can't take
  screenshots, so verify via `read_console_messages`, `javascript_tool` DOM inspection, and `get_page_text`
  instead.

## Git state

Branch: `master`, 1 commit ahead of `origin/master` (`e5142c7`, unpushed — unchanged all session).

Uncommitted, scoped to this folder:
```
 M Outputs/regeneration/CCDV-F_Prose-Gate_v1.md
 M Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md
 M Outputs/regeneration/html/Ch10_The-loop-your-code-owns.html
 M ROADMAP.md
?? Outputs/regeneration/CCDV-F_Calibration-Fixture_v1.md
?? Outputs/regeneration/CCDV-F_Resume-Prompt_v1.md          (pre-existing, unrelated — see Gotchas)
?? Outputs/regeneration/chapters/Ch11_Why-Claude-picked-the-wrong-tool.md
?? Outputs/regeneration/chapters/Ch12_Streaming-without-corrupting-state.md
?? Outputs/regeneration/chapters/Ch13_Four-ways-to-hand-Claude-a-capability.md
?? Outputs/regeneration/chapters/Ch14_Build-once-connect-many.md
?? Outputs/regeneration/html/Ch11_Why-Claude-picked-the-wrong-tool.html
?? Outputs/regeneration/html/Ch12_Streaming-without-corrupting-state.html
?? Outputs/regeneration/html/Ch13_Four-ways-to-hand-Claude-a-capability.html
?? Outputs/regeneration/html/Ch14_Build-once-connect-many.html
?? resume-prompt.md
```

Nothing committed this session — commits happen only on explicit request, held throughout.

Recent commits:
```
e5142c7 Add CCDV-F chapters 6-10: authored, gate-verified, built to HTML
718da8f Add readable HTML for CCDV-F chapters 1-5
411b7e6 Merge remote-tracking branch 'origin/master'
14ce3ed Sync CCDV-F docs to the regeneration decision
a9fbdf8 Add CCDV-F exam prep folder (was never tracked)
```

No version-bump marker files (`package.json`, `pyproject.toml`, `VERSION`, `Cargo.toml`) exist in this
project — not applicable.
