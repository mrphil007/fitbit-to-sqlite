import click
import json
import zipfile
import sqlite_utils
from . import utils


@click.group()
@click.version_option()
def cli():
    "Save Fitbit data to a SQLite database"


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
def distance(db_path, zip_path):
    "Save Distance data from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find all the relevant distance files
    distances = [f.filename for f in zf.filelist if "distance" in f.filename]
    with click.progressbar(distances, label="Loading distance data") as bar:
        utils.save_distances(db, zf, bar)
    # Add view on distance data
    utils.create_views(db)


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
    sedentary_minutes = [f.filename for f in zf.filelist if "sedentary" in f.filename]
    with click.progressbar(
        sedentary_minutes, label="Loading sedentary minutes data"
    ) as bar:
        utils.save_sedentary_minutes(db, zf, bar)
    # Find relevant lightly active minutes files
    lightly_active_minutes = [
        f.filename for f in zf.filelist if "lightly_active" in f.filename
    ]
    with click.progressbar(
        lightly_active_minutes, label="Loading lightly active minutes data"
    ) as bar:
        utils.save_lightly_active_minutes(db, zf, bar)
    # Find relevant moderately active minutes files
    moderately_active_minutes = [
        f.filename for f in zf.filelist if "moderately_active" in f.filename
    ]
    with click.progressbar(
        moderately_active_minutes, label="Loading moderately active minutes data"
    ) as bar:
        utils.save_moderately_active_minutes(db, zf, bar)
    # Find relevant very active minutes files
    very_active_minutes = [
        f.filename for f in zf.filelist if "very_active" in f.filename
    ]
    with click.progressbar(
        very_active_minutes, label="Loading very active minutes data"
    ) as bar:
        utils.save_very_active_minutes(db, zf, bar)
    # Create analysis view
    utils.create_views(db)


@cli.command(name="exercise")
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
def exercise(db_path, zip_path):
    "Save data on Exercise activities from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find relevant exercise files
    exercise = [f.filename for f in zf.filelist if "exercise" in f.filename]
    with click.progressbar(exercise, label="Loading exercise data") as bar:
        utils.save_exercise(db, zf, bar)


@cli.command(name="sleep")
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
def sleep(db_path, zip_path):
    "Save data on Sleep from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find relevant sleep files
    sleep = [f.filename for f in zf.filelist if "sleep-" in f.filename]
    with click.progressbar(sleep, label="Loading sleep data") as bar:
        utils.save_sleep(db, zf, bar)
    # Also save the sleep scores which are in a separate CSV
    sleep_scores = [f.filename for f in zf.filelist if "sleep_score.csv" in f.filename]
    utils.save_sleep_scores(db, zf, sleep_scores)


@cli.command(name="heart-rate-zones")
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
def heart_rate_zones(db_path, zip_path):
    "Save data on Time in Heart Rate Zones from Takeout zip to SQLite"
    db = sqlite_utils.Database(db_path)
    zf = zipfile.ZipFile(zip_path)
    # Find relevant heart rate zones files
    heart_rate_zones = [
        f.filename for f in zf.filelist if "heart_rate_zones" in f.filename
    ]
    with click.progressbar(
        heart_rate_zones, label="Loading heart rate zones data"
    ) as bar:
        utils.save_heart_rate_zones(db, zf, bar)
