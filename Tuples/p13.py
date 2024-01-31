#Convert Nested Tuple to Custom Key Dictionary


def convert_nested_tuple_to_dict(nested_tuple):
    return {tpl[0]: tpl[1] for tpl in nested_tuple}

# Example
my_nested_tuple = (('a', 1), ('b', 2), ('c', 3))
result = convert_nested_tuple_to_dict(my_nested_tuple)
print(result)
