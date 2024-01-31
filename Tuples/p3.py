#Create a list of tuples from a given list having a number and its cube in each tuple

def create_cubed_tuples(input_list):
    return [(num, num**3) for num in input_list]

# Example
my_list = [1, 2, 3, 4, 5]
result = create_cubed_tuples(my_list)
print(result)
