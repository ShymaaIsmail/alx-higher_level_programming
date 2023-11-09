#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman_symbol = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is not None and isinstance(roman_string, str):
        for i in range(len(roman_string)):
            c = roman_string[i]
            prev_c = roman_string[i - 1]
            if i > 0 and roman_symbol[c] > roman_symbol[prev_c]:
                number += roman_symbol[c] - 2 * roman_symbol[prev_c]
            else:
                number += roman_symbol[c]
    return number
