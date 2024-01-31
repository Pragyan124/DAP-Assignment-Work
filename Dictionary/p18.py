#Check if binary representations of two numbers are anagram


def are_binary_anagrams(num1, num2):
    binary_num1 = bin(num1)[2:]
    binary_num2 = bin(num2)[2:]

    return sorted(binary_num1) == sorted(binary_num2)

# Example
number1 = 8
number2 = 4
result = are_binary_anagrams(number1, number2)
print(result)
