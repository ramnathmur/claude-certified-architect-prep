# CCAR-P Lesson — Domain 7: Developer Productivity & Operational Enablement

**Weight:** 7% of the paper (official exam guide v1.0, effective July 2026, §6)

**Published objectives, verbatim:**
1. Configure Claude tools and environments for teams (e.g., Claude Code)
2. Improve developer workflows using AI-assisted tooling
3. Support debugging and operational issue resolution

---

## 0. What this domain is actually about, and how much of your attention it deserves

Six of the seven CCAR-P domains ask you to design something. This one asks you to make a design
*land* inside an organisation of engineers who did not attend your design review, will not read your
architecture document, and will each configure their own tooling on the first Monday if you let them.

That is the whole subject: the distance between a system that works when the architect drives it and
a system that works when twenty other people drive it. Everything in the three objectives is a
mechanism for closing that distance — shared configuration closes it for behaviour, workflow design
closes it for process, and operational debugging closes it for the moment things go wrong at 2am and
you are not there.

The domain carries 7%. The exam has 63 items in total. Proportionally that is roughly four or five
items, and you should study it as if it were four or five items: thoroughly, but once. The paper has
no per-domain floor score — pass and fail are decided by the total scaled score alone (guide §9) — so
there is no scenario in which mastering Domain 7 rescues a weak Integration performance. Spend your
marginal hour on Integration, which is 19%.

Two things about the paper's structure are genuinely unknown and worth naming so you do not build a
strategy on either. First, whether the 63 items stand alone or are grouped into shared-scenario
blocks: the guide's item-format line describes multiple-choice and multiple-response items and states
that each item tells you how many responses to select, but it never uses the word "scenario" to
describe a block structure, and it never describes a pool or a draw. Second, whether
multiple-response items award partial credit. The guide says nothing. The Foundations sitting was
all-or-nothing and it cost eight marks, so answer every multiple-response item as if a single missing
selection zeroes it — but do not tell yourself you know that, because you do not.

Where the domain repays study out of proportion to its weight is in the habits it drills. Two
objectives on the real Foundations score report came back at 0%: selecting the Claude Code
configuration mechanism, and choosing between plan mode and direct execution. Both sit inside this
domain. Both are cheap to close. §4 of this lesson is dedicated to them, and it is the section to
re-read if you only re-read one.

A note on register before we start. Everything below that names a specific Claude Code file path,
flag, or frontmatter key is grounded in the Foundations Domain 3 corpus, which was itself built
against the product documentation and the Foundations exam guide. Where that corpus does not support
a specific, this lesson teaches the underlying property instead and says so. Guessing a file name in
a lesson is how a wrong fact enters a corpus and then enters a mock paper.

---

## 1. Objective 7.1 — Configure Claude tools and environments for teams

### 1.1 The problem configuration solves

Start from what a language model actually is at the moment of a request. It is a function from a body
of text to a body of text. It has no memory of yesterday, no awareness of your repository's history,
and no opinion about your team's conventions except the one you put in front of it. Every constraint
you want it to honour has to arrive as tokens in that request.

That single fact produces the entire configuration problem. If an engineer wants Claude to follow the
house convention for error handling, the convention has to be in the request. If they type it into
the chat each morning, it is in the request for that session and gone by Tuesday. If they put it in a
file the tool loads automatically, it is in every request for as long as the file exists. If they put
it in a file on their own machine, it is in every request they make and none that their teammates
make.

Configuration is the mechanism for turning a rule someone knows into a rule that is present in the
request whether or not anyone remembers it. That is the definition worth carrying into the exam,
because it explains every answer in this objective. When you are asked which mechanism to use, you
are being asked: which mechanism puts this content in front of the model, at the right moment, for
the right people, without depending on anyone's memory?

What breaks without it is not dramatic. Nothing crashes. Output quality simply becomes a function of
who ran the tool. Three engineers get code with comprehensive error handling and the fourth gets code
without it, because three of them wrote the convention into their personal configuration years ago
and the fourth joined last week. Nobody notices for a quarter, because nobody is looking at output
variance across engineers — they are looking at pull requests, one at a time, each of which looks
plausible in isolation.

### 1.2 The layers, and what each one is for

Claude Code discovers instruction files at several levels and concatenates them into context, loading
from the root down to the working directory. The Foundations corpus is explicit on this point, and it
is a point people get backwards: this is a **concatenated load order, not an override precedence**.
All discovered files contribute. A directory-level file does not silently replace the project-level
one for that directory. If two files conflict, the model sees both, and the fix is to edit the files
rather than to hope one of them wins.

The levels:

| Level | Path | Reach |
|---|---|---|
| User | `~/.claude/CLAUDE.md` | Every project this one person opens. Not in version control, not shared |
| Project | `<repo>/CLAUDE.md` or `<repo>/.claude/CLAUDE.md` | Everyone who clones the repository |
| Directory | `CLAUDE.md` in any subdirectory | Loaded when working with files in that directory |
| Path-scoped rules | `.claude/rules/*.md` with YAML frontmatter | Loaded only when the files in play match the declared glob patterns |

Alongside the instruction layers sit two invocation layers. Skills live at `.claude/skills/<name>/SKILL.md`
and are invoked on demand rather than loaded into every session. Custom slash commands live at
`.claude/commands/` for the project or `~/.claude/commands/` for one person, and the text typed after
the command name arrives inside the command file as `$ARGUMENTS`. In current Claude Code the two are
unified — `.claude/commands/` is legacy but supported, and both produce a `/name` command.

Skill frontmatter is where the exam likes to live, because it is where a behaviour gets scoped:

| Key | What it does |
|---|---|
| `description` | The text shown in the slash-command menu |
| `argument-hint` | Prompts for the arguments the skill expects |
| `context: fork` | Runs the skill in an isolated subagent context, so its output does not pollute the main conversation |
| `allowed-tools` | Scopes which tools the skill may use |

`allowed-tools` carries a documented double framing worth knowing, because it changes what a
real-world answer should be without changing the exam answer. The Foundations exam guide framed it as
restricting tool access during skill execution. Current product documentation frames it as a list of
tools the skill may use *without prompting the user* — a permission pre-grant, where unlisted tools
follow the normal permission flow rather than being hard-blocked. Both framings agree on the
judgement the exam tests: `allowed-tools` in SKILL.md frontmatter is where you scope what a skill may
do. In production, scope it minimally, because the mechanism is a pre-grant.

Precedence between personal and project skills runs the other way from the instruction files:
a personal skill overrides a project skill **of the same name**. An engineer who wants their own
`/commit` behaviour creates `~/.claude/skills/commit/SKILL.md` — same name, personal override, team
unaffected. Creating `~/.claude/skills/my-commit/` instead produces a second command with an
unfamiliar name and leaves the shared one still firing.

One more mechanism for keeping instruction files navigable: `@import`. A CLAUDE.md can reference
another file with `@path` — the `@` immediately before the path with no space, relative and absolute
paths both supported, and a relative path resolving against the file that contains the import rather
than against the working directory. The maximum nesting depth is contested between the Foundations
study material and the current product documentation, so treat the number as unsafe and never build
an answer on it. The syntax and the resolution rule are stable and are what a sensible question would
test.

### 1.3 What belongs in committed project context, and what does not

The recurring failure on real codebases is not repository size, language, or contributor count.
It is the absence of committed context describing the codebase's conventions and structure. A model
handed a 400,000-line monorepo with a good `CLAUDE.md` produces better work than one handed a
40,000-line service with none, because the constraint that binds is not how much code exists but how
much of the code's *implicit* knowledge is written down anywhere the tool can reach.

So the useful question is which knowledge is implicit. Roughly:

**Belongs in committed project context.** Architectural shape and where things live. Naming and
module conventions that a reader could not infer from any single file. The testing framework, fixture
conventions, and what "done" means for a change. Build and run commands that are not obvious.
Constraints that exist for a reason nobody documented — the library you must not use, the directory
that is generated and must not be hand-edited, the API surface that is public and versioned. Review
criteria, if reviews are automated.

**Does not belong there.** Anything the model can read directly from the code faster than you can
describe it. Anything one engineer prefers and the team has not agreed. Secrets, credentials, and
customer data, for the same reason they do not belong in any other committed file. Workflow
procedures that are only needed occasionally — those become skills, invoked on demand, rather than
tokens paid for in every session.

That last split is a real cost decision, and it is the Professional-tier version of this question.
Project instruction files load in every session. A 500-line file is 500 lines of tokens on every
request every engineer makes, all day. The Foundations corpus records the standard answer to a
CLAUDE.md that has grown to 400 or 500 lines mixing coding standards with PR checklists and deploy
procedures: keep the universal standards in CLAUDE.md, move workflow-specific guidance into skills
with trigger keywords, and move file-type-scoped conventions into `.claude/rules/` where glob
patterns load them only when relevant. Moving *everything* to skills is the wrong end of the same
axis — universal standards would then need explicit invocation every time, which is exactly the
memory dependency configuration exists to remove.

### 1.4 Worked example: the fourth developer

A platform team of four has been using Claude Code for six months. Three engineers consistently get
generated code with comprehensive error handling — try/except around external calls, typed error
returns, structured log lines on the failure path. The fourth engineer, who joined three weeks ago,
consistently does not. All four work in the same repository, on the same branch, with the same
version of the tool. The new engineer's pull requests come back with the same review comment every
time, and they have started manually adding error handling after generation, which is slower than
writing it themselves.

The diagnosis has one likely shape. The three original engineers wrote "always include comprehensive
error handling" into `~/.claude/CLAUDE.md` when they set up the tool. User-level configuration is not
in version control. The new engineer cloned the repository and got everything in it, which does not
include the other three engineers' home directories.

The confirming step is `/memory`, which lists the memory files actually loaded in the current
session. Run it on the new engineer's machine and the project-level file will be there and the
instruction will be visibly absent. Run it on an original engineer's machine and the user-level file
appears with the instruction inside it. That is the diagnosis closed in about ninety seconds, without
a single hypothesis about model versions.

The fix is to move the instruction into the project-level configuration and commit it. Every clone
then carries it, including clones made by people who have not been hired yet.

Now push it to Professional tier, because the exam will. The immediate fix is one line in one file.
The architect's answer includes three more things:

- **The other three engineers' personal copies now duplicate the project rule.** Harmless today.
  Tomorrow the team decides error handling should use a shared decorator instead of inline try/except,
  they update the project file, and three engineers keep generating the old pattern because their
  personal file still says the old thing and both files are concatenated. Personal copies of a rule
  that has been promoted to the project should be deleted, not left as a redundant safety net.
- **Cost.** Every convention added to the always-loaded file is paid for on every request by every
  engineer. Error handling is universal and earns its place. A twelve-step release checklist does not.
- **How you explain it to a delivery manager who asks why the new joiner is slower.** Not "their
  configuration is wrong." Rather: the team's coding standards were living on individual laptops
  instead of in the repository, so a new joiner inherited none of them, and the fix is to move the
  standards into the repository where onboarding already picks them up. That framing gets funded.
  The first one gets a shrug.

### 1.5 How the exam probes this

The scenario shape is consistent enough to recognise on sight. You are given a team, a symptom of
inconsistency, and a set of four plausible-sounding remedies. The correct answer names a specific
configuration location or mechanism. The distractors are almost never absurd; they are usually the
right idea placed at the wrong layer, or the right layer addressed by the wrong mechanism.

Three recurring question stems:

**"Why does this behaviour differ between engineers?"** The answer is nearly always a scope mismatch
between where the instruction lives and who needs it. User-level configuration is the usual culprit
because it is invisible in code review — nobody can see another person's home directory in a pull
request.

**"Where should this rule live?"** Answered by asking two questions in order. Who needs it — one
person or the team? That picks user-level versus project-level. When is it needed — always, on
certain file types, or on demand? That picks CLAUDE.md versus `.claude/rules/` versus a skill.

**"How do we make this available to everyone who clones the repo?"** The word "clones" is doing the
work. Anything in `.claude/` inside the repository travels with a clone. Anything in `~/.claude/`
does not.

A Professional-tier variant adds a constraint that changes the answer: a cost ceiling, a regulated
sector, or a partner team outside your organisation. Watch for those, because they promote a
different mechanism. A rule that must be *auditable* is not the same as a rule that must be
*followed*, and a rule that must be *enforced* is not the same as either.

### 1.6 The wrong turns

**Answering with a document.** A wiki page describing the conventions is tempting because it is
genuinely useful to humans and takes ten minutes. It has no effect on generated output, because the
model never reads it. Any option whose mechanism is "write it down somewhere people can find it" is
answering a different question.

**Answering with a training session.** Same defect, wrapped in more effort. A one-hour session
transfers knowledge to the people in the room on the day, and its half-life is about a fortnight. It
does not reach anyone hired afterwards.

**Answering with a recorded walkthrough.** The most sophisticated version of the same mistake, and
the one that catches careful people, because a recording feels durable in a way a meeting does not.
It is durable and it is also frozen. The moment the configuration changes, the recording is teaching
the old thing with full confidence.

**Adding a subdirectory instruction file to override a project one.** This assumes an override
precedence that the concatenation model does not provide. Both files load. If they conflict, you have
given the model two contradictory instructions and a coin.

**Reaching for the strongest available mechanism.** Enforcement mechanisms that operate outside the
model's discretion are the right answer when a rule must hold every time regardless of what any
prompt says. They are the wrong answer for a style preference, because you have converted a
suggestion into a hard failure and someone now has to get a config change merged to format a file.
The exam calls this OVERSPEC, and it is the family that punishes people who are trying to look
thorough.

### 1.7 Takeaways

- Every constraint you want honoured must arrive in the request. Configuration is the mechanism that
  makes that happen without depending on anyone's memory.
- Instruction files concatenate from root to working directory. All discovered files contribute.
  There is no documented override precedence between CLAUDE.md levels.
- Project-level configuration is version-controlled and reaches everyone who clones. User-level
  configuration reaches one person and is invisible in review.
- Personal skills override project skills of the same name. That is the deliberate escape hatch for
  one engineer's preference.
- Always-needed content goes in the project instruction file, file-scoped content in `.claude/rules/`
  with globs, on-demand procedures in skills. The axis is when it is needed, and the cost is tokens
  per session.
- Committed context describing conventions and structure is what unblocks work on an existing
  codebase. Repository size is not the binding constraint.
- `/memory` lists what is actually loaded. It is the first diagnostic for any "works for them, not
  for me" report.

---

## 2. Objective 7.2 — Improve developer workflows using AI-assisted tooling

### 2.1 What "improving a workflow" means here

The naive model of AI-assisted development is substitution: the engineer used to write the function,
now the model writes the function, and the saving is the time it took to write the function. That
model predicts a modest, bounded gain and it is roughly what teams get when they adopt the tool
without changing anything else.

The gains that justify the spend come from a different place. They come from changing where in the
process work happens. Three examples, each of which the Foundations corpus supports directly:

**Requirements move earlier.** In the interview pattern, instead of generating from an
underspecified brief and iterating on wrong output, you have the model interview you first — ask its
clarifying questions before it implements anything. A caching layer prompts questions about
invalidation strategy, tolerance for stale reads when the cache is unavailable, per-user versus
global scoping, and expected data volume. Those are exactly the questions whose answers you discover
by shipping the wrong thing three times. One interview turn replaces several correction cycles. The
value is not typing speed; it is that a requirements gap surfaces before code exists rather than
after.

**Verification moves earlier.** Write the test suite first — expected behaviour, edge cases,
performance requirements — then iterate by feeding failures back. Tests are a machine-checkable
definition of done. Prose acceptance criteria are not, and prose descriptions of an edge case get
interpreted differently on each pass. A migration script mishandling nulls is fixed fastest by
supplying a sample input row containing nulls and the exact expected output, then iterating until it
passes. Describing the bug more emphatically produces partial fixes and a longer meeting.

**Review moves outward.** A session that generated code is less effective at reviewing that code,
because it carries its own reasoning context and is less likely to challenge the decisions it just
made. The workflow change is to run review in an independent instance rather than asking the author
session to grade itself.

Each of those changes the shape of the process, not just its speed. That is what the objective means
by improving a workflow, and it is what the exam rewards.

### 2.2 The four refinement techniques, and when each one is right

The Foundations corpus names four. They are worth holding as a set because exam scenarios usually
describe a failure that one of them fixes and three of them do not.

**The interview pattern** — for underspecified tasks, unfamiliar domains, and problems with
non-obvious implications. Diagnostic: each generated version misses a *different* requirement. That
pattern means the brief is incomplete, not that the model is weak, and no amount of iterating on
output completes a brief.

**Test-driven iteration** — for tasks with a checkable definition of correctness. Diagnostic: you can
state what right looks like as an assertion. Write it, run it, feed the failure back.

**Concrete input/output examples, two or three of them** — for transformations described in prose and
interpreted inconsistently. Diagnostic: output shape varies run to run while the instruction stays
the same. Examples show the format and the decision logic unambiguously, and the model generalises
the pattern to new inputs rather than parroting the samples. Lengthening the prose description with
more adjectives leaves it ambiguous, only longer.

**Batching feedback correctly** — this one has two directions, and the exam tests the less obvious
one. When issues *interact*, put them in a single detailed message, because fixing them separately
lets the second fix contradict the first. When issues are independent, iterate one at a time so each
change stays easy to verify. A review that found a locking bug, a retry bug whose behaviour depends
on the locking design, and an unrelated typo in a log string should send locking and retry together;
the typo can go either way. The rule "always report one issue per message so it can focus" is a
reasonable-sounding generalisation that is wrong precisely where it matters.

### 2.3 Putting the tool into the pipeline

Interactive use helps individuals. Pipeline use is where a workflow change becomes a team property,
because it happens whether or not anyone chooses it.

For non-interactive execution, `claude -p "<prompt>"` (equivalently `--print`) processes the prompt,
prints to stdout, and exits. Without it, the tool waits for interactive input and the pipeline hangs
until it times out. The Foundations corpus records three specific distractors that do not exist or do
not apply: a `--batch` flag, a `CLAUDE_HEADLESS=true` environment variable, and redirecting stdin
from `/dev/null` — the last being a Unix workaround rather than the documented mechanism.

When the output has to be consumed by another program rather than read by a person, ask for it
structurally: `--output-format json` forces JSON, and `--json-schema` enforces a schema so downstream
parsing is safe. A CI job that posts each finding as an inline pull-request comment needs a file
path, a line number, a severity, and a suggested fix, all reliably present. Adding an "Output Format"
section to the instruction file is not equivalent, and neither is asking for JSON in the prompt.
Both produce output that is usually right, and "usually right" is a parse error in production.

Two pipeline behaviours are worth memorising because they are the difference between a review bot
people trust and one they mute:

**Re-runs must carry prior findings.** When a review re-runs after new commits, feed the previous
run's findings into the prompt and instruct it to report only new or still-unaddressed issues. A
blank-slate re-run re-litigates settled findings and floods the pull request with near-duplicate
comments in slightly different wording every time the author pushes. The blank-slate instinct is
usually defended as objectivity. It produces noise, and noise gets the bot turned off.

**Give the CI-invoked instance project context.** The instruction file is the mechanism for handing
CI-invoked Claude the testing standards, fixture conventions, and review criteria it needs. For test
generation specifically, putting the existing test files in context prevents it from proposing
scenarios the suite already covers.

Scheduling is a cost decision with a clear discriminator: is anyone waiting? Blocking pre-merge
checks are synchronous, because a developer is sitting there. Overnight tech-debt reports, nightly
test generation, and weekly security audits fit the Message Batches API, which halves cost against a
window of up to 24 hours with no latency SLA, and matches outputs to inputs via a `custom_id` per
request. One hard limitation decides several exam questions: batch cannot execute a tool mid-request
and return the result to the model. Any analysis that needs to fetch related files partway through
cannot use batch, regardless of how flexible its deadline is.

### 2.4 Measuring whether it was worth it

This is the part a consultant transitioning to architect is best placed to get right and most likely
to over-engineer.

The wrong measurement is activity. Invocations per week, seats onboarded, hours spent in the tool,
lines of generated code accepted — these all move when adoption moves, which makes them satisfying
and makes them useless. They tell you the tool is being used. Nobody asked whether the tool is being
used. They asked whether the delivery outcomes improved.

So measure the outcome the tool was adopted to improve. If it was adopted to shorten cycle time,
measure cycle time from first commit to merge. If it was adopted to reduce defect escape, measure
defects found in production per release. If it was adopted to cut code-review latency, measure time
from review requested to review completed. If it was adopted to accelerate onboarding, measure time
from a new engineer's start date to their first merged non-trivial change.

Three disciplines make those numbers survive contact with a sceptical executive:

**Name the metric before adoption, not after.** A metric selected after the fact is selected because
it moved, and everyone in the room knows it.

**Establish a baseline.** A cycle-time figure with nothing to compare it against is a number, not
evidence.

**State the confound.** Team size changed, the release process changed, a large refactor landed
mid-quarter. Naming the confound yourself is the difference between a credible measurement and a
sales pitch, and it is exactly the register the Stakeholder Communication domain also rewards.

There is one legitimate use for activity data: as a leading indicator during rollout, to tell you
whether the thing you are about to measure is even being used yet. Low adoption explains a flat
outcome metric. It does not substitute for one.

### 2.5 Worked example: the review bot nobody trusts

A 40-engineer organisation runs an automated first-pass review on every pull request. Six weeks in,
the numbers look healthy — the job runs on every PR, it posts a median of nine comments, and it has
never failed. Engineers have quietly agreed to ignore it. The team lead asks what to fix.

Pull the actual complaints apart and there are usually three, each with a different mechanism.

*It repeats itself.* Every push produces a fresh batch of comments including ones from the previous
run, reworded. Fix: feed prior findings into the re-run prompt and instruct it to report only new or
unresolved issues.

*It flags things that are conventions here.* It objects to the repository pattern in the data layer,
which is deliberate and documented nowhere the tool can see. Fix: put the review criteria and the
architectural conventions in the project instruction file, which is the mechanism for giving a
CI-invoked instance project context.

*Its comments land as one wall of prose per PR instead of on the offending lines.* Fix:
`--output-format json` with `--json-schema`, so each finding carries a file path, a line number, and
a severity that the GitHub API can place inline.

None of those three is a prompt-quality problem, and the instinct to rewrite the prompt would have
fixed none of them. Now the measurement question. Six weeks of "the job ran on every PR" told the
team nothing, because run count is activity. The outcome this was adopted to improve was review
latency and defect escape. Baseline both, then compare after the three fixes land — and say out loud
that the team also grew by five people during the window, so the cycle-time figure has a confound in
it.

### 2.6 How the exam probes this

The scenario gives you a workflow that is technically functioning and practically failing, then asks
for the intervention. The correct answer is usually a change to *where in the process* something
happens, or to *what context the tool receives*. Distractors are usually a change to how the prompt
is worded, or a change of model.

Watch for these tells:

- "Each generated version misses a different requirement" points at the interview pattern. The brief
  is incomplete.
- "Interpreted inconsistently across runs" points at concrete examples. Prose is ambiguous.
- "Downstream system needs to parse it" points at schema-enforced structured output.
- "Duplicate comments on every push" points at prior findings in the re-run prompt.
- "Not blocking anyone, runs overnight" points at the Batches API — unless the task needs tool calls
  mid-request, in which case it cannot.
- "How do we know it's working?" points at the delivery outcome, with a baseline and a named confound.

### 2.7 The wrong turns

**Rewriting the prompt when the mechanism is the problem.** The single most expensive habit in this
domain, and §4 is about it.

**Upgrading the model to fix a context problem.** A larger model does not know your fixture
conventions either.

**Iterating on output when the input was incomplete.** Each round fixes the requirement you just
noticed and disturbs the one you fixed last round. Restart with the interview.

**Sending interdependent issues one at a time.** Feels disciplined. Produces contradictory patches.

**Measuring adoption and calling it value.** Feels rigorous because it has numbers in it.

**Using the batch API for anything that needs tool calls mid-request.** The 50% saving is real and
the limitation is absolute.

### 2.8 Takeaways

- The gains come from moving requirements and verification earlier and moving review outward, not
  from typing faster.
- Interview pattern for incomplete briefs, tests for checkable correctness, two or three concrete
  examples for inconsistent transformations, batched feedback for interacting issues.
- `-p` / `--print` for non-interactive execution. `--output-format json` with `--json-schema` when a
  program consumes the output.
- Re-runs carry prior findings. Blank-slate re-runs generate duplicates and lose the team's trust.
- The instruction file is how a CI-invoked instance gets project context.
- Batch API: 50% cheaper, up to 24 hours, `custom_id` for matching, and no tool calls mid-request.
- Measure the delivery outcome the tool was adopted to improve, against a baseline, with the confound
  stated. Activity metrics are a rollout indicator, not evidence of value.

---

## 3. Objective 7.3 — Support debugging and operational issue resolution

### 3.1 Why debugging an agentic system is different

Conventional debugging rests on determinism. The same input produces the same output, so you bisect:
halve the search space, observe, halve again. Ten steps and you have the line.

An agentic system breaks two assumptions in that method. Output varies between runs on identical
input, so a symptom that disappears is not evidence that a change fixed it. And "the input" is not
one thing — it is the assembled result of several layers, most of which nobody looked at. The model
saw a system prompt, some concatenated instruction files, possibly some path-scoped rules, a tool
schema, retrieved documents, prior turns of conversation, and the user's actual message. When
behaviour is wrong, the wrongness lives in exactly one of those layers, and the layer is rarely the
one named in the bug report.

So the method changes from bisecting the code to identifying the layer. The question is not "what
line is wrong" but "which layer owns this symptom, and did the content I think is present actually
arrive?"

That reframing is the single most useful thing in this objective, and it generalises past Claude
Code to any production Claude system you are asked about in Domain 4 or Domain 3.

### 3.2 The diagnostic ladder

Work these in order. Each rung is cheaper than the one below it, and each one eliminates a family of
causes.

**Rung 1 — Is the content actually loaded?** Before theorising about model behaviour, verify what the
model received. `/memory` lists the memory files loaded in the current session, and it is the first
step for any symptom of the form "it follows this rule sometimes but not always" or "it works on
their machine." Half of the reports in this family close here: the file holding the rule is at the
wrong level, in the wrong directory, or in someone's home folder.

**Rung 2 — Is it in the right layer for the behaviour we want?** Loaded is not sufficient. A rule
loaded as always-on instruction context is a strong suggestion the model weighs against everything
else in context. A rule expressed as a tool permission scope is a boundary. A rule enforced outside
the model's discretion holds every time. If a rule must never be violated and it is currently sitting
in instruction prose, the rule is in the wrong layer and no rewording moves it.

**Rung 3 — Is the context polluted or stale?** Long sessions accumulate. A skill that produces large
exploratory output floods the window and the original task drifts out of focus — `context: fork` runs
it in an isolated subagent context and returns only the result. Tool results from earlier in a
session can be stale if files have changed since, and a fresh session seeded with a short summary of
prior findings beats resuming with old tool data. `/compact` compresses context while preserving what
it judges essential, with a documented risk: exact numeric values, dates, and specific details can be
lost in the summarisation. Compacting mid-task, when the implementation phase still needs the
discovery detail, is the classic wrong call — the right one is to isolate the verbose discovery work
in a subagent from the start so the main session never fills.

**Rung 4 — Is the tooling wired correctly?** Wrong tool selected, a tool the agent should not have
had at all, a subagent spawned without the permissions it needs, or a capability present that nothing
in the task requires. The exam guide's own sample material carries the governing principle here:
least privilege means **removing** an unneeded capability, not logging its use or asking for
confirmation each time. Logging tells you afterwards. Confirmation makes a human the rate limiter.
Neither is least privilege.

**Rung 5 — Is it retrieval?** When a system that was accurate turns confidently wrong, and something
changed in the data rather than in the prompt or the model, look at retrieval and indexing first. The
guide's sample material is explicit that a RAG system going confidently wrong right after a document
refresh points at the retrieval and indexing layer, not at the model. Confident and wrong is the
signature of correct reasoning over incorrect retrieved content, because the model has no way to know
the passage it was handed is the wrong one.

**Rung 6 — Only now, the prompt or the model.** By this point you have eliminated absence, layer
mismatch, pollution, wiring, and retrieval. What remains is genuinely a prompting or model-fit
problem, and it is a much smaller category than the bug reports suggest.

### 3.3 Worked example: "it works on my machine"

An engineer reports that Claude Code applies the team's API error-envelope convention in some
sessions and not others, on the same repository, within the same week. They have started prefixing
their prompts with the convention manually, in capitals, which works about four times in five.

Rung 1. Run `/memory` in a session where the convention held and in one where it did not, and compare
the loaded set. Suppose the convention lives in a path-scoped rule with a glob for `src/api/**/*.ts`.
Sessions started while working in the API directory load it. Sessions started at the repository root,
or from a test file elsewhere, do not. The behaviour is not intermittent; it is conditional, and the
condition is the file path, exactly as configured.

That reframes the fix into a genuine design choice with no default answer. If the convention truly
only applies to API handlers, the current configuration is correct and the engineer's real problem is
that they are editing API code from outside the directory. If the convention applies to any code that
constructs an error response anywhere in the repository, the glob is too narrow and should be
widened, or the rule belongs in the always-loaded project file instead.

Note what did not fix anything: capitalising the instruction in the prompt. It worked four times in
five, which is the worst possible outcome, because a workaround that mostly works suppresses the
signal that would have led to the actual cause.

### 3.4 Worked example: the pipeline that went quiet

A nightly job generates integration tests for services that changed that day, using the Batches API
because nothing blocks on it. It has run for two months. This week the generated tests started
duplicating scenarios the existing suite already covers, and one service's tests began referencing a
fixture helper that was deleted in a refactor.

Two distinct faults, and the temptation is to treat them as one "quality regression" and reach for a
more capable model.

The duplication is a context fault. Test generation avoids proposing already-covered scenarios when
the existing test files are in context. If the job's file-collection step changed — a path filter, a
renamed directory, a glob that no longer matches — the model is now generating against a suite it
cannot see, and it will cheerfully re-invent it.

The stale fixture is also a context fault, one layer up. The fixture conventions live in the project
instruction file, which is the mechanism for giving a CI-invoked instance project context. If the
refactor deleted the helper without updating that file, the instruction file is now describing a
codebase that no longer exists, and it is being loaded with full authority on every run. Committed
context is an asset that decays; nothing warns you when it goes stale.

The operational answer has two parts. Fix both context inputs. Then close the loop that let the
instruction file drift for a week without anyone noticing, because the same drift will happen again
after the next refactor. That second part is the one the Professional tier is asking for.

### 3.5 How the exam probes this

Scenarios present a symptom, some environmental detail, and four candidate root causes or four
candidate fixes. The correct answer names the layer that owns the symptom. Distractors are causes
from a layer the evidence has already excluded, or fixes that treat the symptom at a layer below the
cause.

The evidence in the stem is what excludes layers, so read it for exclusions rather than for
atmosphere:

- "In a short conversation" excludes context-window exhaustion.
- "Same repository, different engineers" points at user-level versus project-level scope.
- "Started right after a document refresh" points at retrieval and indexing.
- "Confidently wrong, not refusing or hedging" points at correct reasoning over wrong retrieved
  content.
- "Works in some sessions, not others" points at conditional loading — check what is loaded.
- "The subagent has the tool but never uses it correctly" points at wiring and permissions, not at
  prompting.

### 3.6 The wrong turns

**Treating variance as intermittency.** "Sometimes it works" usually means "there is a condition and
you have not identified it." Conditional is not random.

**Declaring a fix on a single passing run.** Non-deterministic output means one clean run is weak
evidence. This is the point where the discipline from Domain 4 earns its keep — a fix is demonstrated
against a test set, not against an anecdote.

**Compacting to make room mid-task.** Buys context space by paying in precision, and the details it
drops are disproportionately the exact values you were about to need.

**Adding a confirmation step where a capability should have been removed.** Sounds cautious, reads as
governance, and leaves the capability in place with a human clicking through the prompt.

**Reaching for a bigger model.** The rung-6 answer applied at rung 1. It is expensive, it is slow to
evaluate, and when it appears to help it often just perturbed a non-deterministic system.

### 3.7 Takeaways

- Identify the layer, do not bisect the code. Wrongness lives in one layer and rarely the one named
  in the report.
- Verify what is loaded first. `/memory` closes a large fraction of "works for them, not for me."
- Context pollution is fixed by isolating verbose work in a forked subagent context, not by
  compacting mid-task.
- Least privilege means removing the unneeded capability. Logging and confirming are not substitutes.
- Confidently wrong after a data change points at retrieval and indexing before the model.
- Prompt and model are the last rung, not the first.
- Committed context decays silently. A refactor that invalidates it needs a step that updates it.

---

## 4. The two documented gaps: the mechanism reflex, and plan mode versus direct execution

Both objectives in this section returned 0% on the real Foundations paper. They are here because they
are known-weak, not because they are hard.

### 4.1 The mechanism reflex

State it as a rule and then earn it:

> **A behaviour governed by a configuration mechanism is corrected by adjusting that mechanism.
> Adding a prompt instruction beside it that asks for the same outcome is not a fix.**

Why it is tempting. A prompt instruction is fast, it is reversible, it requires no merge, and it
often appears to work on the first try. It reads as pragmatic. Every incentive in the moment points
at it.

Why it fails. A prompt instruction is advisory input the model weighs against everything else in
context. A configuration mechanism sets a condition. When the two disagree, the mechanism is the
thing that is actually true, and you have created a system whose behaviour depends on which of two
contradictory inputs happens to dominate on a given run. You will then debug the *model* for a week.

Three concrete shapes of this error:

| Symptom | The prompt-instruction non-fix | The mechanism fix |
|---|---|---|
| A skill uses a tool it should not touch | Add "do not use the Bash tool" to the skill body | Scope `allowed-tools` in the skill's frontmatter |
| A skill's exploratory output crowds out the main task | Add "be concise, summarise your findings" | Set `context: fork` so it runs in an isolated context |
| A convention applies only to test files but bleeds elsewhere | Add "only apply this to tests" to the project file | Move it to `.claude/rules/` with a glob for test paths |

In each row the left column asks the model to simulate a constraint the right column simply imposes.
The left column will work most of the time, which is what makes it dangerous.

The generalisation that carries into every other domain: when an option adjusts the existing
mechanism narrowly and another option adds something beside it, prefer the narrow adjustment. The
distractor families named in the corpus template describe the two ways people miss this — DISCARD
replaces the working mechanism instead of adjusting it, and REPAIR fixes downstream what the
mechanism could have prevented upstream.

### 4.2 Selecting the mechanism

Two questions, asked in this order, resolve most of these items.

**Question 1: When does this need to be in effect?**

| When | Mechanism |
|---|---|
| Always, for everyone on the project | Project-level instruction file, version-controlled |
| Always, for one person across all their projects | User-level instruction file, not shared |
| Only when specific files or paths are in play | `.claude/rules/` with glob patterns in YAML frontmatter |
| Only when someone deliberately invokes a procedure | A skill in `.claude/skills/`, or a command in `.claude/commands/` |

**Question 2: How strongly must it hold?**

| Strength required | Mechanism family |
|---|---|
| Guidance the model should follow, weighed with other context | Instruction context — CLAUDE.md, rules files |
| A capability boundary during a defined activity | Tool scoping — `allowed-tools` in skill frontmatter |
| Isolation, so one activity cannot contaminate another | `context: fork` |
| Must hold every time regardless of what any prompt says | Deterministic enforcement outside the model's discretion |

That last row deserves care in a lesson rather than a guess. The general property is what the exam
tests: a mechanism that runs outside the model's discretion is what you reach for when a rule must
hold unconditionally, and it is over-specification to reach for it when the rule is a preference.
Where a scenario names a specific enforcement mechanism, answer with the property — unconditional
enforcement, no model judgement involved — rather than from a half-remembered file schema.

Two cross-checks close most remaining ambiguity. *Does it need to survive a clone?* If yes, it is
inside the repository, not in a home directory. *Does it need to be paid for on every request?*
Always-loaded content costs tokens in every session for every engineer, which is the reason
on-demand skills exist.

### 4.3 Plan mode versus direct execution

The discriminator is not task size and it is not difficulty. It is **whether the approach is already
determined**.

If several valid approaches exist and choosing wrong means expensive rework, plan first: the tool
explores, understands, and designs, presenting a plan before executing, and it is confined to
read-only operations while doing so. If the scope is clear and the approach is defined, execute
directly, because a planning round on a determined task is pure overhead.

From the Foundations corpus:

| Situation | Mode | Why |
|---|---|---|
| Restructure a monolith into services, dozens of files | Plan | Many approaches; wrong choice is expensive to unwind |
| Add Slack support, multiple valid integration approaches | Plan | The approach is the actual decision |
| Library migration touching 45+ files | Plan | Blast radius; a mid-migration reversal is costly |
| Implement a function against a well-defined input/output spec | Direct | Approach is determined by the spec |
| Single-file bug fix with a clear stack trace | Direct | Nothing to decide |

The documented trap is worth quoting because it is the option people pick: "start in direct execution
and switch to planning when it gets hard." That is wrong, and not for a subtle reason. By the time it
has got hard, the tool has made structural decisions on a path it chose without deliberation, and
those decisions are now sunk. Reactive switching costs more than planning upfront on the tasks that
warranted planning, and the tasks that did not warrant planning never trigger the switch anyway.

The combined pattern is the one to name in an answer when it is offered: plan mode for investigation
and design, a human approving the plan, then direct execution to implement.

One Professional-tier extension. Plan mode is not only a quality mechanism, it is a stakeholder
mechanism. A plan produced before execution is a reviewable artifact — something a tech lead can
challenge, something a regulated-sector change process can attach to a ticket, something a
non-engineer sponsor can be walked through. A large refactor that arrives as a completed diff offers
no such surface. If a scenario mentions review, approval, or auditability alongside a
multiple-approach task, plan mode is answering two requirements at once.

---

## 5. Synthesis: enabling a team end to end

Put the three objectives together and the shape of a real enablement engagement falls out. This is
the structure to reach for when a scenario asks you to roll a Claude tooling capability out to an
organisation, and it is also the structure to reach for when a stakeholder asks what your plan is.

**Establish the baseline before you change anything.** Pick the delivery outcome the adoption is
meant to improve and measure it now, while nobody has an interest in the number. Without this, every
later claim is unfalsifiable, and unfalsifiable claims do not survive a budget review.

**Write the codebase's implicit knowledge into committed context.** Structure, conventions, testing
and fixture standards, the constraints that exist for reasons nobody wrote down. This is the step
that unblocks work on an existing codebase, and it is the step teams skip because it looks like
documentation rather than engineering.

**Split configuration by scope and by strength.** Universal standards in the project instruction
file. File-scoped conventions in path-scoped rules with globs. Occasional procedures in skills, so
they cost nothing when unused. Capability boundaries in tool scoping. Unconditional rules in
deterministic enforcement. Version-control all of it, because the point is that it survives a clone
and a personnel change.

**Build an onboarding path a new engineer actually walks.** Cloning the repository must be sufficient
to inherit the team's configuration — that is the test. Whatever cannot be inherited by cloning has
to be a step in an onboarding checklist someone owns, not a paragraph in a wiki someone wrote.

**Change the process, not just the tooling.** Requirements gathered by interview before generation.
Tests written before implementation. Review run in an independent instance from the one that
generated the code. Pipeline jobs that carry prior findings and emit schema-enforced structured
output. These are the changes that produce a different number at the end.

**Instrument for the debugging you will need.** Somebody will report inconsistent behaviour in week
three. The team needs to know to check what is loaded before theorising, and to reach for the
mechanism rather than a louder prompt.

**Re-measure the outcome, with the confounds named.** The same metric, against the same baseline,
with an honest account of what else changed. This is the artifact that gets the second year funded.

**Own the decay.** Committed context describes a codebase that keeps moving. Nothing in the system
tells you when the description stopped being true. Whatever process updates the code has to have a
step that updates the context, or the whole apparatus quietly becomes confident misinformation.

That final point is where this domain stops being about tooling. Enablement is not a project with an
end date; it is a maintained asset, and an architect who hands over shared configuration without
handing over the responsibility for keeping it true has handed over a liability with good initial
conditions.

---

## 6. Misconceptions

| Misconception | Correction |
|---|---|
| "A lower-level CLAUDE.md overrides the project-level one for that directory." | Instruction files are concatenated from root to working directory. All discovered files contribute; there is no documented override precedence between levels. |
| "If the convention is documented, the team will follow it and so will the tool." | Only content that reaches the model in the request shapes output. A wiki page reaches nobody's request. |
| "A recorded walkthrough is a durable way to share a setup." | It is durable and frozen. It teaches the old configuration confidently the day after the configuration changes. |
| "The blocker on a legacy codebase is its size, language, or contributor count." | The blocker is the absence of committed context describing conventions and structure. Size is not the binding constraint. |
| "Adoption is up and usage is high, so the investment is paying off." | Activity metrics move with adoption, not with value. Measure the delivery outcome the tool was adopted to improve, against a baseline. |
| "If the model does the wrong thing, tell it more firmly in the prompt." | A behaviour governed by a configuration mechanism is corrected at that mechanism. Prose beside it competes with it. |
| "Personal configuration is fine as long as everyone sets it up the same way." | It is invisible in review and it does not travel with a clone, so a new joiner inherits none of it. |
| "Start executing and switch to planning if the task turns out to be complex." | By then structural decisions are already sunk. Plan upfront when several valid approaches exist. |
| "Plan mode is for big tasks." | Plan mode is for undetermined approaches. A large task with a determined approach executes directly. |
| "Each CI re-run should start clean so the review stays objective." | Blank-slate re-runs re-litigate settled findings and post duplicate comments. Feed prior findings in and ask for new or unresolved issues only. |
| "Asking the model to interview me first wastes a turn." | For an underspecified task, one interview turn replaces several correction cycles and surfaces requirements before code exists. |
| "Report one issue per message so it can focus." | True for independent issues. For interacting issues, separate fixes contradict each other — send them together. |
| "Adding examples makes it copy the samples instead of generalising." | Two or three well-chosen input/output pairs demonstrate the pattern and the model applies it to novel inputs. |
| "The batch API is the cheap option for any non-urgent job." | It cannot execute a tool mid-request and return the result. Any analysis needing mid-request tool calls is disqualified regardless of deadline. |
| "`/compact` is the right move when context fills up mid-task." | It can drop exact values, dates, and specifics. Isolate verbose work in a forked subagent context instead. |
| "Least privilege means logging or confirming the sensitive capability." | Least privilege means removing the capability that is not needed. Logging is after the fact; confirming makes a human the rate limiter. |
| "Behaviour that works sometimes is non-deterministic and hard to pin down." | It is usually conditional. Find the condition — start by checking what is actually loaded. |
| "A single clean run proves the fix worked." | Output varies between runs. A fix is demonstrated against a test set, not an anecdote. |

---

## 7. Quick reference

**Configuration scope.** Project-level = version-controlled, reaches everyone who clones. User-level
= one person, invisible in review, does not travel. Personal skills override project skills of the
same name.

**Configuration loading.** Instruction files concatenate root → working directory; all contribute.
`.claude/rules/*.md` load conditionally on glob match. Skills and commands load on invocation.
`@import` uses `@` immediately before the path, no space, relative paths resolving against the
importing file. Import depth is contested between sources — never answer on the number.

**Skill frontmatter.** `description` for the menu · `argument-hint` for expected arguments ·
`context: fork` for isolated execution · `allowed-tools` for scoping what it may do.

**Mechanism selection.** When is it needed → always/path-scoped/on-demand. How hard must it hold →
guidance / tool scope / isolation / deterministic enforcement. Does it need to survive a clone → in
the repository. Does it need to be paid for every session → weigh always-loaded against on-demand.

**Plan vs direct.** Undetermined approach with expensive rework → plan first, read-only exploration,
plan presented before execution. Determined approach → direct. Never switch reactively once it "gets
hard." Plan output doubles as a reviewable artifact for approval and audit.

**Refinement techniques.** Different requirement missed each round → interview pattern. Checkable
correctness → tests first, iterate on failures. Inconsistent transformation → two or three concrete
input/output pairs. Interacting issues → one message. Independent issues → sequential.

**Pipeline.** `-p` / `--print` for non-interactive. `--output-format json` plus `--json-schema` when a
program parses the output. Project instruction file supplies CI context. Existing tests in context
prevent duplicate test generation. Re-runs carry prior findings. Review in an instance separate from
the one that generated the code.

**Batch vs synchronous.** Someone waiting → synchronous. Overnight, nightly, weekly, nobody blocked →
Batches API: 50% cheaper, up to 24 hours, `custom_id` matches outputs to inputs, and no tool calls
mid-request.

**Debugging ladder.** Loaded? → right layer? → context polluted or stale? → tooling wired and scoped?
→ retrieval? → only then prompt or model.

**Diagnostic tells.** Short conversation → not the context window. Same repo, different engineers →
scope mismatch. After a document refresh, confidently wrong → retrieval and indexing. Some sessions
only → conditional loading.

**Measurement.** Cycle time, defect escape, review latency, time to a new joiner's first merged
change. Baseline before adoption, metric chosen before adoption, confounds stated. Invocations,
seats, and hours in the tool are rollout indicators, not evidence of value.

**Exam posture for this domain.** Roughly four or five items out of 63. No per-domain floor score, so
study it once and thoroughly, then put the marginal hour into Integration at 19%. Answer every
multiple-response item as if a single missing selection zeroes it, and do not assume you know how the
items are grouped.
