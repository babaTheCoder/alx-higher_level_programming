#!usr/bin/python

"""This module takes two values and return their sum"""


def add_integer(a, b=98):
    """Adds two values or integers

    Args:
        a (int): First value for addition
        b (int): second value

    Returns:
        value of summation of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        a = int(b)

    return (a+b)
