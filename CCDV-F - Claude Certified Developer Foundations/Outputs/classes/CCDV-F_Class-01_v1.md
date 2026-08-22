# Class 1 — Whose hands

**Course:** Claude Certified Developer – Foundations
**Covers:** Claude Application Design (part 1 of 3)
**Built around:** Claude is text-in, text-out, running on someone else's computer. An instruction is
text you got into a finite window; a capability is whatever the machine at the far end can touch.
**Delivered:** 2026-08-20

---

## The surgeon on the video link

A surgeon in Boston operates on a patient in Nairobi. She is on a video link. Her hands are in Boston
and they stay in Boston for the entire procedure — at no point does any part of her enter that theatre.
What happens in Nairobi happens because she says "clamp" and somebody there closes a clamp.

Now vary one thing and only one thing: who is holding the instruments in Nairobi.

If it is your surgical team, in your hospital, using your tray, then "clamp" reaches for your clamp. If
it is a robot arm in *her* building with a standard-issue tray, "clamp" still works — there is still a
clamp — but it is not your clamp, and your tray is five thousand miles away connected to nothing.

That is the entire architecture of building on Claude. Notice what did not change between those two
cases. The surgeon did not move. She was never in the room.

## Claude is never in the room

The weights sit on Anthropic's accelerators in Anthropic's data centre. Your program's whole
relationship with Claude is an HTTPS request carrying text out and text coming back. That is the
interface, all of it.

This holds when you run Claude Code in your terminal. It feels local — files open, tests run, your disk
changes — and none of that is Claude touching anything. What is on your machine is a *harness*: a
program that receives a tool-call request over the wire, executes it with your machine's hands, and
reports back what happened, as text. Claude asked. Your computer did it.

So there is exactly one variable across every way you can build on this platform:

> **Who is holding the hands, and what can those hands reach?**

Hold that and you can derive cases this class never covers. Take it on faith and you will memorise a
table.

## The whiteboard rewritten before every sentence

Second physical fact. Everything about where instructions live falls out of it.

The API keeps no memory between calls. None. Each request is complete in itself — your entire
conversation is serialised and sent again, from the top, every turn. A forty-turn conversation means
turn forty is one request containing all forty turns.

Picture a whiteboard of fixed size that has to be rewritten from scratch before every sentence anyone
says. That is not a metaphor for the context window. It is a description of it.

Two consequences worth more than any rule:

**Anything permanently lettered in the corner of that board shrinks the board for every sentence,
forever.** It is not a one-time cost paid at setup. It is rent, charged on every turn.

**The board is finite for a reason, and the reason is not storage.** Attention compares every token
against every other token, so the work grows faster than the text does. And a longer board is a harder
board to find one sentence on. Filling it costs money and costs the model's ability to locate what
matters.

Every instruction you write is therefore a claim on a scarce, repeatedly repurchased resource. From
here the design of the whole instruction system is something you could have invented yourself.

## Where instructions live, and why there are exactly these options

You have forty sets of instructions and a board that fits maybe one of them comfortably. What do you
do?

You do what a reference library does. The catalogue stays in the room — one name, one line each, thirty
tokens apiece, forty of them fitting on about a page. The books stay on the shelf, costing nothing
until somebody wants one. When a book is wanted it gets fetched, and only then does it take space on
the table.

That is a **skill**: a `SKILL.md` file with a name, a description and a body. The name and description
are the catalogue entry — always resident, always cheap. The body sits on disk and enters the window
only when wanted. The pattern is called progressive disclosure, and it is the most elegant idea in this
subject because it is a direct answer to a hard physical limit.

Against that, some things genuinely are relevant to every task in a repository — the language version,
the conventions, the directories nobody touches. Those go in **`CLAUDE.md`**, which loads
unconditionally into every session. It is lettered in the corner of the board. That is the right trade
when the content applies to everything, and a bad trade the moment it does not, because a bloated
`CLAUDE.md` does not only cost tokens. It competes for attention with the task.

**Typed into the conversation** is the third option, worth understanding mechanically rather than as a
category. Why does something you typed last as long as the conversation? Not because it is stored
anywhere. Because your client retypes it into every request. Why is it gone when the session ends?
Because nothing was ever kept. There is no state to lose.

## Why the description is the only thing that matters

There is no matcher. No keyword index, no similarity search, no routing table, no component whose job
is deciding which skill applies. The catalogue is plain text sitting in the prompt alongside your
request, and Claude does the only thing it ever does — predict the next move from what it can see.
Given your message and forty one-line entries, the likeliest next move is a request to read whichever
entry reads as though it were written for a request like yours.

Once you see that, the rule stops being advice and becomes unavoidable. **The description works alone.**
The body cannot argue for itself, because at the moment of the decision nothing has read the body. It
is not in the room.

So write the sentence somebody would say out loud at the moment they would want this skill — *"when
reviewing a pull request that touches database migrations"* — rather than the summary you would write
after reading the body. A librarian who shelves the migrations book under "Assorted Engineering Topics"
has not lost it. Anyone who needs it simply never has a reason to walk to that shelf.

Expect this to be probabilistic, because it is. A good description makes loading likely, never certain.
When a skill does not fire and you go hunting for the broken lookup, you will hunt for a long time —
nothing broke, a judgment went the other way, and the fix lives in that one sentence rather than in the
plumbing.

## The four surfaces, derived

Go back to the surgeon and ask the only question: whose hands?

**Claude Code in your terminal.** The harness is a program on your machine, so the hands are yours, on
your disk, with your tools. Instructions are found by looking in `.claude/skills` — a place on your
disk, which your harness can obviously read. Your own operating theatre.

**The Agent SDK.** The same engine running as a library inside a program *you* wrote, which might be a
web service with no repository anywhere near it. So it will not sweep files off disk into your prompts
unless you say so. You turn that on with `settingSources`, explicitly. A library that silently read the
host filesystem would be a defect. The hands are still yours; you hand over the keys deliberately.

**The Messages API, called from a service.** Ask where a skill's body would have to live to be readable
at the moment of the decision. The decision happens on Anthropic's side of the wire, so the filesystem
a skill sees is the filesystem next to the model, and Anthropic operates that machine. It is a
standard-issue container.

There is a stronger reason than topology. Even if Anthropic wanted to hand that container your disk,
there is no channel. Your request went *outbound* to `api.anthropic.com`. The container has no route
back through your network, no credentials, no address for you. And it must not have one, because the
moment such a route exists, some Anthropic-run container can reach some customer's filesystem, and the
boundary that lets a bank and a two-person startup share the same inference fleet is gone.

**A hosted agent that Anthropic runs.** The same container logic plus one addition: it persists. You
reach it by an agent ID and it is still there next session. Anthropic operates the whole theatre, robot
arm and tray, and keeps it between procedures.

Four surfaces, one variable. A skill that works in your terminal and shells out to
`./scripts/lint-diff.sh` will move to the Messages API, load perfectly, and fail — because you wrote
instructions for your own tray and handed them to a robot arm in another country.

## The subagent: two rules, two different reasons

When you delegate to a subagent it starts with no conversation history. It has only the skills its own
configuration lists — nothing arrives by inheritance. And it runs with the parent's permission scope.

Those two facts have reasons of entirely different kinds.

**The blank context is the product.** You delegate *because* the board is finite and shared. If the
child inherited the parent's transcript you would have paid for those tokens twice and bought nothing —
a second, more expensive copy of the same conversation. Delegation earns its keep precisely because the
child starts empty: it can spend sixty thousand tokens reading files and hand back three hundred tokens
of conclusion, and the parent's board absorbs three hundred. Context isolation is the entire good being
purchased.

**Inherited authority is close to forced.** If a child could hold rights its parent lacked, spawning a
subagent would be a privilege-escalation primitive — anything that persuaded the model to call for a
helper would get a fresh, more powerful agent for free. A delegate never exceeds its delegator. Same
rule as a power of attorney, which cannot grant more authority than the grantor holds. The child is not
a new principal. It is you, in a second room, still wearing your badge.

The asymmetry is where the incidents come from. **Context does not travel; authority does.** Missing
knowledge fails closed — a child without a skill produces visibly mediocre work and you notice.
Inherited authority fails open — a child that arrived with a destructive permission and *without* the
cautionary rules that lived in the parent's `CLAUDE.md` can do damage the parent would have refused.
The guardrails stayed behind. The capability walked through the door.

## Alex Morgan's laptop

A developer wrote a deployment workflow as a skill, bundled it with hooks into a plugin, tested it
locally, and shipped it to the team through an internal marketplace. Every teammate's install
succeeded. Every teammate's run failed.

The skill file carried a command pointing at `/Users/alexmorgan/projects/deploy-utils/validate.sh`.
That directory existed on exactly one machine on earth. A second skill in the same bundle read an
environment variable, `DEPLOY_TOKEN`, that Alex had set in a shell profile years earlier and never
thought about again. Nothing in the package mentioned it. Three people spent two hours finding that
one.

The principle underneath is **late binding**, and it generalises far past plugins. A path written in a
file is an unresolved reference — a promise that some name will mean something later. Copying bytes
resolves nothing. Resolution happens at run time, against a namespace that exists on one particular
machine. Install and run are different events, and the gap between them is where every assumption you
did not know you had made comes due.

The remedies follow directly:

- Reference paths **relative to the project root**, never absolutely.
- `$CLAUDE_PROJECT_DIR` for scripts kept in the project; `${CLAUDE_PLUGIN_ROOT}` for scripts bundled
  inside the plugin. Two variables because there are two different "heres" — the repository someone is
  working in, and the package your skill shipped inside. If your plugin's own script is the thing you
  are calling, it is `${CLAUDE_PLUGIN_ROOT}`.
- Document and **validate every environment variable at install time**, so a missing one announces
  itself immediately instead of two hours into somebody's afternoon.
- **Install once on a clean machine** before handing it to anybody.

Alex had no way to see any of this. That machine satisfied every assumption Alex had made, so the
testing confirmed nothing. Local verification is structurally blind to environmental assumptions — you
cannot test for the presence of something that is always present.

## What is forced and what is just this release

Worth separating, because they deserve different amounts of memory.

**Close to physics.** The model runs on Anthropic's hardware and never on yours. The API is stateless.
The window is finite and re-read every turn. A delegate cannot exceed its delegator. The container has
no route back to your network. These will still be true in five years and you can reason from them.

**This release's conventions.** That the file is spelled `CLAUDE.md`. That skills live in
`.claude/skills`. That the SDK's filesystem sources default to off. That the variables are
`$CLAUDE_PROJECT_DIR` and `${CLAUDE_PLUGIN_ROOT}`. Learn them, because the exam names mechanisms in its
options and you have to recognise them — but hold them as vocabulary, not as principle.

---

## Understanding check

A team keeps its coding standards in `CLAUDE.md` and gets good, consistent results in the terminal.
They move the same workflow into a scheduled overnight job on the Agent SDK, pointed at the same
repository. The output comes back ignoring several of those standards — **not always, but often enough
to notice.**

1. What do you check first?
2. What does the intermittency tell you? If a file simply never loads, the standards would be missing
   every night rather than most nights.
