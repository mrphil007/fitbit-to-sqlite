from fitbit_to_sqlite.utils import save_moderately_active_minutes
import pathlib
import sqlite_utils
from .utils import create_zip


def test_moderately_active_minutes():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    moderately_active_minutes = [
        f.filename for f in zf.filelist if "moderately_active" in f.filename
    ]
    save_moderately_active_minutes(db, zf, moderately_active_minutes)
    moderately_active_minutes = list(sorted(db["moderately_active_minutes"].rows, key=lambda r: r["date"]))
    assert [
        {
          "date": "2018-01-01",
          "value": 22
        },
        {
          "date": "2018-01-02",
          "value": 17
        },
        {
          "date": "2018-01-03",
          "value": 13
        }
    ] == moderately_active_minutes
