# Class 4 — The Bread That Stopped Rising

**Course:** Claude Certified Developer – Foundations
**Covers:** Configuration Management
**Built around:** Configuration is the written record of what was true when it worked. Without it,
"it got worse" is a complaint; with it, "it got worse" is a question you can answer.
**Delivered:** 2026-08-20

---

You have made the same loaf for two years. Same recipe, same oven, same hands. Last Tuesday it came out
flat and it has been flat since.

You did not change the recipe. So what changed?

The flour is from a different mill, because the shop ran out. The yeast is a new packet from a new box.
It is November and the kitchen sits four degrees colder than it did in September. And the oven has been
drifting low for a while, slowly enough that nobody noticed.

The recipe was never the system. It was one part of a system whose other parts were changing quietly
the whole time.

Can you find out which one did it? Only if you wrote down what they were. Notes saying "flour: bread
flour" are finished — you cannot get back to the flour that worked. Notes saying "flour: Shipton Mill,
batch 4471" let you buy that flour and settle it in an afternoon.

**Configuration is the written record of what was true when it worked.**

## What changes under you without you touching anything

This catches people who have built ordinary software for twenty years. You know how to version code.
But in a Claude application most of what decides behaviour is not your code.

- **The model.** A new version ships. If you pointed at a moving alias rather than a fixed version, you
  are now running something different and did not ask to be.
- **The prompt.** Someone tuned a sentence to fix a complaint. That sentence is behaviour. If it lives
  in a config UI or a database row it changed with no diff and no review.
- **A skill or plugin.** Installed from a marketplace, updated to a new version, instructions now
  different.
- **The settings.** Somebody adjusted a permission or a deny rule.
- **Something a plugin depends on** that is not in the plugin — a script, an environment variable, a
  tool it shells out to.

Five moving parts. Your git log records one of them.

## Pinning the model, and why it matters more here

In ordinary software you pin library versions because a minor upgrade might change behaviour in some
documented way you would rather review first. Sensible, dull, well understood.

Model versions are the same practice for a sharper reason.

When a library changes, the change is **discrete and documented**. Some function returns something
different, it is in the changelog, you can read it and reason about whether it affects you.

When a model changes, the change is **statistical and undocumented**. Nothing in particular broke. Your
outputs are a bit different across the board — slightly different phrasing, a slightly different rate of
choosing tool A over tool B, an eval score three points down. There is no line item explaining it
because there is no line. The new model is a different function from text to text, and no changelog can
enumerate what that means for your prompts.

So point at a specific dated version, not a moving alias. Upgrade deliberately, as a change with a date
attached, and re-run your evals when you do. The blueprint names this outright — *breaking behaviour
changes across model releases*.

The failure it prevents is precise. Without pinning, your model changed on a Tuesday, your prompt
changed on a Wednesday, your quality dropped on a Thursday, and there is no way to tell which did it.
With pinning, one of those dates leaves the suspect list.

## A prompt is source code

The prompt is the part of your system that most directly determines what it does. That makes it source
code: in version control, reviewed before it changes, with a readable diff and a date and a name.

The common failure is a prompt living somewhere convenient and unversioned — a database row, an admin
panel, a config service — precisely so it can be tweaked without a deploy. That works until somebody
says "it got worse sometime last month" and there is no history, no diff, and nobody quite remembers.

Convenient to edit and impossible to attribute are the same property described twice.

## Plugins bring what they declare, and nothing else

A plugin bundles skills, hooks, subagents and MCP servers into one installable thing. It does **not**
bundle anything the author relied on but never listed — the deny rule that made a hook safe on their
machine, the environment variable in their shell profile, the script one directory up.

Those were part of the working system. They were not part of the package.

An undeclared dependency is not one that travels badly. It is one that does not travel at all, and
fails **silently**, because the install succeeded and everything looks fine until the exact step that
needed it.

So: declare what you depend on, validate it at install time so a missing one announces itself
immediately, and test the install on a clean machine — the only test where your own assumptions are not
quietly holding the thing up.

The same logic runs upward. An organisation can deploy plugins centrally through managed settings, and
managed settings sit above user and project settings, so something deployed at that level cannot be
overridden locally. That is how a company makes a control hold rather than merely recommending it. Full
hierarchy in Class 5.

## Reproducible is not the same as identical

Pin everything — model version, prompt, skills, settings, temperature — run the same input twice, and
you can still get two different answers. That is sampling. Not a bug, not a configuration failure.
Class 6 covers why.

So what did the pinning buy?

It bought the ability to **tell a change from noise**. With everything pinned, your evals give a
distribution — some spread, some average. Run them next week and you get the spread again. If the
average has moved outside that spread, something real changed and you have a short list of candidates.
If it has not, that was just the day.

Without pinning, every measurement mixes variance and drift and you can never separate them. You argue
from anecdote, which is where "we need a better model" comes from.

**Configuration does not make the system deterministic. It makes the system attributable.**

---

## Understanding check — and the answer

**The question.** A support-triage agent. On the 3rd the team upgraded to a newer model. On the 5th
somebody tightened two sentences in the system prompt. On the 9th a ticket-lookup plugin auto-updated.
On the 12th, misroutes are up by about a third. The prompt is in git; the model points at a moving
alias; the plugin version is unrecorded. Which can they investigate, which are they guessing about —
and if they had pinned everything perfectly, what would they *still* need?

**Answered correctly:** they would have to know what "misroutes" means before the 3rd.

That is the more important half. Configuration tells you what changed. It cannot tell you whether the
result got worse, because "up by about a third" compares to a number nobody wrote down. And "misroute"
must be defined tightly enough that two people counting the same tickets get the same figure, or the
metric moves when the counter's mood moves. That is what an eval is, and why Class 26 exists.
**Configuration makes inputs attributable; evals make outputs measurable.** Either alone leaves you
guessing.

**The mechanical half.** The prompt is investigable — diff it, revert it, re-run. The model is not: a
moving alias means they cannot establish what ran on the 3rd, on the 12th, or whether it changed again
on the 8th. "The upgrade on the 3rd" is not even a well-defined event, which is strictly worse than not
upgrading, because now they do not know what they have. The plugin is not investigable either, with no
recorded version to return to.

One of three is answerable. Two are permanent guesses. And the misroutes could be caused by none of
them — a shift in what customers wrote that fortnight produces the same graph.
