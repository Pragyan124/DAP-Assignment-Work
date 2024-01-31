def reverse_words(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

def main():
    input_string = input("Enter a string: ")
    print(reverse_words(input_string))

if __name__ == "__main__":
    main()

