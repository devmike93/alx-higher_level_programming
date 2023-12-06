#!/usr/bin/python3
"""
def search_replace(my_list, search, replace):
    #  replaces all occurrences of an element by another in a new list
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
"""


def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list """
    new_list = [replace if x == search else x for x in my_list]
    return new_list
