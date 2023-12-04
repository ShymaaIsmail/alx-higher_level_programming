#!/usr/bin/python3
"""
This is 1-my_list MyList class doc
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def __init__(self):
        """
          init function
        """
        super().__init__()
  
    def print_sorted(self):
        """print_sorted
        """
        super().sort(self)
        print(super().items)
