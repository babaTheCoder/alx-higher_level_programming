#!/usr/bin/python3

"""This module checks if an object is an instance of a given class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a class

    Args:
        obj: This is the object instance
        a_class: This is the class

    Returns:
        True if obj is an instance of a_class else False
    """

    return type(obj) is a_class
