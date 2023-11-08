#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = []
    for item in my_list:
        existing_item = list(filter(lambda x: x == item, uniq_list))
        if len(existing_item) == 0:
            uniq_list.append(item)
    for num in uniq_list:
        result += num
    return result
