#!/usr/bin/python3
def number_of_lines(filename=""):
    my_lines = 0
    with open(filename) as f:
        for line in f:
            my_lines += 1
    return my_lines
