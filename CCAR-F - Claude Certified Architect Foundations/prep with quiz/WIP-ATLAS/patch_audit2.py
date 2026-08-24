"""Tighten the six Remember lines that the audit fixes pushed over the 30-word target. Same abort-on-mismatch rule."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = [
("items_d1a.py",
 "Gap evaluation belongs to the coordinator: re-delegate targeted queries, re-invoke synthesis, stop on a coverage criterion. Handing synthesis the full search tool set is the distractor; one narrowly scoped lookup tool for a frequent simple check is the keyed answer on that question, as D2-08 sets out.",
 "Gap evaluation belongs to the coordinator: re-delegate, re-invoke synthesis, stop on a coverage criterion. Handing synthesis the full search toolset is the distractor; one scoped lookup tool is not (D2-08)."),
("items_d2a.py",
 "One tool, several jobs → split it, one purpose per tool with its own input and output contract. Consolidating is a valid design in its own right, but it is not the fix for a tool whose description cannot state one purpose.",
 "One tool, several jobs → split it, one purpose per tool with its own contract. Consolidating is valid elsewhere, not the fix when a description cannot state one purpose."),
("items_d4b.py",
 "Confidence routes a finding; it never suppresses one. Reporting it per finding and sending the doubtful ones to a person is the answer, while instructing the model to report only high-confidence findings is the distractor (D4-01, D4-02).",
 "Confidence routes a finding; it never suppresses one. Report it per finding, send the doubtful ones to a person. Filtering to high-confidence only is the distractor (D4-01)."),
("items_d5a.py",
 "Specific recall from months of history → retrieval of the relevant exchanges rather than a summary. The exam-relevant half is that summarisation keeps the gist and loses the sentence being asked about; the guide puts embedding and vector-database implementation details out of scope, so no question will turn on how retrieval is built.",
 "Specific recall from months of history → retrieve the actual exchange; summarisation keeps the gist and loses the sentence being asked about. How retrieval is built is out of scope."),
("items_d5b.py",
 "Agents write state to a known path; the coordinator reads the manifest on resume and injects it. Designing recovery around exported state is the point; assuming the dead run's context is still there is the distractor.",
 "Agents write state to a known path; the coordinator reads the manifest on resume and injects it. Assuming the dead run's own context is still available is the distractor."),
("items_d5b.py",
 "`/compact` shrinks a session already full of discovery output, which is exactly what the guide lists it for. Where the choice is still open, isolating discovery in a subagent keeps the detail out of the main window in the first place.",
 "`/compact` shrinks a session already full of discovery output, which is what the guide lists it for. Where the choice is still open, isolate discovery in a subagent instead."),
]

errs = [f"{f}: {open(os.path.join(HERE,f),encoding='utf-8').read().count(o)} matches :: {o[:60]}"
        for f, o, n in P if open(os.path.join(HERE, f), encoding="utf-8").read().count(o) != 1]
if errs:
    print("ABORTED:"); [print("  -", e) for e in errs]; sys.exit(1)

for f, o, n in P:
    p = os.path.join(HERE, f)
    s = open(p, encoding="utf-8").read().replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)
print(f"{len(P)} Remember lines tightened")
