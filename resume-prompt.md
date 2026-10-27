# Resume Prompt — CCAR-P syllabus course (all 38 objectives written)
_Generated: 2026-10-27 • Repo: C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCAR-P - Claude Certified Architect Professional\.claude\worktrees\evaluate-certifications-repo-cdf916 • Branch: claude/evaluate-certifications-repo-cdf916 • Last commit: 5f801c0 (nothing committed or pushed)_

## Context
Ram asked for one self-contained HTML course teaching all 38 objectives of Anthropic's CCAR-P exam guide v1.0 (sit before 2026-12-07). BASE = `<repo>\CCAR-P - Claude Certified Architect Professional\Outputs\_course-build`. The course is finished and delivered: `Outputs\CCAR-P_Syllabus-Course_v1.html` (1.2 MB, 38 of 38 objectives, d1 to d7 openers) was built with plain `node build.js` and sent to Ram on 2026-10-27.

## What's done
- All 38 chapters plus openers d1 to d7, Start and Sources pages updated. Full build: every gate passes. Browser sweep of all 38 chapters clean in both themes; 390 px check clean.
- One cold-review round (auditor then cold reader) done for every domain D1 to D7, in `C:\Claude Cowork\Projects\_cold-review-scratch\course-dN-r1\{A,B}\findings-*.md`. All auditor findings and the real cold-reader findings fixed. D6 and D7 cold-reader findings were only skimmed (the clear ones applied).
- Live-docs facts saved in `BASE\_authoring\facts\` D2.md, D3.md, D7.md.
- `gates.js` patched: voice lint skips `ul.objlist` (guide headings) and CLAUDE.md/SKILL.md/AGENTS.md file names; a repeated section id `cN.N` is allowed (7.8 is taught in both O7.1 and O7.3). `src/foot.html` router now scopes section anchors to the current page.

## What's open
- Ram has not been asked about review round 2 for any domain (global rule: ask after each round). Recommend not running more: the auditors now return mostly NOTE-level items.
- Optional: a second look at the D6 and D7 cold-reader files; the D5 reader was triaged in full.
- Corpus gaps to show Ram, not fix: no zero-shot rule (O2.3 says so); Agent SDK subagent wiring and index types absent; few-shot count and extended thinking differ from live docs; the 20-minute caching row assumes the 5-minute cache (docs offer 1 hour); O7.2/O7.1 `allowed-tools` is pre-approval in the live docs but a restriction in the corpus row (dated notes added); corpus oddities: §1.4 "comprehensive" wording, F-1.1-02/05 and F-1.2-04 have no scenario, F-1.2-04 repeats F-1.12-04.
- Nothing is committed. Ram has not asked for a commit or push.

## Next action (do this first)
Ask Ram (AskUserQuestion) what he wants next: (a) commit the work (`git add` only the paths under `Outputs\_course-build`, `Outputs\CCAR-P_Syllabus-Course_v1.html`, and the other uncommitted course files; then `git remote -v` and `git branch --show-current` before any push), (b) a further review round, or (c) nothing, then read the course. Do not commit or push unless he says so.

## Decisions locked in
- Look "Drawing set", Study edition, top bar plus slide-over index plus Ctrl-K search, no Educational Playbook; build D1 to D7 at the built length.
- Source authority: guide PDF, EXAM-FACTS VERIFIED rows, corpus, lessons for worked examples only. Never edit the corpus. Product facts beyond the corpus are fetched live and dated or left out; where docs differ, teach the corpus row and add a dated note.
- "Known" says only what the guide shows. The guide assigns its three samples to domains, so chapters say "none of them is a sample for this domain" or "is worked through in" an objective, never "gives nothing" or "belongs to".
- Rule rows say "Rules out:" not "Not the cause:".
- Chapters were authored in the main thread, never by agents or forks.

## Files touched this session
- `BASE\fragments\` all o*.html and d*.html, start.html, sources.html; `BASE\gates.js`, `BASE\src\foot.html`, `BASE\PROGRESS.md`, `BASE\_authoring\facts\D3.md` and `D7.md`, packs for O3 to O7.
- `Outputs\CCAR-P_Syllabus-Course_v1.html`, `ROADMAP.md` (course lines), this file; memory note `ccarp-syllabus-course-plan.md`.
- Not mine: `prep with quiz\CCAR-P-Orchestration-Prompt_v2.md` "Corrected 2026-09-02" note.

## Gotchas / watch-outs
- Plain `node build.js` overwrites the deliverable; use `COURSE_OUT=<file>` for private builds.
- Voice gate bans words such as alignment, harness, ensure, load-bearing, actionable, comprehensive, best practice; paragraphs over 75 words warn.
- Preview server: `python -m http.server 18792 --bind 127.0.0.1 --directory "<repo>\CCAR-P ...\Outputs"` (stopped at handoff). Chrome tab 1575918251 may still be open.
- A peer session said origin/master stops at 87fca1d (PR #6); Papers 4 and 5 exist only on this branch's remote. Do not push or merge unprompted.

## Git state
- Branch `claude/evaluate-certifications-repo-cdf916`, HEAD 5f801c0, no commits this session.
- About 25 uncommitted entries (modified CLAUDE.md, README.md, index.html, resume-prompt.md and CCAR-P docs; untracked Outputs\_course-build, Syllabus-Course_v1.html, three Antigravity files, section-drills, drill tools). No version-bump files changed.
