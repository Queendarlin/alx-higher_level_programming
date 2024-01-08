#!/usr/bin/python3
"""
Module for add_attribute
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception with the message "can't add new attribute"
    if the object can't have a new attribute.

    Args:
        obj: Object to which the new attribute will be added.
        attribute: Name of the new attribute.
        value: Value of the new attribute.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
