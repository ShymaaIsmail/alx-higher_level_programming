#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle():
    """A class that represents a rectangle."""

    @property
    def width(self):
        """get width"""
        return self._width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """get height"""
        return self._height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @property
    def dict(self):
        """return dictionary representation of object"""
        return {
            'width': self.width,
            'height': self.height
        }
    def __init__(self, width=0, height=0):
        """Initialize attributes of the Rectangle object."""
        self.width = width
        self.height = height
