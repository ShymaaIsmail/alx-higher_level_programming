#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        max_num = 0
        for n in my_list:
            if (n > max_num):
                max_num = n
        return max_num
    else:
        return None
