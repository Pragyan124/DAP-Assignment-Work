def count_matching_characters(string1, string2):
    common_characters = set(string1) & set(string2)
    return len(common_characters)

def main():
    input_string1 = input("Enter the first string: ")
    input_string2 = input("Enter the second string: ")
    
    result = count_matching_characters(input_string1, input_string2)
    print(f"{result} characters are matching.")

if __name__ == "__main__":
    main()
