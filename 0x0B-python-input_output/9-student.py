#!/usr/bin/python3
"""
9-student class

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
        json = {}
        json['first_name'] = self.first_name
        json['last_name'] = self.last_name
        json['age'] = self.age
        return json
