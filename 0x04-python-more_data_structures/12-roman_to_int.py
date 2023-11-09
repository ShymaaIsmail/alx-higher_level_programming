#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman_symbol = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is not None and isinstance(roman_string, str):
        for c in roman_string:
            number += roman_symbol.get(c)
    return number
