# Website measurement | February–March 2026 learning chapter
**GA4 · GTM measurement planning · SEO · Excel-style KPI analysis**

The starting point is a common marketing question: people are visiting a website, but what should we measure before calling its digital activity successful?

This is a **reconstructed, synthetic practice case organised under the February–31 March learning period**. It is not a historical GA4 export or evidence that tags were deployed in those months. My broader marketing analytics experience informs the questions.

## The practical assignment
Imagine a museum website receiving organic search, email and social traffic. Write a measurement plan that separates reach, engagement and actions indicating interest.

| Question | Useful measurement | Tool |
| --- | --- | --- |
| Who arrives? | Active users, acquisition source | GA4 |
| Do they explore? | Engaged sessions, engagement rate | GA4 |
| What are they looking for? | Opening-hours, ticket-info, directions interactions | Event design / GTM |
| Can people find the site in search? | Queries, search impressions, clicks | Google Search Console |
| What changed between snapshots? | Rates, counts, definitions and checks | Excel / Python |

Read the [event plan](MEASUREMENT-PLAN.md), inspect the [fictional data](data/website-kpis.csv), then run `python3 projects/00-marketing-measurement/analyze.py`.

## Interpretation
An engagement rate tells us something about session behaviour, not actual museum attendance. A click on ticket information is an expression of interest, not proof of a sale. This distinction informs every later project.

**Next chapter:** [Campaign measurement](../01-campaign-performance/) uses spend and conversion data to ask whether more activity is accompanied by better measured outcomes.
