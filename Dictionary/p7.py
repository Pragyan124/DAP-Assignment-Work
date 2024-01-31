
#Convert key-values list to flat dictionary
def list_to_dict(key_value_list):
    return dict(key_value_list)


key_value_list = [('a', 1), ('b', 2), ('c', 3)]
result = list_to_dict(key_value_list)
print(result)
