#!/usr/bin/python3
"""
This module contains a function that finds a peak element in a array
of integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.

    Args:
        list_of_integers (List[int]): The input list of integers.

    Returns:
        int: The index of a peak element, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = left + (right - left) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the middle element is greater than its right neighbor,
            # search in the left half.
            right = mid
        else:
            # Otherwise, search in the right half.
            left = mid + 1

    return list_of_integers[left]
