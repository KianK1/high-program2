#!/usr/bin/python3
def pow(a, b):
    result = a ** b
    print("{} ^ {} = {}".format(a, b, result))
a = int(input("First number: "))
b = int(input("Second number: "))
pow(a, b)
