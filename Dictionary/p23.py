
#Python counter and dictionary intersection example

from collections import Counter

def can_make_string(str1, str2):
    counter_str1 = Counter(str1)
    counter_str2 = Counter(str2)

    intersection = counter_str1 & counter_str2

    return sum((counter_str1 - intersection).values()) == 0

# Example
string1 = 'abc'
string2 = 'bac'
result = can_make_string(string1, string2)
print(result)
