#!/usr/bin/python3

"""It is a module for class Rectangle
that inherits directly from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class as child of Base
    it has private and specific values
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor to set init value after validations"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """apply area equation to w and h

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """display # sign to draw rectangle"""
        for r in range(0, self.__height + self.__y):
            for c in range(0, self.__width + self.__x):
                if (r < self.__y):
                    break
                if (c < self.__x):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """set  an arg val to its relevant attr
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if (args and len(args) > 0):
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
                else:
                    break
        else:
            for arg in kwargs:
                if arg in attributes:
                    new_value = kwargs[arg]
                    setattr(self, arg, new_value)

    def __str__(self):
        """__str__"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    """width prop getter"""
    @property
    def width(self):
        """width prop getter"""
        return self.__width

    @width.setter
    def width(self, val):
        """width prop setter"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    """height prop"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")

        self.__height = val

    """x prop"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    """y prop"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")

        self.__y = val

    def to_dictionary(self):
        """ to_dictionary to_dictionary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,

        }
