#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle():
    """A class that represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """get width"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """get height"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    @property
    def dict(self):
        """return dictionary representation of object"""
        return {
            '_Rectangle__width': self.width,
            '_Rectangle__height': self.height
        }

    def __init__(self, width=0, height=0):
        """Initialize attributes of the Rectangle object."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """destructor for the Rectangle object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculate Area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate Perimeter"""
        result = 0
        if (self.width > 0 and self.height > 0):
            result = 2 * (self.height + self.width)
        return result

    def print(self):
        """Print print_symbol rectangle"""
        print(self.str())

    def __str__(self):
        """Stringify the rectangle object"""
        result = ""
        if (self.height > 0 and self.width > 0):
            for row in range(0, self.height):
                for column in range(0, self.width):
                    result = result + str(self.print_symbol)
                result = result
                if (row != self.height - 1):
                    result += "\n"
        return result

    def __repr__(self):
        """Returns valid python representation for Rectangle"""
        return f"Rectangle({self.width}, {self.height})"
