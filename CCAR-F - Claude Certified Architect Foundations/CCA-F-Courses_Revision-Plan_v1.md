# CCA-F Courses — Tone & Engagement Revision Plan v1

**Date:** 2026-07-03
**Author role:** Curriculum Product Manager (persona, routed via `AI agents personas/ROUTER.md`, clear-fit)
**Inputs:** Senior Curriculum IA Reviewer lens (structure) + Senior Learning Content Reviewer lens (pedagogy) + Ram's own evidence-based anti-AI-writing rubric (`About Me/anti-ai-writing-style_v1.md`, `my-voice.md`) applied as the tone standard, run across all 12 HTML files in `courses/`.
**Scope:** `claude-101` (7 files) + `introduction-to-subagents` (5 files, including the 202 deep-mastery lesson). `mcq-practice/index.html` and `EXAM-DIGEST.html` are out of scope — not under `courses/` — see Open Question at the end.
**What this is not:** This is a scoping decision, not the rewrite itself. No HTML files were edited to produce this plan. "Illustrative rewrite direction" below shows the target voice, not final copy — the actual line edit is a follow-up pass.

---

## Read this first: one fix, twelve files

The twelve files don't have twelve different problems. They have one problem, at a consistent severity, everywhere:

| File | Prose words | Em-dashes | Rate /500w | vs. 2.0 ceiling |
|---|---|---|---|---|
| claude-101.html | ~7,000 | ~95 | 6.8 | 3.4x |
| introduction-to-subagents.html | ~4,490 | 93 | 7.3–7.7 | 3.7x |
| tool-use-agent-loop.html | ~4,060 | 48–78 | 5.8–5.9 | 2.9x |
| context-management-reliability.html | ~6,100 | 96 | 7.9 | 4.0x |
| mcp-at-a-builder-level.html | ~8,300 | 132 | 8.0 | 4.0x |
| prompt-caching-economics.html | ~8,430 | 139 | 8.3 | 4.1x |
| prompt-engineering-depth.html | ~9,265 | 145 | 7.8 | 3.9x |
| claude-code-configuration.html | ~9,360 | 138 | 7.4 | 3.7x |
| orchestration-patterns.html | ~5,880 | 101 | 8.6 | 4.3x |
| subagents-as-sdk-primitive.html | ~4,200–6,400 | 110–125 | 6.9–8.6 | 3.9x |
| orchestrator-worker-at-scale.html | ~6,880 | 113 | 8.2 | 4.1x |
| orchestrator-worker-at-scale-202.html | ~5,340 | 106 | 9.9 | 5.0x |

Twelve files, twelve independent audits, zero outliers below 3x. This is not a style quirk in one lesson — it's a systemic pattern in how the content was drafted, and it's the single highest-leverage fix available: bringing every file down to Ram's own stated ceiling (~2 em-dashes per 500 words) would, on its own, resolve the "sounds like AI" complaint more than any other single edit.

Three findings underneath the headline number, present in most files:

1. **Citation-collage voice.** The courses are unusually careful about sourcing — nearly every claim traces to a quoted Anthropic doc line, which is a real strength (it's the opposite of hallucination). But the mechanism that delivers that rigor — stitch quote, stitch quote, add one connective clause, repeat — is the actual source of the "written by AI" feeling, more than vocabulary. `mcp-at-a-builder-level.html`, `subagents-as-sdk-primitive.html`, both `orchestrator-worker-at-scale` files, and `claude-code-configuration.html` show this most.
2. **Banned vocabulary is mostly clean.** Contrary to what you'd expect from an "AI voice" complaint, the corpus barely uses the classic tells (leverage, delve, robust, seamless, unlock). The handful of real hits: "seamlessly" ×3 and "comprehensive" ×4 in claude-101.html, "ecosystem" ×1 in mcp-at-a-builder-level.html, "robust" ×2 in subagents-as-sdk-primitive.html, "best practices" as the author's own phrase (not a quote) once in tool-use-agent-loop.html. This is a five-minute find-and-replace, not the real fix.
3. **Topic-list openers with no hook.** About half the files open sections with "X consists of three things:" instead of a scenario, a stake, or a question. Every file also contains at least one genuinely good, human-written analogy (the chef's cutting board, the newsroom editor vs. the assembly line, the hiring form vs. job description, the intern who reads the whole archive) — proof the target voice already exists in this material. The fix extends that voice outward, it doesn't invent a new one.

**One factual correctness issue, unrelated to tone, found in passing:** `prompt-engineering-depth.html` Section G is headed "the **seven** anti-patterns" but the table below it lists **eight** rows. This is a citation-fidelity issue per this project's own QA-gate standard, not a style call — fix regardless of whether the tone pass proceeds.

---

## The decision

**REVISE** — all 12 files, prose layer only. Not RESTRUCTURE (the IA/nav work is already shipped per `ENHANCEMENT-RECOMMENDATIONS_v1.md` — V-P1 complete), not CUT, not ADD, not KEEP.

**Alternatives considered for the overall call** (per the Decision-family contract — naming what wasn't picked and why):
- **RESTRUCTURE-only** (reorder sections/diagrams, leave sentence-level prose untouched) — rejected: every audit confirms the problem is inside sentences (em-dash density, quote-stitching), not document layout. Reordering wouldn't touch it.
- **KEEP** (leave as-is; content is technically accurate and already passed two QA gates) — rejected: accuracy was never in question. The brief is specifically "does not sound like it was written by AI" and "more engaging" — a KEEP call ignores the actual ask.
- **CUT and rebuild from scratch** — rejected: the good analogies already in the files (see above) prove a full rebuild is unnecessary and would throw away material worth keeping. This is a line-edit job, not a rewrite-from-zero job.

**Confidence: high** on the em-dash finding (it's a hard count, independently reproduced by 12 separate audits with no coordination between them) — **medium** on the qualitative "engagement verdict" per file (that's a reasoned judgment call, not a metric; two of the twelve found real strengths worth preserving, not just problems).

---

## Priority tiers

**P0 — do first (flagship lessons, highest learner traffic):**
`claude-101.html`, `introduction-to-subagents.html` — these are the entry point to each course. Every student reads these; the extensions are opt-in depth.

**P1 — do next (exam-weighted extensions, worst individual scores or a correctness issue):**
`prompt-engineering-depth.html` (has the anti-pattern count error — fix regardless), `claude-code-configuration.html` (longest file, densest field-dump sections), `mcp-at-a-builder-level.html` (worst citation-collage pattern), `context-management-reliability.html`, `prompt-caching-economics.html`, `tool-use-agent-loop.html`.

**P2 — do last (subagents-course extensions, lower traffic; the 202 file is an explicitly-flagged "orphan tier" per the prior enhancement doc):**
`orchestration-patterns.html`, `subagents-as-sdk-primitive.html`, `orchestrator-worker-at-scale.html`, `orchestrator-worker-at-scale-202.html`.

---

## Per-file findings

### 1. claude-101.html — P0
- **Findings:** 6.8 em-dashes/500w (3.4x). Banned vocab: "seamlessly" ×3, "comprehensive" ×4, "deep dive" ×1 (as a lesson title), soft "transform(s)" ×2. Same idea restated 3–4 times across diagram/bullets/prose/example (the "3-part prompt" concept, lines ~353–372). Lessons 8, 11, 12 run 350–700 words with zero check-in — a new pacing gap not covered by the prior enhancement pass.
- **Decision:** REVISE — target: key-takeaway callouts (lines 661, 673, 686, 962, 1108) and the Lesson 4/8/11/12 bullet dumps.
- **Illustrative rewrite direction:** "Projects scale automatically. When your knowledge base approaches context limits, Claude seamlessly enables Retrieval Augmented Generation (RAG) mode..." → "Fill a project past its context limit and Claude switches to RAG mode on its own — same quality, more room." (Cuts "seamlessly enables... while maintaining," states the mechanism plainly.)
- **Alternatives considered:** RESTRUCTURE only the redundant 3-part-prompt passage (rejected — the redundancy is a symptom of the same drafting habit seen everywhere else, not a one-off worth a special-case fix); KEEP (rejected — flagship lesson, sets the tone for the whole course, highest-leverage place to fix first).
- **Confidence:** high.

### 2. introduction-to-subagents.html — P0
- **Findings:** 7.3–7.7 em-dashes/500w (3.7x). Banned vocab: "best practices"/"ensuring" (author's own voice, not a quote) — 4 hits. "Not just X" rhythm ×2 (lines 557, 647) plus a textbook "Whether you're using X or Y..." closer at line 379, in the most-read spot in the file (end of the Lesson-1 takeaways box). Lesson 4 stacks three concept sections before its first check-in.
- **Decision:** REVISE — target: the Lesson 1 takeaways closer (line 379) first, then the four-characteristics numbered list (lines 735–739).
- **Illustrative rewrite direction:** "Whether you're using the built-in subagents or creating your own, they're a practical way to get more out of longer Claude Code sessions." → "Built-in or custom, subagents buy you the same thing: a cleaner main thread and a longer session before context runs out." (Drops the banned rhythm, keeps the claim.)
- **Alternatives considered:** RESTRUCTURE (move the Lesson-4 check-in earlier without touching prose — rejected, doesn't fix the closer line every student reads); KEEP (rejected — same flagship-lesson logic as claude-101.html).
- **Confidence:** high.

### 3. mcp-at-a-builder-level.html — P1
- **Findings:** 8.0 em-dashes/500w (4.0x) — 132 occurrences, including in headings ("Why MCP Exists — the M×N Problem"). Banned vocab: "ecosystem" ×1 (author's own summary line, line 350). Worst citation-collage pattern of the twelve files: multiple passages are 3–4 stitched quotes with a `(source: ...)` tag breaking the paragraph mid-flow. Otherwise strong: formative-check coverage is actually a model for the other files (every section has an MCQ).
- **Decision:** REVISE — target: the quote-stacked passages in Section 2 (line 388) and Section 8.1 (lines 1020–1032); move inline `(source: ...)` citations to a consistent end-of-paragraph position.
- **Illustrative rewrite direction:** "The MCP host 'accomplishes this by creating one MCP client for each MCP server...' (source: architecture) A host with three servers has three clients." → "One client per server, always — a host running three servers keeps three separate connections, never a shared one. (Anthropic's architecture docs call this out explicitly; it's the single most testable fact in this lesson.)" (States the rule first, cites second, keeps the "testable fact" framing that was already good.)
- **Alternatives considered:** RESTRUCTURE (reorganize citation placement only, leave quote-density untouched — rejected, the density itself is the problem, not just where the tags sit); KEEP (rejected — worst-scoring file on the primary tone metric among the extensions).
- **Confidence:** high.

### 4. claude-code-configuration.html — P1
- **Findings:** 7.4 em-dashes/500w (3.7x) across the longest file in the corpus (~9,360 words). Banned vocab: clean (the few hits are inside verbatim doc quotes or a citation title). Section C stacks four dense blocks (precedence ladder, two diagrams, two field-dump bullet lists) before the first MCQ; Section H dumps 15 CLI flags in one sentence. Real strength: the exam-trap callouts and predict-first reveals show genuine voice where the file isn't just enumerating fields.
- **Decision:** REVISE — target: the Section C field-dump bullets (lines 549–566) and the Section H flag list (line 1250).
- **Illustrative rewrite direction:** "`cleanupPeriodDays` (default 30), `includeCoAuthoredBy` (Deprecated — 'Use `attribution` instead'), `attribution`..." → "Three fields worth knowing: `cleanupPeriodDays` controls retention (30 days by default), and `attribution` replaced the now-deprecated `includeCoAuthoredBy`." (One sentence carrying the same facts, instead of a bare field list.)
- **Alternatives considered:** RESTRUCTURE (split Section C's two field lists apart with an example in between, leave the enumeration style — rejected, the enumeration style itself is the tone problem, not just its length); KEEP (rejected — second-longest file, second-most exposure to a listless reference-manual voice).
- **Confidence:** high.

### 5. context-management-reliability.html — P1
- **Findings:** 7.9 em-dashes/500w (4.0x). Banned vocab: clean (only a legitimate proper-noun citation of an Anthropic doc title contains "harness"). Two "not just X" fragments. Section 8 stacks four sub-topics before its one MCQ. Real strength: the "scalpel vs. blunt instrument" and "chef's cutting board" analogies are genuinely good — they're islands surrounded by quote-stitched paragraphs.
- **Decision:** REVISE — target: Section 5's back-to-back blockquotes (the "art of compaction" passage) and Section 9's four label-colon-quote checkpointing bullets.
- **Illustrative rewrite direction:** "Session init: 'Read the git logs...' State verification: 'run a basic test...' Clean handoffs: 'leave the environment...'" → "Good handoffs do four things in sequence: read the git log to get oriented, run a basic test to confirm the state you inherited, leave things clean when you're done, and touch one feature at a time." (One flowing sentence instead of four label-quote pairs.)
- **Alternatives considered:** RESTRUCTURE (add a mid-section check-in to Section 8 without touching the quote-stitching — rejected, treats the pacing symptom, not the voice problem the brief actually asked about); KEEP (rejected — same reasoning as the other P1 files).
- **Confidence:** high.

### 6. prompt-caching-economics.html — P1
- **Findings:** 8.3 em-dashes/500w (4.1x) — the highest raw count in the file set (139). Banned vocab: clean, zero hits on the full list. The "Turn 1... Turn 2... Turn 10..." triplet and the "Pays off when... / Loses on:..." symmetrical construction read as engineered-for-emphasis rather than spoken. Section D (Economics) runs ~20 minutes of content with only two predict-reveals and no MCQ until the very end — the highest-yield exam fact in the lesson (the break-even derivation) currently gets no scored check.
- **Decision:** REVISE — target: the Section D "Pays off when / Loses on" passage and the Turn-1/2/10 triplet.
- **Illustrative rewrite direction:** "Pays off when a large, byte-identical prefix is reused many times within the TTL... Loses on: sub-minimum prefixes, single-shot prompts, changing prefixes..." → "This only pays off if the same large block of text gets reused, byte-for-byte, before the cache expires — a long conversation or an agent loop. It doesn't help a one-shot prompt or a prefix that changes on every call." (Same facts, no engineered binary structure.)
- **Alternatives considered:** RESTRUCTURE (add the missing mid-section MCQ after the break-even derivation, leave prose untouched — rejected as the *only* fix; worth doing in addition, but doesn't address the tone finding the plan is scoped to); KEEP (rejected — same file-length/exposure logic).
- **Confidence:** high.

### 7. tool-use-agent-loop.html — P1
- **Findings:** Lowest em-dash rate of the twelve (5.8–5.9/500w) but still 2.9x over ceiling. Banned vocab: one real hit, "best practices" as the author's own transition phrase (line 681, not a quote). Heaviest reliance on quote-collage of any file audited: whole paragraphs are built from 3–4 stitched fragments with connective tissue like "Per the source" or "The source's verdict." One quiz-coverage gap: the "consolidate operations / namespacing / high-signal responses" trio (line 681) is presented but never checked anywhere in the lesson.
- **Decision:** REVISE — target: the Section 5 "quote-collage paragraph" (line 759) and the Section 4 "best practices" line.
- **Illustrative rewrite direction:** "Agents begin with 'a command from, or interactive discussion with, the human user.' Once the task is clear, they 'plan and operate independently,' gaining 'ground truth from the environment at each step...'" → "An agent starts from a task the user gives it, then works independently from there — checking its progress against what actually happens in the environment, not just what it expects to happen." (States the idea once, in one voice, instead of assembling it from four quoted fragments.)
- **Alternatives considered:** RESTRUCTURE (add the missing quiz item for the consolidate/namespace trio without touching prose — rejected as a partial fix; do both, but the tone fix is the scoped ask); KEEP (rejected — lowest score doesn't mean acceptable, it means least-worst).
- **Confidence:** medium — the em-dash finding is high-confidence; the "heaviest quote-collage" ranking is a comparative judgment across 12 files, not a hard metric.

### 8. prompt-engineering-depth.html — P1
- **Findings:** 7.8 em-dashes/500w (3.9x). Banned vocab: clean (the "highest-leverage" and "deep-dive" repeats are borderline but load-bearing terms, not filler). **Correctness issue, independent of tone:** Section G heading says "the seven anti-patterns," the table below lists eight rows. Section E (Structured Output) runs ~850 words before its first check-in, the largest gap in the file.
- **Decision:** REVISE (tone) — target: the Tier-1 four-levers numbered list (lines 750–756) and the Structured Outputs limits callout (line 791). **Fix the "seven vs. eight" heading mismatch regardless of whether the tone pass proceeds** — this is a factual-accuracy defect a certification-exam reader will notice and lose trust over.
- **Illustrative rewrite direction:** "Four levers (verbatim): 1. 'Tell Claude what to do instead of what not to do'... 2. 'Use XML format indicators'..." → "Four things move formatting reliability the most: say what to do rather than what to avoid, mark sections with XML tags, match your prompt's register to the output you want, and spell out formatting preferences explicitly when they matter." (One sentence, same four facts, no bare-quote numbered list.)
- **Alternatives considered:** DEFER the tone fix until after the correctness fix ships (rejected as the ordering — both are cheap enough to do in the same pass; no reason to sequence them); KEEP (rejected — the correctness error alone requires touching this file regardless of the tone question).
- **Confidence:** high on the correctness issue (it's a countable row mismatch); high on the em-dash finding; medium on which passages are "worst" (qualitative).

### 9. orchestration-patterns.html — P2
- **Findings:** 8.6 em-dashes/500w (4.3x) — second-highest rate in the corpus. Banned vocab: clean (all 4 hits are inside direct Anthropic quotes or a verbatim code sample). Lesson 10 stacks five content blocks (architecture bullets, two tables, an economic-gate paragraph) before its first check-in — the densest pre-checkpoint run found in any file.
- **Decision:** REVISE — target: the Lesson 10 quote-mosaic paragraph (line 900) and the four-bullet "reference architecture" list (lines 837–842).
- **Illustrative rewrite direction:** "A lead agent analyzes the query... Subagents operate in parallel... Subagents perform web searches... A dedicated CitationAgent then..." → "Here's the sequence: the lead agent breaks down the query, hands pieces to subagents that search in parallel, and a dedicated CitationAgent adds sourcing before anything ships." (Turns a four-bullet spec sheet into the one-sentence story it actually is.)
- **Alternatives considered:** RESTRUCTURE (split Lesson 10 into two shorter subsections with an earlier check-in, leave prose as-is — rejected as the only fix; the pacing gap and the voice gap are both real but the tone fix is the scoped ask here); KEEP (rejected — second-worst em-dash score in the set).
- **Confidence:** high.

### 10. subagents-as-sdk-primitive.html — P2
- **Findings:** 6.9–8.6 em-dashes/500w depending on scope measured (3.5–4.3x). Banned vocab: "robust" ×2 (same phrase reused twice, lines 656/1145), "unlocks" ×1 (borderline). Two clear triple-bullet-as-chopped-prose cases. Lesson 2 stacks two full code listings plus a 14-row table before its first check-in — the densest pre-checkpoint run found in this course. Real strength: the "hiring form vs. job description" and "emailing a contractor who wasn't in the meeting" analogies are genuinely good.
- **Decision:** REVISE — target: the "three ways to create a subagent" bullet list (lines 297–302) and the quote-over-quoting passage at line 747.
- **Illustrative rewrite direction:** "Subagents can be created three ways: Programmatically — ... Filesystem-based — ... built-in general-purpose — ..." → "You can define a subagent three ways: in code, as a file on disk, or just use the built-in general-purpose one Claude ships with." (Drops the bold-label-dash template repeated three times in a row.)
- **Alternatives considered:** RESTRUCTURE (add a checkpoint after Lesson 2's code blocks, leave the bullet templates untouched — rejected as partial); KEEP (rejected — same reasoning as the other P2 files, but noting this file's two hand-written analogies are worth explicitly preserving verbatim during the edit, not just cutting dashes around them).
- **Confidence:** high.

### 11. orchestrator-worker-at-scale.html — P2
- **Findings:** 8.2 em-dashes/500w (4.1x). Banned vocab: clean — the cleanest file in the corpus on this axis. Section 3 is the single longest uninterrupted teaching run found across all 12 files (two diagrams, four "Job N" subsections, a six-row table, and a ~1,600-word code block before any check-in) — and the six-principle table is never quizzed anywhere in the lesson, including the final 10-question quiz. Real strength: "the architect's instinct is suspicion of the fan-out, not enthusiasm for it" is some of the best writing in the whole corpus.
- **Decision:** REVISE — target: the "Why bother, given the cost? Three reasons" topic-list opener and the CitationAgent passage (repeats the same point three ways).
- **Illustrative rewrite direction:** "A dedicated 'CitationAgent' 'processes the documents...' ensuring claims are attributed before delivery. This is a distinct worker role: verification is architecturally separated from research. The agents that find information are not the agent that checks it — a separation-of-concerns move..." → "A separate CitationAgent checks claims before anything ships — the agents that find information aren't the ones that verify it, which is the whole point." (States the separation-of-concerns idea once instead of three times.)
- **Alternatives considered:** RESTRUCTURE (add a check-in for the six-principle table, leave prose voice as-is — rejected as partial, do both but tone is the scoped fix); KEEP (rejected — clean vocabulary doesn't offset the highest-density em-dash pattern in the file).
- **Confidence:** high.

### 12. orchestrator-worker-at-scale-202.html — P2
- **Findings:** 9.9 em-dashes/500w (5.0x) — the highest rate of any file audited. Banned vocab: clean (the one "alignment" hit is inside a direct academic-paper quote). Three literal "not just X, but Y" rhythm hits, more than any other file. Real strength: the newsroom-editor analogy and "you will manipulate the economics, not just read them" show a genuinely engaged voice — this is the 202/advanced tier, and the extra rigor shows in good ways too, not just density.
- **Decision:** REVISE — target: the three "not just X" hits (lines 280, 300, 642) and the citation-stitched passage at line 410.
- **Illustrative rewrite direction:** "You will manipulate the economics, not just read them." → keep this one, it's a strong line and not the banned rhythm's weakest form — but fix the two others: "not just name 8 modes, but explain how each compounds..." → "Name all 8 failure modes, explain how each compounds, and match each one to the mitigation that attacks its root cause." (Drops the "not just X, but Y" scaffold, keeps the same requirement.)
- **Alternatives considered:** DEFER the whole file until the 202-tier "orphan pilot" sequencing question (C-P2-2 in `ENHANCEMENT-RECOMMENDATIONS_v1.md`) is resolved (rejected — that's a decision about whether to build a sibling 202 lesson, unrelated to whether this existing one reads well; no reason to block a tone fix on an unrelated sequencing call); KEEP (rejected — worst em-dash rate in the entire set, at 5x ceiling).
- **Confidence:** high.

---

## Open question (named, not resolved)

`mcq-practice/index.html` and `EXAM-DIGEST.html` were not audited — the request scoped to "the HTML files in this course," which is the `courses/` folder. If Ram wants the same tone pass applied to the cram/practice materials, that's a second, smaller round using the same method. Naming it rather than silently expanding scope, per this plan's own discipline about not forcing a call the evidence doesn't cover yet.
