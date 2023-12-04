#!/usr/bin/python3
"""
This is
4-inherits_from
module
"""


def inherits_from(obj, a_class):
    """ inherits_from

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    return issubclass(type(obj), a_class)
