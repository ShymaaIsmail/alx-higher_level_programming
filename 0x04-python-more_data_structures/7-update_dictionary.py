#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = dict(a_dictionary)
    existing_item = dict(filter(lambda k: k == key, a_dictionary.items()))
    if len(existing_item) > 0:
        new_dict.update(key, value)
    else:
        new_dict[key] = value
    return new_dict
