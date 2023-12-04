#!/usr/bin/python3
"""
This is 7-base_geometry
doc BaseGeometry
task
number 7
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
