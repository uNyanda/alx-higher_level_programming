#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it
to stdout.
"""


def read_file(filename=""):
    """
    This module reads a file (UTF-8) and prints to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
