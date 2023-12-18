#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_elements = 0
    index = 0

    try:
        while num_elements < x:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                num_elements += 1
            index += 1
        print()
        return num_elements
    except IndexError:
        pass
    print()
    return num_elements
