#!/usr/bin/python3

"""
models.rectangle module
Rectangle Class
very long text
"""
from models.base import Base


"""
models.rectangle module
Rectangle Class
very long text
"""


class Rectangle(Base):
    """Rectangle class with private attributes
    Args: width, height, x, y
    Raises : TypeError, ValueError
    """

    """attribute prop"""
    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """_summary_

        Args:
            width (_type_): _description_
        """
        self.__validate_int("width", width)
        self.__validate_positive("width", width)
        self.__width = width

    """attribute prop"""
    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, height):
        """_summary_

        Args:
            height (_type_): _description_
        """
        self.__validate_int("height", height)
        self.__validate_positive("height", height)
        self.__height = height

    """attribute prop"""
    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """_summary_

        Args:
            x (_type_): _description_
        """
        self.__validate_int("x", x)
        self.__validate_negative("x", x)
        self.__x = x

    """attribute prop"""
    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """_summary_

        Args:
            y (_type_): _description_
        """
        self.__validate_int("y", y)
        self.__validate_negative("y", y)
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor to set attributes upon instantiation"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be greater than zero!")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be greater than zero!")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be greater than zero!")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be greater than zero!")
        self.__y = y

    def __validate(self, width, height, x, y):
        """_summary_

        Args:
        width (_type_): _description_
        height (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        """
        self.__validate_int("width", width)
        self.__validate_positive("width", width)
        self.__validate_int("height", height)
        self.__validate_positive("height", height)
        self.__validate_int("x", x)
        self.__validate_negative("x", x)
        self.__validate_int("y", y)
        self.__validate_negative("y", y)

    def __validate_int(self, name, value):
        """
        __validate_int
        validates value:
        you can assume name is always a string
        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        if value.__class__ != int:
            raise TypeError(f"{name} must be an integer")

    def __validate_negative(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __validate_positive(self, name, value):
        """
        __validate_positive
        """
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """area"""
        return self.__width * self.__height

    def display(self):
        """display"""
        for r in range(0, self.__height + self.__y):
            for c in range(0, self.__width + self.__x):
                if (r < self.__y):
                    break
                if (c < self.__x):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """__str__"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """update"""
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
                    setattr(self, arg, kwargs[arg])

    def to_dictionary(self):
        """_summary_   this is very long description
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
