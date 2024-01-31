my_list = [(1, 2), (), (3, 4), (), (), (5, 6)]

filtered_list = [tpl for tpl in my_list if tpl]

print("Updated list after removing empty tuples:", filtered_list)