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

    modified_contents = []
    for line in file_contents:
        modified_contents.append(line)
        if search_string in line:
            modified_contents.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(modified_contents)
