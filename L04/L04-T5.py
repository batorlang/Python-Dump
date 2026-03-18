choice = ''
while choice != 0:
    print('''This calculator can perform the following functions:
1) Enter numbers
2) Sum
3) Subtract
4) Multiplication
5) Division
6) Power of
0) Stop''')
    choice = int(input("Select function (0-6):\n"))
    if choice == 1:
        number1 = int(input("Enter the first number:\n"))
        number2 = int(input("Enter the second number:\n"))
        print(f"You entered numbers {number1} and {number2}")
    elif choice == 2:
        print(f"Sum {number1} + {number2} =", number1+number2)
    elif choice == 3:
        print(f"Subtraction {number1} - {number2} =", number1-number2)
    elif choice == 4:
        print(f"Multiplication {number1} * {number2} =", number1*number2)
    elif choice == 5:
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Division {number1} / {number2} =", round(number1/number2, 2))
    elif choice == 6:
        print(f"Power of {number1} ** {number2} =", number1**number2)
    elif choice == 0:
        print('''Stopping
Bye''')
    else:
        print("Unknown selection, try again.")
