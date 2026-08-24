# CCAO-F Domain Corpus — File Template

Copy this shape for every `CCAO-F_Domain-N_v1.md`. It reproduces the structure of the CCAR-F `_v2`
files, which is the only structure this project has evidence for: fourteen mock papers were generated
from files in this shape and produced a first-attempt pass at 851.

**The rule it enforces:** a domain file states decisions, not explanations. Every section must be
answerable as "given this situation, do X, not Y." A section that only explains a concept cannot
generate a question, and cannot catch a misconception.

---

## Template

````markdown
# Domain N — <Official domain name from the exam guide>

**Weight:** X% (source: official exam guide vN, dated YYYY-MM-DD)
**Objectives covered:** <the published objectives this file serves>

## N.1 <Section title>

### Core Facts

| Attribute | Value |
|---|---|
| ... | ... |

### <Decision axis> — <Option A> vs <Option B>

State the discriminator in one line, before the table. The discriminator is the thing the exam
actually tests; the table is only there to apply it.

| Situation | Answer | Why |
|---|---|---|
| ... | ... | ... |

### Exam scenario: <one-line situation>
- ✅ <the correct action, stated as an action>
- ❌ <the tempting wrong option> — <why it is tempting, then why it is wrong>
- ❌ <a second wrong option, from a different distractor family>

### ❌ Misconception
"<the wrong belief, written as someone would actually hold it>" — <the correction, one sentence>
````

---

## Rules for writing sections

1. **One decision per section.** If a section contains two independent decisions, split it. Misses are
   logged by section, and a section covering two things cannot tell you which one failed.
2. **Name the discriminator explicitly.** The CCAR-F misses were overwhelmingly *wrong-axis* errors —
   applying "severity" where the real axis was "do the issues interact". Sections that state their
   axis in one line prevent this; sections that only describe both options do not.
3. **Write both directions of every decision.** On CCAR-F the `tool_choice` trap closed in the
   under-specification direction and immediately reopened in the over-specification direction, because
   only one direction had ever been drilled. Every decision table needs a row where the *other* option
   wins.
4. **Misconceptions are quoted, not paraphrased.** Write the wrong belief the way someone would say it
   out loud. "Projects share knowledge across the whole team by default" is a usable misconception;
   "confusion about project sharing" is not.
5. **Distractor families.** Vary the ❌ options across recognised families rather than writing three
   flavours of the same wrong answer. The families that actually caught Ram on CCAR-F:
   - **OVERSPEC** — a stronger guarantee than the requirement asks for
   - **DISCARD** — replace a working mechanism instead of adjusting it narrowly
   - **REPAIR** — fix downstream what a constraint could have prevented upstream
   - **ARCHITECTED** — the option that sounds more professional or more thorough
   - **HALF-MOVE** — a partial version of the right answer
   - **WRONG-AXIS** — right vocabulary, wrong discriminator
6. **Cite nothing external inside the file.** Corpus files are self-contained. Provenance belongs in
   `CCAO-F_Corpus-Index_v1.md`.
7. **Numbering is permanent.** Once `N.4` exists it stays `N.4` forever.

---

## Associate-tier specifics — what makes this different from the CCAR-F files

CCAR-F tested whether a design is correct. CCAO-F tests whether a working professional can **operate
Claude well and know where the edges are**. Sections should therefore carry, where relevant:

- **The plan tier.** Which plans have this — Free, Pro, Max, Team, Enterprise. Associate items turn on
  availability far more often than architect items do.
- **The limit.** Caps, quotas, retention, context behaviour, what happens when you exceed it.
- **The admin boundary.** What a user can change versus what an org admin controls.
- **The everyday situation.** The stem should be a real desk problem — a report to check, a team
  workflow to set up, a document to summarise — not a system to architect.

A section that reads like it belongs in the CCAR-F corpus is pitched a tier too high and will train
the wrong instinct.

### The ARCHITECTED family is the dangerous one here

Ram holds CCAR-F. On this exam the more-architected-sounding option is a distractor more often than it
is the answer. Deliberately over-supply the ARCHITECTED family in distractors, and tag every miss
against it as `ALTITUDE` in the exam log so the pattern is visible if it forms.
