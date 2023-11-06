#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_tuple = (0, 0)
    if len(tuple_a) == 0:
        tuple_a = tuple_a + temp_tuple
    elif len(tuple_a) < 2 and len(tuple_a) > 0:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) == 0:
        tuple_b = tuple_b + temp_tuple
    elif len(tuple_b) < 2 and len(tuple_b) > 0:
        tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
