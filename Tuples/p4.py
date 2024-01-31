#Adding Tuple to List and vice – versa

def add_tuple_to_list(input_list, input_tuple):
    input_list.append(input_tuple)
    return input_list

# Example
my_list = [(1, 2), (3, 4)]
my_tuple = (5, 6)
result = add_tuple_to_list(my_list, my_tuple)
print(result)
