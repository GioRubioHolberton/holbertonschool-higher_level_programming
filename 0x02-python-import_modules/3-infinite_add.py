#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for it in range(1, len(argv)):
        add = add + int(argv[it])
    print(add)