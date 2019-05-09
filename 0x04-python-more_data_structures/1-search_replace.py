#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list
    new = list(map(lambda y: replace if y == search else y, new))
    return new
