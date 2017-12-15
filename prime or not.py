def prime(userval):
    count=0
    for x in range(1,userval+1):
        if userval%x==0:
            count+=1
    if count==2:
         print "prime number"
    elif count>2:
        print "not a prime"

userval=int(raw_input("enter a number:"))
prime(userval)

