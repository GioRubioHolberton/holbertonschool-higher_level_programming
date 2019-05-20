#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real = 0
    try:
        for count in range(x):
            print("{}".format(my_list[count]), end='')
            real += 1
        print()
    except IndexError:
        print()
    return(real)
