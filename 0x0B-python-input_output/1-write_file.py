#!/usr/bin/python3

"""Module writes a string to a txt file and returns number of chars written"""


def write_file(filename="", text=""):
    total_chars = 0
    with open(filename, mode="w", encoding="utf-8") as currentfile:
        currentfile.write(text)
        total_chars = len(text)

    return total_chars
