#!/usr/bin/python3
"""
This is 1-my_list module
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        super().sort(self)
        print(super().items)
