the_input_vqlue=[]
the_odd_number=[]
for i in range(5):
    i=input("enter the random number =")
    if i.isdigit():
        the_input_vqlue.append(i)
for i in the_input_vqlue:
    c=int(i)
    if(c%2!=0):
        d=c**2
        the_odd_number.append(str(i))
    else:
        pass
e=",".join(the_odd_number)
print(e)
