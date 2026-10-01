# Explained | Why examine cost and conversion, not just clicks?

[← Case overview](README.md) · [Results](RESULTS.md) · [Input data](data/campaigns.csv) · [Code](analyze.py) · [Portfolio home](../../README.md)

## Business question
A manager sees that campaign clicks increased from one month to the next. Should the team call this success? Clicks alone do not tell us how much was spent or how many measured outcomes followed. I therefore analyse volume and efficiency together.

## Data selection
The fictional input has eight campaign-month rows: Brand Search, Non-brand Search, Prospecting Social and an Email Newsletter for February and March. Every row has spend, impressions, clicks, conversions and attributed revenue. These are **practice values**, not platform exports or a claim that email and paid channels follow the same commercial attribution rules.

## Why aggregate before calculating rates?
A rate should be calculated from the relevant totals. For example, February CTR = 3,560 clicks ÷ 113,000 impressions × 100 = **3.15%**. Taking an unweighted average of campaign CTRs would give disproportionate influence to the smallest campaign. The Python script sums the underlying counts first, then calculates each overall rate.

## Calculations worth understanding
| Measure | Formula | February example | Why it matters |
| --- | --- | ---: | --- |
| Click-through rate | Clicks / impressions | 3.15% | Were impressions accompanied by clicks? |
| Conversion rate | Conversions / clicks | 4.49% | How often did a click lead to a recorded outcome? |
| Cost per conversion | Spend / conversions | 11.25 CU | What did each recorded outcome cost? |
| ROAS | Attributed revenue / spend | 4.78 | Value attributed to campaigns relative to spend; **not profit** |

March spend = 1,970 CU, conversions = 179 and cost per conversion ≈ 11.01 CU. Costs rose, but the sample records more conversions and a modestly lower cost per measured outcome.

## Why use Python?
`csv.DictReader` makes each input field explicit. The program checks for negative values, builds monthly and channel-level totals, and avoids division by zero by returning `None` when a denominator is missing. This makes the calculation repeatable and lets a reader inspect it. It is a small analytical exercise rather than a production attribution model.

## Interpretation and boundaries
The observed figures do not establish *incremental* marketing impact. The data lacks control groups, margin, refunds, attribution windows and customer duplication rules. Also, email and advertising spend can have different accounting definitions; real reporting would establish comparable scope before combining channels.

## Next question
Inspect channel-level differences, conversion definitions, tracking quality, spend allocation and profitability before recommending a budget change.

[← Case overview](README.md) · [Results](RESULTS.md) · [Portfolio home](../../README.md).
