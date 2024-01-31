#Extract digits from Tuple list

def extract_digits_from_tuples(tuples_list):
    digits = [digit for tpl in tuples_list for digit in str(tpl[1])]
    return list(map(int, digits))

# Example
my_tuples = [(10, 123), (20, 456), (30, 789)]
result = extract_digits_from_tuples(my_tuples)
print(result)
