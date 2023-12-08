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

    last_index = len(text) - 1
    while last_index >= 0 and text[last_index].isspace():
        last_index -= 1
    
    for i, char in enumerate(text):
        print(char, end="")
        if char in delimiters and i != last_index:
            print("\n", end="")

    if text and text[last_index] not in delimiters:
        print("\n")
    if text and text[-1] not in delimiters:
        print("\n")
