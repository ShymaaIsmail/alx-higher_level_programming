#!/usr/bin/python3
"""
0-read_file module for task 0
This is the full doc
for this task
"""


def read_file(filename=""):
    """read_file

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as f:
            read_data = f.read()
            print(f'{read_data}')
