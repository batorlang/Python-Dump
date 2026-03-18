

def menu():
    print("""Menu:
1) Remove an employee
2) Modify employee data
3) Print all employees
0) Exit""")
    choice = int(input("Enter your choice:\n"))
    return choice


def remove_employee(employee_list):
    print("List of Employees:")
    index = 1
    for i in range(len(employee_list)):
        print(f"{index}) Name: {employee_list[i]['Name']}, Workplace: {employee_list[i]['Workplace']}, Age: {employee_list[i]['Age']}")
        index += 1
    try:
        remove_choice = int(input("Enter the number of the employee to remove:\n"))
        removechoice = remove_choice - 1
        removed_line = employee_list.pop(removechoice)
        print(f"Removed employee: {removed_line['Name']}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def modify_employee(employee_list):
    print("List of Employees:")
    index = 1
    for i in range(len(employee_list)):
        print(f"{index}) Name: {employee_list[i]['Name']}, Workplace: {employee_list[i]['Workplace']}, Age: {employee_list[i]['Age']}")
        index += 1
    try:
        modify_choice = int(input("Enter the number of the employee to modify:\n"))
        modifychoice = modify_choice - 1
        employee = employee_list[modifychoice]
        modify_filed = int(input('''Enter the field to modify:
1) Workplace
2) Age\n'''))
        if modify_filed == 1:
            change_of_workplace = input("Enter new value for Workplace:\n")
            employee['Workplace'] = change_of_workplace
        elif modify_filed == 2:
            change_of_age = int(input("Enter new value for Age:\n"))
            employee['Age'] = change_of_age
    except ValueError:
        print("Invalid input. Please enter a number.")
        


def print_employee(employee_list):
    print("List of Employees:")
    for i in range(len(employee_list)):
        print(f"Name: {employee_list[i]['Name']}, Workplace: {employee_list[i]['Workplace']}, Age: {employee_list[i]['Age']}")


def main():
    employee_dict = [
        {'Name': 'John', 'Workplace': 'LUT', 'Age': 25},
        {'Name': 'Jack', 'Workplace': 'Finnair', 'Age': 18},
        {'Name': 'Robin', 'Workplace': 'JBL', 'Age': 32},
        {'Name': 'Annie', 'Workplace': 'LUT', 'Age': 24},
        {'Name': 'Niels', 'Workplace': 'Microsoft', 'Age': 45}
    ]
    employee_list = employee_dict
    while True:
        choicevalue = menu()
        if choicevalue == 1:
            remove_employee(employee_list)
        elif choicevalue == 2:
            modify_employee(employee_list)
        elif choicevalue == 3:
            print_employee(employee_list)
        elif choicevalue == 0:
            print("See you again!")
            break
        else: 
            print("Invalid input. Please try again!")
main()
