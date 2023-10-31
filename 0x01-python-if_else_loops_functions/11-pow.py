#!/usr/bin/python3
def pow(a, b):
    value = 0
    if b < 0:
       value = 1 / pow(a, -b)
    elif b == 0:
        value = 1
    else:
        value = a * pow(a, b - 1)
    return value
