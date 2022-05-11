

from ast import Lambda
from pickletools import string1

w1=input("word 1: ")
w2=input("word 2: ")
w3=input("word 3: ")
w4=input("word 4: ")
string1="My name is {} and {} {} %s".format(w1,w2,w3) %w4
print(string1)


 