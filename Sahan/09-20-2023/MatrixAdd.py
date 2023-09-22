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

result = [[0 for _ in range(column_B)] for _ in range(row_A)]
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]

print("Addition of two matrix")
for row in result:
    for element in row:
        print(element, end="\t")
    print()
