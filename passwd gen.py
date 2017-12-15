from __future__ import print_function
import random
import string
def password():
    a=list(range(10))
    b=list(string.ascii_lowercase[:])
    c=list(string.ascii_uppercase[:])
    d=["!","@","$","%","^","&","*"]
    e=[a,b,a,b,d,c,b]
    f=[b,b,a,d]
    if userinput=="strong":
        for i in e:
            print (random.choice(i), end='')
    elif userinput=="weak":
        for i in f:
            print(random.choice(i), end='')

userinput=raw_input("type which password u want to generate\nstrong or weak :")
password()
