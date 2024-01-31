def find_remainder(arr, n):
    product_mod_n = 1
    for i in arr:
        product_mod_n = (product_mod_n * (i % n)) % n
    return product_mod_n

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    result = find_remainder(arr, n)
    print("Remainder of the array is:", result)

if __name__ == '__main__':
    main()
