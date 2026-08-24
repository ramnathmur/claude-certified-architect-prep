"""Bring the stem median into the 50-55 band and the inline-token rate into the target
band. Additions carry real situational detail (counts, config, observed behaviour), never
filler; option edits add a code/config token without changing what the option means."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# Clause appended immediately before the closing question sentence.
INSERTS = {
4:  "Two of the three share a surname with the caller.",
5:  "The queue currently receives about ninety transfers a week.",
11: "The subagent has already retried twice on its own before giving up.",
14: "Tools from every configured server are discovered together at connection time.",
21: "The skill currently runs with no scoping at all and has `Bash` available to it.",
23: "The scratchpad question has come up twice before and was deferred each time.",
25: "Each rule file carries a `paths:` list in its YAML frontmatter.",
26: "Roughly sixty of the ninety turns are scheduling talk.",
27: "The job runs unattended at 02:00 and nobody reads its output until morning.",
33: "Roughly forty agreements arrive each month and no two describe the loan identically.",
39: "The worker's own retry succeeds on the second attempt in every observed case.",
42: "Both tools are called on nearly every task, always in the same order.",
45: "Each worker type currently holds between four and six tools.",
47: "The reviewer will process about forty more batches in the same session.",
51: "Extraction volume is roughly 1,800 documents a day across four record types.",
53: "The opener costs about fifteen words before any finding appears.",
56: "Token usage per request has roughly tripled between turn five and turn fifty.",
57: "The coordinator has not responded to either clarification request.",
59: "The quality system's intake checks are documented and stable.",
60: "The two categories accounted for about a third of all findings before they were switched off.",
}

# Option rewrites that introduce an inline code/config token without altering meaning.
OPTION_EDITS = {
6:  {0: "The token would expire before slower callers finish confirming, producing spurious `isError` responses."},
16: {2: "Both files load together and both instructions are in context, so the conflict must be resolved by editing them."},
18: {1: "Plan mode should apply to any change crossing a package boundary, whatever its size."},
24: {0: "Provide the three missed requirements together in one detailed message and regenerate once."},
28: {1: "A JSON Schema attached to the prompt describing the permitted output shape."},
30: {1: "Consumers importing the wrapper names — first collect every exported alias, then Grep for each."},
36: {1: "Glob the module tree and Read each match in order, stopping once the window is two-thirds full."},
39: {3: "Inside the tool, which should return success with the failure recorded in an `isError` metadata field."},
42: {3: "Whether the coordinator's tool count is currently near the reliable four-to-five band."},
2:  {1: "Merge the two into one `lookup_usage` tool that returns billing totals and meter data together."},
8:  {3: "A generic `isError` failure carrying a support reference number the caller can quote later."},
17: {3: "Keep the file as it is but reorder it so the universal standards appear first."},
31: {2: "Increase the number of exploration workers so more files are covered on each run."},
48: {2: "Rate each narrative's unusualness from one to five and surface only the top band."},
}

# Only these actually add a token; the rest are no-ops kept for provenance. Filter at apply time.

def split_tail(stem):
    """Return (body, final question sentence)."""
    parts = re.split(r"(?<=[.?!])\s+", stem.strip())
    return " ".join(parts[:-1]), parts[-1]


ins = opt = 0
for i in range(1, 5):
    p = os.path.join(HERE, f"block{i}.json")
    b = json.load(open(p, encoding="utf-8"))
    for q in b["questions"]:
        g = q["g"]
        if g in INSERTS:
            body, tail = split_tail(q["stem"])
            if tail.lower().startswith("select "):          # MR: keep "Select N." last
                body2, tail2 = split_tail(body)
                q["stem"] = f"{body2} {INSERTS[g]} {tail2} {tail}".strip()
            else:
                q["stem"] = f"{body} {INSERTS[g]} {tail}".strip()
            ins += 1
        if g in OPTION_EDITS:
            for idx, text in OPTION_EDITS[g].items():
                if "`" in text and "`" not in q["options"][idx]:
                    q["options"][idx] = text
                    opt += 1
    json.dump(b, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"stem inserts applied: {ins}")
print(f"option token edits applied: {opt}")
