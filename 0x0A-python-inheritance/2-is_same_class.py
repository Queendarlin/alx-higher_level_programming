#!/usr/bin/python3
"""
Module for returning the type of an object
"""


def is_same_class(obj, a_class):
    """
        Returns True if object is exactly an instance of the specified class;
        otherwise False.

        Args:
            obj: Object to check.
            a_class: Class to compare against.

        Returns:
            bool: True if obj is an instance of a_class;
            otherwise, False.
        """
    return type(obj) is a_class
