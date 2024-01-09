#!/usr/bin/python3
"""
Module for load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """
        Creates an object from a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            obj: The deserialized object.
        """
    with open(filename, 'r', encoding='utf-8') as text_file:
        return json.loads(text_file.read())
