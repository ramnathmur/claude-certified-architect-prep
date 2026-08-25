# Chapter 32: From business requirement to functional and infrastructure requirement

## What would make it fail?

A client sits down with an architect to brief a house. "I want it to feel open," she says. "Somewhere the family actually wants to be." The architect writes both sentences down, then asks one question: what would make it fail?

The question is the whole job. "Feels open" cannot fail an inspection, because nobody can measure open. The client's mortgage lender has already sent a letter, though: the plot sits in a flood zone, and the loan is conditional on the finished floor sitting eighteen inches above base flood elevation. That number can fail an inspection. It arrived from the lender's own underwriting rules before the architect drew a single wall, and it is the first sentence in this brief a surveyor can check with a tape measure.

The same split runs through every software project before a line of code exists. "Feels open" and "expand into the EU market" are the same kind of sentence: a direction that has not yet become a test. The lender's letter and "no customer record may leave EU jurisdiction" are the same kind of sentence too: a constraint arriving from outside engineering, with an inspector already attached to it. This chapter is about what turns the first kind of sentence into the second, and what a solution architecture has to do with either.

## A business requirement names a destination. A functional requirement names the route.

"Expand into the EU market" is a business requirement. It sits at enterprise level, is not written for any one team, and states why the project exists rather than what gets built. Nobody can point to a line of code and say it satisfies "expand into the EU market" on its own; the sentence has no route in it yet.

One level down sits a requirement that names what a specific group needs from the eventual system: "the sales team needs a quote in the customer's local currency." That is a step closer to buildable, but it is still not the business requirement itself, and a stem naming what one team needs is testing whether the reader can tell that step apart from the enterprise-level goal it serves.

Two more steps turn the destination into a route. A functional requirement states what the system does: "the system shall generate a euro-denominated quote from a GBP catalogue price." That sentence is a consequence of the business requirement above it, phrased as behavior: a "shall do" rather than a "shall be." The exam blueprint's own description of this skill names the sentence's two sources directly: "functional and infrastructure requirements from business requirements and solution architecture." Two sources feed the route, and the second one is easy to leave out, because nothing about "expand into the EU market" mentions an architecture at all.

## The second source: what a chosen architecture hands back to the requirements that produced it

A solution architecture is the specific technical shape chosen for one project: which services exist, what talks to what, which vendor is in the loop. It sits at what the architecture literature calls the tactical level, addressing one project, as against enterprise architecture, which spans an organization's whole systems estate at the strategic level. A solution architecture combines the same business, information, and technical viewpoints an enterprise architecture also draws on, applied to one project instead of the whole organization, and a stem naming an organization-wide standard rather than one project's design is testing whether the reader can tell the two scopes apart.

A solution architecture is itself produced from the business and stakeholder requirements above it, the same ordering the last section already covered. Once an architecture exists, though, it generates requirements of its own, and this second direction is the one easy to miss. Choosing a specific payment-processing vendor for the EU expansion produces a functional requirement that did not exist before the choice was made: integrate with that vendor's API. It produces an infrastructure requirement that did not exist before it either: hold card data only inside that vendor's certified boundary. Requirements motivate the architecture, and the architecture then hands requirements back downstream of itself. That loop, not a one-way handoff, is what the blueprint's phrase is naming when it lists solution architecture as a second source alongside business requirements: the second source is partly a product of the first one, and it still counts as its own source because of what it adds once chosen.

## Infrastructure requirement is this course's name for a category every standard checked here calls something else

Every quality-attribute standard and practitioner body checked for this course, ISO/IEC 25010's own classification, a live architecture body of knowledge's own vocabulary, and AWS's published framework, uses "non-functional requirement" for the category of criteria a system's operation is judged against rather than the behavior it performs: latency, availability, auditability, data residency, phrased "the system shall be X" rather than "the system shall do X." None of them uses "infrastructure requirement" as that umbrella term. Where "infrastructure requirement" does show up in practitioner documents, it names something narrower on purpose: a section covering hardware, network, and hosting specifications specifically, filed alongside a separate non-functional-requirements section rather than replacing it. A document that lists "infrastructure requirements" and "non-functional requirements" as two different sections is treating the first as one slice of the second rather than as its synonym.

Read the exam's own phrase as this course's label for the full non-functional category, not as a term any standards body uses interchangeably with it. That reading is the best-supported one across every source checked here, and it comes with two failure modes worth naming so a stem can't trade one for the other. An option that shrinks "infrastructure requirement" down to servers and networking alone is testing the narrower practitioner reading against the exam's own broader usage. An option that treats an infrastructure requirement as identical to a functional requirement collapses a distinction every source in this chapter keeps: one names behavior, the other names a criterion the behavior is judged against.

## The rule the mechanism produces: a preference becomes a requirement at its boundary

"Feels open," "expand into the EU market," and "keep the data private" are all directions. None of them specifies where correctness stops. A functional requirement becomes testable the moment it states a behavior with a checkable boundary. "Generate a quote" turns into "generate a euro-denominated quote from a GBP catalogue price within five seconds." An infrastructure requirement becomes testable the same way. "Keep the data private" turns into "no customer record may be processed by an endpoint outside the EU." The register stayed the same across both rewrites. What changed is that each sentence now names the line failure crosses. That is the mechanism behind the lender's letter, too: "somewhere the family wants to be" has no line in it anywhere, while "eighteen inches above base flood elevation" is a line and nothing else.

This gives a working test for any sentence handed to you as a requirement: try to write the check that would fail it. If the check would have to consult someone's opinion, the sentence is still a preference, however important it is to the person who said it. If the check can consult a number, a named regulation, or a stated boundary, the sentence has become a requirement, and whether it belongs in the functional or infrastructure column depends only on whether it describes behavior or criteria.

## Five constraints, one instruction: name it before you pick an endpoint

A team building a legal-research assistant is told to "keep documents confidential." That reads like a business requirement still waiting for its route, the kind of concern a compliance team can resolve later, after the prompt and tool design are settled.

The mechanism says otherwise. Named specifically as attorney-client privilege rather than left as "confidential," the constraint rules out a consumer-grade surface the firm cannot audit end to end, and it rules out any code path sending privileged content to an endpoint the firm hasn't approved, before a single prompt gets written. What survives is a direct API or SDK call from inside the firm's own application, authenticated through SSO, routed through an approved gateway with full logging. The same shape repeats across four more named constraints. HIPAA rules out any endpoint not covered by a Business Associate Agreement; what survives is a BAA-covered configuration, arranged directly with Anthropic or through a partner's own HIPAA-eligible cloud account. GDPR rules out a delivery route that cannot pin its execution region; what survives is a cloud-mediated route with the region pinned to a covered jurisdiction, since the direct API does not currently offer EU residency. FedRAMP rules out any endpoint outside a small set of specifically authorized routes. An internal data-residency policy rules out any client pointed at a cloud vendor outside the organization's approved list, whatever the underlying technology would otherwise support.

Every row runs the same instruction: the named constraint decides the endpoint, the credentials, and where the logs land, and it decides all three before tool selection, prompt design, or memory architecture enter the conversation. "Confidential" cannot make that decision, because nothing checks it. Attorney-client privilege can, the same way "eighteen inches above base flood elevation" has a surveyor behind it.

## What naming the constraint doesn't decide

Naming the constraint fixes the endpoint and the credential. It does not design what runs on top of them. SOC 2 sits outside this chapter entirely: it governs how a system is built and operated once its delivery route is already chosen, and by the time it applies, the endpoint decision made in the last section is already behind you. That material belongs two chapters over, with identity and access: which identity a deployed agent carries, and how its access gets scoped down to what one task actually needs once the endpoint is fixed, is that chapter's territory. What a life-cycle framework does with a requirement once it exists, and at what point in a system's life a constraint like this one gets revisited, belongs to the chapter on changing a live system. This chapter's job stops at the point where a preference turns into something a reviewer can check a name against; everything downstream of that name is somebody else's chapter.

## The word that turns the stem

A stem where a client "wants," "prefers," or wants something to "feel" a certain way is still describing a preference, whichever domain it is dressed in. The tell that a testable requirement has entered the stem is a named boundary: a regulation, a number, a certification, or "must" attached to something checkable. That word is what moves the option from opinion to requirement.

## Self-test

**1.** A product team writes: "Grow revenue in the Asia-Pacific region by adding local payment methods." Where does this sentence sit in the requirements hierarchy? *(Select one.)*

A. A functional requirement, because it names a specific capability to add.
B. A business requirement, because it states a vision-level outcome without specifying implementable behavior.
C. An infrastructure requirement, because payment processing touches regulated data.
D. A stakeholder requirement, because it names what one team needs.

**2.** A regional sales lead tells the project team: "My team needs quotes to display in the customer's local currency." Which category does this sentence belong to? *(Select one.)*

A. A business requirement, because it comes from a named individual.
B. A functional requirement, because it already states testable system behavior.
C. A stakeholder requirement, because it names what one group needs rather than the enterprise-level goal it serves.
D. An infrastructure requirement, because currency conversion depends on external rate data.

**3.** Which of the following is a properly formed infrastructure requirement rather than a preference? *(Select one.)*

A. "The checkout flow should feel fast and modern."
B. "95% of checkout requests must complete within 800 milliseconds."
C. "Make the system as reliable as possible."
D. "The team wants better uptime this quarter."

**4.** Per the exam blueprint's own description of this skill, functional and infrastructure requirements are derived from which two sources? *(Select one.)*

A. Business requirements and the development team's technical preferences.
B. Stakeholder interviews and a completed solution architecture only.
C. Business requirements and solution architecture.
D. Solution architecture and systems life-cycle documentation.

**5.** A solution architect's choice of payment-processing vendor generates a new rule: card data must never leave that vendor's certified boundary. What does this illustrate about the relationship between solution architecture and requirements? *(Select one.)*

A. Solution architecture only ever responds to requirements; it never generates new ones.
B. Once chosen, a solution architecture can itself generate further functional and infrastructure requirements downstream of the decision.
C. This is a functional requirement rather than an infrastructure requirement, because it names a vendor.
D. Solution architecture and enterprise architecture are the same activity at different scales, so this requirement applies organization-wide.

**6.** How does a solution architecture differ from an enterprise architecture? *(Select one.)*

A. A solution architecture is produced before any requirements exist; enterprise architecture is produced after.
B. A solution architecture addresses one project at a tactical level; enterprise architecture spans the whole organization at a strategic level.
C. A solution architecture concerns only infrastructure; enterprise architecture concerns only functional behavior.
D. The two terms describe the same scope of work under different names.

**7.** A team is told: "Keep all patient records confidential." Under the rule this chapter teaches, what is the correct next step before any design work begins? *(Select one.)*

A. Proceed with design and address confidentiality in a later security review.
B. Replace the vague instruction with the specific named constraint, such as HIPAA, that determines the endpoint, credentials, and logging route.
C. Add a system-prompt instruction telling Claude not to disclose patient data.
D. Treat the instruction as already testable, since "confidential" is a common industry term.

**8.** A team building a healthcare application confirms Anthropic provides Business Associate Agreement coverage for a specific configuration. Which statement correctly reflects what that coverage means? *(Select one.)*

A. It covers every Anthropic surface uniformly, including Console, Workbench, and consumer plans.
B. It covers a dedicated HIPAA-eligible configuration, and the team must still verify which specific features are included before configuring.
C. It replaces the need to check feature eligibility, since BAA coverage is universal once signed.
D. It applies automatically to any cloud-mediated route without further verification.

**9.** As this exam blueprint uses the term, how does an "infrastructure requirement" relate to how the standards sources in this chapter classify the same territory? *(Select one.)*

A. It is a synonym standards bodies use interchangeably with "functional requirement."
B. It is this course's label for the broader category standards bodies call a non-functional requirement, distinct from a narrower practitioner sense limited to hardware and network specs.
C. It refers exclusively to server, network, and hosting specifications, with no broader meaning in any source checked.
D. No standards body or practitioner source checked for this course uses the term in any sense.

**Answers.** 1: B. The sentence states a vision-level outcome with no implementable behavior named, which is the business-requirement level; A and D are wrong because no team-specific need or system behavior is named yet, and C is wrong because nothing about the sentence concerns infrastructure. 2: C. The sentence names what one team needs, bridging the enterprise-level goal and the eventual system, which is a stakeholder requirement; A is wrong because origin from an individual doesn't determine the category, B is wrong because the sentence is not yet phrased as system behavior, and D is wrong because currency display is not an infrastructure concern. 3: B. It names a checkable boundary, a percentile and a number, that a test can fail; A, C, and D are all unmeasurable preferences dressed as goals, with no line a check can consult. 4: C. The blueprint's own scope line names business requirements and solution architecture as the two sources; A invents a source not named, B drops business requirements, and D substitutes a different, unrelated skill. 5: B. The vendor choice generates requirements that did not exist before the architecture decision, showing the relationship runs both directions; A denies that generative direction outright, C misclassifies a data-boundary rule as functional rather than infrastructure, and D conflates two different scopes of architecture. 6: B. Tactical versus strategic scope is the stated distinction; A reverses the actual production order, C assigns each term a concern it doesn't have, and D denies a real distinction the source material states directly. 7: B. Naming the specific regulation is what lets the constraint decide the endpoint, credentials, and logging route before any design choice; A defers a decision that has to happen first, C treats a downstream instruction as a substitute for choosing the route itself, and D treats an unmeasurable word as if it were already a check. 8: B. BAA coverage is scoped to a specific configuration with features that must still be verified; A, C, and D each claim a blanket coverage the source material explicitly denies. 9: B. Every standards and practitioner source checked treats the broader category as a non-functional requirement, with "infrastructure requirement" as a narrower practitioner term used alongside it; A and C both misstate the scope, and D denies that the narrower practitioner usage exists at all.
