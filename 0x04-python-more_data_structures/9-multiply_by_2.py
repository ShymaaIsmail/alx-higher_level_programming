#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for k, v in dict(a_dictionary).items():
        new_dict.update({k: v * 2})
    return new_dict
