# Liban Yusuf | Marketing & Data Analytics
### From measuring digital performance to investigating the data behind it

I have a bachelor's degree in Marketing and Sales Management and practical experience with digital analytics and reporting. Marketing questions came first: who are we reaching, what happens after a visit, and which metrics are useful to a decision-maker? In **March 2026**, I began building a more technical data-analysis practice around SQL and Python. This portfolio connects those two areas rather than presenting them as unrelated tool collections.

The material here is self-contained and uses **synthetic practice data**. Data dates are not publication dates, and a completed exercise does not imply commercial client outcomes. Business-specific work, including NOBIMU, remains in a separate private workspace.

## Pick a question

| Chapter | Business question | Tools and evidence |
| --- | --- | --- |
| [00 · Website measurement](projects/00-marketing-measurement/) | What should a marketing analyst measure before reporting success? | GA4/GTM-style event design, SEO and Excel-style KPI logic; synthetic specification |
| [01 · Campaign performance](projects/01-campaign-performance/) | Did more spend produce stronger measured outcomes? | Python, CSV, campaign KPI calculations and results |
| [02 · Customer behaviour](projects/02-customer-behaviour/) | Who buys again, once, or never? | SQLite, SQL joins, segmentation and data checks |
| [03 · Revenue analysis](projects/03-revenue-analysis/) | Why does sales value move when order count does not? | SQL, revenue measures, quality checks and findings |

**Sample figures, not employer performance:** the campaign exercise moves from 160 to 179 conversions; the customer sample has four repeat purchasers among seven purchasers; the sales sample contains 12 orders worth 2,020 fictional currency units (CU).

## About the analyst

My starting point is commercial understanding: a website visit, campaign click or purchase is only meaningful once its definition and context are clear. I use SQL and Python to examine the underlying records, check a result and explain it in plain language. I want the reader to see both the calculation and the judgement around it — including what cannot be concluded.

## How the disciplines connect

```text
Marketing question
    → measurement plan (GA4 / GTM, SEO, Excel)
    → campaign performance (Python)
    → customers and purchases (SQL)
    → validation and interpretation
    → management reporting (Power BI: in development)
```

## Tools, with honest status

| Area | Tools | Evidence and current depth |
| --- | --- | --- |
| Digital measurement | GA4, GTM, SEO | Professional experience; public fictional measurement exercise |
| Reporting and preparation | Excel, KPI definitions | Professional reporting background; documented analytical measures |
| Querying data | SQL, SQLite | Reproducible customer/revenue analyses and source checks |
| Programming | Python, CSV, standard library | Campaign calculation and cross-project verification scripts |
| Business intelligence | Power BI, Power Query, DAX | Learning and report-design stage; no finished PBIX claimed here |
| Data platforms | Microsoft Fabric | Next area of study; no deployment claimed |
| Working practice | Git/GitHub | Versioned projects and reproducibility checks |

## Learning path, not a fabricated commit timeline

Earlier work centred on marketing measurement, GA4, SEO and reporting. Beginning in **March 2026**, the learning focus expanded to SQL and Python and then to applying technical methods to commercial questions. The case studies here document that *development in subject matter*, not a claim that these particular files were published on historical dates. [See the progression and next experiments](LEARNING-PATH.md).

## Reproduce the analyses

Requires Python 3 and SQLite. From the root of this repository:

```bash
python3 projects/01-campaign-performance/analyze.py
python3 run_checks.py
```

Each chapter has its own README, source data, methods, findings and limitations. Start with the question, inspect the code only when you want to see how the answer was produced.

---
*Making data useful for business decisions.*
