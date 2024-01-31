#Python – Maximum and Minimum K elements in Tuple


def max_min_k_elements(input_tuple, k):
    sorted_tuple = sorted(input_tuple)
    max_k_elements = sorted_tuple[-k:]
    min_k_elements = sorted_tuple[:k]
    return max_k_elements, min_k_elements

# Example
my_tuple = (5, 2, 8, 1, 3, 7)
k_value = 3
result_max, result_min = max_min_k_elements(my_tuple, k_value)
print(result_max, result_min)
