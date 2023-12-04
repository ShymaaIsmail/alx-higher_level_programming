#!/usr/bin/python3
"""
This is
3-is_kind_of_class
module
"""


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if obj is not None and a_class is not None:
        return isinstance(obj, a_class)
    else:
        return False
