#Task three
import math
def valueError():
    try:
        number = int(input("Give a non-negative integer:\n"))
        result = math.sqrt(number)
        print(f"Square root of {number} is {result:.2f}")
    except ValueError:
        print("ValueError happened. Non-negative integer expected for square root.")

def indexError():
    list_of_nums = [11, 22, 33, 44, 55]
    try:
        index = int(input("Enter an index (0-4):\n"))
        print(f"The value at index {index} is {list_of_nums[index]}")
    except IndexError:
        print("IndexError: Index out of bounds.")

def zeroDivisionError():
    try:
        divider = int(input("Enter a divider:\n"))
        result = 4 / divider
        print(f"4 divided by {divider} is {result:.2f}")
    except ZeroDivisionError:
        print("ZeroDivisionError: You cannot divide by zero.")

def typeError():
    try:
        string1 = input("Enter a string:\n")
        string2 = "world"
        result = string1 * string2
        print(result)
    except TypeError:
        print("TypeError: Cannot multiply two strings together.")

def menu():
    print('''What do you want to do:
1) Test for ValueError
2) Test for IndexError
3) Test for ZeroDivisionError
4) Test for TypeError
0) Stop''')
    
    try:
        choice = int(input("Your choice:\n"))
        return choice
    except ValueError:
        print("Please enter a valid integer for menu selection.")
        return None

def main():
    while True:
        choice = menu()
        
        if choice == 1:
            valueError()
        elif choice == 2:
            indexError()
        elif choice == 3:
            zeroDivisionError()
        elif choice == 4:
            typeError()
        elif choice == 0:
            print("See you again!")
            break
        elif choice is not None:
            print("Unknown selection, please try again.")
main()
