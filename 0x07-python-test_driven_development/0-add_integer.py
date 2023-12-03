#!/usr/bin/python3


""" This is 0-add_integer doc string
It it for task 0 in alx
test driven development
project
"""


def add_integer(a, b=98):
    """return sum of 2 integers

    Args:
        a (int): first param
        b (int, optional): second param. Defaults to 98.

    Raises:
        TypeError: "a must be an integer"
        TypeError: "b must be an integer"

    Returns:
        int: sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
