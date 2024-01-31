my_list = [1, 2, 3, 4, 5]

cumulative_sum = [sum(my_list[:i+1]) for i in range(len(my_list))]

print("Original list:", my_list)
print("Cumulative sum list:", cumulative_sum)