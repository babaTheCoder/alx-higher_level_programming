#!/usr/bin/python3

"""This mode converts a JSON file to a data object"""

import json
"""Provides methods for working with JSON data"""


def load_from_json_file(filename):
    """Converts JSON to a data object

    Args:
        filename (str): name fo json file to convert

    Returns:
        a new data object
    """

    with open(filename, mode="r", encoding="utf-8") as currentfile:
        return (json.load(currentfile))
