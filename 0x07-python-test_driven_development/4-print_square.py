#!/usr/bin/python3
"""
4-print_square
"""
def print_square(size):
    """_summary_

    Args:
        size (_type_): _description_
    """
    if (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if (type(size) != int and type(size) != float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        for column in range(0, size):
            print("#", end=" ")
    print()
