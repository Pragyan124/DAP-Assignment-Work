
#Python dictionary, set, and counter to check if frequencies can become the same


from collections import Counter

def can_freq_become_same(input_list):
    freq_counter = Counter(input_list)
    unique_freqs = set(freq_counter.values())

    return len(unique_freqs) <= 1

# Example
my_list = [1, 2, 2, 3, 3, 3]
result = can_freq_become_same(my_list)
print(result)
