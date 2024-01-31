def find_largest_number(lst):
    if not lst:
        return "List is empty"
    else:
        return max(lst)

my_list = [5, 2, 8, 1, 7]
largest_number = find_largest_number(my_list)
print(f"The largest number in the list is: {largest_number}")