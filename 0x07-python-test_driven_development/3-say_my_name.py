#!/usr/bin/python3

"""Prints out a person's full name"""


def say_my_name(first_name, last_name=""):
    """Prints out fullnames
    Args:
        first_name: first name of the person
        last_name: last name of the person
    Raises:
        TypeError: if 'first_name' or 'last_name' not string
    Returns:
        nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f'My name is {first_name} {last_name}')
