special_characters = "@#$"
for i in range(3):#which provide 3 number of trial to enter correct form of pass password
    print("Enter username and password to register")
    a = input("Enter the first name = ")
    b = input("Enter the last name = ")
    print(f"{a} {b}")
    c = input("Enter the password = ")

    if not (any(i.isalpha() for i in c) and 
        any(i.isdigit() for i in c) and
        any(i.isupper() for i in c) and
        any(i.islower() for i in c) and 
        any(c in special_characters for c in special_characters)) :
        print("Password must contain uppercase, lowercase, digits,  alphabets and special characters")
        continue
    if len(c) < 6 or len(c) > 12:
        print("Password must be between 6 and 12 characters long")
        continue
    print("You have registered with a new username and password")
    break