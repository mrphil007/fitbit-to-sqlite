from fitbit_to_sqlite.utils import save_distances
import pathlib
import sqlite_utils
from .utils import create_zip


def test_distances():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    distances = [
        f.filename for f in zf.filelist if "distance" in f.filename
    ]
    save_distances(db, zf, distances)
    distances = list(sorted(db["distance"].rows, key=lambda r: r["dateTime"]))
    assert [
        {
          "dateTime": "2017-12-31T16:42:00",
          "value": 4110
        },
        {
          "dateTime": "2017-12-31T16:43:00",
          "value": 4340
        },
        {
          "dateTime": "2017-12-31T16:44:00",
          "value": 3490
        },
        {
          "dateTime": "2017-12-31T16:45:00",
          "value": 850
        },
        {
          "dateTime": "2017-12-31T16:46:00",
          "value": 0
        }
    ] == distances
