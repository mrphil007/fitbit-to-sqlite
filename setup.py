from setuptools import setup
import os

VERSION = "0.3"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="fitbit-to-sqlite",
    description="Save data from Fitbit Takeout to an SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Phil Rossiter",
    url="https://github.com/mrphil007/fitbit-to-sqlite",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["fitbit_to_sqlite"],
    entry_points="""
        [console_scripts]
        fitbit-to-sqlite=fitbit_to_sqlite.cli:cli
    """,
    install_requires=["sqlite-utils>=2.7.2", "click"],
    extras_require={"test": ["pytest"]},
    tests_require=["fitbit-to-sqlite[test]"],
)
