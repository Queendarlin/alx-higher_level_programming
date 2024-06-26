#!/usr/bin/python3
"""
A script that adds all arguments to a Python list, and then save them to a file
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        the_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        the_items = []
    the_items.extend(sys.argv[1:])
    save_to_json_file(the_items, "add_item.json")
