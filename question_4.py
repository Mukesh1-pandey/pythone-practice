import math
c=50
h=30
d=[]
i=0
for i in range(0,3):
    a=int(input("Enter the number"))
    d.append(a)
for i in range(0,3):
     print("The list element at index",i,"is",d[i])  
print(d[0:])
e=[]
for i in range(0,3):
     a=(2*c*d[i])/h
     q=math.sqrt(a)
     f=int(q)
     e.append(f)
print(e[0:])