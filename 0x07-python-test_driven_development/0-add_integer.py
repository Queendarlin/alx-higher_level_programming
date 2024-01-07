#!/usr/bin/python3
"""
A module for a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    The function that adds two numbers

    Args:
        a: (int or float) the first number
        b: (int of float) the second number

    Return: The addition of a and b (int)

    Raises:
        TypeError: If a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
