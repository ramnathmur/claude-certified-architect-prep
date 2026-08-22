# Held-Out Mock Bank — Domain 3: Claude Code Configuration & Workflows (20%)

> HELD-OUT INTEGRITY: every question is original and does not reuse/paraphrase any practice-bank, checkpoint, study-guide-sample, or teaching stem. For Mock A / Mock B only. Scenario 8 intentionally excluded (uncovered).

## Mock A — Domain 3 (12 questions)

### A-D3-01 · Scenario: 2 · Type: scenario/anti-pattern · Difficulty: med
A monorepo holds a root `CLAUDE.md` and a `packages/billing/CLAUDE.md`. The root file contains the import line `@./standards/security.md`, where `standards/security.md` sits beside the root file. A developer is editing `packages/billing/invoice.ts` and complains that the security standards "aren't being picked up." The team's fix is to copy the `@./standards/security.md` line verbatim into `packages/billing/CLAUDE.md`. The copied import now resolves to nothing. Why did the copied import break, and what is the correct fix?

A. Imports only work in the root `CLAUDE.md`; subdirectory `CLAUDE.md` files cannot use `@path` at all, so the line must be deleted.
B. `@path` imports resolve relative to the file that contains them, so `@./standards/security.md` in `packages/billing/CLAUDE.md` looks for `packages/billing/standards/security.md`; point it at the real location (e.g. `@../../standards/security.md`).
C. The import nesting depth limit of 5 was exceeded by adding a second importer, silently dropping the deepest import.
D. Subdirectory `CLAUDE.md` files load before the root file, so the import fired before `standards/security.md` was available; reordering the files fixes it.

### A-D3-02 · Scenario: — · Type: concept/application · Difficulty: med
An engineer authors a skill `audit-deps/SKILL.md` with frontmatter `allowed-tools: ["Read", "Grep"]` and reasons: "Now while this skill runs, Claude is locked to Read and Grep — it physically cannot call Bash, so it can't run `npm audit` or delete anything." During a run the skill calls `Bash` and executes `npm audit`. Which statement correctly explains the behavior?

A. `allowed-tools` pre-approves Read and Grep (they run without a permission prompt) but does not remove any other tool from the pool; Bash is still callable subject to normal permission settings.
B. The frontmatter is malformed — `allowed-tools` must be a comma-separated string, so it was ignored entirely and every tool stayed available.
C. `allowed-tools` is advisory only and has no runtime effect of any kind; only CLAUDE.md can influence tool availability.
D. `allowed-tools` restricts the toolset as the engineer expected, but `Bash` is exempt because built-in execution tools cannot be restricted.

### A-D3-03 · Scenario: 5 · Type: scenario/anti-pattern · Difficulty: hard
A nightly job runs `claude -p "Summarize today's failing tests and propose fixes" --output-format json` on a shared build server. Results are inconsistent run-to-run: sometimes the summary references a custom `/triage` skill and a project MCP server, sometimes not, depending on which feature branch is checked out (each branch ships its own `.claude/` config and `CLAUDE.md`). The team wants byte-stable behavior independent of the checked-out branch's local config. Which single change most directly fixes this?

A. Add `--permission-mode plan` so the run only reads and never mutates state.
B. Add `--bare`, which skips auto-loading of all local config — hooks, CLAUDE.md, skills, plugins, MCP, and auto-memory.
C. Switch to `--output-format text` so branch-specific JSON schemas can't alter the envelope.
D. Run `/compact` at the start of the prompt to discard any inherited branch context.

### A-D3-04 · Scenario: 7 · Type: scenario/application · Difficulty: med
A conversational-assistant team maintains a long-lived design session in Claude Code. The window is filling with verbose transcripts of past tool output, and the assistant is starting to lose the thread of earlier decisions. They want to free the window while keeping working in the same session, and they accept that some exact figures from old logs may get blurred. Which command fits, and what is the documented risk they're accepting?

A. `/memory` — it persists decisions to CLAUDE.md across sessions; the risk is that the file grows unbounded.
B. `/compact` — it compresses prior history to reclaim context; the risk is that exact numeric values, dates, and specific details can be lost in summarization.
C. `--resume` — it reloads the saved session; the risk is that changed files make tool results stale.
D. `context: fork` — it isolates the verbose output in a subagent; the risk is the subagent cannot see the main thread.

### A-D3-05 · Scenario: — · Type: scenario/anti-pattern · Difficulty: med
A team wants database-migration conventions to apply to every migration file, but those files are scattered: `services/orders/migrations/`, `services/users/db/migrations/`, and `tooling/seed/migrations/`. Their current approach is a `migrations/CLAUDE.md` placed in one of those folders, and they're frustrated the conventions don't apply in the others. What is the recommended mechanism?

A. Put a copy of the directory-level `CLAUDE.md` in each of the three migration folders and keep them in sync manually.
B. A `.claude/rules/` file with `paths:` frontmatter using a glob like `**/migrations/**/*` so the rule loads whenever a matching file is edited, regardless of directory.
C. Append all migration conventions to the root `CLAUDE.md` so they are always loaded in every session.
D. Convert the conventions into a `context: fork` skill so they run in isolation on each migration file.

### A-D3-06 · Scenario: 2 · Type: scenario/application · Difficulty: med
A developer is about to introduce a new authentication library across an unfamiliar 60-file service and isn't sure whether to restructure the middleware layer or wrap the existing one. They want Claude to investigate the codebase and propose an approach for them to approve before any file is touched. Which mode is appropriate, and what is its defining guarantee?

A. Direct execution — for a change this large, Claude should start editing immediately and course-correct as it goes.
B. Planning mode — Claude investigates with read-only tools (Read, Grep, Glob) and produces an implementation plan for approval, making no changes.
C. `--bare` mode — it strips local config so the investigation isn't biased by project standards.
D. `acceptEdits` mode — it lets Claude apply edits without prompting so the plan and implementation happen in one pass.

### A-D3-07 · Scenario: — · Type: recall · Difficulty: easy
Which CLAUDE.md scope is intended for a developer's personal preferences and is NOT shared through version control?

A. The project-level `.claude/CLAUDE.md`.
B. The directory-level `CLAUDE.md` in a subfolder.
C. The user-level `~/.claude/CLAUDE.md`.
D. The root-level `CLAUDE.md` at the repository top.

### A-D3-08 · Scenario: 7 · Type: scenario/anti-pattern · Difficulty: med
A chatbot platform team built a `/persona-tune` skill that loads a 30K-token style guide and runs several exploratory analyses, dumping all of it into the conversation. Operators complain that after invoking it, the main assistant "forgets what it was doing" because the window is swamped with the skill's output. Which frontmatter setting addresses this directly?

A. `argument-hint` — so the skill asks which persona to tune before running.
B. `allowed-tools` — so the skill is limited to read-only tools and produces less output.
C. `context: fork` — so the skill runs in an isolated subagent and its verbose output does not pollute the main session.
D. `disallowed-tools` — so the skill cannot write the large analysis back into the conversation.

### A-D3-09 · Scenario: 5 · Type: scenario/application · Difficulty: hard
A CI step must emit a result the next job can parse with a strict shape: an object with `risk_level`, `blocking`, and `notes`. The team currently runs `claude -p "Assess deployment risk and reply as JSON"` and a downstream `jq` parse intermittently fails on malformed output. Which change makes the output reliably conform to the required shape?

A. Add `--output-format json` alone, which both wraps the result and validates it against the team's field names.
B. Add `--output-format json` together with `--json-schema` describing `risk_level`, `blocking`, and `notes` so the output is constrained to and validated against the schema.
C. Re-word the prompt with "IMPORTANT: respond in strictly valid JSON only" — prompt emphasis is the supported guarantee for shape conformance.
D. Add `--permission-mode dontAsk` so the model isn't interrupted mid-generation and therefore can't produce truncated JSON.

### A-D3-10 · Scenario: — · Type: concept/application · Difficulty: med
A team is deciding where two pieces of guidance should live: (1) "Always use 2-space indentation and conventional-commit messages," which should apply in every session, and (2) "Generate a full release-notes draft from the changelog," a multi-step procedure run only when releasing. What is the correct placement?

A. Both in CLAUDE.md, since CLAUDE.md can hold both always-on standards and on-demand procedures.
B. (1) in CLAUDE.md as always-loaded standards; (2) as a skill invoked on demand for the release task.
C. (1) as a skill so it's reusable; (2) in CLAUDE.md so it's always available when needed.
D. Both as `.claude/rules/` files with `paths:` frontmatter so they load only on matching files.

### A-D3-11 · Scenario: 5 · Type: scenario/anti-pattern · Difficulty: hard
A reviewer wants `claude -p` in a pipeline to behave identically to a clean SDK call and writes: "Plain `claude -p` already ignores the machine's local hooks, CLAUDE.md, and MCP — they only load in interactive mode, so `-p` is inherently reproducible." Where is this reasoning wrong?

A. It's correct; `-p` is non-interactive and therefore loads none of the local config.
B. Plain `-p` does auto-load local config (hooks, CLAUDE.md, skills, plugins, MCP, auto-memory); it is `--bare` that skips all of it. `claude -p "..."` ≠ `claude -p --bare "..."`.
C. `-p` loads local config but `--output-format json` is what suppresses it; adding json mode makes the run reproducible.
D. Only auto-memory is skipped by `-p`; hooks and CLAUDE.md still load, so the claim is half right and needs no further flag.

### A-D3-12 · Scenario: 2 · Type: scenario/application · Difficulty: med
A developer maintains a personal investigative skill that reads a directory tree and reports orphaned files. Invoking it with no argument forces them to type the target path in a follow-up turn every time, which is annoying. They also want teammates to keep their own default targets without editing a shared file. Which two choices fit?

A. Add `argument-hint` to the skill frontmatter to prompt for the path, and keep the skill personal under `~/.claude/skills/`.
B. Add `allowed-tools` to the frontmatter so the path is pre-approved, and store the skill in `.claude/skills/` for the team.
C. Add `context: fork` so the path is remembered across runs, and store the skill in `.claude/commands/`.
D. Hard-code the path in the SKILL.md body and commit it to `.claude/skills/` so everyone shares it.

## Mock B — Domain 3 (12 questions)

### B-D3-01 · Scenario: — · Type: scenario/anti-pattern · Difficulty: med
A startup keeps all of Claude Code's instructions in each engineer's `~/.claude/CLAUDE.md`. Onboarding is painful: every new hire must be hand-walked through the team's testing and naming conventions because Claude doesn't apply them on a fresh clone. What is the root-cause diagnosis and the fix?

A. The conventions belong at user level; the new hire simply hasn't run `/memory` yet to load them.
B. Team conventions placed only in user-level `~/.claude/CLAUDE.md` are personal and not VCS-shared, so a clone gets none of them; move them to a project-level `CLAUDE.md` committed to the repo.
C. CLAUDE.md does not propagate conventions at all; the team needs a PreToolUse hook to enforce naming.
D. The new hire's directory-level `CLAUDE.md` is overriding the user-level file; deleting the directory file restores the conventions.

### B-D3-02 · Scenario: 5 · Type: concept/application · Difficulty: med
For an automated, non-interactive Claude Code invocation in a build pipeline, which flag puts the CLI into non-interactive mode — processing the prompt, printing to stdout, and exiting without waiting for input?

A. `--resume`
B. `-p` (equivalently `--print`)
C. `--output-format json`
D. `context: fork`

### B-D3-03 · Scenario: — · Type: scenario/application · Difficulty: med
A frontend team wants accessibility rules to apply only when Claude touches React component files (`*.tsx`) anywhere in the tree, while leaving non-component TypeScript untouched by those rules. Which configuration achieves conditional, type-based loading?

A. A directory-level `CLAUDE.md` placed in the top-level `components/` folder.
B. A `.claude/rules/a11y.md` file with `paths: ["**/*.tsx"]` frontmatter, loaded only when a matching file is edited.
C. An `@path` import of an accessibility file inside the root `CLAUDE.md`.
D. A skill with `argument-hint` that asks which component to check.

### B-D3-04 · Scenario: 7 · Type: scenario/application · Difficulty: med
An assistant-design team frequently re-explains the same project context — domain glossary, preferred tone, escalation policy — at the start of every working session. They want this to persist and load automatically next time without retyping. Which command is built for this?

A. `/compact` — it preserves context by compressing it for reuse next session.
B. `--fork-session` — it branches the saved context so it reappears automatically.
C. `/memory` — it opens CLAUDE.md for editing so notes and preferences persist across sessions and auto-load on startup.
D. `--bare` — it pins the current context so it reloads on the next run.

### B-D3-05 · Scenario: — · Type: recall · Difficulty: easy
What is the maximum nesting depth for `@path` imports in CLAUDE.md (a file imports another file, which imports another, and so on)?

A. 3
B. 5
C. 10
D. Unlimited

### B-D3-06 · Scenario: 5 · Type: scenario/anti-pattern · Difficulty: hard
A team wires Claude Code into CI to auto-review pull requests, but reuses the very same interactive session that wrote the feature to also "review it for regressions." Reviews are consistently soft — the model rarely flags issues in code it just produced. Beyond switching to headless mode, what is the architectural fix the exam expects?

A. Run the review with `--permission-mode plan` in the same session so the model is forced to think before approving.
B. Use an independent instance for review (a fresh, separate invocation) rather than the session that generated the code, because the generating session retains its reasoning context and is less likely to challenge its own decisions.
C. Increase the review prompt's emphasis with "be extremely critical" — bias is a prompting problem, not an architecture problem.
D. Add `--bare` to the review call; stripping local config removes the generation bias.

### B-D3-07 · Scenario: — · Type: concept/application · Difficulty: med
Which statement best distinguishes when to author a custom skill versus when to add guidance to CLAUDE.md?

A. Skills are for always-loaded general standards; CLAUDE.md is for on-demand task invocation.
B. A skill is for on-demand invocation of a specific multi-step task (e.g. review, analysis, generation); CLAUDE.md holds always-loaded general standards and conventions.
C. They are interchangeable; the only difference is that skills live in VCS and CLAUDE.md does not.
D. Skills can only contain tool permissions, while CLAUDE.md can only contain prose, so the content type decides.

### B-D3-08 · Scenario: 2 · Type: scenario/application · Difficulty: med
A developer has a one-line fix: a stack trace points at a single off-by-one in `parseRange()` in one file, and the change is unambiguous. A teammate insists every change should go through planning mode "to be safe." Why is planning mode the wrong default here?

A. Planning mode cannot edit single files; it only works on changes spanning many files.
B. For a single-file, well-understood, unambiguous fix, direct execution is appropriate; planning mode's investigate-and-propose overhead adds no value where there's no ambiguity or breadth.
C. Planning mode would auto-apply the fix without approval, defeating the teammate's caution.
D. Planning mode disables Read and Grep, so Claude couldn't see the stack trace to fix it.

### B-D3-09 · Scenario: 5 · Type: scenario/anti-pattern · Difficulty: hard
A scripted agent calls `claude -p` in a loop over hundreds of repos and the maintainer wants the call to be self-contained and reproducible — never influenced by whatever `.claude/` config, hooks, or MCP a given repo happens to contain. A colleague proposes `claude -p --output-format json` and argues that JSON mode "runs in a sandbox that ignores repo config." Evaluate.

A. Correct — `--output-format json` sandboxes the run and ignores all repo-local config.
B. Wrong — JSON mode only changes the output envelope; to skip auto-loading of repo-local config (hooks, CLAUDE.md, skills, plugins, MCP, auto-memory) you must add `--bare`.
C. Wrong — reproducibility requires `--permission-mode plan`, not `--bare`; json mode is irrelevant.
D. Correct in effect — json mode plus `-p` already skips config because `-p` is non-interactive.

### B-D3-10 · Scenario: 2 · Type: scenario/application · Difficulty: med
During a long, unfamiliar-codebase investigation, the main session's window is bloating with the raw output of file-discovery scans, crowding out the actual task. The architect wants the noisy discovery to happen somewhere that returns only a concise summary to the main context. Which built-in mechanism fits?

A. The Explore subagent — it isolates verbose discovery output and returns only a summary to the main agent.
B. `/memory` — it moves the discovery output into CLAUDE.md so it leaves the window.
C. `--resume` — it reloads a prior session that already did the discovery.
D. `argument-hint` — it limits how much the discovery step can scan.

### B-D3-11 · Scenario: — · Type: concept/application · Difficulty: hard
Which pair correctly describes the difference between `allowed-tools` and `disallowed-tools` in a skill's frontmatter?

A. `allowed-tools` removes every unlisted tool from the pool; `disallowed-tools` pre-approves the listed tools.
B. `allowed-tools` pre-approves (auto-approves) the listed tools without restricting others; `disallowed-tools` actually removes the listed tools from the pool.
C. Both restrict the toolset identically; the names are aliases kept for backward compatibility.
D. `allowed-tools` applies in interactive mode only; `disallowed-tools` applies in headless mode only.

### B-D3-12 · Scenario: 5 · Type: scenario/anti-pattern · Difficulty: med
A PR-review bot re-runs `claude -p ... --output-format json --json-schema schema.json` after every new commit and posts findings as comments. Reviewers complain that each re-run re-posts the same issues already discussed on earlier commits, drowning new findings. Within the bot's invocation, what is the recommended fix?

A. Switch the bot from `-p` to interactive mode so a human can deduplicate before posting.
B. Include the prior review results in the prompt context and instruct Claude to report only new or unresolved issues.
C. Add `--bare` so the bot forgets prior runs and starts clean each time.
D. Drop `--json-schema` so the output varies enough that the comment de-duplicator catches repeats.

## Answer Key — Domain 3

### Mock A
- **A-D3-01** — Correct: B. `@path` imports are resolved relative to the file that contains the import, so the copied `@./standards/security.md` in `packages/billing/CLAUDE.md` points to a nonexistent `packages/billing/standards/security.md`; the fix is a path that reaches the real file (e.g. `@../../standards/security.md`). Why others fail: A is false — subdirectory CLAUDE.md files do support imports; C misuses the depth-5 limit, which counts nesting of imports, not number of importers, and isn't exceeded here; D invents a load-order/timing rule that doesn't exist. Sub-domain: D3.1.
- **A-D3-02** — Correct: A. `allowed-tools` pre-approves (auto-approves) the listed tools while the skill runs; it does not remove other tools, so Bash remains callable under normal permissions — the classic "sounds restrictive but is permissive" trap. Why others fail: B invents a syntax requirement (a YAML list is valid); C overstates by claiming zero runtime effect (it does auto-approve); D invents a built-in-tool exemption. Sub-domain: D3.3.
- **A-D3-03** — Correct: B. `--bare` skips auto-loading of all local config (hooks, CLAUDE.md, skills, plugins, MCP, auto-memory), which is exactly the branch-specific leakage causing nondeterminism. Why others fail: A (plan mode) controls read/write posture, not config loading; C changes only the output format, not what config loads; D (/compact) compresses in-session history and doesn't prevent local config from loading. Sub-domain: D3.6.
- **A-D3-04** — Correct: B. `/compact` compresses prior history to reclaim the window mid-session; its documented risk is loss of exact numeric values, dates, and specific details during summarization. Why others fail: A (/memory) edits CLAUDE.md for cross-session persistence, not in-session compression; C (--resume) reloads a saved session rather than freeing the current one; D (context: fork) is skill frontmatter, not an in-session window command. Sub-domain: D3.5.
- **A-D3-05** — Correct: B. A `.claude/rules/` file with `paths:` glob frontmatter applies conventions by file pattern regardless of directory — ideal for files scattered across the tree. Why others fail: A is the manual-sync anti-pattern; C bloats the always-on CLAUDE.md with rules relevant only to migrations; D misuses context:fork (an isolation setting, not a path-scoped rule mechanism). Sub-domain: D3.2.
- **A-D3-06** — Correct: B. Planning mode is the fit for a large, unfamiliar, multiple-approach change: Claude explores read-only (Read/Grep/Glob) and proposes a plan for approval, making no changes. Why others fail: A is the risky direct-edit default for an ambiguous large change; C (--bare) is a CI/config-loading flag, unrelated to investigate-then-propose; D (acceptEdits) applies edits without approval, the opposite of what's wanted. Sub-domain: D3.4.
- **A-D3-07** — Correct: C. The user-level `~/.claude/CLAUDE.md` holds personal preferences and is not shared via VCS. Why others fail: A, B, and D are all project/repo-scoped files that ARE shared with contributors. Sub-domain: D3.1.
- **A-D3-08** — Correct: C. `context: fork` runs the skill in an isolated subagent so its verbose output does not pollute the main session — directly fixing the "forgets what it was doing" symptom. Why others fail: A (argument-hint) only prompts for a parameter; B (allowed-tools) pre-approves tools and does not isolate context; D (disallowed-tools) removes tools but does not isolate the skill's output. Sub-domain: D3.3.
- **A-D3-09** — Correct: B. `--output-format json` produces JSON and `--json-schema` constrains/validates the result against the required shape — together guaranteeing the parseable structure. Why others fail: A overstates json-format alone (it wraps output but does not enforce the team's specific fields without a schema); C relies on prompt emphasis, which is probabilistic, not a guarantee; D (dontAsk) is a permission posture unrelated to output shape. Sub-domain: D3.6.
- **A-D3-10** — Correct: B. Always-on coding standards belong in CLAUDE.md (loaded every session); the multi-step on-demand release procedure belongs in a skill. Why others fail: A puts an on-demand procedure into always-loaded context, wasting window and missing the skill's on-demand model; C inverts the mapping; D misuses path-scoped rules for guidance that isn't file-pattern-conditional. Sub-domain: D3.3.
- **A-D3-11** — Correct: B. Plain `-p` DOES auto-load local config; only `--bare` skips hooks, CLAUDE.md, skills, plugins, MCP, and auto-memory — so `claude -p` ≠ `claude -p --bare`. Why others fail: A states the misconception the question targets; C invents a config-suppression role for json mode; D fabricates a partial-skip behavior for `-p`. Sub-domain: D3.6.
- **A-D3-12** — Correct: A. `argument-hint` prompts for the path when none is supplied, and keeping the skill under `~/.claude/skills/` keeps it personal so teammates can maintain their own variants without editing a shared file. Why others fail: B's allowed-tools doesn't supply an argument and team placement defeats the personal-variant goal; C misdescribes context:fork (it isolates context, it doesn't remember a path) and `.claude/commands/` is the shared project location; D hard-codes a single shared path, the opposite of per-developer defaults. Sub-domain: D3.3.

### Mock B
- **B-D3-01** — Correct: B. Conventions placed only in user-level `~/.claude/CLAUDE.md` are personal and not version-controlled, so a fresh clone receives none of them; moving them to a project-level committed `CLAUDE.md` fixes onboarding. Why others fail: A misframes user-level as correct and /memory doesn't pull teammates' personal files; C is false (CLAUDE.md does carry conventions as context); D invents an override by a nonexistent directory file. Sub-domain: D3.1.
- **B-D3-02** — Correct: B. `-p` / `--print` is non-interactive mode: process prompt, print to stdout, exit. Why others fail: A (--resume) reloads a session interactively; C (--output-format json) sets output format, not interactivity; D (context: fork) is skill frontmatter, not a CLI mode. Sub-domain: D3.6.
- **B-D3-03** — Correct: B. A `.claude/rules/` file with `paths: ["**/*.tsx"]` loads only when a matching file is edited, applying the rules by file type anywhere in the tree. Why others fail: A (directory CLAUDE.md) is tied to one folder, not a cross-tree file type; C (@path import) loads in every session regardless of file type; D (skill) is on-demand, not automatic type-conditional loading. Sub-domain: D3.2.
- **B-D3-04** — Correct: C. `/memory` opens CLAUDE.md for editing so notes/preferences persist across sessions and auto-load on startup — exactly the "stop re-explaining every session" need. Why others fail: A (/compact) compresses within a session and doesn't persist across them; B (--fork-session) branches a transcript, not durable startup context; D (--bare) skips config loading, the opposite of persisting it. Sub-domain: D3.5.
- **B-D3-05** — Correct: B. The maximum import nesting depth is 5. Why others fail: A, C, and D are not the documented limit. Sub-domain: D3.1.
- **B-D3-06** — Correct: B. Use an independent instance to review, since the generating session retains its reasoning context and is less likely to challenge its own decisions. Why others fail: A keeps the review in the biased session; C reduces an architectural problem to prompt wording; D (--bare) strips config but does not remove the in-session reasoning bias. Sub-domain: D3.6.
- **B-D3-07** — Correct: B. A skill is for on-demand invocation of a specific multi-step task; CLAUDE.md holds always-loaded general standards. Why others fail: A inverts the two; C reduces the difference to VCS location (both can be project-scoped); D invents a content-type restriction that doesn't exist. Sub-domain: D3.3.
- **B-D3-08** — Correct: B. A single-file, unambiguous fix with a clear stack trace is the textbook direct-execution case; planning mode's investigate-then-propose overhead adds no value here. Why others fail: A is false (planning mode isn't limited to multi-file work); C is false (planning mode proposes, it does not auto-apply); D is false (planning mode uses read-only tools like Read/Grep, it doesn't disable them). Sub-domain: D3.4.
- **B-D3-09** — Correct: B. JSON mode changes only the output envelope; skipping auto-loaded repo-local config (hooks, CLAUDE.md, skills, plugins, MCP, auto-memory) requires `--bare`. Why others fail: A and D wrongly credit json mode / plain `-p` with skipping config (plain `-p` loads it); C misattributes reproducibility to plan mode. Sub-domain: D3.6.
- **B-D3-10** — Correct: A. The Explore subagent isolates verbose discovery output and returns only a summary to the main agent, protecting the main context. Why others fail: B (/memory) edits CLAUDE.md and isn't a discovery-isolation mechanism; C (--resume) reloads a prior session rather than isolating fresh discovery; D (argument-hint) only prompts for a parameter. Sub-domain: D3.4.
- **B-D3-11** — Correct: B. `allowed-tools` pre-approves the listed tools without restricting the rest; `disallowed-tools` actually removes the listed tools from the pool. Why others fail: A swaps the two definitions; C falsely calls them aliases; D invents an interactive/headless split. Sub-domain: D3.3.
- **B-D3-12** — Correct: B. Include prior review results in context and instruct Claude to report only new or unresolved issues — the documented way to prevent duplicate comments on re-review. Why others fail: A abandons automation; C (--bare) skips config but doesn't give the model prior-review awareness (it makes duplication worse); D degrades the parseability guarantee to chase a downstream hack. Sub-domain: D3.6.
