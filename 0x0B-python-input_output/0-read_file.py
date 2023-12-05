#!/usr/bin/python3
"""
    This module reads a text file and prints its content
"""


def read_file(filename=""):
    """This function reads the content of a file

        Args:
            filename: the path to the file to read

        Returns:
            nothing
    """

    with open(filename, encoding="utf-8") as f:
       # data = f.read()
       # print(data)
       print(f.read())
