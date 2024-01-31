def find_largest(arr):
    return max(arr)

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

    result = find_largest(arr)
    print("Largest element in the array is:", result)

if __name__ == '__main__':
    main()
