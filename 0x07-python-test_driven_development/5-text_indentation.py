#!/usr/bin/python3

"""
This module implements a function that indents a
text after certain characters.

Functions:
    text_indentation(text: str) -> None
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of
    these characters: '.', '?', ':'.

    Arguments:
    text : str
        The text to be indented. Must be a string,
        otherwise a TypeError is raised.

    Returns:
    None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    for char in characters:
        text = text.replace(char, char + '\n\n')

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    text = '\n'.join(lines)
    text = text.rstrip('\n')  # Remove trailing newline characters
    print(text)
