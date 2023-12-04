#!/usr/bin/python3
"""
This is 1-my_list
MyList class doc
for task 1
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """
        print_sorted
        print_sorted

        """
        self.sort()
        print(self)
