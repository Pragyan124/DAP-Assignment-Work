def replace_words_with_K(input_text, target_words):
    for word in target_words:
        input_text = input_text.replace(word, "K")
    return input_text

def main():
    input_text = input("Enter a string: ")
    input_text = input_text.lower()
    target_words = input("Enter words to replace separated by spaces: ").split()
    target_words = [word.lower() for word in target_words]
    result = replace_words_with_K(input_text, target_words)
    print(result)

if __name__ == '__main__':
    main()
