#!/usr/bin/python3
"""
This is 7-base_geometry
module
doc
"""


class BaseGeometry:
    """
    BaseGeometry
    Base Class
    """

    def __init__(self):
        """
        BaseGeometry
        init function

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
        """_summary_
        validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message <name> must be greater than 0

        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
