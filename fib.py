def fib():
    i=0
    a=0
    b=1
    print a
    print b
    x=(input-2)
    while i<x:
        next=a+b
        print next
        a=b
        b=next
        i+=1

input = int (raw_input("the number of fib numbers:"))
fib()


