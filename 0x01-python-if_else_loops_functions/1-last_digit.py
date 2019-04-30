#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0:
    digit = (10 - digit) * (-1)
if digit > 5:
    print("Last digit of {:d} is {:d} \
and is greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, digit))
elif digit < 6 and digit != 0:
    print("Last digit of {:d} is {:d} \
and is less than 6 and not 0".format(number, digit))
