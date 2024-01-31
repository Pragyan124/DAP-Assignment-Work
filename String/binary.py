import re

def is_binary_string(string):
    return bool(re.match(r'^[01]+$', string))

def main():
    string = input("Enter a string: ")
    if is_binary_string(string):
        print("The string is a binary string.")
    else:
        print("The string is not a binary string.")

if __name__ == "__main__":
    main()
