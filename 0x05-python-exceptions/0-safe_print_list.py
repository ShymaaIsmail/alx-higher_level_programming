#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    try:
        count = 0
        if (my_list != []):
            for element in my_list:
           		print(element, end = '')
          		count += 1
           		if count == x:
               		print()
               		break
            
    except TypeError:
        pass
    return count
