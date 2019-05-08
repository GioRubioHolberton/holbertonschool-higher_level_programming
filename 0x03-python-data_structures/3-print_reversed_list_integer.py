#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rever = my_list[::-1]
    for num in rever:
        print("{:d}".format(num))
