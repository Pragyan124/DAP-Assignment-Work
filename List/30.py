first_list = [3, 1, 4, 2]
second_list = ['apple', 'orange', 'banana', 'grape']

sorted_result = [x for _, x in sorted(zip(first_list, second_list))]

print("Original lists:")
print("First list:", first_list)
print("Second list:", second_list)
print("Sorted values of the first list using the second list:", sorted_result)