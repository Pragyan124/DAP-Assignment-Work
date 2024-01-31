def calculate_sum(arr):
    return sum(arr)

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    
    result = calculate_sum(arr)
    print("Sum of the array is:", result)

if __name__ == '__main__':
    main()
