#!/usr/bin/python3
"""
This is 8-rectangle
doc
task
number 8
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""_summary_

Returns:
    _type_: _description_
"""


class Rectangle(BaseGeometry):
    """
    Rectangle
    sub Class
    doc

    """

    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        return this rectangle w and h
        stringfied version
        in a certain format
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __repr__(self):
        """__repr__
        this is to return
        str version of the rectangle
        """
        return self.__str__()

    def area(self):
        """area
        this is to calculate th rectangel
        area using its specifc equation
        Returns:
            _type_: _description_
        """
        return self.__width * self.__height
