# Question Archetype Ban-List

**Created:** 2026-08-11 (during Exam 14 generation)
**Applies to:** every FULL-60 and DRILL-30 generated from Exam 14 onward
**Status:** binding. Phase 4.e.6 gains a seventh check — see §4 below.

---

## 0. Why this file exists

A cold audit of all 720 questions across Exams 2–13 (12 unique papers) found that
scenario rotation and block narratives were being varied correctly — same-scenario
narratives sit at 0.12–0.16 mean Jaccard — while the **question archetypes underneath
them were being reskinned**. The same teaching point kept returning in the same
rhetorical shape with only the tool name and the numbers changed.

The existing dedup mechanism did not catch this because it compares **stem wording**.
A reskin that swaps `process_refund` for `merge_duplicate_accounts` changes enough
tokens to pass a 0.30 Jaccard gate while leaving the question cognitively identical.
The learner recognises the shape and answers from memory of the pattern rather than
from the corpus.

Two consequences, both observed in the record:

1. **False mastery.** Exams 7–13 scored 49–55/60. An unknown share of those correct
   answers is template recognition, not knowledge.
2. **A gap that never closed.** D2 §2.8 was missed on Exams 5, 8, 10 and 11 — four
   sittings. The question was substantially the same each time (Exam 10 Q6 vs Exam 11
   Q9 measure 0.717 Jaccard), so a wrong mental model was re-tested rather than
   re-taught.

---

## 1. Banned archetypes (content)

Each entry names the corpus point, the recognisable shape, and every prior instance.
**The corpus point is NOT banned — it is examinable and often important. The SHAPE is
banned.** To test a banned point, use the listed re-frame or invent another.

### BF-1 · Dry-run boolean → token-binding redesign
- **Corpus:** D2 §2.4 (Two-Tool Token-Binding Pattern)
- **Banned shape:** a tool exposes a boolean preview/dry-run/`send_now` flag → logs show
  the agent calls it with the unsafe value on the first attempt → *"Which redesign makes
  skipping the preview architecturally impossible?"*
- **Prior instances (7 exams):** e4 Q2, e5 Q54, e6 Q12, e7 Q7, e10 Q37, e11 Q4, e13 Q6
- **Approved re-frames:** ask what property of the token makes the guarantee hold
  (single-use? server-issued? unguessable?); present a token design that is subtly
  broken and ask why it still permits bypass; contrast it against a `PreToolUse` hook
  (D2 §2.7) and ask which one the situation actually calls for.

### BF-2 · Two habitually-paired tool calls → bundle vs composite
- **Corpus:** D2 §2.8 (Tool Bundling / Composite Tools)
- **Banned shape:** telemetry shows the agent calls tool A, waits a turn, then calls
  tool B with the same identifier on nearly every case → *"two round-trips where one
  would do"* → fix it.
- **Prior instances (4 exams):** e6 Q24, e8 Q11, e10 Q6, e11 Q9 — 0.717 Jaccard at worst
- **Note:** this is the point the learner has missed four times. It must appear in
  Exam 14 in a genuinely unfamiliar frame, not merely a renamed one.
- **Approved re-frames:** start from a team that has *already built* the composite tool
  and is now seeing a second-order cost; ask which of several situations justifies a
  composite over bundling; make the corpus's own preference (prompt-bundling) the
  distractor and a legitimate composite the answer, or vice versa, so the recalled
  slogan does not carry the item.

### BF-3 · Community MCP server vs building your own
- **Corpus:** D2 §2.6 (Community Servers vs Custom Servers)
- **Banned shape:** *"a well-maintained community MCP server already wraps this exact
  registry, but a colleague proposes building a custom one for control"*
- **Prior instances:** e6 Q33, e8 Q28 (0.490)
- **Approved re-frames:** the reverse case — a genuinely team-specific workflow where
  building custom IS correct; a maintenance/ownership question after the community
  server has been adopted.

### BF-4 · Guessed discovery queries → expose an MCP resource catalog
- **Corpus:** D2 §2.6 (MCP Resources as Content Catalogs)
- **Banned shape:** *"the coordinator burns N tool calls per session issuing guessed
  `search_x` queries just to discover which categories exist"*
- **Prior instances:** e4 Q57, e8 Q44 (0.472)
- **Approved re-frames:** contrast a resource against a `list_everything` tool on a
  dimension other than call count (staleness, context cost, invocation reliability);
  ask what a resource cannot do.

### BF-5 · Verbose tool output → PostToolUse trimming
- **Corpus:** D5 §5.5 (Trimming Verbose Tool Outputs)
- **Banned shape:** *"`run_ocr`/`lookup_order` returns 50+/60+ fields per page/call when
  only two matter"* → trim with a hook.
- **Prior instances:** e8 Q25, e10 Q59 (0.585)
- **Approved re-frames:** the trimming hook is already deployed and something else broke
  (a downstream consumer needed a dropped field); ask where trimming should NOT be
  applied; contrast against `/compact` and against summarisation.

### BF-6 · Strict schema shipped, semantic errors remain
- **Corpus:** D4 §4.7 (Syntax vs Semantic Errors)
- **Banned shape:** *"Since the pipeline moved to `tool_use` with a strict schema, every
  record parses cleanly and every field passes its type check. Auditors still find
  values that are wrong."*
- **Prior instances:** e10 Q50, e11 Q48 (0.464)
- **Approved re-frames:** ask which specific validation belongs in code vs schema
  (D4 §4.8); use the self-correction pattern (D4 §4.10) as the subject rather than the
  syntax/semantic distinction itself.

### BF-7 · Three CI workloads → which move to the Batch API
- **Corpus:** D3 §3.10 / D4 §4.11 (Batch vs synchronous)
- **Banned shape:** *"three workloads exist: a pre-merge style check that blocks the PR,
  a nightly test-generation job, and a weekly full-repo security audit"* → which go to
  Batch for the 50% discount?
- **Prior instances:** e2 Q39, e4 Q58 (0.592)
- **Approved re-frames:** SLA arithmetic (D4 §4.11 submission-window subtraction);
  `custom_id` join-key discipline; selective re-submission after partial failure; the
  corrected tool-use-in-batches fact (D4 §4.11 accuracy note), which older material
  gets wrong.

---

## 2. Banned rhetorical furniture (style)

### BF-8 · The "most effective" closing monoculture
Across 720 prior questions, **247 (34.3%)** closed on a "most effective / effectively"
construction, and **81 closed on the byte-identical sentence** *"What is the most
effective fix?"* — spread across every one of the 12 papers.

The official exam does use this register (its own samples read "What change would most
effectively address this reliability issue?"), so it is not banned outright.

**Cap: no closing formula may exceed 20% of a paper, and no two questions in the same
block may close on the identical sentence.** Vary the ask: root cause, which property
holds, what breaks next, what the team should conclude, which two of the following,
what the agent should do at this exact point.

### BF-9 · The "An engineer / The team / The pipeline" opening monoculture
The three most common openings accounted for 61 of 720 stems, and Exams 4–13 opened
almost every stem from the same handful of templates.

**Cap: no opening formula may exceed 15% of a paper.** Open on the artefact, the log
line, the metric, the config, the disagreement between two people, the thing that
changed — not always on the actor.

---

## 3. What is NOT the problem (do not "fix" these)

- **Scenario rotation.** All six official scenarios sat at exactly 8 uses each across
  Exams 2–13. The rotation rule works. Keep it.
- **Block narrative variety.** Same-scenario narratives average 0.12–0.16 Jaccard. They
  are already being rewritten properly.
- **Generic framing.** The absence of named fictional companies from Exam 4 onward is a
  deliberate fidelity fix (Phase 4.e.6 check 1), grounded in an audit of 76 real exam
  texts and confirmed against all 12 official sample questions. **Do not reintroduce
  named companies to solve the freshness problem.** Freshness comes from new industry
  territory described generically — "bills of lading", "phytosanitary certificates",
  "bed-management scheduling" — not from proper nouns.

---

## 4. New Phase 4.e.6 check — ARCHETYPE DEDUP (check 7)

Add to the six existing fidelity checks:

> **7. ARCHETYPE COLLISION.** For every question, name the corpus section it tests and
> the rhetorical shape it uses. Compare against this ban-list AND against the shapes of
> every question already in the paper.
> **THRESHOLD:** 0 questions matching a banned shape; 0 pairs within the paper testing
> the same corpus section through the same shape; no closing formula above 20%; no
> opening formula above 15%.
> **FAIL →** re-frame the question using the section's approved re-frames, or move it to
> a different facet of the same section. Re-run checks 2 and 4 after any swap.

**Mechanised check.** Unlike the by-hand tallies the orchestration prompt assumes, this
check has a script: `tools/archetype_gate.py` computes cross-exam Jaccard for every new
stem against all prior stems, flags anything ≥0.40, and reports closing/opening formula
rates. Run it before shipping. A stem at 0.40+ against any prior question is a reskin
until proven otherwise.

---

## 5. Maintenance

When a new reskin family is found, append it as BF-N with: corpus section, banned shape,
every prior instance with exam and question number, and at least two approved re-frames.
Never delete an entry — a shape that was overused stays overused.
