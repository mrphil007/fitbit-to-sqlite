import json
import datetime
import sqlite_utils


def save_resting_heart_rates(db, zf, heart_rates):

    for filename in heart_rates:
        heart_rate = json.load(zf.open(filename))
        db["resting_heart_rate"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S").date(),
                    "value": row["value"]["value"],
                    "error": row["value"]["error"]
                }
                for row in heart_rate
            ),
            pk="date"
        )


def save_distances(db, zf, distances):

    for filename in distances:
        distance = json.load(zf.open(filename))
        db["distance"].upsert_all(
            (
                {
                    "dateTime": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S"),
                    "value": row["value"]
                }
                for row in distance
            ),
            pk="dateTime",
            columns={"dateTime": str, "value": int}
        )
