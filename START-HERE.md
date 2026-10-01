# Start here | A five-minute reading guide

Welcome. This is a set of three **synthetic** marketing-analysis exercises arranged as a February–31 March 2026 learning chapter. The files were published later with their actual GitHub timestamps.

## If you have two minutes
Read the [homepage](README.md) and the [one-page management brief](docs/MANAGER-BRIEF.md). They explain the questions, selected results and limits without requiring you to read code.

## If you have five to ten minutes
| Question | Open | What to notice |
| --- | --- | --- |
| What belongs in a measurement plan? | [Website measurement](projects/00-marketing-measurement/README.md) and [event design](projects/00-marketing-measurement/MEASUREMENT-PLAN.md) | Proposed events are not evidence of deployment |
| What happened to campaign efficiency? | [Campaign results](projects/01-campaign-performance/RESULTS.md) | Spend, conversion rate and attributed ROAS belong together |
| Did organic search change? | [SEO findings](projects/02-organic-search/FINDINGS.md) | Weighted CTR is total clicks divided by total impressions |

The [KPI dictionary](docs/KPI-DICTIONARY.md) defines terms in everyday language. The [About me](docs/ABOUT-ME.md) page explains how this marketing work relates to the later technical projects.

## If you want to reproduce a finding
From a local checkout of this repository, run:

```bash
python3 projects/00-marketing-measurement/analyze.py
python3 projects/01-campaign-performance/analyze.py
python3 projects/02-organic-search/analyze.py
python3 run_checks.py
```

Everything uses Python 3's standard library. The source datasets are stored next to the corresponding scripts. The cross-project checks recalculate a small set of headline metrics rather than certifying a real marketing system.

## The continuation
The marketing chapter closes on 31 March. For the April–October technical continuation, read the [learning path](LEARNING-PATH.md), the separate [customer SQL case](https://github.com/libana3012-pixel/customer-sales-analysis-sql) or [revenue SQL case](https://github.com/libana3012-pixel/sales-revenue-analysis-sql).

**Privacy:** This public repository excludes employer exports and NOBIMU business-specific data.
