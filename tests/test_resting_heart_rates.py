from fitbit_to_sqlite.utils import save_resting_heart_rates
import pathlib
import sqlite_utils
from .utils import create_zip


def test_resting_heart_rate():
    zf = create_zip()
    db = sqlite_utils.Database(memory=True)
    heart_rates = [
        f.filename for f in zf.filelist if "resting_heart_rate" in f.filename
    ]
    save_resting_heart_rates(db, zf, heart_rates)
    heart_rates = list(sorted(db["resting_heart_rate"].rows, key=lambda r: r["date"]))
    assert [
        {
            "date": "2018-12-30",
            "value": 59.420772552490234,
            "error": 6.787134170532227
        },
        {
            "date": "2018-12-31",
            "value": 58.29636573791504,
            "error": 6.787102699279785
        },
    ] == heart_rates
