from fitbit_to_sqlite.utils import save_exercise
import pathlib
import sqlite_utils
from .utils import create_zip


def test_exercise():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    exercise = [
        f.filename for f in zf.filelist if "exercise" in f.filename
    ]
    save_exercise(db, zf, exercise)
    exercise = list(sorted(db["exercise"].rows, key=lambda r: r["start_time"]))
    assert [
        {
          "date": "2018-01-01",
          "start_time": "2018-01-01T14:25:33",
          "activity_type": "Walk",
          "log_type": "auto_detected",
          "duration": 1229000,
          "average_heart_rate": 114,
          "steps": 1838,
          "sedentary_minutes": 0,
          "lightly_active_minutes": 1,
          "fairly_active_minutes": 2,
          "very_active_minutes": 18,
          "out_of_zones_minutes": 0,
          "fat_burn_minutes": 17,
          "cardio_minutes": 1,
          "peak_minutes": 0,
          "distance": None
        },
        {
          "date": "2018-01-02",
          "start_time": "2018-01-02T15:07:22",
          "activity_type": "Walk",
          "log_type": "auto_detected",
          "duration": 972000,
          "average_heart_rate": 108,
          "steps": 1376,
          "sedentary_minutes": 0,
          "lightly_active_minutes": 0,
          "fairly_active_minutes": 1,
          "very_active_minutes": 15,
          "out_of_zones_minutes": 1,
          "fat_burn_minutes": 14,
          "cardio_minutes": 1,
          "peak_minutes": 0,
          "distance": None
        },
        {
          "date": "2018-01-03",
          "start_time": "2018-01-03T18:25:35",
          "activity_type": "Run",
          "log_type": "tracker",
          "duration": 1168000,
          "average_heart_rate": 139,
          "steps": 2927,
          "sedentary_minutes": 0,
          "lightly_active_minutes": 0,
          "fairly_active_minutes": 0,
          "very_active_minutes": 20,
          "out_of_zones_minutes": 0,
          "fat_burn_minutes": 0,
          "cardio_minutes": 20,
          "peak_minutes": 0,
          "distance": 2.087447
        },
    ] == exercise
