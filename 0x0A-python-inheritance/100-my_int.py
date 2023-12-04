#!/usr/bin/python3
"""
This is 100-my_int
MyInt  class doc
for task 100
"""


class MyInt (int):
    """_summary_

    Args:
        int (_type_): _description_
    """
    def __eq__(self, other):
        """
        revert eq
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        revert eq
        """
        return not self.__eq__(other)
