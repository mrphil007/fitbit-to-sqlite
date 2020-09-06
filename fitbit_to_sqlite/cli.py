import click
import json
import zipfile
import sqlite_utils
from . import utils


@click.group()
@click.version_option()
def cli():
    "Save FitBit data to a SQLite database"


@cli.command(name="resting-heart-rate")
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "zip_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
def resting_heart_rate(db_path, zip_path):
    "Save resting heart rate data from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find all the relevant resting heart rate files
    heart_rates = [
        f.filename for f in zf.filelist if "resting_heart_rate" in f.filename
    ]
    with click.progressbar(heart_rates, label="Loading resting heart rate data") as bar:
        utils.save_resting_heart_rates(db, zf, bar)


@cli.command(name="distance")
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "zip_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
def resting_heart_rate(db_path, zip_path):
    "Save Distance data from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find all the relevant distance files
    distances = [
        f.filename for f in zf.filelist if "distance-2019" in f.filename
    ]
    with click.progressbar(distances, label="Loading distance data") as bar:
        utils.save_distances(db, zf, bar)
