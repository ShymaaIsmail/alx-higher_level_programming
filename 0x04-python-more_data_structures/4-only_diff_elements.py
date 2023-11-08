#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()
    for item in set_1:
        existing_item = set(filter(lambda x: x == item, set_2))
        if len(existing_item) == 0:
            diff_set.add(item)
    for item in set_2:
        existing_item = set(filter(lambda x: x == item, set_1))
        if len(existing_item) == 0:
            diff_set.add(item)
    return diff_set
