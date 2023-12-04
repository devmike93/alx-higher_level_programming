#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]  # new_list is copy of original
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element  # replace inde with elementS
    return new_list
