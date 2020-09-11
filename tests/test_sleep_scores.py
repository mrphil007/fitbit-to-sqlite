from fitbit_to_sqlite.utils import save_sleep_scores
import pathlib
import sqlite_utils
from .utils import create_zip


def test_sleep_scores():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    sleep_scores = [
        f.filename for f in zf.filelist if "sleep_score.csv" in f.filename
    ]
    save_sleep_scores(db, zf, sleep_scores)
    sleep_scores = list(sorted(db["sleep_scores"].rows, key=lambda r: r["sleep_date"]))
    assert [
        {
          "sleep_date": "2019-08-22",
          "overall_score": 82,
          "composition_score": 21,
          "revitalization_score": 22,
          "duration_score": 39,
          "deep_sleep_minutes": 71,
          "resting_heart_rate": 56,
          "restlessness": 0.082497213
        },
        {
          "sleep_date": "2019-08-29",
          "overall_score": 75,
          "composition_score": 18,
          "revitalization_score": 20,
          "duration_score": 37,
          "deep_sleep_minutes": 77,
          "resting_heart_rate": 59,
          "restlessness": 0.070093458
        },
    ] == sleep_scores
