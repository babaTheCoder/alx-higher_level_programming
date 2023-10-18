#!/usr/bin/python3

"""This module reads a file and print its content to standard output"""


def read_file(filename=""):
    """This functions reads the content of a file

    Args:
        filename (str): The name of the file to open

    Returns:
        nothing at all
    """

    with open(filename, encoding="utf-8") as currentfile:
        print(currentfile.read())
        print()
