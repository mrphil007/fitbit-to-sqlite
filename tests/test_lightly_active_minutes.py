from fitbit_to_sqlite.utils import save_lightly_active_minutes
import pathlib
import sqlite_utils
from .utils import create_zip


def test_lightly_active_minutes():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    lightly_active_minutes = [
        f.filename for f in zf.filelist if "lightly_active" in f.filename
    ]
    save_lightly_active_minutes(db, zf, lightly_active_minutes)
    lightly_active_minutes = list(sorted(db["lightly_active_minutes"].rows, key=lambda r: r["date"]))
    assert [
        {
          "date": "2018-01-01",
          "value": 266
        },
        {
          "date": "2018-01-02",
          "value": 165
        },
        {
          "date": "2018-01-03",
          "value": 160
        }
    ] == lightly_active_minutes
