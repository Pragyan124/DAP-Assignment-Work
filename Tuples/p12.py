#Flatten tuple of List to tuple


def flatten_tuple_of_lists(tuple_of_lists):
    return tuple(item for sublist in tuple_of_lists for item in sublist)

# Example
my_tuple = ([1, 2], ['a', 'b'], [3, 4])
result = flatten_tuple_of_lists(my_tuple)
print(result)
