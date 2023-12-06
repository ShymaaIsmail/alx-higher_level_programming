#!/usr/bin/python3
"""
100-append_after

"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function appends a string after the first occurrence
    of another string in a file.
    """
    with open(filename, 'r') as file:
        file_contents = file.readlines()
    for line_num, line in enumerate(file_contents):
        if search_string in line:
            position = line.index(search_string) + 1
    file_contents.insert(position - 1, new_string)
    with open(filename, 'w') as file:
        file.writelines(file_contents)
