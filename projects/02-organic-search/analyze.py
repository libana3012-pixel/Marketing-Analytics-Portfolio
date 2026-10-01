"""Reproduce a fictional SEO review using Python's standard library only."""
from pathlib import Path
from collections import defaultdict
import csv

SOURCE = Path(__file__).parent / "data/search-performance.csv"

def calculate(path=SOURCE):
    totals = defaultdict(lambda: {"impressions": 0, "clicks": 0})
    pages = defaultdict(dict)
    with Path(path).open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            period, group = row["period"], row["page_group"]
            impressions, clicks = int(row["impressions"]), int(row["clicks"])
            if impressions < 0 or clicks < 0 or clicks > impressions:
                raise ValueError(f"Invalid search metrics: {row}")
            if period in pages[group]:
                raise ValueError(f"Duplicate period/page group: {row}")
            pages[group][period] = {"impressions": impressions, "clicks": clicks}
            totals[period]["impressions"] += impressions
            totals[period]["clicks"] += clicks
    for period, metrics in sorted(totals.items()):
        metrics["ctr_pct"] = round(100 * metrics["clicks"] / metrics["impressions"], 2) if metrics["impressions"] else None
    return dict(totals), dict(pages)

if __name__ == "__main__":
    totals, pages = calculate()
    print("TOTAL ORGANIC SEARCH PERFORMANCE (synthetic)")
    for period, metrics in sorted(totals.items()):
        print(period, metrics)
    print("\nPAGE GROUP PERFORMANCE")
    for group, periods in sorted(pages.items()):
        for period, m in sorted(periods.items()):
            rate = 100 * m["clicks"] / m["impressions"] if m["impressions"] else 0
            print(f"{group} | {period}: {m['clicks']:,} clicks / {m['impressions']:,} impressions, {rate:.2f}% CTR")
