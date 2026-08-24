# Domain 2 part A — Tool Design & MCP Integration · building: the library

ITEMS = [
{
 "id": "D2-01",
 "title": "The description is the interface",
 "concept": "Tool descriptions are the primary mechanism a model uses to select a tool; a good one gives input formats, example queries, edge cases and when-to-use boundaries.",
 "tested": "Production logs show the agent calling `get_customer` for order questions while both tools carry one-line descriptions and accept similar identifier formats, and the question asks the most effective first step. The answer expands each description with input formats, example queries, edge cases and boundaries explaining when to use it versus the similar tool. Distractors add five to eight few-shot examples, insert a pre-routing classifier that pre-selects the tool, or consolidate the pair into one general lookup tool.",
 "remember": "Misrouting among similar tools → rewrite the descriptions first. Adding a routing layer or more examples leaves the ambiguity in place.",
 "analogy": "The reference librarian chooses a room by the blurb on its door, not by what is inside it. When two doors say much the same thing, readers are sent to the wrong room, and the repair is to rewrite the blurbs: what the room holds, a typical question it answers, when the room next door is the better one. Posting a porter in the corridor to redirect people leaves both blurbs as they were.",
 "svg": """<circle cx="26" cy="28" r="8"/><path d="M26 36 v18 M14 44 h24"/>
<line class="dash thin" x1="40" y1="36" x2="70" y2="36"/>
<rect class="tint" x="76" y="16" width="52" height="88" rx="2"/>
<circle class="thin" cx="120" cy="62" r="2"/>
<rect class="acc" x="84" y="24" width="36" height="32" rx="2"/>
<line class="acc thin" x1="90" y1="32" x2="114" y2="32"/>
<line class="acc thin" x1="90" y1="40" x2="114" y2="40"/>
<line class="acc thin" x1="90" y1="48" x2="106" y2="48"/>
<text class="lbl" x="35" y="70" text-anchor="middle">route</text>
<rect class="dash" x="12" y="76" width="46" height="26" rx="2"/>
<line class="no" x1="19" y1="82" x2="51" y2="96"/>
<line class="no" x1="51" y1="82" x2="19" y2="96"/>""",
 "alt": "Librarian reading a detailed door sign; a routing box crossed out",
},
{
 "id": "D2-02",
 "title": "Overlapping descriptions misroute — rename and differentiate",
 "concept": "Two tools whose descriptions read almost the same, `analyze_content` and `analyze_document`, draw work to the wrong one; renaming one to `extract_web_results` and rewriting its description for a distinct purpose removes the overlap.",
 "tested": "A web-search agent's `analyze_content` and a document agent's `analyze_document` carry near-identical descriptions and the agent routes to the wrong one; the question asks the fix. The answer renames the web tool to `extract_web_results` and rewrites its description around web search and URLs. The distractor adds a pre-routing classifier, which buys infrastructure while the functional overlap stays where it was.",
 "remember": "Two tools that read the same → rename one for its actual purpose and rewrite its description. A pre-routing classifier steers around the overlap instead of removing it.",
 "analogy": "Two reading rooms on the same corridor carry door signs that read almost the same, so the librarian sends readers to whichever comes first. Repainting one door as the web-clippings room, with a sign saying it holds search results and URLs, separates them at the point where the choice is actually made.",
 "svg": """<rect class="tint" x="14" y="22" width="46" height="82" rx="2"/>
<circle class="thin" cx="52" cy="64" r="2"/>
<rect class="paper" x="20" y="30" width="34" height="22" rx="2"/>
<line class="thin" x1="26" y1="38" x2="48" y2="38"/>
<line class="thin" x1="26" y1="46" x2="42" y2="46"/>
<rect class="tint" x="100" y="22" width="46" height="82" rx="2"/>
<circle class="thin" cx="138" cy="64" r="2"/>
<rect class="acc" x="106" y="30" width="34" height="22" rx="2"/>
<text class="lbl" x="123" y="45" text-anchor="middle">web</text>
<rect class="dash thin" x="106" y="66" width="34" height="22" rx="2"/>
<line class="no" x1="110" y1="70" x2="136" y2="84"/>
<line class="no" x1="136" y1="70" x2="110" y2="84"/>""",
 "alt": "Two door signs; the duplicate is crossed out, one renamed web",
},
{
 "id": "D2-03",
 "title": "Split generic tools into purpose-specific ones",
 "concept": "A generic `analyze_document` splits into `extract_data_points`, `summarize_content` and `verify_claim_against_source`, each with a defined input and output contract.",
 "tested": "One tool covers several unrelated jobs, so its description cannot state a single purpose, and the question asks how to redesign the interface. The answer splits it into purpose-specific tools with defined input and output contracts: `analyze_document` becomes `extract_data_points`, `summarize_content` and `verify_claim_against_source`. The distractor family runs the other way, consolidating tools into one general-purpose entry point that accepts anything and decides internally which backend to query.",
 "remember": "One tool, several jobs → split it, one purpose per tool with its own contract. Consolidating is valid elsewhere, not the fix when a description cannot state one purpose.",
 "analogy": "One room signed Document Work holds the extraction bench, the abstracting desk and the fact-checking desk, so its sign can say only that documents are handled somewhere inside. Three rooms, each signed with what goes in and what comes back out, let the librarian choose without opening any door.",
 "svg": """<rect class="tint" x="12" y="30" width="36" height="72" rx="2"/>
<rect class="paper" x="17" y="38" width="26" height="18" rx="2"/>
<line class="thin" x1="22" y1="47" x2="38" y2="47"/>
<circle class="thin" cx="42" cy="70" r="2"/>
<path d="M54 66 h12 M60 60 l6 6 -6 6"/>
<rect class="acc" x="72" y="48" width="20" height="54" rx="2"/>
<rect class="acc" x="100" y="48" width="20" height="54" rx="2"/>
<rect class="acc" x="128" y="48" width="20" height="54" rx="2"/>
<circle class="thin" cx="87" cy="76" r="2"/>
<circle class="thin" cx="115" cy="76" r="2"/>
<circle class="thin" cx="143" cy="76" r="2"/>
<text class="lbl" x="82" y="42" text-anchor="middle">ext</text>
<text class="lbl" x="110" y="42" text-anchor="middle">sum</text>
<text class="lbl" x="138" y="42" text-anchor="middle">ver</text>""",
 "alt": "One wide general door replaced by three narrow labelled doors",
},
{
 "id": "D2-04",
 "title": "Keyword-sensitive prompt wording overrides good descriptions",
 "concept": "Wording in the system prompt can bind a tool to a keyword and create an unintended association that overrides well-written tool descriptions.",
 "tested": "Descriptions are already specific and differentiated, yet one tool is still selected whenever a particular word appears in the request, and the question asks where to look next. The answer reviews the system prompt for keyword-sensitive instructions that created the association. Distractors rewrite the descriptions a second time or add examples, both of which leave the prompt wording untouched.",
 "remember": "Descriptions already differentiated and one word still skews selection → read the system prompt, where a keyword-sensitive instruction can outrank the descriptions.",
 "analogy": "The standing instruction pinned behind the desk says that anything to do with records goes to the archive room, and the librarian follows it even where the door signs are clear and specific. When the signs are already good and one word still sends every request to the same room, the instruction behind the desk is what to read.",
 "svg": """<rect class="paper" x="12" y="18" width="58" height="48" rx="3"/>
<line class="thin" x1="20" y1="30" x2="62" y2="30"/>
<rect class="acc" x="20" y="38" width="28" height="14" rx="2"/>
<text class="lbl" x="34" y="49" text-anchor="middle">recs</text>
<line class="thin" x1="20" y1="58" x2="62" y2="58"/>
<path class="acc" d="M74 42 h18 M86 37 l6 5 -6 5"/>
<rect class="tint" x="96" y="24" width="50" height="80" rx="2"/>
<circle class="thin" cx="138" cy="66" r="2"/>
<rect class="dash thin" x="102" y="32" width="36" height="24" rx="2"/>
<line class="dash thin" x1="108" y1="40" x2="132" y2="40"/>
<line class="dash thin" x1="108" y1="48" x2="126" y2="48"/>""",
 "alt": "Pinned notice with a highlighted word overriding a door sign",
},
{
 "id": "D2-05",
 "title": "isError plus structured error metadata",
 "concept": "An MCP tool signals failure with `isError` and should carry `errorCategory`, an `isRetryable` boolean and a human-readable description, because a generic \"Operation failed\" gives the agent nothing to decide on.",
 "tested": "A tool returns the same \"Operation failed\" for a timeout, a malformed argument and a policy refusal, and the agent retries all three; the question asks what the tool should return instead. The answer carries `isError` with an `errorCategory`, an `isRetryable` boolean and a readable description, so the agent retries only what is retryable and explains the rest. The distractor keeps one uniform failure string and moves the decision into the prompt. Retrying a transient failure inside the tool is correct and is not the fault here.",
 "remember": "`isError` plus `errorCategory`, `isRetryable` and a readable description. A uniform failure status narrows every recovery down to retry or abort.",
 "analogy": "A request slip returned stamped only Not Available tells the reader nothing about what to do next. The same slip returned with the reason written on it, and a line saying whether coming back later would help, lets the reader decide without going to the desk again.",
 "svg": """<rect class="paper" x="16" y="40" width="46" height="42" rx="2"/>
<line class="thin" x1="24" y1="62" x2="54" y2="62"/>
<line class="no" x1="22" y1="46" x2="56" y2="76"/>
<line class="no" x1="56" y1="46" x2="22" y2="76"/>
<rect class="paper" x="84" y="16" width="58" height="88" rx="2"/>
<rect class="acc" x="92" y="24" width="42" height="16" rx="2"/>
<text class="lbl" x="113" y="36" text-anchor="middle">err</text>
<line class="thin" x1="92" y1="52" x2="134" y2="52"/>
<line class="thin" x1="92" y1="62" x2="134" y2="62"/>
<line class="thin" x1="92" y1="72" x2="126" y2="72"/>
<circle class="accfill" cx="96" cy="88" r="3"/>
<line class="acc" x1="104" y1="88" x2="134" y2="88"/>""",
 "alt": "Request slip carrying a reason code; a bare failure slip crossed out",
},
{
 "id": "D2-06",
 "title": "Four error kinds: transient, validation, business, permission",
 "concept": "Tool errors divide into transient (timeouts, service unavailability), validation (invalid input), business (policy violations) and permission kinds, and each one calls for a different move.",
 "tested": "A tool fails and the question asks what it should hand back or what the agent should do next. A refund refused by a policy window is a business error, returned with `retriable: false` and a customer-friendly explanation so the agent explains the outcome instead of retrying. The trap pairs a timeout, which is transient and worth a retry, against a query that ran and matched nothing, which is a successful empty result rather than an error.",
 "remember": "Transient → retry; validation → fix the input; business → `retriable: false` and explain the policy; permission → get access. Zero matches is a result, not a failure.",
 "analogy": "The slip comes back with one of four stamps: the room is shut for the afternoon, the form was filled in wrongly, the item is held back by lending policy, or the shelf is staff-only. Each stamp sends the reader somewhere different: wait and ask again, redo the form, accept the answer, or apply for a different card. A search that ran and found nothing on the shelves carries no stamp; it is a completed request with an empty result.",
 "svg": """<rect class="tint" x="12" y="42" width="28" height="46" rx="2"/>
<rect class="tint" x="48" y="42" width="28" height="46" rx="2"/>
<rect class="tint" x="84" y="42" width="28" height="46" rx="2"/>
<rect class="tint" x="120" y="42" width="28" height="46" rx="2"/>
<line class="thin" x1="18" y1="62" x2="34" y2="62"/>
<line class="thin" x1="54" y1="62" x2="70" y2="62"/>
<line class="thin" x1="90" y1="62" x2="106" y2="62"/>
<line class="thin" x1="126" y1="62" x2="142" y2="62"/>
<circle class="acc" cx="26" cy="26" r="9"/>
<path class="accfill" d="M26 15 l7 4 -7 4 z"/>
<circle class="thin" cx="98" cy="26" r="9"/>
<path class="thin" d="M98 15 l7 4 -7 4 z"/>
<line class="no" x1="88" y1="17" x2="108" y2="35"/>
<line class="no" x1="108" y1="17" x2="88" y2="35"/>
<text class="lbl" x="26" y="102" text-anchor="middle">tran</text>
<text class="lbl" x="62" y="102" text-anchor="middle">valid</text>
<text class="lbl" x="98" y="102" text-anchor="middle">biz</text>
<text class="lbl" x="134" y="102" text-anchor="middle">perm</text>""",
 "alt": "Four error slips; the retry loop crossed out on the business one",
},
{
 "id": "D2-07",
 "title": "Fewer tools per agent",
 "concept": "Giving an agent eighteen tools instead of four or five degrades tool selection reliability by increasing decision complexity.",
 "tested": "An agent holding a large tool set picks the wrong one often while a peer with a role-sized set does not, and the question asks the change to make. The answer cuts the set to the four or five tools the role needs. The distractor keeps all of them and writes a more detailed description for every one, which leaves the same number of candidates to discriminate between on every turn.",
 "remember": "A tool count in the scenario, 18 against 4–5, is the tell: cut the set to the role's tools. Better descriptions on all eighteen leave the decision space unchanged.",
 "analogy": "A librarian facing eighteen doors along one corridor weighs eighteen possibilities before every request, however clearly each one is signed. A reference desk with four or five rooms behind it lands on the right one more often, because fewer rooms could plausibly be the answer.",
 "svg": """<rect class="tint" x="12" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="26" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="40" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="54" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="68" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="82" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="96" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="110" y="20" width="12" height="26" rx="1"/>
<rect class="tint" x="124" y="20" width="12" height="26" rx="1"/>
<line class="no" x1="64" y1="16" x2="84" y2="50"/>
<line class="no" x1="84" y1="16" x2="64" y2="50"/>
<text class="lbl" x="140" y="38" text-anchor="middle">18</text>
<rect class="acc" x="30" y="66" width="20" height="36" rx="2"/>
<rect class="acc" x="56" y="66" width="20" height="36" rx="2"/>
<rect class="acc" x="82" y="66" width="20" height="36" rx="2"/>
<rect class="acc" x="108" y="66" width="20" height="36" rx="2"/>
<circle class="thin" cx="46" cy="86" r="2"/>
<circle class="thin" cx="72" cy="86" r="2"/>
<circle class="thin" cx="98" cy="86" r="2"/>
<circle class="thin" cx="124" cy="86" r="2"/>
<text class="lbl" x="140" y="88" text-anchor="middle">4-5</text>""",
 "alt": "A row of eighteen doors crossed out; four wider doors below",
},
{
 "id": "D2-08",
 "title": "Scoped tools per role, with one cross-role exception",
 "concept": "Each subagent gets only its role's tools; for a high-frequency cross-role need, give it a narrowly scoped tool such as `verify_fact` and route complex cases through the coordinator.",
 "tested": "A synthesis agent keeps returning control to the coordinator for fact checks, most of them simple lookups, adding round trips and latency, and the question asks how to cut the overhead without losing reliability. The answer gives it a scoped `verify_fact` tool for the common case while complex verifications keep going through the coordinator. Distractors hand it the full web search tool set, which is the cross-specialisation misuse that scoping exists to prevent, or batch the checks until the end of the pass.",
 "remember": "The role's tools, plus one narrow tool for a frequent cross-role need; complex cases still route through the coordinator. Distributing tools is a separate lever from `tool_choice`.",
 "analogy": "A reader's card opens the rooms their work needs and no others. When one reader is at the map room counter twenty times a day for a single date, the library adds that one lookup to their card rather than handing over the map room, and the long research questions still go through the desk.",
 "svg": """<rect class="tint" x="12" y="20" width="56" height="40" rx="3"/>
<circle class="thin" cx="26" cy="36" r="4"/>
<circle class="thin" cx="40" cy="36" r="4"/>
<circle class="accfill" cx="54" cy="36" r="4"/>
<text class="lbl" x="40" y="54" text-anchor="middle">web</text>
<rect class="tint" x="92" y="20" width="56" height="40" rx="3"/>
<circle class="thin" cx="106" cy="36" r="4"/>
<circle class="thin" cx="120" cy="36" r="4"/>
<circle class="thin" cx="134" cy="36" r="4"/>
<text class="lbl" x="120" y="54" text-anchor="middle">syn</text>
<path class="acc" d="M54 42 v38 h60 v-20"/>
<line class="dash thin" x1="68" y1="30" x2="92" y2="30"/>
<line class="no" x1="72" y1="22" x2="88" y2="38"/>
<line class="no" x1="88" y1="22" x2="72" y2="38"/>""",
 "alt": "One web tool wired into the synthesis room; full access crossed out",
},
{
 "id": "D2-09",
 "title": "Constrained alternatives to generic tools",
 "concept": "Replacing a generic tool with a constrained alternative, `fetch_url` giving way to a `load_document` that validates document URLs, enforces the boundary at the interface rather than in the prompt.",
 "tested": "A document analysis agent holds a general `fetch_url` tool and starts pulling pages that are not documents, and the question asks how to stop it. The answer replaces the tool with `load_document`, which validates that the URL points to a document format. Distractors add a prompt instruction, which is probabilistic, or block particular domains, which is fragile and dates quickly.",
 "remember": "A broad tool being misused → replace it with a narrower one that validates its own input. A prompt instruction asks; a constrained interface removes the option.",
 "analogy": "A slip that says bring me what is at this address comes back with whatever the address points at, a report one day and a page of search results the next. A slip headed document request, which the desk refuses unless the reference is a document, keeps the errand inside its purpose without anyone having to remember the rule.",
 "svg": """<line x1="12" y1="90" x2="148" y2="90"/>
<rect class="tint" x="54" y="36" width="50" height="54" rx="3"/>
<line x1="54" y1="54" x2="104" y2="54"/>
<text class="lbl" x="79" y="49" text-anchor="middle">doc</text>
<rect class="acc" x="64" y="62" width="30" height="22" rx="2"/>
<line class="acc thin" x1="70" y1="72" x2="88" y2="72"/>
<path class="thin" d="M138 72 h-22 M126 66 l-10 6 10 6"/>
<circle class="tint" cx="26" cy="60" r="13"/>
<line class="thin" x1="13" y1="60" x2="39" y2="60"/>
<line class="no" x1="17" y1="51" x2="35" y2="69"/>
<line class="no" x1="35" y1="51" x2="17" y2="69"/>""",
 "alt": "A hatch marked doc accepts a document; a generic item crossed out",
},
{
 "id": "D2-10",
 "title": ".mcp.json is shared; ~/.claude.json is personal",
 "concept": "MCP servers the whole team uses are configured in the repository's `.mcp.json`, while personal or experimental servers belong in the user's `~/.claude.json`.",
 "tested": "A team wants every developer on the same MCP server while each keeps their own token, and the question asks where the configuration belongs. The answer is the project-scoped `.mcp.json`, version-controlled, with the token supplied by environment variable expansion. Distractors have each developer add the server to their own `~/.claude.json`, which leaves the team on inconsistent tooling, or commit a placeholder token into the repository.",
 "remember": "Shared with the team and version-controlled → `.mcp.json` at the project root. Personal, experimental or your own credentials → `~/.claude.json` in your home directory.",
 "analogy": "The building's institutional subscription is registered at the front desk, so anyone who joins the library that morning can use the databases it covers. A subscription taken out on your own card sits in your wallet: it works for you, it does not appear at the desk, and the reader who joined last week has never heard of it.",
 "svg": """<circle cx="24" cy="16" r="5"/>
<circle cx="41" cy="16" r="5"/>
<circle cx="58" cy="16" r="5"/>
<rect class="acc" x="14" y="28" width="54" height="48" rx="3"/>
<line class="acc thin" x1="22" y1="42" x2="60" y2="42"/>
<line class="acc thin" x1="22" y1="52" x2="60" y2="52"/>
<line class="acc thin" x1="22" y1="62" x2="50" y2="62"/>
<text class="lbl" x="41" y="92" text-anchor="middle">proj</text>
<circle cx="119" cy="24" r="6"/>
<line class="dash thin" x1="119" y1="32" x2="119" y2="46"/>
<rect class="tint" x="96" y="46" width="46" height="30" rx="3"/>
<line class="thin" x1="104" y1="62" x2="128" y2="62"/>
<text class="lbl" x="119" y="92" text-anchor="middle">user</text>""",
 "alt": "Shared register used by three readers; one personal card beside it",
},
]
