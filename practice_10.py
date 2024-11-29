i=input('enter a line of code with whitespace\n')
a=i.split(' ')
b=set()
c=[]
for word in a:
    if word not in b:
        b.add(word)
        c.append(word)
d=' '.join(c)                  
print(d)