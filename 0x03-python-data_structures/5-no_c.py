#!/usr/bin/python3

def no_c(my_string):
    n_str = ''.join(char for char in my_string if char != 'C' and char != 'c')
    return n_str
