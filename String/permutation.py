import itertools

def generate_permutations(input_string):
    chars = list(input_string)
    permutations = itertools.permutations(chars)
    result = [''.join(perm) for perm in permutations]
    return result

def main():
    input_string = input("Enter a string: ")
    permutations = generate_permutations(input_string)
    print(permutations)

if __name__ == "__main__":
    main()
