# Results: marketing performance (fictional exercise)

The source is eight synthetic campaign/month rows from May and June 2026. All currency values are illustrative CU and the revenue field is **attributed revenue**, not proven incremental sales.

| Measure | May | June |
| --- | ---: | ---: |
| Spend | 1,800 CU | 1,970 CU |
| Impressions | 113,000 | 121,500 |
| Clicks | 3,560 | 3,835 |
| Conversions | 160 | 179 |
| Attributed revenue | 8,600 CU | 9,610 CU |
| CTR | 3.15% | 3.16% |
| Conversion rate | 4.49% | 4.67% |
| ROAS | 4.78 | 4.88 |
| Cost per conversion | 11.25 CU | 11.01 CU |

## How to explain it
June has more conversions and a modestly lower cost per conversion despite higher spend. This is the kind of relationship worth investigating rather than reporting clicks alone.

## What this does *not* prove
The exercise does not include margin, returns, attribution windows, customer overlap or a control group. Attributed revenue is not profit, and an association is not a causal marketing lift.

## Reproduce
Run `python3 projects/01-campaign-performance/analyze.py` from the portfolio root. The table uses the same sum and rate definitions as the script.
