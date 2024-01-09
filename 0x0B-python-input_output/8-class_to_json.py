#!/usr/bin/python3
"""
Module for class_to_json function
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for
    JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary description of the object for JSON serialization
    """
    return obj.__dict__
