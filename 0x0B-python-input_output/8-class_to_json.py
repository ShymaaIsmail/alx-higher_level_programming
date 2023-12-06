#!/usr/bin/python3
"""
8-class_to_json module

"""


def class_to_json(obj):
    """class_to_json

    Args:
        obj (_type_): _description_
    """
    result = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
    return result
