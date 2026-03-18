def create_matrix(rows, cols):
    list_of_lists = []
    templist = []
    input_string = ""
    for i in range(rows):
        while True:
            input_string = input(f"Give row {i+1}:\n")
            templist = input_string.split(" ")
            if len(templist) == cols:
                for j in range(len(templist)):
                    templist[j] = int(templist[j])
                list_of_lists.append(templist)
                break
            else:
                print("Error: Invalid number of elements in the row. Please try again.")
    return list_of_lists

rows = int(input("Enter the number of rows:\n"))
cols = int(input("Enter the number of columns:\n"))
def print_matrix(matrix):
    for row in matrix:
        print("|", end="")
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i], end="")
            else:
                print(row[i], end="\t")
        print("|")
matrix = create_matrix(rows, cols)
print_matrix(matrix)
