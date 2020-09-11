from fitbit_to_sqlite.utils import save_sleep
import pathlib
import sqlite_utils
from .utils import create_zip


def test_sleep():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    sleep = [
        f.filename for f in zf.filelist if "sleep.json" in f.filename
    ]
    save_sleep(db, zf, sleep)
    sleep = list(sorted(db["sleep"].rows, key=lambda r: r["sleep_date"]))
    assert [
        {
          "sleep_date": "2018-02-02",
          "start_time": "2018-02-01T22:36:00",
          "end_time": "2018-02-02T06:42:00",
          "minutes_asleep": 452,
          "minutes_awake": 34,
          "minutes_to_fall_asleep": 0,
          "minutes_after_wakeup": 15,
          "time_in_bed": 486,
          "efficiency": 68,
          "type": "stages",
          "wake_minutes": 34,
          "light_minutes": 209,
          "deep_minutes": 137,
          "rem_minutes": 106,
        },
        {
          "sleep_date": "2018-02-03",
          "start_time": "2018-02-02T22:27:30",
          "end_time": "2018-02-03T06:57:30",
          "minutes_asleep": 312,
          "minutes_awake": 198,
          "minutes_to_fall_asleep": 0,
          "minutes_after_wakeup": 0,
          "time_in_bed": 510,
          "efficiency": 61,
          "type": "classic",
          "wake_minutes": None,
          "light_minutes": None,
          "deep_minutes": None,
          "rem_minutes": None,
        },
    ] == sleep
