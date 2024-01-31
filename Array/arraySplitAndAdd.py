def split_and_add(arr):
    return arr[len(arr)//2:] + arr[:len(arr)//2] if arr else arr

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

    result = split_and_add(arr)
    print("Rotated array is:", result)

if __name__ == '__main__':
    main()
