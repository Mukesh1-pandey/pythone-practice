for i in range(1):
    print("Enter username and password to register")
    a=input("Enter the fist name =")
    b=input('Enter the last name =')
    print(f"{a} {b}")
    c=input('Enter the password =')
    if any(i.isalpha() for i in c):
        print("Password concist an alphabate")
    else:
        print("The password don't have alphabate ")
        break
    if any(i.isdigit() for i in c):
        print("Password concist of number")
    else:
        print("The password  don't have numbr ")
        break
    if any(i.isupper() for i in c):
        print("Password concist upper case")
    else:
        print("The password  don't have upper case")
        break
    if any(i.islower() for i in c):
        print("Password have lower case")
    else:
        print("The password  don't have lower case")
        break
    if any(i in "@#$" for i in c):
        print("There is presence of spical char")
    else:
        print("There is no presence of spical char, please enter atlest one spical char ")
        break
    if (len(c)<=6):
        print("Plese enter more char")
        break
    elif(len(c)<=12):
        print("You have your strong password")  
print("You have register with new username and password")