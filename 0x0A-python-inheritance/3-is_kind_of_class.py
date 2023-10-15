#!/usr/bin/python3
"""This module checks if an object is same kind as a given class"""


def is_kind_of_class(obj, a_class):
    """Checks using issinstance

    Args:
        obj: object to check
        a_class: Class to check against

    Returns:
        True if obj is isinstance of a_class or False
    """

    return isinstance(obj, a_class)
