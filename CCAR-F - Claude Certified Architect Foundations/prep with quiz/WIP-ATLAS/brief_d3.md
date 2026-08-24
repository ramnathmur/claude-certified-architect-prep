# Authoring brief — D3 Claude Code Configuration & Workflows (20%) · building: The office

Corpus depth file: `prep with quiz/CCA-Prep_Domain-3_v2.md`. Official guide text: `prep with quiz/source/CCA-F-Official-Exam-Guide_text.txt` (task statements 3.1–3.x and the sample questions).

24 cards, in this order (ids fixed):

## D3-01 — CLAUDE.md hierarchy: user, project, directory
Home task statement: TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization
Gist (the concept, to be written as one flat sentence): ~/.claude/CLAUDE.md, .claude/CLAUDE.md or root CLAUDE.md, and subdirectory files all load — they stack, they do not replace each other.
Official-guide bullets this card must cover:
- [3.1-K1] The CLAUDE.md configuration hierarchy: user-level (~/.claude/CLAUDE.md), project-level (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files)
Appendix items it also serves: [APP-I9] CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rul…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

## D3-02 — User-level is personal — it never reaches teammates
Home task statement: TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization
Gist (the concept, to be written as one flat sentence): Instructions in ~/.claude/CLAUDE.md are not version-controlled; a new teammate not receiving them is the diagnostic.
Official-guide bullets this card must cover:
- [3.1-K2] That user-level settings apply only to that user—instructions in ~/.claude/CLAUDE.md are not shared with teammates via version control
- [3.1-S1] Diagnosing configuration hierarchy issues (e.g., a new team member not receiving instructions because they're in user-level rather than project-level configuration)
Appendix items it also serves: [APP-I9] CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rul…

Key Distinction to weave into `tested` / `remember`:
```
KD #1 — Project scope vs User scope for CLAUDE.md
| | Project scope | User scope |
|---|---|---|
| Location | `.claude/CLAUDE.md` or root `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Version-controlled | ✅ Yes | ❌ No |
| Available to all team members | ✅ Yes | ❌ Only that user |
| Use for | Shared conventions, team standards | Personal preferences, personal workflow |

**Exam trap:** New team member doesn't follow convention that existing members do → convention is in `~/.claude/CLAUDE.md`, not the project file.

---
```

## D3-03 — @import keeps CLAUDE.md modular
Home task statement: TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization
Gist (the concept, to be written as one flat sentence): Reference external standards files so each package pulls in only what applies to it.
Official-guide bullets this card must cover:
- [3.1-K3] The @import syntax for referencing external files to keep CLAUDE.md modular (e.g., importing specific standards files relevant to each package)
- [3.1-S2] Using @import to selectively include relevant standards files in each package's CLAUDE.md based on maintainer domain knowledge
Appendix items it also serves: [APP-I9] CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rul…

## D3-04 — .claude/rules/ splits a monolith into topic files
Home task statement: TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization
Gist (the concept, to be written as one flat sentence): testing.md, api-conventions.md, deployment.md instead of one long CLAUDE.md.
Official-guide bullets this card must cover:
- [3.1-K4] .claude/rules/ directory for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md
- [3.1-S3] Splitting large CLAUDE.md files into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md)
Appendix items it also serves: [APP-I9] CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rul…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

Key Distinction to weave into `tested` / `remember`:
```
KD #3 — `.claude/rules/` vs CLAUDE.md vs Skills
| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---
```

## D3-05 — /memory shows what actually loaded
Home task statement: TS 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization
Gist (the concept, to be written as one flat sentence): When behaviour differs between sessions, /memory lists the memory files in force.
Official-guide bullets this card must cover:
- [3.1-S4] Using the /memory command to verify which memory files are loaded and diagnose inconsistent behavior across sessions
Appendix items it also serves: [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

## D3-06 — Slash commands: .claude/commands/ ships with the repo, ~/.claude/commands/ is yours
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): Project commands are version-controlled and available to everyone who clones; user commands are personal.
Official-guide bullets this card must cover:
- [3.2-K1] Project-scoped commands in .claude/commands/ (shared via version control) vs user-scoped commands in ~/.claude/commands/ (personal)
- [3.2-S1] Creating project-scoped slash commands in .claude/commands/ for team-wide availability via version control
Appendix items it also serves: [APP-I10] Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

## D3-07 — Skills live in .claude/skills/<name>/SKILL.md with frontmatter
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): SKILL.md frontmatter supports context: fork, allowed-tools and argument-hint.
Official-guide bullets this card must cover:
- [3.2-K2] Skills in .claude/skills/ with SKILL.md files that support frontmatter configuration including context: fork, allowed-tools, and argument-hint
Appendix items it also serves: [APP-I10] Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

## D3-08 — context: fork runs the skill in an isolated sub-agent
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): Verbose or exploratory skill output stays out of the main conversation.
Official-guide bullets this card must cover:
- [3.2-K3] The context: fork frontmatter option for running skills in an isolated sub-agent context, preventing skill outputs from polluting the main conversation
- [3.2-S2] Using context: fork to isolate skills that produce verbose output (e.g., codebase analysis) or exploratory context (e.g., brainstorming alternatives) from the main session
Appendix items it also serves: [APP-I10] Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-…

Key Distinction to weave into `tested` / `remember`:
```
KD #13 — `context: fork` in skills vs Running in main session
| | `context: fork` | Main session |
|---|---|---|
| Output stored | Isolated subagent context | Main conversation |
| Effect on subsequent turns | None — isolation prevents contamination | Large output or rejected alternatives bleed into next responses |
| Use for | Discovery, analysis, exploration, brainstorming | Implementation, design, conversation |

---
```

## D3-09 — allowed-tools restricts what a skill may do
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): Frontmatter limits tool access during the skill, e.g. no destructive operations.
Official-guide bullets this card must cover:
- [3.2-S3] Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions)
Appendix items it also serves: [APP-I10] Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-…

## D3-10 — argument-hint prompts for missing parameters
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): When the skill is invoked without arguments, the hint tells the developer what to supply.
Official-guide bullets this card must cover:
- [3.2-S4] Using argument-hint frontmatter to prompt developers for required parameters when they invoke the skill without arguments
Appendix items it also serves: [APP-I10] Custom commands and skills: Project vs user scope, context: fork, allowed-tools, argument-…

## D3-11 — Personal skill variants without touching the team's
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): Create a personal variant in ~/.claude/skills/ under a different name so teammates are unaffected.
Official-guide bullets this card must cover:
- [3.2-K4] Personal skill customization: creating personal variants in ~/.claude/skills/ with different names to avoid affecting teammates

Key Distinction to weave into `tested` / `remember`:
```
KD #4 — Project skills vs Personal skills (same name)
Personal skill at `~/.claude/skills/commit/SKILL.md` **overrides** project skill `.claude/skills/commit/SKILL.md` when they share a name.

**Why:** Allows individual customization without forking the team command or creating an unfamiliar command name.

---
```

## D3-12 — Skills are on-demand; CLAUDE.md is always loaded
Home task statement: TS 3.2 — Create and configure custom slash commands and skills
Gist (the concept, to be written as one flat sentence): Universal standards go in CLAUDE.md; task-specific procedures go in skills invoked when needed.
Official-guide bullets this card must cover:
- [3.2-S5] Choosing between skills (on-demand invocation for task-specific workflows) and CLAUDE.md (always-loaded universal standards)

Key Distinction to weave into `tested` / `remember`:
```
KD #3 — `.claude/rules/` vs CLAUDE.md vs Skills
| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---
```

## D3-13 — Path-scoped rules: paths: globs in YAML frontmatter
Home task statement: TS 3.3 — Apply path-specific rules for conditional convention loading
Gist (the concept, to be written as one flat sentence): A rule with paths: ["terraform/**/*"] loads only while editing matching files, saving tokens.
Official-guide bullets this card must cover:
- [3.3-K1] .claude/rules/ files with YAML frontmatter paths fields containing glob patterns for conditional rule activation
- [3.3-K2] How path-scoped rules load only when editing matching files, reducing irrelevant context and token usage
- [3.3-S1] Creating .claude/rules/ files with YAML frontmatter path scoping (e.g., paths: ["terraform/**/*"]) so rules load only when editing matching files
- [3.3-S2] Using glob patterns in path-specific rules to apply conventions to files by type regardless of directory location (e.g., **/*.test.tsx for all test files)
Appendix items it also serves: [APP-I9] CLAUDE.md configuration: Hierarchy (user/project/directory), @import patterns, .claude/rul…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

Key Distinction to weave into `tested` / `remember`:
```
KD #3 — `.claude/rules/` vs CLAUDE.md vs Skills
| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---
```

## D3-14 — Glob rules beat subdirectory CLAUDE.md for conventions spread across the tree
Home task statement: TS 3.3 — Apply path-specific rules for conditional convention loading
Gist (the concept, to be written as one flat sentence): Test files everywhere → **/*.test.tsx rule, not a CLAUDE.md in each folder.
Official-guide bullets this card must cover:
- [3.3-K3] The advantage of glob-pattern rules over directory-level CLAUDE.md files for conventions that span multiple directories (e.g., test files spread throughout a codebase)
- [3.3-S3] Choosing path-specific rules over subdirectory CLAUDE.md files when conventions must apply to files spread across the codebase

Key Distinction to weave into `tested` / `remember`:
```
KD #3 — `.claude/rules/` vs CLAUDE.md vs Skills
| | CLAUDE.md | `.claude/rules/` | Skills |
|---|---|---|---|
| When loaded | Every session | When working on matching file paths | On-demand (slash command) |
| Best for | Universal standards | Path-scoped conventions | Workflow-specific guidance |
| Trigger | Always | Glob pattern match | User invokes `/skillname` |

---
```

## D3-15 — Plan mode for large, ambiguous or architectural work; direct execution for well-scoped fixes
Home task statement: TS 3.4 — Determine when to use plan mode vs direct execution
Gist (the concept, to be written as one flat sentence): Plan first for multi-file changes, migrations and design choices; go direct for a single-file fix with a clear stack trace; plan then execute for a migration.
Official-guide bullets this card must cover:
- [3.4-K1] Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, architectural decisions, and multi-file modifications
- [3.4-K2] Direct execution is appropriate for simple, well-scoped changes (e.g., adding a single validation check to one function)
- [3.4-K3] Plan mode enables safe codebase exploration and design before committing to changes, preventing costly rework
- [3.4-S1] Selecting plan mode for tasks with architectural implications (e.g., microservice restructuring, library migrations affecting 45+ files, choosing between integration approaches with different infrastructure requirements)
- [3.4-S2] Selecting direct execution for well-understood changes with clear scope (e.g., a single-file bug fix with a clear stack trace, adding a date validation conditional)
- [3.4-S4] Combining plan mode for investigation with direct execution for implementation (e.g., planning a library migration, then executing the planned approach)
Appendix items it also serves: [APP-I11] Plan mode vs direct execution: Complexity assessment, architectural decisions, single-file…; [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

## D3-16 — The Explore subagent keeps discovery noise out of the main context
Home task statement: TS 3.4 — Determine when to use plan mode vs direct execution
Gist (the concept, to be written as one flat sentence): Verbose discovery runs in Explore and returns a summary, preserving the main window for multi-phase work.
Official-guide bullets this card must cover:
- [3.4-K4] The Explore subagent for isolating verbose discovery output and returning summaries to preserve main conversation context
- [3.4-S3] Using the Explore subagent for verbose discovery phases to prevent context window exhaustion during multi-phase tasks
Appendix items it also serves: [APP-T3] Claude Code — CLAUDE.md configuration hierarchy (user/project/directory), .claude/rules/ w…

Key Distinction to weave into `tested` / `remember`:
```
KD #22 — Subagent isolation for discovery vs Main-session discovery
For verbose discovery that would exhaust main context:
- ✅ Explore subagent: isolates verbose output, returns concise summary to main session
- ❌ Use `/compact` mid-task (loses precision needed for implementation phase)

---
```

## D3-17 — Two or three concrete input/output examples beat more prose
Home task statement: TS 3.5 — Apply iterative refinement techniques for progressive improvement
Gist (the concept, to be written as one flat sentence): When descriptions are read inconsistently, show the transformation.
Official-guide bullets this card must cover:
- [3.5-K1] Concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently
- [3.5-S1] Providing 2-3 concrete input/output examples to clarify transformation requirements when natural language descriptions produce inconsistent results
Appendix items it also serves: [APP-I12] Iterative refinement: Input/output examples, test-driven iteration, interview pattern, seq…

## D3-18 — Test-driven iteration: write the tests, share the failures
Home task statement: TS 3.5 — Apply iterative refinement techniques for progressive improvement
Gist (the concept, to be written as one flat sentence): Write the suite (behaviour, edge cases, performance) first, then iterate by feeding back failures; fix an edge case with a specific input/expected-output test.
Official-guide bullets this card must cover:
- [3.5-K2] Test-driven iteration: writing test suites first, then iterating by sharing test failures to guide progressive improvement
- [3.5-S2] Writing test suites covering expected behavior, edge cases, and performance requirements before implementation, then iterating by sharing test failures
- [3.5-S4] Providing specific test cases with example input and expected output to fix edge case handling (e.g., null values in migration scripts)
Appendix items it also serves: [APP-I12] Iterative refinement: Input/output examples, test-driven iteration, interview pattern, seq…

## D3-19 — The interview pattern
Home task statement: TS 3.5 — Apply iterative refinement techniques for progressive improvement
Gist (the concept, to be written as one flat sentence): Have Claude ask questions first so it surfaces cache invalidation, failure modes and other considerations you had not anticipated.
Official-guide bullets this card must cover:
- [3.5-K3] The interview pattern: having Claude ask questions to surface considerations the developer may not have anticipated before implementing
- [3.5-S3] Using the interview pattern to surface design considerations (e.g., cache invalidation strategies, failure modes) before implementing solutions in unfamiliar domains
Appendix items it also serves: [APP-I12] Iterative refinement: Input/output examples, test-driven iteration, interview pattern, seq…

## D3-20 — Interacting issues in one message; independent issues one at a time
Home task statement: TS 3.5 — Apply iterative refinement techniques for progressive improvement
Gist (the concept, to be written as one flat sentence): Batch fixes that affect each other; sequence the ones that do not.
Official-guide bullets this card must cover:
- [3.5-K4] When to provide all issues in a single message (interacting problems) versus fixing them sequentially (independent problems)
- [3.5-S5] Addressing multiple interacting issues in a single detailed message when fixes interact, versus sequential iteration for independent issues
Appendix items it also serves: [APP-I12] Iterative refinement: Input/output examples, test-driven iteration, interview pattern, seq…

## D3-21 — -p / --print runs Claude Code non-interactively
Home task statement: TS 3.6 — Integrate Claude Code into CI/CD pipelines
Gist (the concept, to be written as one flat sentence): In CI, -p processes the prompt, prints to stdout and exits; without it the job waits for input.
Official-guide bullets this card must cover:
- [3.6-K1] The -p (or --print) flag for running Claude Code in non-interactive mode in automated pipelines
- [3.6-S1] Running Claude Code in CI with the -p flag to prevent interactive input hangs
Appendix items it also serves: [APP-T4] Claude Code CLI — -p / --print flag for non-interactive mode, --output-format json, --json…

Key Distinction to weave into `tested` / `remember`:
```
KD #15 — `-p` / `--print` flag vs Other approaches for CI/CD
| | `-p` flag | `CLAUDE_HEADLESS=true` | `--batch` | `stdin < /dev/null` |
|---|---|---|---|---|
| Makes Claude non-interactive? | ✅ Yes — documented approach | ❌ Does not exist | ❌ Does not exist | Workaround, not documented |
| Print output to stdout? | ✅ Yes | — | — | — |

---
```

## D3-22 — --output-format json with --json-schema for machine-readable findings
Home task statement: TS 3.6 — Integrate Claude Code into CI/CD pipelines
Gist (the concept, to be written as one flat sentence): Structured CI output can be posted as inline PR comments.
Official-guide bullets this card must cover:
- [3.6-K2] --output-format json and --json-schema CLI flags for enforcing structured output in CI contexts
- [3.6-S2] Using --output-format json with --json-schema to produce machine-parseable structured findings for automated posting as inline PR comments
Appendix items it also serves: [APP-T4] Claude Code CLI — -p / --print flag for non-interactive mode, --output-format json, --json…

## D3-23 — CLAUDE.md is how CI Claude learns your standards, fixtures and criteria
Home task statement: TS 3.6 — Integrate Claude Code into CI/CD pipelines
Gist (the concept, to be written as one flat sentence): Document testing standards, valuable-test criteria and available fixtures so generated tests are worth having.
Official-guide bullets this card must cover:
- [3.6-K3] CLAUDE.md as the mechanism for providing project context (testing standards, fixture conventions, review criteria) to CI-invoked Claude Code
- [3.6-S5] Documenting testing standards, valuable test criteria, and available fixtures in CLAUDE.md to improve test generation quality and reduce low-value test output

## D3-24 — Re-reviews see prior findings; test generation sees existing tests
Home task statement: TS 3.6 — Integrate Claude Code into CI/CD pipelines
Gist (the concept, to be written as one flat sentence): Include last run's findings and ask for new or unaddressed issues only; include existing test files to avoid duplicate scenarios.
Official-guide bullets this card must cover:
- [3.6-S3] Including prior review findings in context when re-running reviews after new commits, instructing Claude to report only new or still-unaddressed issues to avoid duplicate comments
- [3.6-S4] Providing existing test files in context so test generation avoids suggesting duplicate scenarios already covered by the test suite
