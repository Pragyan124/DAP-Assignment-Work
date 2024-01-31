def word_freq(input_string):
    words = input_string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def main():
    input_string = input("Enter a string: ")
    frequency = word_freq(input_string)
    for word, count in frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
