#!/usr/bin/python3

"""This module adds two numbers"""


def add_integer(a, b=98):
    """This function takes two values and return their sum

    Args:
        a (int, float): first addend
        b (int, float): second addend

    Returns:
        sum or a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
