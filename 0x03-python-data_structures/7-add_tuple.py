#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_tuple = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + temp_tuple
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + temp_tuple
    return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
