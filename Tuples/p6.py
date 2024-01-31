#Join Tuples if similar initial element

def join_tuples_with_similar_initial(tuples_list):
    result = []
    current_tuple = None

    for tpl in sorted(tuples_list):
        if current_tuple and tpl[0] == current_tuple[0]:
            current_tuple = (current_tuple[0], current_tuple[1] + tpl[1])
        else:
            if current_tuple:
                result.append(current_tuple)
            current_tuple = tpl

    if current_tuple:
        result.append(current_tuple)

    return result

# Example
my_tuples = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]
result = join_tuples_with_similar_initial(my_tuples)
print(result)
