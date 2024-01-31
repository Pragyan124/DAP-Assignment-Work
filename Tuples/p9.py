#Remove Tuples of Length K

def remove_tuples_of_length_k(tuples_list, k):
    return [tpl for tpl in tuples_list if len(tpl) != k]

# Example
my_tuples = [(1, 2), (3, 4, 5), (6, 7), (8,)]
k_value = 2
result = remove_tuples_of_length_k(my_tuples, k_value)
print(result)
