#Python dictionary with keys having multiple inputs


from collections import defaultdict

def create_multikey_dict(keys_values_list):
    multikey_dict = defaultdict(list)
    for keys, value in keys_values_list:
        for key in keys:
            multikey_dict[key].append(value)
    return dict(multikey_dict)

# Example
keys_values_list = [(['a', 'b'], 1), (['b', 'c'], 2), (['a', 'c'], 3)]
result = create_multikey_dict(keys_values_list)
print(result)
