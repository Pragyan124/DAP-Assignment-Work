def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

result = list(chunks(my_list, chunk_size))

print(f"Original list: {my_list}")
print(f"List broken into chunks of size {chunk_size}: {result}")