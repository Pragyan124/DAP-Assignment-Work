

import re

def remove_duplicates(string):
    pattern = r'(\b\w+\b)(?=.*\b\1\b)'  # PATTERN TAKEN FROM REGEX101 -_-
    replaced_string = re.sub(pattern, '', string)
    return replaced_string

def main():
    input_string = input("Enter a string: ")
    result = remove_duplicates(input_string)
    print(result)

if __name__ == "__main__":
    main()
