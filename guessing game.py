import random
answer = str(random.randrange(1,100))
count=0
while answer:
    user = str(raw_input("enter a number from 1-100 :"))
    count+=1
    if user=="exit":
        print "you quit"
        break
    elif user<answer:
        print "guess higher"
    elif user>answer:
        print "guess lower"
    elif user==answer:
        print "you guessed correctly"
        print "you took",count,"times to guess correctly"
        break

