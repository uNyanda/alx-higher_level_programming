#!/usr/bin/python3
"""
This module contains a function that appendds a string at the end of a textfle
(UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename: the name of the file.
        text: the text to append to the file.

    Returns:
        the number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        content = file.write(text)
        return content
