#Task two
def reading(input_filename):
    integers = []
    counter = 0
    try:
        file1 = open(input_filename, "r")
        for line in file1:
            integers.append(int(line.strip()))
            counter += 1
        file1.close()
        print(f"File '{input_filename}' read successfully, {counter} lines.")
    except (FileNotFoundError, ValueError, IOError):
        print(f"Error processing file '{input_filename}'.")
        return None
    return integers

def writing(output_filename, integers):
    try:
        file2 = open(output_filename, "w")
        for number in integers:
            file2.write(f"{number}\n")
        file2.close()
        print(f"File '{output_filename}' was successfully written.")
    except (FileNotFoundError, ValueError, IOError):
        return False
    return True

def main():
    input_filename = input("Enter the name of the file to be read:\n")
    integers = reading(input_filename)
    if integers is None:
        return

    output_filename = input("Enter the name of the file to be written:\n")
    if not writing(output_filename, integers):
        print(f"Error processing file '{output_filename}'.")

main()
#T2_file_in2.txt
