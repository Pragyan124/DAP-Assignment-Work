my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elements_to_remove = [2, 4, 6, 8]
updated_list = [elem for elem in my_list if elem not in elements_to_remove]
print("Updated list after removing elements:", updated_list)