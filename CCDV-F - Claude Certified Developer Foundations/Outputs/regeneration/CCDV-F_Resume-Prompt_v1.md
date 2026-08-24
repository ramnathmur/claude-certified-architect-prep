# CCDV-F Regeneration — Resume Prompt

You're continuing the CCDV-F (Claude Certified Developer – Foundations) study-material regeneration.
**Before doing any work, ask Ram (via AskUserQuestion) how he wants to proceed** — the question is at
the bottom of this file. Don't start generating HTML or authoring chapters until he's answered.

## Where things stand

Project root: `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude Certified Developer Foundations\`

**Plan of record:** `Outputs\regeneration\CCDV-F_Regeneration-Plan_v1.md` — read this first. Single
source of truth for stage status.

- **Chapter list, budgets, ledgers:** `Outputs\regeneration\CCDV-F_Pedagogy-Design_v2.md` — 34
  chapters, 79,500 words. **Stage 4 is complete for all 34 chapters, not just Part I — do not redo it.**
- **Sub-topic ownership:** `Outputs\regeneration\CCDV-F_Coverage-Contract_v1.md` — 153 sub-topics, one
  owner each, mapped to all 34 chapters.
- **Chapter briefs, all 34:** `Outputs\regeneration\CCDV-F_Chapter-Briefs_v1.md` — form/anchor/opening
  ledgers, boundaries, must-lands, per chapter. Also complete for the whole course already.
- **The writing standard:** `Outputs\regeneration\CCDV-F_Prose-Gate_v1.md` — checks C1 through C14 and
  the verdict rule. **This file is fully current** — C14 (analogy fidelity) and a gap in the verdict
  rule were both found and fixed into the file itself this session. Point reviewer agents at this file
  directly; it no longer needs a C14 addendum pasted into the prompt.
- **v1 design (historical, do not use for numbers):** `CCDV-F_Pedagogy-Design_v1.md` — the record of
  the original blind design, kept unedited as evidence. v2 is authoritative on every number.

## Part I — done, gate-verified, delivered to Ram

`Outputs\regeneration\chapters\Ch01..Ch05_*.md` — 15,414 words. Every chapter cleared all 14 checks on
its final round, reviewed blind by an agent that never saw the brief, the author, or prior rounds'
findings. Rounds needed to reach PASS: ch1 = 5, ch2 = 1 (clean first try), ch3 = 2, ch4 = 3, ch5 = 3.
Full per-chapter defect history is in the Regeneration-Plan's own Part I table — don't re-derive it.

**These are markdown only. No HTML exists for them yet.** Ram has read the raw `.md` files but has not
seen them as a formatted reading experience.

## Chapters 6–34 — not started

Briefs already exist for all of them (see above — Stage 4 covered the whole course). Of the 29
remaining chapters:

- **15 are gap-chapters with source packs already researched**, sitting in
  `Outputs\regeneration\source-packs\`: ch6 & ch7 (Pack A) · ch11, ch13, ch16 (Pack B) · ch21–24
  (Pack C) · ch29–31 (Pack D) · ch6, ch32–34 (Pack E). Authoring these means citing the relevant pack,
  the same way chapters 3, 4, and 7's prose did in Part I.
- **14 are corpus-only**, the same shape as chapters 1, 2, and 5: ch8, 9, 10, 12, 14, 15, 17, 18, 19,
  20, 25, 26, 27, 28. Source directly from `sources\course-transcripts\`.

## What actually worked this session — reuse it, don't rediscover it

1. **Write incrementally.** Any agent authoring a chapter or a source pack should `Write` a skeleton or
   its first section immediately, then extend with `Edit` calls — never compose the whole thing in
   memory and write once at the end. Two agent runs this session lost complete, finished work to a
   stall specifically because they didn't do this.
2. **Blind review is not optional.** Every one of the five Part I chapters self-reported clean; two of
   five genuinely weren't. The gate has to run as a separate agent that never sees the brief or the
   author's own self-audit.
3. **A fix for one check can trip another.** Happened three times this session — a C6 fix tripping C1,
   a C14 fix tripping C5, twice. Re-verify every fix with a fresh blind round, including your own edits.
4. **The written "two rounds then escalate" cap is a floor, not a ceiling, when each round is finding a
   genuinely new, real defect** — chapter 1 took 5 rounds and every single one found something the
   last fix hadn't caused or covered. Escalate to Ram only when a round finds nothing new, or repeats a
   defect a previous fix should already have closed.
5. **Git is tracked and pushed now.** The whole CCDV-F folder was untracked in git until this session's
   `/sync-up` caught it — it's committed and on `origin/master` as of 2026-08-22. Commit as you go
   through chapters 6–34; don't let this much work sit uncommitted again.

## The question to ask Ram — do this first, before anything else

Use `AskUserQuestion`. Something close to:

> Two things are queued: turning chapters 1–5 into readable HTML, and authoring chapters 6–34. How do
> you want to sequence them?
> - **HTML for 1–5 first (Recommended)** — you read Part I as the actual finished reading experience,
>   not raw markdown, before more chapters commit to the same voice and shape. This is close to why
>   Part I was gated before continuing in the first place.
> - **Chapters 6–34 first** — keep building; HTML comes later, you read the markdown as-is for now.
> - **Both at once** — the two are independent work streams with no real dependency between them, if
>   speed matters more than reviewing Part I's finished shape before scaling up.

If HTML comes first, also ask: one combined reader (an index hub plus 5 chained pages with prev/next,
mirroring how `Outputs\classes\html\` was built for the old, superseded classes) or five standalone
files? And — per the project's standing Educational HTML rule — ask whether to use the Educational
HTML Design Playbook (`C:\Claude Cowork\my blueprints\educational-html\`, cite whichever version is
actually the highest one present in that folder) before reading it. Don't skip that prompt; it's a
standing instruction, not optional for this kind of content.
