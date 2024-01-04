#!/usr/bin/python3
'''
A class to define a rectangle
'''


class Rectangle:
    '''
    Class for defining a rectangle

    Attributes:
    -width (int): The width of the rectangle.
    -height (int): The height of the rectangle.
    '''

    def __init__(self, width=0, height=0):
        '''
        Initialization of the instance of the Rectangle class

        Args:
        -width (int): The width of the rectangle initialized to 0.
        -height (int): The height of the rectangle initialized to 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter method for the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method for the width attribute

        Args:
        -value (int): The width value to set.

        Raises:
        -TypeError: The width must be an integer
        -ValueError: The width cannot be negative
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Getter method for the height attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method for the height attribute

        Args:
        -value (int): The height value to set.

        Raises:
        -TypeError: The height must be an integer
        -ValueError: The height cannot be negative
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
