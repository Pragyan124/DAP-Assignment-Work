def rotate_string(input_string, rotation_count):
    n = len(input_string)
    rotation_count = rotation_count % n
    rotated_string = input_string[rotation_count:] + input_string[:rotation_count]
    return rotated_string

def main():
    input_string = input("Enter a string: ")
    rotation_count = int(input("Enter a number: "))
    rotated_string = rotate_string(input_string, rotation_count)
    print(rotated_string)

if __name__ == '__main__':
    main()
