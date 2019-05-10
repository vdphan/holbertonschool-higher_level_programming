#!/usr/bin/python3
def weight_average(my_list=[]):
    i = 0
    j = 1
    s = 0
    if my_list:
        for x in my_list:
            s += x[0] * x[1]
            i += x[1]
        return s / i
    return 0
