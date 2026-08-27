# Domain 7 — Developer Productivity & Operational Enablement

**Weight:** 7% (source: official exam guide v1.0, effective July 2026 — `sources/CCAR-P_Official-Exam-Guide_v1.0.pdf`)
**Objectives covered:** Configure Claude tools and environments for teams (e.g., Claude Code) · Improve developer workflows using AI-assisted tooling · Support debugging and operational issue resolution

---

## 7.1 Configuration Scope & Durable Enablement

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Configure Claude tools and environments for teams |
| Instruction-file levels | User `~/.claude/CLAUDE.md` · Project `<repo>/CLAUDE.md` or `<repo>/.claude/CLAUDE.md` · Directory-level file · `.claude/rules/*.md` |
| Load semantics | **Concatenated** root → working directory. All discovered files contribute. No documented override precedence between CLAUDE.md levels |
| Shared vs personal | Project-level is version-controlled and reaches everyone who clones. User-level reaches one person and is invisible in code review |
| Skill precedence | Personal skill overrides project skill **of the same name** |
| Verification command | `/context` — shows what actually loaded into the current session (`/memory` lists memory file locations, which is a different question) |
| Cost dimension | Always-loaded content is paid for in tokens on every request by every engineer |

### Durability axis — inherited artifact vs person-dependent transfer

Does the thing survive a clone and reach someone who was not present? If not, it is not enablement.

| Situation | Answer | Why |
|---|---|---|
| Three engineers apply a convention, a fourth (new) does not, same repo | The convention lives in the originals' `~/.claude/CLAUDE.md`; move it to project-level and commit | User-level config is not in version control, so a clone inherits none of it |
| A partner team wants to adopt your Claude Code setup | Version-controlled shared configuration, skills and commands, plus an onboarding path they follow | The artifact is inherited; nothing depends on who attended what |
| Same situation, offered as a recorded walkthrough | Reject | Durable and frozen — teaches the old setup with full confidence the day it changes |
| Same situation, offered as a shared chat channel for questions | Reject | Reactive support, not an inherited artifact |
| Results on a large legacy codebase are poor; team blames repo size and contributor count | Write the conventions and structure into committed project context | Missing committed context is the blocker; size, language, and contributor count are not |
| One engineer wants their own `/commit` behaviour without affecting the team | `~/.claude/skills/commit/SKILL.md` — same name, personal override | Personal skills override project skills of the same name; teammates are unaffected |
| A subdirectory file is added to "override" the project file for that directory | Reject | Files concatenate; both load, and a conflict leaves the model with two contradictory instructions |

**Stakeholder answer:** the team's standards were living on individual laptops instead of in the
repository, so a new joiner inherited none of them. **Failure mode:** silent output variance by
engineer, invisible in per-PR review.

### Exam scenario: a newly hired engineer's generated code omits a convention the other three engineers always get

- ✅ The convention is in the other engineers' user-level configuration, not project-level; move it into the version-controlled project configuration and confirm with `/context`
- ❌ Have the new engineer prefix every prompt with the convention — **REPAIR**: patches each session downstream of a configuration gap that a committed file closes once, and fails silently the first time they forget
- ❌ Add the convention to a team wiki page and link it in the onboarding email — **HALF-MOVE**: transfers the knowledge to a human and never reaches the model's request at all

### ❌ Misconception
"Personal configuration is fine as long as everyone sets it up the same way." — Personal configuration is invisible in review and does not travel with a clone, so every new joiner starts with none of it.

---

## 7.2 Configuration Mechanism Selection

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Configure Claude tools and environments for teams |
| Skill location | `.claude/skills/<name>/SKILL.md` · commands at `.claude/commands/` (project) or `~/.claude/commands/` (personal); `$ARGUMENTS` holds the text typed after the command |
| Skill frontmatter keys | `description` (menu text) · `argument-hint` · `context: fork` (isolated subagent context) · `allowed-tools` (scopes what the skill may do) |
| Path-scoped rules | `.claude/rules/*.md` with YAML frontmatter `paths:` globs — loaded only when matching files are in play |
| `@import` | `@` immediately before the path, no space; relative paths resolve against the importing file. **Nesting depth is contested between sources — never key an answer on the number** |
| The reflex | A behaviour governed by a configuration mechanism is corrected at that mechanism, not by prose beside it |

### Mechanism axis — two questions, in order

Q1: *when* must this be in effect (always / on matching paths / on invocation)? Q2: *how hard* must it hold (guidance / capability boundary / isolation / unconditional enforcement)?

| Situation | Answer | Why |
|---|---|---|
| A skill uses a tool it should not touch | Scope `allowed-tools` in that skill's frontmatter | The frontmatter key is the mechanism that governs the behaviour |
| Same situation, fixed by adding "do not use that tool" to the skill body | Reject | Advisory prose competes with context; it does not set the condition |
| A skill's exploratory output crowds the main task out of context | Set `context: fork` | Runs it in an isolated subagent context; only the result returns |
| Same situation, fixed by adding "be concise" to the skill | Reject | Asks the model to simulate isolation instead of imposing it |
| A convention applies only to test files but bleeds elsewhere | `.claude/rules/` entry with a glob for test paths | Deterministic path matching, not model inference from headings |
| Universal coding standards | Project CLAUDE.md | Needed every session; on-demand invocation would depend on memory |
| A 500-line CLAUDE.md mixing standards, PR checklists and deploy steps | Keep universal standards; move workflow procedures to skills, file-scoped conventions to `.claude/rules/` | Always-loaded tokens are paid every session; occasional procedures should cost nothing when unused |
| Same situation, fixed by moving everything into skills | Reject | Universal standards would then need explicit invocation every time |
| A rule that must hold every time regardless of what any prompt says | Deterministic enforcement — a hook, or a `deny` rule in `settings.json` permissions (§7.8) | Instruction prose is weighed against other context; enforcement is not |
| A style preference, proposed for deterministic enforcement | Reject | A suggestion converted into a hard failure someone must merge a config change to undo |

**Compliance constraint:** a rule that must be *auditable*, a rule that must be *followed*, and a
rule that must be *enforced* are three different requirements and select three different mechanisms.

### Exam scenario: a skill must be prevented from performing destructive operations

- ✅ Set `allowed-tools` in the skill's SKILL.md frontmatter to the minimal set it needs
- ❌ Add an instruction inside the skill body telling it not to perform destructive operations — **REPAIR**: asks the model to honour a boundary the frontmatter can impose, and it competes with everything else in context
- ❌ Configure the restriction in `.mcp.json` or the project CLAUDE.md — **WRONG-AXIS**: right intent, wrong mechanism; skill tool scoping lives in SKILL.md frontmatter

### ❌ Misconception
"If the model does the wrong thing, tell it more firmly in the prompt." — A behaviour governed by a configuration mechanism is corrected by adjusting that mechanism; prose beside it creates two contradictory inputs and a run-dependent outcome.

---

## 7.3 Plan Mode vs Direct Execution

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Improve developer workflows using AI-assisted tooling |
| Plan mode | Explores, understands, designs, and presents a plan before executing; read-only operations, no side effects |
| Direct execution | Implements immediately |
| Combined pattern | Plan for investigation and design → human approves → direct execution to implement |
| Documented trap | "Start direct and switch to planning when it gets hard" |
| Professional extension | A plan is a reviewable artifact — it satisfies approval and audit requirements a finished diff does not |

### Decision axis — is the approach already determined?

Not size and not difficulty. If several valid approaches exist and choosing wrong means expensive rework, plan first; if the approach is fixed by the spec, execute.

| Situation | Answer | Why |
|---|---|---|
| Restructure a monolith into services across dozens of files | Plan mode | Many valid approaches; a wrong one is expensive to unwind |
| Add a new integration with multiple valid approaches | Plan mode | The approach *is* the decision being made |
| Library migration touching 45+ files | Plan mode | Blast radius; a mid-migration reversal is costly |
| Implement a function against a well-defined input/output spec | Direct execution | The spec determines the approach; a planning round is pure overhead |
| Single-file bug fix with a clear stack trace | Direct execution | Nothing to decide |
| Large task, but the approach was settled in an approved design | Direct execution | Size is not the discriminator |
| Multi-approach refactor in a change-controlled environment | Plan mode | The plan doubles as the artifact the approval process attaches to |

### Exam scenario: a migration touching 45+ files with several viable sequencing strategies

- ✅ Use plan mode to explore and present a sequencing plan for approval, then execute directly against the approved plan
- ❌ Begin executing and switch to planning once the task proves complex — **HALF-MOVE**: by then structural decisions are sunk on a path chosen without deliberation, and reactive switching costs more than planning upfront
- ❌ Adopt a standing rule that every change in the repository goes through plan mode and written approval, single-file fixes included — **OVERSPEC**: a stronger guarantee than the requirement asks for; it taxes every routine change to control a risk that only exists where the approach is undetermined

### ❌ Misconception
"Plan mode is for big tasks." — Plan mode is for undetermined approaches; a large task whose approach is already fixed executes directly, and a small task with two competing designs may warrant a plan.

---

## 7.4 Workflow Refinement Technique Selection

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Improve developer workflows using AI-assisted tooling |
| Interview pattern | Have the model ask its clarifying questions before implementing |
| Test-driven iteration | Write the suite first; iterate by feeding concrete failures back |
| Concrete examples | 2–3 input/output pairs anchor a transformation prose cannot pin down |
| Feedback batching | Interacting issues in one message; independent issues sequentially |
| Review isolation | The session that generated code is less effective at reviewing it; use an independent instance |

### Decision axis — what kind of failure is this?

Match the technique to the failure signature; the signature is stated in the scenario stem.

| Signature in the stem | Technique | Why |
|---|---|---|
| Each generated version misses a *different* requirement | Interview pattern | The brief is incomplete; iterating on output never completes a brief |
| Correctness is checkable as an assertion; prose bug reports get partial fixes | Test-driven iteration with a concrete failing case | Tests are a machine-checkable definition of done; prose edge cases are read inconsistently |
| Output *shape* varies run to run under an unchanged instruction | Add 2–3 concrete input/output pairs | Examples show format and decision logic unambiguously; the model generalises to new inputs |
| Same, addressed by lengthening the prose description | Reject | Still ambiguous, only longer |
| Three review findings, two of which interact | One detailed message for the interacting pair | Separate fixes to interacting issues contradict each other |
| Three findings, all independent | Sequential iteration | Each change stays easy to verify |
| The generating session is asked to review its own output | Use an independent instance | It retains its reasoning context and is unlikely to challenge its own decisions |

### Exam scenario: three attempts at a caching layer in an unfamiliar domain each miss a different requirement

- ✅ Restart with the interview pattern — have the model ask what it needs to know (invalidation strategy, tolerance for stale reads, scoping, volume) before implementing
- ❌ Continue iterating, correcting one missed requirement per round — **HALF-MOVE**: each round fixes the requirement just noticed and can disturb the previous fix; the incomplete brief is never addressed
- ❌ Move to a more capable model on the grounds that the domain is complex — **DISCARD**: replaces a working tool instead of supplying the requirements it was never given

### ❌ Misconception
"Report one issue per message so it can focus." — True for independent issues; for interacting issues, sequential fixes contradict each other and force another round.

---

## 7.5 AI Tooling in the Pipeline

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Improve developer workflows using AI-assisted tooling |
| Non-interactive execution | `claude -p "<prompt>"` (equivalently `--print`) — processes, prints to stdout, exits. Without it the pipeline hangs waiting for input |
| Non-existent options to reject | `--batch` · `CLAUDE_HEADLESS=true` · redirecting stdin from `/dev/null` (a workaround, not the mechanism) |
| Structured output | `--output-format json` forces JSON; `--json-schema` enforces a schema for safe downstream parsing |
| CI context mechanism | The project instruction file supplies testing standards, fixture conventions, and review criteria; existing test files in context prevent duplicate test generation |
| Re-run rule | Feed prior findings in and instruct: report only new or still-unaddressed issues |
| Batch API | 50% cheaper · up to 24 hours, no latency SLA · `custom_id` matches outputs to inputs · **cannot execute a tool mid-request and return the result** |

### Consumption axis — who or what reads the output?

A person reading prose tolerates variation; a program parsing fields does not, and "usually well-formed" is a production parse error.

| Situation | Answer | Why |
|---|---|---|
| Each finding must be posted as an inline PR comment (path, line, severity, fix) | `--output-format json` with `--json-schema` | Guarantees a well-formed, parseable shape every run |
| Same situation, addressed by an "Output Format" section in CLAUDE.md | Reject | Instruction context makes format likely, not guaranteed |
| CI job hangs indefinitely instead of completing | Add `-p` / `--print` | Without it the tool waits for interactive input |
| Review posts near-duplicate comments on every push | Include the prior run's findings in the re-run prompt | A blank-slate re-run re-litigates settled findings |
| Overnight tech-debt report, nobody blocked | Batch API | Flexible deadline; 50% cost saving |
| Blocking pre-merge check | Synchronous | A developer is waiting on it |
| Non-urgent analysis that fetches related files mid-analysis | Synchronous | Batch cannot execute tools during a request; the deadline is irrelevant |

### Exam scenario: an automated review's findings must be posted as inline PR comments by a downstream script

- ✅ Run non-interactively with `--output-format json` and `--json-schema` so every finding carries path, line, severity, and suggested fix in a guaranteed shape
- ❌ Add a detailed "Output Format" section to the project CLAUDE.md — **HALF-MOVE**: raises compliance without guaranteeing it, and the parser fails on the run that deviates
- ❌ Have the downstream script parse the prose output with regular expressions — **REPAIR**: builds tolerance for malformed output downstream instead of enforcing well-formed output at the source

### ❌ Misconception
"The batch API is the cheap option for any job that isn't urgent." — Batch cannot execute a tool mid-request and return the result, so any analysis needing mid-request tool calls is disqualified no matter how flexible its deadline.

---

## 7.6 Measuring AI Tooling Value

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Improve developer workflows using AI-assisted tooling |
| Measure | The change in the delivery outcome the tooling was adopted to improve |
| Do not measure as value | Invocation counts · seats onboarded · hours in the tool · lines of generated code accepted |
| Discipline | Name the metric before adoption · establish a baseline · state the confound |
| Legitimate use of activity data | A leading indicator during rollout — low adoption explains a flat outcome metric |

### Metric axis — outcome vs activity

Would the number move if the tool were used constantly and nothing shipped faster or better? If yes, it is an activity metric.

| Adoption rationale | Metric | Not the metric |
|---|---|---|
| Shorten delivery cycles | Cycle time from first commit to merge | Invocations per engineer per week |
| Reduce defect escape | Defects found in production per release | Volume of generated code accepted |
| Cut review latency | Time from review requested to review completed | Number of PRs the review job ran on |
| Accelerate onboarding | Time from a new engineer's start date to first merged non-trivial change | Seats provisioned |
| Any of the above, chosen after the data was collected | Reject | A metric selected because it moved is not evidence |
| Any of the above, with no pre-adoption baseline | Reject | A figure with nothing to compare against is a number, not evidence |

**Stakeholder answer:** state the confound yourself — team size changed, the release process changed,
a large refactor landed mid-quarter. Naming it is the difference between a measurement and a pitch.

### Exam scenario: an executive asks whether six months of AI tooling investment paid off

- ✅ Report the delivery outcome the tooling was adopted to improve, against its pre-adoption baseline, with the confounding changes in the period named
- ❌ Report that invocations grew every month and 90% of engineers are now active users — **WRONG-AXIS**: measures adoption, which is a rollout indicator, and says nothing about delivery outcomes
- ❌ Commission a developer satisfaction survey and report the sentiment score — **ARCHITECTED**: sounds rigorous and produces a number, but substitutes perception for the delivery outcome the investment was justified on

### ❌ Misconception
"Adoption is high and usage keeps climbing, so the investment is paying off." — Activity metrics move with adoption, not with value; the claim has to rest on the delivery outcome the tooling was adopted to improve, measured against a baseline.

---

## 7.7 Operational Debugging — Which Layer Owns the Symptom

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Support debugging and operational issue resolution |
| Method | Identify the layer that owns the symptom; bisection assumes determinism an agentic system does not have |
| Rung 1 | Is the content loaded? `/context` shows what actually loaded into the session |
| Rung 2 | Is it in the right layer for the strength required (guidance / tool scope / isolation / enforcement)? |
| Rung 3 | Context polluted or stale? `context: fork` isolates verbose work; `/compact` risks losing exact values, dates, and specifics |
| Rung 4 | Tooling wired and scoped? Least privilege means **removing** the unneeded capability, not logging or confirming its use |
| Rung 5 | Retrieval and indexing — the first suspect when accuracy drops after a data change |
| Rung 6 | Prompt or model — last, not first |
| Evidence rule | Output varies between runs; a fix is demonstrated against a test set, not one clean run |

### Diagnostic axis — what does the stem exclude?

Each environmental detail eliminates a layer; read the stem for exclusions rather than for atmosphere.

| Evidence in the stem | Layer that owns it | Ruled out |
|---|---|---|
| Behaviour differs between engineers on the same repository | Configuration scope — user-level vs project-level | Model version, tool version |
| Works in some sessions, not others, same machine | Conditional loading — check what `/context` reports | Randomness; conditional is not intermittent |
| A fact from two turns ago is missing in a short conversation | The application is not sending prior history | Context-window exhaustion |
| Accuracy collapsed right after a document refresh; answers are confident, not hedged | Retrieval and indexing | The model — confident-and-wrong is correct reasoning over wrong retrieved content |
| A subagent holds the tool but never uses it correctly | Wiring and permissions | Prompt wording |
| Exploratory output pushed the original task out of focus | Context pollution — `context: fork` the verbose step | Model capability |
| Same situation, addressed by `/compact` mid-task | Reject | Precision loss lands on exactly the values the implementation still needs |

**Failure mode to state to stakeholders:** a workaround that works four times in five suppresses the
signal that would have located the cause.

### Exam scenario: a convention holds in some Claude Code sessions and not others, same repository, same week

- ✅ Run `/context` in a working and a failing session and compare what loaded — the rule is in a file that is not consistently discovered (wrong level, wrong directory, or a path-scoped glob that does not match)
- ❌ Restate the convention at the top of every prompt in capitals — **REPAIR**: patches each session downstream of a loading problem, and mostly-working suppresses the diagnostic signal
- ❌ Move to a more capable model on the grounds that instruction-following is inconsistent — **DISCARD**: replaces a working component to explain a symptom the configuration layer already accounts for

### ❌ Misconception
"Behaviour that works sometimes is non-deterministic and hard to pin down." — It is usually conditional rather than random; find the condition, starting with what is actually loaded.

---

## 7.8 Deterministic Enforcement — Hooks and Permission Rules

### Core Facts

| Attribute | Value |
|---|---|
| Objective | Configure Claude tools and environments for teams · support debugging and operational issue resolution |
| Permission rules | `settings.json` → `permissions` object holding three arrays: `allow`, `ask`, `deny`. Entries name a tool and optionally a pattern — `Bash(git push *)`, `Read(./.env)` |
| Permission resolution order | **deny → ask → allow, first match wins. Specificity does not change the order** — a broad `deny` beats a narrow `allow` |
| Enforcement property | Permission rules are enforced by Claude Code, not by the model. Prompt and CLAUDE.md instructions shape what Claude *tries* to do; they do not change what Claude Code *allows* |
| Hooks | User-defined shell commands run at fixed lifecycle points, configured in the same settings files under a `hooks` key, scoped by a `matcher` |
| Hook property | Deterministic control — the action always happens rather than depending on the model choosing to run it |
| Blocking | A `PreToolUse` hook can block the tool call |
| Settings precedence | managed enterprise policy → command line → `.claude/settings.local.json` → `.claude/settings.json` → `~/.claude/settings.json`. **Nothing below managed policy overrides it** |
| Contrast with instruction files | Instruction files *concatenate* — all discovered files contribute, none overrides another. Settings files *resolve by precedence* — there is a winner |

### The two halves behave in opposite ways

| Question | Instruction files | Settings files |
|---|---|---|
| Two files disagree — which wins? | Neither. Both load; the model receives two contradictory instructions | The one higher in the precedence order |
| Can an organisation impose a rule nobody can override? | No | Yes — managed policy |
| Does specificity decide anything? | No | No — order decides, and it is deny → ask → allow |

### Decision table

| Situation | Answer | Why |
|---|---|---|
| A capability must never be exercised, regardless of any prompt | A `deny` rule in `settings.json` permissions | Enforced by Claude Code, outside the model's discretion |
| Same situation, addressed by a strongly-worded CLAUDE.md instruction | Reject | Shapes what Claude tries to do; does not change what is allowed |
| An action must happen every time a tool runs (format, test, audit entry) | A hook on the relevant event, scoped by matcher | The action always happens rather than depending on the model choosing it |
| Same situation, addressed by "remember to run the formatter" in the project file | Reject | A reminder competes with everything else in context |
| A tool call must be stopped before it executes | `PreToolUse` hook, or a `deny` permission rule | Both act before execution; a log acts after |
| A narrow `allow` exists and a broad `deny` also matches | Denied | First match in deny → ask → allow order wins; specificity is irrelevant |
| An organisation must guarantee a rule survives every local override | Managed policy settings | Nothing below it in the precedence order can override it |
| A team style preference, proposed for a hook or a deny rule | Reject | Over-specification: a suggestion converted into a hard failure someone must merge a config change to undo |

### Exam scenario: an agent must never be able to force-push, and a CLAUDE.md instruction saying so has not held

- ✅ Add a `deny` rule for the force-push command pattern to `settings.json` permissions
- ❌ Restate the prohibition more forcefully and in more places in CLAUDE.md — **REPAIR**: instructions shape what Claude tries to do and do not change what Claude Code allows; more prose is more of the thing that already failed
- ❌ Add an `allow` rule listing every git command the agent *may* run, on the grounds that an allow-list is stricter than a deny-list — **HALF-MOVE**: an allow-list narrows the default path but does not stop a matching call the way an explicit `deny` does, and it breaks every legitimate command nobody thought to enumerate

### Exam scenario: a rule must hold on every developer machine and cannot be overridden locally

- ✅ Managed policy settings — nothing below it in the precedence order can override it
- ❌ Put it in the project `.claude/settings.json` and require review on that file — **HALF-MOVE**: `.claude/settings.local.json` sits above it in the precedence order, so a local file still wins
- ❌ Put it in the project CLAUDE.md, which every clone receives — **WRONG-AXIS**: instruction files concatenate and never override, so this cannot produce a rule that wins a conflict at all

### ❌ Misconception
"A more specific permission rule beats a broader one, the way it does in CSS or a firewall." — Rules resolve deny → ask → allow and the first match in that order wins. Specificity never enters into it, so a broad `deny` beats a narrow `allow`.

### ❌ Misconception
"Hooks and permission rules are two names for the same enforcement layer." — A permission rule answers *may this run*. A hook runs your own code at a lifecycle point, and a `PreToolUse` hook can also block. They are configured in the same file and answer different questions.
