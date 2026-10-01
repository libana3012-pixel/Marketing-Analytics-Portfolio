# Data guide | Website measurement

[Project overview](README.md) · [Method](EXPLAINED.md) · [Example data](data/website-kpis.csv) · [Code](analyze.py)

**Source and format:** `website-kpis.csv` is an invented, two-row CSV. It illustrates GA4-style measurement definitions; it is not an export from an account.

| Column | Definition | Why included |
| --- | --- | --- |
| `period` | Named example month | Enables period comparisons |
| `users` | Fictional user count | Audience reach; distinct from sessions |
| `sessions` | Fictional visit/session count | Denominator for session-based rates |
| `engaged_sessions` | Example engaged-session count | Numerator for engagement rate |
| `tracked_actions` | Made-up count of selected actions | Illustrates event reporting, not ticket sales |

**Calculation path:** read each named column as an integer → reject nonpositive user/session totals and impossible engaged counts → engagement rate = engaged sessions / sessions × 100 → actions per 100 sessions = tracked actions / sessions × 100.

February: engagement 310 / 620 = **50.00%**; actions per 100 sessions = 46 / 620 × 100 ≈ **7.42**. March: 359 / 665 ≈ **53.98%**; 58 / 665 × 100 ≈ **8.72**.

An action count can include several actions by one visitor. It cannot be converted into a unique-visitor conversion rate without an additional definition and relevant event-level data. For proposed events and implementation checks, see the [measurement plan](MEASUREMENT-PLAN.md).
