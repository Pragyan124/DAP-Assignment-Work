def rotate_array(arr):
    return [arr[-1]] + arr[:-1] if arr else arr

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

    result = rotate_array(arr)
    print("Rotated array is:", result)

if __name__ == '__main__':
    main()
