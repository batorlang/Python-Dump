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

def print_matrix(matrix):
    for row in matrix:
        print("|", end="")
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i], end="")
            else:
                print(row[i], end="\t")
        print("|")

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    trans_matrix = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(0)
        trans_matrix.append(new_row)
    for i in range(rows):
        for j in range(cols):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix

rows = int(input("Enter the number of rows:\n"))
cols = int(input("Enter the number of columns:\n"))
matrix = create_matrix(rows, cols)
print("The original matrix:")
print_matrix(matrix)
transposed = transpose(matrix)
print("Its transpose:")
print_matrix(transposed)
