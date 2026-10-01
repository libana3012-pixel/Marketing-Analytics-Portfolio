# Liban Yusuf | Marketing Analytics
### February — 31 March 2026 · Marketing measurement, performance and reporting

**GA4 · GTM concepts · SEO · Excel · Campaign KPIs · Python for simple checks**

My background is in Marketing and Sales Management, with practical experience in digital analytics and reporting. This portfolio presents the **marketing-focused chapter** of my learning and professional interests: deciding what to measure, examining campaigns and explaining results in language a business can use.

The February–March label describes the **learning chapter**, not a backdated GitHub publication record. The public examples below use **newly prepared, synthetic datasets** inspired by typical marketing questions; they are not old exports or claimed client results. All commits retain their actual dates.

## About me
I'm Liban Yusuf, based in Oslo. I enjoy connecting commercial questions with useful measurements: what audiences do, what changes between periods, and what a report can — and cannot — tell us. This marketing foundation led naturally into more technical data-analysis work after March 2026.

## Two marketing cases

| Study | The question | Tools | Where to start |
| --- | --- | --- | --- |
| [00 / Website measurement](projects/00-marketing-measurement/) | Before calling a website successful, what should we actually track? | GA4 and GTM measurement planning, SEO, Excel-style KPI logic, a small Python check | [Plain-language guide](projects/00-marketing-measurement/README.md) |
| [01 / Campaign performance](projects/01-campaign-performance/) | Does increased spend come with stronger measured outcomes? | Campaign CSV, Python, CTR, conversions, cost per conversion, ROAS | [Results and method](projects/01-campaign-performance/RESULTS.md) |

## Campaign example at a glance
| Synthetic measurement | February sample | March sample |
| --- | ---: | ---: |
| Spend | 1,800 CU | 1,970 CU |
| Clicks | 3,560 | 3,835 |
| Conversions | 160 | 179 |
| Attributed revenue | 8,600 CU | 9,610 CU |
| ROAS | 4.78 | 4.88 |

CU means fictional currency units. Attributed revenue is not the same as profit or proven incremental return. These are example outputs from the included dataset, not real performance from February or March.

## My approach
1. Start with the business question, not a chart.
2. Define audience, reporting window and useful KPIs.
3. Identify which tool supplies each measure (GA4, GTM, Search Console, Excel).
4. Check source quality, calculate carefully and avoid mixing users, sessions and events.
5. Explain one useful finding and its limits.

## Repository structure
```text
projects/
  00-marketing-measurement/   event plan, fictional web KPIs, analysis
  01-campaign-performance/   campaign data, Python script, results
run_checks.py                 source-level checks for campaign example
LEARNING-PATH.md              transition after 31 March
README.md                     project overview
```

Run the practice examples with Python 3:
```bash
python3 projects/00-marketing-measurement/analyze.py
python3 projects/01-campaign-performance/analyze.py
python3 run_checks.py
```

## What came next: Data Analytics | April–October 2026
The next learning chapter develops relational SQL, customer and sales analysis, Python, data quality and BI. Those cases belong in the **Data Analytics** portfolio rather than extending the marketing chapter past 31 March:
- [Customer analysis / SQL](https://github.com/libana3012-pixel/customer-sales-analysis-sql)
- [Revenue analysis / SQL](https://github.com/libana3012-pixel/sales-revenue-analysis-sql)

Power BI, DAX, Power Query and Microsoft Fabric are skills under development; no unverified platform build or certification is described here as complete. Business-specific NOBIMU materials are kept private pending publication permission.

*Business questions first. Traceable numbers. Clear decisions.*
