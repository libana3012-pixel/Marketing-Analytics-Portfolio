# Explained | Separating search visibility from click-through performance

[← Case overview](README.md) · [Findings](FINDINGS.md) · [Input](data/search-performance.csv) · [Code](analyze.py) · [Portfolio home](../../README.md)

## The question
Organic search clicks rose in the fictional example. There are at least two separate explanations to test descriptively: the site's pages appeared more frequently in search results (**impressions**), and the share of impressions leading to clicks (**CTR**) may have changed. Without separating these, one can overinterpret a raw click count.

## Why group by page type?
The dataset splits results into Exhibitions, Visitor information and Editorial. Different page intentions may affect the likelihood of a search-result click. Looking at page groups can reveal whether the overall result obscures variation.

## Follow the figures
February has 39,000 impressions and 1,650 clicks. Weighted CTR = 1,650 ÷ 39,000 × 100 ≈ **4.23%**. March has 44,500 impressions and 1,965 clicks, giving **4.42%**. The sample therefore records 315 extra clicks (+19.09%) alongside more impressions (+14.10%) and a slightly higher overall CTR.

**Why weighted CTR?** The correct combined rate is total clicks divided by total impressions. An unweighted mean of three page-group rates would treat a small editorial category as equally influential as a larger search category.

## Data checking
The script rejects negative values, clicks larger than impressions and duplicate page-group/period combinations. These safeguards matter because rates calculated from implausible source rows can appear precise while being wrong.

## Limits
The data does not contain search positions, query mix, device, country or a record of SEO interventions. Two months cannot establish why performance changed. Search Console clicks are not interchangeable with GA4 sessions.

## Next step
Compare branded and non-branded queries, search appearance, devices and page-level performance, then review tracking and content changes within the relevant dates before suggesting an action.

[← Case overview](README.md) · [Portfolio home](../../README.md).
