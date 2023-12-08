#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """text_indentation

    Args:
        text (_type_): _description_
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = [":", "?", "."]
    text = text.strip()
    for char in text:
        print(char, end="")
        if char in delimiters:
            print("\n\n", end="")
    if text and text[-1] not in delimiters:
        print("\n")
