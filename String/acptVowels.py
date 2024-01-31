def contains_all_vowels(string):
    vowels = set('aeiou')
    return set(string.lower()) >= vowels

def main():
    input_string = input("Enter a string: ")
    if contains_all_vowels(input_string):
        print("The string contains all vowels.")
    else:
        print("The string does not contain all vowels.")

if __name__ == "__main__":
    main()
