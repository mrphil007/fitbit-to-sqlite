import pathlib
from .utils import create_zip


def test_create_zip():
    zf = create_zip()
    assert {
        "resting_heart_rate.json",
        "distance.json",
        "sedentary_minutes.json",
        "lightly_active_minutes.json",
        "moderately_active_minutes.json",
        "very_active_minutes.json",
        "exercise.json",
    } == {f.filename for f in zf.filelist}
