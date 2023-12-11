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
    Args: id, width, height, x, y
    Raises : Type and Value Errors
    """

  

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        pass

    def area(self):
        """area"""
        return self.__width * self.__height

    def display(self):
        """display"""
        pass

    def __str__(self):
        """__str__"""
        return f"[Rectangle]\
        ({self.id}){self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update"""
        pass



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
        self.__y = y

    def to_dictionary(self):
        """_summary_   this is very long description
        """
        return {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
