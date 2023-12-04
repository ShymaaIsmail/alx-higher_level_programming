#!/usr/bin/python3
"""
This is
2-is_same_class
module
"""
def is_same_class(obj, a_class):
    """ is_same_class

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if obj is not None and a_class is not None:
        return isinstance(obj, a_class)
    else:
        return False
