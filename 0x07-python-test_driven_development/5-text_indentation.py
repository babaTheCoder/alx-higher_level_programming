#!/usr/bin/python3

"""Write a function that prints 2 new lines after some characters"""


def text_indentation(text):
    """Print text with extra indent

    Args:
        text (str): Text to indent
    Returns:
        nothing, prints text with indents
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i in [".", "?", ":"]:
            i = f"{i}\n\n"
        print(i, end="")
