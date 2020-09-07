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
        f.filename for f in zf.filelist if "distance-2020" in f.filename
    ]
    with click.progressbar(distances, label="Loading distance data") as bar:
        utils.save_distances(db, zf, bar)


@cli.command(name="minutes-active")
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
def minutes_active(db_path, zip_path):
    "Save data on minutes active from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find relevant sedentary minutes files
    sedentary_minutes = [
        f.filename for f in zf.filelist if "sedentary" in f.filename
    ]
    with click.progressbar(sedentary_minutes, label="Loading sedentary minutes data") as bar:
        utils.save_sedentary_minutes(db, zf, bar)
    # Find relevant lightly active minutes files
    lightly_active_minutes = [
        f.filename for f in zf.filelist if "lightly_active" in f.filename
    ]
    with click.progressbar(lightly_active_minutes, label="Loading lightly active minutes data") as bar:
        utils.save_lightly_active_minutes(db, zf, bar)
    # Find relevant moderately active minutes files
    moderately_active_minutes = [
        f.filename for f in zf.filelist if "moderately_active" in f.filename
    ]
    with click.progressbar(moderately_active_minutes, label="Loading moderately active minutes data") as bar:
        utils.save_moderately_active_minutes(db, zf, bar)
    # Find relevant very active minutes files
    very_active_minutes = [
        f.filename for f in zf.filelist if "very_active" in f.filename
    ]
    with click.progressbar(very_active_minutes, label="Loading very active minutes data") as bar:
        utils.save_very_active_minutes(db, zf, bar)
    # Create analysis view
    utils.create_views(db)
