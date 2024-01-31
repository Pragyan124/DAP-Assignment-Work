
#Python Dictionary to find mirror characters in a string


def find_mirror_chars(input_str):
    mirror_dict = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b'}

    mirrored_str = ''
    for char in reversed(input_str):
        mirrored_str += mirror_dict.get(char, char)

    return mirrored_str

# Example
input_string = 'bdpqpbd'
result = find_mirror_chars(input_string)
print(result)
