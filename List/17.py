numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

print("Positive numbers in the list are:")
for num in numbers:
    if num > 0:
        print(num)