#Ways to sort list of dictionaries by values in Python – Using lambda function

def sort_by_values_lambda(dictionary_list, key):
    return sorted(dictionary_list, key=lambda x: x[key])

my_list = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 30}]
key_to_sort = 'age'
result = sort_by_values_lambda(my_list, key_to_sort)
print(result)
