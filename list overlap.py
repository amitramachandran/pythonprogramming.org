# defining two lists
a=[1,2,3,4,4,5,6,7]
b=[1,4,6,8,9,10,37,50]
c=[]
for element in a:
    if element in b:
       c.append(element)

print set(c)

