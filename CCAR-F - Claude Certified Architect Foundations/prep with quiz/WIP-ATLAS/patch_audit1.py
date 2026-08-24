"""Apply the fixes from the three blind cold audits. Each replacement must match exactly once, or the script aborts
without writing anything. Run: python patch_audit1.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

P = []          # (file, old, new, why)
def fix(f, old, new, why): P.append((f, old, new, why))

# ---------------------------------------------------------------- audit 1: D1/D2
fix("items_d1a.py",
    "Gap evaluation belongs to the coordinator: re-delegate targeted queries, re-invoke synthesis, stop on a coverage criterion. Letting synthesis search for itself is the distractor.",
    "Gap evaluation belongs to the coordinator: re-delegate targeted queries, re-invoke synthesis, stop on a coverage criterion. Handing synthesis the full search tool set is the distractor; one narrowly scoped lookup tool for a frequent simple check is the keyed answer on that question, as D2-08 sets out.",
    "D1-10: absolute rule would eliminate sample Q9's correct answer (scoped verify_fact)")

fix("items_d1b.py",
    "Distractors add instructions and few-shot examples to the tool description, permit `dry_run=false` only when a matching `dry_run=true` call happened inside a time window, or move the confirmation into the orchestration layer.",
    "Distractors add instructions and few-shot examples to the tool description, or permit `dry_run=false` only when a matching `dry_run=true` call happened inside a time window. This card is about binding the preview into the tool contract; enforcing a required order between two tools is a prerequisite gate, which is the guide's own answer on that question (D1-16).",
    "D1-19: listing the orchestration-layer option as a distractor read as contradicting D1-16 and sample Q1")

fix("items_d2a.py",
    "One tool, several jobs → split it, one purpose per tool with its own input and output contract. Consolidating into a single general-purpose tool is the distractor.",
    "One tool, several jobs → split it, one purpose per tool with its own input and output contract. Consolidating is a valid design in its own right, but it is not the fix for a tool whose description cannot state one purpose.",
    "D2-03: guide calls consolidation 'a valid architectural choice'; card generalised it into a rule")

fix("items_d2a.py",
    r'A search subagent times out and the question asks how that failure should reach the coordinator. The answer returns structured error context: the failure type, the attempted query, any partial results and possible alternatives, so the coordinator can retry with a modified query, take another route, or continue with what it has. Distractors return a generic \"search unavailable\" after internal retries, mark the failure as an empty successful result, or terminate the whole workflow.',
    r'A tool returns the same \"Operation failed\" for a timeout, a malformed argument and a policy refusal, and the agent retries all three; the question asks what the tool should return instead. The answer carries `isError` with an `errorCategory`, an `isRetryable` boolean and a readable description, so the agent retries only what is retryable and explains the rest. The distractor keeps one uniform failure string and moves the decision into the prompt. Retrying a transient failure inside the tool is correct and is not the fault here.',
    "D2-05: 'tested' described sample Q8 (D5-13's territory) and implied internal retries are an anti-pattern")

fix("items_d2a.py",
    "A librarian facing eighteen near-identical doors along one corridor reads eighteen signs before every request, and the near-misses multiply. A reference desk with four or five rooms behind it lands on the right one more often, because fewer rooms could plausibly be the answer.",
    "A librarian facing eighteen doors along one corridor weighs eighteen possibilities before every request, however clearly each one is signed. A reference desk with four or five rooms behind it lands on the right one more often, because fewer rooms could plausibly be the answer.",
    "D2-07: analogy blamed similarity; the guide's mechanism is decision complexity from count")

# ---------------------------------------------------------------- audit 2: D3/D4
fix("items_d3.py",
    "Claude Code loads user-level `~/.claude/CLAUDE.md`, project-level `.claude/CLAUDE.md` or root `CLAUDE.md`, and directory-level subdirectory `CLAUDE.md` files together; the levels stack rather than replace one another.",
    "The `CLAUDE.md` configuration hierarchy has three levels: user-level `~/.claude/CLAUDE.md`, project-level `.claude/CLAUDE.md` or root `CLAUDE.md`, and directory-level `CLAUDE.md` files in subdirectories.",
    "D3-01: 'levels stack rather than replace' is not a guide claim")

fix("items_d3.py",
    "A scenario places an instruction at one level and asks who receives it or which files it governs, or asks where a new instruction should live. Distractors treat one level as overriding another, or name a configuration file that does not exist, such as `.claude/config.json`, as a home for instructions.",
    "A scenario places an instruction at one level and asks who receives it or which files it governs, or asks where a new instruction should live. Distractors put a convention the whole team needs into user-level configuration, or name a configuration file that does not exist, such as `.claude/config.json`, as a home for instructions.",
    "D3-01: removed an elimination rule built on a fact the guide never states")

fix("items_d3.py",
    "The office hands every starter the company handbook, pins floor notices where they apply, and lets each person keep sticky notes on their own monitor. When you sit down to work, all three are in front of you at once; a floor notice does not take the handbook away.",
    "The office hands every starter the company handbook, pins floor notices where they apply, and lets each person keep sticky notes on their own monitor. Which of the three you write in depends on who has to receive the instruction.",
    "D3-01: analogy carried the same unsupported stacking claim")

fix("items_d3.py",
    "`@` directly before a path, no space, inside a `CLAUDE.md`. Per-package selection of standards files is the tell for `@import`.",
    "The guide calls it the `@import` syntax for referencing external files from a `CLAUDE.md`. Per-package selection of standards files is the tell.",
    "D3-03: committed to a literal token form the guide does not spell out")

fix("items_d3.py",
    "A skill is a `SKILL.md` file in its own folder under `.claude/skills/`, and its YAML frontmatter can set `context: fork`, `allowed-tools` and `argument-hint`.",
    "A skill is a `SKILL.md` file under `.claude/skills/`, and its YAML frontmatter can set `context: fork`, `allowed-tools` and `argument-hint`.",
    "D3-07: per-skill folder is not in the guide")

fix("items_d3.py",
    "`.claude/skills/` → folder → `SKILL.md`. Frontmatter keys to know: `context: fork`, `allowed-tools`, `argument-hint`. Skill behaviour is configured in the skill file.",
    "`.claude/skills/` → `SKILL.md`. Frontmatter keys to know: `context: fork`, `allowed-tools`, `argument-hint`. Skill behaviour is configured in the skill file.",
    "D3-07: same")

fix("items_d3.py",
    "`context: fork` in `SKILL.md` frontmatter runs the skill in an isolated sub-agent context, so its output never enters the main conversation.",
    "`context: fork` in `SKILL.md` frontmatter runs the skill in an isolated sub-agent context, which prevents its working from polluting the main conversation; the result still comes back.",
    "D3-08: 'output never enters' contradicted the card's own analogy and overstated the guide")

fix("items_d3.py",
    "A multi-phase task's discovery phase would fill the context window before implementation starts, and the question asks how to preserve the main context. Answer: run discovery in the Explore subagent and take back the summary. The distractor is `/compact` mid-task, which loses precision the implementation phase needs.",
    "A multi-phase task's discovery phase would fill the context window before implementation starts, and the question asks how to preserve the main context. Answer: run discovery in the Explore subagent and take back the summary, which keeps the verbose output out of the main window in the first place. The paired option is `/compact`, which the guide lists for reducing usage once a session has already filled.",
    "D3-16: /compact taught as a distractor; the guide endorses it at TS 5.4-S5")

fix("items_d3.py",
    "Verbose discovery → Explore subagent, summary comes back. `/compact` mid-task is the distractor: it trades away detail the implementation needs.",
    "Verbose discovery → Explore subagent, summary comes back. `/compact` is a guide-listed technique for a session that has already filled, not a wrong answer in itself.",
    "D3-16: same")

fix("items_d3.py",
    "The survey of every floor is done by a runner who comes back with a one-page note, rather than by dragging every drawer's contents onto your desk. Compressing a heaped desk after the fact loses the details you will need.",
    "The survey of every floor is done by a runner who comes back with a one-page note, rather than by dragging every drawer's contents onto your desk. Tidying the desk afterwards is a real option; sending the runner is what keeps it clear.",
    "D3-16: analogy was the delivery mechanism for the /compact error")

fix("items_d3.py",
    "Re-run → previous findings in context, report only new or unaddressed. Test generation → existing tests in context, no duplicates. Blank slate is the distractor.",
    "Re-run → previous findings in context, report only new or unaddressed. Test generation → existing tests in context, no duplicates. Prior review findings travel; the generating session's own reasoning must not (D4-22).",
    "D3-24: no boundary drawn against D4-22's independence rule")

fix("items_d4a.py",
    "The answer adds three or four examples demonstrating the exact format.",
    "The answer adds examples demonstrating the exact format.",
    "D4-04: the guide gives no count for format-demonstration examples")

fix("items_d4a.py",
    "The distractor supplies ten to fifteen examples of clear, unambiguous requests, which never touch the cases that fail.",
    "The distractor supplies ten to fifteen examples of clear, unambiguous requests, which never touch the cases that fail. The same technique reduces false positives in review: examples contrasting acceptable patterns with genuine issues, so judgment generalises instead of matching a fixed list.",
    "4.2-S3 was uncovered: few-shot as a false-positive remedy")

fix("items_d4a.py",
    "Varied layouts → one worked example per layout, showing where the value sits. Examples cut fabrication in extraction; longer instructions do not.",
    "Varied layouts, and informal wordings such as loose measurements → one worked example per case, showing where the value sits. Examples cut fabrication in extraction; longer instructions do not.",
    "4.2-K4's 'informal measurements' cue belongs with few-shot, not normalisation")

fix("items_d4a.py",
    "Source documents write dates, currencies and informal measurements differently, and the extracted values arrive in whatever form the document used even though the schema validates; the question asks what to add.",
    "Source documents write dates and currencies differently, and the extracted values arrive in whatever form the document used even though the schema validates; the question asks what to add.",
    "D4-12: 'informal measurements' is the guide's few-shot illustration, not a normalisation one")

fix("items_d4b.py",
    "Batch is fire-and-forget: one request in, one response out. Work that needs a tool result returned mid-request stays synchronous however patient it is.",
    "One submission, one response per request, and you poll for completion. Work that needs a tool result returned mid-request stays synchronous however patient it is.",
    "D4-18: 'fire-and-forget' conflicts with the guide listing polling for completion")

fix("items_d4b.py",
    "Independence is a property of context, not of effort. Fresh instance, artifact and criteria only, none of the generating conversation.",
    "Independence is a property of context, not of effort. Fresh instance, artifact and criteria only, none of the generating conversation — though earlier review findings may travel, which is a different thing (D3-24).",
    "D4-22: no boundary drawn against D3-24")

fix("items_d4b.py",
    "Confidence is a field on each finding, not a filter in the prompt. High confidence goes straight out; low confidence goes to a person.",
    "Confidence routes a finding; it never suppresses one. Reporting it per finding and sending the doubtful ones to a person is the answer, while instructing the model to report only high-confidence findings is the distractor (D4-01, D4-02).",
    "D4-24: as written, the distractor D4-02 warns against satisfied D4-24's own test")

# ---------------------------------------------------------------- audit 3: D5 + frame
fix("items_d5a.py",
    "Amounts, dates, order numbers and statuses are extracted into a persistent case-facts block",
    "Amounts, percentages, dates, order numbers and statuses are extracted into a persistent case-facts block",
    "5.1-K1 names percentages; the word appeared nowhere in D5")

fix("items_d5a.py",
    "or cost and latency climb as a conversation passes fifty turns, and the question asks the root cause",
    "or the same history is re-sent on every turn and the question asks the root cause",
    "D5-04: fifty-turn figure is not in the guide")

fix("items_d5a.py",
    "Specific recall from months of history → semantic retrieval of the relevant exchanges. Summarisation keeps the gist and loses the sentence being asked about.",
    "Specific recall from months of history → retrieval of the relevant exchanges rather than a summary. The exam-relevant half is that summarisation keeps the gist and loses the sentence being asked about; the guide puts embedding and vector-database implementation details out of scope, so no question will turn on how retrieval is built.",
    "D5-07: recommended a technique the guide's out-of-scope list touches; reconciled with the atlas's own 'will not appear' rule")

fix("items_d5a.py",
    "Proceeding on stated assumptions with an invitation to correct them is the answer; a set of four or more clarifying questions drives people to abandon the interaction, and defaults applied silently leave them puzzled when the output does not match what they meant.",
    "Proceeding on stated assumptions with an invitation to correct them is the answer; a wall of clarifying questions drives people to abandon the interaction, and defaults applied silently leave them puzzled when the output does not match what they meant.",
    "D5-12: the four-question threshold is a behavioural claim absent from the guide")

fix("items_d5a.py",
    "Say what you assumed, do the work, invite correction. Four clarifying questions loses the user; silent defaults produce output they cannot account for.",
    "Say what you assumed, do the work, invite correction. This is an underspecified task request; when a tool returns several possible customers, the guide's answer is to ask for one more identifier instead (D5-11).",
    "D5-12: no boundary against D5-11, whose answer is the guide-supported one")

fix("items_d5a.py",
    "A referral arrives with half the detail filled in. The ward writes down what it has taken the referral to mean, proceeds on that, and asks the referrer to correct it, rather than sending back a questionnaire and waiting.",
    "A request for the usual discharge paperwork does not say which template is meant. The ward notes which one it has assumed, prepares it, and flags the assumption for correction, rather than returning a questionnaire and waiting. Where the doubt is which patient is meant, the wristband is checked instead.",
    "D5-12: analogy taught proceeding without checking, colliding with D5-11's wristband")

fix("items_d5b.py",
    "The answer spawns a subagent per question and takes back a concise summary. The paired distractor runs `/compact` mid-task, which loses precision the implementation phase needs.",
    "The answer spawns a subagent per question and takes back a concise summary, so the verbose output never reaches the main window. The paired option is `/compact`, which the guide lists for reducing usage once a session has already filled.",
    "D5-19: /compact taught as a distractor against the guide")

fix("items_d5b.py",
    "One question per subagent; the summary comes back and the main agent stays at coordination level. `/compact` mid-task is the paired distractor.",
    "One question per subagent; the summary comes back and the main agent stays at coordination level. Isolation prevents the window filling; `/compact` is the guide's remedy once it has.",
    "D5-19: same")

fix("items_d5b.py",
    "Distractors expect the conversation history to survive the crash, or re-run the whole investigation from the start.",
    "Distractors rely on the interrupted run's own context still being available to the new one, or re-run the whole investigation from the start.",
    "D5-21: 'conversation history does not survive a crash' is not a guide claim")

fix("items_d5b.py",
    "Agents write state to a known path; the coordinator reads the manifest on resume and injects it. Conversation history does not survive a crash.",
    "Agents write state to a known path; the coordinator reads the manifest on resume and injects it. Designing recovery around exported state is the point; assuming the dead run's context is still there is the distractor.",
    "D5-21: absolute contradicted D1-23's --resume card")

fix("items_d5b.py",
    "One overall number is evidence about no single segment. Break accuracy down by document type and by field before reducing human review.",
    "An aggregate can mask a bad segment. Break accuracy down by document type and by field before reducing human review.",
    "D5-23: 'evidence about no single segment' overstates the guide's 'may mask'")

fix("items_d5a.py",
    "`/compact` shrinks a session already full of discovery output. Where the choice is still open, isolate discovery in a subagent instead; compaction loses precision.",
    "PLACEHOLDER_NOT_IN_D5A", "unused")

# D5-22 lives in items_d5b.py
P[-1] = ("items_d5b.py",
    "`/compact` shrinks a session already full of discovery output. Where the choice is still open, isolate discovery in a subagent instead; compaction loses precision.",
    "`/compact` shrinks a session already full of discovery output, which is exactly what the guide lists it for. Where the choice is still open, isolating discovery in a subagent keeps the detail out of the main window in the first place.",
    "D5-22: 'compaction loses precision' is not a guide claim")

fix("items_d5b.py",
    "When the question is how to keep that output out of the main window in the first place, the Explore subagent is the answer and `/compact` mid-task is the distractor, because compaction costs precision the implementation phase needs.",
    "When the question is how to keep that output out of the main window in the first place, the Explore subagent is the stronger answer, because it prevents the filling rather than compressing after it.",
    "D5-22: same")

# ---------------------------------------------------------------- key-distinction point + document frame
fix("inventory.py",
    "22: \"Verbose discovery goes to an isolated subagent (Explore) that returns a summary. `/compact` mid-task loses precision.\",",
    "22: \"Verbose discovery goes to an isolated subagent (Explore) that returns a summary, preventing the window from filling. The guide separately lists `/compact` for reducing usage once a session has filled, so it is a listed technique rather than a wrong answer in itself.\",",
    "Traps page #22 repeated the unsupported /compact precision claim")

fix("build_atlas.py",
    "Weights are of scored content; scaled scoring equates forms of slightly different difficulty. No partial credit, no penalty for a wrong answer.",
    "Weights are of scored content; scaled scoring equates forms of slightly different difficulty. The platform requires an answer to every question before you can advance.",
    "exam page asserted a partial-credit/penalty rule the guide does not state")

fix("build_atlas.py",
    "Every sitting shows four of these. Each scenario's questions lean on the domains marked; the exam-wide weights still hold.",
    "Every sitting shows four of these. Each scenario's questions lean on the domains marked; the weights above are of total scored content.",
    "guide says nothing about weights holding across a randomly drawn subset")

fix("build_atlas.py",
    "Distilled from the rationales of the twelve official sample questions. When two options both sound reasonable, these decide.",
    "Distilled from the guide's task statements and the rationales of its twelve sample questions. When two options both sound reasonable, these decide.",
    "three tie-breakers come from task statements, not sample rationales")

fix("build_atlas.py",
    "Every one of those items maps to at least one of the {n_cards} cards below; the mapping is checked by script before this file is built.",
    "Every task statement bullet, technology and in-scope item maps to at least one of the {n_cards} cards below, checked by script before this file is built. The out-of-scope list is reproduced on the exam page rather than carded, because none of it is examinable.",
    "coverage claim was false as written for the out-of-scope items")

# ---------------------------------------------------------------- apply
errs = []
for f, old, new, why in P:
    p = os.path.join(HERE, f)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if n != 1:
        errs.append(f"{f}: {n} matches (want 1) for [{why}] :: {old[:80]}...")
if errs:
    print("ABORTED — nothing written:")
    for e in errs: print("  -", e)
    sys.exit(1)

by_file = {}
for f, old, new, why in P:
    by_file.setdefault(f, []).append((old, new, why))
for f, subs in by_file.items():
    p = os.path.join(HERE, f)
    s = open(p, encoding="utf-8").read()
    for old, new, why in subs:
        s = s.replace(old, new, 1)
    open(p, "w", encoding="utf-8").write(s)
    print(f"{f}: {len(subs)} fixes")
print(f"\ntotal {len(P)} fixes applied")
