#!/usr/bin/python3
"""A function that returns True if object is instance of a class"""


def inherits_from(obj, a_class):
    """Function checks if obj is inherited

    Args:
        obj: object to check
        a_class: Class to compare to

    Returns:
        True if obj is inherited from a_class
    """

    return issubclass(type(obj), a_class) and type(obj is not a_class
