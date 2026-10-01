# Organic search performance | A small SEO review

**Reading order:** [Data fields and worked calculations](DATA-GUIDE.md) · [Overview](README.md) → [Why the method was chosen](EXPLAINED.md) → [Source data](data/search-performance.csv) → [Code](analyze.py) → [Findings](FINDINGS.md) → [Portfolio home](../../README.md).


[← Portfolio home](../../README.md) · [Why each step was chosen](EXPLAINED.md)

**Marketing Analytics · Search Console concepts · CSV · Python**

## Business question
If organic clicks rise, is it because the website appeared more often in search, because people clicked more frequently, or both? This short case compares search impressions, clicks and CTR (click-through rate) across three fictional page groups.

The February and March data are **synthetic** and were created as a portfolio exercise. They are not a historical Search Console export.

## Summary

| KPI | February | March |
| --- | ---: | ---: |
| Search impressions | 39,000 | 44,500 |
| Organic search clicks | 1,650 | 1,965 |
| Weighted CTR | 4.23% | 4.42% |

March has 315 more clicks (+19.09%). Both total impressions and the overall click-through rate increased in the practice dataset. That is a descriptive observation, not proof that any particular SEO change caused it.

## Reproduce
```bash
python3 projects/02-organic-search/analyze.py
```

| File | Purpose |
| --- | --- |
| [Fictional input](data/search-performance.csv) | Period and page-group source rows |
| [Analysis](analyze.py) | Validation, grouping and weighted CTR |
| [Findings](FINDINGS.md) | What the comparison can and cannot tell us |

**Important:** Search Console impressions/clicks and GA4 users/sessions are different measurements. Do not combine them into a single rate or assume they reconcile one-to-one.
