# Resume Prompt — CCDV-F Regeneration: Chapters 6–10 Verification
_Generated: 2026-08-23 • Working dir: `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude Certified Developer Foundations`_

> **✅ RESOLVED 2026-08-23, same day.** Ch07 and Ch10 both re-verified and confirmed PASS — Ch10 after
> one further round (a disguised negation-tricolon recurrence), Ch07 after five further rounds (two real
> fixes, two isolated C13 gaps, and a final C14 finding closed as a Ram-approved documented exception
> rather than a sixth round). Kept as the historical record of this file's own "what's open" list; the
> canonical round-by-round account is now `CCDV-F_Regeneration-Plan_v1.md`'s **Part II** section, and the
> exception itself is documented in `CCDV-F_Prose-Gate_v1.md` §3.3 directly under C14. Chapters 6–10 are
> not yet converted to HTML or committed — that decision is still open, same as this file originally
> flagged.

## Context

This session converted the already-gated Part I (chapters 1–5) to HTML — Ram reviewed and approved it,
now committed and pushed — then authored chapters 6–10 as new markdown and ran them through the
project's blind prose-gate process (author → fresh blind-review agent → fix → fresh blind-review
agent, repeat). The session was cut short by Ram hitting his Claude usage window mid-verification, not
by any blocker in the work itself. Two background review agents were killed mid-run as a direct
consequence.

## What's done

- Chapters 1–5 built to HTML (`Outputs/regeneration/html/Ch01..05_*.html`), one page per chapter, real
  prev/next cross-links, Ram's own `Ram Preferred HTML Style.md` guide as the design system. Approved
  by Ram. Committed as `718da8f` and pushed to `origin/master`.
- Chapters 6–10 authored as markdown (`Outputs/regeneration/chapters/Ch06..10_*.md`), each following
  its own Chapter-Briefs entry (form/anchor/opening ledger, owned sub-topics, source).
- Chapters 6, 8, 9 are **gate-confirmed PASS** — zero FAILs across all 14 checks on their final blind
  round. Treat these three as done; do not re-open them without a specific reason.
- Chapter 7 and Chapter 10 each went through multiple gate rounds, had real defects found and fixed
  each round (see "Gate history" below), and had one further fix applied after their **last completed**
  round — but the next verification round for both was killed before returning a verdict.

## What's open

- **Chapters 7 and 10 are unverified in their current state.** The fixes described below are applied to
  the files on disk, but no blind reviewer has seen these exact versions yet.
- Chapters 11–34 (29 chapters) not started.
- None of chapters 6–10 are converted to HTML yet, and none are committed to git (5 untracked files).
- Whether to do 11–15 next, or pause for Ram to read 6–10 first (mirroring how Part I was gated before
  continuing), has not been decided — ask if it isn't obvious from his next message.

## Next action (do this first)

Dispatch two fresh blind-review agents (background is fine, run both together), one per chapter, using
the exact same prompt template as every other gate round this session (see any of this session's prior
agent dispatches for the wording — read the gate document in full, extract calibration prose from
`Outputs/classes/html/CCDV-F_Class-01.html`, confirm the calibration FAILs with C1/C2/C3/C4/C6/C7
flagged, then gate the real chapter, report calibration + verdict + raw counts + every check + blind
disclosure). Point them at:

- `Outputs/regeneration/chapters/Ch07_When-asking-nicely-stops-working.md`
- `Outputs/regeneration/chapters/Ch10_The-loop-your-code-owns.md`

For Ch07, tell the reviewer explicitly: this chapter failed C14 (analogy fidelity) on three straight
prior rounds, each time because some sentence implied one output-guarantee "rung" was stronger/weaker
than another. The chapter's stated position has just been rewritten to: free text carries *no*
guarantee at all (categorically different, genuinely the weakest starting point); structured outputs
and strict tool use each carry a *real* guarantee, differing only in *scope* (whole-response vs. one
field), with neither outranking the other. Ask the reviewer to verify that position holds consistently
everywhere in the chapter with no contradiction.

For Ch10, tell the reviewer explicitly: this chapter failed C3 (negation tricolon) on two straight
prior rounds, and each round found the *same rhetorical shape* recurring in *different* sentences after
the previously-flagged ones were fixed — the underlying habit, not any one sentence, was the actual
defect. Ask the reviewer to scan the whole chapter for this shape in any phrasing (not only "It isn't X.
It's Y." but also "X never does A. It does B" and similar two-part negate/assert constructions), and to
give C5/C7/C13 full attention too, since a prior round found real (now-fixed) issues on exactly those
three.

If either comes back FIX or FAIL: fix it directly (don't delegate authoring), re-verify with another
fresh blind agent, and treat "two rounds is a floor not a ceiling" as this project's own established
practice — keep iterating only while each round finds something genuinely *new*; escalate to Ram if a
round repeats an already-fixed defect or finds nothing.

Once 6–10 are all confirmed PASS: report that to Ram and ask whether to proceed to HTML for 6–10, or
straight to authoring 11–15, before doing either — don't assume.

## Decisions locked in

- **Gap-chapter list is authoritative from `CCDV-F_Pedagogy-Design_v2.md` §5, not from the historical
  narrative in `CCDV-F_Regeneration-Plan_v1.md` §2.1.** The two lists differ (the Plan's is the
  *pre-correction* adversary finding). Confirmed correct list: **3, 6, 7, 11, 13, 16, 21, 22, 23, 24,
  29, 30, 31, 32, 33, 34** are gap chapters (every claim must cite an Anthropic-controlled URL — verify
  per-chapter against `Chapter-Briefs_v1.md`'s own `Source:` line, which is the real tie-breaker, not
  either list). Chapters 10 and 28 are corpus-only despite appearing in the Plan's older list.
- **Source-pack-to-chapter mapping, confirmed from actual filenames in `source-packs/`:** Pack-A =
  ch3+ch7 · Pack-B = ch11+13+16 · Pack-C = ch21-24 · Pack-D = ch29-31 · Pack-E = ch6+32-34. Chapters
  10, 8, 9 sourced from `sources/course-transcripts/` (M2 mainly; M4 for ch9's cost/caching material).
- **Citation style for gap chapters:** verbatim Anthropic quotes woven into prose with attribution
  ("Anthropic's own guidance states...", "Anthropic states X, verbatim: '...'") — no footnotes, no
  references appendix. Matches how chapter 3 (already built) does it.
- **The recurring authorial defect this session** (heavy "X, not Y" / negation-tricolon overuse,
  recurring even after sentence-level fixes) is saved as a standing memory —
  `feedback_ccdv-f-contrast-pair-tic.md` — and should inform how 11–34 get drafted: suppress the
  construction while writing, don't rely on the gate to catch it after the fact.
- **HTML build system for 1–5 is the template for 6–34** once each part's markdown is gated. Don't
  redesign it; the style guide, box-vocabulary mapping, and per-chapter custom-SVG pattern are settled.

## Files touched this session

- `Outputs/regeneration/html/Ch01_The-one-budget-everything-spends.html` (edited: live cross-links)
- `Outputs/regeneration/html/Ch02..05_*.html` (new)
- `Outputs/regeneration/chapters/Ch06_Diagnosing-a-prompt-by-its-failure.md` (new, gate-PASS)
- `Outputs/regeneration/chapters/Ch07_When-asking-nicely-stops-working.md` (new, fixed post-round-3, unverified)
- `Outputs/regeneration/chapters/Ch08_Keeping-a-long-session-inside-the-budget.md` (new, gate-PASS)
- `Outputs/regeneration/chapters/Ch09_Paying-once-for-what-does-not-change.md` (new, gate-PASS)
- `Outputs/regeneration/chapters/Ch10_The-loop-your-code-owns.md` (new, fixed post-round-2, unverified)
- `ROADMAP.md`, `Outputs/regeneration/CCDV-F_Regeneration-Plan_v1.md` (status lines updated)
- Memory: `project_claude-cert-four-exam-structure.md` (updated), `feedback_ccdv-f-contrast-pair-tic.md` (new), `MEMORY.md` (updated)

## Gotchas / watch-outs

- **Don't re-litigate the gap-chapter list** — it looks contradictory across two project files until you
  know Pedagogy-Design v2 supersedes the Plan's own historical narrative. See "Decisions locked in."
- **A "killed" background-agent task-notification can mean the user deliberately stopped it**, not a
  crash. If you see one, don't just silently relaunch — check with Ram first, exactly as this session
  did, unless he's already told you to keep going.
- **When re-verifying Ch07/Ch10, don't assume the fix worked.** Both chapters have a track record of the
  same defect resurfacing in new phrasing after a seemingly-clean fix. Read the actual current file
  before trusting this document's description of it.
- The receipt-agent/25,600-of-40,000 example belongs to chapter 1 alone. Don't reuse it as a worked
  example in any other chapter (chapter 8 originally did, by accident, until a C14 review caught the
  anchor collision — see the "carry vs. pruning" mapping fix in that chapter if you want the concrete
  lesson).

## Git state

Not committed yet — 5 untracked files (all of chapters 6–10's markdown):

```
?? Outputs/regeneration/chapters/Ch06_Diagnosing-a-prompt-by-its-failure.md
?? Outputs/regeneration/chapters/Ch07_When-asking-nicely-stops-working.md
?? Outputs/regeneration/chapters/Ch08_Keeping-a-long-session-inside-the-budget.md
?? Outputs/regeneration/chapters/Ch09_Paying-once-for-what-does-not-change.md
?? Outputs/regeneration/chapters/Ch10_The-loop-your-code-owns.md
```

Recent commits (`git log --oneline -3`):
```
718da8f Add readable HTML for CCDV-F chapters 1-5
411b7e6 Merge remote-tracking branch 'origin/master'
14ce3ed Sync CCDV-F docs to the regeneration decision
```

Branch is in sync with `origin/master` (no ahead/behind) as of the last push. Do not commit chapters
6–10 until Ch07 and Ch10 are actually re-verified — commit only what's confirmed, matching how this
session handled 1–5 (build → verify → only then commit on explicit request).
