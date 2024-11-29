a=[]
for i in range(4):
    b=input("enter a number having a binary digit 0 and 1 = ")
    a.append(b)
print(a)
c=[]
for i in a:
    i=int(i)
    if(i%5==0):
        c.append(i)
f=[]        
for i in c:
    g=str(i)
    f.append(g)
d=','.join(f)
print("the binary number which is divisible by 5 is")
print(d)