def digit_sum(number):
    return sum(int(digit) for digit in str(number))

my_list = [123, 45, 678, 9]

sum_of_digits = sum(digit_sum(num) for num in my_list)

print("Original list:", my_list)
print("Sum of digits in the list:", sum_of_digits)