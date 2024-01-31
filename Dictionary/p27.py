#Python – Keys associated with Values in Dictionary

def keys_associated_with_value(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]

# Example
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
value_to_find = 1
result = keys_associated_with_value(my_dict, value_to_find)
print(result)
