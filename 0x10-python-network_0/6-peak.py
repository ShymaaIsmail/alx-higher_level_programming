#!/usr/bin/python3
""" Peak finder"""


def find_peak(list_of_integers):
    """find peak"""
    if len(list_of_integers) == 0:
        return None
    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = (left + right) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) \
                and (mid == len(list_of_integers) - 1
                     or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid < len(list_of_integers) - 1 \
                and list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return None
