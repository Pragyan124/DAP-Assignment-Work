def interchange_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

original_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_and_last(original_list)
print(f"Original List: {original_list}")
print(f"Interchanged List: {interchanged_list}")