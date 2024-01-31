#Closest Pair to Kth index element in Tuple


def closest_pair_to_kth_index(input_tuple, k):
    sorted_tuples = sorted(input_tuple, key=lambda x: abs(x[0] - k))
    return sorted_tuples[0]

# Example
my_tuple = [(1, 2), (3, 4), (5, 6), (7, 8)]
k_value = 5
result = closest_pair_to_kth_index(my_tuple, k_value)
print(result)
