#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This is 8-rectangle
doc
task
number 8
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
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.width = width
            self.height = height
        except (ValueError, TypeError) as e:
            raise e
