from collections import Counter

def max_freq(string):
    counter = Counter(string)
    max_frequent_count = max(counter.values())
    max_frequent_chars = [char for char, count in counter.items() if count == max_frequent_count]
    return max_frequent_chars

def main():
    input_string = input("Enter a string: ")
    max_frequent = max_freq(input_string)
    
    if max_frequent:
        print(f"The most frequent character(s) in '{input_string}' is/are: {', '.join(max_frequent)}")
    else:
        print("No characters found in the string.")

if __name__ == "__main__":
    main()
