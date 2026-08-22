# Pack E — Source Pack for Chapter 6, Chapter 32, Chapter 33, and Chapter 34

**Built:** 2026-08-22 · **All facts fetched:** 2026-08-22
**For:** CCDV-F course regeneration — Chapter 6 ("Diagnosing a prompt by its failure"), Chapter 32
("From business requirement to functional and infrastructure requirement"), Chapter 33 ("Reading and
reviewing code you did not write"), Chapter 34 ("Changing a live system without breaking it")
**Rule applied:** no source, no claim. Every fact below carries the URL it was read on and the date. Anything
not established is in the gap lists at the end, not filled in from memory.

**This pack has two halves with different source rules**, per the brief:

- **Chapter 6 (Half One):** Anthropic-controlled sources only — `platform.claude.com/docs`,
  `docs.claude.com`, `anthropic.com`. Every search below was run without domain restriction but only
  Anthropic-controlled results were fetched or cited; community explainer content that surfaced in
  search results was not used even when convenient.
- **Chapters 32–34 (Half Two):** general engineering sources are permitted — standards bodies
  (ISO/IEC/IEEE), established references (IIBA, PMI, Google engineering practices, NIST), major cloud
  well-architected guidance. Preference order followed: primary/standards text first, blogs last resort
  and flagged when used.

## How to read this pack

**Fetch-fidelity marker**, following the convention set in Pack A:

- **[RAW]** — the fetch returned the page's own markdown, frontmatter intact (`---\ntitle: ...\nurl:
  ...\ndescription: ...\n---`). Quoted strings are the page's own words.
- **[VIA-SUMMARIZER]** — the fetch tool returned a model-written answer *about* the page rather than
  page source (no frontmatter, narrated preamble like "here is the content"). The content is still
  sourced from the real page, but a "quoted" string may be a paraphrase. Re-fetch before quoting
  directly in the chapter.
- **[SEARCH-SYNTHESIS]** — content came only from a WebSearch tool's own synthesized answer, with no
  follow-up fetch of the underlying page. Treated as the weakest tier; used only where explicitly
  labelled, and never quoted as if verbatim.

**[VOLATILE]** marks a number, price, date, or version-specific detail likely to drift before this
course is next revised. The exam is judgement-shaped and closed-book, so these are present for the
writer's context, not for the reader to memorise.

---

# CHAPTER 6 — "Diagnosing a prompt by its failure"

**Source discipline:** every fact below is from `platform.claude.com/docs`. Two redirect chases
confirmed `docs.claude.com` now 302-redirects prompt-engineering sub-paths to the same
`platform.claude.com/docs` pages — there is no separate "docs.claude.com" content for this topic, just
one canonical host reached by two hostnames.

**Structural finding, load-bearing for how this chapter should be written:** the three sub-pages the
exam blueprint's wording implies are separate — "system prompts," "multishot prompting," and the
general techniques page — have been **merged into one living reference page**,
`claude-prompting-best-practices`. Fetching `.../prompt-engineering/overview`,
`.../prompt-engineering/system-prompts`, and `.../prompt-engineering/multishot-prompting` on
2026-08-22 returned three different URLs but the **system-prompts and multishot-prompting paths both
served the identical best-practices page** — confirmed by identical title/description frontmatter and
byte-identical section content. The overview page explicitly says why: "All prompting techniques (from
clarity and examples to XML structuring, role prompting, thinking, and prompt chaining) are covered in
[Prompting best practices] ... That's the living reference; start there." This is a real structural
fact about the current documentation, not a fetch error — cite the merged page for all of these
sub-topics, not separate ones.

## RQ1 — Instruction clarity ("be clear and direct")

**Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
— fetched 2026-08-22 **[RAW]**

Verbatim, under "Be clear and direct":

> "Claude responds well to clear, explicit instructions. Being specific about your desired output can
> help enhance results. If you want 'above and beyond' behavior, explicitly request it rather than
> relying on the model to infer this from vague prompts."

> "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The
> more precisely you explain what you want, the better the result."

**Golden rule, verbatim:** "Show your prompt to a colleague with minimal context on the task and ask
them to follow it. If they'd be confused, Claude will likely be too."

Concrete guidance given: be specific about desired output format and constraints; provide instructions
as sequential numbered/bulleted steps when order or completeness matters. The page's own example
("Create an analytics dashboard" vs. the same instruction with explicit scope and thoroughness
language) is the canonical less-effective/more-effective pair.

**A second, related technique on the same page — adding context/rationale:**

> "Providing context or motivation behind your instructions, such as explaining to Claude why such
> behavior is important, can help Claude better understand your goals and deliver more targeted
> responses."

Its own example: "NEVER use ellipses" (less effective) vs. "Your response will be read aloud by a
text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to
pronounce them" (more effective). The page's own framing: "Claude is smart enough to generalize from
the explanation." **This is a distinct, separately named technique from bare clarity** — clarity fixes
underspecification; added rationale fixes a rule followed to the letter but not the spirit.

**Discriminator:** a scenario where Claude's output is technically compliant with an instruction but
misses the point is a rationale-gap, not a clarity gap — the fix documented is explaining *why*, not
just restating *what* more forcefully.

## RQ2 — Few-shot / multishot examples, and the zero-shot terminology gap

**Source:** same best-practices page — fetched 2026-08-22 **[RAW]**, section "Use examples effectively":

> "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A
> few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and
> consistency."

Documented quality criteria for examples — verbatim list:

> "**Relevant:** Mirror your actual use case closely. **Diverse:** Cover edge cases and vary enough
> that Claude doesn't pick up unintended patterns. **Structured:** Wrap examples in `<example>` tags
> (multiple examples in `<examples>` tags) so Claude can distinguish them from instructions."

**Quantity guidance, verbatim:** "Include 3–5 examples for best results. You can also ask Claude to
evaluate your examples for relevance and diversity, or to generate additional ones based on your
initial set."

**The zero-shot gap — established, not inferred.** The exam blueprint names "zero-/single-/multi-shot
prompting" as a unit. Anthropic's current developer documentation does not. Three checks:

1. The best-practices page (the living techniques reference) uses only "few-shot or multishot
   prompting" — "zero-shot" does not appear anywhere in that section or elsewhere on the page.
2. The Glossary page (https://platform.claude.com/docs/en/about-claude/glossary — fetched 2026-08-22
   **[RAW]**, full page read) defines Context window, Fine-tuning, HHH, Latency, LLM, MCP, MCP
   connector, Pretraining, RAG, RLHF, Temperature, TTFT, Tokens. **No entry for zero-shot, one-shot,
   single-shot, or few-shot.**
3. Two site-restricted searches — `"zero-shot" site:platform.claude.com` and `"zero-shot"
   site:anthropic.com`, both run 2026-08-22 — surfaced the term only in evaluation/research contexts:
   multilingual benchmark results ("robust performance on zero-shot tasks across various languages," on
   the multilingual-support doc) and alignment-research papers (reward-tampering study, weak-to-strong
   generalization). **Not once as a named prompting technique for developers.**

**What this means for the chapter:** "few-shot / multishot" is Anthropic's own vocabulary and is
richly documented with concrete guidance (3–5 examples, relevance, diversity, `<example>` tag
structure). "Zero-shot" is real terminology — it is standard in the wider field and the exam blueprint
uses it — but it is not a term Anthropic's own prompt-engineering guide defines or gives technique-level
guidance on. Teach zero-shot as "the default state when you provide no examples," sourced to the
absence of examples described throughout the multishot section, not as a technique with its own
Anthropic-documented best practices. Do not present a fabricated Anthropic "zero-shot" quote.

**Discriminator this section supports:** a scenario testing whether the candidate reaches for examples
at all (zero-shot failing on format/tone consistency) vs. a scenario testing *how many* and *how
structured* those examples should be (few-shot execution quality) are different failure diagnoses, and
only the second has explicit Anthropic guidance to cite.

## RQ3 — System vs user placement

**Source:** same best-practices page, section "Give Claude a role" — fetched 2026-08-22 **[RAW]**:

> "Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a
> single sentence makes a difference."

The page's own worked example (all eight SDK/CLI variants shown) puts the **persona/standing context in
`system`** — `"You are a helpful coding assistant specializing in Python."` — and the **specific,
one-off task in `user`** — `"How do I sort a list of dictionaries by key?"` This is a structural
demonstration of the placement rule, not just an assertion: role and standing behaviour go in `system`;
the concrete ask goes in `user`.

**Corroborating source, independent page:** "Reduce prompt leak" —
https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak —
fetched 2026-08-22 **[RAW]**:

> "Separate context from queries: You can try using system prompts to isolate key information and
> context from user queries."

And, describing its own worked example, this page states directly that role-prompting in the system
turn is Anthropic's recommended default:

> "Notice that this system prompt is still predominantly a role prompt, which is the **most effective
> way to use system prompts**."

(That phrase links to the "Give Claude a role" anchor on the best-practices page — i.e., two separate
pages converge on the same claim: role/standing-context is what the system prompt is documented to be
*for*.)

**Third corroboration:** "Increase output consistency" —
https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency —
fetched 2026-08-22 **[RAW]**, section "Keep Claude in character": "Use system prompts to set the role:
Use system prompts to define Claude's role and personality. This sets a strong foundation for
consistent responses."

**What was searched for but not corroborated on a raw fetch:** an earlier WebSearch synthesis
(not a page fetch) returned the sentence "Put everything else, like task-specific instructions, in the
user turn instead," attributed to a system-prompts page. **This exact sentence was not found in the
current merged best-practices page on a direct raw fetch**, and `docs.claude.com`'s standalone
system-prompts URL 302-redirects to the same merged page rather than serving separate content. Treat
that specific sentence as **[SEARCH-SYNTHESIS]**, not verified — the *pattern* it describes (role in
system, task in user) is verified structurally via the code example above, but that specific wording is
not confirmed verbatim on any page fetched today. Do not quote it as an Anthropic quotation.

**Discriminator:** a scenario testing "does standing behaviour/persona belong in system or user" has
direct, multiply-corroborated documentation support (system). A scenario testing per-turn task content
placement is supported by the same worked example (user) but should be taught as "the task/query," not
quoted with the unverified sentence above.

## RQ4 — Placement across components (where instructions, examples, and data go)

**Source:** same best-practices page, sections "Structure prompts with XML tags" and "Long context
prompting" — fetched 2026-08-22 **[RAW]**.

**On XML structuring, verbatim:**

> "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes
> instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag
> (for example, `<instructions>`, `<context>`, `<input>`) reduces misinterpretation."

Best practices given: use consistent, descriptive tag names across prompts; nest tags when content has
a natural hierarchy (documents inside `<documents>`, each inside `<document index="n">`).

**On ordering within a long prompt, verbatim — this is the direct answer to "where in a request do
instructions, examples and data go":**

> "**Put longform data at the top:** Place your long documents and inputs near the top of your prompt,
> above your query, instructions, and examples. This improves performance across all models."

With a quantified claim attached: "Queries at the end can improve response quality by up to 30 percent
in tests, especially with complex, multidocument inputs." **[VOLATILE — the percentage, not the
ordering principle]**

Also documented: "Structure document content and metadata with XML tags" (wrap each document in
`<document>` with `<document_content>` and `<source>` subtags), and "Ground responses in quotes" — ask
Claude to quote relevant parts of long documents before carrying out the task, "to focus on the relevant
content and ignore the rest."

**Synthesis of the placement rule, grounded in the two quotes above:** long/bulk data goes at the top;
instructions, examples, and the query go after the data, nearest the end of the prompt; each distinct
content type (instructions, context, examples, input, per-document metadata) gets its own XML tag so
Claude does not have to infer where one kind of content ends and another begins. This is Anthropic's own
stated placement doctrine, not an inference beyond it.

**Discriminator:** a scenario with a large document plus a short instruction is testing whether the
candidate knows to put the document first and the instruction last — the "up to 30 percent" framing
signals this is a real, not cosmetic, quality lever.

## RQ5 — Output constraints

**Source A:** best-practices page, section "Control the format of responses" — fetched 2026-08-22
**[RAW]**:

Four documented levers, verbatim structure:

> "1. **Tell Claude what to do instead of what not to do** — Instead of: 'Do not use markdown in your
> response.' Try: 'Your response should be composed of smoothly flowing prose paragraphs.'
> 2. **Use XML format indicators** — Try: 'Write the prose sections of your response in
> `<smoothly_flowing_prose_paragraphs>` tags.'
> 3. **Match your prompt style to the desired output** — ...removing markdown from your prompt can
> reduce the volume of markdown in the output.
> 4. **Use detailed prompts for specific formatting preferences**"

**Discriminator embedded in technique 1:** negative instructions ("do not do X") are documented as
*less* reliable than positive ones ("do Y instead") — a scenario option phrased as a prohibition is the
weaker of two otherwise-similar options.

**Source B:** "Increase output consistency" —
https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency —
fetched 2026-08-22 **[RAW]**. This page opens with an explicit boundary that matters for a
diagnosis-shaped chapter:

> "**For guaranteed JSON schema conformance** — If you need Claude to always output valid JSON that
> conforms to a specific schema, use Structured Outputs instead of the prompt engineering techniques
> below. Structured outputs provide guaranteed schema compliance and are specifically designed for this
> use case. The techniques below are useful for general output consistency or when you need flexibility
> beyond strict JSON schemas."

**This is itself a discriminator worth teaching directly:** "constrain output via prompt engineering"
and "guarantee schema conformance via Structured Outputs" are documented as two different tools for two
different jobs — a scenario demanding *guaranteed* schema compliance should not be answered with prompt
phrasing alone, per Anthropic's own framing.

Four prompt-engineering-level techniques the page documents for the flexible case: specify the desired
output format precisely (JSON/XML/custom template, shown with a worked customer-feedback example);
prefill the Assistant turn to bypass preamble and force structure (flagged: **"Prefilling is not
supported on Claude 4.6 and later models and Claude Mythos Preview"** [VOLATILE — generation-specific] —
use Structured Outputs or system-prompt instructions instead on those models); constrain with worked
examples ("Provide examples of your desired output. This is more effective than abstract
instructions."); and ground in retrieval for tasks needing consistent context (verbatim: "use retrieval
to ground Claude's responses in a fixed information set").

## RQ6 — Iterative refinement

**Source:** "Define success criteria and build evaluations" —
https://platform.claude.com/docs/en/test-and-evaluate/develop-tests — fetched 2026-08-22, re-fetched
for raw fidelity, confirmed **[RAW]** (frontmatter present on second fetch).

Opening framing, verbatim:

> "Building a successful LLM-based application starts with clearly defining your success criteria and
> then designing evaluations to measure performance against them. This cycle is central to prompt
> engineering."

The page's own flowchart image caption states the refinement cycle explicitly, as five stages in order:
**"test cases, preliminary prompt, iterative testing and refinement, final validation, ship."** This is
the direct documented answer to "what is iterative refinement of a prompt" — it is not a standalone
technique but a stage in a named five-step cycle that starts from success criteria and test cases,
passes through a first-draft ("preliminary") prompt, and only then iterates.

Documented success-criteria qualities, verbatim: "Specific," "Measurable," "Achievable," "Relevant" —
each with a worked bad/good pair (e.g., "Safe outputs" [bad] vs. "Less than 0.1% of outputs out of
10,000 trials flagged for toxicity by the content filter" [good]).

Documented eval-design principles, verbatim: "**Be task-specific:** Design evals that mirror your
real-world task distribution. Don't forget to factor in edge cases!"; "**Automate when possible:**
Structure questions to allow for automated grading"; "**Prioritize volume over quality:** More
questions with slightly lower signal automated grading is better than fewer questions with high-quality
human hand-graded evals."

**Second source, reinforcing the same cycle from the security side — continuous monitoring feeding back
into refinement.** "Mitigate jailbreaks and prompt injections" —
https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks —
fetched 2026-08-22 **[RAW]**, section "Continuous monitoring":

> "Regularly analyze outputs for signs of successful injection. Use this monitoring to iteratively
> refine your prompts, validation, and filtering strategies."

**Third source, the chaining mechanism for refinement within a single pipeline.** Best-practices page,
section "Chain complex prompts" — fetched 2026-08-22 **[RAW]**:

> "The most common chaining pattern is **self-correction:** generate a draft → have Claude review it
> against criteria → have Claude refine based on the review. Each step is a separate API call so you
> can log, evaluate, or branch at any point."

**Discriminator:** a scenario testing whether a candidate treats "iterative refinement" as a one-off
polish pass versus a structured cycle (criteria → test cases → draft → test → refine → validate → ship,
with each stage a checkpoint) should be answered against the five-stage flowchart, not against ad hoc
prompt tweaking.

## RQ7 — Input sanitization

**Source:** "Mitigate jailbreaks and prompt injections" —
https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks —
fetched 2026-08-22 **[RAW]**, full page read.

**Framing note for the chapter:** this page lives under Test and Evaluate → Strengthen Guardrails, which
is adjacent to (not the same as) the Security and Safety domain's "prompt injection awareness and
mitigation" skill (domain 7). The exam blueprint places "input sanitization" specifically under the
**Prompt Engineering** skill in domain 6, alongside clarity and examples — so this chapter should teach
input sanitization as a prompt-construction discipline (how you shape a request so untrusted data cannot
be read as instructions), not repeat the domain-7 material on jailbreak defence wholesale. The
overlapping source is real; the emphasis should differ by chapter.

The page opens by naming two distinct threat models, verbatim:

> "**Jailbreaks and direct prompt injection**, where the *user* of your application is the adversary and
> crafts inputs intended to bypass your guardrails."
> "**Indirect prompt injection**, where the user is trusted but Claude processes *third-party content*
> (web pages, emails, documents, tool results) that contains adversarial instructions."

**Documented sanitization techniques for the direct case:**

> "**Input validation:** Filter user input for known injection patterns before it reaches Claude. You
> can use an LLM to create a generalized validation screen by providing known jailbreaking language as
> examples."

> "**Harmlessness screens:** Use a lightweight model like Claude Haiku 4.5 to pre-screen user input
> before it reaches your main conversation. Use structured outputs to constrain the response to a
> simple classification." [VOLATILE — the specific model name]

**Documented sanitization techniques for the indirect case (untrusted third-party content), which map
more directly onto "placement" than "filtering":**

> "**Put untrusted content only in tool results.** Deliver third-party content to Claude inside
> `tool_result` blocks, never in `system` prompts or plain user `text` blocks. Claude is trained to
> treat instructions that appear inside tool results with appropriate skepticism."

> "**Tell Claude what the content is and where it came from.**" — explicit provenance in the tool
> description or result structure "helps Claude calibrate how much to trust embedded directives."

> "**JSON-encode untrusted content.** Where possible, wrap third-party strings in a JSON object rather
> than concatenating them into free-form text. JSON escaping provides unambiguous delimiters between the
> untrusted payload and the surrounding structure, so an attacker cannot close a quote or tag to 'break
> out' into an instruction context."

> "**Don't put your own instructions in tool results.** Because Claude treats tool-result content as
> untrusted data, instructions you place there may be ignored or flagged as a potential injection. Send
> your instructions in a `user` turn that follows the `tool_result` block."

> "**Limit Claude's access to sensitive data and actions.** Apply the principle of least privilege so
> that a successful injection can do minimal damage."

**Discriminator:** a scenario about a user directly trying to jailbreak the system points to input
validation / harmlessness screening (filter before it reaches Claude). A scenario about third-party
content (an email body, a fetched web page, a tool's return value) carrying embedded instructions points
to placement and encoding (tool_result blocks, JSON-encoding, provenance) — **not** to input filtering,
because the content is not necessarily malicious on its face, it is merely untrusted. This is the
sharpest two-option discriminator this section supports: filter-before-reaching-Claude vs.
structurally-isolate-and-flag-provenance answer different threat shapes.

## Chapter 6 synthesis — technique → failure map

This table exists because the chapter is organised as a diagnosis. Every row is grounded in the RQ
sections above; nothing here is a new unsourced claim.

| Technique (Anthropic's own term) | Failure it is documented to fix | Grounded in |
|---|---|---|
| Be clear and direct | Vague/underspecified output; Claude fails to go "above and beyond" because it was never explicitly asked | RQ1 |
| Add context / explain rationale | Instruction followed to the letter but the *point* is missed (rule obeyed, goal not met) | RQ1 |
| Few-shot / multishot examples | Format, tone, or structure drift; inconsistency across repeated calls | RQ2 |
| XML tags for instructions/context/examples/input | Claude misinterprets which part of a mixed prompt is instruction vs. data | RQ4 |
| Role in the system prompt | Wrong tone/register; responses drifting outside the task's bounds | RQ3 |
| Put long data at top, query/instructions last | Degraded quality on long, multi-document inputs (up to ~30% in Anthropic's own tests) | RQ4 |
| Positive format instructions over negative ones | Claude ignoring a "don't do X" instruction more often than a "do Y" one | RQ5 |
| Structured Outputs (vs. prompt-only formatting) | Non-guaranteed schema conformance when the requirement is strict JSON validity | RQ5 |
| Prefill / constrain-with-examples / retrieval grounding | Preamble noise, inconsistent structure, ungrounded answers in a knowledge-base task | RQ5 |
| Five-stage test/refine/validate/ship cycle | A prompt that looks fine on first read but was never checked against real success criteria | RQ6 |
| Self-correction chaining (draft → review → refine) | Single-pass output that hits a quality ceiling a second look would catch | RQ6 |
| Input validation / harmlessness screens | A user directly crafting an adversarial prompt (jailbreak, direct injection) | RQ7 |
| tool_result isolation, provenance labelling, JSON-encoding | Untrusted third-party content (email, web page, tool output) carrying embedded instructions that could "break out" into an instruction context | RQ7 |

---

# CHAPTER 32 — "From business requirement to functional and infrastructure requirement"

**Source discipline for this chapter and the two after it:** general engineering sources are permitted
per the brief. Preference order actually achieved, honestly reported: IIBA's own knowledge-hub pages
(primary body, but the substantive definitions sit behind a member paywall — confirmed by direct fetch,
see below), ISO's standard-abstract pages (blocked by 403 on every attempt — ISO standards are
commercial documents, confirmed inaccessible), a professional architecture body's freely published body
of knowledge (IASA's BTABoK, fully public on GitHub Pages), a major cloud provider's well-architected
documentation (AWS), and Wikipedia as tertiary corroboration where primary text was paywalled — flagged
every time it is the source of record rather than just a pointer.

## RQ1 — Business requirements: canonical definition

**Primary-source access result, reported honestly:** IIBA's BABOK Guide is the standard reference body
for this term. Two direct fetches of IIBA's own knowledge-hub pages —
https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/2-business-analysis-key-concepts/2-3-requirements-classification-schema/
and
https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-30-non-functional-requirements-analysis/
— both fetched 2026-08-22, returned **navigation shell only; the substantive definitions are behind a
member login.** This is a confirmed access limitation, not an absent source: BABOK is real and is the
standard reference, but its text could not be read today.

**What was established, via WebSearch synthesis of secondary explainer pages that themselves describe
BABOK's classification** — 2026-08-22, **[SEARCH-SYNTHESIS]**, treat as a paraphrase of BABOK, not a
quotation from it:

BABOK's requirements classification schema, in hierarchy order: **Business Requirements** → 
**Stakeholder Requirements** → **Solution Requirements** (split into **Functional** and
**Non-Functional**) → **Transition Requirements**.

- **Business requirements** sit at enterprise level, are not specific to any one stakeholder group,
  are "high-level statements that define the Vision, Scope and Duration of the project," and "express
  why the project is being undertaken but cannot be directly implemented in a system."
- **Stakeholder requirements** "define the needs of a particular group of stakeholders," bridging
  business requirements and solution requirements.
- **Solution requirements** "describe the capabilities and qualities of a solution that meets the
  stakeholder requirements" at implementation-ready detail, and split into functional and
  non-functional.
- **Transition requirements** "define characteristics that a solution must have in order to transition
  from the current state to the desired future state" — these disappear once the transition is
  complete, unlike the other categories.

**Discriminator this gives the chapter directly:** a scenario stating "why we're doing this project" or
naming vision/scope/ROI is a business requirement. A scenario naming what a specific user group needs
from the solution is a stakeholder requirement, not a business requirement — a common one-step-removed
distractor.

## RQ2 — Functional requirements: canonical definition

**Source:** Wikipedia, "Non-functional requirement" article —
https://en.wikipedia.org/wiki/Non-functional_requirement — fetched 2026-08-22. Fetch returned
processed/synthesized content rather than raw article wikitext (no visible citation markers in the
returned text), so this is marked **[VIA-SUMMARIZER]** — corroborated below by a second, independent
search.

> Functional requirements define what a system should *do* — conventionally phrased "system shall do
> \<requirement>." Planning for functional-requirement implementation happens at the system-design
> level.

**Corroborating source, independent search** — 2026-08-22, **[SEARCH-SYNTHESIS]**, aggregating multiple
requirements-engineering explainer sources: "Functional requirements specify what a system must do,
including its behaviors, capabilities, and responses to inputs," individually phrased as "system shall
do \<requirement>."

**Relationship to business requirements, from the same synthesis:** "If business requirements define
the destination, functional requirements describe the route." Functional requirements are what converts
a business goal into "specific features, behaviors, and system capabilities" — i.e., functional
requirements are downstream of, and derived from, business requirements, matching the BABOK hierarchy in
RQ1.

## RQ3 — Non-functional vs. "infrastructure" requirements: the naming question, established

This is the chapter's central discriminator question, and it was checked against four independent
bodies rather than one. **Finding: "non-functional requirements" is the universal standard umbrella
term. "Infrastructure requirements" is real, current industry vocabulary — but it names a narrower
subset (hardware, network, hosting, deployment environment), not the whole non-functional category. The
exam's phrase is best read as its own umbrella label for that same territory, not as a term any
standards body uses interchangeably with "non-functional."**

**Check 1 — Wikipedia's own list of NFR synonyms, fetched 2026-08-22.** The article's canonical
definition: "a requirement that specifies criteria that can be used to judge the operation of a system,
rather than specific behaviours," phrased "system shall be \<requirement>," with non-functional
requirements planned "at the systems architecture level" (vs. functional requirements at the design
level — a second useful discriminator: NFRs are an architecture-level concern, not a design-level one).
The article's own exhaustive list of alternate/synonymous terms it names: **"quality attributes"**
(primary alternative), **"architectural characteristics,"** **"cross-functional requirements (CFR)"**
(a ThoughtWorks-proposed alternative specifically to counter the "non-functional sounds unimportant"
criticism), **"qualities," "quality goals," "quality of service requirements," "constraints,"
"non-behavioral requirements," "technical requirements,"** and the informal **"ilities."** **This list
does not include "infrastructure requirements."** The article cites ISO/IEC 25010:2011 and ISO/IEC 9126
as the relevant quality-attribute standards.

**Check 2 — ISO/IEC 25010, the standard Wikipedia points to for NFR-adjacent quality characteristics.**
Both the 2011 abstract page (iso.org/standard/35733.html referenced in search results) and the 2023
edition's Online Browsing Platform page (https://www.iso.org/obp/ui/en/#!iso:std:78176:en, fetched
2026-08-22) were **inaccessible — 403 Forbidden on the OBP page; the standard is a commercial ISO
document.** What is established only via WebSearch synthesis, **[SEARCH-SYNTHESIS]**: ISO/IEC 25010
organizes quality into **product quality** and **quality in use**, with product quality classified into
characteristics including functional suitability, performance efficiency, compatibility, usability,
reliability, security, maintainability, and portability (eight in the 2011 edition; the 2023 revision is
reported to have expanded this, exact current count **not independently confirmed** — flagged as a gap
below). **"Infrastructure" does not appear as one of the named characteristics** in any source consulted
— infrastructure concerns (capacity, hosting, deployment topology) would be treated as inputs to
achieving characteristics like performance efficiency and reliability, not as a standalone quality
characteristic in this model.

**Check 3 — a professional architecture body's freely published body of knowledge (not paywalled).**
IASA's BTABoK, "Architecture Description" page —
https://iasa-global.github.io/btabok/architecture_description.html — fetched 2026-08-22. The page
states an Architecture Description's purpose is transforming "collected and organized architectural
information and intents into viable models, **describing the functional and non-functional requirements
of the architecture**." **This is a live, freely accessible architecture body of knowledge using
"non-functional requirements" as its own term, not "infrastructure requirements."**

**Check 4 — a major cloud provider's well-architected guidance (explicitly permitted per the brief).**
AWS Well-Architected Framework, via WebSearch synthesis of AWS's own pillar documentation — 2026-08-22,
**[SEARCH-SYNTHESIS]** of docs.aws.amazon.com/wellarchitected content, not independently raw-fetched:
"These pillars allow for systems to be architected such that they have **non-functional requirements
(NFRs)** addressed upfront, enabling the organization to focus on functional requirements." AWS's six
pillars — Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization,
Sustainability — are, on this framing, a decomposition of non-functional concerns for cloud
infrastructure specifically. **AWS names its own infrastructure-quality concerns via "non-functional
requirements," not "infrastructure requirements," as the umbrella term.**

**Check 5 — how "infrastructure requirements" is actually used where it does appear in practice.** A
search for infrastructure-requirements document templates, 2026-08-22, **[SEARCH-SYNTHESIS]**, found the
term used for a specific, narrower artifact: "Infrastructure requirements outline the specific
requirements for hardware, software, network, power, and other critical infrastructure elements...
specifications for the type, capacity, and performance requirements of servers, networking devices, and
storage systems; software requirements such as operating systems and middleware; network requirements
like bandwidth, latency, and security measures" — explicitly distinguished in the same material from a
functional-requirements document that also covers non-functional requirements as one of its own
sections. **This confirms the subset reading: where practitioners write an "infrastructure requirements
document," it is one physical/deployment-focused slice of the broader non-functional space, sitting
alongside — not replacing — the standard NFR category.**

**Verdict for the chapter, stated as the chapter should teach it:** treat "non-functional requirements"
as the term every standards/professional body in this pack uses for the category the exam blueprint
labels "infrastructure requirements." Teach the exam's phrase as this course's/blueprint's own label for
that same territory — most plausibly written by test-designers reaching for a more concrete,
less-abstract-sounding word than "non-functional" — while flagging that "infrastructure requirements"
also has real, narrower, independent currency (hardware/network/hosting specs) in practitioner
documents. A scenario option that reduces "infrastructure requirements" to *only* servers-and-networking
would be too narrow against the exam's own apparent usage (which sits at the same level as "functional,"
i.e., the full non-functional category); a scenario that treats "infrastructure requirements" as
identical to "functional requirements" is simply wrong under every source checked.

## RQ4 — Solution architecture, canonically defined as an input to requirements

**Source A — Wikipedia's "Solution architecture" article** —
https://en.wikipedia.org/wiki/Solution_architecture — fetched 2026-08-22 **[VIA-SUMMARIZER]** (processed
content, no visible inline citation markers preserved in the returned text; treat quoted phrases as
close paraphrase pending re-fetch). The article aggregates several named definitions rather than
asserting one on its own authority:

- **TOGAF-attributed:** "a description of a discrete and focused business operation or activity and how
  IS/IT supports that operation."
- **Gartner (2013), as reported by the article:** a solution architecture combines guidance from
  enterprise-architecture viewpoints (business, information, technical) applied to a specific solution.
- **Greefhorst & Proper (2013), as reported by the article** (academic source, *Architecture Principles:
  The Cornerstone for Enterprise Coherence*): architecture of a system offering coherent
  functionalities, encompassing the properties necessary to meet essential requirements.
- **Scaled Agile (2020), as reported:** solution architects communicate a shared technical vision across
  a "Solution Train" to ensure systems are fit for purpose.

**The level distinction, which is the direct answer to "solution architecture as an input to
requirements":** the article states solution architecture operates at the **tactical level**, addressing
a specific business problem or project, while enterprise architecture operates at the **strategic
level**, across the whole organization — both span business, information, application, and technology
architecture, but at different scope. Solution architecture is described as closely tied to actual
projects/initiatives — "the means to execute or realise a technology strategy." **Notable caveat the
article itself raises:** despite over 55,000 "Solution Architect" job postings referenced, **The Open
Group's TOGAF does not formally recognize a distinct "Solution Architect" role** in its skills framework
— solution architecture is a widely-practiced, industry-standard *term*, but not one uniformly codified
by the field's leading enterprise-architecture standard.

**Source B — a freely accessible professional body of knowledge, IASA's BTABoK** — 2026-08-22,
covering two pages: https://www.iasaglobal.org/solution-architecture/ **[VIA-SUMMARIZER]** and
https://iasa-global.github.io/btabok/architecture_description.html **[VIA-SUMMARIZER]**. IASA frames
solution architecture through **four primary aspects** delivered to stakeholders (the fetch did not
return the four aspects by name — see gap list), with certification-curriculum evidence of the
business-requirements link: a module explicitly titled "Business Architecture for Solutions, Strategy
and Business Models, Value Management, and how Business Cases impact solution success," and an
"EA/SA Bridge" module connecting enterprise- and solution-level architecture. Separately, BTABoK's
Architecture Description page (already cited in RQ3) states that an architecture description's role is
to capture and formalize "the functional and non-functional requirements of the architecture" — i.e.,
in this body's framing, **architecture description is downstream of requirements** (it documents and
formalizes them), which is the reverse direction from "architecture as an input to requirements." Both
directions are real and not contradictory: business/stakeholder requirements motivate an architecture,
and the resulting solution architecture then constrains and shapes the functional/non-functional
requirements that get written for a specific system — a feedback loop, not a one-way pipeline.

**Source C — TOGAF's own primary text: access result, reported honestly.** Three direct-fetch attempts
against The Open Group's own hosted TOGAF documentation
(`pubs.opengroup.org/togaf-standard/adm/chap01.html`, `pubs.opengroup.org/architecture/togaf8-doc/arch/chap15.html`,
and the legacy free mirror `togaf.org/chap01.html`) **all failed** — the first two redirect to an
OAuth/SSO login wall (`identity.opengroup.org`), the third failed on a TLS certificate mismatch (the
legacy domain's certificate no longer matches its hostname). **TOGAF's primary Requirements Management
phase text could not be read today.** What follows is WebSearch synthesis of secondary TOGAF-explainer
sites (Visual Paradigm, TopicTrick, Orbus Software), **[SEARCH-SYNTHESIS]**, not a TOGAF quotation:
Requirements Management is commonly depicted as the **central hub of the ADM's circular diagram**,
continuously feeding into and receiving from every lettered phase (Preliminary, A–H) rather than running
as one sequential phase with a start and end date; per this secondary material, "the requirements
management process itself does not dispose of, address, or prioritize any requirements: this is done
within the relevant phase of the ADM. It is merely the process for managing requirements throughout the
overall ADM." If this detail is used in the chapter, it should be presented as widely-reported
TOGAF-derived practitioner knowledge, not as a verified primary quotation — the primary source was not
reachable today.

**Discriminator RQ4 supports:** a scenario testing "does architecture come from requirements or do
requirements come from architecture" should be taught as bidirectional per Source B — business/
stakeholder requirements motivate the solution architecture, and the chosen architecture then shapes
which functional and non-functional requirements are written and how. A scenario conflating solution
architecture with enterprise architecture is testing the tactical-vs-strategic distinction in Source A.

---

# CHAPTER 33 — "Reading and reviewing code you did not write"

**Source discipline:** general engineering sources permitted per the Half Two preamble above; primary
and standards sources preferred, blogs flagged when used. This chapter draws on one long-established
primary practitioner reference (Google's Engineering Practices documentation), one formal IEEE standard
(accessed only at abstract/scope level — full text is a commercial document, same access pattern already
hit on ISO texts in Chapter 32), one historical primary source (Fagan's inspection method, read via
Wikipedia's treatment of it), one platform vendor's own responsible-use documentation (GitHub, for the
AI-reviewer-limits question), and one empirical research source (DORA/Accelerate) for the human-gate
question, which bridges directly into Chapter 34.

## RQ1 — Canonical purposes and practices of code review

**Source:** Google Engineering Practices, "The Standard of Code Review" —
https://google.github.io/eng-practices/review/reviewer/standard.html — fetched 2026-08-22
**[VIA-SUMMARIZER]** (fetch tool returned a processed answer, not raw page markdown; quoted phrases
below are reported as returned — re-fetch before quoting as verbatim page text in the final chapter).

Stated primary purpose, as returned: "The primary purpose of code review is to make sure that the
overall code health of Google's code base is improving over time."

Stated approval standard, as returned: "In general, reviewers should favor approving a CL [changelist]
once it is in a state where it definitely improves the overall code health of the system being worked
on, even if the CL isn't perfect." Nothing in the standard "justifies checking in CLs that definitely
worsen the overall code health of the system" — the two-sided rule (approve imperfect-but-improving
work; block regressive work) is the entire standard in one sentence.

A second, separately named purpose on the same page: teaching. "Code review can have an important
function of teaching developers something new about a language, a framework, or general software design
principles" — non-critical educational comments are marked as optional so they do not block the CL.

**Source, same documentation set:** "What to Look For In a Code Review" —
https://google.github.io/eng-practices/review/reviewer/looking-for.html — fetched 2026-08-22
**[VIA-SUMMARIZER]**. The documented review checklist, in the page's own order: **Design** ("the most
important thing to cover... do the interactions of various pieces of code in the CL make sense?"),
**Functionality** ("does this CL do what the developer intended? Is what the developer intended good for
the users of this code?"), **Complexity** (code where "developers are likely to introduce bugs when they
try to call or modify"), **Tests** (unit/integration/end-to-end as appropriate), **Naming**,
**Comments** (should "explain why some code exists" — information the code itself can't contain — not
restate what it does), **Style** (conformance to the team's style guide), and **Documentation** (READMEs
and reference docs kept current).

**Discriminator this gives directly:** design and functionality are documented as the priority — placed
before style or naming in the page's own list — so a scenario where a reviewer spends the cycle on
formatting nits while a design flaw ships is a misapplication of the reviewer's own documented priority
order, not a defensible stylistic disagreement.

**Historical/canonical grounding — why review is a distinct discipline from testing.** Source:
Wikipedia, "Fagan inspection" — https://en.wikipedia.org/wiki/Fagan_inspection — fetched 2026-08-22
**[VIA-SUMMARIZER]**. Michael Fagan formalized software inspection at IBM in 1976 ("Design and Code
Inspections to Reduce Errors in Program Development," IBM Systems Journal). The canonical six-step
process, as documented: **planning** (materials and participants arranged), **overview** (group
education, role assignment), **preparation** (individual review before the meeting), **inspection
meeting** (the actual defect-finding session), **rework** (correcting what was found), **follow-up**
(verifying the rework). The article's stated rationale for inspecting rather than relying on testing
alone: catching a defect early is documented as "10 to 100 times less" costly than fixing the same
defect during maintenance. On the specific system Fagan studied, inspection found a reported 38 defects
per KLOC versus 8 per KLOC from unit testing, and caught 82% of the defects eventually found in the
released product. **[VOLATILE — the specific defect-rate figures are a single 1976 IBM study; the
early-detection-is-cheaper principle is the durable claim, the multiplier is not]**

**Formal-standard grounding — the naming vocabulary an exam is more likely to test than a single vendor's
house terms.** Source: IEEE 1028-2008, "IEEE Standard for Software Reviews and Audits," abstract/scope —
https://standards.ieee.org/standard/1028-2008.html — fetched 2026-08-22 **[VIA-SUMMARIZER]**, full
standard text not accessible (commercial document). The standard's own scope: it defines **five** types
of software review and audit, each with its own required procedure: **management reviews, technical
reviews, inspections, walk-throughs,** and **audits**. The standard explicitly states it does not itself
define when a review is necessary or what to do with the results — it standardizes *how* each type is
run, not *whether* or *why* to run one.

**Discriminator this supports, and a naming trap worth flagging directly:** "code review" as practised on
a modern pull-request workflow (Google's CL review, a GitHub PR review) is colloquial usage, not one of
IEEE 1028's five formal names. It sits closest to — and is frequently described in secondary literature
as a lightweight, continuous descendant of — the **technical review** and **inspection** categories:
technical review evaluates a work product for conformance to specifications and fitness for its intended
use; inspection is the more rigorous, structured, defect-hunting variant Fagan formalized. A scenario
testing whether the candidate can distinguish an inspection (structured, role-based, with a rework-and-
follow-up loop) from a walkthrough (author-led, primarily educational, IEEE 1028's own separate category)
is testing this formal distinction — modern PR-based code review borrows from both traditions without
being formally either one.

## RQ2 — What an automated or AI reviewer can and cannot establish from a diff alone

**Source, a platform vendor's own documentation of the limits of its shipped feature — the strongest
tier available for this question.** GitHub, "Responsible use of GitHub Copilot code review" —
https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-review
— fetched 2026-08-22 **[RAW]** (direct quotes returned on fetch).

Documented limitations, verbatim: "Copilot may not identify all of the problems that are present in
code, especially where changes are large or complex." On hallucination risk: comments "generated by
Copilot code review should be carefully reviewed and considered before taking action" — flagged because
the tool can surface issues that are not actually present. On suggestion quality: generated code or fixes
"may appear to be valid but may not actually be semantically or syntactically correct, or may not
correctly resolve the problem." The page's own conclusion: "Copilot code review should be supplemented
with careful human code review."

**Source, procedural confirmation — GitHub's own workflow documentation, fetched separately.**
https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review —
fetched 2026-08-22 **[RAW]**: "Copilot always leaves a 'Comment' review, not an 'Approve' or 'Request
changes' review. Its reviews do not count toward required approvals and will not block merging." Its
comments otherwise "work like comments from human reviewers" in the interface — reactions, replies,
resolution — but structurally cannot satisfy a required-review gate. **This is a directly documented,
platform-enforced fact, not an inference:** an AI reviewer's output is treated as input to the review,
never as the approval itself.

**What this establishes about diffs specifically, synthesized from the two fetches above, not a further
quotation:** a diff shows the *change*, not the *reason* for the change or its *effect at runtime*.
Large/complex changes are the specific case GitHub's own documentation names as where problems get
missed — which is precisely where the relationship between a change and its downstream or runtime effect
is least visible from the lines that changed.

**Weaker-tier corroboration, flagged explicitly per this pack's convention — vendor and aggregator blog
content, WebSearch synthesis only, not independently fetched from a primary page:** 2026-08-22,
**[SEARCH-SYNTHESIS]**, aggregating several AI-code-review vendor blogs (Aviator, CodeRabbit, Codacy) and
one arXiv preprint: recurring claims that architectural alignment, business-logic correctness, and
cross-team or downstream impact require context a diff does not carry, and that reconstructing intent
from a diff alone — without the ticket, the PR description, or the "implementation journey" — is the
documented bottleneck these vendors built their products to address. **These are vendor claims about the
products they sell and should not be taught as standards-backed fact.** They are directionally consistent
with GitHub's own documented limitations above, which is the only reason they are reported here at all —
but they carry a commercial incentive to describe the problem as larger than a competing methodology
might, and none was corroborated on a primary fetch.

**Discriminator:** a scenario stating that an AI/automated reviewer flagged a change as clean and asking
whether that is sufficient to merge is directly testable against the GitHub-documented facts above — the
tool's own review type cannot satisfy a required-approval gate, and the vendor's own documentation names
large/complex changes as where it is most likely to miss something. A scenario asking what an automated
reviewer *is* good for (mechanical issues, style conformance, a fast first pass) is supported by the same
sources read the other way.

## RQ3 — Where a human gate is canonically placed

**Source:** GitHub Docs, "About protected branches" —
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
— fetched 2026-08-22 **[VIA-SUMMARIZER]**. The documented mechanism: repository administrators "can
require that all pull requests receive a specific number of approving reviews before someone merges the
pull request into a protected branch," and approving reviews must come "from people with write
permissions in the repository or from a designated code owner." Read together with RQ2's finding that an
AI reviewer's comments explicitly do not count toward this number, the gate is not merely "reviewed by
someone or something" — it is structurally reserved for a human (or a human-designated code-owner role)
by the platform mechanism itself.

**Source, empirical — where this gate is best placed in the larger change-management picture, not just
the repository.** DORA (DevOps Research and Assessment, Google Cloud), "Streamlining Change Approval" —
https://dora.dev/capabilities/streamlining-change-approval/ — fetched 2026-08-22 **[RAW]**. This source
draws on the Accelerate / State of DevOps Report research program and speaks directly to a common
exam-shaped distractor pair: a heavyweight, separate change-approval board versus review folded into the
development workflow itself.

Verbatim, describing the traditional external-board pattern: "Reliance on a centralized Change Approval
Board (CAB) to catch errors and approve changes. This approach can introduce delay and often error," and
"heavyweight approaches tend to slow down the delivery process leading to the release of larger batches
less frequently, with an accompanying higher impact on the production system." The research finding,
stated directly: "no evidence was found to support the hypothesis that a more formal, external review
process was associated with lower change fail rates."

The documented alternative, stated as the recommended practice: "Use peer review to meet the goal of
segregation of duties, with reviews, comments, and approvals captured in the team's development platform
as part of the development process." A modernized CAB, where one still exists, is redirected toward
"facilitating notification and coordination between teams" rather than gatekeeping every change.

**Discriminator, and the bridge from this chapter into Chapter 34:** a scenario describing a separate,
formal, external approval body sitting between "code merged" and "code deployed" is describing the
pattern DORA's research found *worse* for stability than no separate approval step at all — not a safer
option, however much safer it sounds when read cold. A scenario describing mandatory peer review captured
in the same platform the code was written in — the pull-request gate from RQ1–RQ2 above — is describing
the practice the same research found effective for the same stated goal (segregation of duties) without
the delay cost. **The human gate is canonically placed at the peer-review point inside the development
workflow, not at a downstream external board** — the same gate this chapter's first two questions already
located structurally (required PR approval) and functionally (AI review does not satisfy it).

---

# CHAPTER 34 — "Changing a live system without breaking it"

**Source discipline:** as declared for Half Two. This chapter checks five distinct frameworks against the
exam's own four-term phrasing (develop, implement, operate, maintain) rather than assuming any one of
them is the source — the same discipline Chapter 32 applied to "infrastructure requirements." ISO
standard text remains commercially blocked (the same access class already confirmed in Chapter 32, not
re-tested here); NIST's own PDF could not be parsed by the fetch tool despite being freely hosted, a
different failure mode from a paywall and flagged where it occurs below. Refactoring is sourced to the
field's own originating reference (Martin Fowler) and to a major engineering organization's public
documentation of the same practice at scale (Google, via its freely published engineering book). Version
control is sourced to DORA/Accelerate, the empirical research program the brief permits and already used
in Chapter 33.

## RQ1 — Canonical SDLC phase models, and whether any one names develop/implement/operate/maintain

**The exam's own four terms were searched for as a literal set first, deliberately, before consulting any
individual framework — result: no framework checked uses exactly this four-term set as its own named
phase list.** What follows is what each framework actually does name, so the chapter can teach the real
vocabulary rather than force a fit.

**ISO/IEC/IEEE 12207 — the standard the field treats as authoritative for this question.** Primary-text
access result: standards.iso.org and the OBP viewer sit behind commercial access, the same class of block
Chapter 32 already hit and documented, not re-tested here. What is established via a secondary technical
summary — arc42's quality-model reference, https://quality.arc42.org/standards/iso12207, fetched
2026-08-22 **[VIA-SUMMARIZER]**, describing the 2017 edition: the standard organizes work into four
process groups — **Agreement**, **Organizational Project-Enabling**, **Technical Management**, and
**Technical** processes. Inside **Technical Management Processes** sits **configuration management** as
its own named process — the standards-level home for what this chapter's RQ3 calls version control.
Inside **Technical Processes**, three of the exam's four terms appear as separately named processes, each
with its own one-line documented scope: **Implementation** ("realization of software components according
to design specifications"), **Operation** ("deployment and operation of software in its intended
environment"), and **Maintenance** ("evolution and support of software throughout its operational life").
**"Development" is not a fourth co-equal Technical Process alongside these three in the 2017 list** — the
pre-implementation technical processes (business/mission analysis, requirements, architecture, design) are
what "development" informally names as a group, not one named process. **[VOLATILE — process names have
shifted between editions; treat "12207" as a standard family, not one frozen wording]**

**Where "Development" does appear as a peer to Operation and Maintenance: the standard's own lineage.**
The same secondary source states the original 1995 edition "was divided into five primary processes
(acquisition, supply, **development**, **operation**, and **maintenance**)" — the older structure had
Development as a single umbrella primary process sitting beside Operation and Maintenance, with
Implementation as one internal activity of Development rather than its own top-level process. **The
2017 technical-process list and the 1995 primary-process list are two different segmentations of the same
underlying lifecycle, not the same list under two names** — which of the exam's four terms sit at the same
level depends on which edition is being described.

**NIST SP 800-64 Rev. 2 — a second, independent framework, U.S. federal and freely published (though
withdrawn).** Status confirmed via direct fetch of its own record page,
https://csrc.nist.gov/pubs/sp/800/64/r2/final, fetched 2026-08-22 **[VIA-SUMMARIZER]**: the document "was
withdrawn on May 31, 2019," with NIST directing readers to **SP 800-160 Volume 1** for current guidance.
**The five-phase list itself could not be confirmed on a raw fetch** — two direct attempts against the
hosted PDF (nvlpubs.nist.gov) both returned only encoded PDF stream data the fetch tool could not parse
into text, a distinct failure mode from a paywall: the document is free, the extraction failed. What is
reported below is therefore **[SEARCH-SYNTHESIS]** only, corroborated across two independent searches,
2026-08-22: **Initiation, Development/Acquisition, Implementation/Assessment, Operations/Maintenance,
Disposition.** If accurate, this is a third segmentation again — Development and Acquisition sharing one
phase, Implementation named on its own, Operations and Maintenance sharing one phase rather than standing
separately the way 12207's technical processes do.

**ITIL — both editions checked, because the current one differs materially from the one most search
results default to.** ITIL v3's five-stage service lifecycle — Service Strategy, Service Design,
**Service Transition**, **Service Operation**, Continual Service Improvement — is what most secondary
ITSM material (practitioner and vendor ITSM sites; 2026-08-22, **[SEARCH-SYNTHESIS]**, AXELOS's own
primary text not reached in this session) still describes by default, but v3 is the legacy structure. The
**current** framework, ITIL 4, replaced the lifecycle with a **Service Value Chain** of six activities —
Plan, Improve, Engage, **Design & Transition**, **Obtain/Build**, **Deliver & Support** — per the same
class of secondary ITSM sources, 2026-08-22, **[SEARCH-SYNTHESIS]**. Neither edition uses "implement,"
"operate," or "maintain" as its own term: v3 says **Transition** where the exam says implement, and folds
maintenance-type work into **Operation** and **Continual Service Improvement** rather than naming it
separately; ITIL 4 says **Obtain/Build** and **Design & Transition** across what the exam calls
develop/implement, and folds operate-and-maintain together into one activity, **Deliver & Support**. **A
scenario using ITIL vocabulary (Transition, Deliver & Support) should not be mapped one-for-one onto the
exam's own four terms** — they are different frameworks' words for overlapping but non-identical
territory.

**A historical primary source worth naming precisely, because it is commonly misquoted.** Winston Royce's
1970 paper, "Managing the Development of Large Software Systems: Concepts and Techniques" (WesCon 1970) —
not independently fetched from a primary archive this session; reported via two converging secondary
sources, 2026-08-22, **[SEARCH-SYNTHESIS]**, with a flagged inconsistency between them: one source lists
seven steps ending in **Coding, Testing, Operations**; another, describing the same paper, compresses the
same territory into five steps ending in **"operation and maintenance"** as one combined final phase. Both
secondary sources agree on the historically load-bearing point: **Royce presented this sequential model as
an example that does not work**, and argued for iteration between adjacent steps — the strict, one-pass
"waterfall" reading became the industry's name for a model its own author was critiquing. **[VOLATILE and
unverified at primary-source level, flagged again below — the exact step count is secondary-sourced and
inconsistent between sources; "Royce critiqued his own strawman" is the more load-bearing fact and is
where both sources agree.]**

**A fifth reference point, current and vendor-neutral in principle though not standards-body-owned: the
"DevOps lifecycle" loop.** Reported consistently across several vendor documentation sites (2026-08-22,
**[SEARCH-SYNTHESIS]**, no single primary owner identified — this is now genericized industry vocabulary,
not one company's proprietary framework): eight phases, **Plan, Code, Build, Test** on the development
side and **Release, Deploy, Operate, Monitor** on the operations side, conventionally drawn as an infinity
loop because "the output of Monitor... becomes the input of Plan." Like ITIL, this loop has no separate
"maintain" step — ongoing maintenance is distributed across the whole cycle rather than named once.

**Verdict for the chapter, stated as it should be taught:** the exam's "develop, implement, operate,
maintain" reads as a **pedagogical compression**, closest in spirit to ISO/IEC/IEEE 12207:2017's technical
processes (which do separately name Implementation, Operation, and Maintenance) with the earlier technical
processes — requirements, architecture, design — folded into a single "develop" for teaching purposes, the
way 12207's own 1995 edition folded them into one "Development" primary process. This is the same finding
shape as Chapter 32's "infrastructure requirements" verdict: real vocabulary, real standards, but the
exact four-word framing is most plausibly the course's or blueprint's own simplification rather than one
framework's verbatim phrase — no source checked contradicts the four stages as a *sequence*, only the claim
that any single framework names all four terms identically.

## RQ2 — Refactoring, canonically defined at small and large scale

**Small scale — the field's originating reference.** Source: Martin Fowler, "Refactoring" —
https://martinfowler.com/books/refactoring.html — fetched 2026-08-22 **[RAW]**. Verbatim: "Refactoring is
a controlled technique for improving the design of an existing code base. Its essence is applying a
series of small behavior-preserving transformations, each of which [is] 'too small to be worth doing'."
On why small steps specifically: "The cumulative effect of each of these transformations is quite
significant. By doing them in small steps you reduce the risk of introducing errors," and the discipline
lets a team "gradually refactor a system over an extended period of time" without the system ever being
left broken mid-restructure. The book this page describes catalogs roughly seventy named refactorings,
each with motivation, mechanics, and an example — refactoring, on this definition, is a **named,
catalogued technique**, not a loose synonym for "cleaning up code."

**Discriminator embedded in the definition itself:** a change that alters observable behavior is not a
refactoring under this definition, however small — behavior-preservation is not a side-effect of the
technique, it is the technique's defining constraint. A scenario describing a change that fixes a bug or
adds a capability, however minor, is describing something other than a refactoring by this canonical
definition, whatever the change is colloquially called on the team making it.

**Large scale — where the small-scale definition's own assumption breaks, documented by the organization
that hit the limit.** Source: "Software Engineering at Google," Chapter 22, "Large-Scale Changes" —
https://abseil.io/resources/swe-book/html/ch22.html — fetched 2026-08-22 **[VIA-SUMMARIZER]**. Defined
verbatim: a Large-Scale Change (LSC) is "any set of changes that are logically related but cannot
practically be submitted as a single atomic unit" — because the change touches more files than the
version-control system can commit as one unit, or because the changes are so extensive that merge
conflicts become unavoidable if attempted as one. The chapter's own framing of why this is a different
problem, not just a bigger version of the same one: as a codebase and its engineering population grow,
"the maximum size of atomic changes actually decreases" rather than increases — so the ordinary,
small-scale refactoring assumption (bundle logically-related edits into one atomic commit, per Fowler
above) becomes unusable exactly where a change is most sweeping, not more usable.

Documented principles for doing this safely, as returned: **automation over manual editing** (LSC tooling
generates the change; humans do not hand-edit each of potentially thousands of call sites); **sharding**
(one logically-related change is split into many small, independently-submittable, independently-testable
pieces — each individual shard is small in Fowler's sense even though the aggregate is not); **transitive
test coverage per shard** to catch unintended effects; **centralized ownership**, with the infrastructure
team driving the migration rather than an unfunded mandate landing on every product team; and **prevention
mechanisms** (static checks that block reintroduction of the pattern being removed, so the large change
does not silently erode over time).

**The discriminator this pair of sources supports directly:** small-scale refactoring is defined by
*behavior preservation within one reviewable, atomic change*; large-scale refactoring is defined by what
happens when the change is logically one thing but **cannot** be one atomic change — the documented
response is not "do the same thing, just bigger," it is a different discipline (automated generation,
sharding, per-shard testing, drift prevention) built specifically because the atomic-commit safety net
Fowler's definition relies on does not scale. A scenario contrasting "one team refactors one module" with
"a single naming or API change must land across hundreds of call sites and teams" is testing whether the
candidate reaches for Fowler's small-steps discipline or Google's LSC discipline — both are refactoring,
canonically, but they are not the same technique at greater volume.

## RQ3 — Version control as a safety mechanism during change

**Source:** DORA (DevOps Research and Assessment, Google Cloud), "Version Control" —
https://dora.dev/capabilities/version-control/ — fetched 2026-08-22 **[RAW]**. Definition, verbatim:
version control systems "provide a logical means to organize files and coordinate their creation,
controlled access, updating, and deletion across teams and organizations." The page states that version
control statistically "predicts continuous delivery" as a capability — DORA's own research vocabulary for
a measured predictive relationship, not a forecasting claim — i.e., it is documented as a precondition
correlated with being able to deliver changes safely and often, not an optional accompaniment to it.

**What the page documents belongs in version control — not application code alone, verbatim list:**
application code and dependencies; database schema scripts and reference data; environment-creation
tooling (Terraform, Docker files); automated tests and test scripts; deployment and provisioning scripts;
AI artifacts (prompts, agent configuration files); container-orchestration configuration; cloud
configuration files (CloudFormation, Pulumi); and infrastructure and network configuration scripts. The
canonical claim here is that version control's safety function is documented as covering the whole system
that must move together — code and its supporting infrastructure/configuration as one version-controlled
unit — not source code narrowly.

**On the safety-net function specifically, verbatim:** "Version control is our safety net. It allows us
to revert AI-generated mistakes instantly and gives us a history we can audit." The page connects version
control to a named list of downstream capabilities it enables: disaster recovery, auditability, higher
quality, capacity management, and rapid response to defects — stating specifically that it lets a team
"roll back to a previously verified working state quickly and reliably."

**Corroborating source, same research program, a specific practice rather than the general capability.**
DORA, "Trunk-based development" — https://dora.dev/capabilities/trunk-based-development/ — fetched
2026-08-22 **[RAW]**. Defined verbatim: "Each developer divides their own work into small batches and
merges that work into trunk at least once (and potentially several times) a day," which "reduces the
complexity of merging events and keeps code current by having fewer development lines and by doing small
and frequent merges." The empirical claim attached: teams practising this "achieve higher levels of
software delivery and operational performance (delivery speed, stability, and availability)." This
directly connects RQ2's small-scale refactoring discipline (small, individually safe steps) to RQ3's
version-control discipline (small, frequent, trunk-bound commits) — both are documented as deriving their
safety from the same mechanism: keeping each individually-committed change small enough to reason about
and revert cleanly, rather than making a large change safe by being careful within it.

**Corroborating source, a major cloud provider's own operational guidance (explicitly permitted per the
brief).** AWS Well-Architected Framework, Operational Excellence pillar, "Evolve" —
https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-evolve.md — fetched 2026-08-22 **[RAW]**.
Under its own numbered practice OPS 11 ("How do you evolve operations?"), verbatim: "Successful evolution
of operations is founded in: frequent small improvements; providing safe environments and time to
experiment, develop, and test improvements; and environments in which learning from failures is
encouraged." AWS's own documented mechanism for this: "operations support for sandbox, development, test,
and production environments, with increasing level of operational controls" — the same change moves
through progressively stricter gates rather than jumping straight from a developer's machine to
production, with version control implicitly the mechanism that makes "the same change" a well-defined,
promotable, revertible object at every stage.

**Discriminator:** a scenario asking what makes a change to a live system safely reversible should be
answered with version control's documented role — a single committed, revertible, auditable unit that
travels through environments — not with "careful testing" alone; testing and version control are
documented as complementary, not substitutes for each other (AWS's own framing pairs "safe environments
and time to... test improvements" with the small-batch, revertible-commit discipline, not instead of it).

## RQ4 — SDLC integration: how these three findings compose into one picture

This question is a synthesis, not a fourth independent research thread — grounded entirely in RQ1–RQ3
above, not a new claim.

Read together, the three RQs above describe one connected picture rather than three separate topics.
**Develop** and **implement** (RQ1, closest to ISO/IEC 12207's technical processes) are where **small-scale
refactoring** (RQ2, Fowler) and **trunk-based, version-controlled small commits** (RQ3, DORA) are the
documented safety mechanism — each change small enough to be one atomic, revertible, reviewable unit,
which is also where Chapter 33's peer-review gate sits. **Operate** and **maintain** are where a
correction to something already live has to be made either as another small, version-controlled, reviewed
change (the same mechanism, run again) or, if the change is a sweeping one that cannot be made atomic — a
mass API deprecation, a security-driven library migration — where the **large-scale change** discipline
from RQ2 (Google's LSC: automate, shard, test each shard, prevent drift) becomes the operative technique
specifically because the ordinary safety net stops covering the size of change being made.

**The cross-reference to Chapter 33, stated once rather than re-derived:** the human gate this chapter's
"implement" stage relies on is the same peer-review gate Chapter 33 located structurally (required PR
approval, not satisfied by an AI reviewer's comment) and empirically (DORA's finding that a downstream
external change-approval board is *worse* for stability than peer review folded into the development
platform). A scenario that separates "the developer's safety practice" from "the operations team's change
control" as if they were two different mechanisms is describing a division the DORA research specifically
found unsupported — the documented safety mechanism for developing, implementing, operating, and
maintaining a system is the same one, run continuously: small version-controlled changes, peer-reviewed
before merge, promoted through environments with increasing control, revertible at every stage.

---

# CLOSING — WHAT THIS PACK COULD NOT ESTABLISH, AND WHAT CAME ONLY FROM WEAK SOURCES

Covers all four chapters in this pack (6, 32, 33, 34), written once at the end rather than duplicated per
chapter, per the brief. Nothing below is new research — it indexes gaps and fidelity-tier facts already
flagged inline above, plus a small number of access-attempt failures that are noted here for the first
time because they produced no citable content and so never appeared in the chapter text itself (SWEBOK,
the two NIST PDF attempts).

## What could not be established

**Chapter 6** (for completeness — this chapter is the strongest-sourced in the pack; both gaps below are
already flagged inline and are narrow):
- The exact sentence "Put everything else, like task-specific instructions, in the user turn instead"
  (attributed to a system-prompts page by an earlier search synthesis) was **not** found verbatim on any
  page reached by direct fetch. The underlying *pattern* it describes (role in system, task in user) is
  independently verified structurally via Anthropic's own worked code example; this specific wording is
  not. See RQ3.
- Anthropic's documentation does not define "zero-shot" as a named prompting technique anywhere (confirmed
  absent from the Glossary and from the multishot section on direct fetch, and from two site-restricted
  searches). This is a confirmed finding of absence, not an open gap — but it means no Anthropic-sourced,
  technique-level guidance exists to cite for zero-shot specifically, only for few-shot/multishot. See RQ2.

**Chapter 32:**
- IIBA's BABOK Guide — the standard reference for "business requirements" — could not be read past its
  navigation shell; both direct fetches hit a member-login wall. The requirements-classification hierarchy
  reported (Business → Stakeholder → Solution [Functional/Non-Functional] → Transition) is
  SEARCH-SYNTHESIS of secondary explainer pages describing BABOK, not a BABOK quotation. See RQ1.
- ISO/IEC 25010 — both the 2011 abstract page and the 2023 edition's OBP viewer returned 403 Forbidden.
  The exact count of quality characteristics in the current (2023) edition was explicitly flagged as "not
  independently confirmed." See RQ3, Check 2.
- TOGAF's own primary Requirements Management text could not be read: two attempts against
  pubs.opengroup.org redirected to an OAuth/SSO login wall, and the legacy free mirror (togaf.org) failed
  on a TLS certificate mismatch. All ADM-related claims in RQ4 Source C are SEARCH-SYNTHESIS of secondary
  TOGAF-explainer sites, not TOGAF quotations.
- IASA's BTABoK: the "four primary aspects" of solution architecture that the body's own framing refers to
  were never returned by name on any fetch attempted. The existence of the four-aspect framing is
  reported; its content is not. See RQ4, Source B.

**Chapter 33:**
- SWEBOK (IEEE Computer Society), Chapter 10 "Software Quality" — the wiki page returned 403 Forbidden on
  the only attempt made. **No SWEBOK content was used anywhere in Chapter 33 as a result** — a real gap in
  a chapter about code review, since SWEBOK is a standard reference for software-quality practice
  including reviews, and it was not reached even at the abstract level IEEE 1028 was. The official PDF
  (ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf, located in search results but not
  fetched this session) is the natural next attempt.
- Two NIST sources on static-analysis/automated-review limitations (SP 500-297, and a paper by Paul E.
  Black at tsapps.nist.gov/publication/get_pdf.cfm?pub_id=901506) were located but **both returned
  unparseable PDF binary data on fetch** — a distinct failure mode from a paywall, hit again in Chapter 34
  against NIST SP 800-64. Neither is cited in the chapter text because nothing readable was returned; RQ2's
  material on static-analysis limits rests on weaker vendor-blog sourcing as a direct consequence.
- IEEE 1028-2008's full text (the five review/audit types and their required procedures) was read only at
  abstract/scope level via standards.ieee.org. The procedural detail — what a "technical review" requires
  that a "walkthrough" does not, beyond the one-line summaries reported — is a commercial document and was
  not read.

**Chapter 34:**
- ISO/IEC/IEEE 12207's primary text was not attempted directly (the same commercial-access class Chapter
  32 already confirmed blocked); all 12207 content rests on one secondary technical summary (arc42), not
  the standard itself. This is the single largest unverified load-bearing claim in the whole pack: RQ1's
  entire verdict depends on "Implementation / Operation / Maintenance are three separately named Technical
  Processes," which has not been checked against ISO's own text.
- NIST SP 800-64 Rev. 2's five-phase list (Initiation, Development/Acquisition, Implementation/Assessment,
  Operations/Maintenance, Disposition) is SEARCH-SYNTHESIS only. Two direct fetch attempts against the
  hosted PDF both returned encoded stream data, not text — the document is free (unlike ISO/BABOK/TOGAF)
  but the fetch tool could not extract it. The document is also withdrawn (2019) and superseded by SP
  800-160 Vol. 1, which was never fetched at all — a clear next step if this chapter is revised.
- ITIL — neither v3 nor ITIL 4 primary text (AXELOS/PeopleCert) was reached. Every phase/activity name
  reported for both editions is SEARCH-SYNTHESIS from practitioner ITSM sites, not the framework's own
  publication.
- Winston Royce's original 1970 paper was never located and fetched directly. The two secondary sources
  used disagree with each other on the step count (seven steps vs. five) — the disagreement is reported
  in-chapter rather than resolved, because resolving it needs the primary paper, which this session did
  not reach.
- The "DevOps lifecycle" eight-phase loop has no identified primary owner or standards body — by its
  nature it may not have one — so "canonical" is a stretch for this specific item; it is reported as
  widely-documented industry vocabulary, not a named framework's own standard.
- AWS Well-Architected: only the "Evolve" best-practice page (oe-evolve.md) under Operational Excellence
  was read in full. Three sibling pages seen only as navigation entries — oe-organization.md,
  oe-prepare.md, oe-operate.md — were never opened. "Prepare" in particular is a plausible location for
  more AWS-specific version-control/change-management guidance this pack does not contain.

## What came only from weak (non-authoritative) sources

This is about source *tier*, not correctness — everything below may well be accurate, but it should not
be taught as if it carries a standards body's or a primary vendor's authority, and a stronger source
should replace it if one becomes reachable later.

**[SEARCH-SYNTHESIS]** items (WebSearch's own synthesized answer, no follow-up fetch of the underlying
page) that teaching content actually depends on, not just corroborates:

- **Chapter 32:** the entire BABOK requirements-classification hierarchy (RQ1); ISO/IEC 25010's quality-
  characteristic list (RQ3, Check 2); the "infrastructure requirements" practitioner-document meaning
  (RQ3, Check 5); the AWS Well-Architected NFR framing (RQ3, Check 4); the TOGAF ADM/Requirements
  Management description (RQ4, Source C).
- **Chapter 33:** the vendor-blog material on what AI code review cannot see (Aviator, CodeRabbit, Codacy,
  one arXiv preprint) — flagged explicitly in-chapter as carrying commercial incentive, since these
  vendors sell the product being described as necessary.
- **Chapter 34:** nearly all of RQ1's framework survey outside the one arc42-sourced ISO summary — NIST
  SP 800-64's phase list, both ITIL editions' activity names, Royce's original phase count, and the
  DevOps loop's eight phases are all SEARCH-SYNTHESIS. **RQ1 is the weakest-sourced research question in
  this entire pack:** five frameworks were surveyed and only one (ISO/IEC 12207, via secondary summary)
  goes beyond search synthesis at all, and even that one never reached ISO's own text.

**[VIA-SUMMARIZER]** items (a real page was fetched, but the tool returned a processed answer rather than
raw source text — reliable but not verbatim, flagged wherever chapter text quotes it as if exact wording):

- **Chapter 6:** none. Every Chapter 6 citation is **[RAW]** — this chapter is the firmest-sourced in the
  pack, a direct consequence of its narrower, single-host source discipline (platform.claude.com only).
- **Chapter 32:** both Wikipedia articles used (Non-functional requirement, Solution architecture) and
  both IASA BTABoK pages.
- **Chapter 33:** both Google Engineering Practices pages, the Fagan inspection Wikipedia article, the
  IEEE 1028 abstract page, and the GitHub "About protected branches" page. RQ2 and the second half of RQ3
  rest instead on **[RAW]** GitHub and DORA fetches and are on firmer footing than RQ1.
- **Chapter 34:** the arc42 ISO/IEC 12207 summary, the NIST SP 800-64 withdrawal-notice page, and the
  Google "Software Engineering at Google" LSC chapter. RQ2's Fowler citation and all of RQ3 (DORA ×2, AWS)
  are **[RAW]** and are the firmest ground in the chapter.

**Cross-chapter pattern worth naming once, since it recurs across both halves of this pack:** every time a
commercial standards body's text was the natural first source — ISO/IEC 25010, ISO/IEC 12207, IEEE 1028
beyond its abstract, BABOK, TOGAF — it was inaccessible without payment or membership, and the pack fell
back to secondary summaries of that same text. **No fact in this pack that depends on a paywalled
standard's exact wording should be taught as a verbatim standards quotation.** Only Chapter 6's
Anthropic-controlled sources and the freely-hosted primary sources named above — Google Engineering
Practices, GitHub's own documentation, DORA, AWS Well-Architected, Martin Fowler, Google's SWE book,
Wikipedia, arc42, and NIST's own withdrawal-notice pages — were read in full or in raw form. Everything
else in Chapters 32–34 is one step removed from the text it describes, by varying distances, and the
distance is marked at every point it matters above.
