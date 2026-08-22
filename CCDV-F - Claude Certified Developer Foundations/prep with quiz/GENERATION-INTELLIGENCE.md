# CCDV-F Generation Intelligence Log

**Last updated:** 2026-08-20 · **Sessions recorded: 1** (engine build — no paper generated yet)

> AI-to-AI learning log. Records what each generation run discovered, so the next run starts from
> accumulated intelligence rather than cold. `EXAM-LOG.md` is the audit trail of what was *scored*;
> this file is the living record of what was *learned while building*. Modelled on the CCAR-F file of
> the same name, which reached 21 sessions and is the reason that project passed first attempt.

> **NO PAPER HAS BEEN GENERATED YET.** Session 1 built the mock-exam engine only. Paper generation is
> gated behind the corpus: questions may come only from `CCDV-F_Domain-N_v1.md` files, and none exist.
> The trackers below are seeded and empty on purpose — they are ready, not stale.

---

## How to use this file

**Before generating:** read the Open Findings Ledger top to bottom, then the Section Coverage Tracker
and Distractor Family Rotation to decide what this paper should reach for.

**After generating:** add a Session Reflection, update the two trackers, and raise any new finding as a
numbered `DV-NN` entry. A finding with no number cannot be cross-referenced later and will be
rediscovered from scratch.

**Findings are numbered permanently.** Never renumber. A closed finding stays in the ledger marked
CLOSED, with what closed it — the record of a mistake being fixed is worth more than a tidy list.

---

## Open Findings Ledger

Prefix `DV` so these never collide with CCAR-F's `PB-NN` findings when both files are read together.

### DV-01 — A single large `Write` will kill the generating agent · OPEN · CRITICAL

**What happened.** The first agent read everything it needed, reported "I have everything I need. Now
writing the template file," and died on an API error before a single byte reached disk. The template is
84 KB. The CCAR-F reference files are 170–200 KB.

**The fix that worked.** Build incrementally. Write a skeleton first containing the head, the complete
CSS, the body structure, and empty script sections marked with anchor comments — `/* ==== ITEMS ==== */`,
`/* ==== SCORING ==== */` and so on. Then fill each anchor with a separate `Edit` call, one section per
call, roughly 300 lines maximum. Write the README last as its own file.

**Also require the agent to report which anchors it filled**, so a partial failure is visible rather
than silent. A half-written file that nobody notices is worse than a crash.

**Generalises to:** any artifact over roughly 40 KB. This is the single most important entry in this
file for the next run.

### DV-02 — The CCAR-F reference is not self-contained · CLOSED (fixed in the template)

The reference implementation carries a Google Fonts `<link>` — a live network call in a file that is
supposed to run offline in a proctored-practice setting. Copying CCAR-F forward propagates it silently.
Removed and replaced with local font stacks. **Check for it again in anything else ported across.**

### DV-03 — Block architecture must be removed, not bypassed · CLOSED

CCAR-F grouped items into scenario blocks. CCDV-F items are standalone and the guide is explicit about
it. `renderBlockHdr`, `isFirstOfBlock`, `DATA.blocks`, `q.block`, `perBlock`, the jump-map grouping, the
per-block results grid and four CSS classes all came out. **Verify by grepping for zero references in
both the source and the rendered DOM** — dead code that never executes still misleads the next reader.

### DV-04 — Multiple-response state bug · CLOSED (found by exercising, not by reading)

Dropping a multiple-response selection back below the required count cleared the stored answer but left
the Next button enabled, contradicting the exam-mode spec. Fixed with `syncNextBtn()`.

**The lesson is the method.** This was not visible from reading the code or rendering the page. It
appeared only when someone clicked through the state transition and back again. **Exercise the
transitions, do not just confirm the render.**

### DV-05 — The project's own summary of the guide was wrong, and had been for a day · CLOSED

Every project file said the guide publishes **21 skills**. It publishes **25**. Counting the guide's own
Section 6 objective headings: 3 + 6 + 1 + 1 + 4 + 3 + 4 + 3 = 25, weights summing exactly to their
domains and to 100.0.

**What caught it:** building the engine required enumerating every section to construct the `SECTIONS`
map. Nothing else in the project had ever forced that enumeration.

**The generalisable rule:** when a generation run needs a number, count it from
`sources/CCDV-F_Official-Exam-Guide_v1.0.pdf`, not from a project file that summarises it. A figure can
propagate unchallenged precisely because it looks like it was already verified. Corrected in nine files
and recorded in `EXAM-FACTS_v1.md` §4.

### DV-06 — Browser screenshots are unavailable in this environment · OPEN

The Browser pane does not composite frames, so `screenshot` times out for both the main session and
subagents. Two consequences:

- **Verify through `read_page`, `read_console_messages`, and computed styles.** These confirm structure,
  absence of errors, and that CSS applies. They do not confirm the thing looks right.
- **Serve over `localhost`, never `file://`.** The preview pane serves `file://` as a `data:` URL, which
  breaks in-page anchors. The repo root is already configured as `cca-cert-hub` on port 18792.

**A human glance at the rendered page is still an open verification gap** on anything visual.

### DV-07 — Item section assignments are inference, not published fact · OPEN

The guide gives a **domain** for each of its three sample items and never gives a section. Every `N.M`
tag on an item is this project's judgement. Sample 3 was genuinely contested — §8.3 Agentic
Customization against §8.2 MCP Server Development — and was settled 2026-08-20 as **§8.3**, on the
grounds that the item's task is choosing among four approaches, which is how the guide defines §8.3.
The MCP server is the answer, not the subject.

**Rule going forward:** where a section assignment is arguable, record the reasoning in a code comment
at the item. Section numbering is permanent because misses are logged against it.

### DV-08 — Exporter and schema can drift · CLOSED

The results export emitted a `section_scores` field that `DASHBOARD-SCHEMA.md` did not define. The
building agent **flagged it rather than editing the schema itself**, which was the correct call — a
schema is a contract and gets signed off, not amended in passing. Extended additively 2026-08-20.

**Require this behaviour in every generation brief:** an agent that finds a contract mismatch reports
it and stops. It does not reconcile the contract to its own output.

### DV-09 — The corpus gate is real and blocks paper generation · OPEN

Practice questions may come **only** from `CCDV-F_Domain-N_v1.md` files. None exist. Until they do, the
engine ships with the three official sample questions from the guide, which are legitimate — published
by Anthropic, explicitly not drawn from the live item bank, and provided to show item style.

**Do not soften this.** On CCAR-F a community source claiming the exam draws 8 scenarios (the real
number is 6) reached generated practice material. That is what the rule exists to prevent.

### DV-10 — The agent brief shape that worked · OPEN · reuse verbatim

The successful brief had five parts, and the fifth is the one usually left out:

1. **An explicit read-order list** with full paths, including which file is the reference implementation
   and roughly how much of it to read.
2. **What to carry forward** from the reference, named specifically.
3. **What differs and must change**, numbered, each with its reason.
4. **Constraints** — read-only folders, self-contained output, no invented content.
5. **"Verify your own work, and state plainly what you verified by checking versus what you only
   reasoned about."** The agent came back with an honest list of what it could not confirm. Without that
   sentence, the same agent would very likely have reported the work as fully verified.

---

## Section Coverage Tracker

One row per published skill section. `≈items` is the weight applied to 53 — arithmetic, not stated by
the guide. Empty until the first paper is generated.

| § | Skill | % | ≈items | Papers used in | Learner signal |
|---|---|---|---|---|---|
| 1.1 | Agent Architecture | 4.5 | 2.4 | — | — |
| 1.2 | Agent Construction with Claude | 5.3 | 2.8 | — | — |
| 1.3 | Agent Patterns and Frameworks | 4.9 | 2.6 | — | — |
| 2.1 | Understanding Requirements | 3.4 | 1.8 | — | — |
| 2.2 | Systems Life Cycle | 2.8 | 1.5 | — | — |
| 2.3 | Claude API Mechanics | 6.8 | 3.6 | engine demo (official Sample 1) | — |
| 2.4 | Software Engineering Foundations | 7.4 | 3.9 | — | — |
| 2.5 | Claude Application Design | 8.6 | 4.6 | — | — |
| 2.6 | Configuration Management | 4.1 | 2.2 | — | — |
| 3.1 | Claude Code Operation | 3.1 | 1.6 | — | — |
| 4.1 | Debugging and Error Handling | 2.6 | 1.4 | — | — |
| 5.1 | LLM Fundamentals | 5.2 | 2.8 | — | — |
| 5.2 | Technical Fundamentals | 6.1 | 3.2 | — | — |
| 5.3 | Model Selection and Tradeoffs | 2.7 | 1.4 | — | — |
| 5.4 | Cost and Token Management | 2.8 | 1.5 | — | — |
| 6.1 | Context Engineering | 3.8 | 2.0 | — | — |
| 6.2 | Prompt Engineering | 4.6 | 2.4 | — | — |
| 6.3 | Output Handling | 2.6 | 1.4 | — | — |
| 7.1 | AI Application Security | 3.2 | 1.7 | engine demo (official Sample 2) | — |
| 7.2 | Guardrails and Safe Deployment | 2.3 | 1.2 | — | — |
| 7.3 | Claude Hooks | 1.0 | 0.5 | — | — |
| 7.4 | Identity, Secrets, and Key Management | 1.6 | 0.8 | — | — |
| 8.1 | Tool Implementation | 4.4 | 2.3 | — | — |
| 8.2 | MCP Server Development | 2.1 | 1.1 | — | — |
| 8.3 | Agentic Customization | 4.1 | 2.2 | engine demo (official Sample 3) | — |

**Sections under 1.5 expected items** — 2.2, 4.1, 5.4, 6.3, 7.2, 7.3, 7.4, 8.2, and 3.1 — will appear
zero or one times on any given paper. That is the real paper's shape. Do not force them in to make the
tracker look even, and do not read a trend from a single appearance.

---

## Distractor Family Rotation

Ten families. Six carried from CCAR-F, where each caught Ram at least once. Four lifted from how the
official sample rationales reject their own wrong options.

| Family | What it is | Used in |
|---|---|---|
| OVERSPEC | A stronger guarantee than the requirement asks for | — |
| DISCARD | Replace a working mechanism instead of adjusting it narrowly | — |
| REPAIR | Fix downstream what a constraint could have prevented upstream | — |
| ARCHITECTED | The option that sounds more professional or thorough | — |
| HALF-MOVE | A partial version of the right answer | — |
| WRONG-AXIS | Right vocabulary, wrong discriminator | — |
| IRRELEVANT-LEVER | A real control that does nothing for this problem | Sample 2 (temperature against injection) |
| UNENFORCEABLE | A request where a control is needed | Sample 2 (asking users politely in the system prompt) |
| BIGGER-HAMMER | Scale or upgrade instead of solving | Samples 1 and 2 (downsize/upsize the model) |
| FALSE-CAPABILITY | Assumes a capability the thing does not have | Sample 3 (built-in tools reach any internal REST API) |

**Vary families within each item.** Three flavours of the same wrong answer make an item that tests
nothing.

**Note what the official samples actually do:** `BIGGER-HAMMER` appears in two of three, and in Sample 2
the guide points out the bigger model can make injection *worse*. That is the house style — the wrong
option is a real technique, correctly described, that does not match the stated constraint.

---

## Item Pattern Library

Observations about item construction. Seeded from the three official samples; grows per paper.

- **Every stem carries a constraint.** All three samples do: *cost is the primary concern* · *hidden
  text in user-submitted content* · *reusable across several applications and maintained independently*.
  A stem with no constraint has no correct answer, only a preferred one.
- **No code appears in any official sample, and none is asked for.** Code belongs in an item only where
  the decision is *about* the code — schema shape, defensive parsing, error-handling strategy — and even
  then the question is which approach, never what the parameter is called.
- **Items are standalone.** Each states its own response count. No scenario blocks.
- **Stems run short.** All three samples are two or three sentences. Resist building a paragraph of
  scene-setting; the constraint is the payload.

---

## Rationale Quality Notes

- **The guide's own rationale style:** one sentence for why the correct answer is correct, then each
  wrong option dismissed in a clause naming *why the technique fails this constraint* — not why the
  technique is bad. "Sending requests synchronously in parallel does not reduce per-token cost" respects
  the technique and rejects it on the constraint.
- **The three official rationales are reproduced verbatim** in the engine's demo items. The only
  editorial change: the guide's combined per-sample sentence was split into per-option rows and the
  inline "(A)"/"(C)"/"(D)" markers dropped, since the interface already labels each row.

---

## Pending Decisions

| # | Decision | Status |
|---|---|---|
| 1 | Are multiple-response items all-or-nothing or partial credit? | **Unknown — the guide does not say.** Engine assumes all-or-nothing, marked in a comment at the scoring site. Confirm from the real score report after the sitting |
| 2 | Does the score report break down below domain level? | Unknown. Guide says percent-correct "within each content domain" — reads as 8 domains, not 25 sections |
| 3 | What counts as a "clean" paper for the booking gate? | Proposed ≥800 estimated scaled, based on CCAR-F precedent. **Awaiting Ram's confirmation** |
| 4 | Scaled-score estimator mapping | `round(correct / items × 900 + 100)`, same as CCAR-F so the two stay comparable. Pass line lands at **37 of 53**. Estimate only — labelled as such on the results card and flagged `authoritative: false` in the export |

---

## Session Reflections

### Session 1 — 2026-08-20 · Engine build, no paper

Built `mock-exams/CCDV-F_MockTest-TEMPLATE_v1.html` (84 KB) and its README, carrying the CCAR-F design
system forward with exam mode baked in from the start rather than retrofitted the way CCAR-F's Test 19
was.

**What went well.** The kept-versus-removed instruction produced a clean port with no dead block-
architecture code. Requiring the agent to state what it verified by checking versus by reasoning
produced an honest gap list instead of a confident all-clear. A Node harness of 111 assertions over the
scoring, estimator, tagging and export paths caught a real state bug (DV-04).

**What went wrong.** The first attempt died mid-write (DV-01) and produced nothing. Recovery cost one
full re-run, though the agent's context survived so the reading did not have to be repeated.

**The unexpected find.** The skill count (DV-05). Worth dwelling on: the error was not found by an audit
of the documents, but by a build that needed the number to be real. **Machinery that must consume a fact
is a better check on that fact than any number of readings of the file that states it.**

**Ready for Session 2**, which is the first real paper, and which cannot start until domain corpus files
exist. When it does: read the ledger first, seed from the Section Coverage Tracker and the Distractor
Family Rotation, and log every item's section as it is written rather than reconstructing afterwards —
CCAR-F's tracker went stale at Exam 12 precisely because reconstruction was left for later and then
could not be done honestly.
