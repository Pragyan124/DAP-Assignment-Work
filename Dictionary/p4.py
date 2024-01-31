#Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter

def sort_by_values(dictionary_list, key):
    return sorted(dictionary_list, key=itemgetter(key))


my_list = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 30}]
key_to_sort = 'age'
result = sort_by_values(my_list, key_to_sort)
print(result)
