import math

def valueError():
    try:
        user_input = input("Give a non-negative integer: \n")
        number = int(user_input)
        if number < 0:
            raise ValueError("Non-negative number expected for square root.")
        result = math.sqrt(number)
        print(f"Square root of {number} is {result:.2f}.")
    except ValueError as ve:
        print("ValueError happened. Non-negative number expected for square root.")

def indexError():
    sample_list = [11, 22, 33, 44, 55]
    try:
        index = int(input("Input index 0-4: \n"))
        print(f"List value is {sample_list[index]} at index {index}.")
    except IndexError:
        print(f"Got an IndexError with index {index}.")
    except ValueError:
        print("ValueError happened. Enter the selection as an integer.")

def zeroDivisionError():
    try:
        divider = int(input("Enter divider: \n"))
        result = 4 / divider
        print(f"4/{divider} = {result:.2f}.")
    except ZeroDivisionError:
        print(f"ZeroDivisionError occurred, divider {divider}.")
    except ValueError:
        print("ValueError happened. Enter the selection as an integer.")

def typeError():
    try:
        user_input = input("Enter number:\n")
        result = int(user_input) * "string"
        print("This should not be printed.")
    except TypeError:
        print("Got TypeError. Two strings cannot be multiplied together.")
    except ValueError:
        print("ValueError happened. Enter the selection as an integer.")

def main():
    while True:
        print("What do you want to do:")
        print("1) Test for ValueError")
        print("2) Test for IndexError")
        print("3) Test for ZeroDivisionError")
        print("4) Test for TypeError")
        print("0) Stop")
        try:
            choice = int(input("Your choice:\n"))
        except ValueError:
            print("Got TypeError. Two strings cant be multiplied together.")
            continue
        
        if choice == 0:
            print("See you again!")
            break
        elif choice == 1:
            valueError()
        elif choice == 2:
            indexError()
        elif choice == 3:
            zeroDivisionError()
        elif choice == 4:
            typeError()
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
