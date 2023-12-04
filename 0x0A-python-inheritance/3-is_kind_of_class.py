#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Checks whether an object is an instance of a class

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        True or False
    """

    return isinstance(obj, a_class)
