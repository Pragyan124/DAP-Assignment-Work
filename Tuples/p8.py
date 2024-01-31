#All pair combinations of 2 tuples

def all_pair_combinations(tuple1, tuple2):
    return [(x, y) for x in tuple1 for y in tuple2]

# Example
tuple1 = (1, 2)
tuple2 = ('a', 'b')
result = all_pair_combinations(tuple1, tuple2)
print(result)
