#!/usr/bin/python3
"""
1-write_file module for task 1
This is the full doc
for this task
"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'w') as file:
        return file.write(text)
