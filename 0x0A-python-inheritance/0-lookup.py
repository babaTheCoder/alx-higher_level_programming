#!/usr/bin/python3
"""
Return list of available attr of objects
"""

def lookup(obj):
    """Lists available attribs and methods in an object

    Args:
        obj (obj): obj to fine attrib and methods

    Returns:
        list of attribs and methods
    """
    return dir(obj)
