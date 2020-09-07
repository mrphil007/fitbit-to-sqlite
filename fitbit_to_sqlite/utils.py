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


def save_sedentary_minutes(db, zf, sedentary_minutes):
    for filename in sedentary_minutes:
        sedentary_minutes = json.load(zf.open(filename))
        db["sedentary_minutes"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S").date(),
                    "value": row["value"]
                }
                for row in sedentary_minutes
            ),
            pk="date",
            columns={"date": str, "value": int}
        )


def save_lightly_active_minutes(db, zf, lightly_active_minutes):
    for filename in lightly_active_minutes:
        lightly_active_minutes = json.load(zf.open(filename))
        db["lightly_active_minutes"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S").date(),
                    "value": row["value"]
                }
                for row in lightly_active_minutes
            ),
            pk="date",
            columns={"date": str, "value": int}
        )


def save_moderately_active_minutes(db, zf, moderately_active_minutes):
    for filename in moderately_active_minutes:
        moderately_active_minutes = json.load(zf.open(filename))
        db["moderately_active_minutes"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S").date(),
                    "value": row["value"]
                }
                for row in moderately_active_minutes
            ),
            pk="date",
            columns={"date": str, "value": int}
        )


def save_very_active_minutes(db, zf, very_active_minutes):
    for filename in very_active_minutes:
        very_active_minutes = json.load(zf.open(filename))
        db["very_active_minutes"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["dateTime"], "%m/%d/%y %H:%M:%S").date(),
                    "value": row["value"]
                }
                for row in very_active_minutes
            ),
            pk="date",
            columns={"date": str, "value": int}
        )


def create_views(db):
    for name, sql in (
        (
            "minutes_active_v",
            """
SELECT
    'sendentary'  AS minutes_type,
    d.*
FROM
    sedentary_minutes d
UNION ALL
SELECT
    'lightly_active'  AS minutes_type,
    d.*
FROM
    lightly_active_minutes d
UNION ALL
SELECT
    'moderately_active'  AS minutes_type,
    d.*
FROM
    moderately_active_minutes d
UNION ALL
SELECT
    'very_active'  AS minutes_type,
    d.*
FROM
    very_active_minutes d
        """,
        ),
    ):
        try:
            db.create_view(name, sql)
        except Exception:
            pass
