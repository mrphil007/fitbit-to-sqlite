from fitbit_to_sqlite.utils import save_very_active_minutes
import pathlib
import sqlite_utils
from .utils import create_zip


def test_very_active_minutes():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    very_active_minutes = [
        f.filename for f in zf.filelist if "very_active" in f.filename
    ]
    save_very_active_minutes(db, zf, very_active_minutes)
    very_active_minutes = list(sorted(db["very_active_minutes"].rows, key=lambda r: r["date"]))
    assert [
        {
          "date": "2018-01-01",
          "value": 33
        },
        {
          "date": "2018-01-02",
          "value": 59
        },
        {
          "date": "2018-01-03",
          "value": 42
        }
    ] == very_active_minutes
