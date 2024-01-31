def find_uncommon_words(input_str1, input_str2):
    words1 = input_str1.split()
    words2 = input_str2.split()
    set1 = set(words1)
    set2 = set(words2)
    uncommon_words = set1.symmetric_difference(set2)
    return uncommon_words

def main():
    input_str1 = input("Enter the first string: ")
    input_str2 = input("Enter the second string: ")
    uncommon_words = find_uncommon_words(input_str1, input_str2)
    print("Uncommon words:", uncommon_words)

if __name__ == "__main__":
    main()
