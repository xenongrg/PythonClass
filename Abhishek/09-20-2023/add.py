matrix_A = [[1, 2, 1], [3, 4, 1]]
matrix_B = [[5, 6, 1], [7, 8, 1]]
result = []
# Get the dimensions of the matrices
rows = len(matrix_A)
cols = len(matrix_A[0])
# Initialize loop control variables
i = 0
while i < rows:
    j = 0
    temp_matrix = []
    while j < cols:
        temp_matrix.append(matrix_A[i][j] + matrix_B[i][j])
        j += 1
    result.append(temp_matrix)
    i += 1
# Print the result
print("Addition of two matrices:")
i = 0
while i < rows:
    j = 0
    while j < cols:
        print(result[i][j], end="\t")
        j += 1
    print()
    i += 1