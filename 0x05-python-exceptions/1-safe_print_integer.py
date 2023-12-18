#!/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
