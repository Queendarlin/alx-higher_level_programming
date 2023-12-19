#!/usr/bin/python3
"""
Python file that defines a square
"""


class Square:
    """Square class with private instance attribute"""

    def __init__(self, size=0):
        """Initializes Square instance with the attribute for size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
