from fitbit_to_sqlite.utils import save_heart_rate_zones
import pathlib
import sqlite_utils
from .utils import create_zip


def test_heart_rate_zones():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    heart_rate_zones = [
        f.filename for f in zf.filelist if "heart_rate_zones" in f.filename
    ]
    save_heart_rate_zones(db, zf, heart_rate_zones)
    heart_rate_zones = list(
        sorted(db["heart_rate_zones"].rows, key=lambda r: r["date"])
    )
    assert [
        {
            "date": "2018-01-02",
            "below_zone_1": 1037,
            "in_zone_1": 154,
            "in_zone_2": 20,
            "in_zone_3": 10,
        },
        {
            "date": "2018-04-11",
            "below_zone_1": 1239,
            "in_zone_1": 115,
            "in_zone_2": 0,
            "in_zone_3": 0,
        },
    ] == heart_rate_zones
