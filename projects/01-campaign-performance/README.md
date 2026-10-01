# Marketing performance: traffic is not the whole story

**Reading order:** [Overview](README.md) → [Why the method was chosen](EXPLAINED.md) → [Source data](data/campaigns.csv) → [Code](analyze.py) → [Results](RESULTS.md) → [Portfolio home](../../README.md).


[← Portfolio home](../../README.md) · [Why each step was chosen](EXPLAINED.md)
**Python · CSV · KPI interpretation · Synthetic data**

## The question
A marketing manager sees clicks rising. Did the campaigns produce more business value too? This small case looks at spend, clicks, conversions and attributed revenue together rather than judging a campaign by traffic alone.

## Start here
1. Read `data/campaigns.csv`: eight made-up campaign/month records from February and March 2026.
2. Run `python3 projects/01-campaign-performance/analyze.py` from the portfolio root. No extra packages needed.
3. Compare the result with `RESULTS.md`.
4. Try changing one row and rerunning the program.

## What the words mean
| Term | Everyday meaning |
| --- | --- |
| CTR | Clicks out of all impressions |
| Conversion rate | Conversions out of clicks |
| Cost per conversion | Spend divided by conversions |
| ROAS | Attributed revenue divided by marketing spend; not profit |

The revenue figures in this exercise are hypothetical attribution values. They do not establish that an ad *caused* a sale, and a high ROAS does not guarantee profitability.

## What I would present to a manager
A one-page table with monthly spend, conversions, attributed revenue, ROAS and cost per conversion, followed by an explanation of trade-offs. The reproducible code and data are the evidence behind the summary.
