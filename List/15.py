def print_even_numbers_in_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print(f"The even numbers in the range [{start}, {end}] are: {even_numbers}")

start_range = 1
end_range = 10
print_even_numbers_in_range(start_range, end_range)