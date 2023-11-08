#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    soreted_dic = sorted(dict(a_dictionary))
    for k, v in soreted_dic:
        print("{}: {}".format(k,v))
