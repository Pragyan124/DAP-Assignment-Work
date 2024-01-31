#Append Dictionary Keys and Values (In order) in dictionary

def append_keys_values(dict1, dict2):
    result_dict = {}
    for key in dict1:
        result_dict[key] = dict1[key] + dict2[key]
    return result_dict

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'c': 6}
result = append_keys_values(dict1, dict2)
print(result)



