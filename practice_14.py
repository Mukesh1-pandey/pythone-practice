a=input("enter a string which have both alpha and digit.\n")
the_count_upper=0
the_count_lower=0
for i in a:
    if i.isupper():
        the_count_upper+=1
    if i.islower():
        the_count_lower+=1
    else:
        pass
print(the_count_upper)
print(the_count_lower)