#K’th Non-repeating Character in Python using List Comprehension and OrderedDict

from collections import OrderedDict, Counter

def kth_non_repeating_char(string, k):
    count_dict = OrderedDict(Counter(string))
    non_repeating_chars = [char for char, count in count_dict.items() if count == 1]

    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k-1]
    else:
        return None

# Example
input_str = 'geeksforgeeks'
k_value = 3
result = kth_non_repeating_char(input_str, k_value)
print(result)
