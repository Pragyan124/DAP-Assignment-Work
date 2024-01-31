#Counting the frequencies in a list using dictionary in Python


def count_frequencies(input_list):
    freq_dict = {}
    for item in input_list:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

# Example
my_list = ['a', 'b', 'a', 'c', 'b', 'a']
result = count_frequencies(my_list)
print(result)
