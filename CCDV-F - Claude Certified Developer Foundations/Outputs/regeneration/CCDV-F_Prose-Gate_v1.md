# CCDV-F Prose Gate

Writing standard for the regenerated CCDV-F class material. Built from the four standards files plus a line-level scan of the 14 HTML classes produced in the previous attempt.

Scope: prose quality only. Nothing here touches syllabus, sequencing, or teaching architecture.

---

## 0. Method and corpus

**Standards read in full:** `C:\Claude Cowork\About Me\anti-ai-writing-style_v1.md`, `C:\Claude Cowork\About Me\my-voice.md`, `C:\Claude Cowork\About Me\my-rules.md`, and the "TEACHING / EXPLAINER PROSE — HARD BAN" section of `C:\Users\ramna\.claude\CLAUDE.md`.

**Corpus scanned:** all 14 files in `C:\Claude Cowork\Projects\Claude Certified Architect Prep\CCDV-F - Claude Certified Developer Foundations\Outputs\classes\html\`. Prose was extracted from `h1`–`h4`, `p`, `li`, `blockquote`, `figcaption`, `td`, `th` with CSS and script stripped. Total body prose: **25,714 words**. Classes 01, 02, 03, 05, 06, 09, 10, 12 were read end to end; 04, 07, 08, 11, 13, 14 were read in part and machine-counted in full.

**Headline finding:** the vocabulary is clean. Ram's banned-word list from `my-voice.md` returns 5 hits in 25,714 words (`journey` once, `essentially` once, `nuanced` once, `highest-leverage` three times in Class 14, plus a literal `navigates away` that is a browser term and not the metaphor). The banned "not just X, but Y" family is **absent** in its rhetorical sense. Every defect in this document is structural: sentence architecture, paragraph rhythm, and the relationship the writer strikes with the reader. A word-list gate would have passed this material. That is why the checks below count shapes, not words.

---

## 1. Defect catalogue

Ranked by observed frequency. Every entry is anchored to a verbatim quote with its file and approximate location.

### D1 — The "X, not Y" contrast pair
**56 instances. All 14 files. Average 4.0 per class. This is the texture of the whole course.**

It appears most often in figure captions, opening bullet lists, and closing recaps — the load-bearing summary slots, where it becomes the shape the reader carries away.

- `CCDV-F_Class-14.html`, figcaption, screen 1: *"Caching is a property of ordering, not of configuration."*
- `CCDV-F_Class-09.html`, figcaption, screen 1: *"The SDK is convenience, not capability."*
- `CCDV-F_Class-07.html`, figcaption, screen 1: *"Four positions, not one slider."*
- `CCDV-F_Class-08.html`, figcaption, screen 1: *"Model choice is a per-workload setting, not an architectural commitment."*
- `CCDV-F_Class-01.html`, figcaption, screen 3: *"Progressive disclosure is forced, not clever."*
- `CCDV-F_Class-02.html`, standalone paragraph, screen 2: *"It's the appointment, not the file."*
- `CCDV-F_Class-01.html`, screen 2: *"It's rent, not a purchase."*
- `CCDV-F_Class-12.html`, recap bullet: *"A stream is events, not an object."*
- `CCDV-F_Class-10.html`, recap bullet: *"The fix is structural, not phrasing."*

Nobody holds the negated half of most of these. No reader believes caching is "a property of configuration" or that a stream is "an object" as a stated position. The negation exists to give the sentence a fulcrum.

Two instances in the corpus are **justified** and should survive into the new material as models of correct use:
- `CCDV-F_Class-05.html`, screen 3: *"dontAsk is the strictest, not the loosest."* The mode's name genuinely misleads.
- `CCDV-F_Class-08.html`, screen 2: *"You are billed per token, not per request."* Readers do assume per-request billing.

Also note verbatim self-repetition: *"Loading is a prediction, not a lookup"* appears in Class 01's opening bullet list and again in its closing recap. *"A stream is events, not an open object"* / *"A stream is events, not an object"* appears twice in Class 12.

### D2 — Em-dash as the default connector
**332 instances. 12.9 per 1,000 words. Every file between 11.2 and 15.5 per 1,000.**

`anti-ai-writing-style_v1.md` sets a ceiling of two per page, roughly 4–5 per 1,000 words. The corpus runs about three times over, uniformly, which rules out "one dramatic class" and confirms it as a house habit.

| File | Words | Em-dashes | Per 1,000 |
|---|---|---|---|
| Class 01 | 3,825 | 43 | 11.2 |
| Class 04 | 1,806 | 28 | 15.5 |
| Class 10 | 1,506 | 23 | 15.3 |
| Class 12 | 3,859 | 46 | 11.9 |
| **All 14** | **25,714** | **332** | **12.9** |

Two-em-dash sentences are common:
- `CCDV-F_Class-14.html`, final screen: *"Move the volatile content below the breakpoint — the date and the user id belong in the turn, not in the system prompt — and make schema serialisation deterministic."*
- `CCDV-F_Class-01.html`, screen 1: *"If it allows it, the harness opens the file — your computer, your disk, your permissions — and then types the contents back down the phone."*

### D3 — The diagnose-negate-reveal tricolon
**27 pattern matches. Present in 11 of 14 files.** This is the specific construction the CLAUDE.md hard ban names.

- `CCDV-F_Class-01.html`, screen 1: *"It isn't an action. It's a sentence. It's a request, written down, and it arrives the same way every other piece of text arrives."*
- `CCDV-F_Class-12.html`, screen 1: *"because 'Forty-two' isn't a short address. It isn't an address at all. It's a piece of one, and a piece of an address will send a van to a street that doesn't exist."*
- `CCDV-F_Class-01.html`, screen 4: *"That's a judgment. Not a lookup."*
- `CCDV-F_Class-06.html`, screen 4: *"The test isn't detecting a defect. It's detecting a synonym."*
- `CCDV-F_Class-10.html`, screen 4: *"That is not a prompting failure. It is what a request is."*
- `CCDV-F_Class-02.html`, screen 4: *"It was never a tool problem. It was a memory architecture problem wearing a tool problem's clothes."*
- `CCDV-F_Class-05.html`, final screen: *"A control that the constrained person can switch off isn't a control — it's a preference with good intentions."*

The Class 05 `dontAsk` passage shows the construction applied to a real misconception and still overrun: *"dontAsk is not the relaxed one. It's the strictest one. It doesn't stop asking because it trusts you — it stops asking because anything not explicitly allowed is denied and there's nobody to ask."* Four beats where two would do the work.

### D4 — Sweeping or superlative claim, then defended
**~29 sweeping markers across 10 of 14 files.**

- `CCDV-F_Class-06.html`, standfirst: *"Almost everything that feels strange about working with this thing follows from that one sentence — including why your test suite keeps failing on correct answers."*
- `CCDV-F_Class-06.html`, recap: *"One mechanism — a draw from a distribution, one token at a time — and everything odd about the system falls out of it."*
- `CCDV-F_Class-08.html`, standfirst: *"reaching for the most capable model by default is the most common and most expensive model-selection mistake in production"* — asserted again inside the class as *"It feels safe and it is the single most common and most expensive model-selection error."* No source for either.
- `CCDV-F_Class-05.html`, standfirst: *"the whole skill of configuring it is knowing which of the four a given piece of knowledge belongs in"*
- `CCDV-F_Class-09.html`, screen 3: *"By the end of this screen you'll never conflate non-blocking concurrency with batch processing again"* — a promise the text cannot keep.
- `CCDV-F_Class-01.html`, screen 8: *"Some of what I've told you is close to physics. It'll be true in five years, and you can work things out from it."*
- `CCDV-F_Class-12.html`, screen 3: *"One rule falls out of that picture, and it is most of getting streaming right."*

### D5 — Isolated dramatic one-liner as punctuation
**25 short standalone paragraphs; roughly 10 of them carry no fact. 9 of 14 files.** CLAUDE.md permits one per document. Class 01 alone has four.

- `CCDV-F_Class-01.html`, close of screen 1: *"You can't reach through a telephone. Not even a very good telephone."*
- `CCDV-F_Class-01.html`, screen 2: *"That isn't an analogy for how it works. That's how it works."*
- `CCDV-F_Class-01.html`, screen 2: *"This one is stranger than the first."*
- `CCDV-F_Class-02.html`, screen 5: *"What it cost was when."*
- `CCDV-F_Class-10.html`, screen 1: *"Only a boundary creates a boundary."*
- `CCDV-F_Class-10.html`, screen 4: *"Capital letters are not an enforcement mechanism."*
- `CCDV-F_Class-12.html`, screen 4: *"Prompt bugs don't care about the network. This one is made of nothing else."*
- `CCDV-F_Class-05.html`, final screen: *"Bold type doesn't change what kind of thing a sentence is."*
- `CCDV-F_Class-09.html`, screen 1: *"Same three letters, unrelated jobs."*

### D6 — Second and third sentences re-say the first with more feeling
**~12 clear cases across 8 of 14 files.**

- `CCDV-F_Class-01.html`, screen 1: *"When your program uses Claude, here is the whole of what physically happens: some text goes out over the internet, and some text comes back. Out, and back. There is no other part to it."*
- `CCDV-F_Class-01.html`, screen 2: *"Every request that goes over the wire is complete in itself, and between requests nothing is kept. Nothing at all."*
- `CCDV-F_Class-01.html`, screen 4: *"There isn't one. There's no such machinery anywhere in the system."*
- `CCDV-F_Class-01.html`, screen 3: *"That's the trick, and it's exactly the trick."*
- `CCDV-F_Class-12.html`, screen 4: *"Everything about the failing request is innocent, because the failing request is innocent. It's carrying somebody else's mistake."*
- `CCDV-F_Class-03.html`, screen 3: *"There's no mode where the machine starts emitting objects. It's text. It's always text."*
- `CCDV-F_Class-05.html`, screen 1, heading plus first two sentences: heading *"Three kinds of safety measure, and they aren't the same thing"*, then *"Walk into a good workshop and you'll see three different kinds of safety measure. It's worth noticing that they're genuinely different things, rather than three flavours of the same thing."* The same claim three times inside a heading and two sentences.

### D7 — Manufactured strawman and reader mind-reading
**13 instances, clustered in Classes 01 (4), 03 (4), 10 (3), 12 (2).**

Applied to a genuine misconception, which the hard ban permits:
- `CCDV-F_Class-01.html`, screen 1: *"Now you're going to object, and it's a good objection, because everybody makes it."* Readers do believe Claude Code runs locally. This one earns its setup, though it is longer than it needs to be.

Applied to a plain checkable fact, where it is never justified:
- `CCDV-F_Class-01.html`, screen 4: *"You're imagining machinery. Something that takes your request, looks at the forty descriptions, works out which one matches best, and picks a winner. An index. A search. A lookup."* A detailed belief is constructed for the reader across four sentences so the next line can demolish it.
- `CCDV-F_Class-12.html`, figcaption on the image-cost screen: *"The difference is that you agonised over the system prompt and pasted the screenshots without thinking."* A claim about the reader's past behaviour, with no basis, attached to an arithmetic fact.
- `CCDV-F_Class-12.html`, screen 5: *"The instinct when a stream cuts out is to keep what you've got. You have most of a response sitting there; throwing it away feels wasteful. That instinct is the bug."*
- `CCDV-F_Class-03.html`, screen 5: *"Your instincts will fight this one."*
- `CCDV-F_Class-03.html`, screen 4: *"You created a position where the likely completion is a value — then were surprised to get one."*

### D8 — Rule-of-three padding
**7 clear cases across 5 of 14 files.**

- `CCDV-F_Class-01.html`, screen 1: *"Not on your laptop, not on your server, not anywhere you can point at."*
- `CCDV-F_Class-01.html`, screen 4: *"An index. A search. A lookup."*
- `CCDV-F_Class-12.html`, screen 1: *"There's no live handle, nothing to poll, nothing that stays open."*
- `CCDV-F_Class-12.html`, screen 4: *"The van was fine, the driver was fine, the manifest was fine."*
- `CCDV-F_Class-03.html`, screen 5: *"same fluency, same steadiness, same air of having checked"*
- `CCDV-F_Class-04.html`, screen 3: *"Sensible, dull, well understood."*

### D9 — Rhetorical question answered in the same breath
**6 clear cases across 4 of 14 files.** Lower frequency than the others, and some are legitimate Socratic pivots. The tell is when the question is asked and answered inside one paragraph with no pause for the reader.

- `CCDV-F_Class-01.html`, screen 2: *"So how do you have a conversation with it? Your program cheats."*
- `CCDV-F_Class-04.html`, screen 1: *"You didn't change the recipe. So what changed?"*
- `CCDV-F_Class-04.html`, screen 4: *"So what did all that pinning buy?"*
- `CCDV-F_Class-01.html`, screen 6: *"Ask why permissions must carry over. Suppose they didn't"*

### D10 — Template scaffolding repeated verbatim
**"By the end of this screen you'll…" appears 66 times across the 14 files. "Next. …" appears 50 times.** Every teaching screen in the course opens and closes with the same two stems. Not an AI tell in a single instance; at 66 repetitions in a fixed slot, it reads as generated to template rather than written.

### D11 — Looked for and NOT found
State these as absent rather than manufacturing examples.

- **"It's not just X, it's Y" and family.** Zero rhetorical instances. Five hits for the string "not just" and all five are ordinary adverbial use: *"A crowded board makes the thing dumber, not just slower"* (Class 01), *"not just its benefit"* (Class 02), *"not just test fixtures"* (Class 14). "Not only X but also Y", "it's not about X it's about Y" and "whether you're X or Y" do not appear at all.
- **Banned vocabulary from `my-voice.md`.** Five hits in 25,714 words: `journey` (Class 11, metaphorical), `essentially` (Class 14, "essentially zero", mid-sentence rather than as an opener), `nuanced` (Class 05, "more nuanced"), `highest-leverage` three times in Class 14. `delve`, `robust`, `seamless`, `comprehensive`, `ensure`, `leverage` as a verb, `landscape`, `unlock`, `holistic`, `in conclusion`, `it's worth noting`, `however,` and `specifically,` as sentence openers: all zero.
- **"I hope this helps" style closers, emoji, LinkedIn-voice throat-clearing.** All absent.

---

## 2. Where the prose genuinely works

The gate needs a positive target. These are quoted verbatim and are the model for the new material.

**Flat statement of a checkable fact, once.**
- `CCDV-F_Class-06.html`, screen 2: *"The context window is the total number of tokens the model can take in for a single request. It holds everything at once: system prompt, the full conversation so far, injected documents, every tool result, and the model's own output."* No wrapper, no reveal. The colon does the work an em-dash would have taken.
- `CCDV-F_Class-14.html`, screen 1: *"Prompt caching stores the processing work done on a stable prefix of your request, so follow-up requests can reuse it instead of reprocessing the same tokens."*

**Arithmetic done in front of the reader.**
- `CCDV-F_Class-12.html`, screen 6: *"Take a 1,000×1,000 screenshot. A thousand divided by 28 is about 36, so you get a 36×36 grid, which is 1,296 tokens. Do that arithmetic once by hand and you'll never need the formula again."* Concrete, checkable, and the reader can reproduce it.

**Numbers carrying the persuasion instead of adjectives.**
- `CCDV-F_Class-02.html`, screen 4: *"By the fourth session the history being injected at the start ran to more than forty thousand tokens. Before a single tool call. Add the system prompt and the tool schemas and the agent had burned over forty-five thousand tokens of its budget before doing one useful thing."*
- `CCDV-F_Class-11.html`, screen 1: *"The 4,000-token file you read on turn three is still being re-sent on turn nineteen, at full length, whether or not anything still depends on it."*

**A decision presented as questions with answers attached, no rhetoric at all.**
- `CCDV-F_Class-05.html`, screen 5: *"Is it true everywhere in this project? → CLAUDE.md / Is it true only in one part of the code? → a rules file with a paths glob / Must it happen every single time, regardless of what the model decides? → a hook / Would doing it flood the board? → a subagent"*

**Analogy that carries transferable detail rather than a mood.**
- `CCDV-F_Class-04.html`, screen 1: *"If your notes say 'flour: bread flour,' you're finished — you can't get back to the flour that worked. If they say 'flour: Shipton Mill, batch 4471,' you can go and buy that flour and settle the question in an afternoon."* The two branches do different work and the specificity is the point being taught, not decoration.

**Mechanism stated once with its cause.**
- `CCDV-F_Class-05.html`, screen 6: *"Configure a PostToolUse hook that runs Prettier, and it happens every single time, without exception, because the hook fires independently of anything the model decided."*

**Answer first, then the reason.**
- `CCDV-F_Class-12.html`, exercise answer, screen 4: *"Two tool_result blocks — one for toolu_01A and one for toolu_01B. The invariant counts blocks and matches ids; it does not ask whether your tool succeeded."*

**What these have in common:** a number, an API name, or a mechanism does the persuading. The sentence states its fact and stops. Where an analogy is used, the detail inside it maps onto something the reader will have to do. None of them tells the reader what they were thinking, and none of them ends on a flourish.

---

## 3. THE GATE

### 3.1 The voice target, stated positively

A confident professor teaching a capable student states the fact, gives the reason, and moves on. They do not build suspense about a schema field. They assume the student can hold a plain sentence without being warmed up for it. Eight rules, each with a before/after where the "before" is a real sentence from the old classes.

---

**Rule 1 — A checkable fact gets one flat sentence. No setup, no reveal.**

Before (`Class-01`, screen 1): *"Claude runs on machines in Anthropic's data centre. Not on your laptop, not on your server, not anywhere you can point at. When your program uses Claude, here is the whole of what physically happens: some text goes out over the internet, and some text comes back. Out, and back. There is no other part to it."*

After: "Claude runs on Anthropic's servers. Your program sends text over the internet and gets text back. That is the whole of the interaction."

---

**Rule 2 — Contrast only when a named person holds the other view. Otherwise assert.**

Before (`Class-14`, figcaption): *"Caching is a property of ordering, not of configuration."*

After: "Caching depends on request order. The cache is read from the start of the request up to your breakpoint, so anything that changes above the breakpoint destroys the hit."

Keep, as the model of a contrast that earns its place (`Class-05`): *"dontAsk is the strictest, not the loosest."* The mode's name misleads, so there is a real belief to correct.

---

**Rule 3 — Never tell the reader what they were thinking.**

Before (`Class-01`, screen 4): *"You're imagining machinery. Something that takes your request, looks at the forty descriptions, works out which one matches best, and picks a winner. An index. A search. A lookup."*

After: "There is no matcher. The descriptions sit on the board next to your question, and Claude predicts which one a question like yours would call for."

---

**Rule 4 — Say it once. If the next sentence adds no fact, delete it.**

Before (`Class-01`, screen 2): *"I don't mean it forgets. Forgetting means you had something and lost it. It never had it. Every request that goes over the wire is complete in itself, and between requests nothing is kept. Nothing at all."*

After: "It never had it. Every request is complete in itself, and nothing is kept between requests."

---

**Rule 5 — One em-dash per paragraph at most. Reach for a colon, a full stop, or a comma.**

Before (`Class-14`, final screen): *"Move the volatile content below the breakpoint — the date and the user id belong in the turn, not in the system prompt — and make schema serialisation deterministic."*

After: "Move the volatile content below the breakpoint. The date and the user id belong in the turn. Make schema serialisation deterministic."

---

**Rule 6 — Let a number carry the weight. If you cannot source the superlative, drop it.**

Before (`Class-08`, standfirst): *"reaching for the most capable model by default is the most common and most expensive model-selection mistake in production"*

After: "Teams default to the most capable model. An eval on your own hardest cases is what tells you whether the extra cost bought anything."

The rule is not "find a statistic". It is: if you cannot write the number, do not write "most".

---

**Rule 7 — Keep the analogy, cut the curtain call.**

Before (`Class-01`, close of screen 1): *"So Claude never touched your file. Your own computer touched your file, because Claude asked it to. // You can't reach through a telephone. Not even a very good telephone."*

After: "So Claude never touched your file. Your own computer touched it, because Claude asked."

---

**Rule 8 — Ask a question only if you intend to leave it with the reader.**

Before (`Class-01`, screen 2): *"So how do you have a conversation with it? Your program cheats. Every time you send a new message, it sends the entire conversation again, from the very first line."*

After: "A conversation works because your program re-sends the whole transcript on every request. Turn forty is one request containing all forty turns."

---

### 3.2 Prohibition list, ranked by observed frequency

Ranked by how often the defect actually occurred in the 25,714-word scan, not by how bad it sounds in theory.

| # | Prohibition | Observed | Files affected |
|---|---|---|---|
| 1 | "X, not Y" contrast pairs where nobody holds Y | 56 | 14 / 14 |
| 2 | Em-dash as default connector (>5 per 1,000 words) | 332 (12.9/1k) | 14 / 14 |
| 3 | Diagnose-negate-reveal tricolon | 27 | 11 / 14 |
| 4 | Sweeping or superlative claim then defended | ~29 | 10 / 14 |
| 5 | Isolated dramatic one-liner as punctuation | ~10 fact-free of 25 short paras | 9 / 14 |
| 6 | Second/third sentence re-saying the first | ~12 | 8 / 14 |
| 7 | Manufactured strawman / reader mind-reading | 13 | 5 / 14 (clustered) |
| 8 | Rule-of-three padding | 7 | 5 / 14 |
| 9 | Rhetorical question answered in the same paragraph | 6 | 4 / 14 |
| 10 | Template stem repeated in a fixed slot | 66 + 50 | 14 / 14 |
| 11 | "not just X, but Y" family | **0** | 0 / 14 — keep it that way |
| 12 | Banned vocabulary from `my-voice.md` | 5 | 4 / 14 — near clean already |

The ranking matters operationally. Items 1 and 2 are the whole document's texture and will not be fixed by spot edits: they need to be designed out of the sentence template the writer is working from. Item 7 is rarer but is the one Ram rejected the previous course over, so it carries a zero-tolerance verdict despite its low count.

---

### 3.3 Mechanical checklist

Run over one finished chapter. Each check is phrased so two reviewers counting independently land on the same number. "Chapter" means one class; "screen" means one teaching unit within it.

**C1 — Contrast-pair budget.**
Count sentences containing `, not <word>` or an `is/isn't X … it's Y` pair. **FAIL if the count exceeds 2 for the chapter, or if any appears in a figure caption, an opening bullet list, or a closing recap bullet.** For each survivor the author must be able to name who holds the negated belief in one line. Old corpus: 56, average 4.0 per chapter.

**C2 — Em-dash density.**
Count `—` in body prose. **FAIL if the count exceeds 5 per 1,000 words, or if any single sentence contains more than one.** Old corpus: 12.9 per 1,000, with multiple two-em-dash sentences.

**C3 — Negation tricolon. Zero tolerance.**
**FAIL on any run of two or more consecutive sentences that each negate the same subject before asserting** ("It isn't X. It's Y."; "That is not A. That is B."). The only exemption: the author records, in a comment beside the passage, the specific misconception being corrected and where a reader would have picked it up. An exemption claimed without that comment is a FAIL.

**C4 — One-liner budget.**
Count standalone paragraphs of 12 words or fewer. For each, apply the deletion test: remove it and ask whether any fact is lost. **FAIL if more than one fact-free short paragraph survives in the chapter.** Old corpus: Class 01 had four.

**C5 — Repetition check.**
Walk each paragraph sentence by sentence and mark every sentence that introduces a fact absent from all sentences before it. **FAIL if any paragraph contains two consecutive unmarked sentences.**

**Ram-approved exception, 2026-08-23 (Ch11, round 2).** Flagged: *"Both descriptions need the boundary. Fixing just one leaves the other's description exactly as ambiguous as it was."* (`Ch11_Why-Claude-picked-the-wrong-tool.md`, section "Writing a label that survives contact with a real question"). This was chapter 11's second gate round, at the process's 2-round cap, and the reviewer itself flagged the finding as involving interpretive judgment rather than a bare mechanical count. Presented with the exact sentence and three options (patch and re-round, review it himself, rewrite the section from outline), Ram chose to waive it and proceed, without reading the sentence himself. **Unlike the C14 exception above, this is not a finding that the passage is sound** — it is a pragmatic one-off call to stop spending rounds on a narrow, contested, non-zero-tolerance hit. Do not cite this as precedent for waiving a future C5 finding; each gets evaluated fresh.

**C6 — Reader mind-reading. Zero tolerance for the unsourced form.**
**FAIL on any sentence asserting what the reader believes, expects, imagines, feels, or previously did**, unless the same paragraph names the source of that claim (an exam distractor, a documented misconception, a named incident). Even sourced, **FAIL if more than one appears per chapter.** Test case from the old corpus that must FAIL: *"The difference is that you agonised over the system prompt and pasted the screenshots without thinking."*

**C7 — Unsourced superlative.**
**FAIL on "most common", "most expensive", "the whole of", "everything", "almost everybody", "never", "always" used as a claim about people or the industry, unless a number or citation appears in the same paragraph.** Claims about mechanism are exempt ("the model never has state between calls" is a fact about the system, not about people). The distinguisher: is the superlative about the world of humans, or about the API.

**Ram-approved exception, 2026-08-23 (Ch11, round 2).** Flagged: *"it's the one that actually resolves an overlap"* (following "most descriptions skip [the exclusion clause]"), plus a second, weaker instance, *"this covers most tool-use traffic in practice"* (`Ch11_Why-Claude-picked-the-wrong-tool.md`, same section as the C5 exception above: "Writing a label that survives contact with a real question" / "Who actually walks to the shelf"). Same round, same disposition, same reasoning as the C5 exception directly above — Ram waived both without reading the sentences himself, to close out the chapter rather than run a third round on checks the reviewer flagged as judgment calls. **Not a finding that the sentences are sound.** Do not cite as precedent for a future C7 finding.

**Ram-approved exception, 2026-08-24 (Ch14, round 2).** Flagged: *"A user can already ask for most tasks in plain language"* (`Ch14_Build-once-connect-many.md`, opening paragraph explaining when a prompt earns its place). Same disposition as the Ch11 exceptions above — Ram waived without reading the sentence in isolation, choosing to close the chapter rather than dispatch a further round on a check the reviewer flagged as one of a two-item bucket FAIL. **Not a finding that the sentence is sound.** Do not cite as precedent for a future C7 finding.

**C8 — Rule-of-three.**
Count asyndetic three-item lists. Classify each as enumerative (items are distinct and at least one is referenced later) or rhythmic (items are near-synonyms, or two could be cut with no fact lost). **FAIL if more than one rhythmic triple appears in the chapter.**

**C9 — Rhetorical question.**
**FAIL if a question mark is followed by its own answer inside the same paragraph.** A question may open a screen and be answered after the reader has been asked to attempt something, or may close a screen unanswered.

**C10 — Template stem.**
Count occurrences of any identical sentence stem of 4+ words appearing in the same structural slot. **FAIL if any stem occupies the same slot in more than 3 units of one chapter.** Old corpus: "By the end of this screen you'll…" 66 times, "Next. …" 50 times.

**C11 — Banned constructions. Zero tolerance.**
Search for "not just … but", "not only … but also", "it's not about … it's about", "whether you're … or". **FAIL on any hit.** Old corpus: absent. This check is a regression guard, not a repair.

**C12 — Banned vocabulary.**
Run the `my-voice.md` master list. **FAIL on any hit** other than a literal technical use (`harness` as the Claude Code component, `navigate` as a browser action). Old corpus: 5 hits.

**C13 — Fact density (positive check).**
**FAIL any screen that contains no number, API name, file path, parameter, or precisely stated mechanism.** Analogy without checkable content does not pass.

**Ram-approved exception, 2026-08-24 (Ch14, round 2).** Flagged: the chapter's opening section, a water-main analogy with no number, API name, file path, parameter, or stated mechanism. Part of the same round-2 bucket FAIL as the C7 exception above (two hits in the ten-check bucket). Ram waived without requesting a rewrite, the same pragmatic close-the-chapter disposition as the other Ch14 and Ch11 exceptions on this page. **Not a finding that the opening carries sufficient fact density** — a deliberate tradeoff, made once, at the chapter's round cap. Do not cite as precedent for a future C13 finding on an analogy-only opening.

**C14 — Analogy fidelity.** *Added 2026-08-22, after the specimen chapter in `CCDV-F_Specimen-Gated_v1.md` passed every check above while its own analogy inverted on its own stated discriminator — a subscription owned externally, mapped onto an MCP server the reader owns, under a discriminator the chapter itself named as "who owns the capability when it changes."* For each extended analogy in the chapter, build a two-column table: every analogue named, and the referent it is mapped onto. Then, for each row, search the chapter for a sentence that assigns the referent a property contradicting the analogue's stated property. **FAIL on any contradicted row.** Separately, **FAIL on any sentence claiming the mapping is exact, complete, or one-to-one** ("maps exactly", "the same X", "identical") **unless the chapter also states, in one sentence, what the analogy does not carry.** Zero tolerance — same tier as C3/C6/C11.

**Ram-approved exception, 2026-08-23.** The unhedged-exact-mapping clause above does not require a
hedge sentence on an analogy's own *introductory* transition ("X runs along the same line as Y", "the
same pattern applies here") once that analogy's own fidelity table has been built and confirms zero
contradicted rows. The clause exists to stop an analogy from claiming precision it doesn't have; once
fidelity is independently verified, forcing a carve-out sentence onto the sentence that merely
announces the analogy is redundant rather than protective. This does **not** relax the clause for a
claim about one specific transferred property — a row still needs either a true, uncontradicted mapping
or a stated carve-out — only for the sentence that opens the comparison. Precedent:
`Ch07_When-asking-nicely-stops-working.md`, "Claude's output guarantees run along the same line"
(opening the "Three rungs" section), flagged on gate round 5 of that chapter despite that same round's
own two fidelity tables — covering every extended analogy in the chapter — finding zero contradicted
rows in either. Closed by Ram rather than running a sixth round on a passage three consecutive rounds
had already confirmed substantively sound.

**Ram-approved exception, 2026-08-24 (Ch14, round 2).** Flagged: the self-test's Question 4 stem describes a committed per-client stdio MCP configuration as making "every clone launch[] the same server automatically" — reusing "launches" for the shared-server case that the chapter's own "What actually runs when three people connect" section spends a full section establishing does *not* hold for that setup (`Ch14_Build-once-connect-many.md`, self-test Question 4 vs. that section). This is the first C14 hit located inside a self-test item rather than teaching prose, and — unlike the Ch7 exception above — **not a finding that the passage is sound**: Ram waived it without independent verification, the same pragmatic disposition as the C5/C7 Ch11 exceptions, extended here for the first time to a zero-tolerance check. Presented with the exact contradiction verbatim and three options (targeted fix, waive, fix-plus-third-review), he chose to waive and close the chapter. Do not cite this as precedent for waiving a future C14 finding by default — each zero-tolerance hit is still evaluated on its own facts; this one was a deliberate cost/thoroughness tradeoff, not a determination that self-test/teaching-prose contradictions are acceptable going forward.

**Verdict rule.**
- Any FAIL on **C3, C6, C11, or C14** → chapter FAILS outright. These are zero-tolerance; a single instance of any one is sufficient.
- Two or more FAILs across the remaining ten checks (C1, C2, C4, C5, C7, C8, C9, C10, C12, C13) → chapter FAILS.
- **Exactly one FAIL on any single one of those same ten checks** → verdict is **FIX**, with the offending sentences quoted. This applies uniformly across all ten — there is no narrower "budget checks" subset that gets FIX while the rest get something else. *Two independent chapter reviews (Ch03, Ch04 — 2026-08-22) found the original wording named only five of the ten and had no defined outcome for a single failure on C5, C7, C9, C12, or C13. Both reviewers independently extended the same proportionate logic by analogy and flagged the gap rather than guessing silently. This revision closes it so the next reviewer does not have to re-derive it.*
- No FAILs → **PASS**.

---

### 3.4 Worked demonstration

Verbatim from `CCDV-F_Class-01.html`, screen 1 ("Where is the thing you're talking to?"), 224 words:

> Not in the room with you.
>
> Claude runs on machines in Anthropic's data centre. Not on your laptop, not on your server, not anywhere you can point at. When your program uses Claude, here is the whole of what physically happens: some text goes out over the internet, and some text comes back. Out, and back. There is no other part to it.
>
> Now you're going to object, and it's a good objection, because everybody makes it. You've sat and watched Claude Code work in your terminal. It opened your files. It changed them. It ran your tests and read the output. You watched it happen with your own eyes. So it must be on your machine.
>
> It isn't. And what really happened is more interesting than what you thought happened.
>
> There's a small program running on your laptop — the thing you started when you typed claude. Call it the harness, which is what everyone calls it. That little program is the one on the phone, and it's the one with hands.
>
> Claude sends back a piece of text that says, more or less, "I'd like to open the file at src/main.py." Now look carefully at what that is. It isn't an action. It's a sentence. It's a request, written down, and it arrives the same way every other piece of text arrives.

**Rewritten to the standard, 155 words:**

> Claude runs on Anthropic's servers. Your program sends text over the internet and gets text back. That is the whole of the interaction, on every surface, including the one where you watched Claude Code edit a file on your own disk.
>
> Here is what happened in that case. When you typed `claude`, you started a small program on your laptop. Everyone calls it the harness. Claude sent it a piece of text saying, in effect, "open src/main.py". The harness read that text, decided whether to allow it, opened the file with your permissions, and sent the contents back.
>
> So the request came from Anthropic's machines and the file operation happened on yours. Claude asked; the harness acted.
>
> That split decides everything that follows. Whatever the harness can reach, Claude can reach by asking. Whatever the harness cannot reach, no instruction will get to.

**What changed, and why.**

The 54-word strawman went. The original built a belief for the reader ("you're going to object", "You watched it happen with your own eyes") so it could be knocked down; the rewrite states the fact and then walks through the case that looks like a counterexample. Three restatement runs went with it: *"Out, and back. There is no other part to it."*, *"It isn't an action. It's a sentence. It's a request, written down"*, and *"what really happened is more interesting than what you thought happened"*, which is a prediction about the reader's reaction rather than information. The mechanism is now given once in sequence (receive, decide, open, return), and the closing lines say what the fact is *for* instead of ending on the telephone flourish. Word count fell by 31 per cent while the passage gained a fact the original had deferred to a later paragraph: the harness checks permission before acting.

---

### 3.5 How the gate runs

**Unit.** One chapter of finished prose. Run it on the prose source before it becomes HTML, so the reviewer counts sentences rather than markup, and so a fix does not mean re-styling a page.

**Point in the pipeline.** After the chapter is drafted, before it is styled or published. Re-run after any edit adding more than one paragraph. Never run it on a partial draft: several of the defects above are only visible at chapter scale, because their signature is repetition.

**Who runs it.** A separate reviewer agent that has not seen the draft's brief, the teaching architecture, the previous CCDV-F classes, or the earlier gate report for the same chapter. It receives the chapter text plus this document and nothing else. This follows the blind-review rule in `CLAUDE.md`: state in the reviewer's prompt what was deliberately withheld.

**What it returns.**
1. A verdict line: PASS, FIX, or FAIL.
2. Raw counts for C1, C2, C4, C8, C10, with the denominator (word count) shown for C2.
3. For every other check: "clear", or the offending sentence quoted verbatim with its check number and screen. Paraphrase is not accepted. A defect reported without its quote is dropped from the report.

**On FIX.** The author agent repairs only the quoted sentences and re-runs the gate. Counts must be re-measured and re-reported, never asserted as fixed.

**On FAIL.** The chapter is rewritten from its outline rather than patched. Patching a chapter that failed C3 or C6 moves the defect instead of removing it, because those defects live in how the passage was conceived, not in its wording.

**Rounds.** Two gate verdicts, maximum — a hard cap, not a guideline subject to judgment. Draft → gate (round 1) → fix → gate (round 2). **If round 2 does not return PASS — FIX or FAIL, either one — stop and escalate to Ram immediately with both gate reports.** Do not dispatch a second fix. Do not dispatch a third gate round. Do not reason past this because a round-2 finding looks narrow, or because it's technically a new defect rather than a repeat of an already-fixed one — that exact reasoning produced a real overrun on chapter 13 (2026-08-23): round 2 returned FIX rather than PASS, and rather than stopping there, a second fix and a third full blind review were dispatched anyway, pushing the chapter's running total past 800,000 tokens — most of the way back to an unoptimized chapter's cost — before Ram interrupted it directly and pointed out that repeated full blind reviews were themselves the largest remaining cost driver. Three rounds of the same agent editing the same prose also converges on text that satisfies the counters and still reads wrong, which is the failure mode that produced the previous attempt. **Round 3 (if the chapter needs anything at all after round 2) is Ram's decision, not another agent's** — and it should usually be cheap: read the fix agent's own quoted before/after report and decide, rather than commissioning a fresh comprehensive blind review of the whole chapter to confirm what a targeted diff already shows.

**Calibration control.** Before trusting the gate on new material, confirm it correctly fails
`CCDV-F_Calibration-Fixture_v1.md` (in this same folder), flagging at least C1, C2, C3, C4, C6 and C7.
A gate that passes the fixture is miscalibrated and its verdicts on new chapters mean nothing.

**Changed 2026-08-23, cost audit.** The calibration target was the full `CCDV-F_Class-01.html`
(1,193 lines / 66,209 bytes), of which 371 lines — a `<style>` block and a `<script>` block — carry no
prose at all and were read in full on every round regardless. Of the file's ten teaching screens, five
(screens 1, 2, 3, 4 and 8) already contain a confirmed instance of every check this control requires;
the other five add no defect type the required six don't already cover. `CCDV-F_Calibration-Fixture_v1.md`
is those five screens, markup-stripped of everything but prose structure, verified 2026-08-23: 2,054
words, 22 em-dashes (10.4 per 1,000, clear of the C2 ceiling of 5), and the same defect-bearing
sentences the worked demonstration and defect catalogue above already cite as confirmed C1, C3, C4 and
C6 hits, present verbatim. No sentence was cut from context to make a check fire — every screen kept is intact,
contiguous chapter prose. The one check not independently hand-confirmed on this fixture is C7; a
reviewer may still find it fires (screen 1 carries "the whole of what physically happens" and
"everybody makes it," screen 8 carries "close to physics"), but this was not verified against C7's
exact wording the way the other five were, so the first run against this fixture should still watch
for it rather than assume it.

**Calibration log, added 2026-08-23, checksum scope fixed 2026-08-23.** Re-deriving this from scratch
every round was measured at roughly 183,000 tokens and 13 minutes per round across chapters 7 and 10's
five re-verify rounds — pure overhead, since the result depends only on this document's own check
definitions (§3.1–§3.3) and the fixed calibration input, neither of which changes round to round. Trust
a logged calibration instead of re-running it, under this rule:

1. Compute a checksum over **§3.1–§3.3 only**, not the whole file — everything from the line beginning
   `### 3.1` up to (not including) the line beginning `### 3.4`. Reproducible one-liner:
   `sed -n '/^### 3.1 /,/^### 3.4 /p' CCDV-F_Prose-Gate_v1.md | sed '$d' | sha256sum`.
   **Why not the whole file, as this section originally specified:** the log below is itself inside
   this file, in this same section, so hashing the whole file made every appended row invalidate the
   file for the very next round — confirmed empirically on chapter 11, whose round 2 could not match
   round 1's brand-new entry and had to re-run full calibration anyway. Scoping the hash to §3.1–§3.3
   hashes only the content the result actually depends on, so appending a log row here in §3.5 never
   moves the checksum a future round needs to match. The scope can still drift on a genuine rule change
   — a new exception note added inside §3.3 (as C5's and C7's already are) will change this checksum,
   correctly, because that is a real change to what a reviewer is being asked to apply.
2. If the log below has an entry whose checksum matches, cite that entry's verdict and flagged checks
   in your report instead of re-scoring the fixture. State plainly that you did this — skipping the
   re-derivation is not the same as skipping the report of the result.
3. If no entry matches (§3.1–§3.3 changed since the last logged run, or the log has no row under the
   current scheme yet), run the full calibration control as specified above, then append a new row
   below: date, the checksum you computed, the verdict, and the checks flagged.
4. Never cite a log entry without checking the checksum yourself first. Citing a stale entry without
   checking is itself a calibration failure, not a shortcut.

**Legacy rows below (2026-08-23, both same-day) were computed under the old whole-file scheme, against
the old full-HTML calibration target, and cannot be matched against a §3.1–§3.3-only checksum or cited
for a run against the fixture — they are kept only as a record that the gate reliably flagged the
required six checks twice running before this change.** The table has no row yet under the new scheme;
the next reviewer to run calibration will be the first to populate one, against the fixture, at the
fixture's lower cost rather than the full file's.

| Date | Checksum (scope) | Verdict | Checks flagged |
|---|---|---|---|
| 2026-08-23 | 3EC566CC0A7C (whole file — legacy, see above) | FAIL | C1, C2, C3, C4, C6, C7 |
| 2026-08-23 | F20DA6CF909B (whole file — legacy, see above) | FAIL | C1, C2, C3, C4, C6, C7 |
| 2026-08-23 | 47011b7a2c6bb260bf56367f6cd5855f1beb5d0d7b24d063b78b26a452270bfb (§3.1–§3.3, sha256, fixture run) | FAIL | C1, C2, C3, C4, C6, C7 |
