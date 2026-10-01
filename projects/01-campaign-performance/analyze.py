"""Aggregate an illustrative two-month marketing dataset; standard library only."""
import csv
from collections import defaultdict
from pathlib import Path

SOURCE = Path(__file__).parent / "data" / "campaigns.csv"
FIELDS = ("spend", "impressions", "clicks", "conversions", "revenue")

def run(path=SOURCE):
    by_month = defaultdict(lambda: defaultdict(float))
    by_channel = defaultdict(lambda: defaultdict(float))
    with open(path, newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            for field in FIELDS:
                value = float(row[field])
                if value < 0:
                    raise ValueError(f"Negative {field}: {row}")
                by_month[row["month"]][field] += value
                by_channel[row["channel"]][field] += value
    def report(name, values):
        spend, revenue = values["spend"], values["revenue"]
        clicks, impressions = values["clicks"], values["impressions"]
        conversions = values["conversions"]
        return {
            "name": name,
            "spend": round(spend, 2),
            "revenue": round(revenue, 2),
            "roas": round(revenue / spend, 2) if spend else None,
            "ctr_pct": round(clicks / impressions * 100, 2) if impressions else None,
            "conversion_rate_pct": round(conversions / clicks * 100, 2) if clicks else None,
            "cost_per_conversion": round(spend / conversions, 2) if conversions else None,
        }
    return [report(month, totals) for month, totals in sorted(by_month.items())], [report(channel, totals) for channel, totals in sorted(by_channel.items())]

if __name__ == "__main__":
    months, channels = run()
    print("MONTHLY PERFORMANCE")
    for item in months:
        print(item)
    print("CHANNEL PERFORMANCE")
    for item in channels:
        print(item)
