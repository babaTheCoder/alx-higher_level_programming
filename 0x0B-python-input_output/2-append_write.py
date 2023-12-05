#!/usr/bin/python3
"""
    This module defines a function that
    opens a file and appends data to it
"""


def append_write(filename="", text=""):
    """appends a string to a given file

        Args:
            filename (FILE): filepath to append data
            text (str): String to append to string

        Returns:
            number of bytes appended
    """

    with open(filename, "a", encoding="utf-8") as f:
        write_data = f.write(text)
        return (write_data)
