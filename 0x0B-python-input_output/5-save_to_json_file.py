#!/usr/bin/python3

"""This module saves an object to json file"""

import json
"""Provides methods for working on JSON objects"""


def save_to_json_file(my_obj, filename):
    """Saves given object to a json file

    Args:
        my_obj (obj): object to save in json file
        filename (str): name of JSON file

    Returns:
        nothing
    """

    with open(filename, mode="w", encoding="utf-8") as currentfile:
        currentfile.write(json.dumps(my_obj))
