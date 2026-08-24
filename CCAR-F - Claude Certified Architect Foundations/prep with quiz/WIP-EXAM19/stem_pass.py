"""Stem rewrite pass for Exam 19.

Why: the archetype gate found 27 stems at or above the 0.40 reskin threshold against
Exams 17 and 18. The dedup_check.py run before it compared only against the 886-stem
ledger built from EXAM-LOG Exams 2-16 plus the community stems, so the two papers
generated in the same session were invisible to it. The gate is the backstop that
caught it; the ledger is rebuilt from all 18 papers afterwards.

The collisions are real rather than an artefact of tokenisation. Exam 19 re-tests the
Exam 17 misses on the Professor's Note's instruction and reuses three of Exam 17's four
scenarios, so it inherited both the corpus vocabulary and the scenario nouns. Each stem
below keeps its question and its corpus point and moves the situation onto different
concrete ground: different subsystems, different symptoms, different numbers.

Options and rationales are untouched -- the gate scores stems only, and the reasoning
each question tests is unchanged.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

NEW = {
 5: "Ofcom rules require a contract's cooling-off status to be checked before any plan change is applied, with no exceptions. That instruction sits in the system prompt, and a quarterly audit of 1,200 conversations found 27 plan changes applied with no check recorded against them. Select TWO changes that make the requirement deterministic.",

 10: "The retention desk receives handoffs as a single line reading `escalate: early-termination fee disputed`. Specialists cannot see the conversation, so they open by asking for the account number, the amount and what was already offered. Post-handoff handling time averages fourteen minutes against a six-minute target. What should the payload carry?",

 17: "Two constraints are agreed in the opening minutes of a long session: one adapter keeps its public signature, and a particular date library is off limits. Around turn eighteen a change lands that alters the signature and imports the banned library. Neither constraint was removed from the conversation and the context limit is nowhere near. What is the effective mitigation?",

 19: "A `/release-notes` command should reach the whole team on clone. Its author has it working; three colleagues who pulled the same branch see no such command, and `/memory` on their machines lists nothing by that name. The file sits at `~/.claude/commands/release-notes.md` and its frontmatter parses cleanly. What is the fix?",

 20: "Two and a half hours into a session that has traced the booking flow across roughly sixty files, answers are getting vaguer and one referred to a helper renamed an hour earlier. The engineer has another two hours of work planned on the same area. Select TWO steps that fit.",

 21: "An expensive trace of the booking flow has just finished. The team now wants to weigh two idempotency designs — a request-key table against a natural-key upsert — and needs each judged on its merits rather than against whichever was examined first. Both should begin from the completed trace. What mechanism fits?",

 23: "An assistant answers questions about the scheduling service. Some turns draw on the conversation — 'what did we decide about the upsert?' — and some need a repository search. It runs with `tool_choice` set to `{\"type\": \"any\"}`, and engineers report a search is now fired before answering questions that needed no lookup at all. What is the correct setting?",

 25: "A design conversation is approaching the context limit. An engineer proposes trimming the oldest quarter of turns from each subsequent request, on the reasoning that recent turns already carry the current state. The trimmed range contains the agreed idempotency strategy and the list of endpoints excluded from it. What is wrong, and what should replace it?",

 26: "'Trace every path that writes a booking' is handed to a subagent. A colleague objects that one investigation cannot be parallelised, so the delegation buys nothing. What is the stronger argument for delegating it anyway?",

 28: "Decisions taken weeks ago keep having to be re-argued: why the upsert was chosen, which retry library was rejected, what ruled out the second caching layer. Sessions start fresh each morning and those decisions live only in old transcripts nobody opens. What works?",

 29: "A quality sweep over 35 service modules runs as a single pass. The first several modules come back with specific, located findings and the rest with one or two general remarks. An engineer argues that naming the five required checks explicitly in the prompt removes any need for a multi-pass design. What is the flaw?",

 30: "An agent must raise the timeout on one of five `MAX_ATTEMPTS` declarations in a settings module. Its first edit reports the anchor is not unique. It responds by reading all 1,100 lines of the file and writing the whole file back with that one line changed. What should it have done, and why does the difference matter?",

 35: "Findings come back through a tool call whose schema types every field and forbids properties it does not declare. The pipeline still rejects some payloads downstream. Select TWO defect classes that pass the schema and need separate validation.",

 36: "A validator confirms that each finding's `line` sits inside a changed hunk of the file it names, and about 7% do not. The current retry re-sends the original prompt verbatim, and the second attempt fails at roughly the same rate. What should the retry carry?",

 39: "The reviewer flags pull requests for 'inadequate test coverage'. Two engineers auditing the same week's flags disagreed with the reviewer on about a third of them and with each other on a similar share. The instruction reads: 'Flag anything where testing looks thin.' What is the correct revision?",

 43: "Pull requests touching more than a dozen files come back uneven: the first files get located, specific findings and the last get a line each, and a defect spanning a changed interface and its callers in another file went unreported twice last month. The review runs as one pass over the diff. What architecture fixes this?",

 44: "The reviewer has run the same four checks in the same order for five months. None consumes another's findings. An engineer proposes replacing the sequence with a coordinator that reads the diff and decides which checks are worth running. Should the team adopt it?",

 45: "Promotion always fetches the build manifest, verifies its signature, then records the promotion — in that order, every time. Logs show a promotion recorded with no verification between them, and another where the signature checked was from a manifest fetched two steps earlier. An engineer proposes folding all three into one `promote_build` tool. Is that right?",

 47: "A validation exercise puts field-level accuracy at 96% over 2,500 records, and the team proposes auto-confirming everything above the confidence cut-off. Asked for the number broken down, the exercise shows application forms and declarations in the mid-nineties and budget exports — 7% of volume — at 58%. What does that establish?",

 51: "Applications the pipeline cannot safely complete should go to a human. The current rule sends anything the model reports low confidence on. The queue has filled with routine applications while two packs carrying a declaration format the pipeline has no extractor for went through untouched. What should trigger a handoff instead?",

 52: "A single prompt asks the model to identify each document in the pack, pull the fields belonging to each, check the budget export against the amount requested on the form, and recommend an eligibility outcome. Output quality is poor and no failure can be traced to a particular part of the work. What is the correct restructuring?",

 54: "A summarisation step returns a JSON object the assessment system parses, and roughly one call in ten opens with a sentence introducing the object before the object itself, which the parser rejects. Tool-based structured output is unavailable for this step. What constrains the response most directly?",

 55: "The panel view runs everything together as prose: the institution's supporting narrative, the budget lines with their amounts, and the four eligibility clauses in play. Panel members report they cannot check the arithmetic without transcribing it and keep scrolling back to find clause wording. What should change?",

 56: "The repository's `CLAUDE.md` opens with four paragraphs on the funding programme's history, moves to the record-schema conventions, returns to background on how the panel works, and closes with the rule that every extractor change ships with a fixture. Engineers report the fixture rule is frequently not applied. What is the most likely problem?",

 58: "Extracted records carry a `budget_lines` array and a `total_requested`. Every record parses, and reconciliation shows that on about 5% the total does not match the sum of the lines — a subtotal or a prior-year figure has been picked up from elsewhere on the export. What catches this before assessment?",

 59: "Budget exports of around 40 pages are handled by splitting them into five-page batches, extracting each batch on its own, and concatenating the results. Extraction inside a batch is accurate. Across the whole export, lines that continue over a batch boundary appear twice and the running subtotals no longer reconcile. What is missing?",

 60: "Every file under `extractors/` must declare its document type in a header block and register a fixture, and this has to apply whenever Claude edits one of those 24 files without anyone asking for it. An engineer proposes a skill carrying a `paths` entry. What is the better mechanism, and on what grounds?",
}

# Q39's second option ran to 37 words against the gate's 35-word cap.
OPT_FIX = {
 39: (1, "Instruct the reviewer to reason step by step about each pull request before deciding, so the judgement becomes more deliberate."),
}

def words(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())

changed = 0
for n in range(1, 5):
    path = os.path.join(HERE, f"block{n}.json")
    d = json.load(open(path, encoding="utf-8"))
    for q in d["questions"]:
        if q["g"] in NEW:
            q["stem"] = NEW[q["g"]]
            changed += 1
        if q["g"] in OPT_FIX:
            idx, text = OPT_FIX[q["g"]]
            before = words(q["options"][idx])
            q["options"][idx] = text
            print(f"  Q{q['g']} option {chr(65+idx)}: {before} -> {words(text)} words")
        # block 1 repeated the closing 'What is the correct change?' twice
        if q["g"] == 15:
            q["stem"] = q["stem"].replace("What is the correct change?",
                                          "How should the tool be scoped?")
    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print(f"stems rewritten: {changed}")
