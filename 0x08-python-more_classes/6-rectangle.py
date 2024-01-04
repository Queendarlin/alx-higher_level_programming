#!/usr/bin/python3
"""
Class to define a rectangle
"""


class Rectangle:
    """
    Class for a rectangle.

    Attribute:
    -__width (int): The width of the rectangle
    -__height (int): The height of the rectangle
    -number_of_instances (int): Class attribute to track number of instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialization of the instance of the Rectangle class

        Args:
        -width (int): The width of the rectangle initialized to 0.
        -height (int): The height of the rectangle initialized to 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute

        Args:
        -value (int): The width value to set.

        Raises:
        -TypeError: The width must be an integer
        -ValueError: The width cannot be negative
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute

        Args:
        -value (int): The height value to set.

        Raises:
        -TypeError: The height must be an integer
        -ValueError: The height cannot be negative
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        For calculating the area of the rectangle.

        :return:
        -int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        For calculating the perimeter of the rectangle.

        :return:
        -int: The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns unofficial string representation of the rectangle for end user

        :return:
        -str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        print_str = ''
        for index in range(self.__height):
            for index2 in range(self.__width):
                print_str += '#'
            print_str += '\n'
        return print_str[:-1]

    def __repr__(self):
        """
        Returns official string representation of the rectangle for developer

        :return:
        -str: The string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
