numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

print("Negative numbers in the list are:")
for num in numbers:
    if num < 0:
        print(num)