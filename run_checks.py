"""Recalculate headline values from this portfolio's synthetic source files.

Run from anywhere: python3 run_checks.py
Uses the Python standard library. Throws AssertionError if a metric changes unexpectedly.
"""
from collections import defaultdict
from pathlib import Path
import csv
import sqlite3

BASE = Path(__file__).resolve().parent


def sql_check(folder, expected):
    db = sqlite3.connect(":memory:")
    db.executescript((BASE / folder / "data.sql").read_text(encoding="utf-8"))
    for label, sql, value in expected:
        actual = db.execute(sql).fetchone()[0]
        assert actual == value, f"{folder}: {label}: expected {value}, found {actual}"
        print(f"PASS  {label}: {actual}")
    db.close()


def campaign_check():
    source = BASE / "projects/01-campaign-performance/data/campaigns.csv"
    months = defaultdict(lambda: defaultdict(float))
    with source.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for field in ("spend", "impressions", "clicks", "conversions", "revenue"):
                v = float(row[field])
                assert v >= 0, f"Negative value: {row}"
                months[row["month"]][field] += v
    expected = {
        "2026-05": {"spend": 1800, "clicks": 3560, "conversions": 160, "revenue": 8600},
        "2026-06": {"spend": 1970, "clicks": 3835, "conversions": 179, "revenue": 9610},
    }
    for month, metrics in expected.items():
        for field, value in metrics.items():
            actual = months[month][field]
            assert actual == value, f"{month} {field}: {actual} != {value}"
            print(f"PASS  {month} {field}: {actual:g}")


if __name__ == "__main__":
    print("Campaign performance")
    campaign_check()
    print("\nCustomer behaviour")
    sql_check("projects/02-customer-behaviour", [
        ("Registered customers", "SELECT COUNT(*) FROM customers", 8),
        ("Orders", "SELECT COUNT(*) FROM orders", 12),
        ("Repeat customers", """SELECT COUNT(*) FROM
            (SELECT customer_id FROM orders GROUP BY customer_id HAVING COUNT(*) > 1)""", 4),
        ("Customers without orders", """SELECT COUNT(*) FROM customers c WHERE NOT EXISTS
            (SELECT 1 FROM orders o WHERE o.customer_id=c.customer_id)""", 1),
    ])
    print("\nSales and revenue")
    sql_check("projects/03-revenue-analysis", [
        ("Orders", "SELECT COUNT(*) FROM orders", 12),
        ("Order lines", "SELECT COUNT(*) FROM order_items", 19),
        ("Units", "SELECT SUM(quantity) FROM order_items", 28),
        ("Gross sales value", "SELECT SUM(quantity*unit_price) FROM order_items", 2020),
    ])
    print("\nAll portfolio checks passed.")
