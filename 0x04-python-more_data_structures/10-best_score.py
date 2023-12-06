#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        biggest_int_value = max(a_dictionary, key=a_dictionary.get)
        return biggest_int_value
    else:
        return None
