#Handling missing keys in Python dictionaries

def handle_missing_keys(dictionary, key, default_value=None):
    return dictionary.get(key, default_value)

# Example
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'd'
result = handle_missing_keys(my_dict, key_to_check, default_value=-1)
print(result)
