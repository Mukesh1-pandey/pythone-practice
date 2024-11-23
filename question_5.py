l=[]
x=int(input("enter the x="))
y=int(input("enter the y="))
for i in range(x):
    row=[]
    for j in range(y):
        a=i*j
        row.append(a)
    l.append(row)
for row in l:
    print(row)
