#Python program to Order Tuples using external List

def order_tuples_using_external_list(tuples_list, order_list):
    return sorted(tuples_list, key=lambda x: order_list.index(x[0]))

# Example
my_tuples = [('b', 2), ('a', 1), ('c', 3)]
order_list = ['a', 'b', 'c']
result = order_tuples_using_external_list(my_tuples, order_list)
print(result)
