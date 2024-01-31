def check_substring(string, substring):
    return substring in string

def main():
    input_string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    
    if check_substring(input_string, substring):
        print(f"The substring '{substring}' is in the string '{input_string}'.")
    else:
        print(f"The substring '{substring}' is not in the string '{input_string}'.")

if __name__ == "__main__":
    main()
