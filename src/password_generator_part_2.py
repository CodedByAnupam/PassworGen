# Write your solution here

# from string import *
# from math import *

import string
import random


def generate_strong_password(length, arg1, arg2):
    a = string.ascii_lowercase
    b = string.digits
    c = "!?=+-()#"
    password = ""

    password += random.choice(string.ascii_lowercase)
    if arg1:
        password += random.choice(b)
    if arg2:
        password += random.choice(c)

    pool = a

    if arg1:
        pool += b
    if arg2:
        pool += c

    while len(password) < length:
        password += random.choice(pool)

    # random.shuffle(password)

    return password


if __name__ == "__main__":
    generate_strong_password()
