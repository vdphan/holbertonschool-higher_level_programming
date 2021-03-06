#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    m = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        for i in roman_string:
            for j in d:
                if i == j:
                    if d[j] > m:
                        n += d[j] - 2 * m
                    else:
                        n += d[j]
                    m = d[j]
        return n
    return 0
