def is_monotonic(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    result = is_monotonic(arr)
    print("Is Monotonic: ", result)

if __name__ == '__main__':
    main()
