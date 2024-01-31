#Remove all duplicates words from a given sentence

def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = set(words)
    return ' '.join(unique_words)

# Example
input_sentence = 'hello world world is beautiful'
result = remove_duplicates(input_sentence)
print(result)
