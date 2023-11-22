#!/usr/bin/python3
"""Square class summary
"""


class Square:
    """square constructor
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        self._Square__position = position
    """area
    """

    def area(self):
        return self._Square__size * self._Square__size

    """size getter
    """
    @property
    def size(self):
        return self._Square__size
    """size setter
    """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    """print square of sign #
    """

    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
    """position getter
    """
    @property
    def position(self):
        return self._Square__position
    """position setter
    """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 elements")

        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value
