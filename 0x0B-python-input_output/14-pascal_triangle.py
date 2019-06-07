#!/usr/bin/python3
def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    l = []
    if n <= 0:
        return l
    for i in range(n):
        m = [1]
        if i > 0:
            for j in range(i):
                m.append(sum(l[-1][j:j+2]))
        l.append(m)
    return l
