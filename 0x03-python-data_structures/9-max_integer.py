#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        c = my_list[0]
        for i in my_list:
            if i > c:
                c = i
        return c
    return None
