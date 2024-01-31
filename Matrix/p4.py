# Function to create an n x n matrix
def create_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

# Example usage
n = int(input("Enter the value of n: "))
matrix = create_matrix(n)

# Display the created matrix
print(f"\n{n} x {n} Matrix:")
for row in matrix:
    print(row)
