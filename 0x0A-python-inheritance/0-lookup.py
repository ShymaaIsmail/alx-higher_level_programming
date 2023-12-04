#!/usr/bin/python3
"""
0-lookup.py

summary
"""


def lookup(obj):
    """lookup function
    to list all attrs and methods
    in an obj
    """
    list = []
    if obj is not None:
        list = dir(obj)
    return list
