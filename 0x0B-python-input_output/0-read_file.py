#!/usr/bin/python3
"""
Module for read_file function
"""


def read_file(filename=""):
    """
        Reads a text file (UTF8) and prints it to stdout.

        Args:
            filename (str): The name of the file to read.
        """
    with open(filename, 'r', encoding='utf-8') as text_file:
        print(text_file.read(), end="")
