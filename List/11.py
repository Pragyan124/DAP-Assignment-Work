def find_second_largest(lst):
    if len(lst) < 2:
        return "List should have at least two elements"
    else:
        unique_numbers = set(lst)
        unique_numbers.remove(max(unique_numbers))
        return max(unique_numbers)

my_list = [5, 2, 8, 1, 7]
second_largest_number = find_second_largest(my_list)
print(f"The second-largest number in the list is: {second_largest_number}")