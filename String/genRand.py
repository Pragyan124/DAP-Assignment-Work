import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_until_match(target_string):
    attempts = 0
    while True:
        generated_string = generate_random_string(len(target_string))
        attempts += 1
        print(f"Attempt {attempts}: {generated_string}")
        if generated_string == target_string:
            print(f"Match found after {attempts} attempts.")
            break

def main():
    target_string = input("Enter the target string: ")
    generate_until_match(target_string)

if __name__ == "__main__":
    main()
