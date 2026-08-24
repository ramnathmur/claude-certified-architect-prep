# -*- coding: utf-8 -*-
"""Lessons 1 and 2, verbatim as taught."""

L1 = dict(
    slug="claude-code",
    nav="Claude Code",
    title="Claude Code Configuration and Workflows",
    weight="20% of the paper, about 12 questions",
    body=r"""
Let's start with what's actually on the paper, because that shapes how hard you need to work on each piece.

This domain is twenty percent of the exam, so roughly twelve questions. The published objectives cover six things: how CLAUDE.md files are organised and scoped, how to create commands and skills, how path-specific rules work, when to use plan mode instead of just executing, how to iterate toward a better result, and how to run Claude Code inside a CI pipeline. That's the whole list. When we went through this material the first time I also taught you permission rules and settings precedence, because you were learning the product rather than only the exam. Those are genuinely useful and they are not on Tuesday's paper. I'd leave them alone this week.

## The picture to hold in your head

When we did this the first time, I gave you a workshop, and I want to bring it back because it does most of the work for you.

You share a workshop with a team. By the door there are notes pinned to the wall: how the bench gets left, which glue is banned, whose turn it is to sweep. You don't decide to read them. They're the first thing in front of you every time you walk in.

Inside the lathe cabinet there's a second note, taped to the door. You only see it when you open that cabinet, and that's the point. It's about the lathe. Pinned on the wall by the entrance it would just be noise for everyone who never touches the lathe.

On the shelf there's a folder labelled FITTING A NEW HANDLE. Twelve steps. You go and fetch it by name on the days you're fitting a handle, and it stays on the shelf the rest of the year.

Then on the cupboard with the good chisels there's a lock. Now, the lock is a different kind of object entirely, and this is the part I want you to sit with. Someone can read every note on that wall, understand them, agree with them, and fully intend to comply, and still not get a chisel out of that cupboard. Notes ask. The lock refuses.

Those are your four surfaces. The notes on the wall are your memory files. The note in the cabinet is a path-scoped rule. The folder on the shelf is a skill. The lock is the permission system.

| Surface | When Claude sees it | What it's for | Can it refuse? |
|---|---|---|---|
| Memory files | Every session | Standing conventions the project shares | No |
| Path-scoped rules | When the file being worked on matches a pattern | Conventions tied to a file type or area | No |
| Skills | When somebody calls one by name | Procedures you run occasionally | No |
| Permission rules | Every tool call | Refusing an action outright | Yes |

Here's how to use that in the exam room. Before you read the four options, decide which surface the question is about. You'll find that quite often two or three of the options are describing the wrong surface, and they eliminate themselves before you've thought about the substance at all. And if a question asks you to make something happen *every time*, without exception, then you already know that three of these four surfaces can't deliver it, because three of them only ask.

## The notes on the wall

There are three places a memory file can live. One in your own home folder, which applies to every project you work on. One in the project itself, either at the root or inside its `.claude` folder. And one in a subdirectory, which comes into play when you're working on files there.

Claude walks from the top of the tree down to where you're working, and it joins together every file it finds along the way into a single set of instructions.

I want to spend a moment on why it works that way, because you've lost a mark on this three times now, in Exam 4 twice and again in Exam 7, and I don't think the fact is the problem. I think the reason is.

Imagine it worked the other way, and a deeper file replaced the one above it. You put your team's five hard rules in the project file. A colleague drops a two-line file into the payments folder that says nothing except "log every rejected charge." Under a replacement model, those two lines have just switched off all five of your team's rules for everything in payments, permanently, and nobody is ever told. No sensible configuration system behaves like that, and this one doesn't either. A deeper file adds. It never cancels.

The reason this catches you is worth naming, because it isn't carelessness. Nearly every configuration system you've worked with in fifteen years of consulting resolves conflicts by precedence, and your hands answer before your head does. So carry one word into the exam room and say it to yourself whenever a stem uses the word "hierarchy" about these files: concatenated.

The other half of the wall is about who else can read it. Your home folder file never goes through version control. The project file lives in the repository and reaches everyone who clones it. That gives you a scenario you'll almost certainly meet: three developers have followed a convention for a year, a fourth joins the same repository, and doesn't. Every instinct says go and look at the new person's setup. Look instead at where the rule lives. It's been sitting in the other three people's personal files the whole time, invisible to version control, and therefore invisible to the newcomer.

Three details are worth memorising rather than reasoning about. Imports use an at-sign immediately before the path, with no space:

```markdown
Coding standards: @./standards/coding-style.md
Test requirements: @./standards/testing-requirements.md
```

A relative path resolves against the file that contains the import, not against wherever you happen to be standing. Those two are stable and worth knowing cold.

I owe you a correction on the third one. When I first taught this I told you the maximum import nesting depth is five, and to memorise it rather than reason about it. That number is contested. Your corpus says five, inherited from the community study guide. The current Claude Code documentation says something different, in as many words: "Imported files can recursively import other files, with a maximum depth of four hops." And the official exam guide is silent, naming the `@import` syntax without giving any depth at all.

So if a question does turn on the digit, answer five, because the paper is scored against its own guide. But do not spend revision time on it, and do not let it decide an answer for you. The syntax rules above are the part that is actually stable.

And `/memory` shows you which memory files are actually loaded right now. When a rule is followed some sessions and ignored in others, that's nearly always a rule that is loaded some sessions and not others. Before you argue about what an instruction says, find out whether the file holding it was even in the room.

## The note inside the cabinet

Path-scoped rules live in `.claude/rules/`, and each one carries its glob patterns in a small settings block at the top of the file.

The thing to be precise about is what triggers them. It is the path of the file being worked on. Not the project you're in, not the folder you launched the session from, not a setting somebody enabled. Claude touches a file whose path matches the pattern, and the rule loads. It touches anything else, and the rule stays out of context and costs you nothing.

That property is exactly why this beats a subdirectory memory file for the case the exam keeps returning to. Test files sit next to the code they test, so they're scattered through every directory in the repository. A note taped inside one cabinet can't cover a convention that lives everywhere and nowhere in particular. A pattern like `**/*.test.tsx` catches all of them wherever they landed.

The two alternatives fail in ways worth understanding. Put the same conventions under headings in one large project file, and you're asking the model to work out which heading applies to the file in its hands. That's inference where you could have had a path match. Turn them into a skill instead, and you've made an automatic thing manual, which is the exact property you were trying to preserve.

## The folder on the shelf

A skill is a folder under `.claude/skills/` with a `SKILL.md` inside it, and it shows up as a slash command you type. The older `.claude/commands/` directory works the same way and is still perfectly current. You lost a mark in Exam 5 to an option claiming commands had stopped working once skills arrived. That was invented. When an option asserts that something you use has been deprecated, be suspicious rather than impressed.

Choosing between a skill and a memory file is a question about frequency. Standing conventions go on the wall because they apply to everything you do. A twelve-step release runbook doesn't. Put it on the wall and it sits in front of the model on every unrelated turn, all year, for the four days a year it matters.

That reasoning also answers the bloated-file question when it comes up. A project file that has grown to four hundred lines, mixing coding standards with pull-request checklists and deployment steps, needs sorting by how often each part applies. The standards stay. The runbooks become skills. Moving everything into skills is wrong, because the universal standards would then need invoking each time, and splitting it all into path-scoped rules is wrong too, because a deployment runbook isn't tied to any file path.

Now the frontmatter, which is where your marks have actually gone:

```yaml
---
description: Generate a database migration file
argument-hint: "<migration-name>"
context: fork
allowed-tools: [Write, Read]
---
```

Two of these decide questions, and both of them live in the skill's own file. Not in a server configuration, not in a memory file, not in an array inside some settings file. If an option puts them anywhere else, it's wrong on location alone, before you've even read what it claims to do.

`context: fork` runs the skill in an isolated sub-agent context, so whatever it produces stays there and only a result comes back. You missed this in Exam 4, and the stem shape is very recognisable once you've seen it. The skill runs perfectly. The catalogue it produces is accurate. And then the next twenty minutes of conversation go strange, with Claude referring to modules nobody asked about. Every symptom is about later turns, never about the run itself. When the damage is to the conversation rather than to the output, the answer is isolation. The distractors are usually a faster model, a shorter summary, and splitting the skill in two, and none of them change where the output lands.

`allowed-tools` scopes what the skill may touch while it runs. You missed this one in Exam 6. There's a wrinkle here I want you to hold consciously. The certification treats this key as a restriction: you set it to hold a skill down to safe operations like file writes so it can't do damage. Current product documentation frames the same key as a pre-grant, meaning those tools run without stopping to ask while anything unlisted follows the normal permission flow. Answer the paper with the certification's framing. Both readings agree on the thing a question actually turns on, which is that this key lives in this file.

One more, and it's small but it has come up. Project skills are checked in and reach the team. Personal skills sit in your home folder and reach only you. When both exist under the same name, yours wins. So if you want the team's commit command to behave differently for you without touching anyone else, you create a personal skill with the same name. Renaming it to `my-commit` looks tidier and defeats the purpose, because now there are two commands and you've given up the name your fingers already know.

## Looking before you cut

Plan mode is Claude exploring and designing without touching anything. It reads, searches, and comes back with a plan you approve before a line gets written.

You reach for it when the scope is large, when several approaches are genuinely defensible, when there's an architectural decision sitting inside the task, or when the change is spread across many files. The cases that recur are breaking a monolith into services, choosing between integration approaches with different infrastructure costs, and a library migration touching forty-five files.

Direct execution is right when the scope is settled and the change is routine. A single-file bug fix with a stack trace pointing at the line. Adding one date-validation condition. Planning that is ceremony, and ceremony costs you turns.

There's one wrong answer here that sounds like good judgement, which is why it works as a distractor: start with direct execution and switch to plan mode if it turns out to be complicated. Look closely at those stems and you'll notice the complexity was already stated in the requirements. You didn't need to discover it. You needed to read it. And switching halfway throws away work you've already paid for.

## Getting a better second attempt

Four techniques here, and the exam tends to test which one fits a described failure rather than whether you know they exist.

When the brief is thin and you're working in a domain you don't know well, have Claude interview you before it writes anything. The signal is three generated versions each missing a different requirement. That's not a model problem, it's a specification problem, and the objection that an interview wastes a turn is bad arithmetic when it replaces several rounds of correction.

When a transformation described in prose comes back a different shape every run, stop rewriting the prose and give two or three concrete input and output pairs instead. Prose has already failed at that point, and saying it more emphatically is still prose.

Writing the test suite before the code gives you a machine-checkable definition of done, which acceptance criteria in prose never are. Every iteration then has a concrete failure to aim at.

And when you have several fixes to ask for, the question is whether they interact. A locking bug and a retry bug that depends on the locking behaviour go in one detailed message, because fixing the retry without knowing the new locking design produces a patch that collides with it. Independent problems go one at a time so each round stays easy to verify.

## Running the workshop with nobody in it

In a pipeline there's no one there to answer a prompt, so without the flag that makes the run non-interactive, the process waits for input that never comes and the job hangs until something kills it. That flag is `-p`, or `--print` if you prefer it spelled out. It processes the prompt, writes to standard output, and exits.

Three of the four options on that question will name things that don't exist: a `--batch` flag, a headless environment variable, and redirecting standard input from `/dev/null`, which is a shell workaround rather than the documented route. Make it a rule for yourself never to pick a flag you haven't seen with your own eyes.

If the pipeline is going to act on the result, prose is useless to it. `--output-format json` forces JSON, and `--json-schema` holds that output to a shape, so the script posting comments can rely on a file path, a line number, a severity and a suggested fix all being present. Asking for JSON in the prompt is not the mechanism, because a written format request is obeyed inconsistently. The memory file is still how you give the run its project context: your testing standards, what counts as a valuable test, which fixtures exist, plus the existing test files so it doesn't propose scenarios the suite already covers.

Then there's the re-run problem, and I like this one because the instinct that causes it is a good instinct. Someone pushes a follow-up commit, the review runs again, and the pull request fills with near-identical comments about code nobody touched. The natural thought is that each run should start from a blank slate to stay objective. In this case that's the bug. Feed the previous run's findings into the new prompt and tell it to report only new or still-unaddressed issues.

And the one I'd least like you to lose: the session that wrote the code is the worst available reviewer of it. It's carrying its own reasoning, it already decided why each choice was fine, and re-reading its own justifications it agrees with them. Review in an independent instance that receives the code and the criteria and none of the argument that produced them.

## A note on the built-in tools

Grep, Glob, Read, Write and Edit sit in the tool design domain rather than this one, so they're marked separately on your score report. They belong to the same workshop though, and you've dropped marks on them twice, so they're worth thirty seconds here.

One question separates Grep from Glob: what do you already know? If the thing you know sits inside the files, search the contents. Every caller of a function, an error string, an import statement. If the thing you know is the shape of the name, match names and paths. Every file ending in the test suffix. The trap runs in both directions, so watch for the reversed version too, where someone searches file contents for the word "test" to find test files and misses every test file that doesn't happen to contain that word.

On Edit, the word that matters is unique. It works by locating one exact piece of text, and if that text appears in four places it can't tell which one you meant, so it refuses. You went wrong here in Exam 4 by reasoning rather than guessing, which I'd rather see, so let me correct the reasoning. The failure says the anchor isn't unique, so the instinct is to change it, and change almost always means shorten. A shorter string collides more often, not less. The recovery is dull and it always works: read the file, make the change, write it back.

## Where I'd put your time

You have six days. Of everything above, the concatenation of memory files is the one I'd fix first, because three misses on one mechanism is a pattern rather than bad luck, and the fix is a single word you can rehearse. After that, the two skill frontmatter keys, because they're worth two questions between them and they're pure recall rather than judgement.

Everything else in this domain you've been getting right.
""")


L2 = dict(
    slug="agentic",
    nav="Agentic Architecture",
    title="Agentic Architecture and Orchestration",
    weight="27% of the paper, about 16 questions",
    body=r"""
Twenty-seven percent, so about sixteen questions. The largest block on the paper by a clear margin.

The objectives cover seven things: building the agentic loop, orchestrating coordinators and subagents, configuring how subagents get spawned and what context they receive, enforcing multi-step workflows, using hooks to intercept tool calls, choosing a decomposition strategy, and managing sessions across days. You've averaged around ninety percent here across eight papers, so this is your strongest domain. I'd still give it the most time, because sixteen questions means a bad day here costs more than a bad day anywhere else.

## The surgeon and the scrub nurse

Start with the thing that has to be straight before anything else. When you give Claude a tool, Claude does not run it. Not once, not ever. The model writes down what it wants and stops talking. Your code runs the thing, your code hands the answer back, and then the model picks up from where it left off.

The picture I gave you was a surgeon with both hands inside a patient. She says one word: scalpel. She doesn't turn around, she doesn't walk to the trolley, she doesn't go hunting through the drawer. She holds out her hand and waits. Choosing the instrument is hers. Fetching it is yours.

Now walk the loop itself, slowly, because a lot of the paper balances on this and nothing else. You send the conversation so far, along with the tools available. You receive the response. You look at one field, the reason it stopped. If that reason is `tool_use`, you pull out what it asked for, run it, append the result to the conversation, and go back to the start. If the reason is `end_turn`, the turn is over and you return the text to the person.

There's a part of step three people skip, and it's the part that makes the whole thing work. The result gets appended to the conversation. That accumulation is how the model reasons forward. Without it, the next call has no idea what came back.

Learn the stop reasons as obligations rather than as meanings, because the questions put you inside a situation and ask what you do next. `tool_use` obliges you to execute, append and call again. `end_turn` obliges you to stop. That's the only pair that decides the loop.

Then there are three ways of deciding the loop is finished that feel entirely reasonable when you write them, and all three are named anti-patterns. Reading the response text for something that sounds like a conclusion. Setting an iteration cap and treating it as the stopping condition rather than as a safety backstop. Treating the presence of assistant text as a completion signal. Each of these is written in the register of careful engineering, which is exactly why they work as distractors. Watch for the moment an option starts to sound sensible, because that moment is the trap.

## The kitchen at service

For orchestration I gave you a kitchen brigade, and I want to keep it because the job description falls straight out of it.

The chef at the pass does four things. She splits the work. She writes the brief for each station. She decides which stations to call at all for this particular order. And she takes back what they produce, checks it, and turns it into one plate.

Notice what she does not do. She does not do the research herself. And the stations never talk to each other. Every message goes across the pass. That is hub and spoke, and the reasons are observability, one consistent way of handling errors, and control over what each worker sees.

Now the failure that follows from it. The fish station cannot hear the sauce station. A subagent starts empty. It does not inherit the coordinator's conversation and it shares no memory between invocations. So when your synthesis worker produces a fluent report that cites nothing, the instinct is to add a line to its prompt telling it to cite its sources. It cannot cite what it never received. Whatever it needs goes into its prompt, in a structured form that keeps the claim and its source travelling together.

Here is the idea I most want you carrying out of this chapter, and it's the one you've dropped twice, in Exam 4 and again in Exam 5. A research system is asked about the impact of AI on the creative industries. The coordinator splits the job into subtasks about painting, illustration and image generation. Every worker executes cleanly, every result is accurate and well sourced, and the error log is empty. The final report is thorough on visual art and silent on music, literature and film.

Where is the bug? Not in the search worker's queries, not in the document worker's filters, not in the synthesis worker's gap detection. The workers did what they were handed. **When every component reports success and the output still has holes, look at what they were asked, not at how they performed.** Three of your four options will point downstream, and they will all sound plausible because each one names a real mechanism.

Two more from the kitchen. The chef tells the fish station what has to be on the plate and how good it has to be, not how to hold the knife. An over-prescribed worker brief reads like a script, and it shatters the moment the third search result turns out to be a paywall. Goals and quality criteria survive contact with reality; step-by-step procedures do not.

And stations cook at the same time, which has an exact mechanical condition attached. Multiple spawn calls emitted in a single coordinator response run in parallel. The same calls spread across separate turns run one after another. Same workers, same briefs, completely different wall clock.

## A prompt is a request, a tool list is a fact

You've missed this twice, in Exam 4 and Exam 7, so let me put it bluntly. You do not tell a worker not to change files. You do not give it the ability to change files.

A worker's configuration has three levers doing different kinds of work. Its name and description say what this worker type is for, so the orchestration layer can pick it. Its system prompt shapes how it behaves. Its tool list decides what it is physically able to touch. Only the third of those is a guarantee.

The same logic sits behind the whole enforcement chapter, where I gave you the poster and the turnstile. Two buildings both want strangers out of the server room. One has a poster saying AUTHORISED PERSONNEL ONLY. Most people read it and turn around. Some are in a hurry, some misread it, some decide the rule was written for other people, and the poster never finds out about any of them. The other has a turnstile. No badge, no turn. It does not persuade and it does not care how good your reason is.

Code that runs around a tool call fires every time, whatever the model was thinking. A sentence in a prompt fires most of the time, and the misses cluster exactly where the conversation got complicated, which is exactly where the stakes were highest. So when a scenario involves money, identity or safety, the answer is enforced in code.

Two details inside that. Before the call you can stop or change it; after the call you can only reshape what the model sees. Detection after the fact is not prevention, however good the alert looks. And the limit has to live where the caller cannot set it. If the refund tool takes a maximum-allowed field that the model fills in from policy, then any request the model can make, it can make with a generous limit attached. That is a parameter wearing a gate's clothing.

## Coming back to it tomorrow

Long work spans days, and one question picks between the four moves: how much of yesterday's evidence is still true?

Resuming a named session brings back a specific prior conversation with its saved context, and it's right when what you learned still holds. It carries one risk, which is the risk they test. A resumed session treats its saved tool results as current. If files changed overnight, it reasons over yesterday's contents as though nothing happened, and it does so confidently. So when the evidence has gone stale, start fresh and inject a short summary of what you concluded. When you do resume after changes, name the files that changed so it re-checks those and only those.

Forking a session branches from a shared baseline, which is what you want when comparing two approaches from the same analysis.

The last piece is the one you dropped in Exam 11, and it's worth being precise about because two patterns sound similar. A second agent that receives a finished draft, with none of the drafting agent's reasoning, and returns corrections that the first agent applies, is evaluator-optimizer. The independence is the point. Context isolation is a different thing: scoping a worker's input so verbose material stays out of a window. Both involve limited context. Only one of them is about critique.

The reason self-review fails is structural. A model that has just generated something is carrying its own reasoning, and asking it to review its own work has it re-read its own justifications and agree with them. Which is why adding "review your work carefully" to the generation prompt doesn't help, and neither does extended thinking. Neither one removes the anchoring.
""")
