"""Second pass over Exam 18 stems.

Two gate findings:
  - check 1 flagged 'Reviews', 'Complex' and 'Late' as possible coined names. They are
    ordinary words capitalised by sentence position that happen never to appear in lower
    case elsewhere on the paper. Rephrased so the detector has nothing to catch.
  - check 3 requires a stem median of 50-55 words, calibrated against the real exam's
    style profile. The drafted median was 46, so the sixteen shortest stems are extended
    with concrete situational detail -- metrics, log output, config specifics -- which is
    the register PRACTICE-TEST-STEMS_v1.md SS3 documents. No stem's question changes.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

NEW_STEMS = {
 3: "An engineer adds `.claude/rules/schema.md` and reports that running `/memory` afterwards 'did not activate it'. The rule's conventions are still not being applied when they edit a schema file, and they ask whether the command needs a flag to force a reload. What should they be told?",

 6: "An engineer wants a `/scaffold` command available to the team. They create `.claude/skills/scaffold.md` in the repository, commit it, and pull on a second machine. The command appears in neither place, and `/memory` lists no skill by that name. The file's contents are correct and its frontmatter parses. What is wrong?",

 8: "A prompt classifies each pull request as a refactor, a feature or a fix, and the label drives which review checklist runs. It carries six examples covering the clear cases. Those are handled well; changes that add a feature while restructuring the code around it are labelled inconsistently, sometimes one way and sometimes the other on near-identical diffs. What would most improve it?",

 9: "A long refactoring conversation is approaching the context limit. An engineer proposes dropping the oldest third of the turns from every subsequent request to make room, arguing that the recent turns carry the current state anyway. Those early turns are where the module boundary and the deprecation list were agreed. What is wrong with this, and what should be done instead?",

 11: "Yesterday a session analysed a 50-file module and produced a working understanding of its call graph and its test coverage. Overnight three of those files were refactored; the other 47 are untouched. The engineer wants to carry on this morning from where they left off rather than rebuild that understanding. What is the correct approach?",

 12: "A generation step returns a structured change plan through a tool call, and every field in its schema is currently marked required. Reviewers find `rollback_step` and `owning_team` populated with confident-looking values on plans where the request mentioned neither, and the values are plausible enough that two of them were acted on. Select TWO changes that reduce this.",

 20: "A specialist is being defined to audit dependency licences against the team's approved list. It needs to read manifests and search the repository, must not modify anything, and will be spawned by the coordinator once per release. The approved list and the manifest locations are both known to the coordinator. Select TWO configuration choices that follow the corpus.",

 22: "To cut latency, an engineer proposes letting the test-analysis specialist send its findings straight to the code-generation specialist, skipping the coordinator hop and saving roughly four seconds per exchange. Both already run under the same coordinator, and the payload is a short structured summary. What is the objection?",

 26: "A `delete_branch` tool is occasionally called on branches that still carry unmerged commits — three times last month, twice recoverable from the reflog. The team wants deletion to be impossible unless the agent has first seen exactly what would be removed, and wants that guarantee to hold without depending on the model remembering to check. Which tool design achieves it?",

 27: "The team wants Claude to recall architectural decisions made in sessions weeks earlier — why a queue was chosen over polling, which retry library was rejected and on what grounds, and which of two caching strategies was ruled out. Sessions are started fresh each morning and the decisions are currently only in old transcripts. Select TWO approaches that work.",

 33: "The team must migrate the pipeline off a deprecated test runner. The replacement is chosen and its basic invocation is documented, but the configuration mapping is unclear in three places, two custom reporters may have no equivalent at all, and roughly 40 spec files will need changing. How should Claude Code be used for this work?",

 34: "The nightly job runs four analyses across the repository. On one run the dependency-graph analysis fails on a malformed lockfile, after the complexity, coverage and dead-code analyses have all completed and produced their sections. The orchestrator's current handler aborts the run and writes nothing at all. What should it do instead?",

 35: "An engineer wants to move three Claude workloads to the Message Batches API to cut cost: an interactive query tool a developer waits on, a pre-merge check that blocks the pipeline, and a monthly architecture report nobody reads until the following week. Select TWO properties of that API that constrain which of them can move.",

 38: "A generation step writes database migration scripts and a review step checks them against the schema before they are applied. Both currently run as consecutive turns in one session. Across roughly ninety migrations the review has never rejected a script, and two migrations that reached production had to be rolled back. What change makes the review meaningful?",

 42: "The same prompt against the same commit gives different verdicts on different runs — one run flags a naming violation the next ignores, and the pipeline's pass/fail parse sometimes fails outright because the summary wording changed. The team wants the CI review reproducible. Select TWO changes that address this.",

 44: "Each CI review is currently invoked with `--resume` against a long-lived session, so the reviewer 'remembers the repository'. The reviews have begun citing helper functions that were deleted a fortnight ago and referring to a directory layout that changed in the same window. What should the pipeline do?",

 57: "The claim form gives a date of loss of 12 March and the adjuster's narrative gives 14 March. Both documents are part of the same pack, both are legitimate sources, and the policy's waiting period makes the two dates lead to different settlement outcomes. Select TWO things the extraction output should do.",

 55: "The harder claims are handled in a multi-turn session with a reviewer, and history is summarised every few turns to control length. Towards the end of these sessions the agent begins restating the policy number with a transposed digit and rounding the excess to the nearest ten pounds. What should be done?",
}

BLOCK_OF = {g: (0 if g <= 15 else 1 if g <= 30 else 2 if g <= 45 else 3) for g in NEW_STEMS}

def words(s):
    return len(re.sub(r"<[^>]+>", "", s).split())

changed = 0
for n in range(1, 5):
    path = os.path.join(HERE, f"block{n}.json")
    d = json.load(open(path, encoding="utf-8"))
    for q in d["questions"]:
        if q["g"] in NEW_STEMS:
            before = words(q["stem"])
            q["stem"] = NEW_STEMS[q["g"]]
            after = words(q["stem"])
            print(f"  Q{q['g']}: {before} -> {after} words")
            changed += 1
    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print(f"stems rewritten: {changed}")
