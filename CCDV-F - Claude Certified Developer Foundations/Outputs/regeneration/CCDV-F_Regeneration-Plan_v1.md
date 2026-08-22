# CCDV-F — Study Material Regeneration Plan

**Created:** 2026-08-22 · **Status:** ✅ Part I (chapters 1–5) complete and gate-verified · **Awaiting Ram's review before Stage 5/6 continues on chapters 6–34**
**Supersedes:** `Outputs/CCDV-F_Syllabus_v1.md` (29 classes, 14 built).

**Authoritative chapter list and budgets: `CCDV-F_Pedagogy-Design_v2.md` — 34 chapters, 79,500 words.**
**Authoritative sub-topic assignment: `CCDV-F_Coverage-Contract_v1.md` — 153 sub-topics, one owner each.**
Chapter briefs are built from the contract, never from the chapter one-liners.

## Part I — delivered 2026-08-22

| Ch | Title | Words | Rounds to PASS | Real defects fixed |
|---|---|---|---|---|
| 1 | The one budget everything spends | 2,585 | 5 | Mildest possible C3 hit · 2 fact-free one-liners · **an arithmetic impossibility in the worked example** (dev/prod overhead required a negative per-turn rate) · a follow-on C1 hit and C5 hit introduced by two of the fixes themselves · a causal claim contradicted by the chapter's own numbers |
| 2 | Why the same prompt answers twice differently | 2,360 | 1 | None — passed clean first time |
| 3 | Two dials, not one | 3,109 | 2 | Opening section had no checkable content (C13) |
| 4 | What is actually on the wire | 4,018 | 3 | Two separate C3 instances, each in a different paragraph, found by different reviewers on different rounds · a heading promising four items, delivering three · a `same three things` label on a four-item list, repeated twice |
| 5 | Who is waiting? | 3,342 | 3 | Two negation pairs · an ungrounded cold open · a closing overclaim contradicting an earlier-established fact · **a fresh C5 hit introduced by the very fix that resolved the C14 overclaim** |

**15,414 words total.** Every chapter cleared all 14 checks (C1–C14) on its final round, verified by a reviewer blind to the brief, the author, and every prior round's findings. Each final round's calibration control — a synthetic passage built to fail, checked against the gate before the real chapter is judged — held every time.

**What the process actually found, worth carrying into chapters 6–34:**
1. **Self-audits are not sufficient.** All five chapters self-reported clean; two were not. Independent blind review is load-bearing, not decorative.
2. **A fix for one check can trip another.** This happened three times — a C6 fix introducing a new C1 hit (ch.1), a C14 fix introducing a new C5 hit (ch.5), an arithmetic-consequence fix introducing a new C1 hit (ch.1 again). Every fix must be re-verified, including the reviewer's own.
3. **Reviewers catch different things.** Chapter 4's two C3 instances were each found by a *different* reviewer in a *different* round — round 1 missed the second one entirely.
4. **The gate document itself had gaps**, closed mid-run: C14 wasn't in the file at all until this session (added 2026-08-22, formally documented with the specimen finding as rationale), and the verdict rule had no defined outcome for a single failure on 5 of the 14 checks (closed the same day).
5. **The deepest defect found had nothing to do with prose style.** Chapter 1's worked numerical example was internally impossible — verified by solving the underlying system of equations, which returned a negative, physically-impossible rate. No amount of sentence-level polishing would have caught this; it required doing the chapter's own arithmetic by hand.
Re-run `budget-check.py` after any budget edit; it verifies attribution consistency and the ±20% rule.

> **The acceptance test, and the only bar that matters.** A student is dropped in cold. He studies
> this material and **nothing else**. Then he sits CCDV-F: 53 items, 120 minutes, closed book,
> multiple-choice and multiple-response. He passes.
>
> Everything in this plan is subordinate to that sentence.

---

## 1. Why this exists

The previous attempt produced 14 of a planned 29 classes. It was not abandoned for being wrong. It
was regenerated because the teaching was to be designed fresh, uncoloured by the existing syllabus,
from three inputs only: the corpus, the published weights, and the exam expectations.

Four agents were run to design and stress-test the replacement. Two were commissioned; two more were
added because the first two would otherwise have produced a teaching design and a writing standard
that had never been tested against each other.

| Agent | Given | Blind to | Result |
|---|---|---|---|
| Pedagogy architect | corpus, weights, exam expectations | old syllabus, old classes, project teaching contract | 32 chapters, 7 parts, 74,700 words → `CCDV-F_Pedagogy-Design_v1.md` |
| Prose gate | Ram's style files + the CLAUDE.md hard ban; scanned all 14 old classes | the teaching design | 13 mechanical checks from 25,714 words of evidence → `CCDV-F_Prose-Gate_v1.md` |
| Gate reviewer | the gate + one unlabelled passage | author, course, brief | **FIX** — design and gate are compatible |
| Cold-start adversary | the design + the blueprint | the old material | **Pass achievable, with 8 conditions** |

The architect confirmed it encountered none of the withheld material.

---

## 2. The four findings that shape the build

### 2.1 The corpus cannot produce a passing course

Two agents grepped `sources/course-transcripts/` independently and agree. These return **zero** across
all 381,000 characters:

`Strands` · `LangGraph` · `PydanticAI` · `built-in tool` · `pinning` · `prompt versioning` ·
`plugin dependenc` · `SDLC` · `life cycle` · `websocket` · `socket` · `PII` ·
`business requirement` · `functional requirement` · `session hygiene` · `large-scale refactor` ·
`auto-mode` · `streaming mode`

The adversary then swept the blueprint's own bolded language and found **eleven further zeros the
architect missed**: `sanitiz`, `iterative refinement`, `self-hosted`, `fast mode`,
`client-side tool` / `server-side tool`, `approval pattern`, `data leakage`, `confidentiality`,
`content policy`, `guardrail layer`, `identity validation`.

**Twenty-one gaps, not ten.** `Claude Desktop` appears once in the entire corpus — inside Claude
Application Design, the largest single skill on the paper at 8.6%.

Consequence: the gap-filling chapter list must be **6, 7, 10, 11, 13, 16, 21, 22, 23, 28, 29, 30, 31,
32** — the architect's list omitted 6, 7, 10, 11, 28 and 29, so an author working from the design
alone would write them from the corpus and inherit its blind spots.

### 2.2 Instrumentation decides pass or fail, not prose

`CCAR-F/prep with quiz/EXAM-LOG.md` states the scoring convention explicitly:
`round((correct/60) × 900 + 100)`, with the pass boundary recorded at 42/60 = 730 and 41/60 = 715.

Applied to 53 items: **720 = 37 correct. The margin is 16 items.**

> **Caveat, carried deliberately.** That map is this project's own mock-scoring convention, verified
> internally consistent across its own scored papers. Pearson's real scaling for CCDV-F is not
> published. It is the only calibration available.

The design as written offers **one** practice paper. The same candidate sat roughly twenty on the
sibling exam before passing it. Under an acceptance test that says *studies this and nothing else*,
there is no external bank to close that.

### 2.3 The design and the writing standard are compatible

The architect's specimen passage was handed to a reviewer who knew only the gate. Verdict: **FIX**.
It cleared all three zero-tolerance checks — negation tricolon, reader mind-reading, banned
constructions — and failed only em-dash density, 6 in 592 words against a ceiling of 3.

The reviewer passed a calibration control first: it wrote a deliberately defective passage and
confirmed the gate failed it. The clean verdict is not a rubber stamp.

### 2.4 The gate has a hole, and the design walks through it

The specimen states its discriminator as *"They differ on one question: who owns the capability when
it changes."* Its fourth analogue is a subscription to someone else's service — owned externally. Its
fourth referent is an MCP server, *"You build it once"* — owned by the reader.

**The mapping the passage calls exact inverts on the one variable it declared decisive.** No check
C1–C13 catches it. The design mandates 32 unique never-reused anchors, so this is systemic.

**C14 — Analogy fidelity** is therefore added to the gate:

> For each extended analogy, build a two-column table of every analogue and the referent it maps
> onto. For each row, search the chapter for a sentence assigning the referent a property that
> contradicts the analogue's stated property. **FAIL on any contradicted row.** Separately, **FAIL on
> any sentence claiming the mapping is exact, complete or one-to-one** unless the chapter also states,
> in one sentence, what the analogy does not carry.

---

## 3. Decisions locked 2026-08-22

| # | Decision | Chosen |
|---|---|---|
| 1 | Input set | Corpus + weights + exam expectations **+ Anthropic product and platform docs, cited per claim** for the 21 gaps |
| 2 | Scope | Course **+ full instrumentation** — 30-item diagnostic pre-test, three full weighted mocks, RECALL/CONCEPT miss log |
| 3 | Cadence | **Gate after Part I.** Build 5 chapters, Ram reads them, briefs adjust, then the remaining 27 |
| 4 | Format | **Paged HTML only, canonical.** Resolves the markdown/HTML duplication left open in the syllabus on 2026-08-20 |

Existing classes archive to `Outputs/classes/_v1-archive/`. Nothing is deleted.

---

## 4. Defects to repair before any chapter is written

From the adversary's audit. All verified against the design file.

**Coverage**

1. **"Invoking Claude through third-party vendors" appears nowhere.** Bolded inside a 6.8% skill.
   `Bedrock` and `Vertex` are in the corpus (M2 ×4, M4 ×2) — the design dropped them while its
   word-count audit showed the skill healthy at +2.4%. Author into ch.24.
2. **The three named frameworks have no word budget.** §6 says they must be authored; §3 allocates
   them nothing. Ch.16 is billed 100% to a different skill.
3. **"Guardrail layering" and "content policy" appear in no chapter line.** Layering is the exact
   shape of the guide's own sample item 2.
4. **Prompt Engineering at −24.3%, undefended.** Invisible because Domain 6 nets to −0.3pp. Restore
   to ≥3,000 words or defend it in writing as the other six breaches are.
5. **Ch.23 carries four unrelated sub-topics in 3,000 words** — 750 each, with two of them
   duplicating ch.28 and ch.11. Split it.
6. **A factual error in the D2 defence.** The design says the residual 967-word deficit sits in two
   skills "both under 8% off share." They are 9.7% and 15.1%.

**Sequence — five forward references**

| Ref | Chapter | Uses | Taught in | Distance |
|---|---|---|---|---|
| FR1 | 7 | strict tool use | 10–11 | 3 |
| FR2 | 8 | subagent handoff | 18 | **10** |
| FR3 | 6 | input sanitisation | 28 | **22** |
| FR4 | 13 | Skills, MCP servers | 14 / 20–21 | 1 and 7 |
| FR5 | 19 | deny over ask over allow | 20 | 1 |

FR3 is not an ordering nit — it forces ch.6 to state sanitisation as a decree, which is the one thing
the design says it never does. FR2 is obscured in the design's own §2, which credits ch.1 with
unlocking subagent handoffs; ch.1 teaches the context window, not subagents.

Also: ch.19 and ch.21 both own hooks. That is the retrieval ambiguity FM2 exists to prevent.

**The Domain 2 experience substitution — judged unsafe as stated**

The design discounts Software Engineering Foundations, Understanding Requirements and Systems Life
Cycle by 2,660 words on the strength of twenty years of consulting. `EXAM-FACTS_v1.md` §3 agrees on
the terrain. The adversary's objection is that the discount is applied to the wrong axis: experience
substitutes for *understanding* the material, not for *recognising this exam's vocabulary* for it, and
these are the most definitional skills on the blueprint. Together they are 7.2 items against a 16-item
margin, with zero corpus cross-check.

**Resolution adopted: hold the word cut, triple the item counts.** For definitional skills, item drill
tests vocabulary recognition and prose does not.

---

## 5. The ten stages

| # | Stage | Owner | Input | Output | Acceptance test |
|---|---|---|---|---|---|
| 1 | ✅ **Repair the design** | Claude | §4 above | `CCDV-F_Pedagogy-Design_v2.md` | **Done 2026-08-22.** Seven repairs; 32 → 34 chapters, 74,700 → 79,200 words. All 34 chapters' attributions verified to sum exactly. Five ±20% breaches remain, all defended, none new — every skill v1 left undefended is now inside tolerance. FR3 resolved as a side effect |
| 2 | ✅ **Sub-scope coverage sweep** | auditor agent | all 25 scope cells, phrase by phrase | `CCDV-F_Coverage-Contract_v1.md` | **Done 2026-08-22.** 153 sub-topics atomised, each placed exactly once — 108 explicit · 44 implied · 1 absent (`integrity`, now in ch.29). Nine **bolded** sub-topics were implied-only and are now verbatim in their chapter lines. Ch.20's line named none of the five Claude Code primitives. 13 double-owned sub-topics given an owner. Total 79,200 → 79,500 |
| 3 | ✅ **Fix forward references** | Claude | FR1–FR5 | `Pedagogy-Design_v2.md` §7 | **Done 2026-08-22.** All five closed by spiral, none by reordering. Hooks assigned to ch.19 alone; ch.21 becomes *three* places. **One item held open for Stage 2 reconciliation: Skills have no home chapter** despite appearing in two published skills totalling 7.2% |
| 4 | ✅ **Ledgers and chapter briefs** | Claude | design v2 + coverage contract | `CCDV-F_Chapter-Briefs_v1.md` | **Done 2026-08-22.** 34 briefs, each carrying its idea, form, opening, anchor, owned sub-topics, source, boundary and must-lands. All three ledgers verified by `ledger-check.py`: 34 forms summing correctly with none over the cap of 3, zero adjacent form repeats, zero adjacent opening repeats, 34 distinct anchors. Heading rule is a build-time grep, run at Stage 7 |
| 5 | Source packs for gap chapters | research agents | the 21 gaps | cited extracts | Every claim traceable to an Anthropic-controlled URL. Gap list includes ch.6, 7, 10, 11, 28, 29 |
| 6 | Author, part by part | author agents, one per chapter | brief + source pack | chapter prose | Skeleton first, then anchor-by-anchor `Edit` calls ≤300 lines (DV-01). Agent reports which anchors it filled |
| 7 | Gate each chapter | fresh reviewer, blind | chapter + gate | PASS / FIX / FAIL | C1–C14. Reviewer fails its own defective passage first. **Two rounds maximum, then escalate to Ram** — never a third |
| 8 | Items and interference sets | item agents | chapter + the 3 published distractor families | items | 3–5 per chapter, **8–10 for ch.30–32**. Interference sets carry stated counts. MCQ/MR only, never fill-in-the-blank. One chapter teaches elimination-to-the-count |
| 9 | Instrumentation | Claude | design v2 | pre-test, 3 mocks, miss log | 30-item diagnostic before ch.1; three full weighted 53-item papers, attempt-dated; RECALL/CONCEPT tagging with the threshold at which the judgement-not-syntax assumption is declared wrong |
| 10 | Build and verify HTML | Claude | approved prose | paged course | Prev **and** next on every chapter; diagram floor per chapter, enforced; chain verified in a browser |

---

## 6. Defects in the previous build these stages exist to prevent

Found by direct inspection of `Outputs/classes/html/`, not reported by any agent.

| Defect | Evidence | Guarded by |
|---|---|---|
| No `prev` links | Class 06 links only to 07; Class 12 only to 13 | Stage 10 |
| Diagram density decayed | SVGs per class: 6, 3, 3, 2, 2, 2, 1, 1, 2, 1, 1, 4, 1, 1 | Stage 10 diagram floor |
| Thin per screen | 25,714 words / 92 screens ≈ 280 per screen | Stage 1 word budget |
| Template stems | "By the end of this screen you'll…" ×66; "Next. …" ×50 | Gate C10 |
| One mock only | design as written | Stage 9 |

---

## 7. Standing rules for every stage

- **Blind review is real.** Every reviewer agent states in its own report what was deliberately
  withheld from it. A reviewer that has seen the brief is not reviewing.
- **No source, no claim.** Gap-chapter facts cite an Anthropic-controlled URL. Empty search results
  are reported as empty.
- **DV-01.** Any artifact over ~40 KB is built as a skeleton then filled anchor by anchor. A single
  large `Write` killed the generating agent once already.
- **DV-10.** Every agent brief ends with: *state plainly what you verified by checking versus what
  you only reasoned about.*
- **Volatile facts go to the marked appendix**, and self-test items may not test anything in it. The
  guide is v1.0 and states it is subject to change without notice.
- **Nothing here overrides `EXAM-FACTS_v1.md`.** If the guide moves past v1.0, that file is corrected
  first and this plan second.

---

## 8. Open risks not yet closed

1. **Nothing yet falsifies the founding assumption.** The whole design rests on the exam being
   judgement-shaped rather than recall-shaped. Stage 9's miss log is the tripwire; until it runs,
   the assumption is untested. `EXAM-FACTS_v1.md` §5 warns to stay alert for code-bearing stems.
2. **Technical Fundamentals is 6.1% with an unenumerable scope** — "foundational technical concepts"
   plus two examples. 3.2 items whose content cannot be predicted. Needs a breadth strategy; the
   design has no position on it.
3. **Nothing watches the blueprint itself.** The §3 weight contract is the spine of the design, and a
   silent guide revision would invalidate it with no chapter, ledger or guard noticing.
4. **Habit 1 is never drilled.** The project records three behavioural habits behind all 64 CCAR-F
   misses. The *break* step attacks habit 3 well. Habit 1 — reaching for a workaround beside a
   mechanism instead of a narrow adjustment to it — is named but not drilled as a habit.
