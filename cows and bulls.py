import random
def ran():
    userinput = str(raw_input('type a four digit number:-'))
    a=map(int,userinput)
    cow=0
    bull=0
    count=0
    print number
    #if number == userinput or cow == '8':
        #print "you win!!!"
    while True:
        if number==userinput:
            print "you win!!!", "you took", count, "tries"
            break
        if number != userinput:
            count += 1
            for i in a:
                if i in map(int,number):
                    cow+=1
                else:
                    bull+=1
            print "Number of cows:-", cow
            print "Number of bulls:-", bull
            ran()


if __name__=="__main__":
    number = str(random.randint(1000, 9999))
    ran()


