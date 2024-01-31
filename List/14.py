def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    print(f"The odd numbers in the list are: {odd_numbers}")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_numbers(my_list)