#!/usr/bin/python3
"""
    This module defines a function
    that writes a given string to a file
"""


def write_file(filename="", text=""):
    """Writes a string to a given file

        Args:
            filename: path to file
            text (str): string to write to file

        Returns:
            nothing
    """

    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
