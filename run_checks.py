"""Check fictional February/March marketing figures using only the standard library."""
import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent

def main():
    months = defaultdict(lambda: defaultdict(float))
    path = BASE / "projects/01-campaign-performance/data/campaigns.csv"
    with path.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            for key in ("spend","impressions","clicks","conversions","revenue"):
                number = float(row[key])
                if number < 0:
                    raise ValueError(f"Negative {key}: {row}")
                months[row["month"]][key] += number
    expected = {
        "2026-02":{"spend":1800,"impressions":113000,"clicks":3560,"conversions":160,"revenue":8600},
        "2026-03":{"spend":1970,"impressions":121500,"clicks":3835,"conversions":179,"revenue":9610}
    }
    for month, metrics in expected.items():
        for key, expected_value in metrics.items():
            actual = months[month][key]
            assert actual == expected_value, f"{month} {key}: {actual} != {expected_value}"
            print(f"PASS {month} {key}: {actual:g}")
    print("All synthetic campaign checks passed.")

if __name__ == "__main__":
    main()
