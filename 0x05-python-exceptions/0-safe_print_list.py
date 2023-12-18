#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        num_elements = 0
        for index in range(x):
            print(my_list[index], end="")
            num_elements += 1
        print()
        return num_elements

    except IndexError:
        print()
    return num_elements
