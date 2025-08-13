#!/usr/bin/python3
import random
import string
letter = random.choice(string.ascii_letters)
if letter.islower():
    print (f"{letter}", True)
else:
    print(f"{letter}", False)
