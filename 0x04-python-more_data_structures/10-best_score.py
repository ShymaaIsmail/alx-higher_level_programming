#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    key = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max_score:
                max_score = v
                key = k
    return key
