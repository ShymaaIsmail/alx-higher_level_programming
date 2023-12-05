#!/usr/bin/python3
"""
5-save_to_json_file module

"""
import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename(_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, 'a', encoding="utf-8") as file:
        str = json.dumps(my_obj)
        file.write(str)
