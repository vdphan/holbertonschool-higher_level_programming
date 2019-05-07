#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    imax = 0
    for i in my_list:
        if i > imax:
            imax = i
    return imax
