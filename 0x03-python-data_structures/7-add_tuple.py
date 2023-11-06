#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_tuple = (0, 0)
    if tuple_a and len(tuple_a) < 2:
        tuple_a = tuple_a + temp_tuple
    elif tuple_b and len(tuple_b) < 2:
        tuple_b = tuple_b + temp_tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
