a=[]
for i in range(1):
    i=input('enter a value')
    if i.isdigit():
        a.append(int(i))
    if i.isalpha():
        a.append(i)
    else:
        pass
print(a)
for i in a:
    if isinstance(i,str):
        b=a[0]
        c=a[0]*2
        d=a[0]*3
        e=b+c+d
        print(f"{b}+{c}+{d}")
    else:
        b=int(str(a[0]))
        c=int(str(a[0])*2)
        d=int(str(a[0])*3)
        e=b+c+d
        print(e)


