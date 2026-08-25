# Chapter 33: Reading and Reviewing Code You Did Not Write

## A clean review, and the incident two days later

A payments team merges a pull request touching the retry logic for a downstream billing call. An AI reviewer scanned the diff and left three comments: a missing null check, an unclosed database connection, a naming inconsistency. The author fixed all three. Nothing else got flagged. The team read the silence as a clean pass and merged.

Two days later, the retry logic double-charges a batch of customers. The bug isn't on any line the reviewer touched. It's in how the new retry interacts with a timeout setting three services upstream, something the diff never showed, because that setting lives in a file nobody on this pull request opened.

## What a diff actually shows

Code review exists, in Google's own engineering guidance for its reviewers, to keep a codebase's overall health improving over time. The standard is stated as a two-sided rule: a reviewer should favor approving a change once it clearly improves the code, even an imperfect one, and nothing justifies approving a change that clearly makes the codebase worse. The same guidance orders what a reviewer looks for: design and functionality come first, ahead of complexity, tests, naming, comments, style, and documentation. Whether the pieces fit together and whether the change does what the author intended sit at the top of that list, because they're the hardest thing to see and the most expensive to get wrong.

The categories underneath design and functionality aren't decoration. Complexity review asks whether the next engineer to touch this code will be able to, without introducing a bug of their own. Tests review asks whether the change is defended by something that would fail if the change broke. Naming, comments, style, and documentation come last, because getting those wrong costs less than getting the first two wrong. A reviewer working from nothing but the diff can still work this list in order, because it doesn't require anything the diff withholds until the top two categories, design and functionality, ask a question the diff alone often can't answer: whether this specific change is good for the people who depend on the system it touches.

That ordering assumes a reviewer who can see the whole system. A diff carries the lines that changed. The ticket that explains why, the conversation that shaped the design, and what happens when the code runs against real traffic all sit outside it. A reviewer working only from the diff can prove the things visible inside it: a missing null check on a line you can point to, a resource opened and never closed, a variable named for the wrong thing. That same reviewer cannot prove what the change does once it's running, or how it lands on a system the diff doesn't touch, because that information was never in the diff to find.

## Proving a finding instead of guessing at one

A proofreader given one page of a manuscript can do real work on that page. A misspelled name, a subject that doesn't agree with its verb, a quotation mark left open — all of it checkable against the page itself, and settled by pointing at the line. What that same proofreader cannot do from one page is say whether the scene contradicts something the book established four chapters earlier, or whether the printer's press will render a color plate the way the page implies it will. Answering either question means leaving the page: reading the rest of the manuscript, or knowing something about the press. The proofreader isn't careless for not doing this. Working page by page during production, nobody handed them the rest of the book to check against.

An automated reviewer working from a diff sits in a narrower version of that same spot, and the gap between the two is worth naming: a proofreader could ask for the rest of the manuscript and choose not to look. A reviewer commenting on a diff has no equivalent choice, because runtime behavior and another system's state aren't present anywhere in a diff for it to read even if it wanted to. That's the discriminator this chapter turns on. A finding backed by the lines it cites is provable on the page in front of it. A finding about what happens when the code runs, or how it interacts with a service three files away, is a guess dressed as a finding, because the reviewer made the claim without the evidence that would settle it.

Anthropic's own developer training states the resulting rule directly: an AI code review gives you a set of findings to triage, not a verdict to apply. Trust what the reviewer can prove from the diff in front of it, and confirm it on the lines it cites. Treat any claim about runtime behavior or another system as a hypothesis to test, because the reviewer made that claim without the evidence that would prove it. Put the human gate at the point where a finding turns into an action that's hard to reverse.

The same guidance adds a lever most teams leave unused: a reviewer's accuracy on the provable half of its job rises when it's given the conventions it would otherwise have to guess at. A reviewer that doesn't know this codebase treats every timestamp as UTC will either miss a real violation or flag correct code as wrong, purely because it had to guess. Handing it the actual convention, the same way a style guide or a project's own instructions would, narrows the guessing to the part of the job that was never provable from the diff anyway.

The same logic runs in reverse for what a team owes the reviewer before review starts. A team that never states which errors are expected to be handled locally and which are expected to propagate is asking the reviewer to guess at a decision the codebase itself never wrote down, and a wrong guess there looks identical to a wrong guess about a genuine defect. Fixing that isn't a defect in the reviewer. It's missing information the codebase owed it before the review began.

Where the human gate actually sits depends on what the finding is attached to. A comment about renaming a private helper function carries almost no cost if it's wrong, so acting on it without a second look is a reasonable bet even when the reviewer offers no evidence beyond the suggestion itself. A comment sitting next to a database migration, a permissions change, or anything else with no clean way back carries a cost on the other end of that scale. The cost of being wrong is what decides whether a human reads the diff before it runs. A confident-sounding comment doesn't change that arithmetic.

## The comment that was never an approval

Go back to the payments team. The reviewer's three comments were real findings, each pointing at a line in the diff, each fixed. What the team read into the fact that nothing else got flagged is where the mechanism breaks the surface reading. GitHub's own documentation of its review agent states the limitation directly: it "may not identify all of the problems that are present in code, especially where changes are large or complex" — and a retry path touching a call three services upstream is exactly that kind of change. The same documentation treats the tool's comments as a starting point rather than a verdict: they "should be carefully reviewed and considered before taking action," because the reviewer can also surface a problem that was never actually there. That risk cuts both ways in practice: a variable flagged as unused because the diff view doesn't surface the decorator or the dynamic lookup that actually calls it is the same class of error as the missed defect, just pointed in the opposite direction. Either kind is expensive if it's trusted rather than checked. The retry-logic pull request from the opening of this chapter shows that risk from a third angle: every comment the reviewer left was accurate, and the team's mistake was reading its silence as another finding it never actually made.

There's a second, structural fact underneath the first. GitHub's own workflow documentation states that its review agent "always leaves a 'Comment' review, not an 'Approve' or 'Request changes' review," and that this comment "does not count toward required approvals" and "will not block merging." A team that reads a clean automated pass as sign-off is trusting a control the platform itself never wired to gate anything. What actually stood between this diff and production was whichever human reviewer's approval the branch's protection rule required, and on this pull request nobody filled that role, because everyone treated the AI's silence as if it already had.

The same mechanism shows up a level higher, in how a team structures approval itself. A different team, burned by a bad merge, responds by adding a separate change-approval board that every release must clear before deployment: a heavier gate, further from the code, that reads as more careful. Research from Google's DORA program, drawing on its long-running State of DevOps studies, found the opposite. A formal, external review board introduces delay without a matching safety benefit — the research states plainly that "no evidence was found to support the hypothesis that a more formal, external review process was associated with lower change fail rates." The heavier gate doesn't fail for lack of diligence. It fails for the same reason the AI comment failed to gate anything: added distance from the code costs time without adding scrutiny. DORA's own recommendation runs the other way — peer review captured inside the same platform the code was written in, comments and approvals on the record there, which is the same required-approval gate this chapter already located.

## Where this chapter's gate stops

This chapter's territory is the decision at the review step itself: which findings to trust, which to verify, and where to place the point nobody skips. It doesn't extend to what happens once a change is already running in production — rolling out gradually, watching for regression, rolling back cleanly. That's chapter 34's ground, changing a live system without breaking it, and the retry bug above is exactly the kind of failure that chapter picks up once code review has already done what it can do.

It also doesn't extend to review's other documented purpose. The same Google guidance that sets the code-health standard names teaching as a second, separate function of review — a reviewer can leave an optional comment that explains a better pattern without holding up the change over it. That's a real purpose of review, and a separate one from what this chapter is built on: a teaching comment carries no claim to verify, so nothing is at stake if it happens to be wrong.

## Reading the giveaway in a stem

The stem's tell is a scenario where an automated or AI reviewer already looked at the change, flagged something or flagged nothing, and the question asks whether that's enough to merge or deploy. That phrasing is asking whether a comment counted as a gate. Check what the branch's protection rule actually required before trusting what the tool said.

## Self-test

**1.** An AI reviewer left three comments on a diff touching retry logic: a missing null check, an unclosed resource, a naming inconsistency. All three were fixed. No further comments appeared. The branch's protection rule requires two approving reviews from repository collaborators before merge. What does the absence of further comments from the AI reviewer mean for those two required approvals? *(Select one.)*

A. It satisfies one of the two required approving reviews.
B. It never counts toward the required approving reviews, because the AI review is a Comment-type review regardless of what it found.
C. It means the change is safe to merge without any human approval.
D. It should be converted into a Request Changes review before merging.

**2.** A review pass on one diff produces two findings: (1) "line 42 opens a file handle without a matching close" and (2) "this change will slow the nightly batch job by roughly 20%." How should these two findings be treated? *(Select one.)*

A. Both are equally trustworthy because they came from the same review pass.
B. Finding 1 is provable on the cited line; finding 2 is a claim about runtime behavior outside the diff and needs to be tested before anyone acts on it.
C. Finding 2 is more trustworthy because it names a bigger consequence.
D. Neither should be trusted until a second reviewer reproduces both from the diff alone.

**3.** A company, after a bad release, adds a separate change-approval board that every deployment must clear before it reaches production. Which two conclusions does the DORA research described in this chapter support about that decision? *(Select 2 of 4.)*

A. A formal, external review board introduces delay without a matching reduction in change failure rate.
B. Peer review captured inside the same development platform meets the same segregation-of-duties goal without that delay cost.
C. The board should review every individual commit rather than every release.
D. The research recommends giving the board authority over deployment timing.

**4.** A team wants an automated reviewer to stop flagging violations of a convention the team has never written down anywhere. What does this chapter's mechanism say to do? *(Select one.)*

A. Ignore the reviewer's comments on that convention from now on.
B. Give the reviewer the convention explicitly, in a style guide or a project instruction file, so it has less to guess at.
C. Replace the reviewer with a stricter one.
D. Remove the convention from the codebase so there's nothing left to flag.

**5.** An automated reviewer's finding reads "this refactor is safe" on a change that deletes a database column and triggers a migration with no rollback path. Per this chapter's rule for where the human gate belongs, what should happen before the migration runs? *(Select one.)*

A. Nothing further — the "safe" finding is enough, since the diff shows the column deletion clearly.
B. A human review gate specifically at this point, because the migration is the kind of action that's hard to reverse if the finding turns out to be wrong.
C. The migration should proceed automatically once any review, human or automated, completes.
D. No human gate is needed, because irreversible actions are exactly what automated reviewers are best at catching.

**Answers.** 1: B. GitHub's own documentation states its review agent always leaves a Comment-type review, never an Approve or Request Changes review, and that this never counts toward required approvals; A and C both treat the comment as if it were an approval it structurally cannot be, and D describes a conversion the review type doesn't support. 2: B. Finding 1 names a specific line and is checkable against it directly; finding 2 is a claim about behavior at runtime, which the diff cannot establish and which needs to be tested rather than trusted on the reviewer's word. A collapses a provable finding and a hypothesis into one category; C bases trust on the size of the consequence instead of on provability; D asks for a redundant confirmation of something already provable without addressing the finding that actually needs testing. 3: A and B. Both are the research's own stated findings — no reduction in failure rate from the external board, and peer review inside the platform meeting the same goal without the delay. C and D both describe giving the board more authority, an approach the research found ineffective at the goal it's meant to serve. 4: B. This chapter's mechanism holds that a reviewer's accuracy rises when it's given the conventions it would otherwise guess at; A leaves the underlying noise in place, C doesn't address the missing information at all, and D removes the convention instead of documenting it. 5: B. The chapter's rule places the human gate at the point where a finding becomes an action that's hard to reverse, and an irreversible migration is exactly that point regardless of what the automated finding claims; A treats an unverifiable claim as sufficient, C removes the gate entirely, and D gets the mechanism backwards — irreversible actions are precisely the cases the diff-only reviewer has the least evidence to support a claim about.
