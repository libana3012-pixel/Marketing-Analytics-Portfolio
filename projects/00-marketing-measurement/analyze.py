"""Synthetic website measurement exercise; not an actual GA4 export."""
import csv
from pathlib import Path

with (Path(__file__).parent / "data" / "website-kpis.csv").open(newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        users = int(row["users"])
        sessions = int(row["sessions"])
        engaged = int(row["engaged_sessions"])
        actions = int(row["tracked_actions"])
        if not (users > 0 and sessions > 0 and 0 <= engaged <= sessions and actions >= 0):
            raise ValueError(f"Invalid row: {row}")
        print(f'{row["period"]}: users={users}; engagement rate={100*engaged/sessions:.2f}%; '
              f'actions per 100 sessions={100*actions/sessions:.2f}')
