#!/usr/bin/python3
"""
2-append_write module for task 2
This is the full doc
for this task
"""


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'a') as file:
        return file.write(text)
