# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [1 if num >= 1 else 0 for num in old_list]
print(binary_list)
