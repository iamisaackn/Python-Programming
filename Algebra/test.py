def matrixMultiplication(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

tMatrix = matrixMultiplication(matrix1, matrix2)
print(f"Answer: {tMatrix}")
