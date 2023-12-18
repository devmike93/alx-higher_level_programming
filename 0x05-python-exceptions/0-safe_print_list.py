#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    arg_count = 0
    while arg_count < x:
        try:
            print(f"{my_list[arg_count]}", end='')
        except IndexError:
            break
        arg_count += 1
    print()
    return arg_count
