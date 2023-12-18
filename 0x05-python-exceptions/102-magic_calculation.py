#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
        except Exception:
            result += (a ** b) / i
        else:
            result += b + a

    return result
