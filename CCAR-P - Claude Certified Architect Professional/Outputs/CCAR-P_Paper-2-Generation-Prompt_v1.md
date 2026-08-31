# CCAR-P Paper 2 — Generation Prompt (v1)

**Written 2026-08-30.** Paste the block below into a new Claude Code session opened in this repo.
Intended for **Sonnet**, so it is prescriptive rather than exploratory: explicit steps, explicit
files, explicit stop conditions.

Regenerate this prompt if Paper 2 slips past Paper 3, or if the orchestration prompt changes again.

---

```
Generate CCAR-P Mock Test Paper 2.

## 0 — Before anything else

Work inside your own git worktree, on your own branch. Use paths RELATIVE to your worktree root.
Never write to an absolute path outside it: a previous background task was handed absolute paths into
the main checkout, edited a tree it did not own, and could not commit its own work.

Read these four files, in this order, before you plan anything:

1. `CLAUDE.md` (repo root)
2. `CCAR-P - Claude Certified Architect Professional/CLAUDE.md`
3. `CCAR-P - Claude Certified Architect Professional/prep with quiz/CCAR-P-Orchestration-Prompt_v2.md`
   — this is THE AUTHORITY for how a paper is generated. Everything below is a summary of it plus
   what changed after Paper 1. Where this prompt and that file disagree, that file wins and you
   should say so.
4. `CCAR-P - Claude Certified Architect Professional/EXAM-FACTS_v1.md`

All paths below are relative to `CCAR-P - Claude Certified Architect Professional/prep with quiz/`.

**The one rule that outranks everything else:** the seven `CCAR-P_Domain-N_v1.md` corpus files are the
ONLY permitted source for any item, option, rationale, or explanation. Never generate from memory,
from the web, or from a community guide. Never generate from `EXAM-FACTS_v1.md`'s UNVERIFIED table.

## 1 — Preflight. Abort and report if any of these fails.

1. `EXAM-FACTS_v1.md` shows no unresolved rows for domain list, weightings, or item count.
2. All seven `CCAR-P_Domain-N_v1.md` files exist.
3. `FACET-LEDGER.md`, `STEM-LEDGER.md`, `ARCHETYPE-LEDGER.md`, `CCAR-P_Objective-Map_v1.md` exist.
4. `mock-exams/CCAR-P_MockTest-2_v1.html` does NOT already exist, and `DASHBOARD-DATA.jsonl` has no
   line with `"paper_n": 2`.

### 1a — The targeting question. Resolve this before planning, and record which branch you took.

Check `EXAM-LOG.md` for a `## Paper 1 — SCORED <date>` heading.

- **If Paper 1 HAS been scored:** read its miss table and the Professor's Note written after it.
  Apply Phase 7.1 in full — every targeting triple gets at least one item from the OPPOSITE facet or
  direction, satisfied inside the fixed domain quota, and at least 3 previously-missed triples are
  left deliberately untargeted and named. Gate check 13 applies normally.

- **If Paper 1 has NOT been scored** (as of 2026-08-30 it had not): there is no Professor's Note and
  none should be invented. `EXAM-LOG.md` states that Paper 2's note is written after Paper 1 is
  scored, per Phase 9. Generate Paper 2 as an **explicitly untargeted second diagnostic**, record
  that decision in the generation entry, and mark gate check 13 `N/A — no Professor's Note exists`.
  Do NOT fabricate targeting triples. Before you start, tell the user this is what you are doing and
  ask them to confirm they want Paper 2 now rather than after sitting Paper 1.

## 2 — What changed after Paper 1. Read this or your paper will fail the gate.

**a. `deepDive` is now a required field on every item.** Orchestration prompt §5.5 and §5.6. This is
the largest change and it roughly doubles the authoring work per item.

```
deepDive: {
  principle: "...",                      // 45-75 words
  rightDeep: "...",                      // 60-100 words
  wrongDeep: { A:"...", B:"...", D:"..." }  // 45-80 words each
}
```

- `wrongDeep` holds exactly one entry per NON-correct option letter — the same key set as `whyWrong`.
  No entry for a correct letter, none missing for a wrong one.
- `principle` states the governing rule the item is an instance of, drawn from the cited section's
  Core Facts discriminator and its decision table's framing sentence. Not "why C wins here".
- `rightDeep` ties the key to the SPECIFIC decision-table row that fires — quote or closely
  paraphrase that row's Situation, Answer and Why text, then say what in the stem makes it fire.
- Each `wrongDeep` gives the real mechanism: the decision-table row that option WOULD be correct for,
  or the section's own documented Misconception it embodies. Never "this is the trap."
- Read each item's own cited corpus section IN FULL before writing that item's `deepDive`. Never from
  memory of what a section "probably" says.
- Plain text only. No markdown, no HTML, no newlines inside a string, no second person, no invented
  company/product/persona names.

`validateItems()` enforces presence and the key set. A paper missing `deepDive` fails gate check 1.

**b. Resolve `t1Alt` to a named corpus row AT AUTHORING TIME.** `GENERATION-INTELLIGENCE.md` F-12:
13 of Paper 1's 63 items record a `t1Alt` that resolves to no corpus row anywhere in the domain file.
Gate check 12 passed all 13, because it only checks the field is populated. For each item, name the
decision-table row where the `t1Alt` option is the corpus answer once `t1Clause` is deleted or
inverted. If no such row exists, pick a different `t1Clause`/`t1Alt` pair. Do not ship an item whose
counterfactual you cannot point at a row for.

**c. The grounding audit is a SEPARATE agent from the author.** F-13. An author asked to check its
own grounding finds its own paraphrase sufficient. Across Paper 1's deep-dive pass, two independent
grounding agents raised 67 findings; 54 were real. The recurring failure was mis-paraphrase, not
invention — a row quoted with a load-bearing precondition silently dropped.

**d. AUTHOR mode is the only mode.** Phase 2 was corrected 2026-08-30. TRANSCRIBE was rejected
outright: 84% of the corpus's 79 ready-made scenarios have the correct answer as the longest option
against ~33% chance. Do not reintroduce it.

**e. The accuracy pill and the deep-dive renderer are already in the template.** You inherit them by
copying the template. Nothing to build.

## 3 — Plan the paper. Compute ALL of this centrally BEFORE writing any option text.

- **Domain quota, exactly:** D1 11 · D2 8 · D3 12 · D4 10 · D5 9 · D6 9 · D7 4 = 63.
  No confirmed-weakness adjustment is possible — that needs two scored papers by attempt date.
- **Objective coverage:** floor pass gives all 38 objectives one item; 25 discretionary items follow;
  cap 3 items per objective.
- **Format split:** 55 single-answer + 8 multiple-response, `selectN: 2` on all eight. Every
  multi-response stem must state its count in the stem text ("Select two."). Draw a multi-response
  item only from a section whose decision table holds at least 2 independently-true rows for the same
  situation. Across the eight, no correct pair appears more than twice.
- **Correct-answer letters, pre-planned before drafting:** the multiset {A×14, B×14, C×14, D×13},
  shuffled into a random per-item order. **Paper 2's short letter is C** — so C×13 and A/B/D×14.
  (Rotation: P1 short D, P2 short C, P3 short B, P4 short A.) Decide each item's correct letter here;
  drafting writes the correct option into that position.
- **Facets:** read `FACET-LEDGER.md` for what Paper 1 consumed. No facet twice on one paper. No facet
  reused until every facet in its section has been used once. A section contributes at most 2 items.
  When a section's facets are exhausted, use its misconception unit `M-<section>` before reusing.
- **Shapes:** Papers 1-3 build recognition. Same 8 shapes from `ARCHETYPE-LEDGER.md`, each appearing
  6-9 times, with entirely different content. Within-paper dedup is on `(section, facet)`, NOT shape.
- **Distractor families,** across the paper's 181 distractors: 3 different families per item; no
  family above 47; EVIDENCE-MISMATCH at least 15; DETECTIVE-FOR-PREVENTIVE at least 9; ARCHITECTED at
  most 19.
- **Style caps, binding:** stem at most 45 words (band 28-40); option at most 20 words; within-item
  option spread at most 8 words; third person, no "you"; ZERO invented company/product/persona names;
  inline code/config tokens in at most 15% of options and never in a D1, D5 or D6 option.

Every item must pass T1-T4 (orchestration prompt §5.3). T1 is load-bearing: name one stem clause
whose deletion or inversion makes a DIFFERENT option correct, and record it as `t1Clause`/`t1Alt` —
subject to §2b above.

## 4 — Build the file

Copy `mock-exams/CCAR-P_MockTest-TEMPLATE_v1.html` to `mock-exams/CCAR-P_MockTest-2_v1.html`.
Change exactly three things, then replace the `ITEMS` array with your 63 items:

- `const PAPER_N   = 2;`
- `const KEY       = "ccarp-mocktest-2-v1";`
- `const EXAM_MODE = false;`   (stays false — only Papers 8 and 10 are Exam Mode)

Update the file's top-of-file HTML comment and the `ITEMS` schema-comment header so neither describes
the template's demo content. Change nothing else in the engine.

## 5 — Fidelity gate. The paper may not ship until this is clean.

```
node tools/run-gate.js mock-exams/CCAR-P_MockTest-2_v1.html 63
```

Requires **0 errors**. Then work through all 13 checks in Phase 6 and report each with its computed
value, its threshold, and any fix applied. Re-run checks 2, 3, 6 and 10 after ANY fix that swaps or
reorders an item — a swapped item carries its own domain, letter and family.

Check 3 is the one that has failed before elsewhere: verify every item's `domain` tag against the
domain of every section cited in its `whyRight`, its `whyWrong`, and its `deepDive`. Run it per item.

## 6 — Close out (Phase 8)

1. Append the Paper 2 generation entry to `EXAM-LOG.md`: mode, which Professor's Note and Insights
   Round were consumed (or that none existed), the quota used, facets targeted with direction,
   sections deliberately left untargeted, and the full 13-row gate table with computed values.
2. Append one line to `DASHBOARD-DATA.jsonl` with null scores, matching `DASHBOARD-SCHEMA.md`.
3. **Rebuild** `STEM-LEDGER.md`, `FACET-LEDGER.md` and `ARCHETYPE-LEDGER.md` from the SHIPPED HTML
   file — never from your own account of what you wrote. Two seed records were lost that way once.
4. Append a Session 4 entry to `GENERATION-INTELLIGENCE.md` with any findings, using the promotion
   gate at the top of that file. Note in particular whether F-12 recurred: how many of your 63 items
   needed a `t1Clause`/`t1Alt` pair changed because the first choice resolved to no row.

## 7 — Cost, and a decision that is yours

`GENERATION-INTELLIGENCE.md` F-11 measured Paper 1's real generation cost at ~7.7-8M tokens, before
`deepDive` existed. Adding a corpus-grounded deep dive to all 63 items will add materially to that.
Pending decision 3 in that file lists cost-optimisation options — collapsing the 4-stage pipeline,
explicit effort tiers, a retry cooldown, resume-duplicate-dispatch prevention — and records that they
are the Paper 2 session's call. Decide deliberately, state what you chose, and report actual cost.

Practical shape that worked for Paper 1: one authoring agent per domain, each given ONLY its own
corpus file and its own items; then a separate grounding agent per domain that reads only the corpus
and the output. Do not let an authoring agent grade itself.

## 8 — Stop and ask, do not guess

Stop and ask the user if: any preflight condition fails · Paper 1 turns out to be scored and its
Professor's Note conflicts with an Insights Round · the corpus cannot supply a facet a quota needs ·
the gate cannot be brought to 0 errors without changing an item's `correct[]` · you would need to
edit any `CCAR-P_Domain-N_v1.md` corpus file (that needs Ram's explicit decision).

Report honestly. Quote real command output rather than reconstructing it. If a check did not run,
say so. Do not report the paper as generated until the gate is clean and the ledgers are rebuilt.
```
