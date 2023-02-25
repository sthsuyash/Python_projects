# program to generate random password of desired length, typically set to 10 characters of alphanumeric characters

import random
import string


def random_password_generator(length):
    password = ''
    string.printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t'

    for i in range(length):
        password += random.choice(string.printable)

    return password


length = int(input("Enter the length of password you want to generate: "))
print(random_password_generator(length))
