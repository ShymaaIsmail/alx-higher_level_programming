#!/usr/bin/python3
"""
10-student class

"""


class Student:
    """A student has a name and an age."""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json
        """
        result = {}
        for attr, value in self.__dict__.items():
            if not (isinstance(value, (str)) and len(value) == 0):
                result[attr] = value
        return result
