# fitbit-to-sqlite

Save data from FitBit Takeout to an SQLite database.

## How to install

    $ pip install fitbit-to-sqlite

Request your Fitbit data from the `Export Your Account Archive`  section from this page https://www.fitbit.com/settings/data/export - wait for the email and download the zip file.

This tool only supports a subset of the available options. More will be added over time.

## Resting Heart Rate

You can import data on your resting heart rate over time by using this command:

    $ fitbit-to-sqlite resting-heart-rate fitbit.db MyFitbitData.zip

This will create a database file called `fitbit.db` if one does not already exist.

## Distance

You can import data on the distance you have travelled each minute of each day by using this command:

    $ fitbit-to-sqlite distance fitbit.db MyFitbitData.zip

## Browsing your data with Datasette

Once you have imported Fitbit data into a SQLite database file you can browse your data using [Datasette](https://github.com/simonw/datasette). Install Datasette like so:

    $ pip install datasette

Now browse your data by running this and then visiting `http://localhost:8001/`

    $ datasette fitbit.db

