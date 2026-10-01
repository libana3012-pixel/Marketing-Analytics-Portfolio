# Explained | Designing a useful website measurement plan

[← Case overview](README.md) · [Event specification](MEASUREMENT-PLAN.md) · [Example input](data/website-kpis.csv) · [Analysis script](analyze.py) · [Portfolio home](../../README.md)

## The business situation
A fictional museum reports that visitors come to its website. The team wants to know whether the website helps people plan a visit. Reporting only users or page views would answer an audience question, not whether people found useful information. My first task is therefore to distinguish **reach, engagement and useful actions**.

## Why these measures and tools?
- **GA4 active users and sessions:** describe different units, people-like identities versus visit sessions. They should not be used interchangeably.
- **Engaged sessions / sessions:** show a rate of engagement under GA4's definition, rather than counting raw activity only.
- **Event planning in GTM:** defines what a directions, opening-hours or ticket-information interaction would mean. A good event needs a real trigger, consent review and testing.
- **Search Console:** answers a different search visibility question. Its clicks are not GA4 sessions.
- **Excel or simple Python checks:** turn counts into documented rates and catch impossible inputs such as engaged sessions exceeding sessions.

## Walk through a calculation
The fictional February sample contains **310 engaged sessions of 620 sessions**, yielding 310 ÷ 620 × 100 = **50.00% engagement rate**. The March sample contains 359 ÷ 665 × 100 ≈ **53.98%**. The fictional action counts are 46 and 58, but these are input examples, **not evidence that tracking was implemented**.

## Why the event names are descriptive
An event such as `view_directions` names a meaningful action. It is not called `conversion` by default: the organisation must first decide which actions genuinely qualify and validate their collection. See the [event plan](MEASUREMENT-PLAN.md) for proposed triggers and testing steps.

## What a manager could conclude
In this small example, the engagement share is higher in the second snapshot. That is a descriptive comparison, not evidence of increased attendance, ticket sales or a causal improvement. Before a real report, validate website definitions, data collection, consent conditions, reporting periods and the actual business outcomes.

## Next investigation
Test the event plan in an authorised environment, confirm duplicate-firing behaviour, segment the results carefully by acquisition source and device, and create a reporting dictionary. Do not publish real-world results until the source and permissions are understood.

[← Case overview](README.md) · [Portfolio home](../../README.md).
