import random

def generate():
    b=[]
    for i in range(10):
        a=(random.randint(0,100))
        b.append(a)
        b.sort()
    return b
    binarysearch(b)

def binarysearch(b):
    mid=(len(b)-1)/2
    if b[mid] == int(userinput):
        print "true"
    elif b[mid] < int(userinput):






if __name__=='__main__':
    userinput=raw_input("enter a number within 100:-")
    b=generate()
    print b
    '''if int(userinput) in b:
        print "True"
    else:
        print "false"'''