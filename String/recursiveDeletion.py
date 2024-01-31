def is_empty_string(input_string):
    if len(input_string) == 0:
        return True
    else:
        return is_empty_string(input_string[1:])

def main():
    input_string = input("Enter a string: ")
    if is_empty_string(input_string):
        print("The string can become empty by recursive deletion")
    else:
        print("The string cannot become empty by recursive deletion")

if __name__ == '__main__':
    main()
