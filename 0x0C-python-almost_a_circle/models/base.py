#!/usr/bin/python3

"""base clase
module do
"""
import json


class Base:
    """Base Class
    """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
