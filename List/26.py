my_list = [1, 2, 3, 2, 4, 5, 6, 1]

duplicates = set()
seen = set()

print("Duplicates in the list are:")
for num in my_list:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))