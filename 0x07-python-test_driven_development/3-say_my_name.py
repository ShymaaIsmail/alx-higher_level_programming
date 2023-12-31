#!/usr/bin/python3
"""3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
