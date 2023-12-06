#!/usr/bin/python3
"""
    def uniq_add(my_list=[]):
    #  adds all unique integers in a list (only once for each integer)
    result = sum(set(my_list))
    return result
"""


def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer) """
    unique_set = set()
    result = 0

    for num in my_list:
        if num not in unique_set:
            result += num
            unique_set.add(num)
    return result
