#!/usr/bin/python3

"""Opens and appends text to a file"""


def append_write(filename="", text=""):
    """Appends text to a file [Creates file if doesn't exist]

    Args:
        filename (str): name of the file
        text (str): text or string to append to file

    Returns:
        the number of chars appended
    """

    with open(filename, mode="a", encoding="utf-8") as currentfile:
        currentfile.write(text)

    return len(text)
