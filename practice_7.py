l=[]
x=int(input("enter the value of x="))
y=int(input("enter the value of y="))
for i in range(x):
    a=[]
    for j in range(y):
        b=i*j
        a.append(b)
    l.append(a)
for a in l:
    print(a)