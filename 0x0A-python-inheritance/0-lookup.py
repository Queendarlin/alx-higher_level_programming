#!/usr/bin/python3
"""
A module for a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Function that returns the list of attributes and methods an object has

    :param obj: The object

    :return: A list object
    """
    return dir(obj)
