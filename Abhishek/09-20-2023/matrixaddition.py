# making empty array to store elements of matrix
matrix_A = []
matrix_B = []

# inputting rows and columns for matrix_A
row_A = int(input("Enter row value of matrix_A: "))
column_A = int(input("Enter column value of matrix_A: "))

# inputting elements of matrix_A
print(f'Enter the {row_A}x{column_A} matrix_A element:')    # 2D array input

# loop for making matrix_A
i = 0
while i < row_A:
    j = 0
    temp_matrix = []    # temporary variable of matrix for storing elements
    while j < column_A:
        temp_matrix.append(int(input()))    # append function to input array
        j = j + 1
    matrix_A.append(temp_matrix)  # using append again to put the value in matrix_A
    i = i + 1

# inputting rows and columns for matrix_B
row_B = int(input("Enter row value of matrix_B: "))
column_B = int(input("Enter column value of matrix_B: "))

# inputting elements of matrix_B
print(f'Enter the {row_B}x{column_B} matrix_B element:')    # 2D array input
# loop for making matrix_B
i = 0
while i < row_B:
    j = 0
    temp_matrix = []       # temporary variable of matrix for storing elements
    while j < column_B:
        temp_matrix.append(int(input()))       # append function to input array
        j = j + 1
    matrix_B.append(temp_matrix)   # using append again to put the value in matrix_A
    i = i + 1

# printing matrix_A
print("Matrix_A = ")        # 2D array print
# loop for printing matrix_A
i = 0
while i < row_A:
    j = 0
    while j < column_A:
        print(matrix_A[i][j], end="\t")     # printing the matrix_A
        j = j + 1
    print()
    i = i + 1

# printing matrix_B
print("Matrix_B = ")        # 2D array print
# loop for printing matrix_B
i = 0
while i < row_B:
    j = 0
    while j < column_B:
        print(matrix_B[i][j], end="\t")     # printing the matrix_B
        j = j + 1
    print()
    i = i + 1

# addition of matrix_A & matrix_B
sum_AB = [[0 for _ in range(column_A)] for _ in range(row_A)]
# if column_A == row_B:
i = 0
while i < len(matrix_A):
    j = 0
    while j < len(matrix_A[0]):
        sum_AB[i][j] = matrix_A[i][j] + matrix_B[i][j]
        j = j + 1
    i = i + 1

print("Sum of Matrix A & B: ")
i = 0
while i < row_A:
    j = 0
    while j < column_A:
        print(sum_AB[i][j], end="\t")
        j = j + 1
    print()
    i = i + 1

# else:
#     print("The sizes of the matrix doesn't match to perform addition.")


