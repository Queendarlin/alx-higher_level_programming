#!/usr/bin/python3
"""Module for returning instance of an object"""


def is_kind_of_class(obj, a_class):
    """
        Function Returns True if the object is an instance of,
        or if the object is an instance of a class that inherited
        otherwise, False.

        Args:
            obj: Object to check.
            a_class: Class to compare against.

        Returns:
            True if obj is an instance of a_class or its subclass;
            otherwise, False.
        """
    return isinstance(obj, a_class)
