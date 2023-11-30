#!/usr/bin/python3
import sys
if __name__ == "__main__":

    len_arg = len(sys.argv)

    print(f"{len_arg - 1} {'argument' if len_arg == 2 else 'arguments'}:")

    for index in range(1, len_arg):
        print("{0}: {1}".format(index, sys.argv[index]))
