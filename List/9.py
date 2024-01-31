def find_smallest_number(lst):
    if not lst:
        return "List is empty"
    else:
        return min(lst)

my_list = [5, 2, 8, 1, 7]
smallest_number = find_smallest_number(my_list)
print(f"The smallest number in the list is: {smallest_number}")