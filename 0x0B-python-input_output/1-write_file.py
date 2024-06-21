#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename: the name of the file to write to.
        text: the text to write into the file.

    Returns:
        the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
