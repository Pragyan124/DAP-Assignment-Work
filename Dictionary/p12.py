#Sort Python Dictionaries by Key or Value

def sort_dict(dictionary, by_key=True):
    return dict(sorted(dictionary.items(), key=lambda x: x[0 if by_key else 1]))

# Example
my_dict = {'b': 2, 'a': 1, 'c': 3}
result = sort_dict(my_dict, by_key=True)
print(result)
