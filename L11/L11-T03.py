import numpy as np

while True:
    rows1 = int(input("Enter the number of rows for the first matrix:\n"))
    cols1 = int(input("Enter the number of columns for the first matrix:\n"))
    break
print(f"Enter values for a {rows1}x{cols1} matrix:")
matrix1 = []
for i in range(rows1):
    while True:
        row1 = input(f"Enter {cols1} values for row {i + 1} (separated by space):\n").strip().split()
        if len(row1) != cols1:
            print(f"Row must have {cols1} values. Try again.")
            continue
        row1_values = []
        for value in row1:
            row1_values.append(float(value))
        matrix1.append(row1_values)
        break
complete_matrix1 = np.array(matrix1)

print(f"This is matrix 1:\n{complete_matrix1}")



while True:
    rows2 = int(input("Enter the number of rows for the second matrix:\n"))
    cols2 = int(input("Enter the number of columns for the second matrix:\n"))
    break
print(f"Enter values for a {rows2}x{cols2} matrix:")
matrix2 = []
for i in range(rows2):
    while True:
        row2 = input(f"Enter {cols2} values for row {i + 1} (separated by space):\n").strip().split()
        if len(row2) != cols2:
            print(f"Row must have {cols2} values. Try again.")
            continue
        row2_values = []
        for value in row2:
            row2_values.append(float(value))
        matrix2.append(row2_values)
        break
complete_matrix2 = np.array(matrix2)


print(f"This is matrix 2:\n{complete_matrix2}")
try:
    print_sum = complete_matrix1 + complete_matrix2
    print("Matrix sum:")
    print(print_sum)
except ValueError:
    print("Error: sum not possible")
try:
    print_mult = complete_matrix1 @ complete_matrix2
    print("Matrix multiplication:")
    print(print_mult)
except ValueError:
    print("Error: multiplication not possible")
