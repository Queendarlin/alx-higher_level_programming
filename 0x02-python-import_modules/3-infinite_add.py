#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result_add = 0
    for index in sys.argv[1:]:
        result_add += int(index)

    print(result_add)
