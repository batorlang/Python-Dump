def menu():
    print('''Select one of the following operations:
1) Enter integers
2) Sum
3) Subtract
4) Multiplication
5) Division
0) Stop''')
    choice = int(input("Select the function (0-5):\n"))
    return choice
def enter_integer(text):
    return int(input(text))
def sum(value1, value2):
    return f"Sum {value1} + {value2} = {value1 + value2}"
def subtract(value1, value2):
    return f"Subtract {value1} - {value2} = {value1-value2}"
def multiplication(value1, value2):
    return f"Multiplication {value1} * {value2} = {value1*value2}"
def division(value1, value2):
    if value2 == 0:
        return "You cannot divide by zero."
    else:
        return f"Division {value1} / {value2} = {round(value1/value2, 2)}"
def main():
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            number1 = enter_integer("Enter first integer: \n")
            number2 = enter_integer("Enter second integer: \n")
            print(f"You inputted integers {number1} and {number2}")
        elif choicevalue == 2:
            print(sum(number1, number2))
        elif choicevalue == 3:
            print(subtract(number1, number2))
        elif choicevalue == 4:
            print(multiplication(number1, number2))
        elif choicevalue == 5:
            print(division(number1, number2))
        elif choicevalue == 0:
            print('''Bye.''')
            break
        else:
            print("Unknown selection, try again.")
main()
