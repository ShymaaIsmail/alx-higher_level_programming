#!/usr/bin/python3

"""base
class
module doc
"""
import json


class Base:
    """Base Class
    Attributes
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

    @staticmethod
    def check_object_types(list_objs, base_type, type):
        """_summary_

        Args:
            list_objs (_type_): _description_
            base_type (_type_): _description_
            type (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not isinstance(list_objs, list):
            return False
        for obj in list_objs:
            if not isinstance(obj, base_type):
                return False
        return True

    @classmethod
    def save_to_file(cls, list_objs):
        """to_json

        Args:
            list_dictionaries (_type_): _description_
        """
        data = "[]"
        if ((list_objs is not None) and len(list_objs) > 0):
            obj_type = type(list_objs[0]).__name__
            valid_type = cls.check_object_types(list_objs, Base, obj_type)
            if (valid_type):
                file_name = f"{obj_type}.json"
                data = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
        else:
            file_name = f"{cls.__name__}.json"
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string

        Args:
            json_string (_type_): _description_
        """
        data = []
        if (json_string is not None):
            data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """create
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**item) for item in data]
                return instances
        except FileNotFoundError:
            return []
