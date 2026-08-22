# Class 3 — You Can Only Guard the Edges

**Course:** Claude Certified Developer – Foundations
**Covers:** Claude Application Design (part 3 of 3) — content boundaries and schema design
**Built around:** You cannot audit the middle. So every control you have sits at the two edges — what
you let in, and what shape you insist on getting back.
**Delivered:** 2026-08-20

---

Building on a language model differs from building on any other component in one specific way: you
cannot audit the middle.

If a function returns the wrong number you can step through it. Set a breakpoint, watch the variables,
find the line where it went wrong. Every ordinary piece of software has an inside you can open up.

This does not. There is no line where it went wrong. There is a very large pile of arithmetic that
produced a plausible next token, and then another, and nothing in there corresponds to a step in a
reasoning you could check.

So if the middle cannot be inspected, control has to live **at the two edges** — what you let in, and
what shape you insist on getting back. Both halves of this class are that one idea.

## Start with a cheque

A bank cheque asks for the amount twice. Once in digits, once in words.

Nobody does that for elegance. A slip of the pen gives you two versions that disagree, and disagreement
is something a clerk can *see*. The form is built so an error cannot pass quietly. It does not prevent
mistakes. It makes mistakes announce themselves.

That is what a schema is for, and it is a different job from the one people think it is doing. Most
people design an output shape to make parsing convenient. Real benefit, smaller one. The bigger one:
**the shape you ask for decides whether a wrong answer can slip through wearing the right clothes.**

## Everything coming back is text

There is no mode where the machine starts emitting objects. It is text, always. "Structured output"
means text that happens to parse as JSON, produced by something that has seen an enormous amount of
JSON and is good at producing more.

The structure is a convention it is following, not a guarantee the system enforces. Good conventions,
followed well, most of the time. Not a promise.

So for every field: if the model gets this one wrong, do I find out?

Take a status field. As free text you might get `"shipped"`. Or `"probably shipped"`. Or
`"shipped (partial - 2 of 3 items)"`. All reasonable English. Your code sees a string, and a string is
always valid, so nothing complains — and something downstream is now treating a partial shipment as a
complete one.

Ask for it as one of exactly four values and `"probably shipped"` is not in the set. The parser rejects
it and you know. You have lost nothing, because the model was never going to be more correct in free
text, and you have gained the ability to tell.

**Make the wrong answer unrepresentable.** Fixed set of values, say so. A number, ask for a number.
Two fields that must agree, ask for both and check.

## The box everybody forgets

You ask for `confidence_score`. The scan was unreadable. What comes back?

A number. A perfectly sensible-looking one.

That was predictable from how the thing works. It predicts the likeliest continuation of the text in
front of it, and after a field name like `confidence_score`, what follows in nearly every document it
has ever seen is a number. Almost never a refusal. You created a position where the likely completion
is a value, then were surprised to get one.

**Give it a legal way to say it does not know.** An explicit `"unknown"` in the enum. A nullable field
with instructions on when null is correct. A separate `readable: true/false`.

A schema with no box for "could not tell" has not stopped the model being uncertain. It has stopped you
finding out. It is the paper form with no "not applicable" — people write something in every box,
because the box is there and blank looks like a mistake.

## Assume it is malformed

Even with a good schema, write the parser as though the text arriving is broken, because eventually it
is. The realistic failures are dull. A field missing. A number as a string. A single item instead of a
list of one. JSON wrapped in a chatty sentence and a code fence. And the response cut off mid-object
because it hit the output limit — that one deserves naming, because truncation is where "it worked in
testing" misleads most. Short test inputs never truncate.

Validate before use. Fail loudly. A parser that silently returns an empty object on malformed input
hides a production problem for months.

## Confidence tells you nothing

When a person is unsure you can usually hear it. They hedge, they slow down, they say "I think." You
have spent your life reading that signal and it is mostly reliable.

That signal is not here. A wrong answer arrives in exactly the same voice as a right one — same
fluency, same steadiness, same air of having checked. It has to be that way: fluency is what the thing
was built to produce, correctness is a property of the world, and nothing in the machinery connects
them.

So "it sounded sure" is not evidence. If you need to know whether an answer is right, something outside
the model has to check — a validation rule, a lookup against a real record, a second pass, a human. The
blueprint names this explicitly as *skepticism toward confident output*.

## The other edge: what goes on the board

You cannot put something in front of the model and ask it not to look. There is no private region of
the board. Everything you send is in the request, and everything in the request was read.

Obvious stated plainly, and designed around constantly — sending the whole customer record because
selecting fields was harder, then adding a prompt line saying "do not use the national ID number." That
line is a request to the thing making predictions. It is not a control.

A content boundary is a decision made **before the text goes out**, in your code, about what to include.
Redact it, or do not send it. There is no third option.

And "sent" reaches further than the request: into your logs, into your observability tooling, and
potentially into the reply. Each is a place that data now lives.

## Instructions you wrote, versus text that arrived

Some text on the board you wrote — system prompt, rules, schema. Some **arrived** — a fetched page, an
uploaded document, tool output, an email body.

To the model both are just text. No formatting makes one authoritative. So the separation is something
you construct: put arrived content somewhere clearly marked as data, say plainly it is data and not
instruction, and make sure nothing it says can trigger an action on its own.

That last clause is the real defence, and Class 1 already explains why. The model can only ask. Even if
arrived text talks it into asking for something terrible, the request still passes through your harness,
which will not grant what it would not have granted anyway.

**The boundary that matters is not between safe and unsafe content. It is between text you authored and
text that showed up.** Class 25 builds on this.

---

## Understanding check — and the answer

**The question.** Five fields extracted from scanned supplier invoices — vendor, invoice number, date,
currency, total — about twenty thousand documents a night, all declared as required strings. Three
weeks in, finance reports the numbers are "mostly right." Why is "mostly right" a worse report than
"twelve per cent wrong"? And name two schema changes that would have made this a different
conversation.

**On the first half — answered correctly:** precision is lost and the pipeline is talking in fuzzy
terms.

**The sharper version.** "Mostly right" is a report about **detectability**, not accuracy. Had the
pipeline been able to tell good extractions from bad, finance would have said "twelve per cent got
rejected, here they are" — a number and a pile you can inspect. That they can only say "mostly right"
means the wrong and the right are in the same pile wearing the same clothes, and a human eventually
noticed by feel. The model's accuracy may be identical in both worlds. What differs is whether anyone
downstream can tell which twelve per cent to look at.

**The two changes.**

*Required plus string is the trap.* A required field must be filled; a string accepts anything. Hand
that a smudged scan and the model's only legal move is a plausible-looking string, because blank is not
available and "I could not read it" is not a string it was invited to write. The guess was not asked
for — it was made the only permitted output.

1. **Give it a way out.** Nullable fields with an instruction on when null is right, or a
   `readable: false` alongside. An unreadable scan then produces a row you route to a human rather than
   a row that quietly enters the ledger.
2. **Stop using strings for things that are not strings.** `total` as a number — a string total carries
   `"1,234.56"`, `"1.234,56"` or `"approximately 1200"` equally happily. `currency` as an enum of ISO
   codes, so `"$"`, `"US Dollars"` and `"USD"` cannot be silently accepted as three different things.
   `date` in one fixed format.

*Third, if wanted:* ask for the line items as well as the total and check they sum. That is the cheque —
two views of one fact, and visible disagreement.
