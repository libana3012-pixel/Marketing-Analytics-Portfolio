# Data guide | Organic search

[Project overview](README.md) · [Method](EXPLAINED.md) · [CSV](data/search-performance.csv) · [Python](analyze.py) · [Findings](FINDINGS.md)

**Source:** six synthetic Search Console-style records covering three page groups and two months. They are not actual account exports.

| Column | Meaning | Why it is included |
| --- | --- | --- |
| `period` | Example month | Enables comparable monthly groups |
| `page_group` | Exhibitions, Visitor information or Editorial | Shows which content group contributed to change |
| `impressions` | Number of fictional appearances in search results | Denominator for click-through rate |
| `clicks` | Fictional search-result clicks | Numerator for click-through rate |

**How the calculation works:** read source rows → reject negative numbers, clicks greater than impressions and duplicated period/page-group pairs → sum clicks and impressions by month → compute total clicks / total impressions × 100.

February: 18,000 + 12,000 + 9,000 = **39,000 impressions**, while 720 + 660 + 270 = **1,650 clicks**. Hence CTR = 1,650 / 39,000 × 100 ≈ **4.23%**. March: 1,965 / 44,500 × 100 ≈ **4.42%**.

**Reason for using totals:** simply averaging the three category CTRs assigns equal weight to groups with different impression counts. The weighted rate uses the actual underlying denominators.

The observed change is descriptive. The data has no queries, ranking positions or documented intervention with which to identify a cause. Search-result clicks are not equivalent to website sessions.
