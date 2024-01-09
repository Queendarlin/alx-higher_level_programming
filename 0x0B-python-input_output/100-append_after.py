#!/usr/bin/python3
"""
Module for append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each lin
        containing the search string.
    """
    line_text = ""
    with open(filename) as text_file:
        for line in text_file:
            line_text += line
            if search_string in line:
                line_text += new_string
    with open(filename, "w") as text_file:
        text_file.write(line_text)
