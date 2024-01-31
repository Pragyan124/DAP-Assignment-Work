#Possible Words using given characters in Python

from collections import Counter

def possible_words(characters, dictionary):
    char_count = Counter(characters)
    possible_words_list = [word for word in dictionary if Counter(word) & char_count == Counter(word)]
    return possible_words_list

# Example
char_input = 'abc'
word_dict = ['abc', 'cab', 'def', 'fed']
result = possible_words(char_input, word_dict)
print(result)
