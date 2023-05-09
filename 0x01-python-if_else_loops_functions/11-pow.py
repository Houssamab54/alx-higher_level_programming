#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
    for i in range(abs(b)):
        result *= a
    return result
