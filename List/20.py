start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Negative numbers in the range from", start_range, "to", end_range, "are:")
for num in range(start_range, end_range + 1):
    if num < 0:
        print(num)