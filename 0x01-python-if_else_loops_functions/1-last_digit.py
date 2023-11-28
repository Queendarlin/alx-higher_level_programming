#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_no = abs(number) % 10
if number < 0:
    last_no = -last_no
print(f"Last digit of {number:d} is {last_no:d} and is ", end=" ")
if last_no > 5:
    print("greater than 5")
elif last_no == 0:
    print("0")
else:
    print("less than 6 and not 0")
