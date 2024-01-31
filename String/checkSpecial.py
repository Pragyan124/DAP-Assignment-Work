import re

def check_special(string):
    return bool(re.search(r'[^a-zA-Z0-9\s]', string))

def main():
    string = input("Enter a string: ")
    if check_special(string):
        print("The string contains special characters.")
    else:
        print("The string does not contain special characters.")

if __name__ == "__main__":
    main()
