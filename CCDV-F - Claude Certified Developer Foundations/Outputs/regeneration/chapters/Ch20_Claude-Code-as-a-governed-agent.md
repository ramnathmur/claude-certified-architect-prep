# Chapter 20: Claude Code as a Governed Agent

## A term that undersells itself

Ask a developer what Claude Code is and the answer arrives fast: a coding assistant that lives in the terminal. That much is accurate. What it leaves out is the machinery underneath: a harness that receives Claude's requests and decides, action by action, whether to carry them out, under a permission system with six distinct modes and four levels of configuration. Every named feature this chapter covers, a permission mode, a slash command, the file `/init` writes for you, is a lever on one of two questions: what reaches the agent's context, and what its hands are allowed to touch.

A professional kitchen sorts its whole operation around two comparable questions: who may reach what, and what's already decided before anyone arrives. Each cook works a fixed station, scoped to the tools and ingredients that station reaches. Standing orders, the prep list, the allergen protocol, apply every night regardless of who's cooking. And the head chef can pull in an extra hand for one specific dish without changing anything about how the rest of the kitchen runs. Stations map to permission scoping, standing orders map to a CLI session's defaults and repository initialization, and the extra hand maps to invoking a Skill or a command on demand.

Where that mapping breaks is worth catching now. The extra hand a head chef calls in exercises independent judgment once they're at the station. A Skill has none of that: it is a written procedure loaded into the context of the same agent that was already working.

## Six modes, one shared question: what runs without asking

Permission modes control how much a CLI session lets through before a person has to look. There are exactly six, and the mode set when a CLI session starts is the default every other control in this chapter sits on top of.

| Mode | What it controls | Limitation |
|---|---|---|
| `default` | Reads run free; almost every edit and command still prompts first | Safe on trusted work, but slow; the baseline for an unfamiliar codebase |
| `acceptEdits` | Auto-approves reads, edits, and common filesystem commands inside the working directory; protected paths still prompt | Shell commands outside that scope still gate; wrong choice if the agent must run arbitrary scripts |
| `plan` | Reads only; researches and proposes a plan; makes no edits until you approve it | No output until approval, so wrong for a task that must actually write something |
| `auto` | Auto-approves everything, but a classifier reviews each action and blocks anything that escalates beyond the request or targets unrecognized infrastructure; production deploys and migrations, mass deletes, credential exfiltration, and force-push to main are blocked by default | A research preview: reduces prompts without guaranteeing safety, and availability depends on plan, model version, and admin settings |
| `dontAsk` | Runs only pre-approved allow-listed tools plus read-only commands; auto-denies everything else, with no queue to appeal to | Built for locked-down CI and scripts; the wrong tool for reducing friction on interactive work |
| `bypassPermissions` | Runs every tool call with no prompts and no checks, except a last-resort prompt on a catastrophic delete like `rm -rf /` | Appropriate only inside an isolated, disposable container or VM, never a live developer workstation |

`auto` is easy to mistake for a safe default, since it still runs a classifier. The section on where the surface reading gets it backwards, later in this chapter, works through exactly what that mistake costs.

## Where a setting is allowed to live

Modes set the default for a CLI session; allow and deny rules refine it from outside, and both live in a settings file that can sit at four levels. User level, `~/.claude/settings.json`, applies to every project on the machine. Project level, `.claude/settings.json`, is committed and applies to everyone who clones the repository. Local project level, `.claude/settings.local.json`, is personal and gitignored. Enterprise level, `managed-settings.json`, is set by administrators and cannot be overridden by users or project files.

A deny rule wins over an allow rule at any level, in any mode. That single fact is what makes an enterprise-level deny the most durable control available: no project file and no individual developer's mode choice can remove it, and it still applies even when someone has set a bypass mode locally.

## What a CLI session actually bounds

The CLI session is the unit all of this applies to. It begins when you start Claude Code in a project directory: `CLAUDE.md` loads, applicable rules load, a configured `SessionStart` hook fires, and the permission mode in effect is set for everything that follows until you change it or the CLI session ends and `SessionEnd` fires. Inside that boundary, a task runs through explore, plan, and code: Claude reads and traces the relevant code first, proposes a plan, and only writes once you approve it. `plan` mode holds a CLI session in the first of those three stages on purpose. Every other mode still runs the same sequence; it just auto-approves different points along it.

## A procedure the agent loads on demand

A Skill is a portable Markdown file, `SKILL.md`, placed in `.claude/skills`. Its frontmatter carries a name and a description; its body carries the steps. Claude loads a Skill automatically when a request matches its description, or you invoke it directly by name. That's the primitive itself. How it compares to a built-in tool or an MCP server, and when each is the right call for a given job, is a four-way tradeoff chapter 13 works through in depth.

## An explicit entry point, built-in or your own

Claude Code ships built-in slash commands, `/init`, `/hooks`, `/permissions`, `/plugin marketplace add`, among others, for actions the harness itself performs on request. For your own workflows, current Claude Code treats a Skill as the recommended format for both kinds of invocation: `/skill-name` runs it directly, and Claude loads it automatically when relevant. Set `disable-model-invocation: true` in a Skill's frontmatter and it only ever runs when called by name, which is the shape a custom command usually wants.

The older `.claude/commands/` directory still works. "Legacy" here means superseded, not broken, but a new workflow written today has no reason to start there. Inside a plugin, a command's name gets prefixed by the plugin's own name, so a `run-tests` command shipped in a plugin called `payments` is invoked as `/payments:run-tests`. That prefix is why two plugins can each ship a `run-tests` command without colliding.

## Running where nobody's watching

Headless mode runs Claude Code non-interactively, invoked with the `-p` (`--print`) flag, so a CI pipeline or a script can call it the way it calls any other command-line tool: no terminal UI, no one present to answer a prompt. That's the documented core of it. It's also why `dontAsk` mode exists in the list above: a headless run with nobody to ask needs a mode that denies by default rather than one that waits.

## Streaming mode, named but not detailed here

The exam guide lists streaming mode as its own Claude Code item, and the material available for this course does not document its flags or its exact output format, so this section stays narrow rather than invent them. What's safely inferable from adjacent, sourced material: Claude Managed Agents pass events between your application and the agent as a run progresses, instead of handing back one buffered result at the end. A Claude Code streaming mode plausibly extends that same idea to the CLI, consuming the harness's own output as a live sequence of events rather than waiting for one finished answer. That is an inference from a related pattern. No specific flag, command, or output format is confirmed here, and none should be assumed.

## The file `/init` writes, and why it needs a look

Running `/init` scans the codebase and writes a starter `CLAUDE.md`, saving you the first draft of the standing orders every later CLI session will load. The generated file is a genuinely useful baseline, and the source material is direct about the rest: validate it before you rely on it. A scan can misread a convention or miss a constraint, and whatever `CLAUDE.md` contains loads into every CLI session from that point forward, unreviewed or not.

## Underneath all eight, one pattern

Run the inventory back and one pattern holds for every entry in it. A permission mode decides what the agent's hands may do without asking. A settings level decides who gets to set that. A CLI session decides how long that setting holds. A Skill or a command decides what specialized knowledge enters the agent's context and when. Headless and streaming modes decide who or what is watching the output. Repository initialization decides what's already loaded before anyone asks the agent anything. Two questions repeat across every row: what does this let into the context window, and what does this let the hands touch without a person checking first.

That's also the derivation for how to pick one. The higher the cost of a wrong action, and the harder it is to undo, the more a primitive needs to gate rather than auto-approve. That is the same worst-case question chapter 19 uses to place a human review gate, applied here to choosing a mode in the first place: a mode and a gate are the same decision viewed from two angles, since the mode sets what happens by default across a whole CLI session, and a gate is where you carve out an exception to that default for the one action whose cost is too high to leave to it.

The same logic sorts the two entry points for on-demand work. A description that matches naturally, a PR review someone might ask for in different words each time, belongs in a Skill and is found by matching intent. A procedure with a fixed name someone will type the same way every time, a release checklist, benefits from an explicit invocation and `disable-model-invocation: true`, because there's no ambiguity in the request worth spending a match on.

## Where the surface reading gets it backwards

A team wiring Claude Code into an automated pipeline picks `auto` mode for a batch of routine dependency updates. Their reasoning: the classifier reviewing every action is real protection, since it blocks production deploys, mass deletes, credential exfiltration, and force-push to main by default, and that list covers exactly the kind of mistake the team is worried about. The surface features point toward a safe choice: a screening layer sits between every action and execution, and the specific worst cases are named as blocked.

The mechanism points somewhere else. The source describing `auto` calls it a research preview: it reduces prompts without guaranteeing safety, and its availability depends on plan, model version, and admin settings that can shift under a pipeline built to depend on it. A classifier reviewing whether an action escalates beyond the original request catches drift, a tool call reaching wider than what was asked; it was never built to judge whether the request itself was the wrong thing to automate in the first place; that judgment is about the task as a whole, sitting a level above any single action inside it.

The blocked-by-default list doesn't change that gap. It names four categories a classifier reliably stops. Everything outside those four, including a build script the dependency update happens to touch, runs exactly as unreviewed as it would under `bypassPermissions`, watched by a classifier the source never describes as a guarantee. A pipeline that actually needs a person to catch this belongs back at the question chapter 19 already answers: what's the worst outcome if this runs unchecked, and is anyone positioned to catch it before it does?

## What this chapter does not own

The exam guide names five primitives for customizing Claude Code: Rules, Skills, Commands, Agents, and Agent Memory. This chapter is where two of them get named and taught in full: Skills, the procedure the agent loads on demand, and Commands, the explicit entry point whether built-in or your own. The other three sit beside them but belong elsewhere. Rules files and Agents, two more durable-instruction primitives, belong to chapter 21. Agent Memory, the mechanism that carries state across CLI sessions, was already taught in chapter 18.

Picking a Skill over a built-in tool or an MCP server for a given job is a four-way tradeoff chapter 13 works through in depth. And where a human review gate goes inside an agent's loop is chapter 19's decision in full; this chapter only borrowed its worst-case-cost logic to explain why a permission mode gets chosen the way it does.

One more boundary matters for vocabulary rather than mechanism. Everything above has been about the CLI session: what loads when Claude Code starts, what a permission mode governs for its duration, what ends it. A different kind of session, the application's own, belongs to chapter 24, and the two concepts are not interchangeable.

## What the stem says when it means this chapter

A stem naming a permission mode by behavior ("blocks everything but a pre-approved list," "no prompts except a catastrophic delete"), naming `/init` or a generated `CLAUDE.md`, or asking what a CI pipeline should invoke Claude Code with, is this chapter. A stem about what Claude remembers between CLI sessions, or where a durable rule should live, is chapter 18's or chapter 21's.

## Self-test

**1.** A CI pipeline needs to run Claude Code with nobody present to answer a prompt. The only actions that should ever run are a short pre-approved list of build and lint tools, plus anything read-only; everything else must be refused automatically, with nothing sitting in a queue. *(Select one.)*

A. `default` — it only prompts before edits and commands, which is close enough for an unattended job.
B. `auto` — the classifier screens every action, so nothing unapproved gets through.
C. `dontAsk` — only the allow-listed tools and read-only commands run; everything else is denied with no queue.
D. `bypassPermissions` — no prompts at all, so the pipeline never stalls waiting for a person.

**2.** An organization wants a rule blocking edits to a credentials path that no individual developer's local settings, and no project's own `settings.json`, can remove or override. *(Select one.)*

A. Add the rule to `.claude/settings.json` and ask every contributor to keep it committed.
B. Add the rule to `managed-settings.json` at the enterprise level.
C. Add the rule to `~/.claude/settings.json` on each developer's machine.
D. Switch the team to `plan` mode by default, which blocks all edits until approved.

**3.** A team wants a release-checklist workflow that a developer will always type the same way, and that should never run automatically just because a request sounds similar. Using the current recommended approach: *(Select one.)*

A. Write it as a Skill with a broad description, so it matches more requests.
B. Write it as a Skill with `disable-model-invocation: true`, invoked only as `/release-checklist`.
C. Place it in the legacy `.claude/commands/` directory, since that format is built for this exact case.
D. Write it as a rules file scoped with a `paths` glob to the release directory.

**4.** A developer runs `/init` on an unfamiliar codebase, gets a generated `CLAUDE.md`, and commits it immediately without reading it, reasoning that the tool already scanned the whole repository. *(Select one.)*

A. Reasonable — `/init` reads the codebase directly, so its output needs no review.
B. Not reasonable — the generated file is a baseline that should be validated before use, and whatever it contains loads into every later CLI session.
C. Reasonable, but only if the team also runs `plan` mode for the first CLI session after the commit.
D. Not reasonable — `CLAUDE.md` should never be generated automatically; it should always be written by hand from the start.

**5.** Which two statements correctly describe `acceptEdits` mode, as documented? *(Select 2 of 4.)*

A. It auto-approves reads, edits, and common filesystem commands inside the working directory.
B. It gates writes outside the working directory and edits to protected paths.
C. It removes the last-resort catastrophic-delete check that other modes keep.
D. It is appropriate for a task that must run arbitrary scripts outside the project folder.

**Answers.** 1: C. `dontAsk` denies anything not on its allow-list or read-only, with no queue for a human to clear, which is what "refuse automatically, nobody present" requires; `auto`'s classifier reduces risk but is documented as a research preview, and `default` still needs a person to answer its prompts. 2: B. Only a rule at the enterprise level, in `managed-settings.json`, sits above every other level and survives an individual's local file or a project's own `settings.json`. 3: B. `disable-model-invocation: true` is what stops a Skill from loading on a description match; the legacy commands directory still works but isn't the currently recommended path, and a rules file scopes instructions rather than naming an invokable procedure. 4: B. The source is explicit that a `/init`-generated file is a baseline meant to be validated, and whatever it contains loads into every CLI session that follows. 5: A and B. Both describe the documented scope of `acceptEdits`; C and D describe `bypassPermissions`, and a task needing arbitrary scripts outside the project folder is exactly what `acceptEdits` is not built for.
