###Task five
##def main():
##    name = input("Enter the name of the file to read:\n")
##    file1 = open(name, "r")
##    file2 = open("Exercise5_output.txt", "w")
##################################################################
##def menu():
##    print('''Select one of the following operations:
##1) Enter the values
##2) Sum
##3) Subtract
##4) Multiply
##5) Divide
##0) Stop''')
##    choice = int(input("Select the function (0-5):\n"))
##    return choice
##################################################################
##def read_value(file1):
##     line = file1.readline()
##    if line == '':
##        print("End of values, end the program.")
##        return 0
##    return float(line.strip())
##################################################################
def menu():
    print('''This calculator can perform the following functions:
1) Enter the values
2) Sum
3) Subtract
4) Multiply
5) Divide
0) Stop''')
    choice = int(input("Select the function (0-5):\n"))
    return choice

def read_value(file_handle):
    line = file_handle.readline()
    if line == '':
        print("End of values, end the program.")
        return 0
    return int(line.strip())

def sum_values(value1, value2):
    return f"sum {value1} + {value2} = {value1 + value2}"

def subtract(value1, value2):
    return f"subtract {value1} - {value2} = {value1 - value2}"

def multiplication(value1, value2):
    return f"multiply {value1} * {value2} = {value1 * value2}"

def division(value1, value2):
    if value2 == 0:
        return "Cannot divide by zero."
    else:
        return f"division {value1} / {value2} = {round(value1 / value2, 2)}"

def main():
    filename = input("Enter the name of the file to read:\n")
    file1 = open(filename, 'r')
    file2 = open("Exercise5_output.txt", 'w')
    number1 = 0
    number2 = 0

    while True:
        choice = menu()
        
        if choice == 1:
            number1 = read_value(file1)

            number2 = read_value(file1)

            print(f"Values {number1} and {number2} were read")

        elif choice == 2:
                result = sum_values(number1, number2)
                print("Result saved in file.")
                file2.write(result + '\n')

        elif choice == 3:
                result = subtract(number1, number2)
                print("Result saved in file.")
                file2.write(result + '\n')

        elif choice == 4:
                result = multiplication(number1, number2)
                print("Result saved in file.")
                file2.write(result + '\n')

        elif choice == 5:
                result = division(number1, number2)
                print("Result saved in file.")
                file2.write(result + '\n')

        elif choice == 0:
            print("Stopping")
            break

        else:
            print("Unknown selection, try again.")

    file1.close()
    file2.close()

main()
