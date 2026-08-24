# Domain 2 — Tool Design & MCP Integration (18%)
S = 'stroke="#15130F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ITEMS = [
{
 "title": "The guarantee ladder — auto · any · forced",
 "world": "workshop", "flag": "live", "cite": "D2 §2.5 · D4 §4.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="8" y="18" width="30" height="84" rx="6" fill="#fff"/>
   <rect x="14" y="26" width="18" height="12" rx="3" fill="#fff"/>
   <path d="M18 32h10" stroke-width="3"/>
   <rect x="14" y="44" width="18" height="10" rx="3" fill="#B8791C"/>
   <rect x="45" y="18" width="30" height="84" rx="6" fill="#fff"/>
   <rect x="51" y="26" width="18" height="10" rx="3" fill="#B8791C"/>
   <rect x="51" y="42" width="18" height="10" rx="3" fill="#B8791C"/>
   <rect x="51" y="58" width="18" height="10" rx="3" fill="#B8791C"/>
   <rect x="82" y="18" width="30" height="84" rx="6" fill="#fff"/>
   <rect x="88" y="42" width="18" height="10" rx="3" fill="#E8552F"/>
   <circle cx="97" cy="80" r="9" fill="#FDF0D8"/><path d="M97 76v8" stroke-width="4"/></g></svg>''',
 "story": "Three vending machines. The first has a <b>speech-bubble slot</b> among the snacks — it might just "
          "talk to you. The second has no chat slot: something drops, you do not choose what. The third has "
          "B4 already pressed: that exact item, every time.",
 "tell": "<code>auto</code> permits text. <code>any</code> guarantees a call, model picks. "
         "<code>{\"type\":\"tool\",\"name\":\"X\"}</code> guarantees <b>that</b> call. "
         "Match the guarantee to what the requirement names — a stronger one is still the wrong answer.",
},
{
 "title": "tool_result carries the tool_use id",
 "world": "post", "flag": "live", "cite": "D2 §2.1",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="22" width="42" height="32" rx="5" fill="#E1EAFB"/>
   <path d="M20 46h30" stroke-width="3"/>
   <rect x="64" y="66" width="42" height="32" rx="5" fill="#fff"/>
   <path d="M70 90h30" stroke-width="3"/>
   <path d="M56 38h12a10 10 0 0 1 10 10v18" stroke="#2F5FBF"/>
   <rect x="24" y="28" width="22" height="11" rx="3" fill="#2F5FBF"/>
   <rect x="74" y="72" width="22" height="11" rx="3" fill="#2F5FBF"/></g></svg>''',
 "story": "Every parcel has a <b>tracking number</b>, and the receipt you send back has to quote it. "
          "Narrating what happened in prose is not the protocol — the calls stay open and get asked again.",
 "tell": "Results re-enter as <code>tool_result</code> blocks keyed to their <code>tool_use</code> "
         "<code>id</code>. Not prose, not ordering, not a timestamp.",
},
{
 "title": "The description IS the interface",
 "world": "workshop", "flag": "live", "cite": "D2 §2.2 · KD#10",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="24" width="38" height="72" rx="5" fill="#fff"/>
   <rect x="66" y="24" width="38" height="72" rx="5" fill="#FDF0D8"/>
   <path d="M24 40h22" stroke-width="3"/>
   <path d="M74 38h22M74 50h22M74 62h14M74 74h18" stroke-width="3"/>
   <circle cx="35" cy="70" r="9" fill="#FF4757"/>
   <path d="M31 66l8 8M39 66l-8 8" stroke="#fff" stroke-width="3.5"/></g></svg>''',
 "story": "Two drawers labelled with one word each, holding parts that look the same. Of course people open "
          "the wrong one. The fix is <b>writing on the drawer</b> — what goes in, the formats, and what "
          "explicitly does not belong here.",
 "tell": "Misrouting? Fix descriptions first — inputs, examples, boundaries, when NOT to use. "
         "Not a classifier, not merging the tools, not a prompt rule.",
},
{
 "title": "Four kinds of error, four different moves",
 "world": "workshop", "cite": "D2 §2.3 · KD#9",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="14" width="42" height="42" rx="6" fill="#F5C518"/>
   <path d="M28 42a26 26 0 0 1 14-18" stroke-width="4"/><path d="M42 20v6h-6" stroke-width="4"/>
   <rect x="64" y="14" width="42" height="42" rx="6" fill="#fff"/>
   <path d="M76 26h18M76 36h18M76 46h10" stroke-width="3.5"/>
   <rect x="14" y="64" width="42" height="42" rx="6" fill="#fff"/>
   <path d="M26 84h18" stroke-width="5"/>
   <rect x="64" y="64" width="42" height="42" rx="6" fill="#FF4757"/>
   <rect x="76" y="82" width="18" height="14" rx="3" fill="#fff"/>
   <path d="M80 82v-6a5 5 0 0 1 10 0v6" stroke="#fff" stroke-width="3.5"/></g></svg>''',
 "story": "<b>Transient</b> — try again. <b>Validation</b> — fix the input and re-call. <b>Business</b> — the "
          "answer is no, and retrying will never change it. <b>Permission</b> — wrong key, escalate.",
 "tell": "A policy refusal is a valid answer, not a failure: <code>retriable: false</code> plus a "
         "customer-friendly explanation. Retrying it burns turns for an outcome that cannot move.",
},
{
 "title": "Zero results is a result",
 "world": "workshop", "cite": "D2 §2.3",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="30" width="40" height="56" rx="5" fill="#fff"/>
   <path d="M26 58h20" stroke-width="3"/>
   <circle cx="36" cy="42" r="4" fill="#2E7D5B"/>
   <rect x="64" y="30" width="40" height="56" rx="5" fill="#FF4757"/>
   <path d="M76 46l16 16M92 46l-16 16" stroke="#fff"/></g></svg>''',
 "story": "\"I looked, there is nothing\" and \"I could not look\" are different sentences. Collapse them and "
          "the agent tells a customer they have no orders <b>because the database was down</b>.",
 "tell": "Query ran, nothing matched → success with an empty set. Query could not run → "
         "<code>isError: true</code> with a category. Never the other way round.",
},
{
 "title": "The token that cannot be forged",
 "world": "workshop", "flag": "clear", "cite": "D2 §2.4 · KD#12",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="40" width="40" height="40" rx="6" fill="#fff"/>
   <circle cx="34" cy="60" r="10" fill="#FDF0D8"/><path d="M34 54v12"/>
   <path d="M54 60h16"/>
   <rect x="70" y="40" width="36" height="40" rx="6" fill="#B8791C"/>
   <path d="M80 60h16" stroke="#fff"/>
   <circle cx="62" cy="34" r="9" fill="#F5C518"/><path d="M62 30v8" stroke-width="3.5"/></g></svg>''',
 "story": "<code>preview_x</code> hands you a single-use ticket; <code>execute_x</code> will not move without "
          "it. Skipping the preview is not discouraged — it is <b>impossible</b>, because the ticket does not exist yet.",
 "tell": "You have this one — three papers running. Single-use and bound to <b>that</b> preview. "
         "A signature stops forgery, not replay; an expiry narrows the window without closing it.",
},
{
 "title": "Eighteen tools is the bug",
 "world": "workshop", "cite": "D2 §2.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M14 96h92" stroke-width="6"/>
   <path d="M22 96V56M32 96V64M42 96V52M52 96V70M62 96V58M72 96V66M82 96V54M92 96V68" stroke-width="4"/>
   <circle cx="22" cy="52" r="5" fill="#FDF0D8"/><circle cx="32" cy="60" r="5" fill="#FDF0D8"/>
   <circle cx="42" cy="48" r="5" fill="#FDF0D8"/><circle cx="52" cy="66" r="5" fill="#FDF0D8"/>
   <circle cx="62" cy="54" r="5" fill="#FDF0D8"/><circle cx="72" cy="62" r="5" fill="#FDF0D8"/>
   <circle cx="82" cy="50" r="5" fill="#E8552F"/><circle cx="92" cy="64" r="5" fill="#FDF0D8"/></g></svg>''',
 "story": "A bench with everything on it is slower than a bench with five things on it. Every extra tool is "
          "another near-miss the model has to rule out, <b>on every single turn</b>.",
 "tell": "18 tools vs 4–5 is the guide's own number. Cut the set to the role first. Better descriptions "
         "help but do not shrink the decision space.",
},
{
 "title": "The one sanctioned cross-role tool",
 "world": "workshop", "cite": "D2 §2.5",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="42" cy="56" r="22" fill="#fff"/>
   <path d="M34 56l6 6 12-14"/>
   <path d="M64 56h20" stroke-dasharray="5 6"/>
   <rect x="84" y="40" width="22" height="32" rx="5" fill="#FDF0D8"/>
   <path d="M90 52h10M90 62h6" stroke-width="3"/></g></svg>''',
 "story": "The writer needs to check one fact a hundred times a day. Sending each check back through the "
          "editor is silly; handing them the whole research desk is worse. Give them a <b>narrow window</b>.",
 "tell": "High-frequency simple need → narrowly scoped cross-role tool (<code>verify_fact</code>). "
         "Complex cases still route through the coordinator. Never full <code>web_search</code>.",
},
{
 "title": "MCP: tools act, resources are read, prompts are templates",
 "world": "workshop", "cite": "D2 §2.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="12" y="34" width="30" height="52" rx="5" fill="#B8791C"/>
   <path d="M20 60h14" stroke="#fff"/>
   <rect x="46" y="34" width="30" height="52" rx="5" fill="#fff"/>
   <path d="M54 48h14M54 60h14M54 72h8" stroke-width="3"/>
   <rect x="80" y="34" width="28" height="52" rx="5" fill="#FDF0D8"/>
   <path d="M88 48h12M88 60h12" stroke-width="3" stroke-dasharray="4 4"/></g></svg>''',
 "story": "Tools are the <b>levers</b> you pull. Resources are the <b>catalogue on the wall</b> you read for "
          "free. Prompts are pre-written <b>order forms</b>.",
 "tell": "Agent burning calls guessing what exists? Expose a resource catalogue — it is readable context, "
         "not another call it has to remember to make.",
},
{
 "title": "Shared server, personal key",
 "world": "house", "cite": "D2 §2.6 · KD#2",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="16" y="28" width="88" height="56" rx="7" fill="#fff"/>
   <path d="M16 46h88"/>
   <path d="M28 62h30" stroke-width="3"/>
   <rect x="66" y="54" width="28" height="18" rx="4" fill="#DFF2E7"/>
   <path d="M72 63h4M82 63h4" stroke-width="3"/>
   <circle cx="79" cy="63" r="3.5" fill="#2E7D5B"/></g></svg>''',
 "story": "The server config is <b>team property, checked in</b>. The credential is not — it is read from "
          "your own environment at runtime.",
 "tell": "<code>.mcp.json</code> at project root, version-controlled, with <code>${'{'}GITHUB_TOKEN{'}'}</code> "
         "substitution. <code>~/.claude.json</code> is personal. Never commit a placeholder token.",
},
{
 "title": "Community server for standard, custom for yours alone",
 "world": "workshop", "cite": "D2 §2.6",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="42" width="40" height="40" rx="6" fill="#fff"/>
   <path d="M22 62h24M34 50v24" stroke-width="4"/>
   <rect x="66" y="42" width="40" height="40" rx="6" fill="#B8791C"/>
   <path d="M76 56l10 10 10-16" stroke="#fff"/>
   <path d="M34 32V20M86 32V20" stroke-width="4"/></g></svg>''',
 "story": "Nobody hand-builds a kettle. But nobody sells the jig that only fits <b>your</b> bench either.",
 "tell": "Standard integration (issue tracker, source host, chat) → existing community server. "
         "Unique team workflow → build custom. The rule runs both ways.",
},
{
 "title": "It keeps choosing Grep over your clever MCP tool",
 "world": "workshop", "cite": "D2 §2.6 · KD#29",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="44" cy="50" r="20" fill="#fff"/><path d="M58 64l16 16" stroke-width="6"/>
   <rect x="66" y="20" width="40" height="30" rx="5" fill="#FDF0D8"/>
   <path d="M74 32h24M74 42h14" stroke-width="3"/>
   <path d="M52 88h44" stroke="#2E7D5B" stroke-width="4"/>
   <path d="M88 82l8 6-8 6" stroke="#2E7D5B" stroke-width="4"/></g></svg>''',
 "story": "Selection runs on descriptions. If your semantic index does not <b>say out loud</b> what it can do "
          "that a text search cannot, the model reaches for the familiar hammer.",
 "tell": "Enhance the MCP tool's description. Do not remove Grep, and do not add a \"prefer MCP tools\" "
         "rule — both break the cases where the built-in is genuinely right.",
},
{
 "title": "PreToolUse prevents · PostToolUse tidies",
 "world": "workshop", "cite": "D2 §2.7",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <path d="M60 14v92" stroke-dasharray="7 8" stroke-width="4"/>
   <rect x="12" y="40" width="36" height="40" rx="6" fill="#FF4757"/>
   <path d="M22 60h16" stroke="#fff" stroke-width="6"/>
   <rect x="72" y="40" width="36" height="40" rx="6" fill="#fff"/>
   <path d="M80 56h20M80 66h12" stroke-width="3.5"/>
   <circle cx="60" cy="24" r="7" fill="#B8791C"/></g></svg>''',
 "story": "One is the bouncer at the door; the other is the cleaner after closing. Both are deterministic "
          "code — but only one of them <b>stops the thing happening</b>.",
 "tell": "Block above a threshold, validate, gate → <code>PreToolUse</code>. Normalise formats, trim "
         "verbose output → <code>PostToolUse</code>. If the requirement is \"must never happen\", it is Pre.",
},
{
 "title": "Bundle the requests before you build a composite",
 "world": "workshop", "flag": "live", "cite": "D2 §2.8",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="34" cy="40" r="14" fill="#fff"/><circle cx="34" cy="80" r="14" fill="#fff"/>
   <path d="M48 40h14M48 80h14" stroke-dasharray="4 5"/>
   <rect x="66" y="46" width="40" height="28" rx="6" fill="#B8791C"/>
   <path d="M76 60h20" stroke="#fff" stroke-width="4"/>
   <path d="M86 34v10M86 76v10" stroke="#FF4757" stroke-width="4"/></g></svg>''',
 "story": "Two calls that always travel together look like one tool waiting to be born. But a welded-shut "
          "composite <b>hides the seam</b> — and the next workflow only wants the second half.",
 "tell": "Missed on five papers. The documented preference is to <b>prompt the agent to bundle both "
         "requests into one turn</b>. The agent can already ask for several tools at once.",
},
{
 "title": "Grep looks inside · Glob looks at names",
 "world": "workshop", "cite": "D2 §2.9 · KD#26",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="14" y="20" width="40" height="52" rx="5" fill="#fff"/>
   <path d="M22 36h24M22 48h24M22 60h14" stroke-width="3"/>
   <circle cx="40" cy="48" r="14" fill="none" stroke="#B8791C" stroke-width="5"/>
   <path d="M50 58l10 10" stroke="#B8791C" stroke-width="5"/>
   <rect x="68" y="20" width="38" height="24" rx="4" fill="#FDF0D8"/>
   <path d="M76 32h22" stroke-width="3"/>
   <path d="M68 62h38M68 76h38M68 90h24" stroke-width="4"/></g></svg>''',
 "story": "Grep reads the <b>pages</b>. Glob reads the <b>spines</b>. \"Who calls this function\" is a pages "
          "question; \"every test file\" is a spines question.",
 "tell": "Globbing a symbol name finds files <b>named</b> after it, not files that use it — which is why "
         "the search comes back clean and the build then breaks.",
},
{
 "title": "Edit needs a unique anchor",
 "world": "workshop", "flag": "watch", "cite": "D2 §2.9 · KD#27",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <rect x="18" y="18" width="52" height="70" rx="5" fill="#fff"/>
   <path d="M28 34h30M28 48h30M28 62h30" stroke-width="3"/>
   <rect x="26" y="44" width="34" height="9" rx="3" fill="#F5C518"/>
   <rect x="26" y="58" width="34" height="9" rx="3" fill="#F5C518"/>
   <path d="M78 40l14-14 12 12-14 14z" fill="#B8791C"/>
   <path d="M78 40l-4 18 18-4"/></g></svg>''',
 "story": "The anchor appears four times, so Edit refuses — it cannot guess which. A <b>shorter</b> anchor "
          "matches more places, not fewer.",
 "tell": "Fall back to Read → modify → Write the whole file. Not a shorter anchor, not <code>sed</code>.",
},
{
 "title": "Grep then Read — never read the whole repo first",
 "world": "workshop", "cite": "D2 §2.9 · KD#28",
 "svg": f'''<svg viewBox="0 0 120 120"><g {S}>
   <circle cx="34" cy="36" r="15" fill="none" stroke="#B8791C" stroke-width="5"/>
   <path d="M45 47l10 10" stroke="#B8791C" stroke-width="5"/>
   <path d="M58 60h12"/>
   <rect x="70" y="44" width="34" height="30" rx="5" fill="#fff"/>
   <path d="M78 56h18M78 66h12" stroke-width="3"/>
   <path d="M20 84h64" stroke-dasharray="5 7"/>
   <path d="M34 96l-8-8 8-8" stroke-width="4"/></g></svg>''',
 "story": "Find the door before you map the building. Content search finds the entry point, then you read "
          "<b>only</b> what it pointed at, then you follow the imports.",
 "tell": "\"Read every file for full context\" is the named anti-pattern — and so is globbing the tree and "
         "reading every match.",
},
]
