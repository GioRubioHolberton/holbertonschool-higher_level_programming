#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = ord(i)
        if (ord(i) > 96 and ord(i) < 123):
            letter = ord(i) - 32
        print("{:c}".format(letter), end='')
    print()
