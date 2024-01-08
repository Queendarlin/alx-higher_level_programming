#!/usr/bin/python3
"""
Module for Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A class representing a rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
                Initializes a Rectangle instance with given width and height.

                Args:
                    width (int): Width of the rectangle.
                    height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
