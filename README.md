# Liban Yusuf | Marketing Analytics

[![Verify marketing case studies](https://github.com/libana3012-pixel/marketing-analytics-portfolio/actions/workflows/verify.yml/badge.svg)](https://github.com/libana3012-pixel/marketing-analytics-portfolio/actions/workflows/verify.yml)
### Website measurement · Campaign performance · Organic search

[Start here: a five-minute tour](START-HERE.md)

**Portfolio chapter: February – 31 March 2026**  
**Focus:** GA4 · GTM concepts · SEO / Search Console · Excel-style reporting · Python

I'm based in Oslo and have a bachelor's degree in Marketing and Sales Management, with practical experience in digital analytics and reporting. I enjoy turning marketing questions into measurements that can be checked and explained. This collection shows how I approach three everyday marketing-analyst problems, from defining a useful event through to interpreting campaign and organic-search KPIs.

> **A note on dates and evidence:** February–March describes the marketing-focused chapter of my development. The public examples were prepared later using **synthetic data**. They are not historical GA4 exports, employer performance figures, or backdated GitHub work. Commits retain their real timestamps.

## Start with a business question

| Project | What I investigate | Evidence |
| --- | --- | --- |
| [01 — Website measurement](projects/00-marketing-measurement/) | What should we measure before declaring a website successful? | Event plan, fictional website metrics and analysis |
| [02 — Campaign performance](projects/01-campaign-performance/) | Do more clicks and higher spend translate into stronger measured outcomes? | Eight-row campaign CSV, Python, KPI calculations, findings |
| [03 — Organic search](projects/02-organic-search/) | Are extra SEO clicks coming from more visibility, a better CTR, or both? | Page-group search data, weighted CTR and Python checks |

### Selected findings from the practice data

| Measure | February sample | March sample | Interpretation |
| --- | ---: | ---: | --- |
| Campaign conversions | 160 | 179 | Recorded conversions rose alongside spend |
| Campaign cost per conversion | 11.25 CU | 11.01 CU | Lower cost per recorded outcome |
| Campaign ROAS | 4.78 | 4.88 | Attributed revenue / spend, not profit |
| Organic search clicks | 1,650 | 1,965 | Separate fictional SEO dataset |
| Organic search CTR | 4.23% | 4.42% | Calculated from total clicks / total impressions |

CU = fictional currency units. These figures are descriptive, not evidence of causal marketing lift.

## About me

My starting point is a business question rather than a software tool. I want to understand what people do, whether metrics have the right definitions, and what a decision-maker can safely conclude. I use smaller exercises to practise that reasoning and build technical confidence.

[Read my introduction](docs/ABOUT-ME.md) · [One-page manager brief](docs/MANAGER-BRIEF.md) · [KPI definitions](docs/KPI-DICTIONARY.md)

## How I use tools together

```text
Business question
   ├── Website behaviour → GA4 / event specification / GTM
   ├── Search visibility  → Search Console / SEO
   └── Paid campaigns    → Platform exports
               ↓
      Definitions and source checks
               ↓
        Excel / CSV / Python
               ↓
    Clear KPI report and next question
```

GA4 and Search Console are different sources, not interchangeable counts. The event-tracking project is a *design exercise*, not an assertion that a live GTM implementation has been deployed.

## Folder guide

```text
projects/
  00-marketing-measurement/  Event plan, practice metrics, code
  01-campaign-performance/  Campaign CSV, analysis, results
  02-organic-search/        Search CSV, analysis, findings
docs/
  ABOUT-ME.md               Background and approach
  KPI-DICTIONARY.md         Definitions and metric limitations
  MANAGER-BRIEF.md          Example of executive communication
LEARNING-PATH.md            The transition to data analysis
run_checks.py               Recalculates portfolio headline figures
```

## Reproduce the examples

Python 3 is sufficient; no additional packages or account access are required.

```bash
python3 projects/00-marketing-measurement/analyze.py
python3 projects/01-campaign-performance/analyze.py
python3 projects/02-organic-search/analyze.py
python3 run_checks.py
```

## The next chapter | Data Analytics, April–October 2026

After the marketing-focused chapter, I concentrated on SQL, Python, data modelling, quality checks and reporting. You can inspect my separate public [customer analysis](https://github.com/libana3012-pixel/customer-sales-analysis-sql) and [revenue analysis](https://github.com/libana3012-pixel/sales-revenue-analysis-sql) repositories, or read the [learning path](LEARNING-PATH.md).

Power BI, DAX, Power Query and Fabric are part of continued development. I will add verified implementations and certifications when complete. NOBIMU company-specific reporting stays in a separate private workspace pending publication permission.

---
*Business questions first. Traceable numbers. Clear decisions.*
