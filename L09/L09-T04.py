#Task four
def divide_numbers():
        num1_input = input("Enter the first number:\n")
        num2_input = input("Enter the second number:\n")
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result:.8f}")
        except ZeroDivisionError:
            print("You cannot divide by zero")
        except ValueError:
            print("You must enter valid numbers")
divide_numbers()
