#Ways to remove a key from dictionary

def remove_key(dictionary, key_to_remove):
    dictionary.pop(key_to_remove, None)
    return dictionary


my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
result = remove_key(my_dict, key_to_remove)
print(result)