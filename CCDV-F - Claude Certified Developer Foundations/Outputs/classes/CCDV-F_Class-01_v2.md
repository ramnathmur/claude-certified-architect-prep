# Class 1 — You Can't Reach Through a Telephone

**Course:** Claude Certified Developer – Foundations
**Covers:** Claude Application Design (part 1 of 3)
**Built around:** Claude is text in, text out, running on somebody else's machine. An instruction is
text you got onto a blackboard that's only so big. A capability is whatever the person on the other end
of the phone has within arm's reach.
**Version:** v2, rewritten 2026-08-20 in plain language. Supersedes v1.

---

I want to start with a picture, and I want to spend real time on it, because if you get this picture
right then about six things you'd otherwise have to memorise turn out to be the same thing looked at
from different sides.

## Where is the thing you're talking to?

Not in the room with you.

Claude runs on machines in Anthropic's data centre. Not on your laptop, not on your server, not
anywhere you can point at. When your program uses Claude, here is the whole of what physically happens:
some text goes out over the internet, and some text comes back. Out, and back. There is no other part
to it.

Now you're going to object, and it's a good objection, because everybody makes it. You've sat there and
watched Claude Code work in your terminal. It opened your files. It changed them. It ran your tests and
read the output. You watched it happen with your own eyes. So it must be on your machine.

It isn't. And what really happened is more interesting than what you thought happened.

There's a small program running on your laptop — the thing you started when you typed `claude`. Call it
the harness, which is what everyone calls it. That little program is the one on the phone, and it's the
one with hands.

Claude sends back a piece of text that says, more or less, "I'd like to open the file at
`src/main.py`." Now look carefully at what that is. It isn't an action. It's a sentence. It's a request,
written down, and it arrives the same way every other piece of text arrives.

The harness reads that request. It decides whether to allow it. If it allows it, *the harness* opens
the file — your computer, your disk, your permissions — and then types the contents back down the
phone.

So Claude never touched your file. Your own computer touched your file, because Claude asked it to.

You can't reach through a telephone. Not even a very good telephone.

Hold onto that, because everything left in this class is one question: **who's on the other end of the
phone, and what have they got within arm's reach?**

## The second thing, which is about memory

This one is stranger than the first.

Claude doesn't remember your last message.

I don't mean it forgets. Forgetting means you had something and lost it. It never had it. Every request
that goes over the wire is complete in itself, and between requests nothing is kept. Nothing at all.

So how do you have a conversation with it? Your program cheats. Every time you send a new message, it
sends the entire conversation again, from the very first line. Turn forty is one enormous request
containing all forty turns.

Picture a blackboard. Before anybody says a single sentence, somebody wipes the board clean and
rewrites everything that's been said so far, from the beginning. Then the next sentence gets said. Then
they wipe it and write the whole thing out again, including the new bit. Every sentence. All the way
through.

That isn't an analogy for how it works. That's how it works.

Two things follow, and between them they decide everything about where you put your instructions.

**First: anything you write permanently in the corner of that board, you pay for on every sentence.**
Not once, when you set it up. Every time. It's rent, not a purchase.

**Second: the board is only so big.** And you should ask why, because the answer isn't "they ran out of
chalk." When the model reads the board it doesn't go left to right the way you do — it weighs every
word against every other word. Double the words and you've roughly quadrupled the work. There's a
second cost too, and it's the one you feel: the more junk on the board, the harder it is to find the
one line that actually mattered. A crowded board makes the thing dumber, not just slower.

## So where do you put your instructions?

Now you have a real problem, and I want you to feel the problem before I hand you the answer.

You've got forty different sets of rules you'd like followed. Coding standards. A review checklist. How
this team writes migrations. The house format for a report. Written out in full they'd fill the board
and leave no room for the actual work.

So you can't have them all up there. But you don't know in advance which one you'll need.

What do you do in a library? A library has a hundred thousand books and nobody can carry a hundred
thousand books. So the library keeps a card catalogue. One card per book — the title, one line about
what's inside. The cards are tiny. The whole catalogue fits in one room. And the books sit on the
shelves doing nothing at all until somebody actually wants one.

That's the trick, and it's exactly the trick. They call it a **Skill**. It's a file, `SKILL.md`, with a
name, one sentence saying what it's for, and then the whole body of instructions underneath.

The name and the sentence go on the board. Thirty words or so each — forty of them fit in about a page.
The body stays on the disk costing you nothing. And when Claude decides it wants one, it goes and
fetches that one body, and only then does it land on the board.

The name for this is progressive disclosure. Notice it isn't a clever trick somebody dreamed up. It's
forced. The board is finite, so you need a catalogue. You'd have invented it yourself if you'd sat down
with the problem for ten minutes.

Now, some things really are relevant to every job in a repository — the language version, the
conventions, the directories nobody's allowed to touch. Those go in a file called **`CLAUDE.md`**, and
that one loads into every session whether you need it or not. It's the stuff written permanently in the
corner. That's the right trade when it genuinely applies to everything, and a bad trade the moment it
doesn't, because a bloated `CLAUDE.md` doesn't just cost you money — it's more junk competing with the
actual question.

And the third place is just **typing it into the conversation**. Worth understanding mechanically
rather than as a category. Why does something you typed stay around for the whole conversation? Not
because it's stored anywhere — because your program retypes it into every request. Why is it gone when
the session ends? Because nothing was ever kept. There's no state to lose.

## Here's the part almost everybody gets wrong

How does Claude pick which card?

You're imagining machinery. Something that takes your request, looks at the forty descriptions, works
out which one matches best, and picks a winner. An index. A search. A lookup.

There isn't one. There's no such machinery anywhere in the system.

The card catalogue is written on the blackboard, in plain words, sitting right next to your question.
And Claude does the only thing it ever does: it looks at everything on the board and works out what the
likeliest next move is. Given your question and forty little cards, the likeliest next move is asking
for whichever card sounds like it was written for a question like yours.

That's a judgment. Not a lookup.

And now the rule about descriptions stops being advice and becomes something you can't avoid: **the
description does all the work, by itself.** The instructions in the body can't help it. At the moment
the decision gets made, nobody has read the body. It isn't on the board. As far as that decision is
concerned, it doesn't exist.

So when you write that one sentence, write the thing somebody would actually say out loud at the moment
they'd want it. *"When reviewing a pull request that touches database migrations."* Not *"Database
migration review guidelines."* The first sounds like a question somebody asks. The second sounds like a
label on a filing cabinet.

A librarian who files the migrations book under "Assorted Engineering Topics" hasn't lost it. It's
right there on the shelf, perfectly intact. It's just that nobody who needs it will ever have a reason
to walk to that shelf.

One more thing, because it saves you an afternoon. This is a guess, so sometimes it guesses wrong. When
your skill doesn't fire and you go hunting for the broken lookup, you'll hunt for a very long time.
Nothing's broken. A judgment went the other way, and the fix lives in that one sentence, not in the
plumbing.

## Four phones, one question

Back to the telephone. Who's on the other end, and what have they got within reach?

**You're running Claude Code in your terminal.** The harness is on your laptop. Your hands, your disk,
your tools. So where would you keep a skill? On your disk, obviously — a folder called
`.claude/skills`, because the harness is sitting right there and can read it.

**You're using the Agent SDK.** Same engine, but now it's a library living inside a program *you* wrote,
and your program might be a web service on a machine with no repository anywhere near it. So should it
go rummaging around the filesystem and stuff whatever it finds into your prompts? Of course not — that
would be a defect. So it doesn't, unless you tell it to. You tell it with a setting called
`settingSources`. That's not a gotcha to memorise. That's a library minding its own business.

**You're calling the Messages API from a service.** Stop and think about where a skill's body would have
to be for anybody to read it. The decision about which skill to load happens over there, on Anthropic's
side of the wire. So the body has to be over there too. And whose machine is over there? Theirs. So
it's a standard container of theirs, which has never seen your laptop.

There's a harder reason as well, and it's better than the first one. Even if Anthropic wanted to hand
that container your disk, there's no wire to do it on. Your program dialled out to them; they never
dialled in to you. No address, no route back through your firewall, no credentials. And there had
better not be one — because the moment there is, some container in their data centre can reach some
customer's files, and the whole arrangement that lets a bank and a two-person startup share the same
machines falls apart.

**A hosted agent that Anthropic runs for you.** Same container story, with one addition: they keep it.
You call it by an ID and it's still there tomorrow.

So take a skill you wrote in your terminal, one that runs `./scripts/lint-diff.sh`. Move it to the
Messages API. It'll load perfectly. Then it'll die — because you wrote instructions for your own
toolbox and handed them to somebody in another country who's never seen it.

Here's the whole thing on one card, now that you've reasoned it out:

| On the phone with | Who has hands | Where the instructions come from |
|---|---|---|
| Claude Code, your terminal | You, on your disk | `.claude/skills` on your machine |
| Agent SDK, your program | You, if you said so | Your filesystem, once `settingSources` says to |
| Messages API, from a service | Anthropic's container | Enabled on the request; nothing of yours is reachable |
| A hosted agent | Anthropic's container, kept between sessions | Declared in the agent itself |

## The helper who walks in

Now, subagents. When you hand a job off to one, two things are true, and people file them together
under "surprising." They aren't the same kind of fact at all, and one of them will hurt you.

The subagent starts with an empty head. No conversation history. It doesn't inherit your skills either —
it gets only what its own configuration lists.

But it runs with your permissions.

Take the empty head first. That isn't a limitation, it's the entire thing you're buying. Why did you
delegate in the first place? Because the board is only so big and you didn't want to fill it. If the
helper walked in carrying a copy of your whole conversation, you'd have paid for all that text a second
time and got nothing for it. The point is that the helper starts clean — it can go and read sixty
thousand tokens' worth of files in its own room, think it over, and hand you back three sentences. Your
board only ever absorbs the three sentences. The empty head *is* the deal.

Now the permissions, and ask why they must carry over. Suppose they didn't. Suppose a helper could hold
powers you don't. Then "send a helper" becomes a way of getting powers you don't have — anybody who
could talk the system into calling for one would get a free upgrade. So it can't work that way. Someone
you send on an errand can't do things you aren't allowed to do. It's a power of attorney: you can't
hand over more authority than you've got. The helper isn't a new person. It's you, in another room,
still wearing your badge.

And here's the bit that gets missed. **The knowledge doesn't travel. The authority does.** Those two
fail in opposite directions. If the helper's missing some knowledge, you find out — the work comes back
mediocre and somebody notices. If the helper's carrying your permissions but *not* the warnings that
lived in your `CLAUDE.md`, the "never touch the production database" sort of rule, then it can go and do
something you'd have refused. The brakes stayed home. The engine went.

## Alex Morgan's laptop

A fellow wrote a deployment routine as a skill, wrapped it in a plugin, tested it on his own machine,
and shipped it to his team through their internal marketplace. Everybody's install worked. Nobody's run
worked.

Inside the skill was a line pointing at `/Users/alexmorgan/projects/deploy-utils/validate.sh`.

Think about what that line actually is. It isn't a file. It's *directions* to a file. It's somebody
saying "go down the hall, second door on the left." And directions only work if you're standing where
the person who wrote them was standing.

Alex was standing in the right place. Nobody else was.

Now here's the thing that nobody notices until it bites. When you install a package, nobody checks the
directions. Installing copies the paper, and copying the paper tells you nothing about whether the hall
exists or the door is where it says. You find that out later, when somebody tries to walk it — and by
then they're in a different building.

They call this late binding, if you want the term. All it means is that the words get written down now
and looked up later, and "later" happens somewhere else.

There was a second failure in the same package and it's the nastier kind. One of the skills used an
environment variable, `DEPLOY_TOKEN`. Alex had set it in his shell profile years earlier and completely
forgotten about it. It wasn't in the README. Nothing in the package mentioned it at all. Three people
spent two hours chasing that one down.

And this is the part to take away: Alex could not have caught either of these by testing. His machine
had the folder. His machine had the variable. Every test passed, and every test was meaningless,
because you can't test for the absence of something that's always there.

So, the habits, and they follow straight from that:

Don't write absolute paths. Write them relative to the project. When you need to point at a script,
there are two variables for it, and they exist because there are two different meanings of "here."
`$CLAUDE_PROJECT_DIR` means the project somebody's working in. `${CLAUDE_PLUGIN_ROOT}` means the
package your skill shipped inside. If the script came in the box with your plugin, it's the second one.

Write down every environment variable you depend on, and check for it at install time, so a missing one
shouts immediately instead of waiting to trip somebody up halfway through a deploy.

And install it once on a clean machine before handing it to anybody. That's the only test that means
anything, because it's the only one where your own assumptions aren't quietly holding things up.

## What's real, and what somebody just decided one Tuesday

Last thing, and it's a habit worth keeping for the whole course, because it tells you where to spend
your memory.

Some of what I've told you is close to physics. It'll be true in five years and you can reason from it:
the model runs on their machines and never on yours; nothing is remembered between calls; the board is
finite and gets rewritten every time; a helper can't hold more authority than whoever sent it; there's
no wire from their container back to your laptop.

And some of it is just how they've set it up this year: that the file is called `CLAUDE.md`; that
skills live in `.claude/skills`; that the SDK's filesystem setting starts off; that the variables are
spelled `$CLAUDE_PROJECT_DIR` and `${CLAUDE_PLUGIN_ROOT}`.

Learn that second list, because the exam will put those names in front of you and you'll need to
recognise them. But don't mistake them for the first list. From the first list you can work things out.
The second list is vocabulary, and somebody could change it next quarter.

---

## Before we go on

A team keeps its coding standards in `CLAUDE.md`. In the terminal it works fine — good, consistent
results, day after day. Then they take the same workflow and run it as a scheduled overnight job using
the Agent SDK, pointed at the same repository. Now the output comes back ignoring several of those
standards. Not every night. But often enough that somebody noticed and complained.

Two questions.

What's the first thing you'd check?

And then the harder one: what does it tell you that it's *intermittent*? If the file simply never
loaded, you'd expect the standards to be missing every single night, not most nights. So something else
is going on, or something else is going on as well.
