# KPI dictionary | Marketing analytics

A shared vocabulary matters more than a decorative dashboard. These definitions prevent different sources being interpreted as if they measure the same thing.

| Metric | Definition | Source / typical tool | Caution |
| --- | --- | --- | --- |
| Users | People represented by the reporting tool's user identity rules | GA4 | Consent, identity resolution and sampling affect interpretation |
| Sessions | Recorded visit sessions | GA4 | Not the same as users or Search Console clicks |
| Engagement rate | Engaged sessions / sessions | GA4 | Read the report's engaged-session definition |
| Event count | Number of recorded event occurrences | GA4 / GTM setup | Events are not unique people or real-world purchases |
| Search impressions | Times a result appeared in eligible search results | Search Console | Visibility, not visits |
| Search CTR | Search clicks / search impressions | Search Console | Use totals for a weighted combined CTR |
| Campaign CTR | Ad clicks / ad impressions | Advertising platform | Not a conversion measure |
| Conversion rate | Recorded conversions / clicks for this particular exercise | Campaign CSV | Platforms may use different denominators and attribution rules |
| Cost per conversion | Marketing spend / recorded conversions | Campaign CSV | Not necessarily cost per *new customer* |
| ROAS | Attributed revenue / ad spend | Campaign CSV | Not incremental effect and not profit |
| Average order value | Recorded gross sales value / distinct orders | SQL | Avoid multiplying the order count through joins |

**Data contracts:** Align attribution windows, currency, reporting dates, consent conditions, granularity (user/session/event/order), filters and source definitions before comparing reports. Do not describe zero tracked conversions as proof of no business outcomes.

The portfolio uses synthetic examples, while the named tools describe where similar measures might be obtained in real analysis.
