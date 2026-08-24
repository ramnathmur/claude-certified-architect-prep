# CCAR-P Domain Corpus — File Template

Copy this shape for every `CCAR-P_Domain-N_v1.md`. It reproduces the structure of the Foundations
`_v2` files, which is the only structure this project has evidence for: fourteen mock papers were
generated from files in this shape and produced a first-attempt pass.

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

---

## N.2 <next section>
````

---

## Rules for writing sections

1. **One decision per section.** If a section contains two independent decisions, split it. Misses
   are logged by section, and a section covering two things cannot tell you which one failed.
2. **Name the discriminator explicitly.** The Foundations misses were overwhelmingly *wrong-axis*
   errors — applying "severity" where the real axis was "do the issues interact", applying "recurrence
   risk" where the real axis was something else. Sections that state their axis in one line prevent
   this; sections that only describe both options do not.
3. **Write both directions of every decision.** The `tool_choice` trap on Foundations closed in the
   under-specification direction and immediately reopened in the over-specification direction, because
   only one direction had ever been drilled. Every decision table needs a row where the *other* option
   wins.
4. **Misconceptions are quoted, not paraphrased.** Write the wrong belief the way someone would say
   it out loud. "Composite tools are always preferable once a pairing is established" is a usable
   misconception; "confusion about composite tools" is not.
5. **Distractor families.** Vary the ❌ options across recognised families rather than writing three
   flavours of the same wrong answer. The families that actually caught Ram on Foundations:
   - **OVERSPEC** — a stronger guarantee than the requirement asks for
   - **DISCARD** — replace a working mechanism instead of adjusting it narrowly
   - **REPAIR** — fix downstream what a constraint could have prevented upstream
   - **ARCHITECTED** — the option that sounds more professional or more thorough
   - **HALF-MOVE** — a partial version of the right answer
   - **WRONG-AXIS** — right vocabulary, wrong discriminator
6. **Cite nothing external inside the file.** Corpus files are self-contained. Provenance belongs in
   `CCAR-P_Corpus-Index_v1.md`.
7. **Numbering is permanent.** Once `N.4` exists it stays `N.4` forever.

## Professional-tier specifics

Foundations tested whether a design is correct. Professional tests whether it survives production
and can be defended. Sections should therefore carry, where relevant:

- **The cost dimension.** Not just which design works, but which one is affordable at volume.
- **The failure mode.** What breaks first when this design meets real traffic.
- **The stakeholder answer.** How the decision is explained to someone who is not an engineer.
- **The compliance constraint.** What a regulated sector adds to the decision.

A Foundations-shaped section that omits all four is likely pitched a tier too low.
