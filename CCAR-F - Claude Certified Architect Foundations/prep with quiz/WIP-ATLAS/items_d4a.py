# Domain 4 part A — Prompt Engineering & Structured Output · building: the courthouse

ITEMS = [
{
 "id": "D4-01",
 "title": "Explicit categorical criteria beat vague instructions",
 "concept": "Precision comes from explicit categorical criteria — which issues to report and which to skip — not from general instructions like \"be conservative\" or \"only report high-confidence findings\".",
 "tested": "The review flags accurate comments as problems, and the question asks the most effective prompt change. The answer replaces the vague intent with a testable rule — flag a comment only when the behaviour it claims contradicts the code — and names which categories to report and which to skip. Distractors restate the same vague intent in stronger words, or filter by a self-reported confidence threshold, neither of which changes what the model counts as a finding.",
 "remember": "Vague adjectives do not raise precision. Write the categorical rule: report bugs and security, skip minor style and local patterns. A confidence threshold is the distractor.",
 "analogy": "A statute lists the elements of the offence, and the judge convicts only when every element is met. A direction to the bench to be reasonable, or to convict only when sure, decides no case differently, because it never says which facts count.",
 "svg": """<rect class="paper" x="16" y="18" width="72" height="84" rx="3"/>
<rect class="acc" x="26" y="32" width="10" height="10"/><line class="acc" x1="44" y1="37" x2="78" y2="37"/>
<rect class="acc" x="26" y="52" width="10" height="10"/><line class="acc" x1="44" y1="57" x2="78" y2="57"/>
<rect class="acc" x="26" y="72" width="10" height="10"/><line class="acc" x1="44" y1="77" x2="78" y2="77"/>
<text class="lbl" x="123" y="30" text-anchor="middle">vague</text>
<rect class="tint" x="102" y="38" width="42" height="44" rx="3"/>
<line class="dash thin" x1="110" y1="54" x2="136" y2="54"/>
<line class="dash thin" x1="110" y1="66" x2="128" y2="66"/>
<line class="no" x1="106" y1="42" x2="140" y2="78"/>
<line class="no" x1="140" y1="42" x2="106" y2="78"/>""",
 "alt": "Statute sheet with three ticked criteria; a vague sheet crossed out",
},
{
 "id": "D4-02",
 "title": "False positives erode trust — disable the noisy category",
 "concept": "A category with a high false-positive rate makes developers dismiss findings from the accurate categories too, so that category is switched off while its prompt is improved.",
 "tested": "Per-category false-positive rates are given, style and documentation high against security and performance low, developers dismiss every finding, and the question asks how to restore trust. The answer temporarily disables the noisy categories and keeps the precise ones running while their prompts are rewritten. Distractors attach a confidence score to every finding and still show them all, cut strictness uniformly across categories, or work through examples for every category over several weeks.",
 "remember": "A high false-positive category discredits the accurate ones. Turn it off now, fix its prompt, turn it back on. Confidence displays and uniform strictness cuts are the distractors.",
 "analogy": "One list of charges the court throws out week after week teaches the public that the whole docket is worthless, and the sound convictions on the next list are read as noise. The court suspends that list until it is drafted properly and keeps hearing the ones that stand up.",
 "svg": """<rect class="paper" x="20" y="14" width="76" height="92" rx="3"/>
<line class="thin" x1="30" y1="32" x2="86" y2="32"/>
<line class="thin" x1="30" y1="44" x2="86" y2="44"/>
<line class="no" x1="26" y1="26" x2="90" y2="50"/>
<line class="no" x1="90" y1="26" x2="26" y2="50"/>
<text class="lbl" x="122" y="44" text-anchor="middle">off</text>
<line class="acc" x1="30" y1="72" x2="86" y2="72"/>
<line class="acc" x1="30" y1="86" x2="86" y2="86"/>
<circle class="acc" cx="122" cy="79" r="19"/>
<circle class="acc thin" cx="122" cy="79" r="13"/>""",
 "alt": "Docket with the noisy category struck out; the precise one stamped",
},
{
 "id": "D4-03",
 "title": "Severity levels defined by concrete code examples",
 "concept": "Severity classification stays consistent when each level is defined by explicit criteria with a concrete code example attached, rather than by an instruction to rate severity appropriately.",
 "tested": "The same class of issue comes back as critical in one run and medium in the next, and the question asks how to make classification consistent. The answer writes explicit criteria per level and attaches a concrete code example to each one. Distractors ask for severity to be rated appropriately, or filter by a confidence score rather than defining the levels.",
 "remember": "One example of real code per severity level. Definitions plus examples make the boundary testable; an instruction to rate appropriately leaves it to the run.",
 "analogy": "The sentencing grid does not tell the judge to be proportionate; it sets out bands and prints a decided case in each one. Two judges reading the same grid put the same offence in the same band, because they are matching against examples rather than against their own sense of gravity.",
 "svg": """<rect class="tint" x="14" y="16" width="46" height="20" rx="2"/>
<rect class="tint" x="14" y="42" width="46" height="20" rx="2"/>
<rect class="tint" x="14" y="68" width="46" height="20" rx="2"/>
<rect class="tint" x="14" y="94" width="46" height="16" rx="2"/>
<text class="lbl" x="37" y="30" text-anchor="middle">crit</text>
<text class="lbl" x="37" y="56" text-anchor="middle">high</text>
<text class="lbl" x="37" y="82" text-anchor="middle">med</text>
<text class="lbl" x="37" y="106" text-anchor="middle">low</text>
<rect class="acc" x="76" y="16" width="70" height="20" rx="2"/>
<rect class="acc" x="76" y="42" width="70" height="20" rx="2"/>
<rect class="acc" x="76" y="68" width="70" height="20" rx="2"/>
<rect class="acc" x="76" y="94" width="70" height="16" rx="2"/>
<line class="acc thin" x1="84" y1="26" x2="112" y2="26"/>
<line class="acc thin" x1="84" y1="52" x2="118" y2="52"/>
<line class="acc thin" x1="84" y1="78" x2="106" y2="78"/>
<line class="acc thin" x1="84" y1="103" x2="114" y2="103"/>""",
 "alt": "Four severity bands, each paired with a concrete code example",
},
{
 "id": "D4-04",
 "title": "Few-shot examples for consistent format when instructions fail",
 "concept": "Few-shot examples showing the exact required shape — location, issue, severity, suggested fix — are the most effective technique when detailed instructions alone produce inconsistent output.",
 "tested": "The output format varies run to run although the prompt already specifies it, and the question asks the most effective improvement. The answer adds examples demonstrating the exact format. The distractor rewrites the instructions to be longer or more explicit, which adds text to something that is already failing.",
 "remember": "Format inconsistent despite instructions → show the shape, do not describe it again. More explicit wording is the standing distractor wherever examples are the answer.",
 "analogy": "The clerk handed a memo describing how findings should be laid out returns a different layout every week. Two completed forms laid on the desk, as the pattern to follow, end the variation; a longer memo does not.",
 "svg": """<rect class="acc" x="14" y="20" width="34" height="40" rx="2"/>
<line class="acc thin" x1="20" y1="32" x2="42" y2="32"/>
<line class="acc thin" x1="20" y1="44" x2="36" y2="44"/>
<rect class="acc" x="14" y="66" width="34" height="40" rx="2"/>
<line class="acc thin" x1="20" y1="78" x2="42" y2="78"/>
<line class="acc thin" x1="20" y1="90" x2="36" y2="90"/>
<path d="M56 62 h16 M66 56 l6 6 -6 6"/>
<rect class="paper" x="80" y="18" width="30" height="38" rx="2"/>
<line class="thin" x1="86" y1="30" x2="104" y2="30"/><line class="thin" x1="86" y1="42" x2="98" y2="42"/>
<rect class="paper" x="80" y="68" width="30" height="38" rx="2"/>
<line class="thin" x1="86" y1="80" x2="104" y2="80"/><line class="thin" x1="86" y1="92" x2="98" y2="92"/>
<rect class="paper" x="116" y="43" width="30" height="38" rx="2"/>
<line class="thin" x1="122" y1="55" x2="140" y2="55"/><line class="thin" x1="122" y1="67" x2="134" y2="67"/>""",
 "alt": "Two example forms producing three outputs in the same layout",
},
{
 "id": "D4-05",
 "title": "Aim examples at the ambiguous cases, with the reasoning",
 "concept": "Two to four examples aimed at the ambiguous cases, each showing why one action was chosen over a plausible alternative, let the model generalise its judgment to new patterns.",
 "tested": "Requests that sit between two tools are misrouted, or borderline coverage gaps are missed, and the question asks what to add. The answer is a small set of examples on exactly those borderline cases, each carrying the reasoning for the choice. The distractor supplies ten to fifteen examples of clear, unambiguous requests, which never touch the cases that fail. The same technique reduces false positives in review: examples contrasting acceptable patterns with genuine issues, so judgment generalises instead of matching a fixed list.",
 "remember": "Target the boundary, not the clear cases, and include the reasoning. Two to four examples with rationale beat a dozen obvious ones; the reasoning is what generalises.",
 "analogy": "The precedent binder is filled with the cases that could have gone either way, each recorded with the reasoning the court gave for going one way. A run of straightforward judgments would add pages without helping the bench decide the case in front of it, which is hard because it sits on the line.",
 "svg": """<line class="dash" x1="80" y1="14" x2="80" y2="106"/>
<text class="lbl" x="34" y="24" text-anchor="middle">A</text>
<text class="lbl" x="126" y="24" text-anchor="middle">B</text>
<circle class="accfill" cx="70" cy="44" r="5"/>
<circle class="accfill" cx="90" cy="58" r="5"/>
<circle class="accfill" cx="68" cy="74" r="5"/>
<circle class="accfill" cx="92" cy="88" r="5"/>
<circle class="tint" cx="22" cy="60" r="5"/>
<circle class="tint" cx="34" cy="76" r="5"/>
<circle class="tint" cx="24" cy="92" r="5"/>
<line class="no" x1="16" y1="58" x2="40" y2="94"/>
<line class="no" x1="40" y1="58" x2="16" y2="94"/>""",
 "alt": "Examples clustered on the boundary; a clump far from it crossed out",
},
{
 "id": "D4-06",
 "title": "Few-shot for extraction across varied documents",
 "concept": "Few-shot examples covering varied document structures — inline citations versus bibliographies, methodology sections versus details embedded in prose — reduce hallucination in extraction and stop required fields coming back empty.",
 "tested": "12% of extractions carry a fabricated value in a required field, or the same field returns null whenever the source lays it out differently, and the question asks the fix. The answer adds examples showing correct extraction from each document layout the source set actually contains. Distractors write the extraction instructions out in more detail, or add more examples of the one layout that already works.",
 "remember": "Varied layouts, and informal wordings such as loose measurements → one worked example per case, showing where the value sits. Examples cut fabrication in extraction; longer instructions do not.",
 "analogy": "Evidence arrives in whatever form the parties kept it: a source cited in the body of a letter, the same source listed at the back of a report, a method described in a paragraph rather than under a heading. The binder holds one worked example of each form, so the clerk knows where to look instead of leaving the box blank or writing something plausible.",
 "svg": """<rect class="tint" x="12" y="14" width="36" height="26" rx="2"/>
<line class="thin" x1="18" y1="24" x2="42" y2="24"/><line class="thin" x1="18" y1="32" x2="36" y2="32"/>
<rect class="tint" x="12" y="47" width="36" height="26" rx="2"/>
<rect class="thin" x="18" y="53" width="14" height="8"/><line class="thin" x1="18" y1="66" x2="42" y2="66"/>
<rect class="tint" x="12" y="80" width="36" height="26" rx="2"/>
<line class="thin" x1="30" y1="86" x2="30" y2="100"/><line class="thin" x1="18" y1="93" x2="42" y2="93"/>
<line class="acc" x1="52" y1="27" x2="88" y2="52"/>
<line class="acc" x1="52" y1="60" x2="88" y2="60"/>
<line class="acc" x1="52" y1="93" x2="88" y2="68"/>
<rect class="paper" x="92" y="34" width="52" height="52" rx="3"/>
<line class="acc thin" x1="100" y1="50" x2="136" y2="50"/>
<line class="acc thin" x1="100" y1="62" x2="136" y2="62"/>
<line class="acc thin" x1="100" y1="74" x2="124" y2="74"/>""",
 "alt": "Three differently laid-out documents feeding one uniformly filled record",
},
{
 "id": "D4-07",
 "title": "tool_use with a JSON schema is the structured-output guarantee",
 "concept": "Defining a tool whose input schema is the output structure you want, then reading the data from the `tool_use` block, guarantees schema-compliant output and removes JSON syntax errors.",
 "tested": "A pipeline must receive parseable JSON on every document, and the question asks how to guarantee it. The answer defines an extraction tool whose input schema is the target structure and reads the `tool_use` block. Distractors ask in the prompt for valid JSON only, which still returns prose preambles and markdown fences, or bolt a JSON repair library onto free-text output, which treats the symptom.",
 "remember": "The tool need not do anything; its input schema is the contract. `tool_use` removes the syntax class of error, and a prompt asking for JSON does not.",
 "analogy": "The clerk's standard form is the mechanism: a box for each thing the record must contain, and nothing filed that is not on the form. Asking counsel to submit their evidence in a tidy layout produces a different document every time, whereas the form comes back with the boxes filled.",
 "svg": """<rect class="acc" x="42" y="14" width="64" height="90" rx="3"/>
<line class="acc" x1="52" y1="26" x2="96" y2="26"/>
<rect class="thin" x="52" y="36" width="44" height="12" rx="1"/>
<rect class="thin" x="52" y="56" width="44" height="12" rx="1"/>
<rect class="thin" x="52" y="76" width="44" height="12" rx="1"/>
<rect class="tint" x="10" y="34" width="24" height="46" rx="2"/>
<path class="dash thin" d="M15 44 h14 M15 54 h14 M15 64 h10"/>
<line class="no" x1="12" y1="40" x2="32" y2="74"/>
<line class="no" x1="32" y1="40" x2="12" y2="74"/>
<circle class="acc" cx="128" cy="76" r="16"/>
<circle class="acc thin" cx="128" cy="76" r="11"/>""",
 "alt": "Standard form with boxes, stamped; a free-text sheet crossed out",
},
{
 "id": "D4-08",
 "title": "tool_choice: only any and forced guarantee a tool call",
 "concept": "`tool_choice: \"auto\"` lets the model answer in text instead of calling a tool, `\"any\"` forces some tool call with the model choosing which, and `{\"type\": \"tool\", \"name\": \"...\"}` forces that named tool.",
 "tested": "An extraction pipeline must always receive structured output and the document may be an invoice, a receipt or a contract, each with its own tool; the answer is `tool_choice: \"any\"`, and where one named extraction must run before the enrichment steps, `{\"type\": \"tool\", \"name\": \"extract_metadata\"}`. The trap is an option that pairs `auto` with a prompt instruction to always call the tool and offers the pair as a guarantee. `auto` leaves the model free to answer in text, and no instruction in the prompt changes that.",
 "remember": "`auto` = may return text. `any` = must call a tool, model picks which. `{\"type\": \"tool\", \"name\": ...}` = must call that one. A prompt instruction is not a guarantee.",
 "analogy": "The judge can tell the clerk to file if the clerk thinks it appropriate, to file on some form of the clerk's choosing, or to file on form twelve. Only the last two produce a filing; under the first the clerk may hand back a note in their own words, and adding \"be sure to file\" to the direction does not change what was directed.",
 "svg": """<text class="lbl" x="24" y="24" text-anchor="middle">auto</text>
<path class="dash thin" d="M42 20 l16 -6"/>
<path class="dash thin" d="M42 24 l16 6"/>
<rect class="tint" x="62" y="8" width="26" height="14" rx="2"/>
<line class="thin" x1="68" y1="15" x2="82" y2="15"/>
<path class="thin" d="M62 32 q6 -4 11 0 q5 4 11 0"/>
<rect class="tint" x="112" y="10" width="34" height="22" rx="2"/>
<path class="thin" d="M118 21 q5 -3 9 0 q4 3 9 0"/>
<line class="no" x1="114" y1="12" x2="144" y2="30"/>
<line class="no" x1="144" y1="12" x2="114" y2="30"/>
<text class="lbl" x="24" y="64" text-anchor="middle">any</text>
<path class="acc" d="M42 60 h16 M48 55 l6 5 -6 5"/>
<rect class="acc" x="62" y="50" width="26" height="20" rx="2"/>
<rect class="acc" x="94" y="50" width="26" height="20" rx="2"/>
<text class="lbl" x="24" y="104" text-anchor="middle">tool</text>
<path class="acc" d="M42 100 h16 M48 95 l6 5 -6 5"/>
<rect class="acc" x="62" y="90" width="26" height="20" rx="2"/>
<rect class="dash thin" x="94" y="90" width="26" height="20" rx="2"/>""",
 "alt": "auto branches to text or a tool; any and forced always call",
},
{
 "id": "D4-09",
 "title": "Schema-valid is not the same as correct",
 "concept": "A strict JSON schema through tool use eliminates syntax errors but not semantic ones: line items that do not sum to the stated total, or values in the wrong field, pass validation.",
 "tested": "JSON parse failures dropped to zero after the move to `tool_use`, and downstream reconciliation still finds totals that do not match their line items; the question asks what is happening or what to do next. The answer treats this as expected, because the schema removed the syntax class and the remaining failures are semantic and need business-rule checks. Distractors tighten the schema further, which no schema constraint can do for arithmetic, or abandon tool use, which adds the syntax class back on top.",
 "remember": "Schema compliance is structural. Sums, field placement and category choice are semantic and need validation in code. Zero parse errors is not zero extraction errors.",
 "analogy": "Every box on the clerk's form is filled in, legibly and in the right place, and the figures still do not add up to the total written at the foot. The form was checked for completeness, which is a different question from whether the record is true.",
 "svg": """<rect class="paper" x="34" y="12" width="92" height="96" rx="3"/>
<path class="thin" d="M44 20 l4 4 7 -8"/>
<line class="thin" x1="44" y1="32" x2="86" y2="32"/>
<text class="lbl" x="110" y="36" text-anchor="middle">40</text>
<line class="thin" x1="44" y1="50" x2="86" y2="50"/>
<text class="lbl" x="110" y="54" text-anchor="middle">55</text>
<line class="thin" x1="44" y1="68" x2="86" y2="68"/>
<text class="lbl" x="110" y="72" text-anchor="middle">50</text>
<line x1="44" y1="80" x2="118" y2="80"/>
<line class="acc" x1="44" y1="97" x2="86" y2="97"/>
<text class="lbl" x="110" y="101" text-anchor="middle">150</text>
<circle class="acc" cx="110" cy="97" r="12"/>""",
 "alt": "Fully filled form; the circled total does not match the lines",
},
{
 "id": "D4-10",
 "title": "Nullable fields stop fabrication",
 "concept": "Fields whose information may be absent from the source are marked optional or nullable, because a required non-nullable field pushes the model to invent a value to satisfy the schema.",
 "tested": "Extractions come back with a plausible but fabricated value in a required field that the source document never contained, and the question asks the schema change. The answer takes the field out of `required` and allows null, so the model can return `null` instead. The distractor makes every field required so that output is always complete, which buys completeness with fabrication.",
 "remember": "Required means always present in the source, not always wanted in the output. A field that may be missing is nullable, and `null` is a real answer.",
 "analogy": "A box on the form marked as mandatory has to be filled before the form can be filed, so a clerk with nothing to put in it writes something. Marking the box as one that may be left blank is what makes an empty box an honest answer rather than a rejected form.",
 "svg": """<rect class="tint" x="12" y="16" width="60" height="88" rx="3"/>
<line class="thin" x1="20" y1="34" x2="64" y2="34"/>
<rect class="thin" x="20" y="46" width="44" height="16" rx="1"/>
<text class="lbl" x="42" y="58" text-anchor="middle">1234</text>
<line class="thin" x1="20" y1="80" x2="64" y2="80"/>
<line class="no" x1="16" y1="42" x2="68" y2="66"/>
<line class="no" x1="68" y1="42" x2="16" y2="66"/>
<rect class="tint" x="88" y="16" width="60" height="88" rx="3"/>
<line class="thin" x1="96" y1="34" x2="140" y2="34"/>
<rect class="acc dash" x="96" y="46" width="44" height="16" rx="1"/>
<text class="lbl" x="118" y="58" text-anchor="middle">null</text>
<line class="thin" x1="96" y1="80" x2="140" y2="80"/>""",
 "alt": "Required box holding an invented figure, crossed out; nullable box returns null",
},
{
 "id": "D4-11",
 "title": "Enum values: unclear for ambiguity, other plus detail",
 "concept": "An enum gets an `\"unclear\"` value so ambiguous cases are recorded as ambiguous, and an `\"other\"` value with a companion detail string so a category outside the list can still be captured.",
 "tested": "A category field has to cope with documents the model cannot confidently place, and with values that fall outside the list the schema was written against; the question asks the schema change. The answer adds `\"unclear\"` to the enum for the first and `\"other\"` with a detail string for the second, against a distractor that has the model pick from the fixed list anyway, which records a confident wrong category.",
 "remember": "`\"unclear\"` for cannot-tell, `\"other\"` plus a detail string for outside-the-list. An honest `\"unclear\"` beats a confident wrong category.",
 "analogy": "The clerk's form offers a fixed list of pleas, plus a line for a case that fits none of them and a blank to say what it was. There is also a box for cases the clerk cannot classify from the papers in front of them, recorded as such instead of being pushed into the nearest heading.",
 "svg": """<rect class="paper" x="16" y="12" width="76" height="96" rx="3"/>
<circle class="thin" cx="28" cy="30" r="4"/><line class="thin" x1="38" y1="30" x2="82" y2="30"/>
<circle class="thin" cx="28" cy="50" r="4"/><line class="thin" x1="38" y1="50" x2="82" y2="50"/>
<circle class="accfill" cx="28" cy="72" r="4"/>
<text class="lbl" x="60" y="76" text-anchor="middle">other</text>
<circle class="accfill" cx="28" cy="94" r="4"/>
<text class="lbl" x="58" y="98" text-anchor="middle">?</text>
<path class="acc" d="M96 72 h14 M104 67 l6 5 -6 5"/>
<rect class="acc dash" x="112" y="60" width="36" height="24" rx="2"/>
<line class="acc thin" x1="118" y1="72" x2="142" y2="72"/>""",
 "alt": "Enum list with other linked to a detail box and an unclear row",
},
{
 "id": "D4-12",
 "title": "Normalisation rules travel with the schema",
 "concept": "Format normalisation rules go in the prompt alongside the strict output schema, because the schema fixes the shape of the output while the prompt governs how inconsistent source formats map into it.",
 "tested": "Source documents write dates and currencies differently, and the extracted values arrive in whatever form the document used even though the schema validates; the question asks what to add. The answer states the normalisation rules in the prompt beside the schema. The distractor tightens the schema, which can constrain a field's type but cannot decide how a messy input is rewritten into it.",
 "remember": "Schema = shape. Prompt = how messy inputs become that shape. Inconsistent source formatting is a prompt instruction, not a schema constraint.",
 "analogy": "The form has a box for the date of the offence, and the statements in the file write it a dozen ways. The direction to the clerk says which way to render it in the box; the box itself only says that a date belongs there.",
 "svg": """<rect class="tint" x="12" y="14" width="40" height="18" rx="2"/>
<text class="lbl" x="32" y="27" text-anchor="middle">3/4</text>
<rect class="tint" x="12" y="48" width="40" height="18" rx="2"/>
<text class="lbl" x="32" y="61" text-anchor="middle">4 Mar</text>
<rect class="tint" x="12" y="82" width="40" height="18" rx="2"/>
<text class="lbl" x="32" y="95" text-anchor="middle">03-04</text>
<line class="thin" x1="52" y1="23" x2="62" y2="45"/>
<line class="thin" x1="52" y1="57" x2="62" y2="60"/>
<line class="thin" x1="52" y1="91" x2="62" y2="75"/>
<rect class="acc" x="62" y="34" width="34" height="52" rx="3"/>
<line class="acc thin" x1="68" y1="48" x2="90" y2="48"/>
<line class="acc thin" x1="68" y1="60" x2="90" y2="60"/>
<line class="acc thin" x1="68" y1="72" x2="90" y2="72"/>
<path d="M100 60 h12 M108 55 l6 5 -6 5"/>
<rect class="paper" x="116" y="44" width="32" height="32" rx="2"/>
<rect class="thin" x="122" y="54" width="20" height="12" rx="1"/>""",
 "alt": "Three date formats passing through a rules note into one schema box",
},
]
