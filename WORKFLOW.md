# How the analysis was carried out

[Portfolio home](README.md) | [Project guide](START-HERE.md) | [KPI definitions](docs/KPI-DICTIONARY.md)

These are three synthetic marketing-analysis exercises. The source files are transparent CSV examples, rather than live exports. The public scripts use **Python 3** with its standard library, while **GA4, GTM and Google Search Console** supply the measurement concepts. The event plan is a proposed specification, not a deployed setup.

## 1. Website measurement: decide what success means

**Question:** Does a website visit tell us whether a prospective museum visitor found useful information?

**Action and reason:** I separated users, sessions and engaged sessions instead of treating all traffic as the same measure. A session-based engagement rate describes a different question from the number of users. I then outlined events such as viewing directions or ticket information because those interactions could help explain visitor intent. They are not automatically sales or completed visits.

**How:** The [event plan](projects/00-marketing-measurement/MEASUREMENT-PLAN.md) documents suggested triggers and checks. The [CSV](projects/00-marketing-measurement/data/website-kpis.csv) gives two fictional periods. [Python](projects/00-marketing-measurement/analyze.py) validates sensible values and divides engaged sessions by sessions.

**Recreate one answer:** February has 310 engaged sessions out of 620 sessions, so 310 / 620 × 100 = **50.00%**. March has 359 / 665 × 100 = **53.98%**. The comparison illustrates a measurement method; it cannot prove museum attendance or actual event deployment. [Full explanation](projects/00-marketing-measurement/EXPLAINED.md).

## 2. Campaign performance: distinguish activity from efficiency

**Question:** If clicks increase, did measured campaign efficiency also change?

**Action and reason:** I first summed spend, impressions, clicks, conversions and attributed revenue by month. Calculating an overall rate from summed inputs is preferable to averaging the four campaign rates without weighting, because those campaigns have different impression and click volumes.

**How:** The [eight source records](projects/01-campaign-performance/data/campaigns.csv) are processed by [Python](projects/01-campaign-performance/analyze.py). The script checks for negative input, groups records by month and channel, then calculates CTR, conversion rate, cost per conversion and ROAS, with missing denominators handled explicitly.

**Recreate one answer:** February spend of 1,800 CU / 160 recorded conversions = **11.25 CU per conversion**. March's 1,970 / 179 ≈ **11.01 CU**. This suggests a modest difference in the *fictional recorded cost per outcome*, not causal advertising lift or profit. [Interpretation](projects/01-campaign-performance/RESULTS.md) | [Method reasoning](projects/01-campaign-performance/EXPLAINED.md).

## 3. Organic search: separate visibility from click rate

**Question:** Did the extra organic clicks accompany more search visibility, a higher CTR, or both?

**Action and reason:** I grouped the three fictional page types by month and summed impressions and clicks, then calculated the combined CTR from totals. An ordinary average of three individual CTRs would wrongly give every page group equal weight regardless of its impressions.

**How:** Inspect the [source CSV](projects/02-organic-search/data/search-performance.csv) and [script](projects/02-organic-search/analyze.py). The script rejects impossible clicks/impressions and repeated period/group combinations.

**Recreate one answer:** 1,650 clicks / 39,000 impressions × 100 ≈ **4.23%** in February, versus 1,965 / 44,500 × 100 ≈ **4.42%** in March. These are Search Console-style metrics; they are not interchangeable with GA4 sessions. [Interpretation](projects/02-organic-search/FINDINGS.md) | [Method reasoning](projects/02-organic-search/EXPLAINED.md).

## How the output is checked

Run these commands from the repository root with Python 3 (no additional packages):
```bash
python3 projects/00-marketing-measurement/analyze.py
python3 projects/01-campaign-performance/analyze.py
python3 projects/02-organic-search/analyze.py
python3 run_checks.py
```

The [GitHub Actions workflow](.github/workflows/verify.yml) runs the examples and assertions when the relevant files change. The automated checks establish consistency with the included fictional fixtures; they do not establish the validity of any real marketing campaign.
