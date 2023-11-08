#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary).items()
    for k, v in new_dict.items():
        new_dict.updte({k, v * 2})
    return new_dict
