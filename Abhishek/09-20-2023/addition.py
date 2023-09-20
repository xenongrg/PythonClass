matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
i = 0
while i < 2:
        j = 0
        temp_matrix =[]
        while j < 2:
            temp_matrix = matrix_A[i][j] + matrix_B[i][j]
            j = j + 1
            print(temp_matrix, end="\t")
        i = i + 1
