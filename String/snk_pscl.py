def snake_to_pascal(snake_case_string):
    return snake_case_string.title().replace("_", "")

def main():
    input_string = input("Enter a snake_case string: ")
    pascal_case_result = snake_to_pascal(input_string)
    print(f"PascalCase: {pascal_case_result}")

if __name__ == "__main__":
    main()
