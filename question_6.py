#a=["without","hello","bag","world"]
#a.sort()
#b=str(a)
#print(b)

d=[]
i=0
for i in range(0,4):
    a=input("Enter the word")
    d.append(a)
d.sort()
f=','.join(d)
print(f)