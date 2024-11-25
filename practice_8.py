d=[]
i=0
for i in range(0,3):
    a=input("Enter the word ")
    d.append(a)
d.sort()
f=','.join(d)
print(f)