#!/usr/bin/python3
for i in range(0, 100):
    if (i == 1 or ((i % 10) > (i / 10)) and i < 89):
        print("{:0>2d}, ".format(i), end="")
    if i == 89:
        print("{:d}".format(i))
