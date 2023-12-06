#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_keys = [key for key, values in a_dictionary.items() if values == value]
    for key in del_keys:
        del a_dictionary[key]
    return a_dictionary
