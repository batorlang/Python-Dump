import json

def menu():
    print("What do you want to do?")
    print("1) Print students by age")
    print("2) Print students based on the course they are taking")
    print("3) Print students whose first names end with the letter 'a'")
    print("0) Stop the program")  
    try:
        choice = input("Enter your choice:\n")
        return choice
    except ValueError:
        print("Invalid choice. Please try again.")
        return None
        


def load_students(file_path):
    """Load students from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def print_students_by_age(student_list):
    """Print students based on selected age."""
    ages = []
    for student in student_list:
        if student['age'] not in ages:
            ages.append(student['age'])
    age.sort()
    print("Select the ages of the students:")
    index = 1
    for age in ages:
        print(f"{index}) {age}")
        index += 1
    
    try:
        selection = int(input("Enter your selection:\n"))
        selected_age = ages[selection - 1]
        print(f"Students with age {selected_age}:")
        for student in student_list:
            if student['age'] == selected_age:
                print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")

def print_students_by_course(student_list):
    """Print students based on selected course."""
    courses = []
    for student in student_list:
        for course in student['courses']:
            if course not in courses:
                courses.append(course)
    
    print("Select the course:")
    index = 1
    for course in courses:
        print(f"{index}) {course}")
        index += 1
    
    try:
        selection = int(input("Enter your selection:\n"))
        selected_course = courses[selection - 1]
        print(f"Students enrolled in {selected_course}:")
        for student in student_list:
            if selected_course in student['courses']:
                print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}")
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")

def print_students_name(student_list):
    """Print students whose first names ends with "a"."""
    print('Students whose names end with "a":')
    for student in student_list:
        first_name = student['name'].split()[0]
        if first_name.endswith('a'):
            print(f"Student ID: {student['id']}, Name: {student['name']}")

    
def main():
    """Main program to handle user input."""
    file_path = 'students.json'
    student_list = load_students(file_path)
    
    while True:
        choicevalue = menu()
        
        if choicevalue == '1':
            print_students_by_age(student_list)
        elif choicevalue == '2':
            print_students_by_course(student_list)
        elif choicevalue == '3':
            print_students_name(student_list)
        elif choicevalue == '0':
            print("See you again!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
