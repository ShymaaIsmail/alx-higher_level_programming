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

    punctuation_marks = ['.', '?', ':']
    lines = []
    current_line = []

    for char in text:
        current_line.append(char)
        if char in punctuation_marks:
            lines.append(''.join(current_line).strip())
            current_line = []

    lines.append(''.join(current_line).strip())

    for idx in range(0, len(lines)):
        if idx == (len(lines) - 1):
            print(lines[idx].strip(), end="")
        else:
            print(lines[idx].strip(), end="\n")
