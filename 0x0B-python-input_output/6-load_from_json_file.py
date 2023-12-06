#!/usr/bin/python3
"""
6-load_from_json_file module

"""
import json
import os


def load_from_json_file(filename):
    """_summary_

    Args:
        filename(_type_): _description_

    Returns:
        _type_: _description_
    """
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as file:
            content = file.read()
            if len(content) > 0:
                return json.loads(content)
            else:
                return []
    else:
        return []
