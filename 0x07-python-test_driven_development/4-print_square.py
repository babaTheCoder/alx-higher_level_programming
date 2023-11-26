#!/usr/bin/python3

"""This module prints a square with # based off of a given size"""


def print_square(size):
    """Prints a square with given size

    Args:
        size (int): dimensions of square

    Returns:
        nothing, just prints a square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    row = "#" * size

    for i in range(size):
        print(row)
