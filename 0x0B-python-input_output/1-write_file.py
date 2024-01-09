#!/usr/bin/python3
"""
A module for write_file function
"""


def write_file(filename="", text=""):
    """
        Function that writes a string to a text file (UTF8) and
        returns the number of characters written.

        Args:
            filename (str): The name of the file to write.
            text (str): The string to write to the file.

        Returns:
            int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as text_file:
        return text_file.write(text)
