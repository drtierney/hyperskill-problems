# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
groups_dict = dict.fromkeys(groups)

group_count = int(input())
for i in range(group_count):
    children_count = int(input())
    groups_dict[groups[i]] = children_count

print(groups_dict)
