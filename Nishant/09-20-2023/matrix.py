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

print("Matrix_A = ")        # 2D array print
i = 0
while i < row_A:
    j = 0
    while j < column_A:
        print(matrix_A[i][j], end="\t")
        j = j + 1
    print()
    i = i + 1
