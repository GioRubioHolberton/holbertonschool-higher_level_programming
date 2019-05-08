#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        big = my_list[0]
        for mov in my_list:
            if big < mov:
                big = mov
        return big
    else:
        return None
