#!/usr/bin/python3

"""Converts JSON object to corresponding Data Structure"""

import json
"""Provides methods for working on JSON data"""


def from_json_string(my_str):
    """Converst a JSON file to other data structure

    Args:
        my_str (str): JSON object fo convert

    Returns:
        a corresponding data structure object
    """

    return json.loads(my_str)
