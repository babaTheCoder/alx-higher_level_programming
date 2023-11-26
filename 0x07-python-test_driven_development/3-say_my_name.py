#!/usr/bin/python3

"""This module prints out a user name"""


def say_my_name(first_name, last_name=""):
    """Prints out name

    Args:
        first_name (str): first name to print
        last_name (str): last name of person

    Return:
        nothing, prints out full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
