#!/usr/bin/python3
"""
Module for Square class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       A class representing a square that inherits Rectangle.
    """
    def __init__(self, size):
        """
                Initializes a Square instance with the given size.

                Args:
                    size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
