# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposed matrix in a single line
transposed_matrix = [list(row) for row in zip(*matrix)]

# Display the original and transposed matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
