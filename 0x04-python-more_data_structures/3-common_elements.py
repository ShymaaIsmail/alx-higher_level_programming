#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = []
    for item in set_1:
        existing_item = set(filter(lambda x: x == item, set_2))
        if len(existing_item) > 0:
            common_set.append(item)
    return common_set
