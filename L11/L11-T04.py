import numpy as np

print("This program demonstrates use of numpy-matrix.")
def create_matrix():
    rows = int(input("Enter amount of rows:\n"))
    columns = int(input("Enter number of columns:\n"))
    zero_array = np.zeros((rows, columns), dtype=int)
    matrix = zero_array
    print(f"Zero-matrix of the given rows & columns is:\n {matrix}")
    for row in range(rows):
        for column in range(columns):
            matrix[row, column] = (row + 1) * (column + 1)
    print("Matrix printed with np-formatting:")
    print(matrix)
    print("\nMatrix sorted into one array:")
    matrix2 = np.sort(matrix.flatten())
    print(matrix2)

    print("Matrix printed with elements separated by semicolons:")
    print_string = ""
    for i in matrix:
        row_string = ""
        for j in i:
            row_string += str(j) + ";"
        print_string += row_string + "\n"
    print(print_string)
    return matrix

matrix_next = create_matrix()


def reshape():
    while True:
        print("Shaping the matrix. Please, enter the new dimensions.")
        new_rows = int(input("Enter amount of new rows:\n"))
        new_columns = int(input("Enter amount of new columns:\n"))
        try:
            reshaped_matrix = matrix_next.reshape(new_rows, new_columns)
            print(f"Newly shaped matrix is:\n {reshaped_matrix}")
            max_value = np.max(matrix_next)
            min_value = np.min(matrix_next)
            sum_value = np.sum(matrix_next)
            print(f"""Largest number in the matrix is: {max_value}
Smallest number in the matrix is: {min_value}
Sum of all values in the matrix is: {sum_value}""")
            break
        except ValueError:
            print("Faulty shape. Please, try again.")

def list_thing():
    list_values = [int(item) for item in input("Enter the list items:\n").split()]
    unique = np.unique(list_values)
    print(f"Unique values are: {unique}")
    return None
reshape()
list_thing()
