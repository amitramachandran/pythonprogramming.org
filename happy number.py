first_op=raw_input("type the number you want to find whether is happy number")
try:
    first_operand=first_op
    while True:
        digits=[int(j) for j in str(first_operand)]
        first_operand=0
        print digits
        if digits==[1]:
            print first_op, "is happy number"
            break
        elif digits==[4]:
            print first_op,"is sad number"
            break
        for element in digits:
            newnumber=int(element)**2
            first_operand=(first_operand+newnumber)

except IndexError:
    print ""


