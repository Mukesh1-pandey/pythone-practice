a=input("enter a string which have both alpha and digit.\n")
the_count_alpha=0
the_count_digit=0
for i in a:
    if i.isalpha():
        the_count_alpha+=1
    if i.isdigit():
        the_count_digit+=1
    else:
        pass
print(the_count_alpha)
print(the_count_digit)        