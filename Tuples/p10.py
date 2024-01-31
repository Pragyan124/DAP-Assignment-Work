#Sort a list of tuples by the second Item

def sort_tuples_by_second_item(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# Example
my_tuples = [(3, 8), (1, 4), (2, 6), (4, 2)]
result = sort_tuples_by_second_item(my_tuples)
print(result)
