#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = list()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(int('inf'))
print(my_list)
my_list.sort()
print(my_list)
