#!/usr/bin/python3
"""
Module for from_json_string function
"""
import json


def from_json_string(my_str):
    """
        Returns an object (Python data structure) represented by a JSON string.

        Args:
            my_str (str): The JSON string to be deserialized.

        Returns:
            obj: The deserialized object.
        """
    return json.loads(my_str)
