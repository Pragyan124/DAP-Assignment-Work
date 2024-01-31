def replace_substring(original_string, target_substring, replacement):
    return original_string.replace(target_substring, replacement)

def main():
    original_string = input("Enter a string: ")
    target_substring = input("Enter a substring: ")
    replacement = input("Enter a replacement: ")
    
    new_string = replace_substring(original_string, target_substring, replacement)
    print(new_string)

if __name__ == "__main__":
    main()
