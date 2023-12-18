#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        funct_result = fct(*args)
        return funct_result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
