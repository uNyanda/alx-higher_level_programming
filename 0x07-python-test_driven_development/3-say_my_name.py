#!/usr/bin/python3

"""
This module defines a function that prints
a formatted string of a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string of a person's name.

    Args:
        first_name (str): The first name.
        second_name (str, optional): The second name.
        Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name
        is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "" and last_name == "":
        print("My name is")
    elif last_name == "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
