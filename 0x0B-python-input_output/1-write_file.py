#!/usr/bin/python3

"""Module writes a string to a txt file and returns number of chars written"""


def write_file(filename="", text=""):
    """Function that writes to a file

    Args:
        filename (str): the name of the file to write to
        text (str): The string to write to the file

    Returns:
        the number of characters written
    """

    total_chars = 0
    with open(filename, mode="w", encoding="utf-8") as currentfile:
        currentfile.write(text)
        total_chars = len(text)

    return total_chars
