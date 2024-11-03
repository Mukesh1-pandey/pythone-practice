def factorail(n):
    if(n==0 or n==1):
        return 1
    else:
        a=n*factorail(n-1)
        return a
    

i=0
n=int(input("enter the number="))
b=factorail(n)
print(f"the factoral of number = {b}")
c=str(b)
print("the factoral of number is typcasted in to string")
print(type(c))
d=len(c)
print(d)
print("the string which is seperated by a comma ")
print(*c,sep=',')


# for i in range(i,d):
    # print(f"{c[i]},")
# print(c)    