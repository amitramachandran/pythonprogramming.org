import random
values=range(1,100)
b=[]
a=[]
c=[]
e=[]
#two random list generation
for i in range(10):
    b.append(int(random.choice(values)))
    a.append(int(random.choice(values)))
print a,b
#this shows the logic for common element without duplication
c=[num for num in a if num==b[i]]
d=set(c)
print "common elements in both list is :",list(d)
print "the first and last element in list is :"
print [a[0], a[len(a)-1],b[0], b[len(b)-1]]