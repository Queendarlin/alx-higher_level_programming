#!/usr/bin/ python3
"""Function for an algorithm"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of integers.

    Returns:
    - The peak integer if found, None otherwise.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
