def rotate_matrix(matrix):
    row_num = len(matrix)
    col_num = len(matrix[0])
    result = []
    for i in range(col_num):
        result.append([None]*row_num)
    print(result)
    for i in range(row_num):
        for j in range(col_num):
            col = row_num -1 - i
            row = j
            result[row][col] = matrix[i][j]
    print(result)

import math
def rotate_matrix_inplace(matrix):
    n = len(matrix)
    for layer in range(math.floor(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    print(matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8,9]]
rotate_matrix_inplace(matrix)