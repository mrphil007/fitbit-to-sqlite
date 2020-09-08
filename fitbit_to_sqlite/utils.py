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


def save_exercise(db, zf, exercise):
    for filename in exercise:
        exercise = json.load(zf.open(filename))
        db["exercise"].upsert_all(
            (
                {
                    "date": datetime.datetime.strptime(row["startTime"], "%m/%d/%y %H:%M:%S").date(),
                    "start_time": datetime.datetime.strptime(row["startTime"], "%m/%d/%y %H:%M:%S"),
                    "activity_type": row["activityName"],
                    "log_type": row["logType"],
                    "duration": row["activeDuration"],
                    "average_heart_rate": row["averageHeartRate"] if "averageHeartRate" in row else None,
                    "steps": row["steps"] if "steps" in row else None,
                    "sedentary_minutes": row["activityLevel"][0]["minutes"],
                    "lightly_active_minutes": row["activityLevel"][1]["minutes"],
                    "fairly_active_minutes": row["activityLevel"][2]["minutes"],
                    "very_active_minutes": row["activityLevel"][3]["minutes"],
                    "out_of_zones_minutes": row["heartRateZones"][0]["minutes"] if "heartRateZones" in row else None,
                    "fat_burn_minutes": row["heartRateZones"][1]["minutes"] if "heartRateZones" in row else None,
                    "cardio_minutes": row["heartRateZones"][2]["minutes"] if "heartRateZones" in row else None,
                    "peak_minutes": row["heartRateZones"][3]["minutes"] if "heartRateZones" in row else None,
                    "distance": row["distance"] if "distance" in row else None
                }
                for row in exercise
            ),
            pk="start_time"
        )


def save_sleep(db, zf, sleep):
    for filename in sleep:
        sleep = json.load(zf.open(filename))
        db["sleep"].upsert_all(
            (
                {
                    "sleep_date": datetime.datetime.strptime(row["dateOfSleep"], "%Y-%m-%d").date(),
                    "start_time": datetime.datetime.strptime(row["startTime"], "%Y-%m-%dT%H:%M:%S.%f"),
                    "end_time": datetime.datetime.strptime(row["endTime"], "%Y-%m-%dT%H:%M:%S.%f"),
                    "minutes_asleep": row["minutesAsleep"],
                    "minutes_awake": row["minutesAwake"],
                    "minutes_to_fall_asleep": row["minutesToFallAsleep"],
                    "minutes_after_wakeup": row["minutesAfterWakeup"],
                    "time_in_bed": row["timeInBed"],
                    "efficiency": row["efficiency"],
                    "type": row["type"],
                    "wake_minutes": row["levels"]["summary"]["wake"]["minutes"] if row["type"] == "stages" else None,
                    "light_minutes": row["levels"]["summary"]["light"]["minutes"] if row["type"] == "stages" else None,
                    "deep_minutes": row["levels"]["summary"]["deep"]["minutes"] if row["type"] == "stages" else None,
                    "rem_minutes": row["levels"]["summary"]["rem"]["minutes"] if row["type"] == "stages" else None
                }
                for row in sleep
            ),
            pk="sleep_date"
        )


def create_views(db):
    for name, sql in (
        (
            "distance_v",
            """
SELECT
    d.dateTime               AS date_time,
    DATE(d.dateTime)         AS date,
    -- Distance is in cm, convert to km
    CAST(d.value AS FLOAT)/100000 AS distance_km,
    -- Approximate conversation of km to m
    CAST(d.value AS FLOAT)/100000/1.609344  AS distance_miles
FROM
    distance d
            """,

        ),
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
