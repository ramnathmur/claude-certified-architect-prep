# DASHBOARD-DATA.jsonl — schema

One JSON object per line, one line per generated paper. Machine-readable mirror of `EXAM-LOG.md`.
`EXAM-LOG.md` is authoritative; this file exists so trends can be computed without parsing prose.

## Fields

| Field | Type | Notes |
|---|---|---|
| `paper_n` | int | Generation number. **Not** attempt order |
| `format` | string | e.g. `FULL63` — set once the real item count is verified |
| `generated_date` | `YYYY-MM-DD` | |
| `attempted_date` | `YYYY-MM-DD` \| null | null until sat. **All chronology uses this field**, never `paper_n` |
| `score_source` | string \| null | `results-json` preferred. Anything else is lower trust and must be noted in the log |
| `total_correct` | int \| null | |
| `total_questions` | int \| null | |
| `estimated_scaled` | int \| null | Project estimator only — not an Anthropic figure. State the formula in the log entry |
| `total_seconds` | int \| null | Whole paper |
| `single_answer` | `[correct, of]` \| null | Split from multiple-response deliberately |
| `multi_response` | `[correct, of]` \| null | The all-or-nothing leak lives here |
| `domain_scores` | object \| null | `{"D1": [correct, of], ...}` keyed to confirmed domain codes |
| `weakest_domain` | string \| null | Free text. Say "tied" explicitly when it is |
| `confirmed_weakness` | bool \| null | Same domain unambiguously weakest on two consecutive papers **by attempt date**. A tie is `false` |
| `insight_round_due` | bool | True when this scoring brings the count to a multiple of 3 |
| `mode` | string | `exam` (no feedback) or `practice` |

## Example line

```json
{"paper_n": 1, "format": "FULL63", "generated_date": "2026-10-01", "attempted_date": null, "score_source": null, "total_correct": null, "total_questions": 63, "estimated_scaled": null, "total_seconds": null, "single_answer": null, "multi_response": null, "domain_scores": null, "weakest_domain": null, "confirmed_weakness": null, "insight_round_due": false, "mode": "exam"}
```

## Rules

1. A line is written when a paper is **generated**, with nulls. It is updated in place when scored.
2. `domain_scores` uses `[correct, of]` arrays consistently. The Foundations file drifted between
   `{"correct": n, "of": m}` and `[n, m]` mid-project, which broke every downstream reader.
3. Never compute a trend from `paper_n`. Sort by `attempted_date`.
4. If a question is discovered to be domain-mistagged, fix it in `EXAM-LOG.md` as a finding first and
   get explicit sign-off before touching this file. Shipped scores are not silently re-tagged.
