"""Five questions rewritten to a different domain so the block x domain allocation
satisfies the archetype gate's STRICT primacy rule (every primary domain must
outnumber every non-primary domain in its block, not merely tie).

Re-solved allocation (nearest strict-feasible to the drafted one, L1 distance 10):
  CS  D1 4 / D2 4 / D3 2 / D4 2 / D5 3     was  4/3/2/3/3   -> Q13  D4 -> D2
  MR  D1 5 / D2 6 / D3 1 / D4 1 / D5 2     was  5/5/2/1/2   -> Q28  D3 -> D2
  CI  D1 4 / D2 0 / D3 6 / D4 5 / D5 0     was  4/1/5/4/1   -> Q40  D2 -> D3
                                                             -> Q43  D5 -> D4
  SD  D1 3 / D2 1 / D3 3 / D4 4 / D5 4     was  3/2/3/4/3   -> Q59  D2 -> D5

These are rewrites, not re-tags: each question now tests a different corpus section
and carries new options and rationales.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

NEW = {
 13: {
  "g": 13, "block": 0, "domain": "D2",
  "stem": "`find_account` returns `{\"matches\": [], \"status\": \"ok\"}` when a search runs correctly and matches nobody, and the same empty array with `{\"status\": \"ok\"}` when the account service is unreachable and the lookup never ran. The agent retries both cases three times, then tells the customer no account exists. What must change?",
  "options": [
   "The tool must distinguish the two outcomes: a successful search with no matches is a valid result, while an unreachable service is a retryable error with its own category.",
   "The agent should retry any empty result five times rather than three, so a transient outage has longer to recover before the customer is told anything.",
   "The agent should never tell a customer that no account exists, and should escalate every empty result to a specialist instead.",
   "The tool should return a null matches field rather than an empty array when the service is unreachable, letting the agent branch on null."
  ],
  "correct": 0,
  "whyRight": {
   "text": "A search that ran and found nothing is an answer; a search that never ran is a failure. Collapsing both into an empty array with an ok status makes them indistinguishable, so the agent retries the answer and reports the failure as fact. Separating them — valid empty result on one side, categorised retryable error on the other — is what lets the agent stop retrying the first and recover from the second.",
   "cite": "CCA-Prep_Domain-2_v2.md §2.3"
  },
  "whyWrong": [
   {"option": 1, "text": "More retries make the genuine no-match case slower without making either case distinguishable. The customer is still told no account exists when the service was simply down, which is the damaging half of the behaviour.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.3"},
   {"option": 2, "text": "This escalates every genuine no-match — a common, correctly-handled outcome — to work around a signal the tool is failing to send. It buries specialists in cases the agent can resolve and still never learns which empty results were outages.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.3"},
   {"option": 3, "text": "A null in place of an empty array is a sentinel the agent must be taught to read, and it still reports `status: ok` for a call that failed. The corpus asks for an explicit error category and a retryable flag, not a second meaning overloaded onto the result field.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.3"}
  ]
 },

 28: {
  "g": 28, "block": 1, "domain": "D2",
  "stem": "Analysts want the coordinator to know which document collections are available before it decomposes a question — roughly forty collections, each with a title, a coverage note and a date range, changing every few weeks. A developer proposes exposing a `list_collections` tool the coordinator calls at the start of every run. What does the MCP server offer that fits this better?",
  "options": [
   "A prompt, which the coordinator can invoke to have the server describe its collections in natural language.",
   "A resource, which exposes the catalogue as addressable content the client can read without spending a tool call on every run.",
   "A tool with a cached response, so the forty collections are fetched once per session rather than once per question.",
   "A second MCP server dedicated to catalogue metadata, keeping it separate from the retrieval server's tools."
  ],
  "correct": 1,
  "whyRight": {
   "text": "MCP exposes three primitives and they answer different questions. Tools are actions the model chooses to perform; resources are content the client can read. A catalogue of forty collections is reference material the coordinator needs available, not an action it decides to take — so it belongs in a resource, which also keeps it current as the collections change without the coordinator having to remember to re-fetch.",
   "cite": "CCA-Prep_Domain-2_v2.md §2.6"
  },
  "whyWrong": [
   {"option": 0, "text": "Prompts are reusable interaction templates the server offers, not a store of content. Having the server narrate forty collections into the conversation each run costs tokens and produces prose where addressable data is wanted.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.6"},
   {"option": 2, "text": "Caching a tool response reduces the call count while leaving reference material modelled as an action. It also adds an invalidation problem the corpus does not ask anyone to solve, since the collections change every few weeks.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.6"},
   {"option": 3, "text": "Splitting servers relocates the same modelling error and adds a second configuration entry to maintain. The question is which primitive fits catalogue content, not which server should hold it.",
    "cite": "CCA-Prep_Domain-2_v2.md §2.6"}
  ]
 },

 40: {
  "g": 40, "block": 2, "domain": "D3",
  "stem": "Reviewers notice the pipeline applies none of the repository's conventions: it flags naming the team has documented as correct and misses the error-handling rules everyone follows. The same prompt run by a developer in a local checkout applies all of them. The CI job clones the repository and invokes Claude Code from a scratch directory outside it. What is the cause?",
  "options": [
   "The CI runner lacks the permissions to read `CLAUDE.md`, so the file is present but cannot be opened.",
   "Conventions must be passed as prompt text in non-interactive mode, since `-p` disables configuration file loading.",
   "Claude Code is being invoked outside the repository, so the project `CLAUDE.md` is never in the loaded hierarchy and the conventions are absent from context.",
   "The conventions are in a `.claude/rules/` file, and rules do not load in non-interactive invocations."
  ],
  "correct": 2,
  "whyRight": {
   "text": "Configuration loads from the hierarchy around the working directory, so a run started outside the cloned repository picks up nothing from it. The local checkout works for exactly that reason — the developer is inside the tree. The fix is to invoke from the repository root so the project configuration is in scope, which is what makes a CI run's behaviour match a local one.",
   "cite": "CCA-Prep_Domain-3_v2.md §3.1"
  },
  "whyWrong": [
   {"option": 0, "text": "A permissions fault would be a plausible CI-only failure, but the job clones the repository successfully and reads its files to review them. Nothing is unreadable; the configuration is simply outside the directory tree the run is anchored to.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.1"},
   {"option": 1, "text": "`-p` selects non-interactive execution and does not disable configuration loading. Passing every convention as prompt text would work around the problem by duplicating a file that already exists and would drift from it immediately.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.8"},
   {"option": 3, "text": "Path-scoped rules are not restricted to interactive sessions. The observation to explain is that nothing from the repository is reaching the run at all, which no property of one configuration mechanism accounts for.",
    "cite": "CCA-Prep_Domain-3_v2.md §3.3"}
  ]
 },

 43: {
  "g": 43, "block": 2, "domain": "D4",
  "stem": "On long review runs the findings change character as the run proceeds: early comments are specific and cite line numbers, later ones become general observations about style, and the severity labels drift upward. The system prompt specifying the finding format has not changed. What explains this and what fixes it?",
  "options": [
   "Behavioural drift as the model's own accumulated responses come to dominate its recent context; re-anchor by restating the format requirements periodically or by resetting context between segments.",
   "The later files are genuinely harder to review, so the model correctly reports at a higher level and with more caution.",
   "The system prompt is being truncated as the conversation grows, and raising its priority in the request will restore it.",
   "The model is running low on output tokens, so it compresses later findings into general observations."
  ],
  "correct": 0,
  "whyRight": {
   "text": "Over a long run the model's own earlier outputs accumulate and increasingly shape what it produces next, so the style set by a system prompt at the start gradually gives way to the pattern of recent turns. That is behavioural drift, and the corpus's fixes act on the same mechanism: re-state the constraints periodically so they are recent, or segment the run so each part starts clean.",
   "cite": "CCA-Prep_Domain-4_v2.md §4.20"
  },
  "whyWrong": [
   {"option": 1, "text": "This explains away a measurable degradation. File order in a diff is not correlated with difficulty, and the severity labels drifting upward is not something 'more caution' predicts — it is the pattern of recent outputs reinforcing itself.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.20"},
   {"option": 2, "text": "The system prompt is re-sent with every request and is not silently dropped as a conversation grows. It is present and being outweighed by accumulated recent context, which is a different problem with a different fix.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.20"},
   {"option": 3, "text": "Output limits truncate a response, producing a finding that stops mid-sentence. They do not turn specific line-referenced findings into general stylistic observations while severity labels climb.",
    "cite": "CCA-Prep_Domain-4_v2.md §4.20"}
  ]
 },

 59: {
  "g": 59, "block": 3, "domain": "D5",
  "stem": "The nightly run processes around 3,000 documents in one long session. Twice this month it has failed near document 2,400 — once on an out-of-memory kill, once on a network fault — and both times the rerun started again from document 1. What should the pipeline do so a failure does not cost the completed work?",
  "options": [
   "Persist a structured state manifest as it goes — documents completed, records produced, documents failed and why — so a rerun resumes from the manifest instead of from the beginning.",
   "Wrap the run in a retry that restarts the whole session automatically on failure, so no human has to notice and relaunch it.",
   "Split the nightly run into thirty sessions of a hundred documents, so any single failure costs at most a hundred documents of work.",
   "Raise the memory limit and add network retry logic, so the two observed failure causes stop occurring."
  ],
  "correct": 0,
  "whyRight": {
   "text": "The cost here is not that the run failed but that nothing recorded what it had already achieved. A structured state manifest written as work completes turns any interruption into a resumable checkpoint — the rerun reads what is already done and continues, and the record of which documents failed and why survives the crash rather than dying with the session.",
   "cite": "CCA-Prep_Domain-5_v2.md §5.12"
  },
  "whyWrong": [
   {"option": 1, "text": "Automatic restart removes the human delay and repeats the same 2,400 documents unattended. It makes the waste faster and less visible rather than preventing it.",
    "cite": "CCA-Prep_Domain-5_v2.md §5.12"},
   {"option": 2, "text": "Smaller sessions bound the loss, which helps, but without persisted state the pipeline still cannot tell which of the thirty completed on a partial night. It reduces the blast radius while leaving recovery a guess.",
    "cite": "CCA-Prep_Domain-5_v2.md §5.12"},
   {"option": 3, "text": "This addresses the two causes already seen and leaves the third unhandled. A run with no checkpoint loses everything to whatever fails next, so durability should not depend on having enumerated the failure modes.",
    "cite": "CCA-Prep_Domain-5_v2.md §5.12"}
  ]
 },
}

BLOCK_OF = {13: 1, 28: 2, 40: 3, 43: 3, 59: 4}
for g, n in sorted(BLOCK_OF.items()):
    path = os.path.join(HERE, f"block{n}.json")
    d = json.load(open(path, encoding="utf-8"))
    for i, q in enumerate(d["questions"]):
        if q["g"] == g:
            old = q["domain"]
            d["questions"][i] = NEW[g]
            print(f"Q{g} (block {n}): {old} -> {NEW[g]['domain']}")
            break
    else:
        raise SystemExit(f"Q{g} not found in block{n}.json")
    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("rewrites applied")
