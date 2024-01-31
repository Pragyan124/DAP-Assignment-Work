def print_even_length_words(string):
    words = string.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    for word in even_length_words:
        print(word)

def main():
    input_string = input("Enter a string: ")
    print_even_length_words(input_string)

if __name__ == "__main__":
    main()

