#Python program to find the sum of all items in a dictionary

def sum_of_items(dictionary):
    return sum(dictionary.values())


my_dict = {'a': 10, 'b': 20, 'c': 30}
result = sum_of_items(my_dict)
print(result)
