#!/usr/bin/python3
"""This module returns the list of avaliable attributes and methods of
an object"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
