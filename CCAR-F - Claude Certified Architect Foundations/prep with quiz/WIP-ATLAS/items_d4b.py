# Domain 4 part B — Prompt Engineering & Structured Output · building: the courthouse

ITEMS = [
{
 "id": "D4-13",
 "title": "Retry with the specific validation error",
 "concept": "A retry that includes the original document, the failed extraction and the exact validation error gives the model the material it needs to correct format and structural faults.",
 "tested": "Validation fails on a share of extracted documents and the question asks how the retry should be built. The answer sends three things back together — the original document, the previous extraction, and the specific error text, such as a total that does not match the sum of the line items. Distractors resend the document with a bare instruction to try again, or raise the retry ceiling, neither of which carries a correction signal.",
 "remember": "Retry payload = original document + failed extraction + the exact error. A retry with no error text gives the model nothing to act on.",
 "analogy": "An appeal is remitted with the grounds written into the order: which finding is unsupported, and on what point the court below must rule again. The file goes down with the earlier judgment and the ground attached to it, which is what makes the second hearing different from the first.",
 "svg": """<rect class="paper" x="14" y="26" width="46" height="64" rx="3"/>
<line class="thin" x1="22" y1="40" x2="52" y2="40"/>
<line class="thin" x1="22" y1="52" x2="52" y2="52"/>
<line class="thin" x1="22" y1="64" x2="52" y2="64"/>
<line class="no" x1="26" y1="58" x2="38" y2="70"/>
<line class="no" x1="38" y1="58" x2="26" y2="70"/>
<path class="acc" d="M66 58 h18 M78 52 l6 6 -6 6"/>
<rect class="tint" x="92" y="22" width="52" height="20" rx="3"/>
<rect class="tint" x="92" y="48" width="52" height="20" rx="3"/>
<rect class="acc" x="92" y="74" width="52" height="20" rx="3"/>
<text class="lbl" x="118" y="36" text-anchor="middle">doc</text>
<text class="lbl" x="118" y="62" text-anchor="middle">fail</text>
<text class="lbl" x="118" y="88" text-anchor="middle">err</text>""",
 "alt": "Failed form plus the exact error bundled into one retry request",
},
{
 "id": "D4-14",
 "title": "Retry cannot supply information the source lacks",
 "concept": "Retries correct format and structural errors, and no number of them extracts a value that the source document does not contain.",
 "tested": "A required field fails validation on a set of documents and investigation shows those documents never carried that value; the question asks what to change. The answer makes the field nullable and treats absence as a legitimate result. Distractors raise the retry limit, sharpen the wording of the retry feedback, or keep the field required for data quality, which pressures the model into fabricating a value.",
 "remember": "Sort the failure first: format and structure retry well, absent information never appears. Absent means a nullable field, not a higher retry ceiling.",
 "analogy": "The appeals bench can order a point to be heard again, and it cannot rule on evidence that was never entered in the record. A file sent back a second and a third time returns the same finding when the document was never filed.",
 "svg": """<rect class="paper" x="16" y="24" width="56" height="72" rx="3"/>
<line class="thin" x1="26" y1="40" x2="62" y2="40"/>
<line class="thin" x1="26" y1="52" x2="62" y2="52"/>
<rect class="acc dash" x="26" y="62" width="40" height="18" rx="2"/>
<text class="lbl" x="46" y="75" text-anchor="middle">null</text>
<circle cx="112" cy="60" r="24"/>
<polygon points="112,36 118,46 106,46"/>
<line class="no" x1="98" y1="46" x2="126" y2="74"/>
<line class="no" x1="126" y1="46" x2="98" y2="74"/>""",
 "alt": "Document with an empty nullable field; the retry loop crossed out",
},
{
 "id": "D4-15",
 "title": "detected_pattern turns dismissals into a feedback loop",
 "concept": "A `detected_pattern` field on each structured finding records which code construct triggered it, so dismissed findings can be grouped and analysed by pattern.",
 "tested": "Developers dismiss a large share of review findings and the team cannot tell which finding types are noise; the question asks what to add. The answer puts a `detected_pattern` field on every finding so dismissal rates can be read per pattern. The distractor collects a free-text reason on each dismissal, which does not aggregate into anything actionable.",
 "remember": "`detected_pattern` names the construct that fired. Group dismissals by it and the noisy category identifies itself; free-text reasons do not aggregate.",
 "analogy": "Every finding leaves the bench stamped with the ground it was brought under. When the clerk sorts the dismissed files months later, the stamps show which ground keeps failing rather than a shelf of unlike cases.",
 "svg": """<rect class="paper" x="14" y="22" width="32" height="20" rx="2"/>
<text class="lbl" x="30" y="36" text-anchor="middle">P1</text>
<rect class="paper" x="14" y="48" width="32" height="20" rx="2"/>
<text class="lbl" x="30" y="62" text-anchor="middle">P2</text>
<rect class="paper" x="14" y="74" width="32" height="20" rx="2"/>
<text class="lbl" x="30" y="88" text-anchor="middle">P1</text>
<path d="M54 58 h16 M64 52 l6 6 -6 6"/>
<line x1="80" y1="92" x2="148" y2="92"/>
<rect class="acc" x="88" y="34" width="20" height="58"/>
<rect class="tint" x="118" y="70" width="20" height="22"/>
<text class="lbl" x="98" y="106" text-anchor="middle">P1</text>
<text class="lbl" x="128" y="106" text-anchor="middle">P2</text>""",
 "alt": "Findings tagged by pattern, sorted into per-pattern dismissal bars",
},
{
 "id": "D4-16",
 "title": "Self-checking schema: calculated_total beside stated_total",
 "concept": "Extracting `calculated_total` alongside `stated_total` with a `conflict_detected` boolean makes a discrepancy surface as data at extraction time rather than at reconciliation.",
 "tested": "An invoice pipeline reports totals that do not match their line items, discovered weeks later in reconciliation; the question asks how to catch it at extraction. The answer re-derives the total inside the schema and flags disagreement with a boolean. Distractors add a monthly reconciliation report, which keeps the delay, or a prompt instruction to be careful with totals, which builds no detection mechanism.",
 "remember": "Extract the claimed value and an independently derived value, plus a boolean for disagreement. The check belongs in the schema, not in an instruction.",
 "analogy": "The clerk's form asks for the figure twice: as written on the exhibit, and as the clerk adds it up from the items listed. A third box records that the two disagree, so the disagreement travels with the file instead of surfacing at the year-end audit.",
 "svg": """<rect class="paper" x="14" y="24" width="132" height="72" rx="3"/>
<rect class="thin" x="24" y="36" width="46" height="20" rx="2"/>
<text class="lbl" x="47" y="50" text-anchor="middle">150</text>
<rect class="thin" x="90" y="36" width="46" height="20" rx="2"/>
<text class="lbl" x="113" y="50" text-anchor="middle">145</text>
<path class="acc" d="M74 42 h12 M74 50 h12"/>
<line class="acc" x1="86" y1="38" x2="74" y2="54"/>
<rect class="acc" x="24" y="66" width="16" height="16" rx="2"/>
<path class="acc" d="M27 74 l4 5 l8 -10"/>
<line class="thin" x1="48" y1="76" x2="120" y2="76"/>""",
 "alt": "Form holding stated and calculated totals with a conflict box ticked",
},
{
 "id": "D4-17",
 "title": "Batches API: 50% cheaper, up to 24 hours",
 "concept": "The Message Batches API costs 50% less than synchronous calls, with a processing window of up to 24 hours and no guaranteed latency SLA.",
 "tested": "Two workflows run on real-time calls — a blocking pre-merge check and a technical-debt report generated overnight — and a manager proposes moving both to the Batches API for the 50% saving. The answer batches the overnight report and leaves the pre-merge check synchronous, because developers wait on it. Distractors move both with status polling, keep both synchronous over a result-ordering worry that `custom_id` already answers, or add a timeout fallback to real time.",
 "remember": "50% cheaper, up to 24 hours, no latency SLA. Someone is blocked waiting → synchronous. Needed by morning or next week → batch.",
 "analogy": "The night docket costs half as much and usually clears by morning, though the court promises no hour. A matter where the parties are standing in the corridor waiting for the order stays on the day list at full price.",
 "svg": """<circle class="paper" cx="60" cy="58" r="30"/>
<path class="acc" d="M60 58 V28 A30 30 0 1 1 34 73 Z"/>
<path d="M60 58 V36 M60 58 L76 66"/>
<text class="lbl" x="60" y="20" text-anchor="middle">50%</text>
<text class="lbl" x="60" y="102" text-anchor="middle">24h</text>
<circle cx="124" cy="44" r="8"/>
<path d="M124 52 v18 M114 60 h20"/>
<line class="no" x1="112" y1="40" x2="136" y2="72"/>
<line class="no" x1="136" y1="40" x2="112" y2="72"/>""",
 "alt": "Clock sweeping 24h marked 50%, with a waiting person crossed out",
},
{
 "id": "D4-18",
 "title": "A batch request cannot run a tool loop mid-request",
 "concept": "The Batches API does not support multi-turn tool calling inside a single request: it cannot execute a tool mid-request and return the result to the model.",
 "tested": "A workload tolerates delay, but its review fetches related files through tool calls as it goes, and the question asks whether it can move to batch for the saving. The answer keeps it synchronous, because a batch request is one submission and one response. The distractor reads the 50% saving and the tolerance for delay as sufficient and overlooks the tool loop.",
 "remember": "One submission, one response per request, and you poll for completion. Work that needs a tool result returned mid-request stays synchronous however patient it is.",
 "analogy": "A matter placed on the night docket is decided on the papers as filed. If the judge would need to call for a further document, hear the answer and carry on the same night, the matter belongs on the day list.",
 "svg": """<rect class="tint" x="54" y="46" width="52" height="34" rx="4"/>
<path class="acc" d="M16 63 h30 M40 57 l6 6 -6 6"/>
<path class="acc" d="M114 63 h30 M138 57 l6 6 -6 6"/>
<rect class="dash" x="60" y="14" width="40" height="20" rx="3"/>
<text class="lbl" x="80" y="29" text-anchor="middle">tool</text>
<path class="dash thin" d="M68 46 V36"/>
<path class="dash thin" d="M92 36 V46"/>
<line class="no" x1="70" y1="34" x2="90" y2="48"/>
<line class="no" x1="90" y1="34" x2="70" y2="48"/>""",
 "alt": "One request in, one response out; the mid-request tool loop crossed out",
},
{
 "id": "D4-19",
 "title": "custom_id correlates results; resubmit only the failures",
 "concept": "`custom_id` is the field that joins a batch request to its response, which is how failed items are identified and resubmitted with a fix such as chunking.",
 "tested": "A batch returns mostly successes with a few failures, some of which exceeded the context limit, and the question asks what to resubmit. The answer resubmits only the failed items, found by `custom_id`, chunked so they fit. Distractors resubmit the whole batch, resubmit the failures unchanged, or avoid batch altogether over result ordering, which `custom_id` already handles.",
 "remember": "`custom_id` is the join key; arrival order is not. Resubmit only what failed, and change what made it fail.",
 "analogy": "Every file sent to the night docket carries a case-number stamp, and the orders come back stamped the same way in whatever order the court reaches them. The clerk pulls the five that failed by number, has the over-long ones split into volumes, and sends back only those.",
 "svg": """<rect class="paper" x="14" y="22" width="46" height="40" rx="3"/>
<circle class="acc" cx="52" cy="30" r="7"/>
<path d="M68 42 h18 M80 36 l6 6 -6 6"/>
<rect class="tint" x="94" y="22" width="46" height="40" rx="3"/>
<circle class="acc" cx="132" cy="30" r="7"/>
<rect class="paper" x="34" y="76" width="24" height="22" rx="2"/>
<text class="lbl" x="46" y="92" text-anchor="middle">1</text>
<rect class="paper" x="66" y="76" width="24" height="22" rx="2"/>
<text class="lbl" x="78" y="92" text-anchor="middle">2</text>
<rect class="paper" x="98" y="76" width="24" height="22" rx="2"/>
<text class="lbl" x="110" y="92" text-anchor="middle">3</text>
<line class="no" x1="64" y1="74" x2="94" y2="100"/>
<line class="no" x1="94" y1="74" x2="64" y2="100"/>""",
 "alt": "Stamped request and stamped result; matching by position crossed out",
},
{
 "id": "D4-20",
 "title": "Submission cadence from the SLA arithmetic",
 "concept": "Batch submission windows are sized against the 24-hour worst case, so guaranteeing a 30-hour SLA with up to 24 hours of processing means submitting in roughly four-hour windows.",
 "tested": "A recurring pipeline owes results inside a stated SLA and runs on batch, and the question asks how often to submit. The answer works back from the SLA against the full 24-hour worst case rather than typical completion, giving four-hour submission windows for a 30-hour SLA. The distractor plans around how long batches usually take, which no SLA supports.",
 "remember": "Budget the full 24 hours, never the usual completion time. A 30-hour SLA with 24-hour processing gives four-hour submission windows.",
 "analogy": "The night docket clears by morning most nights, and the court undertakes only that it will be within the day. A registry that must return every order inside thirty hours therefore sends files up in short blocks through the day, so no file rests on a promise the court never made.",
 "svg": """<line x1="14" y1="92" x2="146" y2="92"/>
<rect class="acc" x="16" y="76" width="24" height="16" rx="2"/>
<rect class="acc" x="46" y="76" width="24" height="16" rx="2"/>
<rect class="acc" x="76" y="76" width="24" height="16" rx="2"/>
<rect class="acc" x="106" y="76" width="24" height="16" rx="2"/>
<text class="lbl" x="28" y="106" text-anchor="middle">4h</text>
<path class="dash" d="M16 52 H120"/>
<text class="lbl" x="68" y="44" text-anchor="middle">24h</text>
<line x1="140" y1="34" x2="140" y2="62"/>
<text class="lbl" x="140" y="26" text-anchor="middle">30h</text>""",
 "alt": "Four-hour submission blocks under a 24-hour span before a 30-hour deadline",
},
{
 "id": "D4-21",
 "title": "Refine on a sample before the big batch",
 "concept": "Refining the extraction prompt on a small sample before submitting a large batch raises the first-pass success rate and reduces the cost of resubmission.",
 "tested": "A large volume of documents is about to go through one extraction prompt and the question asks what to do first. The answer refines the prompt on a representative sample, then submits the volume. The distractor submits the full batch and iterates on it, where every round pays for the whole batch and waits up to 24 hours to learn one thing.",
 "remember": "Sample first, batch second. A defect found on a sample costs a sample; the same defect found after a full batch costs the batch and up to 24 hours.",
 "analogy": "A registry about to send ten thousand files up on one form tries the form on a dozen first. A defect caught on the dozen costs a morning; the same defect caught after the night docket has run costs every file on it.",
 "svg": """<rect class="paper" x="16" y="36" width="28" height="36" rx="2"/>
<rect class="paper" x="22" y="42" width="28" height="36" rx="2"/>
<rect class="paper" x="28" y="48" width="28" height="36" rx="2"/>
<path class="acc" d="M34 64 l6 7 l10 -14"/>
<path d="M66 62 h18 M78 56 l6 6 -6 6"/>
<rect class="tint" x="94" y="18" width="52" height="14" rx="2"/>
<rect class="tint" x="94" y="36" width="52" height="14" rx="2"/>
<rect class="tint" x="94" y="54" width="52" height="14" rx="2"/>
<rect class="tint" x="94" y="72" width="52" height="14" rx="2"/>
<rect class="tint" x="94" y="90" width="52" height="14" rx="2"/>""",
 "alt": "Small sample checked first, then the full stack submitted",
},
{
 "id": "D4-22",
 "title": "An independent instance reviews; the author does not",
 "concept": "A model that generated code retains its reasoning from that session and is less likely to question its own decisions, so review goes to a second instance without that context.",
 "tested": "Generated code passes its own careful-review step and bugs keep reaching production; the question asks how to restructure the review. The answer routes the artifact to a second, independent instance that never sees the generator's reasoning. Distractors strengthen the self-review instruction, enable extended thinking on the generator, or ask the same conversation for a second pass, all of which keep the original reasoning in context.",
 "remember": "Independence is a property of context, not of effort. Fresh instance, artifact and criteria only, none of the generating conversation — though earlier review findings may travel, which is a different thing (D3-24).",
 "analogy": "The judge who tried the case reads the file through reasoning already settled on. An appeal is heard by a bench that did not sit at the trial and receives only the record and the grounds, which is why it notices what the first judge had explained away.",
 "svg": """<circle cx="38" cy="30" r="9"/>
<path d="M38 39 v22 M26 48 h24"/>
<rect class="dash" x="16" y="70" width="44" height="26" rx="3"/>
<text class="lbl" x="38" y="87" text-anchor="middle">why</text>
<line class="dash thin" x1="60" y1="83" x2="98" y2="83"/>
<line class="no" x1="72" y1="74" x2="86" y2="92"/>
<line class="no" x1="86" y1="74" x2="72" y2="92"/>
<path class="acc" d="M68 46 h22 M84 40 l6 6 -6 6"/>
<circle class="acc" cx="120" cy="30" r="9"/>
<path class="acc" d="M120 39 v22 M108 48 h24"/>
<rect class="paper" x="98" y="70" width="44" height="26" rx="3"/>
<line class="thin" x1="106" y1="80" x2="134" y2="80"/>
<line class="thin" x1="106" y1="88" x2="126" y2="88"/>""",
 "alt": "The trial judge's reasoning does not travel to the second judge",
},
{
 "id": "D4-23",
 "title": "Per-file passes plus a cross-file integration pass",
 "concept": "Splitting a large multi-file review into a focused pass per file for local issues plus a separate integration pass for cross-file data flow avoids attention dilution and contradictory findings.",
 "tested": "A pull request touching 14 files draws detailed feedback on some files, superficial comments on others, missed bugs, and the same pattern flagged in one file and approved in another; the question asks how to restructure the review. The answer analyses each file individually, then runs a separate integration-focused pass over cross-file data flow. Distractors reach for a larger context window, which does not improve attention quality, push developers to split the pull request into smaller submissions, or run three full passes and keep only findings that appear in two of them, which suppresses real bugs caught intermittently.",
 "remember": "Uneven depth and contradictions across files → split the passes. A bigger context window does not buy attention quality, and consensus voting drops real findings.",
 "analogy": "Fourteen exhibits heard in one sitting get uneven attention: the first examined closely, the twelfth waved through, the same clause read two ways in a single judgment. The registry lists each exhibit for its own short hearing, then one further hearing on how they fit together.",
 "svg": """<rect class="paper" x="16" y="16" width="30" height="28" rx="2"/>
<rect class="paper" x="65" y="16" width="30" height="28" rx="2"/>
<rect class="paper" x="114" y="16" width="30" height="28" rx="2"/>
<path class="acc" d="M31 48 v12 M27 56 l4 5 l4 -5"/>
<path class="acc" d="M80 48 v12 M76 56 l4 5 l4 -5"/>
<path class="acc" d="M129 48 v12 M125 56 l4 5 l4 -5"/>
<circle class="acc" cx="31" cy="72" r="8"/>
<circle class="acc" cx="80" cy="72" r="8"/>
<circle class="acc" cx="129" cy="72" r="8"/>
<rect class="tint" x="16" y="90" width="128" height="20" rx="3"/>
<text class="lbl" x="80" y="104" text-anchor="middle">int</text>""",
 "alt": "Three files each get their own pass, then one integration pass",
},
{
 "id": "D4-24",
 "title": "Confidence beside each finding routes the review",
 "concept": "A verification pass in which the model self-reports confidence alongside each finding lets routing be calibrated, so low-confidence findings reach a person.",
 "tested": "A verification pass emits every finding the same way and there is no basis for deciding which need a human; the question asks how to route them. The answer has the model report its confidence with each finding, sending high-confidence items straight out and low-confidence items to review. The distractor filters at the source, instructing the model to report only high-confidence findings, which drops findings rather than routing them.",
 "remember": "Confidence routes a finding; it never suppresses one. Report it per finding, send the doubtful ones to a person. Filtering to high-confidence only is the distractor (D4-01).",
 "analogy": "Each finding leaves the bench with a note of how firmly it is held. The clerk sends the firm ones straight out and lists the doubtful ones for a person to look at, so doubt is routed rather than discarded.",
 "svg": """<rect class="paper" x="12" y="28" width="44" height="22" rx="2"/>
<text class="lbl" x="34" y="43" text-anchor="middle">hi</text>
<rect class="paper" x="12" y="70" width="44" height="22" rx="2"/>
<text class="lbl" x="34" y="85" text-anchor="middle">lo</text>
<path class="acc" d="M62 39 h20 M76 33 l6 6 -6 6"/>
<path class="acc" d="M62 81 h20 M76 75 l6 6 -6 6"/>
<rect class="tint" x="90" y="24" width="54" height="30" rx="3"/>
<path d="M104 39 l5 6 l12 -14"/>
<circle cx="116" cy="70" r="9"/>
<path d="M116 79 v16 M104 87 h24"/>""",
 "alt": "High-confidence finding auto-posted; low-confidence finding routed to a person",
},
]
