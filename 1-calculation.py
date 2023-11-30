#!/usr/bin/python
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    add_calc = add(a, b)
    sub_calc = sub(a, b)
    mul_calc = mul(a, b)
    div_calc = div(a, b)

    print("{} + {} = {}".format(a, b, add_calc))
    print("{} - {} = {}".format(a, b, sub_calc))
    print("{} * {} = {}".format(a, b, mul_calc))
    print("{} / {} = {}".format(a, b, div_calc))
