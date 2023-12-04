#!/usr/bin/python3

def lookup(obj):
    """Lists available attribs and methods in an object

    Args:
        obj (obj): obj to fine attrib and methods

    Returns:
        list of attribs and methods
    """
    return dir(obj)
