import pathlib
from .utils import create_zip


def test_create_zip():
    zf = create_zip()
    assert {
        "resting_heart_rate.json",
        "distance.json"
    } == {f.filename for f in zf.filelist}
