# CCAR-P Deep-Dive Grounding Record — v1

**Built:** 2026-08-30 · **Covers:** the `deepDive` field added to all 63 items of
`prep with quiz/mock-exams/CCAR-P_MockTest-1_v1.html`
**Governed by:** `CCAR-P-Orchestration-Prompt_v2.md` §5.5 and §5.6

This file carries no scores and no exam facts. `EXAM-LOG.md` remains the only source of standing and
`EXAM-FACTS_v1.md` the only source of mechanics. This is a provenance record: what the corpus could
and could not support when the deep explanations were written, kept because the project's rule is
that a claim without a locatable source is not written and the gap is recorded instead.

---

## How the layer was produced

Seven authoring agents, one per corpus domain file, each seeing only its own domain's items and its
own `CCAR-P_Domain-N_v1.md`. Each item's cited section was read in full before that item's text was
written. Then two independent grounding passes, each reading only the corpus and the output — never
the author's reasoning, and never any project document that would bias them toward accepting house
style over facts.

| Pass | Findings | Disposition |
|---|---|---|
| Audit 1 (7 agents) | 33 | all repaired |
| Verification (7 agents, fresh) | 34 | 21 repaired · 13 classified irreducible |

Every finding in both passes was raised against a specific corpus line. The verification pass was
asked to separate two things that look identical in a findings list but need opposite treatment: text
that is wrong where the corpus had a better answer available, and text that is as good as the corpus
permits because the corpus does not carry what the requirement needs.

---

## The 13 irreducible findings — all of one kind

Every one is `T1ALT_MISSING`, and every one is a property of **the item's own recorded `t1Alt`**, not
of the deep-dive text written against it.

§5.5 rule 1 requires the `t1Alt` option's `wrongDeep` entry to name the corpus decision-table row
where that option is the answer once `t1Clause` is deleted or inverted. In these 13 items no such row
exists anywhere in the domain file. Deleting the clause does not surface one, because in most cases
the row that already fires keeps firing without it.

| Item | Cite | t1Alt | The option the item records as becoming correct |
|---|---|---|---|
| g5 | D1 1.11 | A | Score each proposal in a parallel pass and merge the results directly into the award list |
| g12 | D2 2.1 | A | Raise worker concurrency so more records are classified in parallel each night |
| g13 | D2 2.2 | D | State the disclosure format in the system prompt and document the boundary in the on-call runbook |
| g14 | D2 2.3 | C | Rewrite the schema instructions in the system prompt with stricter, more explicit wording |
| g17 | D2 2.4 | C | Lower the sampling temperature so repeated runs of the same quotes return identical orderings |
| g18 | D2 2.6 | B | Move to a model with a larger context window so the agreement fits comfortably |
| g35 | D4 4.10 | C | Benchmark a higher-capability model on the same questions to confirm a reasoning deficit |
| g44 | D5 5.6 | C | Insert deterministic validation checkpoints between the agent's internal steps |
| g54 | D6 6.7 | C | Record the decision, the rejected tier's numbers, the trade-off, and the accuracy edge |
| g55 | D6 6.12 | B | Review the operational error-rate dashboard more frequently |
| g59 | D6 6.8 | A | Revert the configuration change immediately and involve the original team |
| g60 | D7 7.2 | D | Add a hook logging every migration attempt, leaving the skill's permitted tools unchanged |
| g63 | D7 7.1 | B | The batch job is running an older client that ignores CLAUDE.md, so upgrade it |

### How the shipped text handles them

Not by inventing a row. Each of these entries names the row the option's mechanism is closest to,
states what the corpus would additionally need to say for the option to win, and says plainly that
the section carries no such row. Three worked examples, taken from the shipped file:

- **g17 (D2 2.4).** Sampling temperature, determinism and run-to-run variance appear nowhere in
  section 2.4, nor anywhere in Domain 2. The entry says so and otherwise stays on the section's own
  axis, which is whether the task has steps to deliberate through.
- **g35 (D4 4.10).** Section 4.10's only model-related row requires retrieval already verified and
  broad multi-step failure. The entry names that row as the option's home, lists the preconditions it
  would need, and notes that the stem reports the opposite — a production model held constant while
  the index moved underneath it.
- **g44 (D5 5.6).** The corpus *does* hold a row where the option is the answer, the compounding row.
  Reaching it requires substituting a different symptom into the stem, not deleting the recorded
  clause. The entry names the row, states the substitution, and says the clause alone leaves the
  drift row governing.

### What this says about Paper 1

13 of 63 items (21%) carry a `t1Alt` the corpus cannot support. Under Phase 6 check 12 those items
pass — `t1Clause` and `t1Alt` are populated, which is what the check asks. The check does not ask
whether `t1Alt` resolves to a corpus row, and until this pass nothing read it closely enough to
notice. §5.3's own claim that T1 "is cheap to check because the alternative answer is already written
down — it is the row of the same decision table where the other option wins" assumes a resolution
step that was never actually performed.

**Six of the thirteen are D2.** Phase 4 already records D2 as the binding supply constraint — 18
facets against 8 items per paper, with sections 2.6 to 2.9 holding one facet each — and flags roughly
20 more decision-table rows as the fix, due for a decision at the Paper 4 Insights Round. This is
independent corroboration from a different direction: D2 is thin enough that a quarter of its items
cannot state their own counterfactual against it.

This record makes no change to any item. `correct[]`, families, letters, and domain/objective/shape
tagging are untouched, and `t1Clause`/`t1Alt` are left exactly as generated — changing them would
break the miss history they exist to feed.

---

## Partial-support notes carried by 15 items

Separate from the 13 above, 15 items carry an authoring note recording a distractor whose mechanism
the cited section does not cover, where the account was built from what the section does say. These
live in the build-time JSON and are deliberately **not** shipped: the assembly script writes only
`principle`, `rightDeep` and `wrongDeep` into the paper. They are listed here so the gaps are
addressable when the corpus is next extended.

D1 g4 · D1 g5 · D2 g12 · D2 g13 · D2 g14 · D2 g15 · D2 g17 · D2 g18 · D3 g21 · D3 g24 · D3 g29 ·
D3 g31 · D6 g54 · D6 g55 · D6 g59

Six of the fifteen are again D2.

---

## What was verified mechanically, not by reading

Run against the shipped file after assembly:

- All 63 items carry a non-empty `principle` and `rightDeep`, and 181 `wrongDeep` entries whose key
  set is exactly each item's non-correct option letters — no correct letter present, none missing.
- No entry contains an angle bracket, a newline, markdown, a backtick, or second person.
- Word counts inside band on every field: principle 55–75, rightDeep 66–99, wrongDeep 53–80.
- No entry duplicates the quick layer it sits under — highest Jaccard against the item's own
  `whyRight`/`whyWrong` is below 0.55 on all 244 comparisons.
- `whyRight` and `whyWrong` across all 63 items hash identically to their pre-change state
  (sha256 `9565ea2b…a679a5`).
- `node tools/run-gate.js mock-exams/CCAR-P_MockTest-1_v1.html 63` → 0 errors, and its 12 warnings
  are the same 12 stem-length warnings the file carried before this change.
