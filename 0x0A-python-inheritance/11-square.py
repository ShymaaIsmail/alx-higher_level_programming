#!/usr/bin/python3
"""
This is 10-square
doc
task
number 10
"""

Rectangle = __import__('9-rectangle').Rectangle

"""_summary_

Returns:
    _type_: _description_
"""


class Square(Rectangle):
    """
    Square
    sub Class
    doc

    """

    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _description_
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area
        this is to calculate th square
        area using its specifc equation
        Returns:
            _type_: _description_
        """
        return self.__size * self.__size

    def __str__(self):
        """
        return this square w and h
        stringfied version
        in a certain format
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def __repr__(self):
        """__repr__
        this is to return
        str version of the square
        """
        return self.__str__()
