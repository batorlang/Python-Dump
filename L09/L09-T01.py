#Task one
def input_integer():
    try:
        user_int = int(input("Enter an integer:\n"))
        return user_int
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None
def main():
    times = input_integer()
    print(f"Now give {times} integers!")
    while times is None:
        print("Invalid input. Please enter an integer.")
        times = input_integer()
    total_sum = 0
    for i in range(times):
        number = input_integer()
        while number is None:
            number = input_integer()
        total_sum += number
    print(f"The sum of the entered integers is: {total_sum}")
main()
