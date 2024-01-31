def find_n_largest_elements(lst, n):
    if len(lst) < n:
        return f"List has fewer than {n} elements"
    else:
        sorted_list = sorted(set(lst), reverse=True)
        return sorted_list[:n]

my_list = [5, 2, 8, 1, 7, 8, 3]
n = 3
n_largest_elements = find_n_largest_elements(my_list, n)
print(f"The {n} largest elements in the list are: {n_largest_elements}")