#!/usr/bin/python3
"""Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    @property
    def size(self):
        """_summary_
        """
        return self.width

    @size.setter
    def size(self, size):
        """_summary_

        Args:
            size (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.width = size
        self.height = size

    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """update"""
        attributes = ['id', 'size', 'x', 'y']
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
