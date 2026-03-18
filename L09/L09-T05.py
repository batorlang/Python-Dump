#Task five
def access_matrix_value(matrix):
    try:
        row = int(input("Enter the row index:\n"))
        column = int(input("Enter the column index:\n"))

        value = matrix[row][column]
        print(f"Value at position ({row}, {column}): {value}")
    
    except IndexError:
        print("Error: Index out of bounds. Please enter valid row and column indices.")
    
    except ValueError:
        print("Error: Please enter valid integers for row and column indices.")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

access_matrix_value(matrix)
