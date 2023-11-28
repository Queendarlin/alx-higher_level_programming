#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        last_no = (-number % 10)
    elif number >= 0:
        last_no = number % 10
    print("f{num:d}", end="")
    return last_no
