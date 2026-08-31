# CCAR-P Mock-Exam Generation — Cost & Failure Audit

**Written:** 2026-08-30 · **Scope:** why Paper 2 generation cost extraordinary time and failed
outright today, and whether the generation system is over-engineered for what it needs to be.
**Method:** independent cold read of the orchestration spec, three sessions of
`GENERATION-INTELLIGENCE.md`, `EXAM-LOG.md`'s Paper 1 entry, today's `resume-prompt.md`, today's
actual dispatch briefs, the shipped schema/validator, and the deep-dive grounding record. Read-only —
nothing was generated, fixed, or edited as part of this audit.

---

## 1. Verdict

**Yes, over-engineered — but not uniformly, and the two layers do not share the blame equally.**
The core item spec (domain quota, objective floor, letter pre-plan, distractor-family caps, T1–T4,
stem/option word caps, `whyRight`/`whyWrong`) is ambitious but each piece is tied to a specific,
named, measured failure from Ram's real CCAR-F sitting or the official CCAR-P sample rationales — that
part is arguably correctly engineered for a Professional-tier fidelity target, not bloated. The
`deepDive` layer is different: it was added in a later session with no comparable evidence of need, it
roughly triples the prose and fact-checking burden per item, and the project's own audit of it found
that 21% of Paper 1's items (13/63) require a claim the corpus cannot actually support, with a further
15 items carrying an unshipped "partial support" caveat — 44% of the paper, in total, hit some
grounding shortfall in a layer nothing asked Ram to prove was needed. That is the majority of the
answer to "why is this taking so long." **The minority of the answer, but the direct trigger of
today's specific outright failure, is a process choice: dispatching each domain's entire item set (up
to 12 items, each needing ~500–700 words of individually fact-checked prose) as one long, uncheckpointed
agent turn that writes a single file only at the very end.** Today, every dispatch above 4 items failed
identically and completely; the only dispatch that worked was also, by a wide margin, the smallest.
That pattern is not proof of a specific infrastructure bug, but it is a clean, reproducible signal
that the unit of work per dispatch is too large — and shrinking it is warranted regardless of what the
exact "stream watchdog" mechanism turns out to be.

---

## 2. What's driving cost and time

### 2.1 The `deepDive` layer is the largest single cost added, and the least evidenced

Every other mechanism in `CCAR-P-Orchestration-Prompt_v2.md` carries a citation to a specific,
measured problem: the objective floor pass exists because "the real CCAR-F score report returned six
objectives at 0%" (§3.2); the letter pre-plan exists because "one block shipped all 15 questions at
the same option letter, undetected by that block's own QA" (§5.1); the inline-token ceiling is
inverted from the sibling project because "the CCAR-P guide's 12 sample options contain zero inline
code or config tokens" (F-04). `deepDive` has no such citation anywhere in the project. It is not
mentioned once in the original 91KB engine-design audit
(`Outputs/CCAR-P_Mock-Exam-Engine-Audit_v1.md`) — grepping that file for "deepDive" returns zero hits.
It first appears in `GENERATION-INTELLIGENCE.md` Session 3, described only as: "the engine gained a
second per-item explanation layer... both backfilled into Paper 1." No failure it fixes is named.

The size difference is the whole story. The existing "quick verdict" layer is `whyRight` (35–50 words)
plus three `whyWrong` entries (15–30 words each) — roughly 80–140 words per item, and it already
answers "why does this option win, why do the others lose." `deepDive` adds `principle` (45–75 words),
`rightDeep` (60–100 words), and three `wrongDeep` entries (45–80 words each) — roughly 240–415 *more*
words per item, each one required to trace to a specific corpus row, not merely be plausible
(orchestration prompt §5.5, rule 3: "A claim the corpus cannot support is not written"). Per item, that
is roughly 500–700 words of tightly-constrained prose in total (matches the audit brief's own
estimate), and unlike the quick layer, every sentence of it has to survive a **separate, independent
grounding-audit pass** — the spec is explicit that this can't be skipped: "an author asked to check its
own grounding reliably finds its own paraphrase sufficient" (§5.5). That is not a cheap add-on; it is
effectively a second authoring-and-review pipeline stacked on top of the first.

The project's own numbers show this ambition outstripping the corpus. `CCAR-P_DeepDive-Grounding-Record_v1.md`
documents that producing `deepDive` for the already-shipped Paper 1 took **21 additional agent
dispatches** (7 authors + 7 first-pass auditors + 7 second-pass verifiers), on top of whatever the
original 4-stage pipeline already cost — a cost never rolled into the "~7.7–8M tokens" figure, because
that figure was measured before `deepDive` existed. Two independent grounding passes raised 67 findings
between them; 54 were real. Of those, **13 items (21% of the paper) were classified IRREDUCIBLE** —
"every one is `T1ALT_MISSING`... in these 13 items no such row exists anywhere in the domain file"
(F-14, `CCAR-P_DeepDive-Grounding-Record_v1.md` §"The 13 irreducible findings"). A further 15 items
carry an unshipped "partial-support" note for the same reason. **28 of 63 items — 44% of the paper —
hit a real grounding shortfall in this layer alone**, on a paper that had already been through
authoring, verification, repair, and reverification for its base content. The spec's own claim that T1
"is cheap to check because the alternative answer is already written down" (§5.3) is empirically false
for a fifth of the paper (F-12). This is not a process bug; it is the content requirement asking the
corpus for more than 78 sections of decision tables can actually supply, discovered only because
`deepDive` forced a second close reading of material the first pass had already used.

**Would a shorter or absent `deepDive` meaningfully reduce Ram's chance of passing the real exam?**
There is no evidence either way yet — Paper 1 has not been sat. There is a real pedagogical argument
for it (generalizing from "why this option" to "what rule, and what would each wrong option actually
have been right for" targets root habit 3 in `CLAUDE.md` directly). But the project already has a
purpose-built, cheaper, evidence-backed mechanism aimed at that exact habit — Phase 7.1 rule 4, "habit
escalation," which makes an over-used distractor family the *correct* answer on 2–3 items once it
qualifies as a habit. `deepDive` is not the only or the primary lever for the stated goal, it is
untested, it is the single most expensive line item added, and the project's own audit already shows it
exceeds what the corpus can honestly support in nearly half the paper. That combination — expensive,
unproven, and already shown to overreach its source material — is the textbook definition of
cargo-culted rigor, not a demonstrated requirement.

### 2.2 The dispatch shape turns a large task into an all-or-nothing one

Today's session did implement the redesign that followed Paper 1's F-11 cost audit: it collapsed the
4-stage Author→Verify→Repair→Reverify pipeline into (per domain) one authoring pass with `deepDive`
inline, switched from the Workflow tool to the Agent tool specifically to avoid Paper 1's
`resumeFromRunId` duplicate-dispatch bug, and computed the entire central plan (letters, multi-response
pairs, distractor-family minimums, per-domain facet exclusions grepped directly from Paper 1's shipped
HTML) by hand before dispatching anything — exactly per orchestration prompt §5.1's requirement that
"the correct letter for item *k* is decided here," not delegated. That part of the redesign worked: it
is cheap (a single planning pass, not seven), it is well-justified (the letter-bias and family-skew
failures it prevents are independently documented, not hypothetical), and it should not be undone.

What it did not fix is dispatch granularity. `_PAPER2-STAGING/p2-shared-brief.md` and `p2-slots.md`
show each of the seven domain-authoring agents was asked, in one uninterrupted turn, to: read its
entire corpus file (up to 38,970 bytes for D3), then for every one of its 4–12 items independently
re-read the cited section "immediately before writing that item's `deepDive` — not from memory of what
it probably says," produce the full ~500–700-word package per item under the word-count and
family-quota constraints above, self-verify its own family and objective tallies, and write **one JSON
file at the very end**. Nothing is persisted incrementally. If the turn is interrupted at any point
before that final write, the entire domain's work — however much progress was actually made — is lost.

That is exactly what happened, six times out of seven, today: "Every single failure — 6 out of 6
non-D7 dispatches, both original attempts and all 4 retries — carried the identical error: `"Agent
stalled: no progress for 600s (stream watchdog did not recover)"`, with **ZERO partial output** every
time" (`resume-prompt.md`). D1, D2, D3, and D5 failed immediately and failed again on retry. D4 and D6
ran for 41+ minutes showing as `running` before failing the same way — "so 'running long' was not
actually progress, it was a slower path to the same wall" (`resume-prompt.md`). The one dispatch that
succeeded, D7, was also the smallest by a wide margin:

| Domain | Corpus file size | Items requested | Outcome |
|---|---|---|---|
| D1 | 33,671 bytes | 11 | failed (stall, zero output) |
| D2 | 15,564 bytes | 8 | failed (stall, zero output) |
| D3 | 38,970 bytes | 12 | failed (stall, zero output) |
| D4 | 35,538 bytes | 10 | failed (stall, zero output) |
| D5 | 30,643 bytes | 9 | failed (stall, zero output) |
| D6 | 29,729 bytes | 9 | failed (stall, zero output) |
| **D7** | 28,534 bytes | **4** | **succeeded (~191K tokens)** |

This table is my own cross-check, not a repeat of `resume-prompt.md`'s framing — and it sharpens the
signal in a way that file wasn't explicit about. **Corpus input size does not track the outcome**: D2
has the *smallest* corpus file of all seven (15,564 bytes) and still failed; D7's corpus file is not
the smallest, and it succeeded. **Item count — i.e., required output length — tracks the outcome
cleanly**: the only variable that cleanly separates the one success from all six failures is that D7
was asked for 4 items and everything else was asked for 8–12. That points specifically at how much a
single turn is expected to *produce*, not how much it has to *read*.

This is corroborated by Paper 1's own cost data, gathered before today's redesign: F-11 recorded "up to
264,744 output tokens on a single call, 97% of it thinking" for the largest per-domain dispatches under
the *old* 4-stage pipeline — meaning oversized single-turn generations were already producing extreme
thinking overhead before `deepDive` even existed and before today's stalls happened. Two independent
data points, from two different sessions and two different failure modes (huge-but-completing calls
in Paper 1; not-completing-at-all calls today), both implicate the same thing: a per-domain,
single-turn, single-file-at-the-end dispatch is carrying too much work for one turn.

What this audit cannot confirm — and what would need one more piece of evidence to settle absolutely —
is whether today was *also* a service-side degradation independent of task size. The controlled test
that would isolate this (dispatch one mid-size domain alone, no concurrent siblings, per
`resume-prompt.md`'s own proposed next step) was never run today. That gap does not weaken the
recommendation below, because chunking into smaller, checkpointed dispatches is a strict improvement
under either explanation: it shrinks the blast radius of a stall regardless of whether the stall's root
cause is size-correlated or uniformly-probable-per-large-call.

### 2.3 What is *not* the problem, stated plainly

To keep this specific rather than a blanket "everything is bloated" verdict:

- **The 13-check fidelity gate (Phase 6) is not a cost driver.** Twelve of its thirteen checks run
  inside `validateItems()`, a pure JavaScript function with zero LLM calls — instant, free, and
  already proven to catch real problems (it is what caught the two cross-domain `lessonKey` collisions
  on Paper 1 that no per-domain agent could see). The only expensive step feeding *into* satisfying the
  gate is the deep-dive grounding audit (§2.1 above), which is not part of the 13-check table itself.
- **The central pre-planning (§5.1–5.2: letter multiset, multi-response pairs, family quotas, facet
  exclusions) is cheap and well-justified.** It is one reasoning pass done once, not per-agent, and it
  exists to prevent a documented, previously-real failure (the same-letter block). Today's session
  executing it by hand before dispatch is not the source of the slowdown — it is one of the few things
  that worked cleanly today.
- **T1's requirement itself is sound; only its assumed cheapness was wrong.** F-12 shows the spec's
  claim that the alternative answer is "already written down" doesn't hold for a fifth of items, but
  the fix already adopted in today's own brief — "if your first choice of `t1Clause`/`t1Alt` does not
  resolve to an actual row, pick a different clause/alt pair" — is the correct, proportionate response.
  T1 should stay; it should not be blamed for the cost problem.
- **Domain-level parallelism is spec-mandated, not a session's invention.** §5.5 states plainly:
  "Authoring is per-domain and parallel, one worker per corpus file." Faulting today's session for
  fanning out 7 agents would be faulting it for following the orchestration prompt. What is a process
  choice — not mandated by the spec — is making each of those 7 workers do its *entire* domain in one
  uninterrupted turn instead of smaller batches within the domain.

---

## 3. A concrete simpler alternative: thin-ship, thick-review-on-demand

This is a different design, not a smaller version of the same one. It changes *when* `deepDive` gets
written and *for which items*, and it changes the unit of work per dispatch.

**Generation path (blocking — must finish before a paper can be sat):**

1. Ship every item with `stem`, `opts`, `correct`, `whyRight`, `whyWrong`, `t1Clause`, `t1Alt`, and all
   tagging fields — exactly as today, minus `deepDive`. `deepDive` defaults to `null` at ship time.
2. In `validateItems()` (`mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html`, the block at lines 962–983),
   move the `deepDive` presence checks from `E.push` (hard error) to `W.push` (warning) by default, or
   gate them behind an `opts.requireDeepDive` flag the caller sets. This is a small, mechanical change
   to a script that already exists — not new machinery.
3. Keep one authoring agent per domain (the spec's own rationale for domain-scoped expertise and
   bookkeeping still holds), but for any domain with more than ~5 items, split its slot list into
   sub-batches of 5–6 items and dispatch each sub-batch as its own short-lived agent call, writing its
   own small JSON file the moment it finishes — not one file at the very end for the whole domain. A
   stall now costs at most one sub-batch, not an entire domain.
4. Keep the existing repair/verification pass for the *shipped* fields (`whyRight`/`whyWrong`/`t1Alt`)
   — that work is not what is expensive; it is what `deepDive`'s dedicated grounding audit duplicates.

**Review path (only after Ram actually sits the paper — folds into the Phase 9 process that already
exists):**

5. For every item Ram missed — typically a minority of 63, not all of them — dispatch a small,
   targeted authoring pass that reads only the cited section(s) for those specific items and writes
   `principle`/`rightDeep`/`wrongDeep`, patched into the already-shipped HTML. Follow with one
   independent grounding-audit pass sized to that same small set, not to all 63.
6. Optionally expose a manual "explain this one more deeply" trigger for any item Ram got right but
   wants explained further — same small, one-item dispatch, on demand.

**What this gives up, stated plainly:**

- A freshly generated paper no longer arrives with full principle-level explanations for all 63 items
  on day one. Ram gets them for what he actually missed, after he sits the paper, not up front for
  everything.
- The two-pass grounding audit no longer clears a full 63-item `deepDive` layer before a paper ships —
  it clears whatever smaller set gets generated per scoring cycle. Strictly less total verification
  work happens up front, in exchange for verification effort landing only where it gets used.
- More moving parts in Phase 9 (a new miss-driven generation codepath) and in assembly (patching
  `deepDive` into an already-shipped file rather than writing it once at generation time) — a one-time
  build cost, not a recurring per-paper one.
- None of this touches item validity, scoring, or whether a paper is fair to sit. `deepDive` does not
  affect the 13-check gate's pass/fail meaning and does not render at all in Exam Mode (Papers 8 and
  10, per §5.6) — cutting it from the blocking path costs study depth on correctly-answered items, not
  exam fidelity.

---

## 4. Recommendation

**Do not mass-redispatch the same seven full-domain agents a third time**, and do not spend the next
session's time trying to root-cause the exact "stream watchdog" mechanism before acting — the fix below
is warranted regardless of what that root cause turns out to be, and it is cheap to test directly.

**Before generating anything else, make both of these changes, then retry Paper 2:**

1. **Demote `deepDive` from a mandatory, blocking, generation-time requirement to a deferred,
   miss-driven Phase 9 enhancement**, per §3 above. This is a spec change to
   `CCAR-P-Orchestration-Prompt_v2.md` §5.5/§5.6, so record it explicitly as a decision (this project's
   own promotion-gate convention in `GENERATION-INTELLIGENCE.md` requires exactly that for anything
   touching the spec) — but the recommendation itself is not equivocal: cut it from the blocking path.
   It is the single most expensive, least evidence-backed addition in the system, and the project's own
   audit already proved it overreaches the corpus in 44% of Paper 1's items.
2. **Split each domain's authoring dispatch into sub-batches of 5–6 items with immediate per-batch
   persistence**, instead of one long turn per domain writing one file at the end. Keep the domain-level
   parallelism the spec calls for; shrink what happens inside each individual dispatch.
3. **Retry Paper 2 generation under this shape.** Do not recompute the central plan
   (`_PAPER2-STAGING/p2-slots.md` is already correct and cross-checked) — only the authoring-dispatch
   shape and the `deepDive` timing need to change.

Together, these two changes cut the per-item generation burden from ~500–700 words of doubly-audited
prose to roughly 150–250 words of singly-audited prose, and cut the largest single dispatch from a
12-item, all-or-nothing mega-turn down to batches solidly inside the size that already worked today
(D7: 4 items, full old-style content, ~191K tokens, no failure). If Paper 2 still stalls at that size,
the problem is confirmed as infrastructure rather than task design, and that is a different, narrower
investigation — but there is no evidence yet that it is needed, and strong evidence that the design
changes above are needed regardless.
