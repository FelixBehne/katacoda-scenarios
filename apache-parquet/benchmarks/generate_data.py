"""Module to generate fake data."""
import datetime
import csv
import json


from faker import Faker
from numba.core.decorators import jit


# Initiate global faker instance
fake = Faker("en_US")


def generate_random_json(no_rows: int) -> dict:
    """Generates random json data.

    :param no_rows: Number of rows.
    :type no_rows: int
    :return: Fake data in a json format.
    :rtype: dict
    """
    # Instantiate faker instance
    return json.dumps(
        [
            {
                "Email Id": fake.email(),
                "Prefix": fake.prefix(),
                "Name": fake.name(),
                "Birth Date": fake.date(
                    pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)
                ),
                "Phone Number": fake.phone_number(),
                "Address": fake.address(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Country": fake.country(),
                "Year": fake.year(),
                "Time": fake.time(),
                "Link": fake.url(),
                "Text": fake.word(),
            }
            for _ in range(no_rows)
        ]
    )


def generate_random_csv(no_rows: int) -> dict:
    """Generates random csv.

    :param no_rows: Number of rows.
    :type no_rows: int
    :return: Fake data in a json format.
    :rtype: dict
    """

    # Instantiate faker instance
    return json.dumps(
        [
            {
                "Email Id": fake.email(),
                "Prefix": fake.prefix(),
                "Name": fake.name(),
                "Birth Date": fake.date(
                    pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)
                ),
                "Phone Number": fake.phone_number(),
                "Address": fake.address(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Country": fake.country(),
                "Year": fake.year(),
                "Time": fake.time(),
                "Link": fake.url(),
                "Text": fake.word(),
            }
            for _ in range(no_rows)
        ]
    )
