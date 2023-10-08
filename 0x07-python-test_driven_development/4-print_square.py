#!/usr/bin/python

"""Prints a square using '#' character"""


def print_square(size):
    """print out a square of give size
    Args:
        size: dimensions of the square
    Raises:
        ValueError: if size < 0: 'size must be >= 0'
        TypeError: if size is not int, 'size must be int'
        TypeError: if size is float, 'size must be an int'
    Return:
        nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    else:
        print(('#'*size + '\n')*size)
