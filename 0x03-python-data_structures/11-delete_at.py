#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx >= 0 and idx < len(my_list):
        new_list = []
        for i in range(0, len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
        del my_list[idx]
        return new_list
    else:
        return my_list
