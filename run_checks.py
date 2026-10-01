"""Check selected metrics in the synthetic marketing portfolio (Python 3 only)."""
import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent


def campaigns():
    result = defaultdict(lambda: defaultdict(float))
    with (BASE / "projects/01-campaign-performance/data/campaigns.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            for metric in ("spend", "impressions", "clicks", "conversions", "revenue"):
                value = float(row[metric])
                if value < 0:
                    raise ValueError(f"Negative value for {metric}: {row}")
                result[row["month"]][metric] += value
    expected = {
        "2026-02": {"spend": 1800, "impressions": 113000, "clicks": 3560, "conversions": 160, "revenue": 8600},
        "2026-03": {"spend": 1970, "impressions": 121500, "clicks": 3835, "conversions": 179, "revenue": 9610},
    }
    assert set(result) == set(expected), f"Unexpected campaign periods: {set(result)}"
    for month, metrics in expected.items():
        for metric, wanted in metrics.items():
            assert result[month][metric] == wanted, f"Campaign {month}: {metric}"
    print("PASS: campaign totals")


def organic_search():
    actual = defaultdict(lambda: {"impressions": 0, "clicks": 0})
    with (BASE / "projects/02-organic-search/data/search-performance.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            impressions, clicks = int(row["impressions"]), int(row["clicks"])
            assert 0 <= clicks <= impressions, f"Invalid search metrics: {row}"
            actual[row["period"]]["impressions"] += impressions
            actual[row["period"]]["clicks"] += clicks
    expected = {
        "2026-02": {"impressions": 39000, "clicks": 1650},
        "2026-03": {"impressions": 44500, "clicks": 1965},
    }
    assert dict(actual) == expected, f"Unexpected organic search metrics: {dict(actual)}"
    print("PASS: organic search totals")


def website():
    result = {}
    with (BASE / "projects/00-marketing-measurement/data/website-kpis.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            users, sessions = int(row["users"]), int(row["sessions"])
            engaged, actions = int(row["engaged_sessions"]), int(row["tracked_actions"])
            assert users > 0 and sessions > 0 and 0 <= engaged <= sessions and actions >= 0
            assert row["period"] not in result
            result[row["period"]] = (users, sessions, engaged, actions)
    assert result == {
        "February_example": (480, 620, 310, 46),
        "March_example": (515, 665, 359, 58),
    }
    print("PASS: website measurement practice data")


if __name__ == "__main__":
    website()
    campaigns()
    organic_search()
    print("All selected marketing portfolio checks passed.")
