#!/usr/bin/python3

def is_same_class(obj, a_class):
    """checks if an object is an instance of a class

    Args:
        obj: object to check
        a_class: class to check

    Returns:
        True or False
    """
    return type(obj) ==  a_class
