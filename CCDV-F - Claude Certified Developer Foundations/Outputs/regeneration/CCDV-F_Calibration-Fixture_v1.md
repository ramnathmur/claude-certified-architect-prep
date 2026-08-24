# CCDV-F Prose Gate — Calibration Fixture v1

**Purpose.** A cheaper stand-in for `Outputs/classes/html/CCDV-F_Class-01.html` when running the
calibration control specified in `CCDV-F_Prose-Gate_v1.md` §3.5. That control exists to confirm a
reviewer agent can still correctly fail known-bad prose before its verdict on a real chapter is
trusted — it is testing the reviewer, not the fixed input.

**Why this file exists.** The full class file is 1,193 lines / 66,209 bytes, of which 305 lines are a
`<style>` block and 66 lines are a `<script>` block — 371 lines (31%) with zero prose content, read in
full by every calibration run under the original instruction. Of the remaining ten teaching screens,
five (screens 1, 2, 3, 4 and 8, by the gate document's own screen numbering) already contain a verified
instance of every defect class the control requires: C1, C2, C3, C4, C6 and C7. Screens 5, 6, 7, 9 and
10 add no defect type the other five do not already carry. Cutting the file to those five screens and
stripping markup that carries no prose (`<svg>` diagram bodies, nav buttons, `<div>`/`<span>` wrappers)
gives a fixture that reproduces the same required verdict at roughly a quarter of the original line
count, with no cherry-picked or isolated sentences — every screen kept is intact, contiguous, real
chapter prose, not a quote pulled out of context.

**Extracted:** 2026-08-23, from `Outputs/classes/html/CCDV-F_Class-01.html`, screens 1, 2, 3, 4 and 8 —
`<section class="screen">` blocks beginning `"Where is the thing you're talking to?"`,
`"The board that gets rewritten before every sentence"`, `"So where do you put your instructions?"`,
`"The part almost everybody gets wrong"`, and `"What's real, and what somebody just decided one
Tuesday"`. Figure captions, tables and paragraph structure preserved verbatim; `<style>`, `<script>`,
`<svg>` diagram markup and navigation buttons removed as carrying no prose signal.

**Verified stats on this fixture** (recomputed 2026-08-23, not carried over from the gate document's
original corpus scan): 2,054 words, 22 em-dashes → 10.4 per 1,000 words, more than double the C2
ceiling of 5 per 1,000 and consistent with the full file's own 11.2–12.9 per 1,000 (the two figures
differ because the extraction methods count differently, not because the density changed). A reviewer
applying C2 to this fixture alone, without reference to the full file, will still measure a clear
excess.

**What this fixture is not for.** It is a calibration input only — confirming the *reviewer* still
catches known-bad prose. It is not a substitute source for the gate document's own §1 defect catalogue
or §3.4 worked demonstration, both of which cite the full class file directly, and it is not a source
of quotable "good prose" examples — see the gate document's own §2 for those.

---

01 · The wire
<h2>Where is the thing you're talking to?</h2>
<p class="entry"><b>By the end of this screen</b> you'll be able to say exactly what happened when
Claude Code edited a file on your disk — and it isn't what it looks like.</p>

<p>Not in the room with you.</p>

<p>Claude runs on machines in Anthropic's data centre. Not on your laptop, not on your server, not
anywhere you can point at. When your program uses Claude, here is the whole of what physically
happens: some text goes out over the internet, and some text comes back. Out, and back. There is
no other part to it.</p>

<p>Now you're going to object, and it's a good objection, because everybody makes it. You've sat
and watched Claude Code work in your terminal. It opened your files. It changed them. It ran your
tests and read the output. You watched it happen with your own eyes. So it must be on your
machine.</p>

<p>It isn't. And what really happened is more interesting than what you thought happened.</p>

<figure>
<figcaption><b>The model has no hands on any surface.</b> Only text crosses the wire, in both
directions — so every change to your disk was made by a program on your own machine, acting
on a request.</figcaption>
</figure>

<p>There's a small program running on your laptop — the thing you started when you typed
<code>claude</code>. Call it the <strong>harness</strong>, which is what everyone calls it. That
little program is the one on the phone, and it's the one with hands.</p>

<p>Claude sends back a piece of text that says, more or less, <em>"I'd like to open the file at
<code>src/main.py</code>."</em> Now look carefully at what that is. It isn't an action. It's a
sentence. It's a request, written down, and it arrives the same way every other piece of text
arrives.</p>

<p>The harness reads that request. It decides whether to allow it. If it allows it, <em>the
harness</em> opens the file — your computer, your disk, your permissions — and then
types the contents back down the phone.</p>

<p>So Claude never touched your file. Your own computer touched your file, because Claude asked
it to.</p>

<p class="pull">You can't reach through a telephone. Not even a very good telephone.</p>

<p class="exit"><b>Carry this forward.</b> Everything left in the class is one question:
<em>who's on the other end of the phone, and what have they got within arm's reach?</em></p>

---

02 · Memory
<h2>The board that gets rewritten before every sentence</h2>
<p class="entry"><b>By the end of this screen</b> you'll know why a long conversation costs more
than a short one — and why the limit isn't about storage.</p>

<p>This one is stranger than the first.</p>
<p><strong>Claude doesn't remember your last message.</strong></p>
<p>I don't mean it forgets. Forgetting means you had something and lost it. It never had it. Every
request that goes over the wire is complete in itself, and between requests nothing is kept.
Nothing at all.</p>
<p>So how do you have a conversation with it? Your program cheats. Every time you send a new
message, it sends the entire conversation again, from the very first line. Turn forty is one
enormous request containing all forty turns.</p>

<figure>
<figcaption><b>The cost of a conversation is not the last message — it is every message, every
time.</b> Which is why anything you pin permanently into that request is charged again on every
turn that follows.</figcaption>
</figure>

<p>Picture a blackboard. Before anybody says a single sentence, somebody wipes the board clean and
rewrites everything that's been said so far, from the beginning. Then the next sentence gets said.
Then they wipe it and write the whole thing out again, including the new bit. Every sentence. All
the way through.</p>
<p>That isn't an analogy for how it works. That's how it works.</p>

Two consequences worth more than any rule
<p><strong>Anything written permanently in the corner of that board is paid for on every
sentence.</strong> Not once, at setup. Every time. It's rent, not a purchase.</p>
<p><strong>The board is only so big</strong> — and the reason isn't
that they ran out of chalk. When the model reads the board it doesn't go left to right the way
you do; it weighs every word against every other word. Double the words and you've roughly
quadrupled the work. There's a second cost too, and it's the one you feel: the more junk on the
board, the harder it is to find the one line that mattered. A crowded board makes the thing
dumber, not just slower.</p>

<p class="exit"><b>Next.</b> You've now got a hard physical limit and a pile of instructions you'd
like followed. Those two facts are about to collide, and the design of the whole instruction
system falls out of the collision.</p>

---

03 · The library
<h2>So where do you put your instructions?</h2>
<p class="entry"><b>By the end of this screen</b> you'll be able to derive the three homes for
instructions rather than memorise them — and say what each one costs.</p>

<p>Now you have a real problem, and I want you to feel the problem before I hand you the answer.</p>
<p>You've got forty different sets of rules you'd like followed. Coding standards. A review
checklist. How this team writes migrations. The house format for a report. Written out in full
they'd fill the board and leave no room for the actual work.</p>
<p>So you can't have them all up there. But you don't know in advance which one you'll need.</p>
<p>What do you do in a library? A library has a hundred thousand books and nobody can carry a
hundred thousand books. So the library keeps a card catalogue. One card per book — the title,
one line about what's inside. The cards are tiny. The whole catalogue fits in one room. And the
books sit on the shelves doing nothing at all until somebody actually wants one.</p>

<figure>
<figcaption><b>Progressive disclosure is forced, not clever.</b> Given a finite board and an
unknown-in-advance need, a catalogue is the only design that works — you would have invented
it yourself after ten minutes with the problem.</figcaption>
</figure>

<p>That's the trick, and it's exactly the trick. They call it a <strong>Skill</strong>. It's a file,
<code>SKILL.md</code>, with a name, one sentence saying what it's for, and then the whole body of
instructions underneath. The name and the sentence go on the board; the body stays on disk costing
you nothing, and gets fetched only when Claude decides it wants it.</p>

<p>Now, some things really <em>are</em> relevant to every job in a repository — the language
version, the conventions, the directories nobody's allowed to touch. Those go in
<code>CLAUDE.md</code>, which loads into every session whether you need it or not. That's the stuff
written permanently in the corner. Right trade when it genuinely applies to everything, bad trade
the moment it doesn't — because a bloated <code>CLAUDE.md</code> doesn't just cost money, it's
more junk competing with the actual question.</p>

<p>And the third place is just <strong>typing it into the conversation</strong>. Worth understanding
mechanically rather than as a category. Why does something you typed stay around for the whole
conversation? Not because it's stored anywhere — because your program retypes it into every
request. Why is it gone when the session ends? Because nothing was ever kept. There's no state to
lose.</p>

Checkpoint
<p>Your team has a 40-line checklist that applies only when someone touches the payments module.
Where does it go, and what would putting it in the wrong place cost you?</p>
<p>A <strong>Skill</strong> — it applies to some tasks, not all of them. Put it in
<code>CLAUDE.md</code> and you pay for all 40 lines on every turn of every session in the
repository, including the hundreds that never go near payments. And you pay twice: once in
tokens, and once in the dilution of every other instruction on the board.</p>

<p class="exit"><b>Next.</b> The catalogue only works if the right card gets picked. So how does
Claude choose? The answer is not what almost everyone assumes, and getting it wrong sends people
hunting for a bug that doesn't exist.</p>

---

04 · There is no matcher
<h2>The part almost everybody gets wrong</h2>
<p class="entry"><b>By the end of this screen</b> you'll know why a skill that never loads is not a
broken skill — and where the fix actually lives.</p>

<p>How does Claude pick which card?</p>
<p>You're imagining machinery. Something that takes your request, looks at the forty descriptions,
works out which one matches best, and picks a winner. An index. A search. A lookup.</p>
<p><strong>There isn't one.</strong> There's no such machinery anywhere in the system.</p>
<p>The card catalogue is written on the blackboard, in plain words, sitting right next to your
question. And Claude does the only thing it ever does: it looks at everything on the board and
works out what the likeliest next move is. Given your question and forty little cards, the
likeliest next move is asking for whichever card sounds like it was written for a question like
yours.</p>

<p class="pull">That's a judgment. Not a lookup.</p>

<p>And now the rule about descriptions stops being advice and becomes something you can't avoid:
<strong>the description does all the work, by itself.</strong> The instructions in the body can't
help it. At the moment the decision gets made, nobody has read the body. It isn't on the board. As
far as that decision is concerned, it doesn't exist.</p>

<table>
<thead><tr><th>Written as&hellip;</th><th>Reads like</th><th>Result</th></tr></thead>
<tbody>
<tr><td>"When reviewing a pull request that touches database migrations"</td>
    <td>A question somebody asks out loud</td>
    <td>Matches the moment somebody asks it</td></tr>
<tr><td>"Database migration review guidelines"</td>
    <td>A label on a filing cabinet</td>
    <td>Nobody has a reason to walk to that shelf</td></tr>
</tbody>
</table>

<p>A librarian who files the migrations book under "Assorted Engineering Topics" hasn't lost it.
It's right there on the shelf, perfectly intact. It's just that nobody who needs it will ever have
a reason to walk to that shelf.</p>

This saves you an afternoon
<p>It's a guess, so sometimes it guesses wrong. When your skill doesn't
fire and you go hunting for the broken lookup, you'll hunt for a very long time. Nothing's
broken. A judgment went the other way, and the fix lives in that one sentence, not in the
plumbing.</p>

<p class="exit"><b>Next.</b> Back to the telephone — and this time we use it to derive all
four surfaces from a single question.</p>

---

*[Screens 5, 6 and 7 — "Four phones, one question", "The helper who walks in", "Alex Morgan's
laptop" — omitted. Verified during extraction to add no defect type beyond what screens 1–4 and 8
already carry.]*

---

08 · Where to spend your memory
<h2>What's real, and what somebody just decided one Tuesday</h2>
<p class="entry"><b>By the end of this screen</b> you'll have a habit worth keeping for all
twenty-nine classes: sorting what you can reason from against what you must simply
recognise.</p>

<p>Some of what I've told you is close to physics. It'll be true in five years, and you can work
things out from it. Some of it is just how they've set it up this year.</p>
<p>Treating both with the same reverence teaches you to spend memory in the wrong places.</p>

<table>
<thead><tr><th>Close to physics — reason from it</th><th>This release's convention — recognise it</th></tr></thead>
<tbody>
<tr><td>The model runs on their machines and never on yours</td>
    <td>The file is called <code>CLAUDE.md</code></td></tr>
<tr><td>Nothing is remembered between calls</td>
    <td>Skills live in <code>.claude/skills</code></td></tr>
<tr><td>The board is finite and rewritten every turn</td>
    <td>The SDK's filesystem setting starts off</td></tr>
<tr><td>A helper can't hold more authority than whoever sent it</td>
    <td>The variables are <code>$CLAUDE_PROJECT_DIR</code> and <code>${CLAUDE_PLUGIN_ROOT}</code></td></tr>
<tr><td>There's no wire from their container back to your laptop</td>
    <td>Beta header strings and their dates</td></tr>
</tbody>
</table>

<p>Learn the right-hand column, because the exam names mechanisms in its options and you'll have to
recognise them. But don't mistake it for the left. From the left you can derive an answer to a
question nobody taught you. The right is vocabulary, and somebody could change it next quarter.</p>

<p class="exit"><b>One screen left.</b> The recap, and a question that needs the whole class rather
than any one screen.</p>
