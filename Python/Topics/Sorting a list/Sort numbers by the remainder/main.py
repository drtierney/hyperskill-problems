nums = [int(num) for num in list(input())]

# write your code here
print(sorted(nums, key=lambda x: x % 3))
