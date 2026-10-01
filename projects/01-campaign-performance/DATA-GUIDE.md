# Data guide | Campaign performance

[Project overview](README.md) · [Method](EXPLAINED.md) · [CSV](data/campaigns.csv) · [Python](analyze.py) · [Results](RESULTS.md)

**Source:** eight fictional campaign/month records. Currency is an invented unit, CU, not real advertising spend or sales.

| Field | Meaning | Why it is needed |
| --- | --- | --- |
| `month`, `channel`, `campaign` | Dimensions for grouping | Compare performance by period or channel |
| `spend` | Fictional channel cost | Cost-efficiency denominator |
| `impressions` | Fictional appearances | CTR denominator |
| `clicks` | Fictional clicks | Traffic and conversion-rate denominator |
| `conversions` | Recorded fictional outcomes | Outcome volume; not necessarily unique customers |
| `revenue` | Fictional *attributed* sales value | Illustrative ROAS numerator, not profit |

**How the answer is derived:** validate non-negative numeric fields → add rows by month → calculate aggregate rates *from totals* → compare months → explain caveats.

Example, February: spend = 400 + 700 + 600 + 100 = **1,800 CU**; conversions = 72 + 42 + 18 + 28 = **160**; cost per conversion = 1,800 / 160 = **11.25 CU**. Attributed revenue = 3,600 + 2,520 + 1,080 + 1,400 = **8,600 CU**; ROAS = 8,600 / 1,800 ≈ **4.78**.

Why not average campaign ROAS values? Different spend amounts mean an unweighted mean would answer a different question. Total attributed revenue / total spend describes this example's combined ratio.

A real comparison would need consistent outcome definitions, attribution windows, margins and treatment of email-channel costs.
