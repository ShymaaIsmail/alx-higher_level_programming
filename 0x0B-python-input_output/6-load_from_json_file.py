#!/usr/bin/python3
"""
6-load_from_json_file module

"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename(_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        return json.loads(content)
