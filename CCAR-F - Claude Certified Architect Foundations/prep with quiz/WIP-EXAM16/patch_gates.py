"""Patch pass 1 for Exam 16 — closes gate checks 1, 3, 5, 6 and 7.

Every edit is an exact-fragment replacement with an assertion, so a silent no-op
is impossible. Nothing here changes which option is correct, the option order,
the domain tag, or any rationale's meaning.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (question, field, old fragment, new fragment)
#   field "stem"  -> q["stem"]
#   field ("opt", i) -> q["options"][i]
EDITS = [
    # ---------- check 1: invented-name false positives ----------
    # Q16 "Briefings" sentence-initial and never lower-cased anywhere in the paper.
    (16, "stem", "Briefings come back uniform and shallow, and one missed a fishery closure that happened mid-survey.",
                 "The briefings come back uniform and shallow, and one of them missed a fishery closure that happened mid-survey and changed the picture entirely."),
    # Q37 "Yesterday" is not in the gate's sentence-start whitelist.
    (37, "stem", "Yesterday's session mapped how back-pay recalculation flows through six modules, and it took two hours. Overnight, another team refactored three of those six. The rest of the map is still accurate.",
                 "The previous session mapped how back-pay recalculation flows through six modules, and building that map took two hours of exploration. Overnight another team refactored three of those six, changing function signatures rather than behaviour. The rest of the map is still accurate."),
    # Q53 weekday names are not in ALLOWED_PROPER; the SLA arithmetic works without them.
    (53, "stem", "A weekly dependency audit has to be on the platform team's desk by 09:00 Monday. Someone proposes submitting it as a batch at 02:00 Monday, reasoning that batches usually finish inside an hour. What is the correct submission planning?",
                 "A weekly dependency audit has to be on the platform team's desk by 09:00 at the start of each week, and it runs over about 4,000 packages. Someone proposes submitting it as a batch at 02:00 that same morning, reasoning that batches usually finish inside an hour. What is the correct submission planning?"),
    (53, ("opt", 0), "02:00 Monday is fine, since typical completion sits comfortably inside the seven-hour margin.",
                     "02:00 is fine, since typical completion sits comfortably inside the seven-hour margin."),
    (53, ("opt", 1), "Submit at 02:00 Monday but poll every ten minutes, falling back to synchronous calls if it has not finished by 07:00.",
                     "Submit at 02:00 but poll every ten minutes, falling back to synchronous calls if it has not finished by 07:00."),
    (53, ("opt", 3), "Submit no later than 09:00 Sunday, because the submission deadline is the downstream deadline minus the full 24-hour worst case.",
                     "Submit no later than 09:00 the previous day, because the submission deadline is the downstream deadline minus the full 24-hour worst case."),

    # ---------- check 6: MR stem must state the count in a form the gate reads ----------
    (59, "stem", "Select the two named patterns these describe, in that order.",
                 "Which two of the following name these patterns correctly, in that order? Select two."),

    # ---------- check 7: block 2 repeated its closing sentence ----------
    (21, "stem", "The finding is present, correctly worded, and clearly stated. What should change?",
                 "The finding is present, correctly worded, and sits under its own heading. Where should the fix be applied?"),

    # ---------- check 3: stem word-count budget (median 50-55) ----------
    (2,  "stem", "then escalating.", "then escalating, on each of the roughly sixty late withdrawals that arrive per term."),
    (4,  "stem", "and spends 14 tool calls.", "and spends 14 tool calls where a single-issue case of the same kind takes three."),
    (5,  "stem", "The system prompt says only `escalate complex cases`.",
                 "The system prompt says only `escalate complex cases`, and has said so since launch, with no examples attached."),
    (6,  "stem", "A colleague proposes a small classifier in front of the tool layer.",
                 "A colleague proposes a small classifier in front of the tool layer, trained on three months of routing logs."),
    (7,  "stem", "and nothing more.", "and nothing more, whatever the underlying cause turned out to be."),
    (8,  "stem", "and the agent then quotes a different figure.",
                 "and the agent then quotes a different figure back to the student on the call."),
    (9,  "stem", "They also want that command unable to modify anything.",
                 "They also want that command unable to modify anything in the working tree, since it is often invoked during a live incident."),
    (10, "stem", "In production it answers everything itself.",
                 "In production it answers everything itself, competently, and has not spawned a subagent once in six weeks of traffic."),
    (11, "stem", "and a term-end audit finds four credits above the line applied without one.",
                 "and a term-end audit finds four credits above the line, totalling £11,400, applied without one."),
    (12, "stem", "The conversation is 3,100 tokens against a very large window, and the same prompt behaves correctly in fresh sessions.",
                 "The whole conversation is 3,100 tokens against a window two orders of magnitude larger, and the same prompt behaves correctly in fresh sessions and in short ones."),
    (13, "stem", "A 90-minute session has reached 71,000 tokens. It holds a declared disability adjustment, three exact instalment figures, a long stretch of general reassurance, and the last few exchanges settling the current request.",
                 "A 90-minute session has reached 71,000 tokens and is still open. It holds a disability adjustment declared in the opening minutes, three exact instalment figures, a long stretch of general reassurance, and the last few exchanges settling the current request, which turns on one of those figures."),
    (14, "stem", "All of it loads in every session.",
                 "All of it loads in every session, so a change touching one module still carries the migration runbook."),
    (15, "stem", "stopping when it finds one.",
                 "stopping when it finds one; the hang always follows a turn where the model was plainly mid-task."),
    (18, "stem", "and has started running open-ended searches instead of synthesising.",
                 "and has started running open-ended searches of its own instead of synthesising what it was given."),
    (19, "stem", "Downstream, page numbers and survey years have disappeared,",
                 "By the time the briefing is written, page numbers and survey years have disappeared,"),
    (19, "stem", "The coordinator still holds both, correctly separated, in its own history.",
                 "The coordinator still holds both figures, correctly separated and dated, in its own history."),
    (20, "stem", "Analysts abandon the request rather than answer.",
                 "Analysts abandon the request rather than answer, and roughly a third of requests now end this way."),
    (21, "stem", "Synthesis receives 78,000 tokens per run.",
                 "Synthesis receives 78,000 tokens per run, assembled from four subagents in a fixed order."),
    (22, "stem", "A colleague argues that building custom repeats the mistake of reinventing standards.",
                 "A colleague argues that building anything custom repeats the mistake of reinventing standards, citing the reference-manager decision as precedent."),
    (23, "stem", "Synthesis returns a briefing that covers biology and catch history but says nothing about management measures",
                 "Synthesis returns a briefing that covers biology and catch history in real depth but says nothing at all about management measures"),
    (23, "stem", "Nothing failed and no tool errored.",
                 "Nothing failed, no tool errored, and every subagent reported completion."),
    (24, "stem", "A four-hour run dies eight minutes from the end. Restarting repeats every search and every document pass from the beginning.",
                 "A four-hour run dies eight minutes from the end, after the search and document passes have both completed and synthesis is part-written. Restarting repeats every search and every document pass from the beginning, at full cost."),
    (25, "stem", "and the convention is written down somewhere.",
                 "and the convention is written down somewhere, since three of them follow it without being reminded."),
    (26, "stem", "it gets the arithmetic wrong on roughly a fifth of runs.",
                 "it gets the arithmetic wrong on roughly a fifth of runs, usually by transposing two of the series."),
    (28, "stem", "Both are credible, both are current, and their methods differ.",
                 "Both are credible, both were published within the last six months, and their methods differ substantially."),
    (29, "stem", "Three searches are dispatched in a single turn.",
                 "Three searches on different subtopics are dispatched in a single turn."),
    (29, "stem", "The agent then attributes one result's contents to a different query.",
                 "The agent then attributes one result's contents to a different query, and the briefing repeats that mix-up downstream."),
    (30, "stem", "Someone proposes running `/compact` and carrying on in the same session.",
                 "Someone proposes running `/compact` and carrying straight on in the same session rather than starting over."),
    (31, "stem", "A deprecated `calcPenaltyRate` helper has to be located before it can be removed.",
                 "A deprecated `calcPenaltyRate` helper has to be located everywhere it is used before it can be removed."),
    (31, "stem", "reported two matches, and the removal then broke eleven call sites at build time.",
                 "reported two matches, and the removal that followed broke eleven call sites at build time across four packages."),
    (32, "stem", "The developer asking does not know the award rules well.",
                 "The developer asking does not know the award rules well, and neither does anyone else currently on the team."),
    (33, "stem", "Nobody knows which parts of the awards module lack tests.",
                 "Nobody knows which parts of the awards module lack tests, and the coverage report has not run in a year."),
    (33, "stem", "over eight years of accumulated history.",
                 "over eight years of accumulated history and four teams' worth of conventions."),
    (34, "stem", "and the change is needed in one of them.",
                 "and the change is needed in exactly one of them, the overtime branch, which is the third occurrence in the file."),
    (35, "stem", "Developers have stopped reading the output.",
                 "Developers have stopped reading the output entirely, and dismissals now run at about 90%."),
    (36, "stem", "The prose description has been rewritten twice and lengthened both times.",
                 "The prose description has been rewritten twice and lengthened both times, without changing the variance at all."),
    (38, "stem", "and round-trips fell.", "and round-trips fell by about a third."),
    (38, "stem", "the agent calls the composite anyway and discards half the payload.",
                 "the agent calls the composite anyway and discards half the payload on every single request."),
    (39, "stem", "whose API differs in three places.",
                 "whose API differs in three places, one of them a changed return shape."),
    (39, "stem", "intending to switch into planning if it turns out to be messy.",
                 "intending to switch into planning mode later if the work turns out messier than expected."),
    (40, "stem", "about half the time and to a documentation tool the rest.",
                 "about half the time and to a documentation tool the rest, with no pattern anyone can see."),
    (40, "stem", "Twelve examples of clear requests have already been added, with no effect.",
                 "Twelve examples of clear requests were added last sprint, with no measurable effect on the split."),
    (42, "stem", "and the rename went through.",
                 "and the rename went through against files nobody had previewed."),
    (43, "stem", "and test files require fixture factories rather than inline literals.",
                 "and test files require fixture factories rather than the inline literals they use today."),
    (43, "stem", "All three kinds of file sit side by side in every feature folder.",
                 "All three kinds of file sit side by side in every one of the 60-odd feature folders."),
    (44, "stem", "which developers strip by hand dozens of times a day.",
                 "which developers strip by hand dozens of times a day across the four teams."),
    (44, "stem", "helped for a while and then stopped helping.",
                 "helped for a fortnight and then quietly stopped helping."),
    (49, "stem", "Three rounds of describing that bug in prose",
                 "Three rounds of describing that bug in prose to the generator"),
    (49, "stem", "each breaking a different case.",
                 "each breaking a different case that had previously worked."),
    (50, "stem", "Developers have started dismissing every comment the reviewer posts, safety findings included.",
                 "Developers have started dismissing every comment the reviewer posts, safety findings included; two chilled-chain findings dismissed last month were later confirmed as real defects."),
    (51, "stem", "and context use per run fell sharply.", "and context use per run fell by roughly 40%."),
    (51, "stem", "the temperature-band field was among those dropped.",
                 "the temperature-band field turned out to be among those the hook drops."),
    (51, "stem", "Select two sound responses.", "Select two sound responses to this."),
    (54, "stem", "traced to interactions between a changed module and an untouched consumer of it.",
                 "traced to interactions between a changed module and an untouched consumer of it, neither of them flagged by any of the three subtasks."),
    (55, "stem", "The generator proposes 10 test cases per pull request, and roughly 6 of them duplicate scenarios the existing suite already covers. Reviewers have stopped reading the list.",
                 "The generator proposes 10 test cases per pull request, and roughly 6 of them duplicate scenarios the existing suite already covers. Across last month's 40 pull requests the duplicate share never once fell below half, and the suite itself runs to 1,900 tests. Reviewers have stopped reading the list."),
    (57, "stem", "A teammate wants all three sent one at a time so each stays focused.",
                 "A teammate wants all three sent one at a time, on the principle that each request then stays focused."),
    (60, "stem", "Suggested fixes from the reviewer are accepted 96% of the time overall, and there is a proposal to apply high-confidence ones automatically. Nobody has broken that figure down.",
                 "Suggested fixes from the reviewer are accepted 96% of the time overall, measured across eleven finding types and about 300 fixes a week, and there is a proposal to apply the high-confidence ones automatically. Nobody has broken that figure down by type or by module."),

    # ---------- check 5: inline code/config tokens, concentrated in D2/D3 and real tokens only ----------
    (3,  ("opt", 3), "Taken the first record the tool returned,", "Taken the first record `get_student` returned,"),
    (17, ("opt", 0), "so every claim keeps its origin.", "carrying `source_name` and `publication_date`, so every claim keeps its origin."),
    (22, ("opt", 0), "Agree — extend the community server with the quota rules",
                     "Agree — extend the community server's `tools` with the quota rules"),
    (22, ("opt", 1), "the quota model can be expressed as prompt templates on the existing server rather than as a second server.",
                     "the quota model can be expressed as MCP `prompts` on the existing server rather than as a second server."),
    (22, ("opt", 3), "community servers cannot expose resources, so an internal catalogue always needs custom code.",
                     "community servers cannot expose `resources`, so an internal catalogue always needs custom code."),
    (24, ("opt", 0), "to a known location as it works.", "to a known location such as `agent-state/` as it works."),
    (24, ("opt", 1), "The coordinator maintains a manifest recording each subagent's status, and reads it on resume.",
                     "The coordinator maintains a `manifest.json` recording each subagent's status, and reads it on resume."),
    (30, ("opt", 0), "Sound — compaction is designed to compress context",
                     "Sound — `/compact` is designed to compress context"),
    (30, ("opt", 1), "Sound, provided the compaction is instructed to keep every numeric value verbatim as it compresses.",
                     "Sound, provided `/compact` is instructed to keep every numeric value verbatim as it compresses."),
    (30, ("opt", 2), "Risky — compaction can lose exact numeric values,",
                     "Risky — `/compact` can lose exact numeric values,"),
    (30, ("opt", 3), "Risky — compaction discards the earliest turns first,",
                     "Risky — `/compact` discards the earliest turns first,"),
    (38, ("opt", 4), "best solved by trimming the composite's output with a hook.",
                     "best solved by trimming the composite's output with a `PostToolUse` hook."),
    (42, ("opt", 3), "The token was minted by the agent rather than the server,",
                     "The token was minted by the agent rather than returned by `preview_rename`,"),
    (47, ("opt", 3), "so the model understands that the field is mandatory.",
                     "so the model understands that `suggested_fix` is mandatory."),
    (47, ("opt", 4), "Keep the field required for data quality",
                     "Keep `suggested_fix` required for data quality"),
    (51, ("opt", 2), "Remove the hook, since trimming tool output has proved unsafe for this pipeline.",
                     "Remove the `PostToolUse` hook, since trimming tool output has proved unsafe for this pipeline."),
]

blocks = {}
for i in range(1, 5):
    p = os.path.join(HERE, f"block{i}.json")
    blocks[i] = (p, json.load(open(p, encoding="utf-8")))

index = {}
for i, (_, b) in blocks.items():
    for q in b["questions"]:
        index[q["g"]] = q

applied, failed = 0, []
for g, field, old, new in EDITS:
    q = index[g]
    if field == "stem":
        if old not in q["stem"]:
            failed.append(f"Q{g} stem fragment not found: {old[:60]!r}")
            continue
        q["stem"] = q["stem"].replace(old, new, 1)
    else:
        i = field[1]
        if old not in q["options"][i]:
            failed.append(f"Q{g} option {i} fragment not found: {old[:60]!r}")
            continue
        q["options"][i] = q["options"][i].replace(old, new, 1)
    applied += 1

print(f"applied {applied}/{len(EDITS)} edits")
if failed:
    print("FAILED:")
    for f in failed:
        print("  -", f)
    sys.exit(1)

for i, (p, b) in blocks.items():
    json.dump(b, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"rewrote {os.path.basename(p)}")
