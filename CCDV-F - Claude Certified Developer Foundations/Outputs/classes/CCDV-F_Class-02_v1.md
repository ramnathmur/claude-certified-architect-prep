# Class 2 — What the Assistant Knows on Monday Morning

**Course:** Claude Certified Developer – Foundations
**Covers:** Claude Application Design (part 2 of 3) — session hygiene
**Built around:** Memory scope is a design-time decision about what survives the board being wiped.
Every scope trades token cost against reach, and choosing late costs far more than choosing early.
**Delivered:** 2026-08-20

---

Last class we said the blackboard gets rewritten from scratch before every sentence. Now the question
we did not ask.

What happens to the board when everybody goes home?

It gets wiped, and it does not come back. There is no board tomorrow. In fact there was never really a
board at all — there was a request, and a reply, and then nothing. The board is a thing your program
keeps rebuilding out of a transcript it is holding onto.

So if you want your agent to know something on Monday that it learned on Friday, somebody has to write
it down somewhere that is not the board.

That is the whole of what memory means here. It is not a feature you switch on. It is a decision about
what gets copied off the board before the board is wiped, and where you put the copy. And like most
decisions, it is cheap to make early and expensive to make late.

## Four ways of remembering a patient

Forget computers for a minute. Think about doctors, because doctors solved this problem a hundred years
ago and they solved it four different ways depending on the situation.

**You walk into an emergency room in a city you have never been to.** The doctor knows nothing about
you except what you tell them in the next ten minutes. They fix the thing. You leave. Nothing about you
is kept anywhere they will ever look again. That is a **stateless** agent — every job self-contained,
nothing carried in, nothing carried out.

**You go to your own GP.** Before you have sat down they have pulled your file. Everything from every
previous visit is there, written down at the time and read back before the appointment starts. That is
**external storage** — state kept outside the conversation, read in at the start of the next one.

**Now look at what is actually in that file.** It is not a transcript. Nobody wrote down every word of
every appointment. Somebody sat there afterwards and decided what was worth keeping, and wrote four
lines. That is **summarised memory**. It is much cheaper to carry, and it has exactly the failure you
would expect: if the thing that mattered was not judged worth writing down, it is gone — and worse,
nobody knows it is gone. The file looks complete.

**And the appointment itself**, the ten minutes where the doctor still has everything you have said in
their head — that is **in-context**. It works beautifully right up until you walk out the door.

That last one deserves a hard look, because people call it a memory strategy and it really is not.
In-context state does not survive a session ending. It does not survive a clear command. It is what you
get when you have not chosen anything yet. It is the appointment, not the file.

## What each one costs

Nothing here is free, and the costs are in different currencies, which is what makes the choice
interesting.

**In-context** has no retrieval cost at all — the state is already on the board, there is nothing to
fetch. But remember what the board is: everything on it gets re-sent on every turn. So the bill grows
with the length of the conversation, and it grows quadratically in the model's work rather than
linearly. And when the session ends you have nothing.

**External storage** loses nothing on the persistence side. It survives sessions, it can be shared
between several agents, it can move between users. What it costs is latency on every call that touches
it, plus the read-and-write code you now own forever. A database and a few hundred lines, which is not
hard — just not nothing.

**Summarised memory** is cheaper per session than replaying the whole history, and it is what you reach
for when the full history would outgrow the budget before the conversation is finished. What it costs
is whatever the summariser decided not to keep. That decision is made by a prompt you wrote, so a vague
summarisation prompt quietly drops task-critical state on every compression, forever, and silently.

**Stateless** costs nothing, because there is nothing to store or fetch. What it costs is that a
follow-up depending on anything from an earlier session simply cannot work.

## The agent that filled the window on session four

A team built an agent to help a support engineer work through escalation cases. In development it ran
beautifully. The developer would sit down, work a case in one continuous stretch, ten or fifteen turns,
and the in-context state held the whole history perfectly. It shipped. Nobody measured how many tokens
a session was actually using.

Then production, which had a different shape.

Each individual session was *shorter* than in development — an engineer would check in, ask a few
things, go away. But they came back the next day, and the next, on the same case. And the state kept
accumulating across those sessions.

By the fourth session the history being injected at the start ran to more than forty thousand tokens.
Before a single tool call. Add the system prompt and the tool schemas and the agent had burned over
forty-five thousand tokens of its budget before doing one useful thing. Then the tool calls started,
each adding its output to the board, and somewhere in the middle of the analysis the budget ran out.

From the outside, the agent started returning incomplete results. It would start an analysis and not
finish it. The team's first diagnosis was that it was picking the wrong tools.

It was never a tool problem. It was a memory architecture problem wearing a tool problem's clothes.

The fix was about an hour of work: pull the accumulated history out of the live context, put it in a
database, inject only the part each session needs.

## Why an hour of work is the expensive answer

The refactor is mechanical. A few hundred lines, a database the team already has. At design time it
would have been a slightly longer afternoon and nobody would remember it.

What it cost was *when*. That hour happened under production pressure, with users complaining and a
deadline already running, and it was not really an hour — the storage layer, the retrieval logic, what
to inject and what to leave out, all of those are decisions, and decisions made in a hurry with people
watching are worse decisions and slower ones.

Notice what let it happen: the shape of development was not the shape of production. One long session
against many short ones with state piling up between them. Those are different problems, and in-context
memory handles them completely differently. The developer had no way to see it, because their own usage
pattern hid it — the same blindness as Alex Morgan's laptop, in a different costume.

The habit that prevents it is dull and it works. Before choosing in-context, add up what a session will
actually contain — history, plus system prompt, plus tool schemas — and compare that number to the
window. Measure the real shape, not the one you use while building.

## How to choose

Ask these in order and it falls out.

**Does anything at all need to survive this session ending?** If no, you are stateless, and be glad —
it is the cheapest thing on the list and it has no failure modes. A document formatter that takes a
file, transforms it, returns it and terminates has nothing to remember. Do not give it memory it does
not need.

**If yes, it has to live outside the model.** There is no alternative. The board gets wiped, so anything
that survives, survives because you wrote it down. That is external storage.

**Is the full history too big to carry?** If the conversation would outgrow the budget before it is
finished, summarise before you store — and spend real care on the summarisation prompt, because that
prompt now decides what your agent is permanently allowed to know.

In-context is not in that ladder, because it is not an answer to the question. It is what covers you
*within* a session, which you get whether you choose it or not.

Two more things worth holding. State kept outside can be **shared** — between sessions, between users,
between several agents working the same case. State on the board is trapped in one conversation. And
the choice is not once and forever: an agent that starts stateless can grow into needing storage. What
you do not want is to discover that at three in the afternoon with a queue of complaints.

---

## Understanding check — and the answer given

**The question.** A team ships an agent helping an analyst work a quarterly financial close over several
days, the analyst returning each morning. Three weeks in, users report it "gets confused towards the
end" and "forgets what we agreed on Tuesday." The team's theory is that they need a more capable model,
and a budget request is being drafted. What is your theory, and what one number would you make them
produce first?

**Answered correctly:** they ran out of context window, not model capability.

**Worth adding.** The symptom of a full context window is indistinguishable from a model that is not
clever enough. Nothing errors, nothing crashes — the thing just gets vaguer and drops details, which is
exactly what "we need a better model" looks like from outside. That is why the wrong diagnosis is the
natural one.

The two complaints are actually two failures with one root. "Forgets Tuesday" is cross-session — that
state was never written down, so there was nothing to recall. "Gets confused towards the end" is
within-session — the board filled and the line that mattered got buried. One architectural fix removes
both.

**The number:** tokens at session start — history plus system prompt plus tool schemas — measured on a
session four or five days into a real close, not on a fresh one, because a fresh session is the shape
that hid the problem during development.

And before signing the budget request: check whether the more capable model even has a larger window.
Often it does not, and you would pay more per token to hit the same wall slightly later.
