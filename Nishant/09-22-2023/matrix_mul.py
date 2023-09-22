matrix_A = [[1, 2, 1], [3, 4, 1]]
matrix_B = [[4, 3], [2, 1], [1, 1]]
result = []

row_A = len(matrix_A)
col_A = len(matrix_A[0])

row_B = len(matrix_B)
col_B = len(matrix_B[0])

print()
i = 0
while i < row_A:
    j = 0
    while j < col_A:
        print(matrix_A[i][j], end="\t")
        j += 1
    print()
    i += 1

print()
i = 0
while i < row_B:
    j = 0
    while j < col_B:
        print(matrix_B[i][j], end="\t")
        j += 1
    print()
    i += 1

i = 0
while i < row_A:
    j = 0
    temp_matrix = []
    while j < col_B:
        k = 0
        summation = 0
        while k < col_A:
            summation = summation + matrix_A[i][k] * matrix_B[k][j]
            k = k + 1
        temp_matrix.append(summation)
        j = j + 1
    result.append(temp_matrix)
    i = i + 1

print()
i = 0
while i < len(result):
    j = 0
    while j < len(result[0]):
        print(result[i][j], end="\t")
        j += 1
    print()
    i += 1
