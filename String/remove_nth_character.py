def remove_nth_character(input_string, index):
    return input_string[:index] + input_string[index + 1:]

def main():
    input_string = input("Enter a string: ")
    index = int(input("Enter the index of the character to remove: "))
    result = remove_nth_character(input_string, index)
    print(result)

if __name__ == '__main__':
    main()
