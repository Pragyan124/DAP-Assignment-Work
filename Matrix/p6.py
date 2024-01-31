# Function to vertically concatenate two matrices
def vertical_concatenation(matrix1, matrix2):
    return matrix1 + matrix2

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

result_matrix = vertical_concatenation(matrix1, matrix2)

# Display the original matrices and the result
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nVertical Concatenation:")
for row in result_matrix:
    print(row)
