#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        you_list = my_list[:]
        you_list[idx] = element
    return you_list
