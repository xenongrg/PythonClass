matrix_A = []

row_A = int(input("Enter row value of matrix_A: "))
column_A = int(input("Enter column value of matrix_A: "))

print(f'Enter the {row_A}x{column_A} matrix_A element:')    # 2D array input
i = 0
while i < row_A:
    j = 0
    temp_matrix = []
    while j < column_A:
        temp_matrix.append(int(input()))
        j = j + 1
    matrix_A.append(temp_matrix)
    i = i + 1

matrix_B = []

row_B = int(input("Enter row value of matrix_B: "))
column_B = int(input("Enter column value of matrix_B: "))

print(f'Enter the {row_B}x{column_B} matrix_B element:')    # 2D array input
i = 0
while i < row_B:
    j = 0
    temp_matrix = []
    while j < column_B:
        temp_matrix.append(int(input()))
        j = j + 1
    matrix_B.append(temp_matrix)
    i = i + 1

print("Matrix_A = ")        # 2D array print
i = 0
while i < row_A:
    j = 0
    while j < column_A:
        print(matrix_A[i][j], end="\t")
        j = j + 1
    print()
    i = i + 1

print("Matrix_B = ")        # 2D array print
i = 0
while i < row_B:
    j = 0
    while j < column_B:
        print(matrix_B[i][j], end="\t")
        j = j + 1
    print()
    i = i + 1

if column_A != row_B:
    print("Provided matrix can't be multiplied as the column of 1st matrix and row of 2nd matrix are different.")
else:
    result = [[0 for _ in range(column_B)] for _ in range(row_A)]
    for i in range(row_A):
        for j in range(column_B):
            for k in range(row_B):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    print("Multiplication of two matrix")
    for row in result:
        for element in row:
            print(element, end="\t")
        print()
