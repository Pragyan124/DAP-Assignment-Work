from collections import Counter

def least_freq(string):
    counter = Counter(string)
    least_frequent_count = min(counter.values())
    least_frequent_chars = [char for char, count in counter.items() if count == least_frequent_count]
    return least_frequent_chars

def main():
    input_string = input("Enter a string: ")
    least_frequent = least_freq(input_string)
    
    if least_frequent:
        print(f"The least frequent character(s) in '{input_string}' is/are: {', '.join(least_frequent)}")
    else:
        print("No characters found in the string.")

if __name__ == "__main__":
    main()
