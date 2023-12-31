#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle():
    """A class that represents a rectangle."""

    def width(self):
        """get width"""
        return self._Rectangle__width

    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    def height(self):
        """get height"""
        return self._Rectangle__height

    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def __init__(self, width=0, height=0):
        """Initialize attributes of the Rectangle object."""
        self.width(width)
        self.height(height)
