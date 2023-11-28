#!/usr/bin/python3
for tens_num in range(9):
    for ones_num in range(tens_num + 1, 10):
        if tens_num * 10 + ones_num < 89:
            print("{:d}{:d}".format(tens_num, ones_num), end=", ")
print("{:d}".format(89))
