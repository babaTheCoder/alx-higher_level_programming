#!/usr/bin/python3

"""This module returns a list of all methods and attribs in a class"""


def lookup(obj):
    """Get a list of all attribs and methods"""
    attribs = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    methods = [meth for meth in dir(obj) if callable(getattr(obj, meth))]

    return attribs + methods
