#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
The MyList class includes a method to print a sorted version of the list.
"""


class MyList(list):
    """
    A class that inherits from list.

    Methods
    -------
    print_sorted(self)
        Prints the list in ascending order.
    """

    def __str__(self):
        return super().__str__()

    def print_sorted(self):
        """
        Prints a sorted version of the list.
        The list is sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
