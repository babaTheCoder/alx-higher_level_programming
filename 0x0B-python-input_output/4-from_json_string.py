#!/usr/bin/python3
"""This module deserializes a json string to an object"""
import json


def from_json_string(my_str):
    """Converts a json string to an object

        Args:
            my_str (str): Json string to convert

        Returns:
            python data structure
    """

    return json.loads(my_str)
