#!/usr/bin/python3
"""
A module for a function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each character: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for chars_to_newline in ".?:":
        # print(chars_to_newline, text.split(chars_to_newline))
        text = (chars_to_newline + "\n\n").join(
            [lines.strip(" ") for lines in text.split(chars_to_newline)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
