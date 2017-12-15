try:
    b=[]
    c=[]
    for i in range(1, 100):
        d=[int(i) for n in range(2,i) if i%n =='0']
    for first_op in range(1,1000):
        first_operand=first_op
        while True:
            digits=[int(j) for j in str(first_operand)]
            first_operand=0
            #print digits
            if digits==[1]:
                b.append(first_op)
                break
            elif digits==[4]:
                c.append(first_op)
                break
            for element in digits:
                newnumber=int(element)**2
                first_operand=(first_operand+newnumber)
    print "happy one", b
    print "sad one", c
    print d
    #print "common ones",list(set(b).intersection(d))
except IndexError,ZeroDivisionError:
    print ""