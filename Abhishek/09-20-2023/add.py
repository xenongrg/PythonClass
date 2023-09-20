matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
# Get the dimensions of the matrices
rows = len(matrix_A)
cols = len(matrix_A[0])
# Initialize loop control variables
i = 0
while i < rows:
    j = 0
    while j < cols:
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]
        j += 1
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