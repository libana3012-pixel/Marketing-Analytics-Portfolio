# Customer behaviour | Who buys again?
**SQL · Segmentation · Data checks**

The question is not just how many orders a shop receives. It is whether customers return, purchase once, or appear in the register without ever buying anything.

This standalone analysis uses eight **fictional** customers and 12 example orders. Four of seven purchasing customers ordered more than once within the available window. This is an observed repeat-purchase share, **not a long-term retention rate**.

| Group | Customers |
| --- | ---: |
| Purchased more than once | 4 |
| Purchased once | 3 |
| No observed purchases | 1 |

### Read, reproduce, understand
- [Findings and important caveats](FINDINGS.md)
- [Database setup](data.sql)
- [Customer queries](analysis.sql)
- [Integrity checks](quality-checks.sql)

From the consolidated repository root:

```bash
sqlite3 customers.db < projects/02-customer-behaviour/data.sql
sqlite3 -header -column customers.db < projects/02-customer-behaviour/analysis.sql
```

Use a new database for setup. A `LEFT JOIN` keeps customers without purchases visible; a window function identifies their first and later orders. The case demonstrates why a metric needs a precise definition before a manager can act on it.

*Dataset is synthetic; original working files remain in the separate [customer SQL repository](https://github.com/libana3012-pixel/customer-sales-analysis-sql).*
