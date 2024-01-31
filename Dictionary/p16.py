#Print anagrams together in Python using List and Dictionary

from collections import defaultdict

def print_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    for key, anagrams in anagram_dict.items():
        print(f'Anagrams of {key}: {anagrams}')

# Example
word_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print_anagrams(word_list)
