#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l = (number * -1) % 10
else:
    l = number % 10
t = "Last digit of {}".format(number)
if l > 5:
    print("{:s} is {:d} and is greater than 5".format(t, l))
elif l == 0:
    print("{:s} is {:d} and is 0".format(t, l))
else:
    print("{:s} is {:d} and is less than 6 and not 0".format(t, l))
