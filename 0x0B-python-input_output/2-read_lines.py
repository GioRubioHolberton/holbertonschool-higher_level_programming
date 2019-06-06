#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for cont in range(nb_lines):
                print(f.readline(), end="")
