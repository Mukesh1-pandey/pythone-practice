x=3000
for i in range(5):
    i=input('Enter "W" to withdrawal, "D" to  deposit And "E" to complite the proces')
    print(F"The net amount = {x}")
    match i:
        case"W":
            print("The withdrawal start")
            c=int(input("Enter the withdrawal amount"))
            x-=c
            print('The net amount is',x)
        case"D":
            print('The deposit start')
            d=int(input("The deposit value\n"))
            x+=d
            print('the net amount is ',x)
        case"E":
            print('the proces complete')
            print('the NEW TOTAL AMOUNT IS ',x)
            break
        case _:
            print("Invalid option, Please enter 'W', 'D', or 'E'.")