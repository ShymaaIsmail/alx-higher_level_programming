#!/usr/bin/python3
"""0-read_file module for task 0
"""
def read_file(filename=""):
    """read_file

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
