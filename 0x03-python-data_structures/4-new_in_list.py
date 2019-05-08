#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    you_list = my_list[:]
    if idx >= 0 and idx < len(you_list):
        you_list[idx] = element
    return you_list
