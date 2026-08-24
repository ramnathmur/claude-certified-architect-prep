"""Second stem pass for Exam 19.

Six stems still sat at or above the 0.40 reskin threshold after the first pass, and all
six tested the same corpus point as an Exam 17 or Exam 18 item. Reframing the situation
was not enough, because the question itself was the same question. Four of the six now
test a DIFFERENT corpus section in the same domain, and two are re-shaped so the reader
is doing different work:

  Q23  D4  kept SS4.6 (the ladder needs its `auto` rung) but re-shaped from "an existing
           setting is wrong, correct it" to "choose the setting for a new step", which is
           a different reasoning task from Exam 17 Q48.
  Q30  D2  kept SS2.9 and INVERTED it: the case where read-plus-write genuinely is the
           right call because the anchor cannot be disambiguated. Opposite key to
           Exam 18 Q13, so it doubles as a slogan-breaker.
  Q38  D1  SS1.17 independent review -> SS1.2 hub-and-spoke routing.
  Q54  D4  SS4.4 prefilling -> SS4.11 batch `custom_id` join discipline.
  Q58  D4  SS4.10 self-correction -> SS4.5 format normalisation in the schema.
  Q60  D3  SS3.3 rules-vs-skill -> SS3.4 custom slash commands and `$ARGUMENTS`.

Also clears check 1: 'Ofcom' named a real regulator, which the corpus's generic-framing
rule bars as surely as an invented company would, and 'Specialists' was an ordinary word
capitalised by position that appears nowhere else in lower case.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

REPLACE = {
 5: {"stem": "A regulatory rule requires a contract's cooling-off status to be checked before any plan change is applied, with no exceptions. That instruction sits in the system prompt, and a quarterly audit of 1,200 conversations found 27 plan changes applied with no check recorded against them. Select TWO changes that make the requirement deterministic."},

 10: {"stem": "The retention desk receives handoffs as a single line reading `escalate: early-termination fee disputed`. Nobody on that desk can see the conversation, so each one opens by asking for the account number, the amount and what was already offered. Post-handoff handling time averages fourteen minutes against a six-minute target. What should the payload carry?"},

 23: {
  "domain": "D4",
  "stem": "A new triage step is being specified. It reads an incoming request and either points the engineer at existing documentation, which needs no tool, or opens a repository search to locate the relevant module. Both outcomes are legitimate and the split runs about even. Which `tool_choice` setting should the step be built with?",
  "options": [
   "`{\"type\": \"auto\"}`, which lets the model call the search when the request needs it and answer directly when it does not.",
   "`{\"type\": \"any\"}`, so every request produces a tool call and the step's output shape stays uniform.",
   "`{\"type\": \"tool\", \"name\": \"search_repo\"}`, so the step always has search results to reason from.",
   "`{\"type\": \"any\"}` plus a no-op `answer_from_docs` tool for the requests that need no search."
  ],
  "correct": 0,
  "whyRight": {
   "text": "Nothing about this step makes a tool call mandatory — half its work is answering from documentation the model already has. `auto` is the rung that matches: the model decides per request whether a search is warranted. The stronger settings exist for when structured output or a tool call is required, and imposing one here buys uniformity by making half the requests do pointless work.",
   "cite": "CCA-Prep_Domain-4_v2.md §4.6"
  },
  "whyWrong": [
   {"option": 1, "text": "Uniform output shape is not the requirement, and `any` would fire a search for every documentation pointer. It applies a guarantee to a step that has nothing mandatory to guarantee.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.6"},
   {"option": 2, "text": "Forcing the search tool makes every request a repository search, including the half that resolve to a documentation link. It is the strongest rung applied where no rung is needed.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.6"},
   {"option": 3, "text": "A no-op tool re-implements `auto` through a tool the model must remember to choose, adding a definition, a code path and a new failure mode to recover behaviour the parameter already provides.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.6"}
  ]
 },

 30: {
  "domain": "D2",
  "stem": "A generated file declares the same four-line configuration block at the top of each of its six sections, byte for byte, and the third one must change. Widening the anchor pulls in more of the identical block and still matches six times; a replace-all would change all six. What is the correct next step?",
  "options": [
   "Read the file and write it back with the third block changed, since neither widening nor replace-all can isolate one of six identical occurrences.",
   "Widen the anchor further, since a large enough surrounding window always resolves to one occurrence.",
   "Apply replace-all and then revert the five blocks that should not have changed.",
   "Regenerate the file from its template with the third block already correct."
  ],
  "correct": 0,
  "whyRight": {
   "text": "Widening the anchor and replace-all are the documented recoveries and both are exhausted here: the surrounding context is identical in all six places, so no window disambiguates, and only one of the six should change. This is the case the corpus reserves read-plus-write for — the last-resort fallback, used when the cheaper recoveries genuinely cannot pin the target rather than at the first sign of difficulty.",
   "cite": "CCA-Prep_Domain-2_v2.md §2.9"
  },
  "whyWrong": [
   {"option": 1, "text": "The blocks are byte-for-byte identical, so a larger window contains more identical text and matches the same six places. Widening works when the surroundings differ, and here they do not.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.9"},
   {"option": 2, "text": "This makes five unwanted changes and then relies on a second pass to undo them, leaving the file briefly wrong and the reverts themselves subject to the same matching problem.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.9"},
   {"option": 3, "text": "Regenerating replaces the whole file to change four lines and assumes the template can express the difference between the third section and the other five, which is the same disambiguation problem moved upstream.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.9"}
  ]
 },

 38: {
  "domain": "D1",
  "stem": "The pipeline orchestrator spawns one subagent per check. An engineer proposes letting the coverage subagent send its per-file numbers straight to the correctness subagent, which could then weight its findings, rather than both reporting up and the orchestrator passing the numbers down. What is the objection?",
  "options": [
   "The coverage numbers would arrive without the orchestrator's formatting, so the correctness subagent could not parse them.",
   "Both subagents would need each other's tool definitions, widening two tool sets past the reliable range.",
   "A direct channel removes the orchestrator's visibility of what passed between them, its consistent handling of a failure in either, and its control over what each receives.",
   "There is no objection, provided the orchestrator is copied on whatever the two subagents exchange."
  ],
  "correct": 2,
  "whyRight": {
   "text": "Hub-and-spoke routes every exchange through the coordinator, and the reasons are structural rather than stylistic: the coordinator is where failures are handled uniformly, where the flow of information is controlled, and where the run can be observed. A direct channel removes all three, and the corpus rejects it regardless of the efficiency gained.",
   "cite": "CCA-Prep_Domain-1_v2.md §1.2"
  },
  "whyWrong": [
   {"option": 0, "text": "Formatting is solvable and is not what the constraint protects. Framing the rule as a serialisation detail invites someone to agree a payload shape and proceed.",
    "cite": "CCA-Prep_Domain-1_v2.md §1.2"},
   {"option": 1, "text": "Passing a result does not require holding the other agent's tools. This objects on a mechanism that is not implicated and would evaporate if both tool sets happened to be small.",
    "cite": "CCA-Prep_Domain-1_v2.md §1.2"},
   {"option": 3, "text": "Copying the orchestrator restores a log and not control. It still cannot intervene, cannot handle a failure in the exchange, and cannot decide what the receiving subagent should have been given.",
    "cite": "CCA-Prep_Domain-1_v2.md §1.2"}
  ]
 },

 54: {
  "domain": "D4",
  "stem": "An overnight run submits 3,000 extraction requests as a batch. When the results arrive, 41 have failed and the team cannot tell which applications they belong to, because the reassembly step matches results to inputs by their position in the returned array. What discipline was missed?",
  "options": [
   "Each request should carry a caller-supplied identifier that comes back with its result, so reassembly joins on that rather than on ordering.",
   "The batch should be submitted in smaller groups, so a failure affects a narrower range of positions.",
   "The failed requests should be re-submitted as a whole second batch, since identifying individual failures is not possible.",
   "The run should move to the synchronous API, where each response is returned against the request that produced it."
  ],
  "correct": 0,
  "whyRight": {
   "text": "Batch results are joined to their inputs by a caller-supplied identifier carried on each request and returned with each result. Relying on array position assumes an ordering the API does not promise, which is why 41 failures became 41 unattributable failures. With the identifier in place, selective re-submission of just the failed subset also becomes possible.",
   "cite": "CCA-Prep_Domain-4_v2.md §4.11"
  },
  "whyWrong": [
   {"option": 1, "text": "Smaller groups narrow the range of positions to search by hand and leave the join still resting on ordering. It reduces the size of the problem rather than removing it.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.11"},
   {"option": 2, "text": "Re-submitting everything pays for 3,000 extractions to recover 41, and without an identifier the second batch's results are just as unattributable as the first.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.11"},
   {"option": 3, "text": "Abandoning batch for an overnight run that is entirely latency-tolerant gives up the reason it was chosen, to work around a join discipline the batch API already supports.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.11"}
  ]
 },

 58: {
  "domain": "D4",
  "stem": "Award dates reach the assessment system in four shapes — `2026-04-01`, `01/04/2026`, `1 Apr 2026` and `April 2026` — depending on which document the extractor read. Downstream comparison logic handles the first and mis-orders the rest. Where should the normalisation happen?",
  "options": [
   "In the extraction schema, by typing the field as an ISO date so the model emits one shape at the point it fills the field in.",
   "In the comparison logic, by parsing all four shapes before ordering them.",
   "In the prompt, by instructing the model to prefer ISO dates wherever the source allows.",
   "In a post-extraction pass that rewrites whatever shape arrived into ISO before the record is stored."
  ],
  "correct": 0,
  "whyRight": {
   "text": "The schema is where the field's format is declared, and it is what the model reads while it is filling the field in. Typing the field as an ISO date makes one shape the only well-formed answer, so the four variants never enter the record. Every other option accepts the variation and then repairs it somewhere downstream.",
   "cite": "CCA-Prep_Domain-4_v2.md §4.5"
  },
  "whyWrong": [
   {"option": 1, "text": "Teaching the comparison logic four formats leaves the record holding four, so every other consumer has to learn them too. It fixes one reader rather than the data.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.5"},
   {"option": 2, "text": "A prompt preference is a probabilistic control where the schema offers a declarative one, and 'wherever the source allows' hands the judgement back to the model on every field.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.5"},
   {"option": 3, "text": "A rewriting pass is closer — the record ends up consistent — but it repairs after the fact what the schema prevents outright, and it has to correctly guess whether `01/04/2026` is April or January.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.5"}
  ]
 },

 60: {
  "domain": "D3",
  "stem": "The team wants `/reprocess` to take an application reference and re-run the pipeline for it, so an assessor can type `/reprocess GR-2026-0481`. The command file currently hard-codes one reference for testing. How is the reference passed in?",
  "options": [
   "Through the `$ARGUMENTS` variable in the command file, which is substituted with whatever follows the command name.",
   "Through a `paths` entry in the command's frontmatter, which binds the command to the referenced application.",
   "Through an environment variable the assessor sets before invoking the command.",
   "Commands cannot take parameters; a skill with an input schema is required for this."
  ],
  "correct": 0,
  "whyRight": {
   "text": "`$ARGUMENTS` is the substitution point in a custom command file: whatever the user types after the command name is placed there when the command runs. That is exactly the shape this needs — one reference, supplied at invocation, with no per-application file and nothing to set beforehand.",
   "cite": "CCA-Prep_Domain-3_v2.md §3.4"
  },
  "whyWrong": [
   {"option": 1, "text": "`paths` scopes when something applies by matching file paths. It has no relationship to a value typed at invocation and cannot carry an application reference.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.3"},
   {"option": 2, "text": "An environment variable puts the parameter outside the invocation, so the assessor sets a value and then runs a command that looks parameterless. The substitution mechanism exists precisely to avoid that.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.4"},
   {"option": 3, "text": "Custom commands do take arguments. Reaching for a skill here adds structure to work around a facility the command file already has.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.4"}
  ]
 },
}

for n in range(1, 5):
    path = os.path.join(HERE, f"block{n}.json")
    d = json.load(open(path, encoding="utf-8"))
    for i, q in enumerate(d["questions"]):
        if q["g"] in REPLACE:
            r = REPLACE[q["g"]]
            if "options" in r:                    # full replacement
                keep = {"g": q["g"], "block": q["block"]}
                d["questions"][i] = {**keep, **r}
                print(f"  Q{q['g']}: replaced ({r['domain']}, {r['whyRight']['cite']})")
            else:                                  # stem-only edit
                q["stem"] = r["stem"]
                print(f"  Q{q['g']}: stem edited")
    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("pass 2 applied")
