"""Extract every testable bullet from the official CCA-F Exam Guide text into IDs.

Output: bullets.json  -> {"bullets": [{"id": "1.1-K1", "ts": "1.1", "kind": "K", "n": 1, "text": "..."}, ...],
                          "task_statements": {"1.1": "Design and implement agentic loops ...", ...}}
IDs:  <ts>-K<n>  Knowledge-of bullets      <ts>-S<n>  Skills-in bullets
      APP-T<n>   Appendix "Technologies and Concepts"   APP-I<n>  "In-Scope Topics"
      APP-O<n>   "Out-of-Scope Topics"
Run:  python extract_bullets.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "source", "CCA-F-Official-Exam-Guide_text.txt")
OUT = os.path.join(HERE, "bullets.json")

raw = open(SRC, encoding="utf-8").read()
raw = re.sub(r"=== PAGE \d+ ===\n", "", raw)
raw = raw.replace("Claude Certification Program Exam guide\n", "")
lines = raw.split("\n")


def join_wrapped(chunk_lines):
    out = ""
    for ln in chunk_lines:
        ln = ln.strip()
        if not ln:
            continue
        if not out:
            out = ln
        elif out.endswith("-") and not out.endswith(" -"):
            out = out + ln
        else:
            out = out + " " + ln
    return out.replace("ﬁ", "fi").replace("ﬂ", "fl")


bullets = []
task_statements = {}

# ---- domains / task statements ------------------------------------------------
i = 0
cur_ts, cur_kind, cur_n = None, None, 0
buf = []
in_body = False


def flush():
    global buf, cur_n
    if buf and cur_ts and cur_kind:
        cur_n += 1
        bullets.append({"id": f"{cur_ts}-{cur_kind}{cur_n}", "ts": cur_ts, "kind": cur_kind,
                        "n": cur_n, "text": join_wrapped(buf)})
    buf = []


while i < len(lines):
    ln = lines[i]
    m = re.match(r"^Task Statement (\d\.\d): (.*)$", ln)
    if m:
        flush()
        cur_ts = m.group(1)
        title = [m.group(2)]
        j = i + 1
        while j < len(lines) and not lines[j].startswith("Knowledge of:"):
            title.append(lines[j]); j += 1
        task_statements[cur_ts] = join_wrapped(title)
        cur_kind, cur_n = None, 0
        i = j
        continue
    if ln.startswith("Knowledge of:"):
        flush(); cur_kind, cur_n = "K", 0; i += 1; continue
    if ln.startswith("Skills in:"):
        flush(); cur_kind, cur_n = "S", 0; i += 1; continue
    if re.match(r"^Domain \d: ", ln) or ln.startswith("Sample Questions"):
        flush(); cur_ts, cur_kind = None, None
        if ln.startswith("Sample Questions"):
            break
        i += 1; continue
    if cur_ts and cur_kind:
        if ln.startswith("•"):
            flush(); buf = [ln[1:]]
        elif buf:
            buf.append(ln)
    i += 1
flush()

# ---- appendix lists -------------------------------------------------------------
def grab(start_marker, end_marker, prefix, skip_intro=True):
    s = raw.index(start_marker) + len(start_marker)
    e = raw.index(end_marker, s)
    block = raw[s:e].split("\n")
    items, cur = [], []
    for ln in block:
        if ln.startswith("•"):
            if cur: items.append(join_wrapped(cur))
            cur = [ln[1:]]
        elif cur:
            cur.append(ln)
    if cur: items.append(join_wrapped(cur))
    return [{"id": f"{prefix}{k+1}", "ts": "APP", "kind": prefix.rstrip("-")[-1], "n": k+1, "text": t}
            for k, t in enumerate(items)]

app_t = grab("Technologies and Concepts", "In-Scope Topics", "APP-T")
app_i = grab("In-Scope Topics", "Out-of-Scope Topics", "APP-I")
app_o = grab("Out-of-Scope Topics", "Exam Preparation Recommendations", "APP-O")

data = {"task_statements": task_statements, "bullets": bullets + app_t + app_i + app_o}
json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ts_b = [b for b in bullets]
print(f"task statements: {len(task_statements)}")
print(f"TS bullets: {len(ts_b)}  (K={sum(b['kind']=='K' for b in ts_b)}, S={sum(b['kind']=='S' for b in ts_b)})")
print(f"appendix: tech={len(app_t)} in-scope={len(app_i)} out-of-scope={len(app_o)}")
print(f"total ids: {len(data['bullets'])}")
