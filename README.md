# fitbit-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/fitbit-to-sqlite.svg)](https://pypi.org/project/fitbit-to-sqlite/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mrphil007/fitbit-to-sqlite/blob/master/LICENSE)

Save data from Fitbit Takeout to an SQLite database.

## How to install

    $ pip install fitbit-to-sqlite

Request your Fitbit data from the `Export Your Account Archive` section on this page https://www.fitbit.com/settings/data/export - wait for the email and download the zip file.

This tool only supports a subset of the available data sources. More will be added over time.

## Resting Heart Rate

You can import data on your resting heart rate over time by using this command:

    $ fitbit-to-sqlite resting-heart-rate fitbit.db MyFitbitData.zip

This will create a database file called `fitbit.db` if one does not already exist.

## Distance

You can import data on the distance you have travelled each minute of each day by using the following command. Note that this also creates an analysis view called `distance_v` which converts the distances to km and miles.

    $ fitbit-to-sqlite distance fitbit.db MyFitbitData.zip

## Minutes Active

You can import data on your activity minutes, which Fitbit classifies into `Sedentary`, `Lightly Active`, `Moderately Active` and `Very Active` using the following command. Note that this creates separate database tables for each, but they are also combined together into a view for analysis called `minutes_active_v`.

    $ fitbit-to-sqlite minutes-active fitbit.db MyFitbitData.zip

## Exercise

You can import data on your exercise activities using the following command. Note that this imports a subset of all fields.

    $ fitbit-to-sqlite exercise fitbit.db MyFitbitData.zip

## Sleep

You can import sleep log data using the following command. Note that some fields are only populated for sleep captured in `stages`. A second table called `sleep_scores` is also created which includes the scores (out of 100) which Fitbit have started generating.

    $ fitbit-to-sqlite sleep fitbit.db MyFitbitData.zip

## Heart Rate Zones

You can import data on the time you have spent across the four heart rate zones which Fitbit defines based on your maximum heart rate. In the app these are usually referred to as "Below Zones", "Fat Burn", "Cardio" and "Peak" but here they are imported as `below_zone_1`, `in_zone_1`, `in_zone_2` and `in_zone_3`.

    $ fitbit-to-sqlite heart-rate-zones fitbit.db MyFitbitData.zip

## Browsing your data with Datasette

Once you have imported Fitbit data into an SQLite database file you can browse your data using [Datasette](https://github.com/simonw/datasette). Install Datasette like so:

    $ pip install datasette

Now browse your data by running this and then visiting `http://localhost:8001/`

    $ datasette fitbit.db

## Thanks

This package is heavily inspired by the interesting work on [Personal Analytics](https://simonwillison.net/2019/Oct/7/dogsheep/) which Simon
Willison has been doing [here](https://dogsheep.github.io/).
