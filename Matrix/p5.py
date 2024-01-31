# Function to get the Kth column of a matrix
def get_kth_column(matrix, k):
    return [row[k] for row in matrix]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k = int(input("Enter the value of K (0-based index): "))
column = get_kth_column(matrix, k)

# Display the Kth column
print(f"\nKth Column ({k}-th column):")
for element in column:
    print(element)
