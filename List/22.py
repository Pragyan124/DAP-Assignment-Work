my_list = [1, [], 3, [], 5, [], 7]
updated_list = [sublist for sublist in my_list if sublist]
print("Updated list after removing empty lists:", updated_list)