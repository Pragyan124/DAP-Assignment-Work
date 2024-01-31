#Insertion at the beginning in OrderedDict

from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    ordered_dict.update({key: value})
    ordered_dict.move_to_end(key, last=False)
    return ordered_dict

# Example
my_dict = OrderedDict([('b', 2), ('c', 3)])
key_to_insert = 'a'
value_to_insert = 1
result = insert_at_beginning(my_dict, key_to_insert, value_to_insert)
print(result)
