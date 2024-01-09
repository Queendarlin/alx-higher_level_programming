#!/usr/bin/python3
"""Module for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
       Writes an object to a text file using a JSON representation.

       Args:
           my_obj: The object to be serialized and saved.
           filename (str): Name of the file to save the JSON representation
       """
    with open(filename, 'w', encoding='utf-8') as text_file:
        text_file.write(json.dumps(my_obj))
