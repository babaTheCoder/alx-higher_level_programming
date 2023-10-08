#!/usr/bin/python3

"""
Text Indentation Module
"""


def text_indentation(text):
    """
    Text indentation function
    Args:
        text: text to indent
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        #checks if char is in ['.', '?' or ':"]
        if text[i] in (".", "?", ":"):
            if (i + 1) != len(text):
                s = text[i + 1]
                if (s != '.' and s != '?' and s != ':'):
                    print(text[i], end="\n\n")
                    if s == "":
                        i += 2
                    if s != "":
                        i += 1
        else:
            print(text[i], end="")
            i += 1
