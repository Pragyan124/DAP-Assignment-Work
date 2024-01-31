import re

def check_url(string):
    pattern = re.compile(r'^(https?://)?(www\.)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})+(\.[a-zA-Z0-9]{2,})?(/[a-zA-Z0-9]+)?(\?[a-zA-Z0-9_=&]+)?$')
    return bool(re.match(pattern, string))

def main():
    input_string = input("Enter a string: ")
    if check_url(input_string):
        print("The string is a URL.")
    else:
        print("The string is not a URL.")

if __name__ == "__main__":
    main()
