i=999
a=[]
for i in range(999,3001):
    if(i%2==0):
        c=str(i)
        a.append(c)
b=','.join(a)
print('even number between 1000 to 3000 including 1000 and 3000 = ')
print(b)