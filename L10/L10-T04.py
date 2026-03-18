import json




def print_students_by_age(student_list):
    ages = sorted({student["age"] for student in student_list})[1:]
    print("Select the ages of the students:")
    for i, age in enumerate(ages, 1):
        print(f"{i}) {age}")

    try:
        selected_age = int(input("Enter your selection:\n"))
        if 1 <= selected_age <= len(ages):
            selected_age = ages[selected_age - 1]
            for student in student_list:
                if student["age"] == selected_age:
                    print(
                        f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}"
                    )
    except ValueError:
        print("Invalid input. Please enter a number.")
    print("")


def print_students_by_course(student_list):
    all_courses = []
    for student in student_list:
        for course in student["courses"]:
            all_courses.append(course)

    courses = []
    for course in set(all_courses):
        if all_courses.count(course) >= 2:
            courses.append(course)

    print("Select the course:")
    print("1) Computer Science")
    print("2) History")
    print("3) Math")
    print("4) Art")

    selected_course = int(input("Enter your selection:\n"))
    what_courses_mean = {1: "Computer Science", 2: "History", 3: "Math", 4: "Art"}
    selected_course = what_courses_mean[selected_course]

    for student in student_list:
        if selected_course in student["courses"]:
            print(
                f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}"
            )

    print("")


def print_students_name(student_list):
    print("Students whose name end with 'a':")
    for student in student_list:
        first_name = student["name"].split()[0]
        if first_name.endswith("a"):
            print(f"Student ID: {student['id']}, Name: {student['name']}")
    print("")


def main():
    try:
        with open("students.json", "r") as file:
            students_json = json.load(file)
    except FileNotFoundError:
        print("file not found :(")
        return

    while True:
        print("What do you want to do?")
        print("1) Print students by age")
        print("2) Print students based on the course they are taking")
        print('3) Print students whose first names ends with the letter "a"')
        print("0) Stop the program")
        try:
            choice = int(input("Enter your choice:\n"))

            if choice == 0:
                print("See you again!")
                break
            elif choice == 1:
                print_students_by_age(students_json)
            elif choice == 2:
                print_students_by_course(students_json)
            elif choice == 3:
                print_students_name(students_json)
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid choice. Please try again.\n")


main()
