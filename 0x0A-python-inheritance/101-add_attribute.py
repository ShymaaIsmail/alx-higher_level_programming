#!/usr/bin/python3
"""_summary_

last advanced task
"""


def add_attribute(a_class, attr, value):
    """Add an attribute to a class."""
    if attr is not None:
        if not hasattr(a_class, attr):
            setattr(a_class, attr, value)
        if not hasattr(a_class, attr):
            raise Exception("can't add new attribute")
