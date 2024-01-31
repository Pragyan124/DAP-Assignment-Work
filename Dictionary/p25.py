
#Scraping And Finding Ordered Words In A Dictionary using Python

def find_ordered_words(dictionary, prefix):
    ordered_words = [word for word in dictionary if word.startswith(prefix)]
    return ordered_words

# Example
word_dict = {'apple': 1, 'appetizer': 2, 'apricot': 3, 'banana': 4}
prefix_to_search = 'app'
result = find_ordered_words(word_dict, prefix_to_search)
print(result)
