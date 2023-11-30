#!/usr/bin/python3
import sys
if __name__ == "__main__":

    len_arg = len(sys.argv)

    if len_arg == 1:
        print("{} arguments.".format(len_arg - 1))
    elif len_arg == 2:
        print("{} argument:".format(len_arg - 1))
    else:
        print("{} arguments:".format(len_arg - 1))

    for index in range(1, len_arg):
        print("{0}: {1}".format(index, sys.argv[index]))
