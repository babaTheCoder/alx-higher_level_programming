#!/usr/bin/python3
"""
    This module serializes an object to json
"""
import json


def to_json_string(my_obj):
    """Converts an object to json

        Args:
            my_obj (obj): object to serialize
    """

    return json.dumps(my_obj)
