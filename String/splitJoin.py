def split_and_join(input_string):
    words = input_string.split()
    joined_string = " -SPLIT- ".join(words)
    return joined_string

def main():
    input_string = input("Enter a string: ")
    result = split_and_join(input_string)
    print(result)

if __name__ == "__main__":
    main()
