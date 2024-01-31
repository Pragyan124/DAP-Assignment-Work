def find_words_greater_than_length(input_string, k):
    words = input_string.split()
    result = [word for word in words if len(word) > k]
    return result

def main():
    input_string = input("Enter a string: ")
    k = int(input("Enter a number: "))
    result = find_words_greater_than_length(input_string, k)
    
    if result:
        print("Words greater than length {}: {}".format(k, result))
    else:
        print("No words found greater than length {}.".format(k))

if __name__ == '__main__':
    main()
