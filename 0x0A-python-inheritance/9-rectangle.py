#!/usr/bin/python3
"""
This is 8-rectangle
doc
task
number 8
"""


class BaseGeometry:
    """
    BaseGeometry
    Base Class
    doc

    """

    def __init__(self):
        """
        BaseGeometry
        init function
        doc
        """
        pass

    def area(self):
        """
        area function
        for geometery
        calculation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator
        validates value:
        you can assume name is always a string
        Args:
            name (_type_): _description_
            value (_type_): _description_
        """

        if value.__class__ != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle
    sub Class
    doc

    """

    def __init__(self, width, height):
        """__init__

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

    def __rpr__(self):
        """__rpr__
        this is to return
        str version of the rectangle
        """
        self.__str__()

    def area(self):
        """area
        this is to calculate th rectangel
        area using its specifc equation
        Returns:
            _type_: _description_
        """
        return int(self.__width * self.__height)
