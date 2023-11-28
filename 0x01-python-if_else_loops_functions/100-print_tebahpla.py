#!/usr/bin/python3
for number in range(122, 96, -1):
    print("{:c}".format(number if number % 2 == 0 else number - 32), end="")
