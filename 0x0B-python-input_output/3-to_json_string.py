#!/usr/bin/python3

"""Module converts an object(str) to json format"""

import json
"""Module provides methods for working with json"""


def to_json_string(my_obj):
    """function converst object to json

    Args:
        my_obj (str): string to convert

    Returns:
        Json of a string
    """

    return json.dumps(my_obj)
