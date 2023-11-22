#!/usr/bin/python3
"""Square class summary
"""


class Square:
    """square constructor
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
    """area
    """

    def area(self):
        return self._Square__size * self._Square__size

    """size getter
    """

    def size(self):
        return self._Square__size
    """size setter
    """

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
