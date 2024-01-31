#Sort Dictionary key and values List


def sort_dict_list(dictionary):
    return {k: sorted(v) for k, v in dictionary.items()}

# Example
my_dict = {'b': [2, 1, 3], 'a': [4, 2, 1], 'c': [3, 1, 2]}
result = sort_dict_list(my_dict)
print(result)
