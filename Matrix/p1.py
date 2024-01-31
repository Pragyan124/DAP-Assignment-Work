def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for addition."
    
    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result_matrix

def subtract_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for subtraction."
    
    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result_matrix

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Adding matrices
sum_result = add_matrices(matrix1, matrix2)

# Subtracting matrices
difference_result = subtract_matrices(matrix1, matrix2)

# Displaying results
if isinstance(sum_result, str):
    print("Error in addition:", sum_result)
else:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nSum of Matrices:")
    for row in sum_result:
        print(row)

if isinstance(difference_result, str):
    print("\nError in subtraction:", difference_result)
else:
    print("\nDifference of Matrices:")
    for row in difference_result:
        print(row)
