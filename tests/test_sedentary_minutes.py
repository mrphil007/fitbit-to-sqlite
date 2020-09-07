from fitbit_to_sqlite.utils import save_sedentary_minutes
import pathlib
import sqlite_utils
from .utils import create_zip


def test_sedentary_minutes():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    sedentary_minutes = [
        f.filename for f in zf.filelist if "sedentary" in f.filename
    ]
    save_sedentary_minutes(db, zf, sedentary_minutes)
    sedentary_minutes = list(sorted(db["sedentary_minutes"].rows, key=lambda r: r["date"]))
    assert [
        {
          "date": "2018-01-01",
          "value": 600
        },
        {
          "date": "2018-01-02",
          "value": 728
        },
        {
          "date": "2018-01-03",
          "value": 753
        }
    ] == sedentary_minutes
