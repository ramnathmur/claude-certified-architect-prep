# Chapter 21: Three Places a Durable Instruction Can Live

## An alias that quietly changed underneath a service

A team building a production service pinned nothing. Their code called the model alias `opus`, the way the quickstart examples do, and it worked well enough that nobody revisited the choice. Anthropic's own documentation is explicit about what that alias actually is: it points to the recommended version for a given provider, and it updates over time. Across two Claude Code upgrades, it did exactly that — before one release, `opus` resolved to a different Opus version on the Anthropic API than it did after. A separate release the same year stopped supporting prefilled assistant-turn responses entirely, and the team's existing calls, which relied on one, started returning a 400 error instead of running the way they had the day before.

The name they'd typed still resolved to something called `opus`, though nothing about their code had changed; what that name pointed to underneath had moved, and nobody had written down which version they'd actually tested against in the first place.

That's a narrow story about one setting. The question underneath it is wider: for any given decision, where does the instruction that produced a result actually live, and if two of those places disagree, which one wins?

## What actually loads, and in what order

Start from a resolved outcome rather than a rule. Someone runs `claude` from `/repo/services/billing`. Four kinds of CLAUDE.md file exist for that path, and all of them load into the same session:

1. The managed policy file: on Windows, `C:\Program Files\ClaudeCode\CLAUDE.md`, written by the platform team and shared with everyone in the organization.
2. `~/.claude/CLAUDE.md`: this developer's own file, shared with nobody, present in every project they open.
3. `/repo/CLAUDE.md`, then `/repo/services/CLAUDE.md`, then `/repo/services/billing/CLAUDE.md`: project instructions, checked into source control, shared with the team through git.
4. `/repo/services/billing/CLAUDE.local.md`: this developer's personal notes for this one project, gitignored, seen by nobody else.

All of it ends up in context, in exactly the order just listed: managed first, then user, then the project files walked from the filesystem root down to the working directory, then the local file appended last inside each directory it appears in. That ordering is the whole rule. Claude Code discovers every file just described and concatenates them into context rather than picking a winner among them — a project instruction sits in context after a user instruction, because "after" is what loading order buys, and nothing more than that.

Managed policy carries one property none of the others do: it is guaranteed to load before user and project files, and no setting at any other scope can exclude it. The `claudeMdExcludes` key can skip a matched ancestor CLAUDE.md file by glob at user, project, local, or managed scope, but it has no effect on a managed-policy file. A managed CLAUDE.md is also the only kind that can sit directly inside `managed-settings.json`, under a `claudeMd` key, instead of a separate file on disk.

Two mechanics keep a hierarchy like this from becoming unmanageable at scale. A CLAUDE.md file can import another with `@path/to/import`, resolved relative to the importing file's own location, recursively up to four hops deep. An import that resolves outside the current working directory triggers a one-time approval dialog the first time Claude Code meets it in that project. And size is capped in both directions: a file over 4 MiB is skipped entirely, and the target for any single file is under 200 lines.

## Company policy, department rule, team norm

The shape underneath this is one an organization would recognize before it ever touched Claude Code. A company-wide policy is written once and applies everywhere. A department narrows it for one part of the business. A team norm narrows it further still, for the people actually doing the work in one corner of the building. Broader scope, read first; narrower scope, read closer to where the work happens.

| Anchor | Real mechanism |
|---|---|
| Company-wide policy | Managed CLAUDE.md scope, plus the managed level of settings.json |
| Department rule | Project CLAUDE.md scope, plus the shared-project level of settings.json |
| Team norm, narrowest rung | Local CLAUDE.md scope (`CLAUDE.local.md`), plus the project-local level of settings.json |
| Outside the ladder, travels with the person rather than sitting at an altitude | User CLAUDE.md scope (`~/.claude/CLAUDE.md`), plus the user level of settings.json |

The analogy has a real limit, worth stating rather than discovering the hard way. In most organizations, a narrower rule beats a broader one it conflicts with: the department's rule overrides company policy where they clash, and the team's norm overrides both. CLAUDE.md doesn't work that way. Every discovered file lands in context; none of them replaces another. Claude reconciles a conflict between a managed line and a local line with judgment, the same way it reconciles two things a person said earlier in the same conversation. The bottom rung has its own mismatch too: a real team norm is shared knowledge, and the local CLAUDE.md file belongs to exactly one person on exactly one machine, and is never shared with anyone.

## Settings.json: the layer the client enforces

Settings.json is worth pausing on for a structural reason: the exam blueprint names it twice, once under Configuration Management and once under Claude Code Operation, and both listings describe the exact same mechanism. It's taught once, in full, here — the Claude Code Operation section later in this chapter adds only the model-pinning specifics that section separately owns.

CLAUDE.md content is text Claude reads and follows with judgment, the same way it follows anything else sitting in its context window. Settings.json is a different kind of object entirely: a set of JSON keys the Claude Code client itself enforces, independent of anything the model decides. A `permissions.deny` rule blocks a command whether or not Claude would have agreed to run it. Documented keys include `permissions`, `hooks`, an `env` block, `model`, `fallbackModel`, `availableModels`, `autoMemoryEnabled`, `autoMemoryDirectory`, `claudeMdExcludes`, `spinnerTipsEnabled`, and a set of plugin keys: `enabledPlugins`, `pluginConfigs`, `extraKnownMarketplaces`.

Five levels resolve any key that's set more than once, ranked highest to lowest:

| # | Level | Source | Scope |
|---|---|---|---|
| 1 | Managed | `managed-settings.json`, MDM, or the claude.ai console | Everyone in the organization |
| 2 | Command line | `claude --settings`, plus per-session flags and env vars | This session only |
| 3 | Project local | `.claude/settings.local.json` | You, this project |
| 4 | Shared project | `.claude/settings.json` | Everyone on this project, via source control |
| 5 | User | `~/.claude/settings.json` | You, every project |

When the same key is set at more than one level, the highest level that sets it wins outright. A `--model` flag can only select from a model an organization's `availableModels` allowlist already permits.

List-valued keys behave differently from single-valued ones. Setting `permissions.allow` at both the user level and the project level doesn't pick one file over the other; the two lists combine. Two keys are named exceptions to that merge. `fallbackModel` is a single chain rather than a list, so the entire value comes from whichever file at the highest precedence defines it, with no merging. `availableModels` merges normally across ordinary scopes, but the moment any managed source defines it, that managed value is taken as-is and any lower-scope additions to the list are dropped.

A short list of keys inverts the whole table: `disableClaudeAiConnectors`, `isolatePeerMachines`, `remoteControlAtStartup`, `crossSessionInbound`, `useAutoModeDuringPlan`, and `syncClaudeAiSkills`. For these, Claude Code takes whichever value is stricter, even when that value sits at a lower-precedence scope than a more permissive managed setting. It's the one place in the whole system where a narrower scope out-ranks a broader one on its own terms.

One more asymmetry is worth knowing before it surprises anyone. A cloud session, whether Claude Code on the web or `claude --cloud`, runs on a fresh clone on different infrastructure than the machine that started it. It reads the shared-project file, because that file travels with the clone, and it reads managed settings. It never reads `~/.claude/settings.json` or `.claude/settings.local.json`; both stay behind on the machine that launched it.

## When "loads first" is mistaken for "wins"

A platform team adds one line to the managed CLAUDE.md: "Never delete a file without asking first." They've read the precedence table above, seen that managed loads before user and project, and conclude the rule is locked in — no developer's own file can undo it.

A developer opens a scratch repository with a `CLAUDE.local.md` that says the opposite: "This is throwaway, delete freely, don't ask." Both instructions land in the same context. Claude has both sentences in front of it and reconciles them with judgment, the way it reconciles two things a person said in the same conversation. Concatenation is not override: the managed line's earlier position in context buys it nothing beyond being read first.

The platform team's actual tool was one level down, in the sibling mechanism this same chapter owns. A `permissions.deny` rule for delete commands, set at the managed level of settings.json, is enforced by the client regardless of what Claude judges. That is the version of "never delete without asking" a local file genuinely cannot talk its way around.

## Rules: instructions that load themselves in

A third place holds a durable instruction, and it isn't CLAUDE.md at all. Rules are individual markdown files inside a project's `.claude/rules/` directory, discovered recursively, so a subfolder like `.claude/rules/frontend/` works the same way the top level does. A user-level equivalent, `~/.claude/rules/`, applies across every project on the machine, and it loads before project rules — project rules take priority when the two conflict.

Two kinds of rule file exist. A rule with no `paths` frontmatter loads at launch, unconditionally, with the same priority as `.claude/CLAUDE.md` itself. A rule that carries `paths` frontmatter is conditional:

```
---
paths:
  - "src/api/**/*.ts"
---
```

That rule stays out of context until Claude actually reads a file matching the pattern. It triggers on file access, not on every tool call, so a rule scoped to `src/api/**` doesn't load just because Claude ran a shell command somewhere else in the repo.

Rules and skills solve a similar-sounding problem in different ways. A rule loads into context automatically, every session or whenever a matching file is opened. A skill loads only when Claude is invoked to use it, or judges it relevant to the prompt in front of it. An instruction that must be present the moment Claude touches a certain file belongs in a path-scoped rule. An instruction that's only useful for one specific kind of task belongs in a skill.

## Agents: a system prompt with almost nothing inherited

A subagent definition is a fourth place, and it works differently from the first three. It's a markdown file with YAML frontmatter, requiring only two fields, `name` and `description`. The frontmatter's body becomes the subagent's entire system prompt. A subagent receives that body, plus basic environment details like the working directory. It does not receive the main Claude Code system prompt, and it does not receive whatever CLAUDE.md content the main conversation loaded. A rule written for the main thread has to be repeated inside the subagent's own file to apply there at all.

Five locations can define a subagent, and when two of them define one with the same name, priority resolves in this order, highest first: managed settings (organization-wide), the `--agents` CLI flag (current session), `.claude/agents/` (current project), `~/.claude/agents/` (every project), and a plugin's own `agents/` directory (wherever that plugin is enabled). The plugin location sits lowest, which matters for the plugin-dependency material two sections ahead: a plugin can ship a subagent, but a project's own definition of the same name always takes precedence over it.

A subagent's model resolves through its own separate chain, in this order: a `CLAUDE_CODE_SUBAGENT_MODEL` environment variable first, then a per-invocation `model` parameter passed when the main conversation invokes it, then the `model` field in the subagent's own frontmatter, and finally, the default when the field is omitted or set to `inherit`, the model the main conversation itself is using.

## Plugin dependencies: pinning someone else's plugin under yours

A plugin can depend on another plugin, and that dependency is itself a durable, versioned record: the `dependencies` array inside `.claude-plugin/plugin.json`. Each entry is either a bare name, which tracks whatever the latest release happens to be, or an object naming a semver range: `~2.1.0`, `^2.0`, `>=1.4`, `=2.1.0`. A bare name means an upstream release can change what your plugin depends on without any warning. A version range holds it at a tested band until someone deliberately moves it.

Version resolution runs off git tags in the form `{plugin-name}--v{version}`, which the `claude plugin tag --push` command creates, and Claude Code fetches the highest tagged version that satisfies the declared range. Plugins installed from npm, an archive, or a raw command source are the exception: there's no tag to resolve against, so a violated constraint is caught at load time instead, and the plugin is disabled with a `dependency-version-unsatisfied` error.

When two installed plugins each constrain the same dependency, Claude Code intersects the two ranges and installs the highest version satisfying both. If the ranges don't overlap at all, one plugin wanting `~2.1` and another wanting `~3.0`, the second plugin's install fails outright with a `range-conflict` error, and the first plugin's install is untouched.

Enabling a plugin cascades: everything it depends on is enabled with it, at the same scope. Disabling runs the cascade in reverse. When another still-enabled plugin still needs the one being turned off, the disable is blocked, and the error names which plugin depends on it and gives the command to disable that one first.

## Prompt versioning: the one place it's actually documented

No core Claude Code or platform reference page is dedicated to prompt versioning as a general practice. The prompt-engineering reference material covers writing a better prompt: clarity, examples, structure. It says nothing about tracking a prompt's history over time.

One place documents an actual versioning mechanism: Managed Agents, a cookbook tutorial rather than a reference-docs page, and specific to that one feature rather than to prompt engineering generally. Every `agents.update` call produces a new immutable version, numbered from `1` at creation. A session that references an agent by a bare ID gets whatever version is currently latest. A session that passes an explicit `{"type": "agent", "id": ..., "version": N}` stays pinned to exactly that version regardless of what gets published afterward. Rolling back is a caller going back to passing an earlier version number; there's no redeploy step, because nothing was ever overwritten.

That mechanism doesn't generalize. It describes how one server-hosted feature manages its own prompt text, rather than a general practice for versioning prompts inside an ordinary application. A separate claim, that the Claude Console offers its own prompt version-control feature, could not be confirmed against the current documentation and isn't something the exam could reasonably test as fact.

## Where this chapter's ownership stops

A hook is enforced code the client runs at a fixed point in the loop, the same category as a `permissions.deny` rule, not an instruction sitting in someone's context waiting on Claude's judgment. Its mechanics belong to the automation chapter. This chapter's business with hooks ends at that one fact of placement.

Chapter 20 mentions settings.json wherever a Claude Code workflow happens to touch a setting. The schema, the five-level precedence, the merge rule and its exceptions, and the security-key inversion all live here, because nowhere else in this course teaches them.

One more boundary is worth stating plainly. This chapter teaches the precedence order across CLAUDE.md's four scopes: which file wins when several of them disagree. It does not teach the separate discipline of keeping a single CLAUDE.md file short enough that its own instructions stay findable. That's a real failure mode, and it's the reason the 200-line target exists, but it's a question about one file's contents. Precedence across files is a different question, and it's the one this chapter answers.

## The words a stem uses for this

A stem naming this chapter says "which file takes effect" or "what's the precedence order" for CLAUDE.md and settings.json, "load automatically when this file type is touched" for a rules match, "the subagent doesn't see the project's CLAUDE.md" for agent scoping, and "an upstream plugin changed underneath us" for a dependency range.

## Claude Code Operation: pinning what actually runs

Return to the alias from the opening. `opus`, `sonnet`, `haiku`, and the other aliases are convenience names: they point at the recommended version for a given provider, and that pointer moves as new versions ship. Pinning means writing the full model name instead, `claude-opus-5` for instance, or setting the matching environment variable, `ANTHROPIC_DEFAULT_OPUS_MODEL`. A pinned name doesn't move when the provider promotes a new release; an alias does, by definition, every time.

Five places can set which model a session runs, and they resolve in this order, highest first: the `/model` command, typed mid-session; the `--model` flag at startup, which holds for that session only; the `ANTHROPIC_MODEL` environment variable, also session-only; the `model` field inside a settings file, which persists across sessions because it's the same settings.json mechanism covered earlier in this chapter; and the `ANTHROPIC_DEFAULT_MODEL` environment variable, which only sets the starting point for a brand-new session and loses to every option above it. A resumed session, whether reached with `--resume`, `--continue`, or `/resume`, keeps the exact model it was using when its transcript was last saved, no matter what any of the five settings currently say — a form of pinning nobody had to configure.

An organization can force the issue two ways, both stronger than anything an individual sets. `availableModels`, set in managed settings, is an allowlist: nothing outside it is selectable, by alias or by pinned name, from any lower scope. A separate, admin-configured default model in the claude.ai console can go further still and override a user's own `/model` choice outright, reapplying itself on every new launch even after someone picked something else.

None of the five settings-based options would have caught the second half of the opening story. The breaking change there wasn't about which version an alias resolved to. Starting with the newer model generation named in the docs, a request carrying a prefilled assistant-turn response returns a 400 error where it once ran normally. Pinning a model version buys stability against silent drift under a name. It says nothing about a capability change on the exact version someone deliberately moved to; that's read from release notes before moving the pin, a separate habit from writing down which version you're on.

Had the team pinned `claude-opus-5` outright, the alias's version history would never have touched them. Reading the model's own release notes before adopting it would have caught the prefill change before it reached production.

## Self-test

**1.** A repository's `/repo/CLAUDE.md` tells Claude to run tests before committing. The organization's managed CLAUDE.md tells Claude to always ask before running any test suite that takes over five minutes. Both apply to the same directory. *(Select one.)*

A. The project file wins, because it loaded most recently relative to the working directory.
B. The managed file wins outright, and the project file's line is dropped from context.
C. Both instructions are present in context together; Claude reconciles them with judgment, and the managed instruction cannot be excluded by any project or user setting.
D. Neither applies until a hook is configured to enforce one of them.

**2.** An organization sets `availableModels` in managed settings to a short list of two models. A project's `.claude/settings.json` sets `availableModels` to a different, longer list. What is the effective value for someone working in that project? *(Select one.)*

A. The two lists merge into one combined list.
B. The managed list is used as-is; the project's additions are dropped.
C. The project list is used, because project settings load after managed settings.
D. Whichever list was edited most recently takes effect.

**3.** A team wants an instruction to load automatically the moment Claude opens any file under `src/payments/**`, without anyone invoking anything, and without it sitting in context during unrelated work elsewhere in the repo. *(Select one.)*

A. Put it in the project's `CLAUDE.md`.
B. Write it as a skill, so Claude loads it when the task looks relevant.
C. Write it as a rule with `paths: ["src/payments/**"]` in its frontmatter.
D. Put it in a managed-settings `claudeMd` block.

**4.** Which two of the following four statements about a subagent's definition are true? *(Select two of four.)*

A. The frontmatter body becomes the subagent's entire system prompt.
B. A subagent automatically receives the main conversation's full CLAUDE.md content.
C. If a project's `.claude/agents/` and a plugin both define a subagent with the same name, the project's definition takes priority.
D. A subagent always uses the same model the main conversation is using, with no way to set a different one.

**5.** Plugin A declares a dependency on Plugin C with the range `~2.1.0`. Plugin B, installed separately, declares a dependency on the same Plugin C with the range `~3.0.0`. Someone installs both A and B. *(Select one.)*

A. Claude Code intersects the two ranges and installs whichever version of C satisfies both.
B. The install of B fails with a `range-conflict` error, and A's install is unaffected.
C. Plugin C is installed twice, once per range.
D. Claude Code silently picks the higher of the two ranges and ignores the lower one.

**Answers.** 1: C. CLAUDE.md files concatenate rather than override; A and B assume an override that doesn't exist, and D reaches for a mechanism this scenario never asked for. 2: B. `availableModels` is a named exception to list-merging: a managed value is taken as-is once set, and A, C, and D all describe rules the mechanism doesn't have. 3: C. A `paths`-scoped rule triggers only on matching file access; A loads every session regardless, B depends on Claude judging relevance rather than guaranteeing it, and D misapplies a managed-policy mechanism to a team-local need. 4: A and C. The frontmatter body is the whole system prompt, and project-scope definitions outrank plugin-scope ones; B is false because a subagent gets only its own frontmatter plus basic environment details, and D is false because a subagent's model resolves through its own four-step chain. 5: B. Non-overlapping ranges fail the second install with `range-conflict`, leaving the first untouched; A describes overlapping ranges, and C and D describe behavior the mechanism doesn't have.
