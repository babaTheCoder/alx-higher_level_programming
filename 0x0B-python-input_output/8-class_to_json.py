#!/usr/bin/python3

"""Module serializes an obj into a dictionary"""


def class_to_json(obj):
    """Serializes an object to a dictionary data structure

    Args:
        obj (object): instance of a class to serialize

    Returns:
        a dictionary
    """

    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

        return result
