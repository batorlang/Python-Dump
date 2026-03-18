#First Task
year = int(input("Enter a year:\n"))
if year % 400 == 0:
    print(year, "is a leap year.")
else:
    if year % 100 == 0:
        print(year,"is not a leap year.")
    else:
        if year % 4 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
#Second Task
yn = str(input("Do you want to stop the execution of the program (Y/N):\n"))
if yn == 'Y':
    print("Bye!")
elif yn == 'N':
    username = str(input("Enter username:\n"))
    password = str(input("Enter passwors:\n"))
    if username == 'Pekka' and password == 'somerandomthing':
        print("User recognized!")
    else:
        print("You entered an invalid login name or password.")
else:
    print("Invalid input! Please try again.")
#Third Task
integer1 = int(input("Enter the first number:\n"))
integer2 = int(input("Enter the second number:\n"))
print('''The calculator can perform the following operations:
1) Add
2) Subtract
3) Multiply
4) Divide
The numbers you enterd are''', integer1,'''and''', integer2)
choice = int(input("Select the operation (1-4):\n"))
if choice == 1:
    print("Selection 1:", integer1,"+", integer2,"=", integer1+integer2)
elif choice == 2:
    print("Selection 2:", integer1,"-", integer2,"=", integer1-integer2)
elif choice == 3:
    print("Selection 3:", integer1,"*", integer2,"=", integer1*integer2)
elif choice ==4:
    if integer2 == 0:
        print("Error: Zero cannot be used as a divisor.")
    else:
        print("Selection 4q:", integer1,"/", integer2,"=", integer1/integer2)
else:
    print("The operation was not recognized.")
#Fourth Task
points = float(input("Entyer your number of points:\n"))
if points >= 0 and points <= 49:
    print("Your garde is: 0")
elif points >= 50 and points <= 59:
    print("Your garde is: 1")
elif points >= 60 and points <= 69:
    print("Your garde is: 2")
elif points >= 70 and points <= 79:
    print("Your garde is: 3")
elif points >= 80 and points <= 89:
    print("Your garde is: 4")
elif points >= 90 and points <= 100:
    print("Your garde is: 5")

