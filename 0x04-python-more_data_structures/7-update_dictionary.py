#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    existing_item = dict(filter(lambda k: k == key, a_dictionary.items()))
    if len(existing_item) > 0:
        dict(a_dictionary).update(key, value)
    else:
        dict(a_dictionary)[key] = value
    return a_dictionary
