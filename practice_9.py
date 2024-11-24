d=[]
print("pass enter key to stop the input")
while True:
    a=input()
    if a=="":
        break
    d.append(a)
for a in d:
    b=a.upper()
    print(b)