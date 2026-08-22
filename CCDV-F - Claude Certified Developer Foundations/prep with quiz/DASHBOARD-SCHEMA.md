# DASHBOARD-DATA.jsonl — schema

One JSON object per line, one line per generated paper. Machine-readable mirror of `EXAM-LOG.md`.
`EXAM-LOG.md` is authoritative; this file exists so trends can be computed without parsing prose.

## Fields

| Field | Type | Notes |
|---|---|---|
| `paper_n` | int | Generation number. **Not** attempt order |
| `format` | string | **`FULL53`** — confirmed from the official guide (53 items, 120 min) |
| `generated_date` | `YYYY-MM-DD` | |
| `attempted_date` | `YYYY-MM-DD` \| null | null until sat. **All chronology uses this field**, never `paper_n` |
| `score_source` | string \| null | `results-json` preferred. Anything else is lower trust and must be noted in the log |
| `total_correct` | int \| null | |
| `total_questions` | int \| null | |
| `estimated_scaled` | int \| null | Project estimator only — not an Anthropic figure. State the formula in the log entry |
| `total_seconds` | int \| null | Whole paper |
| `single_answer` | `[correct, of]` \| null | Split from multiple-response deliberately |
| `multi_response` | `[correct, of]` \| null | The all-or-nothing leak lives here |
| `recall_misses` | int \| null | Misses tagged `RECALL` — knew the concept, could not produce the specific |
| `concept_misses` | int \| null | Misses tagged `CONCEPT` — did not know which approach was right |
| `domain_scores` | object \| null | `{"D1": [correct, of], ... "D8": [...]}` — **D1 Agents · D2 Applications & Integration · D3 Claude Code · D4 Eval/Testing/Debugging · D5 Model Selection & Optimization · D6 Prompt & Context · D7 Security & Safety · D8 Tools & MCPs** |
| `section_scores` | object \| null | `{"2.3": [correct, of], "7.1": [...], ...}` — one key per **published skill section** touched by the paper, same `[correct, of]` shape as `domain_scores`. Sections absent from a paper are omitted rather than zero-filled. Added 2026-08-20; see rule 8 |
| `weakest_domain` | string \| null | Free text. Say "tied" explicitly when it is |
| `confirmed_weakness` | bool \| null | Same domain unambiguously weakest on two consecutive papers **by attempt date**. A tie is `false`. **D3 and D4 are never eligible** — 1–2 items each |
| `insight_round_due` | bool | True when this scoring brings the count to a multiple of 3 |
| `mode` | string | `exam` (no feedback) or `practice` |

## Example line

```json
{"paper_n": 1, "format": "FULL53", "generated_date": "2026-12-01", "attempted_date": null, "score_source": null, "total_correct": null, "total_questions": 53, "estimated_scaled": null, "total_seconds": null, "single_answer": null, "multi_response": null, "recall_misses": null, "concept_misses": null, "domain_scores": null, "section_scores": null, "weakest_domain": null, "confirmed_weakness": null, "insight_round_due": false, "mode": "exam"}
```

## Rules

1. A line is written when a paper is **generated**, with nulls. It is updated in place when scored.
2. `domain_scores` uses `[correct, of]` arrays consistently. The CCAR-F file drifted between
   `{"correct": n, "of": m}` and `[n, m]` mid-project, which broke every downstream reader.
3. Never compute a trend from `paper_n`. Sort by `attempted_date`.
4. If a question is discovered to be domain-mistagged, fix it in `EXAM-LOG.md` as a finding first and
   get explicit sign-off before touching this file. Shipped scores are not silently re-tagged.
5. `recall_misses + concept_misses` must equal the total miss count. Every miss gets a tag; there is no
   "unclassified". This is the **tripwire** on the judgement-shaped assumption, not the main
   diagnostic — see `EXAM-LOG.md` convention 8.
6. `format` is **`FULL53`**, confirmed from the official guide v1.0 (July 2026). If a paper is
   generated at a different length — a short drill, say — name it explicitly (`DRILL20`) so it is never
   mistaken for a full simulation in a trend.
7. `domain_scores` for **D3 and D4 will often be `[0,1]` or `[1,1]`**. That is the real paper's shape,
   not a data problem. Do not smooth it, and do not read a trend from it.
8. `section_scores` is finer-grained than the real score report, which returns percent-correct by
   **domain** only. It exists because misses are logged by section and the corpus is built section by
   section, so it is the field that tells you which of the **25 published skills** is actually weak.
   Two cautions. Most sections carry **one or two items on a 53-item paper**, so a single section's
   number on a single paper is noise — read it across papers, sorted by `attempted_date`, never
   in isolation. And the section on any given item is **this project's assignment**, not a published
   fact; the guide names domains for its own sample items and never names sections. Rule 4 applies to
   section re-tagging exactly as it does to domain re-tagging: raise it in `EXAM-LOG.md` as a finding
   and get sign-off before changing a shipped paper.
