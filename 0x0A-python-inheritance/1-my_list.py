#!/usr/bin/python3
"""
A module for MyList class
"""


class MyList(list):
    """
    A class that inherits list
    """

    def print_sorted(self):
        """
        The method to use for printing the list in sorted form
        """
        print(sorted(self))
