# Sales and revenue | Why did the numbers change?
**SQL · Commercial performance · KPI validation**

Imagine a shop whose order count stays constant, but revenue changes. What actually drove the movement?

This reproducible, **fictional** dataset has 12 orders and 19 order lines from March–June 2026.

| Measure | Result |
| --- | ---: |
| Gross sales value | 2,020 CU |
| Separate orders | 12 |
| Average order value | 168.33 CU |
| Units sold | 28 |

Every month has three orders. June's 605 CU is the highest monthly sales value in the sample, so the difference comes from basket value rather than more orders. CU means hypothetical currency units.

### Explore
- [Business findings](RESULTS.md)
- [Create the database](data.sql)
- [Analysis queries](analysis.sql)
- [Data checks](quality-checks.sql)

From the consolidated repository root:

```bash
sqlite3 sales.db < projects/03-revenue-analysis/data.sql
sqlite3 -header -column sales.db < projects/03-revenue-analysis/analysis.sql
```

The analysis keeps transaction-time prices on the order line and checks order-level aggregates to avoid duplicate counts when tables are joined. It does not model profit, taxes or returns.

*The original learning history is preserved in the separate [revenue SQL repository](https://github.com/libana3012-pixel/sales-revenue-analysis-sql).*
