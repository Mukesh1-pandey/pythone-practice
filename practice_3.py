a={}
i=1
n=int(input("enter the number="))
for i in range(i,n):
    a.update({i:i*i})
    i+1
print("the dictionary range from 1 to (n-1) number")    
print(a.items())    